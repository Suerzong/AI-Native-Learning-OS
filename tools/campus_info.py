#!/usr/bin/env python3
"""BUPT Campus Information scraper with change detection and email.

Scrapes the consulting/information portal from UCloud root SPA:
  - 教务通知 (type=1): Academic notifications
  - 教务新闻 (type=2): Academic news

Reuses ucloud_auto auth (CAS token). Detects new items since last run
and sends email notifications.

Usage:
  python tools/campus_info.py                  # full run
  python tools/campus_info.py --dry-run        # print email, don't send
  python tools/campus_info.py --print-report   # stdout only
"""

from __future__ import annotations

import argparse
import json
import os
import smtplib
import ssl
import sys
import time
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ucloud_auto as ua

WORKSPACE = Path(__file__).resolve().parents[1]
INFO_DIR = WORKSPACE / "campus-info"
SNAPSHOT_FILE = INFO_DIR / ".latest.json"
TIMEZONE = ZoneInfo("Asia/Shanghai")

CATEGORIES = {1: "教务通知", 2: "教务新闻"}

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


def fetch_news(session: Any, news_type: int, size: int = 50) -> list[dict]:
    resp = ua.api_get(session, "/blade-portal/news/list",
                       {"type": news_type, "current": 1, "size": size})
    data = resp.get("data", {})
    records = data.get("records", []) if isinstance(data, dict) else []
    return [dict(r) for r in records] if records else []


def load_snapshot() -> dict:
    if SNAPSHOT_FILE.exists():
        return json.loads(SNAPSHOT_FILE.read_text(encoding="utf-8"))
    return {"date": "", "items": []}


def save_snapshot(items: list[dict], date: str) -> None:
    INFO_DIR.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_FILE.write_text(json.dumps({
        "date": date,
        "items": [{"id": it.get("id", ""), "title": it.get("title", ""),
                    "type": it.get("type", ""), "date": it.get("date", "")}
                  for it in items],
    }, ensure_ascii=False, indent=2))


def compare_items(current: list[dict], previous: list[dict]) -> list[dict]:
    prev_ids = {it.get("id", "") for it in previous}
    return [it for it in current if it.get("id", "") not in prev_ids]


def build_email_body(new_items: list[dict], date: str) -> str | None:
    if not new_items:
        return None

    lines = [
        f"BUPT 校内信息更新 — {date}",
        "",
        f"新增 {len(new_items)} 条信息：",
        "",
    ]
    for it in new_items:
        cat = CATEGORIES.get(it.get("type", 0), "其他")
        pub_date = it.get("date", "")[:16]
        lines.append(f"  [{cat}] {it['title']}")
        lines.append(f"  发布时间: {pub_date}")
        lines.append(f"  作者: {it.get('author', '未知')}")
        lines.append(f"  链接: https://ucloud.bupt.edu.cn/#/consulting?tab={it.get('type', 1) - 1}")
        lines.append("")

    lines.append("——")
    lines.append("Edge-AI Campus Info Monitor")
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


def generate_report(items: list[dict], date: str) -> str:
    lines = [
        "---",
        f"title: BUPT 校内信息 - {date}",
        f"date: {date}",
        "type: campus-info",
        "tags: [campus, info, news]",
        "---", "",
        f"# BUPT 校内信息 - {date}", "",
        f"共 **{len(items)}** 条信息。", "",
    ]

    for cat_id, cat_name in CATEGORIES.items():
        cat_items = [it for it in items if it.get("type", 0) == cat_id]
        if cat_items:
            lines.extend([f"## {cat_name}", "",
                          "| # | 标题 | 发布时间 | 作者 |",
                          "| --- | --- | --- | --- |"])
            for i, it in enumerate(cat_items, 1):
                pub_date = it.get("date", "")[:16]
                lines.append(f"| {i} | {it['title']} | {pub_date} | {it.get('author', '')} |")
            lines.append("")

    return "\n".join(lines)


def save_outputs(date: str, items: list[dict], report: str) -> None:
    INFO_DIR.mkdir(parents=True, exist_ok=True)
    json_path = INFO_DIR / f"{date}.json"
    json_path.write_text(json.dumps({
        "date": date,
        "fetched_at": datetime.now(TIMEZONE).isoformat(),
        "total": len(items),
        "items": items,
    }, ensure_ascii=False, indent=2))
    md_path = INFO_DIR / f"{date}.md"
    md_path.write_text(report)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="BUPT campus information scraper with change detection."
    )
    parser.add_argument("--dry-run", action="store_true", help="Print email, don't send")
    parser.add_argument("--print-report", action="store_true", help="Print report to stdout")
    parser.add_argument("--full", action="store_true", help="Fetch full content (title+body)")
    args = parser.parse_args()

    load_env_file()
    date = datetime.now(TIMEZONE).strftime("%Y-%m-%d")

    print(f"Campus Info Scraper ({date})")
    print("  Authenticating...")
    try:
        session, _cookies, _uid = ua.ensure_auth()
    except SystemExit:
        print("  Auth failed.", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"  Auth error: {exc}", file=sys.stderr)
        return 1

    print("  Fetching news...")
    all_items: list[dict] = []
    for cat_id, cat_name in CATEGORIES.items():
        records = fetch_news(session, cat_id)
        for r in records:
            r["type"] = cat_id
        all_items.extend(records)
        print(f"  [{cat_name}] {len(records)} items")

    all_items.sort(key=lambda x: x.get("date", ""), reverse=True)

    if args.print_report:
        print(generate_report(all_items, date))
        return 0

    save_outputs(date, all_items, generate_report(all_items, date))

    prev = load_snapshot()
    if not prev.get("date"):
        save_snapshot(all_items, date)
        print(f"  First run — snapshot saved. No comparison yet.")
        return 0

    new_items = compare_items(all_items, prev.get("items", []))
    print(f"  New items: {len(new_items)}")

    if not new_items:
        print("  No new items.")
        return 0

    save_snapshot(all_items, date)

    body = build_email_body(new_items, date)
    if body:
        subject = f"BUPT 校内信息 {len(new_items)}条新增 — {date}"
        send_email(subject, body, dry_run=args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
