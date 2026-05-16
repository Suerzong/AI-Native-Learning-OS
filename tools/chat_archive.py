#!/usr/bin/env python3
"""
Archive natural Weixin chats from cc-connect and generate a daily diary.

The daily window is 02:00 local time to 02:00 the next day.  For example,
--date 2026-05-14 archives messages from 2026-05-14 02:00 to
2026-05-15 02:00 and writes 2026-05-14 outputs.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from pathlib import Path
from typing import Iterable
from zoneinfo import ZoneInfo

try:
    import fcntl
except ImportError:  # pragma: no cover - this script runs on Linux.
    fcntl = None


TZ = ZoneInfo("Asia/Shanghai")
REPO = Path(os.environ.get("EDGE_AI_REPO", Path(__file__).resolve().parents[1]))
CC_SESSIONS = Path(os.environ.get("CC_CONNECT_SESSIONS", "/home/ubuntu/.cc-connect/sessions"))
CHAT_DIR = REPO / "personal" / "chat"
RAW_DIR = CHAT_DIR / "raw"
DIARY_DIR = REPO / "personal" / "diary"
DAILY_RECORD_DIR = REPO / "plan" / "record" / "daily"
LOG_DIR = REPO / "logs"

CHAT_START = "<!-- CHAT_ARCHIVE:START -->"
CHAT_END = "<!-- CHAT_ARCHIVE:END -->"
DIARY_START = "<!-- DIARY_ARCHIVE:START -->"
DIARY_END = "<!-- DIARY_ARCHIVE:END -->"

OPT_OUT_PATTERNS = (
    "别记",
    "不要记",
    "不要存",
    "别存",
    "别写进日记",
    "不要写进日记",
    "这句别记",
    "这段别记",
)

BARE_COMMANDS = {
    "stop",
    "start",
    "new",
    "reset",
    "resume",
    "help",
    "status",
    "停止",
    "中止",
    "继续",
    "新会话",
}


@dataclass(frozen=True)
class ChatEvent:
    timestamp: datetime
    role: str
    content: str
    source_session_id: str
    turn_id: int


@dataclass(frozen=True)
class ArchiveWindow:
    archive_date: date
    start: datetime
    end: datetime


def log(message: str) -> None:
    now = datetime.now(TZ).isoformat(timespec="seconds")
    print(f"[{now}] {message}")


def parse_timestamp(value: str) -> datetime:
    """Parse Go/RFC3339 timestamps with optional nanoseconds."""
    value = value.strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    match = re.match(r"^(.*?T\d{2}:\d{2}:\d{2})\.(\d+)([+-]\d{2}:\d{2})$", value)
    if match:
        head, frac, offset = match.groups()
        value = f"{head}.{frac[:6].ljust(6, '0')}{offset}"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=TZ)
    return dt.astimezone(TZ)


def compute_window(date_arg: str | None) -> ArchiveWindow:
    if date_arg:
        archive_date = date.fromisoformat(date_arg)
    else:
        now = datetime.now(TZ)
        today_at_two = datetime.combine(now.date(), time(2, 0), tzinfo=TZ)
        archive_date = (today_at_two - timedelta(days=1)).date() if now >= today_at_two else (
            today_at_two - timedelta(days=2)
        ).date()
    start = datetime.combine(archive_date, time(2, 0), tzinfo=TZ)
    end = start + timedelta(days=1)
    return ArchiveWindow(archive_date=archive_date, start=start, end=end)


def latest_session_file(explicit: str | None = None) -> Path:
    if explicit:
        path = Path(explicit).expanduser()
        if not path.exists():
            raise FileNotFoundError(path)
        return path
    candidates = sorted(CC_SESSIONS.glob("Edge-AI_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        raise FileNotFoundError(f"No Edge-AI session files found in {CC_SESSIONS}")
    return candidates[0]


def load_command_names() -> set[str]:
    commands = set(BARE_COMMANDS)
    commands_dir = REPO / ".claude" / "commands"
    if commands_dir.exists():
        for path in commands_dir.glob("*.md"):
            commands.add(path.stem)
    return commands


def first_token(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        return ""
    return re.split(r"\s+", stripped, maxsplit=1)[0].strip().lower()


def is_command_turn(user_content: str, command_names: set[str]) -> bool:
    stripped = user_content.strip()
    if not stripped:
        return True
    if stripped.startswith("/"):
        return True
    token = first_token(stripped)
    return token in command_names


def is_opted_out(user_content: str) -> bool:
    return any(pattern in user_content for pattern in OPT_OUT_PATTERNS)


def redact_sensitive(text: str) -> str:
    """Keep private records from storing obvious credentials."""
    redacted_lines: list[str] = []
    sensitive_line = re.compile(r"(token|api[_-]?key|secret|password|passwd|密码|授权码)", re.IGNORECASE)
    key_like = re.compile(r"\b(sk-[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{16,})\b")
    for line in text.splitlines() or [""]:
        if sensitive_line.search(line):
            redacted_lines.append("[已按隐私规则隐藏疑似敏感内容]")
        else:
            redacted_lines.append(key_like.sub("[已按隐私规则隐藏密钥]", line))
    return "\n".join(redacted_lines)


def iter_history_events(session_file: Path) -> Iterable[tuple[str, str, datetime, str]]:
    data = json.loads(session_file.read_text("utf-8"))
    sessions = data.get("sessions", {})
    for session_id, session in sessions.items():
        name = str(session.get("name", ""))
        if name.startswith("cron-"):
            continue
        for item in session.get("history", []):
            role = item.get("role")
            content = item.get("content")
            timestamp = item.get("timestamp")
            if role not in {"user", "assistant"}:
                continue
            if not isinstance(content, str) or not timestamp:
                continue
            yield session_id, role, parse_timestamp(timestamp), redact_sensitive(content)


def collect_chat_events(session_file: Path, window: ArchiveWindow) -> tuple[list[ChatEvent], dict[str, int]]:
    command_names = load_command_names()
    raw_events = [
        (session_id, role, ts, content)
        for session_id, role, ts, content in iter_history_events(session_file)
        if window.start <= ts < window.end
    ]
    raw_events.sort(key=lambda row: row[2])

    accepted: list[ChatEvent] = []
    skipped_command_turns = 0
    skipped_opt_out_turns = 0
    orphan_assistant = 0
    turn_id = 0
    current_include = False
    current_turn_id = 0

    for session_id, role, ts, content in raw_events:
        if role == "user":
            turn_id += 1
            current_turn_id = turn_id
            if is_opted_out(content):
                current_include = False
                skipped_opt_out_turns += 1
                continue
            if is_command_turn(content, command_names):
                current_include = False
                skipped_command_turns += 1
                continue
            current_include = True
            accepted.append(ChatEvent(ts, role, content, session_id, current_turn_id))
            continue

        if current_include:
            accepted.append(ChatEvent(ts, role, content, session_id, current_turn_id))
        else:
            orphan_assistant += 1

    stats = {
        "raw_events": len(raw_events),
        "accepted_events": len(accepted),
        "accepted_turns": len({event.turn_id for event in accepted if event.role == "user"}),
        "skipped_command_turns": skipped_command_turns,
        "skipped_opt_out_turns": skipped_opt_out_turns,
        "orphan_or_skipped_assistant_events": orphan_assistant,
    }
    return accepted, stats


def quote_block(text: str) -> str:
    if text == "":
        return "> "
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def render_chat_block(window: ArchiveWindow, events: list[ChatEvent], stats: dict[str, int], session_file: Path) -> str:
    lines = [
        CHAT_START,
        "## 自动归档",
        "",
        f"- 记录窗口：{window.start.strftime('%Y-%m-%d %H:%M')} 至 {window.end.strftime('%Y-%m-%d %H:%M')}（Asia/Shanghai）",
        f"- 来源：`{session_file}`",
        f"- 收录：{stats['accepted_events']} 条消息，{stats['accepted_turns']} 个闲聊轮次",
        f"- 排除：{stats['skipped_command_turns']} 个命令轮次，{stats['skipped_opt_out_turns']} 个明确不记录轮次",
        "",
        "## 逐字记录",
        "",
    ]
    if not events:
        lines.append("_这个窗口内没有匹配到自然闲聊。_")
    for event in events:
        role_label = "我" if event.role == "user" else "微信机器人"
        lines.extend(
            [
                f"### {event.timestamp.strftime('%H:%M:%S')} · {role_label}",
                "",
                quote_block(event.content),
                "",
            ]
        )
    lines.extend(
        [
            "## 自动摘要",
            "",
            f"- 本窗口共收录 {stats['accepted_turns']} 个自然闲聊轮次。",
            "- 正式日记由 `tools/chat_archive.py` 基于本归档生成。",
            "",
            CHAT_END,
            "",
        ]
    )
    return "\n".join(lines)


def replace_or_append_marked(existing: str, start_marker: str, end_marker: str, block: str) -> str:
    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker) + r"\n?",
        re.DOTALL,
    )
    if pattern.search(existing):
        return pattern.sub(block.rstrip() + "\n", existing)
    if existing and not existing.endswith("\n"):
        existing += "\n"
    return existing + ("\n" if existing.strip() else "") + block


def write_chat_markdown(window: ArchiveWindow, events: list[ChatEvent], stats: dict[str, int], session_file: Path) -> Path:
    CHAT_DIR.mkdir(parents=True, exist_ok=True)
    path = CHAT_DIR / f"{window.archive_date.isoformat()}.md"
    block = render_chat_block(window, events, stats, session_file)
    if path.exists():
        existing = path.read_text("utf-8")
        text = replace_or_append_marked(existing, CHAT_START, CHAT_END, block)
    else:
        text = (
            "# 闲聊记录\n\n"
            f"日期：{window.archive_date.isoformat()}\n\n"
            "## 今日片段\n\n"
            + block
        )
    path.write_text(text, "utf-8")
    return path


def write_raw_jsonl(window: ArchiveWindow, events: list[ChatEvent]) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / f"{window.archive_date.isoformat()}.jsonl"
    with path.open("w", encoding="utf-8") as fh:
        for event in events:
            fh.write(
                json.dumps(
                    {
                        "timestamp": event.timestamp.isoformat(),
                        "role": event.role,
                        "content": event.content,
                        "source_session_id": event.source_session_id,
                        "turn_id": event.turn_id,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
    return path


def find_claude() -> str | None:
    env_bin = os.environ.get("CLAUDE_BIN")
    candidates = [
        env_bin,
        shutil.which("claude"),
        "/home/ubuntu/.npm-global/bin/claude",
        "/usr/local/bin/claude",
        "/usr/bin/claude",
        "/home/ubuntu/.local/bin/claude",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    return None


def truncate_source(text: str, limit: int = 60000) -> str:
    if len(text) <= limit:
        return text
    keep = limit // 2
    return (
        text[:keep]
        + "\n\n[中间内容过长，已在生成日记时截断；原始归档文件保留完整内容。]\n\n"
        + text[-keep:]
    )


def build_diary_prompt(window: ArchiveWindow, chat_text: str, daily_record_text: str) -> str:
    date_str = window.archive_date.isoformat()
    return f"""请基于下面材料，写一篇 {date_str} 的正式日记。

