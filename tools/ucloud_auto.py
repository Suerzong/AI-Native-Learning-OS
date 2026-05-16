#!/usr/bin/env python
"""Fully automated UCloud task scraper with auto-login fallback.

Designed for cron / scheduled execution. No manual intervention needed.

Auth chain:
  1. Use existing cookies (token)
  2. If 401 → refresh_token
  3. If refresh fails → CAS login with stored credentials → save new cookies
  4. Scrape all pending tasks

Credentials stored in ~/.config/edge-ai/ucloud-credentials.json (mode 0600)
Cookies stored in ~/.config/edge-ai/ucloud-cookies.json (mode 0600)

Usage:
  python tools/ucloud_auto.py                         # one-shot scrape
  python tools/ucloud_auto.py --print-report          # stdout only
  python tools/ucloud_auto.py --setup                 # store credentials
"""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import requests

WORKSPACE = Path(__file__).resolve().parents[1]
TASKS_DIR = WORKSPACE / "ucloud-tasks"
CONFIG_DIR = Path.home() / ".config" / "edge-ai"
COOKIE_FILE = CONFIG_DIR / "ucloud-cookies.json"
CREDENTIAL_FILE = CONFIG_DIR / "ucloud-credentials.json"
TIMEZONE = ZoneInfo("Asia/Shanghai")

API_BASE = "https://apiucloud.bupt.edu.cn"
AUTH_BASE = "https://auth.bupt.edu.cn"
UCLASS_URL = "https://ucloud.bupt.edu.cn/uclass"
UCLASS_BASE = "https://ucloud.bupt.edu.cn/uclass/course.html#"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

TYPE_MAP = {3: "assignment", 4: "exam", 5: "survey", 6: "evaluation"}


@dataclass
class PendingTask:
    title: str
    course: str
    task_type: str
    deadline: str = ""
    status: str = "pending"
    url: str = ""
    source_endpoint: str = ""
    raw_extra: dict[str, Any] = field(default_factory=dict)


# ─── CAS Login ──────────────────────────────────────────────────────────────

def _cas_session() -> requests.Session:
    s = requests.Session()
    s.headers["User-Agent"] = USER_AGENT
    return s


def cas_login(username: str, password: str) -> dict[str, str]:
    """Full CAS login flow. Returns {token, refresh_token, identity}.

    Flow: CAS login → extract ticket → exchange ticket for token via API.
    The service URL must be https://ucloud.bupt.edu.cn/uclass (no trailing
    slash) to match what the UCloud backend uses for ticket validation.
    """
    s = _cas_session()

    # Step 1: GET login page → extract execution
    resp = s.get(f"{AUTH_BASE}/authserver/login",
                 params={"service": UCLASS_URL}, timeout=30)
    resp.raise_for_status()
    html = resp.text

    match = re.search(r'name="execution"\s+value="([^"]+)"', html)
    if not match:
        raise RuntimeError("Cannot find execution in CAS login page")
    execution = match.group(1)

    # Step 2: POST login credentials
    data = {
        "username": username,
        "password": password,
        "type": "username_password",
        "execution": execution,
        "_eventId": "submit",
    }
    resp = s.post(f"{AUTH_BASE}/authserver/login",
                  params={"service": UCLASS_URL},
                  data=data, allow_redirects=False, timeout=30)

    if resp.status_code in (401, 200):
        err_match = re.search(
            r'<div[^>]*id="errorDiv"[^>]*>\s*<p[^>]*>(.*?)</p>',
            resp.text, re.S,
        )
        if err_match:
            raise RuntimeError(f"Login rejected: {err_match.group(1).strip()}")
        if "captchaDiv" in resp.text:
            raise RuntimeError(
                "Captcha required. Login in browser once, then retry. "
                "(After a successful browser login, captcha is usually not required "
                "for subsequent logins from the same IP.)"
            )
        raise RuntimeError(f"Login failed: HTTP {resp.status_code}")

    if resp.status_code not in (302, 301, 303, 307, 308):
        raise RuntimeError(f"Unexpected login response: HTTP {resp.status_code}")

    redirect_url = resp.headers.get("Location", "")
    if not redirect_url:
        raise RuntimeError("No redirect after CAS login")

    # Step 3: Extract CAS Service Ticket from redirect URL
    ticket_match = re.search(r'ticket=([^&#]+)', redirect_url)
    if not ticket_match:
        raise RuntimeError(f"No ticket in redirect URL: {redirect_url[:100]}")
    ticket = ticket_match.group(1)

    # Step 4: Exchange ticket for Blade-Auth token via UCloud API
    exchange = requests.post(
        f"{API_BASE}/ykt-basics/oauth/token",
        data={"grant_type": "third", "ticket": ticket},
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
            "Authorization": "Basic c3dvcmQ6c3dvcmRfc2VjcmV0",
            "Tenant-Id": "000000",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        timeout=30,
    )
    if exchange.status_code != 200:
        detail = ""
        try:
            detail = exchange.json().get("error_description", "")
        except Exception:
            pass
        raise RuntimeError(
            f"Ticket exchange failed: HTTP {exchange.status_code} {detail}"
        )

    data = exchange.json()
    access_token = data.get("access_token", "")
    refresh_token = data.get("refresh_token", "")
    if not access_token:
        raise RuntimeError("No access_token in ticket exchange response")

    # Build identity cookie: {role}:{belongDept}
    role = data.get("currentRole", "")
    dept = data.get("belongDept", "undefined")
    identity = f"{role}:{dept}" if role else ""

    cookies = {"token": access_token, "refresh_token": refresh_token}
    if identity:
        cookies["identity"] = identity
    return cookies


