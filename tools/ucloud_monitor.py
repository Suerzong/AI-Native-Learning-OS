#!/usr/bin/env python3
"""Monitor UCloud task changes and send email notifications.

Compares current pending tasks against the last known snapshot.
- New tasks → "你有新的[作业/考试/...]：XXX"
- Completed tasks → "你完成了[作业/考试/...]：XXX"

Intended for cron: runs ucloud_auto scraping + change detection + email.

Usage:
  python tools/ucloud_monitor.py                    # full run
  python tools/ucloud_monitor.py --dry-run           # print email, don't send
  python tools/ucloud_monitor.py --scrape-only       # just scrape, don't compare
"""

from __future__ import annotations

import json
import os
import smtplib
import ssl
import sys
import time
from dataclasses import asdict
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

# Import ucloud_auto for auth + scraping
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ucloud_auto as ua

WORKSPACE = Path(__file__).resolve().parents[1]
TASKS_DIR = WORKSPACE / "ucloud-tasks"
SNAPSHOT_FILE = TASKS_DIR / ".latest.json"
TIMEZONE = ZoneInfo("Asia/Shanghai")

TYPE_CN = {"assignment": "作业", "exam": "考试", "survey": "问卷",
           "evaluation": "互评", "activity": "活动"}

# Email config (reuse same env as email_push.py)
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.qq.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SMTP_FROM = os.getenv("SMTP_FROM", "") or SMTP_USER
EMAIL_TO = os.getenv("TECH_INTEL_TO", "Suerzong@outlook.com")


def load_env_file() -> None:
    env_path = Path.home() / ".config" / "edge-ai" / "email.env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def load_snapshot() -> dict[str, Any]:
    """Load the last known task snapshot."""
    if SNAPSHOT_FILE.exists():
        return json.loads(SNAPSHOT_FILE.read_text(encoding="utf-8"))
    return {"date": "", "tasks": []}


def save_snapshot(tasks: list[dict], date: str) -> None:
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_FILE.write_text(json.dumps({
        "date": date,
        "tasks": [{"activityId": t.get("raw_extra", {}).get("activityId", ""),
                    "title": t["title"],
                    "task_type": t["task_type"],
                    "deadline": t["deadline"]}
                   for t in tasks],
    }, ensure_ascii=False, indent=2))


def save_daily_outputs(date: str, all_tasks: list[dict]) -> None:
    """Write ucloud-tasks/YYYY-MM-DD.json + .md for start-day consumption."""
    TASKS_DIR.mkdir(parents=True, exist_ok=True)

    # JSON
    json_path = TASKS_DIR / f"{date}.json"
    json_data = {
        "date": date,
        "fetched_at": datetime.now(TIMEZONE).isoformat(),
        "total": len(all_tasks),
        "tasks": all_tasks,
    }
    json_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2),
                         encoding="utf-8")

    # Markdown report
    now = datetime.now(TIMEZONE).strftime("%H:%M")
    lines = [
        f"# UCloud 待办任务 — {date}",
        "",
        f"抓取时间：{date} {now}，共 **{len(all_tasks)}** 个待办。",
        "",
    ]

    urgent = [t for t in all_tasks
              if t.get("deadline") and _days_until(t["deadline"]) <= 3]
    if urgent:
        lines.append("## 临近截止（3 天内）")
        lines.append("")
        for t in urgent:
            dl = t["deadline"][:16] if t["deadline"] else "未设置"
            lines.append(f"- [{t['title']}]({t['url']}) — 截止 {dl}")
        lines.append("")

    lines.extend([
        "## 全部待办",
        "",
        "| # | 任务 | 类型 | 截止时间 |",
        "| --- | --- | --- | --- |",
    ])
    for i, t in enumerate(all_tasks, 1):
        dl = t["deadline"][:16] if t.get("deadline") else "未设置"
        tn = TYPE_CN.get(t.get("task_type", ""), t.get("task_type", ""))
        lines.append(f"| {i} | [{t['title']}]({t['url']}) | {tn} | {dl} |")

    lines.append("")
    md_path = TASKS_DIR / f"{date}.md"
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"  [每日输出] {json_path.name} / {md_path.name}")


def _days_until(deadline: str) -> float:
    """Return days until deadline (negative if past)."""
    try:
        dl = datetime.strptime(deadline[:19], "%Y-%m-%d %H:%M:%S").replace(
            tzinfo=TIMEZONE)
        return (dl - datetime.now(TIMEZONE)).total_seconds() / 86400
    except (ValueError, TypeError):
        return 999


def compare_tasks(current: list[dict], previous: list[dict]) -> tuple[list[dict], list[dict]]:
    """Compare current vs previous tasks by activityId.

    Returns (new_tasks, completed_tasks).
    """
    cur_ids = {t.get("raw_extra", {}).get("activityId", "") for t in current if t.get("raw_extra")}
    prev_ids = {t.get("activityId", "") for t in previous}

    new_ids = cur_ids - prev_ids
    completed_ids = prev_ids - cur_ids

    new = [t for t in current
           if t.get("raw_extra", {}).get("activityId", "") in new_ids]
    completed = [t for t in previous
                 if t.get("activityId", "") in completed_ids]

    return new, completed


