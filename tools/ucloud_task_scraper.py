#!/usr/bin/env python
"""Scrape pending tasks from BUPT UCloud platform.

UCloud is a BladeX-based SPA. This script calls the API directly using
cookie-based auth (token stored in cookies after CAS login).

Quick start:
  1. Log into https://ucloud.bupt.edu.cn/uclass/ in your browser
  2. Create ~/.config/edge-ai/ucloud-cookies.json with token, refresh_token, identity
  3. Run: python tools/ucloud_task_scraper.py
  4. Output: ucloud-tasks/YYYY-MM-DD.json + YYYY-MM-DD.md

Primary data source:
  /ykt-site/site/student/undone  — comprehensive pending activity list
Supplementary:
  /ykt-site/evaluate-student/taskPage  — peer evaluation tasks
  /ykt-site/examination/list-stu       — exams (needs siteId context)
"""

from __future__ import annotations

import argparse
import base64
import json
import os
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
TIMEZONE = ZoneInfo("Asia/Shanghai")

API_BASE = "https://apiucloud.bupt.edu.cn"
UCLASS_BASE = "https://ucloud.bupt.edu.cn/uclass/course.html#"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# Task type mapping (from the BladeX undone endpoint)
# type=3: assignment/homework
# type=4: exam/quiz
# type=5: survey
# type=6: evaluation
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


def now_date() -> str:
    return datetime.now(TIMEZONE).strftime("%Y-%m-%d")


def extract_user_id(token: str) -> str:
    """Extract user_id from BladeX JWT payload (no validation)."""
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return ""
        payload = parts[1] + "=" * (4 - len(parts[1]) % 4)
        data = json.loads(base64.urlsafe_b64decode(payload))
        return str(data.get("user_id", ""))
    except Exception:
        return ""


def load_cookies() -> dict[str, str]:
    if not COOKIE_FILE.exists():
        print(
            f"Cookie file not found: {COOKIE_FILE}\n"
            "Create ~/.config/edge-ai/ucloud-cookies.json with: "
            '{"token": "...", "refresh_token": "...", "identity": "..."}',
            file=sys.stderr,
        )
        sys.exit(1)
    return json.loads(COOKIE_FILE.read_text(encoding="utf-8"))


def save_cookies(data: dict[str, str]) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    COOKIE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    os.chmod(COOKIE_FILE, 0o600)


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


def refresh_token(session: requests.Session, cookies: dict[str, str]) -> str | None:
    refresh = cookies.get("refresh_token", "")
    if not refresh:
        return None
    try:
        resp = session.post(
            f"{API_BASE}/ykt-basics/oauth/token",
            data={"grant_type": "refresh_token", "refresh_token": refresh},
            timeout=30,
        )
        if resp.status_code != 200:
            return None
        data = resp.json()
        new_token = data.get("access_token", "")
        new_refresh = data.get("refresh_token", "")
        if new_token:
            cookies["token"] = new_token
            session.headers["Blade-Auth"] = new_token
        if new_refresh:
            cookies["refresh_token"] = new_refresh
        save_cookies(cookies)
        print("  Token refreshed.")
        return new_token
    except Exception:
        return None


def api_get(
    session: requests.Session, path: str, params: dict[str, Any] | None = None
) -> dict[str, Any]:
    resp = session.get(f"{API_BASE}{path}", params=params, timeout=30)
    if resp.status_code == 401:
        return {"error": "unauthorized"}
    resp.raise_for_status()
    return resp.json()


def build_task_url(task_type: str, raw: dict[str, Any]) -> str:
    """Build a clickable UCloud frontend URL for a task."""

    if task_type == "assignment":
        aid = raw.get("activityId") or raw.get("id") or ""
        title = raw.get("activityName") or raw.get("title") or ""
        atype = raw.get("assignmentType", -1)
        estatus = raw.get("evaluationStatus", 0)
        is_open = raw.get("isOpenEvaluation", 0)
        return (
            f"{UCLASS_BASE}/student/assignmentDetails_fullpage"
            f"?activeTabName=first"
            f"&assignmentId={aid}"
            f"&assignmentType={atype}"
            f"&assignmentTitle={title}"
            f"&evaluationStatus={estatus}"
            f"&isOpenEvaluation={is_open}"
            f"&studentGroupId=undefined"
        )

    if task_type == "exam":
        eid = raw.get("activityId") or raw.get("id") or ""
        return f"{UCLASS_BASE}/testing-details?id={eid}"

    if task_type == "survey":
        sid = raw.get("siteId") or raw.get("activityId") or ""
        return f"{UCLASS_BASE}/student/courseDetail?siteId={sid}"

    if task_type == "evaluation":
        sid = raw.get("siteId") or raw.get("activityId") or ""
        return f"{UCLASS_BASE}/student/courseDetail?siteId={sid}"

    # generic / other activity type
    sid = raw.get("siteId") or raw.get("activityId") or ""
    if sid and sid != "-1":
        return f"{UCLASS_BASE}/student/courseDetail?siteId={sid}"
    return "https://ucloud.bupt.edu.cn/uclass/#/student/homePage"