# ─── Credential / Cookie management ─────────────────────────────────────────

def load_credentials() -> dict[str, str]:
    if not CREDENTIAL_FILE.exists():
        print(f"Credentials not found: {CREDENTIAL_FILE}", file=sys.stderr)
        print("Run: python tools/ucloud_auto.py --setup", file=sys.stderr)
        sys.exit(1)
    return json.loads(CREDENTIAL_FILE.read_text(encoding="utf-8"))


def save_credentials(data: dict[str, str]) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CREDENTIAL_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    os.chmod(CREDENTIAL_FILE, 0o600)


def load_cookies() -> dict[str, str]:
    if COOKIE_FILE.exists():
        return json.loads(COOKIE_FILE.read_text(encoding="utf-8"))
    return {}


def save_cookies(data: dict[str, str]) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    COOKIE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    os.chmod(COOKIE_FILE, 0o600)


def extract_user_id(token: str) -> str:
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return ""
        payload = parts[1] + "=" * (4 - len(parts[1]) % 4)
        data = json.loads(base64.urlsafe_b64decode(payload))
        return str(data.get("user_id", ""))
    except Exception:
        return ""


# ─── API session ────────────────────────────────────────────────────────────

def build_session(cookies: dict[str, str]) -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Authorization": "Basic c3dvcmQ6c3dvcmRfc2VjcmV0",
        "Tenant-Id": "000000",
        "Cache-Control": "no-cache",
    })
    token = cookies.get("token", "")
    identity = cookies.get("identity", "")
    if token:
        s.headers["Blade-Auth"] = token
    if identity:
        s.headers["identity"] = identity
    return s


def refresh_token(s: requests.Session, cookies: dict[str, str]) -> bool:
    refresh = cookies.get("refresh_token", "")
    if not refresh:
        return False
    try:
        resp = s.post(
            f"{API_BASE}/ykt-basics/oauth/token",
            data={"grant_type": "refresh_token", "refresh_token": refresh},
            timeout=30,
        )
        if resp.status_code != 200:
            return False
        data = resp.json()
        new_token = data.get("access_token", "")
        new_refresh = data.get("refresh_token", "")
        if not new_token:
            return False
        cookies["token"] = new_token
        s.headers["Blade-Auth"] = new_token
        if new_refresh:
            cookies["refresh_token"] = new_refresh
        save_cookies(cookies)
        return True
    except Exception:
        return False


# ─── Auth orchestration ─────────────────────────────────────────────────────

def ensure_auth() -> tuple[requests.Session, dict[str, str], str]:
    """Get an authenticated session, doing CAS login if needed.

    Returns (session, cookies_dict, user_id).
    """
    cookies = load_cookies()
    credentials = load_credentials()

    # Try 1: existing cookies
    if cookies.get("token"):
        s = build_session(cookies)
        # Quick check: see if token works
        try:
            uid = extract_user_id(cookies["token"])
            resp = s.get(
                f"{API_BASE}/ykt-site/site/student/undone",
                params={"userId": uid, "current": 1, "size": 1},
                timeout=20,
            )
            if resp.status_code == 200:
                return s, cookies, uid
            if resp.status_code == 401:
                print("  Token expired, trying refresh...")
        except Exception:
            pass
    else:
        s = build_session(cookies)

    # Try 2: refresh token
    if cookies.get("refresh_token"):
        s = build_session(cookies)
        if refresh_token(s, cookies):
            uid = extract_user_id(cookies["token"])
            return s, cookies, uid
        print("  Refresh failed, doing CAS login...")
    else:
        print("  No cookies, doing CAS login...")

    # Try 3: CAS login with credentials
    username = credentials.get("username", "")
    password = credentials.get("password", "")
    if not username or not password:
        print("No credentials available. Run --setup first.", file=sys.stderr)
        sys.exit(1)

    new_cookies = cas_login(username, password)
    save_cookies(new_cookies)
    s = build_session(new_cookies)
    uid = extract_user_id(new_cookies.get("token", ""))
    print("  CAS login OK.")
    return s, new_cookies, uid