要求：
- 使用第一人称“我”。
- 文风克制、真实、温和，可以有一点文学感，但不要夸张煽情。
- 不要把零散情绪上升成武断人生结论。
- 保留当天真实发生的事、情绪底色、值得记住的原话。
- 如果材料不足，就如实写成短日记，不要编造。
- 只输出日记正文 Markdown，不要解释，不要写代码，不要调用工具，不要修改文件。

【聊天归档】
{truncate_source(chat_text)}

【学习/每日复盘，可选】
{truncate_source(daily_record_text, 20000) if daily_record_text.strip() else "无"}
"""


def call_claude(prompt: str) -> tuple[bool, str]:
    claude_bin = find_claude()
    if not claude_bin:
        return False, "未找到 claude 命令；已完成聊天归档，跳过日记生成。"
    cmd = [claude_bin, "-p", prompt, "--dangerously-skip-permissions"]
    try:
        result = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        return False, "claude 生成日记超时。"
    if result.returncode != 0:
        err = result.stderr.strip() or result.stdout.strip()
        return False, f"claude 生成日记失败：{err[:1000]}"
    text = result.stdout.strip()
    if not text:
        return False, "claude 没有返回日记正文。"
    return True, text


def write_diary(window: ArchiveWindow, diary_body: str) -> Path:
    DIARY_DIR.mkdir(parents=True, exist_ok=True)
    path = DIARY_DIR / f"{window.archive_date.isoformat()}.md"
    block = "\n".join(
        [
            DIARY_START,
            f"# {window.archive_date.isoformat()} 日记",
            "",
            diary_body.strip(),
            "",
            DIARY_END,
            "",
        ]
    )
    if path.exists():
        existing = path.read_text("utf-8")
        if DIARY_START not in existing or DIARY_END not in existing:
            raise FileExistsError(f"{path} 已存在且不是自动生成文件，跳过覆盖。")
        text = replace_or_append_marked(existing, DIARY_START, DIARY_END, block)
    else:
        text = block
    path.write_text(text, "utf-8")
    return path


def generate_diary(window: ArchiveWindow, chat_md_path: Path) -> tuple[bool, str | Path]:
    chat_text = chat_md_path.read_text("utf-8")
    daily_record_path = DAILY_RECORD_DIR / f"{window.archive_date.isoformat()}.md"
    daily_text = daily_record_path.read_text("utf-8") if daily_record_path.exists() else ""
    ok, body_or_error = call_claude(build_diary_prompt(window, chat_text, daily_text))
    if not ok:
        return False, body_or_error
    try:
        return True, write_diary(window, body_or_error)
    except FileExistsError as exc:
        return False, str(exc)


def acquire_lock():
    lock_path = Path("/tmp/edge-ai-chat-archive.lock")
    lock_fh = lock_path.open("w", encoding="utf-8")
    if fcntl is not None:
        fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
    return lock_fh


def run(args: argparse.Namespace) -> int:
    try:
        lock_fh = acquire_lock()
    except BlockingIOError:
        log("另一个 chat_archive.py 正在运行，本次退出。")
        return 2

    with lock_fh:
        window = compute_window(args.date)
        session_file = latest_session_file(args.session_file)
        events, stats = collect_chat_events(session_file, window)

        log(f"归档日期：{window.archive_date.isoformat()}")
        log(f"窗口：{window.start.isoformat()} -> {window.end.isoformat()}")
        log(f"会话文件：{session_file}")
        log(
            "消息统计："
            f"raw={stats['raw_events']} accepted={stats['accepted_events']} "
            f"turns={stats['accepted_turns']} commands={stats['skipped_command_turns']} "
            f"optout={stats['skipped_opt_out_turns']}"
        )

        if args.dry_run:
            log(f"[dry-run] 将写入：{RAW_DIR / (window.archive_date.isoformat() + '.jsonl')}")
            log(f"[dry-run] 将写入：{CHAT_DIR / (window.archive_date.isoformat() + '.md')}")
            log(f"[dry-run] 将生成日记：{DIARY_DIR / (window.archive_date.isoformat() + '.md')}")
            return 0

        raw_path = write_raw_jsonl(window, events)
        chat_md_path = write_chat_markdown(window, events, stats, session_file)
        log(f"已写入原始 JSONL：{raw_path}")
        log(f"已写入聊天归档：{chat_md_path}")

        if args.no_diary:
            log("已按参数跳过日记生成。")
            return 0

        ok, diary_result = generate_diary(window, chat_md_path)
        if ok:
            log(f"已生成日记：{diary_result}")
            return 0
        log(str(diary_result))
        return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Archive cc-connect Weixin chats and generate a daily diary.")
    parser.add_argument("command", nargs="?", default="run", choices=["run"], help="Command to run.")
    parser.add_argument("--date", help="Archive date in YYYY-MM-DD. Window is date 02:00 to next day 02:00.")
    parser.add_argument("--session-file", help="Explicit cc-connect session JSON path.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing files.")
    parser.add_argument("--no-diary", action="store_true", help="Archive chats only; skip diary generation.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return run(args)
    except Exception as exc:  # Keep cron logs actionable.
        log(f"失败：{exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