def parse_undone_tasks(data: dict[str, Any]) -> list[PendingTask]:
    """Parse response from /ykt-site/site/student/undone.

    This endpoint returns:
      { data: { siteNum, undoneNum, undoneList: [...] } }

    Each undoneList item:
      { siteId, siteName, activityName, activityId, type, endTime,
        assignmentType, evaluationStatus, isOpenEvaluation }
    """
    inner = data.get("data", {})
    rows = inner.get("undoneList") or inner.get("records") or []
    if not rows:
        return []

    tasks = []
    for row in rows:
        raw_type = row.get("type", 0)
        task_type = TYPE_MAP.get(raw_type, "activity")

        title = (
            row.get("activityName")
            or row.get("title")
            or row.get("name")
            or "未命名任务"
        )
        course = (
            row.get("siteName")
            or row.get("courseName")
            or row.get("className")
            or ""
        )

        tasks.append(PendingTask(
            title=str(title),
            course=str(course),
            task_type=task_type,
            deadline=str(row.get("endTime") or row.get("deadline") or ""),
            status=str(
                row.get("evaluationStatus")
                or row.get("status")
                or ""
            ),
            url=build_task_url(task_type, row),
            source_endpoint="undone_activities",
            raw_extra={
                k: v for k, v in row.items()
                if k not in ("activityName", "siteName", "endTime", "evaluationStatus")
            },
        ))
    return tasks


def parse_evaluation_tasks(data: dict[str, Any]) -> list[PendingTask]:
    """Parse response from /ykt-site/evaluate-student/taskPage.

    Standard BladeX paginated response: { data: { records: [...], total, ... } }
    """
    inner = data.get("data", {})
    rows = inner.get("records", []) if isinstance(inner, dict) else []
    if not rows:
        return []

    tasks = []
    for row in rows:
        title = row.get("taskName") or row.get("title") or row.get("name") or "未命名任务"
        course = row.get("siteName") or row.get("courseName") or ""

        tasks.append(PendingTask(
            title=str(title),
            course=str(course),
            task_type="evaluation",
            deadline=str(row.get("endTime") or row.get("deadline") or ""),
            status=str(row.get("taskStatus") or row.get("status") or ""),
            url=build_task_url("evaluation", row),
            source_endpoint="evaluations",
            raw_extra={
                k: v for k, v in row.items()
                if k not in ("taskName", "siteName", "endTime", "taskStatus")
            },
        ))
    return tasks


def generate_report(all_tasks: list[PendingTask], stats: dict[str, Any], date: str) -> str:
    total = len(all_tasks)
    lines = [
        "---",
        f"title: UCloud 待办任务 - {date}",
        f"date: {date}",
        "type: ucloud-tasks",
        "tags: [ucloud, tasks, pending]",
        "aliases:",
        f'  - "UCloud {date}"',
        "---",
        "",
        f"# UCloud 待办任务 - {date}",
        "",
        f"共 **{total}** 个待办任务（课程站点 {stats.get('site_num', 0)} 个）。",
        "",
    ]

    if not all_tasks:
        lines.append("今日没有待办任务。 :sparkles:")
        return "\n".join(lines)

    # Urgent: due within 3 days
    urgent = [t for t in all_tasks if _is_urgent(t.deadline)]
    if urgent:
        lines.append("## 临近截止")
        lines.append("")
        for t in urgent:
            lines.append(f"- **{t.title}** — {t.course} — 截止 {t.deadline[:16]} — [打开]({t.url})")
        lines.append("")

    # Summary table
    lines.extend([
        "## 概览",
        "",
        "| # | 任务 | 课程 | 类型 | 截止时间 |",
        "| --- | --- | --- | --- | --- |",
    ])
    type_label = {"assignment": "作业", "exam": "考试", "survey": "问卷",
                  "evaluation": "互评", "activity": "活动"}

    for idx, task in enumerate(all_tasks, 1):
        dl = task.deadline[:16] if task.deadline else "未设置"
        label = type_label.get(task.task_type, task.task_type)
        course = task.course if task.course else "（未关联课程）"
        lines.append(f"| {idx} | [{task.title}]({task.url}) | {course} | {label} | {dl} |")

    # Detail per task
    lines.append("\n## 详细")
    for idx, task in enumerate(all_tasks, 1):
        dl = task.deadline[:16] if task.deadline else "未设置"
        course = task.course if task.course else "（未关联课程）"
        label = type_label.get(task.task_type, task.task_type)
        lines.append(f"\n### {idx}. {task.title}")
        lines.append(f"- **课程**: {course}")
        lines.append(f"- **类型**: {label}")
        lines.append(f"- **截止时间**: {dl}")
        lines.append(f"- **链接**: [打开]({task.url})")
        if task.status:
            lines.append(f"- **状态**: {task.status}")

    lines.append("")
    return "\n".join(lines)