# ─── Task fetching ──────────────────────────────────────────────────────────

def build_task_url(task_type: str, raw: dict[str, Any]) -> str:
    if task_type == "assignment":
        aid = raw.get("activityId") or raw.get("id") or ""
        title = raw.get("activityName") or raw.get("title") or ""
        return (
            f"{UCLASS_BASE}/student/assignmentDetails_fullpage"
            f"?activeTabName=first"
            f"&assignmentId={aid}"
            f"&assignmentType={raw.get('assignmentType', -1)}"
            f"&assignmentTitle={title}"
            f"&evaluationStatus={raw.get('evaluationStatus', 0)}"
            f"&isOpenEvaluation={raw.get('isOpenEvaluation', 0)}"
            f"&studentGroupId=undefined"
        )
    if task_type == "exam":
        eid = raw.get("activityId") or raw.get("id") or ""
        return f"{UCLASS_BASE}/testing-details?id={eid}"
    sid = raw.get("siteId") or raw.get("activityId") or ""
    if sid and sid != "-1":
        return f"{UCLASS_BASE}/student/courseDetail?siteId={sid}"
    return "https://ucloud.bupt.edu.cn/uclass/#/student/homePage"


def api_get(s: requests.Session, path: str, params: dict | None = None) -> dict:
    resp = s.get(f"{API_BASE}{path}", params=params, timeout=30)
    if resp.status_code == 401:
        return {"error": "unauthorized"}
    resp.raise_for_status()
    return resp.json()


def parse_undone_tasks(data: dict) -> list[PendingTask]:
    inner = data.get("data", {})
    rows = inner.get("undoneList") or inner.get("records") or []
    tasks = []
    for row in rows:
        raw_type = row.get("type", 0)
        task_type = TYPE_MAP.get(raw_type, "activity")
        course = str(row.get("siteName") or row.get("courseName") or "")
        tasks.append(PendingTask(
            title=str(row.get("activityName") or row.get("title") or "未命名任务"),
            course=course if course else "",
            task_type=task_type,
            deadline=str(row.get("endTime") or row.get("deadline") or ""),
            status=str(row.get("evaluationStatus") or ""),
            url=build_task_url(task_type, row),
            source_endpoint="undone_activities",
            raw_extra=row,
        ))
    return tasks


def parse_evaluation_tasks(data: dict) -> list[PendingTask]:
    inner = data.get("data", {})
    rows = inner.get("records", []) if isinstance(inner, dict) else []
    return [
        PendingTask(
            title=str(row.get("taskName") or row.get("title") or "未命名任务"),
            course=str(row.get("siteName") or row.get("courseName") or ""),
            task_type="evaluation",
            deadline=str(row.get("endTime") or row.get("deadline") or ""),
            status=str(row.get("taskStatus") or ""),
            url=build_task_url("evaluation", row),
            source_endpoint="evaluations",
            raw_extra=row,
        )
        for row in rows
    ]


# ─── Report ─────────────────────────────────────────────────────────────────

def now_date() -> str:
    return datetime.now(TIMEZONE).strftime("%Y-%m-%d")


def _is_urgent(deadline: str) -> bool:
    if not deadline:
        return False
    try:
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
            try:
                dt = datetime.strptime(deadline[:19], fmt).replace(tzinfo=TIMEZONE)
                break
            except ValueError:
                continue
        else:
            return False
        return (dt - datetime.now(TIMEZONE)).total_seconds() < 3 * 24 * 3600
    except Exception:
        return False