def build_email_body(new: list[dict], completed: list[dict], date: str) -> str | None:
    """Build notification email body. Returns None if no changes."""
    if not new and not completed:
        return None

    lines = [
        f"UCloud 任务变更通知 — {date}",
        "",
    ]

    if new:
        labels = ", ".join(
            f"{len([t for t in new if t['task_type'] == tp])}{TYPE_CN.get(tp, tp)}"
            for tp in sorted({t["task_type"] for t in new})
        )
        lines.append(f"新增 {len(new)} 个待办（{labels}）：")
        lines.append("")
        for t in new:
            tn = TYPE_CN.get(t["task_type"], t["task_type"])
            dl = t["deadline"][:16] if t["deadline"] else "未设置"
            lines.append(f"  [{tn}] {t['title']}")
            lines.append(f"  截止: {dl}")
            lines.append(f"  链接: {t['url']}")
            lines.append("")
    else:
        lines.append("本次无新增任务。")

    if completed:
        labels = ", ".join(
            f"{len([t for t in completed if t['task_type'] == tp])}{TYPE_CN.get(tp, tp)}"
            for tp in sorted({t["task_type"] for t in completed})
        )
        lines.append(f"完成 {len(completed)} 个任务（{labels}）：")
        lines.append("")
        for t in completed:
            tn = TYPE_CN.get(t["task_type"], t["task_type"])
            lines.append(f"  [{tn}] {t['title']}")
            lines.append(f"  原截止: {t.get('deadline', '')[:16]}")
            lines.append("")
    else:
        lines.append("本次无完成任务。")

    lines.append("——")
    lines.append("Edge-AI UCloud Monitor")
    return "\n".join(lines)


def send_email(subject: str, body: str, dry_run: bool = False) -> bool:
    if dry_run:
        print(f"[DRY RUN] To: {EMAIL_TO}")
        print(f"[DRY RUN] Subject: {subject}")
        print(body)
        return True

    if not SMTP_USER or not SMTP_PASSWORD:
        print("SMTP not configured. Skipping email.", file=sys.stderr)
        print(f"Subject would be: {subject}")
        print(body)
        return False

    msg = EmailMessage()
    msg["From"] = SMTP_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT,
                              context=ssl.create_default_context(),
                              timeout=20) as srv:
            srv.login(SMTP_USER, SMTP_PASSWORD)
            srv.send_message(msg)
        print(f"Email sent to {EMAIL_TO}")
        return True
    except Exception as exc:
        print(f"Email failed: {exc}", file=sys.stderr)
        return False


def main() -> int:
    import argparse
    p = argparse.ArgumentParser(description="Monitor UCloud task changes and email.")
    p.add_argument("--dry-run", action="store_true", help="Print email, don't send")
    p.add_argument("--scrape-only", action="store_true", help="Scrape only, no compare")
    args = p.parse_args()

    load_env_file()
    date = datetime.now(TIMEZONE).strftime("%Y-%m-%d")

    # 1. Scrape current tasks
    print(f"UCloud Monitor ({date})")
    print("  Authenticating + scraping...")
    try:
        session, cookies, user_id = ua.ensure_auth()
    except SystemExit:
        print("  Auth failed.", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"  Auth error: {exc}", file=sys.stderr)
        return 1

    all_tasks: list[dict] = []

    resp = ua.api_get(session, "/ykt-site/site/student/undone",
                      {"userId": user_id, "current": 1, "size": 200})
    parsed = ua.parse_undone_tasks(resp)
    all_tasks.extend(ua.asdict(t) for t in parsed)
    inner = resp.get("data", {})
    print(f"  [教学活动] {len(parsed)} pending (total {inner.get('undoneNum', 0)})")

    resp = ua.api_get(session, "/ykt-site/evaluate-student/taskPage",
                      {"current": 1, "size": 200})
    ev_parsed = ua.parse_evaluation_tasks(resp)
    existing = {
        t.get("raw_extra", {}).get("activityId", "")
        for t in all_tasks if t.get("raw_extra")
    }
    for t in ev_parsed:
        eid = (t.raw_extra.get("id") if hasattr(t, 'raw_extra') else None) \
              or (t.raw_extra.get("taskId") if hasattr(t, 'raw_extra') else None)
        if eid not in existing:
            all_tasks.append(ua.asdict(t))
    print(f"  [互评任务] {len(ev_parsed)} pending")

    # Save snapshot
    save_snapshot(all_tasks, date)

    # Save daily JSON + MD for start-day consumption
    save_daily_outputs(date, all_tasks)

    if args.scrape_only:
        print("  scrape-only mode, skipping comparison.")
        return 0

    # 2. Compare with previous
    prev = load_snapshot()
    if not prev.get("date"):
        print(f"  First run — snapshot saved. No comparison yet.")
        return 0

    # Previous tasks are in the snapshot format
    prev_tasks = prev.get("tasks", [])
    current_tasks = all_tasks
    new, completed = compare_tasks(current_tasks, prev_tasks)

    print(f"  New: {len(new)}, Completed: {len(completed)}")

    if not new and not completed:
        print("  No changes.")
        return 0

    # 3. Build and send email
    body = build_email_body(new, completed, date)
    if body:
        new_summary = f"{len(new)}新增" if new else ""
        comp_summary = f"{len(completed)}完成" if completed else ""
        subject = f"UCloud {' '.join(filter(None, [new_summary, comp_summary]))} — {date}"
        send_email(subject, body, dry_run=args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
