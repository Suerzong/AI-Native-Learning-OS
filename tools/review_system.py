#!/usr/bin/env python3
"""
睡前复习与遗忘曲线系统

子命令：
  ingest   — 从 mistakes / mastery-tracker / inbox 收集知识卡片
  feedback — 处理用户复习反馈，推进间隔复习
  generate — 生成当天 15 分钟复习报告
  send     — 通过邮件发送复习报告
  tick     — 定时检查是否到达配置时间
  set-time — 调整睡前推送时间
  status   — 查看系统状态
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Optional

# ── 路径 ──────────────────────────────────────────────
REPO = Path("/home/ubuntu/Edge-AI")
REVIEW_DIR = REPO / "review"
CONFIG_PATH = REVIEW_DIR / "config.json"
QUEUE_PATH = REVIEW_DIR / "queue.json"
DAILY_DIR = REVIEW_DIR / "daily"
COURSES_DIR = REPO / "courses"
DAILY_RECORD_DIR = REPO / "plan" / "record" / "daily"
SEND_LOG = REVIEW_DIR / "send_log.json"
EMAIL_SCRIPT = REPO / "tools" / "email_push.py"
INBOX_DIR = REPO / "wechat-companion" / "inbox"

DEFAULT_CONFIG = {
    "send_time": "23:00",
    "timezone": "Asia/Shanghai",
    "intensity": "standard",
    "enabled": True,
}

INTERVALS = [0, 1, 3, 7, 14, 30]


# ═══════════════════════════════════════════════════════
# 数据模型
# ═══════════════════════════════════════════════════════

@dataclass
class ReviewCard:
    source: str
    course: str
    module: str
    content: str
    weakness: str = ""
    corrective: str = ""
    retested: bool = False
    accuracy: str = "-"
    last_test: str = ""
    interval_idx: int = 0
    next_review: str = ""
    review_count: int = 0
    added_date: str = ""


# ═══════════════════════════════════════════════════════
# 工具函数
# ═══════════════════════════════════════════════════════

def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text("utf-8"))
    return dict(DEFAULT_CONFIG)


def save_config(cfg: dict) -> None:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), "utf-8")


def load_queue() -> list[dict]:
    if QUEUE_PATH.exists():
        return json.loads(QUEUE_PATH.read_text("utf-8"))
    return []


def save_queue(cards: list[dict]) -> None:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(json.dumps(cards, ensure_ascii=False, indent=2), "utf-8")


def load_send_log() -> dict:
    if SEND_LOG.exists():
        return json.loads(SEND_LOG.read_text("utf-8"))
    return {}


def save_send_log(log: dict) -> None:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    SEND_LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2), "utf-8")


def today_str() -> str:
    return date.today().isoformat()


def card_key(card: dict) -> str:
    return f"{card['source']}|{card['course']}|{card['module']}"


def _extract_field(text: str, field_name: str) -> str:
    m = re.search(rf"{field_name}[：:]\s*(.+)", text)
    return m.group(1).strip() if m else ""


# ═══════════════════════════════════════════════════════
# 解析器
# ═══════════════════════════════════════════════════════

def parse_mastery_tracker(path: Path, course: str, max_days: int = 7) -> list[ReviewCard]:
    """解析 mastery-tracker.md，只收集最近 max_days 天内学过的技能（等级≥2）"""
    cards: list[ReviewCard] = []
    if not path.exists():
        return cards
    text = path.read_text("utf-8")
    current_section = ""
    cutoff = (date.today() - timedelta(days=max_days)).isoformat()
    for line in text.splitlines():
        if line.startswith("## "):
            current_section = line.lstrip("# ").strip()
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        cells = [c for c in cells if c]
        if len(cells) < 7:
            continue
        if cells[0] in ("技能", "---", ":---", ":---:"):
            continue
        if all(c.startswith("-") or c.startswith(":") for c in cells):
            continue
        skill = cells[0].strip("*").strip()
        chapter = cells[1]
        level = cells[2]
        accuracy = cells[3]
        last_test = cells[4]
        weakness = cells[5]
        try:
            if int(level) < 2:
                continue
        except ValueError:
            continue
        if not last_test or last_test == "-":
            continue
        if last_test < cutoff:
            continue  # 超过 7 天的不自动拉入
        cards.append(ReviewCard(
            source="mastery-tracker", course=course, module=skill,
            content=f"{skill}（{current_section}，章节 {chapter}）",
            weakness=weakness, accuracy=accuracy, last_test=last_test,
            added_date=last_test,
        ))
    return cards


def parse_mistakes(path: Path, course: str) -> list[ReviewCard]:
    cards: list[ReviewCard] = []
    if not path.exists():
        return cards
    text = path.read_text("utf-8")
    blocks = re.split(r"\n(?=###\s)", text)
    for block in blocks:
        title_m = re.match(r"###\s+(.+)", block)
        if not title_m:
            continue
        title = title_m.group(1).strip()
        skill = _extract_field(block, "所属技能")
        error = _extract_field(block, "错误表现")
        correct = _extract_field(block, "正确理解")
        task = _extract_field(block, "纠正任务")
        retested_str = _extract_field(block, "是否已复测通过")
        retested = "是" in retested_str
        if not error and not correct:
            continue
        if re.search(r"\[日期\]|#编号|\[编号\]", title):
            continue
        date_m = re.search(r"(\d{4}-\d{2}-\d{2})", title)
        added = date_m.group(1) if date_m else today_str()
        cards.append(ReviewCard(
            source="mistakes", course=course, module=skill or title,
            content=f"错题：{title}", weakness=error, corrective=task,
            retested=retested, added_date=added,
        ))
    return cards


def parse_daily_record(path: Path) -> list[str]:
    if not path.exists():
        return []
    text = path.read_text("utf-8")
    harvests: list[str] = []
    in_harvest = False
    for line in text.splitlines():
        if "今日学习收获" in line or "学习收获" in line:
            in_harvest = True
            continue
        if in_harvest:
            if line.startswith("##") or line.startswith("###"):
                break
            m = re.match(r"\d+\.\s+\*\*(.+?)\*\*[：:]\s*(.+)", line)
            if m:
                harvests.append(f"{m.group(1)}：{m.group(2)}")
    return harvests


def parse_inbox(path: Path) -> list[str]:
    """从 inbox 文件中提取已完成的学习条目"""
    if not path.exists():
        return []
    text = path.read_text("utf-8")
    entries: list[str] = []
    for line in text.splitlines():
        m = re.match(r"-\s+\[\d{2}:\d{2}\]\s+\[已完成\]\s+(.+)", line)
        if m:
            entries.append(m.group(1).strip())
    return entries


# ═══════════════════════════════════════════════════════
# 子命令：ingest
# ═══════════════════════════════════════════════════════

def cmd_ingest(args: argparse.Namespace) -> None:
    existing = load_queue()
    existing_keys = {card_key(c) for c in existing}
    new_cards: list[ReviewCard] = []
    today = date.today()

    if COURSES_DIR.exists():
        for course_dir in sorted(COURSES_DIR.iterdir()):
            if not course_dir.is_dir():
                continue
            course = course_dir.name
            # 错题：全量收集
            mk = course_dir / "mistakes.md"
            new_cards.extend(parse_mistakes(mk, course))
            # 掌握度技能：只收集最近 7 天内学过的（等级≥2）
            mt = course_dir / "mastery-tracker.md"
            new_cards.extend(parse_mastery_tracker(mt, course, max_days=7))

    # daily 记录学习收获
    for i in range(3):
        d = today - timedelta(days=i)
        dp = DAILY_RECORD_DIR / f"{d.isoformat()}.md"
        for h in parse_daily_record(dp):
            new_cards.append(ReviewCard(
                source="daily", course="daily-review",
                module=h[:30], content=h, added_date=d.isoformat(),
            ))

    # inbox 反馈（今日已完成的学习）
    inbox_path = INBOX_DIR / f"{today.isoformat()}.md"
    for entry in parse_inbox(inbox_path):
        new_cards.append(ReviewCard(
            source="inbox", course="inbox",
            module=entry[:30], content=entry, added_date=today.isoformat(),
        ))

    merged_keys = {card_key(c) for c in existing}
    added = 0
    updated = 0
    for nc in new_cards:
        nc_dict = asdict(nc)
        key = card_key(nc_dict)
        if key not in merged_keys:
            nc_dict["next_review"] = nc_dict.get("last_test") or today_str()
            existing.append(nc_dict)
            merged_keys.add(key)
            added += 1
        else:
            for c in existing:
                if card_key(c) == key:
                    if nc_dict.get("accuracy") and nc_dict["accuracy"] != "-":
                        c["accuracy"] = nc_dict["accuracy"]
                    if nc_dict.get("retested"):
                        c["retested"] = True
                    if nc_dict.get("weakness"):
                        c["weakness"] = nc_dict["weakness"]
                    if nc_dict.get("last_test"):
                        c["last_test"] = nc_dict["last_test"]
                    updated += 1
                    break
    save_queue(existing)
    print(f"ingest 完成：新增 {added} 张卡片，更新 {updated} 张，队列共 {len(existing)} 张")


# ═══════════════════════════════════════════════════════
# 子命令：feedback
# ═══════════════════════════════════════════════════════

def cmd_feedback(args: argparse.Namespace) -> None:
    """处理复习反馈，推进间隔复习。格式：'知识点=评分, 知识点=评分'"""
    text = args.text
    cards = load_queue()
    today = date.today()
    updated = 0

    # 解析反馈：逗号分割，每段 "知识点=评分"
    pairs = re.split(r"[,，;；\n]+", text)
    for pair in pairs:
        pair = pair.strip()
        m = re.match(r"(.+?)\s*[=:＝:]\s*(\d)", pair)
        if not m:
            continue
        keyword = m.group(1).strip()
        score = int(m.group(2))
        if score < 1 or score > 4:
            continue

        # 模糊匹配卡片
        matched = None
        for c in cards:
            module = c.get("module", "")
            if keyword in module or module in keyword:
                matched = c
                break
        if not matched:
            # 尝试更宽松的匹配
            for c in cards:
                content = c.get("content", "") + c.get("weakness", "")
                if keyword in content:
                    matched = c
                    break

        if not matched:
            print(f"  未匹配到：{keyword}")
            continue

        # 根据评分更新间隔
        old_idx = matched.get("interval_idx", 0)
        old_next = matched.get("next_review", "")

        if score == 4:
            # 清晰：推进间隔
            new_idx = min(old_idx + 1, len(INTERVALS) - 1)
            matched["interval_idx"] = new_idx
            matched["next_review"] = (today + timedelta(days=INTERVALS[new_idx])).isoformat()
            matched["retested"] = True
        elif score == 3:
            # 基本记得：小幅推进
            new_idx = min(old_idx + 1, len(INTERVALS) - 1) if old_idx < 3 else old_idx
            matched["interval_idx"] = new_idx
            matched["next_review"] = (today + timedelta(days=INTERVALS[new_idx])).isoformat()
            matched["retested"] = True
        elif score == 2:
            # 模糊：明天再复习
            matched["next_review"] = (today + timedelta(days=1)).isoformat()
        else:
            # 完全忘了：重置，今天再复习（实际明天）
            matched["interval_idx"] = 0
            matched["next_review"] = (today + timedelta(days=1)).isoformat()

        matched["review_count"] = matched.get("review_count", 0) + 1
        updated += 1
        print(f"  {matched['module']}: 评分 {score}，下次复习 {matched['next_review']}（间隔 {INTERVALS[matched['interval_idx']]} 天）")

    save_queue(cards)
    print(f"\nfeedback 完成：更新 {updated} 张卡片")


# ═══════════════════════════════════════════════════════
# 子命令：generate
# ═══════════════════════════════════════════════════════

def cmd_generate(args: argparse.Namespace) -> str:
    cards = load_queue()
    today = today_str()
    cfg = load_config()

    # 筛选今天到期的卡片
    due: list[dict] = []
    for c in cards:
        nr = c.get("next_review", "")
        if nr and nr <= today:
            due.append(c)
    if len(due) < 5:
        soon = date.today() + timedelta(days=3)
        for c in cards:
            nr = c.get("next_review", "")
            if nr and today < nr <= soon.isoformat() and c not in due:
                due.append(c)

    def sort_key(c: dict) -> tuple:
        is_unretested = 1 if (c.get("source") == "mistakes" and not c.get("retested")) else 0
        acc_str = c.get("accuracy", "-")
        acc_val = 100
        m = re.search(r"(\d+)", acc_str) if acc_str else None
        if m:
            acc_val = int(m.group(1))
        idx = c.get("interval_idx", 0)
        return (0 if is_unretested else 1, acc_val, idx)

    due.sort(key=sort_key)
    limit = 8 if cfg.get("intensity") == "standard" else 5
    selected = due[:limit]

    lines = [
        "# 睡前复习报告",
        f"日期：{today}",
        f"到期卡片：{len(due)} 张",
        "",
    ]

    # 今日新学知识点（从 inbox 和 mastery-tracker 变更中提取）
    new_today_cards = [c for c in cards if c.get("added_date") == today and c.get("source") in ("mastery-tracker", "inbox")]
    if new_today_cards:
        lines.append("## 今日新学知识点")
        for c in new_today_cards[:8]:
            source_tag = f"[{c.get('course')}]" if c.get("course") != "inbox" else ""
            lines.append(f"- {source_tag} {c.get('module')}：{c.get('content', '')[:60]}")
        lines.append("")

    # 到期复习卡片
    lines.append("## 今日到期复习")
    for i, c in enumerate(selected, 1):
        source_tag = "⚠️错题" if c.get("source") == "mistakes" else ""
        acc_tag = f"正确率 {c.get('accuracy', '-')}" if c.get("accuracy", "-") != "-" else ""
        interval_tag = f"第{c.get('review_count', 0)+1}次复习" if c.get("review_count", 0) > 0 else ""
        tags = " | ".join(filter(None, [source_tag, acc_tag, interval_tag]))
        lines.append(f"{i}. **[{c.get('course')}] {c.get('module')}** {tags}")
        if c.get("source") == "mistakes":
            if c.get("corrective"):
                lines.append(f"   任务：{c.get('corrective')}")
            elif c.get("weakness"):
                lines.append(f"   薄弱点：{c.get('weakness')}")
        else:
            if c.get("weakness") and c.get("weakness") != "-":
                lines.append(f"   薄弱点：{c.get('weakness')}")
        lines.append("")

    # 错题回炉
    mistake_due = [c for c in selected if c.get("source") == "mistakes" and not c.get("retested")]
    if mistake_due:
        lines.append("## 错题回炉")
        for c in mistake_due:
            task = c.get("corrective") or c.get("weakness") or "重做相关练习"
            lines.append(f"- [{c.get('course')}] {c.get('module')}：{task}")
        lines.append("")

    # 主动回忆问题
    lines.append("## 主动回忆问题")
    recall_qs = _generate_recall_questions(selected)
    for i, q in enumerate(recall_qs, 1):
        lines.append(f"{i}. {q}")
    lines.append("")

    # 明日提醒（修复：显示最近到期日期，而非只看明天）
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    upcoming = [c for c in cards if c.get("next_review", "") == tomorrow]
    if upcoming:
        lines.append("## 明日继续")
        for c in upcoming[:5]:
            lines.append(f"- [{c.get('course')}] {c.get('module')}")
    else:
        # 找最近的到期日期
        future = sorted(set(c.get("next_review", "") for c in cards if c.get("next_review", "") > today))
        if future:
            next_date = future[0]
            count = sum(1 for c in cards if c.get("next_review", "") == next_date)
            lines.append("## 下次复习")
            lines.append(f"- {next_date} 有 {count} 张卡片到期")
        else:
            lines.append("## 下次复习")
            lines.append("- 队列中暂无待复习卡片")
    lines.append("")

    lines.append("## 复习反馈")
    lines.append("完成复习后请回复：`复习反馈：知识点=评分`")
    lines.append("评分：1=完全忘了 2=模糊 3=基本记得 4=清晰")
    lines.append("示例：`复习反馈：反向传播=4, 循环队列=2`")

    report = "\n".join(lines)
    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    archive = DAILY_DIR / f"{today}.md"
    archive.write_text(report, "utf-8")
    print(f"报告已生成并归档：{archive}")
    if args.output:
        print(report)
    return report


def _generate_recall_questions(cards: list[dict]) -> list[str]:
    qs: list[str] = []
    for c in cards[:5]:
        module = c.get("module", "")
        weakness = c.get("weakness", "")
        corrective = c.get("corrective", "")
        source = c.get("source", "")
        if source == "mistakes" and weakness:
            qs.append(f"【{module}】你能正确说出：{weakness[:50]} 的正确做法吗？")
        elif corrective:
            qs.append(f"【{module}】动手做：{corrective[:60]}")
        elif weakness and weakness != "-":
            qs.append(f"【{module}】你现在的薄弱点是：{weakness[:50]}，能口述一遍正确理解吗？")
        else:
            qs.append(f"用自己的话解释 {module} 的核心要点")
    if not qs:
        qs.append("回顾今天复习的内容，哪些还不太确定？")
    return qs


# ═══════════════════════════════════════════════════════
# 子命令：send
# ═══════════════════════════════════════════════════════

def cmd_send(args: argparse.Namespace) -> None:
    today = today_str()
    archive = DAILY_DIR / f"{today}.md"
    if not archive.exists():
        print("今日报告尚未生成，先运行 generate")
        return
    report = archive.read_text("utf-8")
    plain = _md_to_plain(report)
    subject = f"[睡前复习] {today} 复习报告"
    if args.dry_run:
        print(f"[dry-run] 将发送邮件：{subject}")
        print(f"[dry-run] 收件人：Suerzong@outlook.com")
        print(f"[dry-run] 正文前 500 字：\n{plain[:500]}")
        return
    cmd = [sys.executable, str(EMAIL_SCRIPT), "--subject", subject, "--body", plain]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"复习报告已发送：{subject}")
        log = load_send_log()
        log[today] = {"time": datetime.now().isoformat(), "status": "sent"}
        save_send_log(log)
    else:
        print(f"发送失败：{result.stderr}", file=sys.stderr)
        log = load_send_log()
        log[today] = {"time": datetime.now().isoformat(), "status": "failed", "error": result.stderr}
        save_send_log(log)


def _md_to_plain(text: str) -> str:
    text = re.sub(r"^#{1,3}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    return text.strip()


# ═══════════════════════════════════════════════════════
# 子命令：tick
# ═══════════════════════════════════════════════════════

def cmd_tick(args: argparse.Namespace) -> None:
    cfg = load_config()
    if not cfg.get("enabled", True):
        return
    send_time = cfg.get("send_time", "23:00")
    now = datetime.now()
    send_h, send_m = map(int, send_time.split(":"))
    send_minutes = send_h * 60 + send_m
    current_minutes = now.hour * 60 + now.minute
    if abs(current_minutes - send_minutes) > 5:
        return
    log = load_send_log()
    today = today_str()
    if today in log and log[today].get("status") == "sent":
        return
    print(f"[{now.isoformat()}] 到达发送时间 {send_time}，开始执行复习流程...")
    cmd_ingest(args)
    cmd_generate(argparse.Namespace(output=False))
    cmd_send(argparse.Namespace(dry_run=False))


# ═══════════════════════════════════════════════════════
# 子命令：set-time
# ═══════════════════════════════════════════════════════

def cmd_set_time(args: argparse.Namespace) -> None:
    new_time = args.time
    try:
        h, m = map(int, new_time.split(":"))
        if not (0 <= h <= 23 and 0 <= m <= 59):
            raise ValueError
    except ValueError:
        print(f"时间格式错误：{new_time}，请使用 HH:MM 格式", file=sys.stderr)
        sys.exit(1)
    cfg = load_config()
    old_time = cfg.get("send_time", "23:00")
    cfg["send_time"] = new_time
    save_config(cfg)
    print(f"推送时间已从 {old_time} 更改为 {new_time}")


# ═══════════════════════════════════════════════════════
# 子命令：status
# ═══════════════════════════════════════════════════════

def cmd_status(args: argparse.Namespace) -> None:
    cfg = load_config()
    cards = load_queue()
    log = load_send_log()
    today = today_str()
    print("=== 睡前复习系统状态 ===")
    print(f"启用状态：{'是' if cfg.get('enabled', True) else '否'}")
    print(f"推送时间：{cfg.get('send_time', '23:00')}")
    print(f"时区：{cfg.get('timezone', 'Asia/Shanghai')}")
    print(f"强度：{cfg.get('intensity', 'standard')}")
    print()
    due = [c for c in cards if c.get("next_review", "") <= today]
    print(f"队列卡片总数：{len(cards)}")
    print(f"今日到期：{len(due)} 张")
    unretested = [c for c in cards if c.get("source") == "mistakes" and not c.get("retested")]
    print(f"未复测错题：{len(unretested)} 张")
    # 间隔分布
    from collections import Counter
    intervals = Counter(c.get("interval_idx", 0) for c in cards)
    print(f"间隔分布：{dict(sorted(intervals.items()))}")
    print()
    if today in log:
        entry = log[today]
        print(f"今日发送状态：{entry.get('status', '未知')}")
        print(f"发送时间：{entry.get('time', '-')}")
    else:
        print("今日尚未发送")
    recent = sorted(log.keys(), reverse=True)[:7]
    if recent:
        print("\n最近发送记录：")
        for d in recent:
            e = log[d]
            print(f"  {d}: {e.get('status', '?')} @ {e.get('time', '-')[:19]}")


# ═══════════════════════════════════════════════════════
# 主入口
# ═══════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(description="睡前复习与遗忘曲线系统")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("ingest", help="从数据源收集知识卡片")
    p_fb = sub.add_parser("feedback", help="处理复习反馈")
    p_fb.add_argument("text", help="格式：知识点=评分, 知识点=评分")
    p_gen = sub.add_parser("generate", help="生成复习报告")
    p_gen.add_argument("--output", action="store_true", help="打印报告到终端")
    p_send = sub.add_parser("send", help="发送复习报告")
    p_send.add_argument("--dry-run", action="store_true", help="只打印不发送")
    sub.add_parser("tick", help="定时检查并自动执行")
    p_time = sub.add_parser("set-time", help="调整推送时间")
    p_time.add_argument("time", help="HH:MM 格式")
    sub.add_parser("status", help="查看系统状态")
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    {
        "ingest": cmd_ingest, "feedback": cmd_feedback,
        "generate": cmd_generate, "send": cmd_send,
        "tick": cmd_tick, "set-time": cmd_set_time, "status": cmd_status,
    }[args.command](args)


if __name__ == "__main__":
    main()