def generate_report(tasks: list[PendingTask], stats: dict, date: str) -> str:
    total = len(tasks)
    type_label = {"assignment": "作业", "exam": "考试", "survey": "问卷",
                  "evaluation": "互评", "activity": "活动"}

    lines = [
        "---",
        f"title: UCloud 待办任务 - {date}",
        f"date: {date}",
        "type: ucloud-tasks",
        "tags: [ucloud, tasks, pending]",
        "aliases:", f'  - "UCloud {date}"',
        "---", "",
        f"# UCloud 待办任务 - {date}", "",
        f"共 **{total}** 个待办任务（课程站点 {stats.get('site_num', 0)} 个）。", "",
    ]

    if not tasks:
        lines.append("今日没有待办任务。 :sparkles:")
        return "\n".join(lines)

    urgent = [t for t in tasks if _is_urgent(t.deadline)]
    if urgent:
        lines.append("## 临近截止")
        for t in urgent:
            lines.append(f"- **{t.title}** — {t.course or '(未关联)'} — 截止 {t.deadline[:16]} — [打开]({t.url})")
        lines.append("")

    lines.extend(["## 概览", "",
                   "| # | 任务 | 课程 | 类型 | 截止时间 |",
                   "| --- | --- | --- | --- | --- |"])
    for i, t in enumerate(tasks, 1):
        dl = t.deadline[:16] if t.deadline else "未设置"
        lines.append(f"| {i} | [{t.title}]({t.url}) | {t.course or '(未关联)'} | {type_label.get(t.task_type, t.task_type)} | {dl} |")

    lines.append("\n## 详细")
    for i, t in enumerate(tasks, 1):
        dl = t.deadline[:16] if t.deadline else "未设置"
        lines.extend([
            f"\n### {i}. {t.title}",
            f"- **课程**: {t.course or '(未关联)'}",
            f"- **类型**: {type_label.get(t.task_type, t.task_type)}",
            f"- **截止时间**: {dl}",
            f"- **链接**: [打开]({t.url})",
        ])
    lines.append("")
    return "\n".join(lines)


def save_outputs(date: str, tasks: list[PendingTask], report: str) -> Path:
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = TASKS_DIR / f"{date}.json"
    json_path.write_text(json.dumps({
        "date": date,
        "fetched_at": datetime.now(TIMEZONE).isoformat(),
        "total": len(tasks),
        "tasks": [asdict(t) for t in tasks],
    }, ensure_ascii=False, indent=2))
    md_path = TASKS_DIR / f"{date}.md"
    md_path.write_text(report)
    return TASKS_DIR


# ─── Main ───────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Auto-scrape UCloud pending tasks with CAS login fallback."
    )
    parser.add_argument("--date", help="Date YYYY-MM-DD (default: today)")
    parser.add_argument("--print-report", action="store_true", help="Print to stdout")
    parser.add_argument("--setup", action="store_true", help="Store BUPT credentials")
    parser.add_argument("--test-login", action="store_true", help="Test CAS login only")
    args = parser.parse_args()

    if args.setup:
        username = input("BUPT username (student ID): ").strip()
        password = getpass.getpass("BUPT password: ").strip()
        if username and password:
            save_credentials({"username": username, "password": password})
            print(f"Credentials saved to {CREDENTIAL_FILE}")
        return 0

    if args.test_login:
        creds = load_credentials()
        print("Testing CAS login...")
        try:
            cookies = cas_login(creds["username"], creds["password"])
            save_cookies(cookies)
            print(f"OK. Got: {list(cookies.keys())}")
        except Exception as e:
            print(f"FAILED: {e}", file=sys.stderr)
            return 1
        return 0

    date = args.date or now_date()

    print(f"UCloud auto-scrape ({date})")
    print("  Ensuring auth...")
    session, cookies, user_id = ensure_auth()

    print("  Fetching tasks...")
    all_tasks: list[PendingTask] = []
    stats: dict[str, Any] = {}

    # Undone endpoint
    resp = api_get(session, "/ykt-site/site/student/undone",
                   {"userId": user_id, "current": 1, "size": 200})
    tasks = parse_undone_tasks(resp)
    all_tasks.extend(tasks)
    inner = resp.get("data", {})
    stats["site_num"] = inner.get("siteNum", 0)
    stats["undone_num"] = inner.get("undoneNum", 0)
    print(f"  [教学活动] {len(tasks)} pending")

    # Evaluations
    resp = api_get(session, "/ykt-site/evaluate-student/taskPage",
                   {"current": 1, "size": 200})
    ev_tasks = parse_evaluation_tasks(resp)
    existing = {t.raw_extra.get("activityId") for t in all_tasks if t.raw_extra}
    for t in ev_tasks:
        eid = t.raw_extra.get("id") or t.raw_extra.get("taskId")
        if eid not in existing:
            all_tasks.append(t)
    print(f"  [互评任务] {len(ev_tasks)} pending")

    all_tasks.sort(key=lambda t: t.deadline if t.deadline else "9999")
    report = generate_report(all_tasks, stats, date)

    if args.print_report:
        print(report)
        return 0

    save_outputs(date, all_tasks, report)
    print(f"  Total: {len(all_tasks)} task(s) → {TASKS_DIR}/{date}.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