def _is_urgent(deadline: str) -> bool:
    """Check if deadline is within 3 days."""
    if not deadline:
        return False
    try:
        # Try common formats
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
            try:
                dt = datetime.strptime(deadline[:19], fmt).replace(tzinfo=TIMEZONE)
                break
            except ValueError:
                continue
        else:
            return False
        delta = dt - datetime.now(TIMEZONE)
        return delta.total_seconds() < 3 * 24 * 3600
    except Exception:
        return False


def save_outputs(date: str, all_tasks: list[PendingTask], report: str) -> Path:
    TASKS_DIR.mkdir(parents=True, exist_ok=True)

    json_path = TASKS_DIR / f"{date}.json"
    json_data = {
        "date": date,
        "fetched_at": datetime.now(TIMEZONE).isoformat(),
        "total": len(all_tasks),
        "tasks": [asdict(t) for t in all_tasks],
    }
    json_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2))

    md_path = TASKS_DIR / f"{date}.md"
    md_path.write_text(report)

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return TASKS_DIR


def run(args: argparse.Namespace) -> int:
    date = args.date or now_date()
    cookies = load_cookies()
    user_id = extract_user_id(cookies.get("token", ""))
    session = build_session(cookies)

    print(f"Fetching pending tasks from UCloud ({date})...")

    all_tasks: list[PendingTask] = []
    stats: dict[str, Any] = {}

    # --- Primary: undone activities ---
    try:
        resp = api_get(session, "/ykt-site/site/student/undone",
                       {"userId": user_id, "current": 1, "size": 200})
    except Exception as exc:
        print(f"  [undone] error: {exc}", file=sys.stderr)
        resp = {}

    if isinstance(resp.get("error"), str) and resp["error"] == "unauthorized":
        print("  [undone] 401; refreshing token...", file=sys.stderr)
        if refresh_token(session, cookies):
            try:
                resp = api_get(session, "/ykt-site/site/student/undone",
                               {"userId": user_id, "current": 1, "size": 200})
            except Exception:
                resp = {}

    tasks = parse_undone_tasks(resp)
    all_tasks.extend(tasks)
    inner = resp.get("data", {})
    stats["site_num"] = inner.get("siteNum", 0)
    stats["undone_num"] = inner.get("undoneNum", 0)
    print(f"  [教学活动] {len(tasks)} pending")

    # --- Supplementary: evaluations ---
    try:
        resp = api_get(session, "/ykt-site/evaluate-student/taskPage",
                       {"current": 1, "size": 200})
    except Exception:
        resp = {}

    if isinstance(resp.get("error"), str) and resp["error"] == "unauthorized":
        if refresh_token(session, cookies):
            try:
                resp = api_get(session, "/ykt-site/evaluate-student/taskPage",
                               {"current": 1, "size": 200})
            except Exception:
                resp = {}

    ev_tasks = parse_evaluation_tasks(resp)
    # Avoid duplicating tasks already in undone list
    existing_ids = {t.raw_extra.get("activityId") for t in all_tasks}
    for t in ev_tasks:
        eid = t.raw_extra.get("id") or t.raw_extra.get("taskId")
        if eid not in existing_ids:
            all_tasks.append(t)
    print(f"  [互评任务] {len(ev_tasks)} pending")

    # Sort by deadline (closest first)
    all_tasks.sort(key=lambda t: t.deadline if t.deadline else "9999")

    report = generate_report(all_tasks, stats, date)

    if args.print_report:
        print(report)
        return 0

    save_outputs(date, all_tasks, report)

    if not all_tasks:
        print("No pending tasks.")
    else:
        print(f"Total: {len(all_tasks)} pending task(s).")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scrape pending tasks from BUPT UCloud platform."
    )
    parser.add_argument("--date", help="Date YYYY-MM-DD (default: today)")
    parser.add_argument("--print-report", action="store_true",
                        help="Print to stdout instead of saving")
    parser.add_argument("--cookie-file", help="Cookie JSON path")
    return parser


if __name__ == "__main__":
    _args = build_parser().parse_args()
    if _args.cookie_file:
        COOKIE_FILE = Path(_args.cookie_file)
    raise SystemExit(run(_args))
