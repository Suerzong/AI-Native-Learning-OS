#!/usr/bin/env python3
"""
学习伴侣系统 — 自动规划 / 晨间启动 / 午间重置 / 晚间复盘 / 睡前复习

子命令：
  autostart         — 凌晨自动运行 /start-day 生成今日计划（由 tick 调用）
  morning           — 生成并发送晨间启动邮件
  midday            — 生成并发送午间重置邮件
  evening           — 生成并发送晚间复盘邮件
  capture "<文本>"  — 解析微信反馈并写入 inbox 和 daily 记录
  status            — 查看配置和当日发送状态
  tick              — 定时检查，自动派发（由 cron 调用）
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, date, timedelta
from pathlib import Path

# ── 路径 ──────────────────────────────────────────────
REPO = Path("/home/ubuntu/Edge-AI")
COMPANION_DIR = REPO / "wechat-companion"
CONFIG_PATH = COMPANION_DIR / "config.json"
STATE_PATH = COMPANION_DIR / "state.json"
INBOX_DIR = COMPANION_DIR / "inbox"
EMAIL_SCRIPT = REPO / "tools" / "email_push.py"
REVIEW_SCRIPT = REPO / "tools" / "review_system.py"
DAILY_PLAN = REPO / "plan" / "daily-plan.md"
TIMETABLE = REPO / "plan" / "timetable.md"
DAILY_RECORD_DIR = REPO / "plan" / "record" / "daily"
REVIEW_QUEUE = REPO / "review" / "queue.json"

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

ENCOURAGEMENTS = [
    "今天也要加油，每一步都算数。",
    "稳扎稳打，比速度更重要的是方向。",
    "你已经在路上了，继续走就好。",
    "今天的努力是明天的底气。",
    "不求最快，只求不停。",
    "每天进步一点点，积累就是力量。",
    "专注当下，未来自来。",
]


# ═══════════════════════════════════════════════════════
# 工具函数
# ═══════════════════════════════════════════════════════

def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text("utf-8"))
    return {
        "morning_time": "07:00",
        "midday_time": "12:30",
        "evening_time": "21:30",
        "sleep_review_time": "23:00",
        "timezone": "Asia/Shanghai",
        "enabled": True,
        "email_to": "Suerzong@outlook.com",
    }


def load_state() -> dict:
    today = date.today().isoformat()
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text("utf-8"))
        if state.get("date") == today:
            return state
    return {
        "date": today,
        "sent": {"morning": False, "midday": False, "evening": False, "sleep_review": False},
    }


def save_state(state: dict) -> None:
    COMPANION_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), "utf-8")


def today_str() -> str:
    return date.today().isoformat()


def today_weekday() -> str:
    return WEEKDAYS[date.today().weekday()]


def send_email(subject: str, body: str, dry_run: bool = False) -> bool:
    """调用 email_push.py 发送邮件"""
    if dry_run:
        print(f"[dry-run] 邮件主题：{subject}")
        print(f"[dry-run] 收件人：Suerzong@outlook.com")
        print(f"[dry-run] 正文前 300 字：\n{body[:300]}")
        return True

    cmd = [sys.executable, str(EMAIL_SCRIPT), "--subject", subject, "--body", body]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"邮件已发送：{subject}")
        return True
    else:
        print(f"发送失败：{result.stderr}", file=sys.stderr)
        return False


# ═══════════════════════════════════════════════════════
# 数据解析
# ═══════════════════════════════════════════════════════

def parse_daily_plan() -> dict:
    """解析 daily-plan.md，提取关键段落"""
    result = {
        "tasks": [],
        "min_line": [],
        "review_questions": [],
        "bonus": [],
        "raw_sections": {},
    }
    if not DAILY_PLAN.exists():
        return result

    text = DAILY_PLAN.read_text("utf-8")
    current_section = ""
    section_lines: list[str] = []
    sections: dict[str, list[str]] = {}

    for line in text.splitlines():
        if line.startswith("## "):
            if current_section and section_lines:
                sections[current_section] = section_lines[:]
            current_section = line.lstrip("# ").strip()
            section_lines = []
        else:
            section_lines.append(line)

    if current_section and section_lines:
        sections[current_section] = section_lines

    result["raw_sections"] = sections

    # 提取任务列表（查找含时间、模块、行动步骤的段落）
    for sec_name, lines in sections.items():
        sec_lower = sec_name.lower()
        content = "\n".join(lines)

        if "任务" in sec_name or "安排" in sec_name:
            for line in lines:
                line_s = line.strip()
                if line_s and not line_s.startswith("#") and not line_s.startswith("|"):
                    # 匹配带 checkbox 或编号的任务行
                    if re.match(r"^[-*]\s|^\d+[.)]", line_s):
                        result["tasks"].append(line_s)

        if "最低" in sec_name or "完成线" in sec_name:
            for line in lines:
                line_s = line.strip()
                if line_s and re.match(r"^[-*]\s|^\d+[.)]", line_s):
                    result["min_line"].append(line_s)

        if "复盘" in sec_name or "反思" in sec_name or "回顾" in sec_name:
            for line in lines:
                line_s = line.strip()
                if line_s and re.match(r"^\d+[.)]", line_s):
                    result["review_questions"].append(line_s)

        if "额外" in sec_name or "加分" in sec_name or "bonus" in sec_lower:
            for line in lines:
                line_s = line.strip()
                if line_s and re.match(r"^[-*]\s|^\d+[.)]", line_s):
                    result["bonus"].append(line_s)

    return result


def parse_timetable_today() -> list[str]:
    """解析 timetable.md，获取今天的课程"""
    if not TIMETABLE.exists():
        return []

    text = TIMETABLE.read_text("utf-8")
    weekday = today_weekday()  # 周一~周日
    courses: list[str] = []

    for line in text.splitlines():
        # 匹配格式：N. 课程名，...，周X第P-Q节，HH:MM-HH:MM，地点
        if not re.match(r"^\d+\.\s", line):
            continue
        if weekday in line:
            # 提取课程名和时间
            m = re.match(r"^\d+\.\s*(.+?)，(.+?)，.+?(\d{2}:\d{2}-\d{2}:\d{2})[，,](.+)", line)
            if m:
                name = m.group(1).strip()
                teacher = m.group(2).strip()
                time_slot = m.group(3).strip()
                room = m.group(4).strip()
                courses.append(f"{time_slot} {name}（{teacher}，{room}）")
            else:
                # 简单提取
                parts = line.split("，")
                if len(parts) >= 2:
                    name = parts[0].split(".", 1)[1].strip() if "." in parts[0] else parts[0]
                    courses.append(name)

    return courses


def parse_daily_record_progress() -> dict:
    """解析当日 daily 记录的任务完成情况"""
    result = {"tasks": [], "harvest": [], "raw": ""}
    record_path = DAILY_RECORD_DIR / f"{today_str()}.md"
    if not record_path.exists():
        return result

    text = record_path.read_text("utf-8")
    result["raw"] = text

    # 解析任务完成表
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        cells = [c for c in cells if c]
        if len(cells) < 3:
            continue
        if cells[0] in ("任务", ":---", "---"):
            continue
        # 判断状态
        status = "pending"
        status_cell = cells[2] if len(cells) > 2 else ""
        if "✅" in status_cell:
            status = "done"
        elif "⚠️" in status_cell or "部分" in status_cell:
            status = "partial"
        elif "❌" in status_cell or "未完成" in status_cell:
            status = "failed"
        result["tasks"].append({"name": cells[0], "status": status, "notes": cells[-1] if len(cells) > 3 else ""})

    # 解析学习收获
    in_harvest = False
    for line in text.splitlines():
        if "学习收获" in line:
            in_harvest = True
            continue
        if in_harvest:
            if line.startswith("##") or line.startswith("###"):
                break
            m = re.match(r"\d+\.\s+\*\*(.+?)\*\*[：:]\s*(.+)", line)
            if m:
                result["harvest"].append(f"{m.group(1)}：{m.group(2)}")

    return result


def get_review_due_count() -> int:
    """获取今日到期复习卡片数"""
    if not REVIEW_QUEUE.exists():
        return 0
    try:
        cards = json.loads(REVIEW_QUEUE.read_text("utf-8"))
        today = today_str()
        return sum(1 for c in cards if c.get("next_review", "") <= today)
    except (json.JSONDecodeError, KeyError):
        return 0


# ═══════════════════════════════════════════════════════
# 子命令：morning
# ═══════════════════════════════════════════════════════

def cmd_morning(args: argparse.Namespace) -> None:
    """晨间启动：今日三件事 + 最低完成线 + 课程表 + 鼓励"""
    plan = parse_daily_plan()
    courses = parse_timetable_today()
    due_count = get_review_due_count()
    weekday = today_weekday()
    today = today_str()

    lines = [
        f"早安，Ethen！今天是 {today}（{weekday}）",
        "",
    ]

    # 今日课程
    if courses:
        lines.append("【今日课程】")
        for c in courses:
            lines.append(f"  {c}")
        lines.append("")

    # 今日三件事（取前 3 个任务，或最低完成线）
    lines.append("【今日三件事】")
    if plan["tasks"]:
        for t in plan["tasks"][:3]:
            lines.append(f"  {t}")
    elif plan["min_line"]:
        for t in plan["min_line"][:3]:
            lines.append(f"  {t}")
    else:
        lines.append("  （daily-plan.md 中未找到任务，请手动规划今日重点）")
    lines.append("")

    # 最低完成线
    if plan["min_line"]:
        lines.append("【最低完成线】")
        for t in plan["min_line"]:
            lines.append(f"  {t}")
        lines.append("")

    # 复习提醒
    if due_count > 0:
        lines.append(f"【复习提醒】今日有 {due_count} 张卡片到期，睡前复习时处理")
        lines.append("")

    # 鼓励
    import random
    lines.append(f"【今日一句】{random.choice(ENCOURAGEMENTS)}")

    body = "\n".join(lines)
    subject = f"[晨间启动] {today} {weekday} 今日三件事"

    if not getattr(args, "dry_run", False):
        state = load_state()
        if send_email(subject, body, dry_run=False):
            state["sent"]["morning"] = True
            save_state(state)
    else:
        send_email(subject, body, dry_run=True)


# ═══════════════════════════════════════════════════════
# 子命令：midday
# ═══════════════════════════════════════════════════════

def cmd_midday(args: argparse.Namespace) -> None:
    """午间重置：上午完成情况 + 下午重点 + 休息提醒"""
    plan = parse_daily_plan()
    progress = parse_daily_record_progress()
    today = today_str()
    weekday = today_weekday()

    lines = [
        f"午间重置 — {today}（{weekday}）",
        "",
    ]

    # 上午完成情况
    done = [t for t in progress["tasks"] if t["status"] == "done"]
    partial = [t for t in progress["tasks"] if t["status"] == "partial"]
    failed = [t for t in progress["tasks"] if t["status"] == "failed"]

    if progress["tasks"]:
        lines.append("【上午进度】")
        if done:
            lines.append(f"  已完成：{len(done)} 项")
            for t in done:
                lines.append(f"    ✅ {t['name']}")
        if partial:
            lines.append(f"  部分完成：{len(partial)} 项")
            for t in partial:
                lines.append(f"    ⚠️ {t['name']}")
        if failed:
            lines.append(f"  未完成：{len(failed)} 项")
            for t in failed:
                lines.append(f"    ❌ {t['name']}")
        if not done and not partial and not failed:
            lines.append("  （暂无进度记录）")
    else:
        lines.append("【上午进度】")
        lines.append("  （今日 daily 记录尚无任务状态，请在下午开始前更新）")
    lines.append("")

    # 下午重点
    lines.append("【下午重点】")
    # 优先选未完成的，再选部分完成的
    afternoon_candidates = failed + partial
    if afternoon_candidates:
        lines.append(f"  优先处理：{afternoon_candidates[0]['name']}")
    elif plan["tasks"] and len(plan["tasks"]) > 3:
        lines.append(f"  推进：{plan['tasks'][3]}")
    else:
        lines.append("  按计划继续推进下午的学习任务")
    lines.append("")

    # 休息提醒
    lines.append("【休息提醒】")
    lines.append("  喝杯水，活动一下身体。")
    lines.append("  如果上午很累，闭眼休息 5 分钟再继续。")
    lines.append("  记得吃午饭，别空腹学习。")

    body = "\n".join(lines)
    subject = f"[午间重置] {today} 下午加油"

    if not getattr(args, "dry_run", False):
        state = load_state()
        if send_email(subject, body, dry_run=False):
            state["sent"]["midday"] = True
            save_state(state)
    else:
        send_email(subject, body, dry_run=True)


# ═══════════════════════════════════════════════════════
# 子命令：evening
# ═══════════════════════════════════════════════════════

def cmd_evening(args: argparse.Namespace) -> None:
    """晚间复盘入口：今日概况 + 反思问题 + 回复提示"""
    plan = parse_daily_plan()
    progress = parse_daily_record_progress()
    today = today_str()
    weekday = today_weekday()

    lines = [
        f"晚间复盘 — {today}（{weekday}）",
        "",
    ]

    # 今日任务完成概况
    if progress["tasks"]:
        done = sum(1 for t in progress["tasks"] if t["status"] == "done")
        total = len(progress["tasks"])
        lines.append(f"【今日完成度】{done}/{total}")
        for t in progress["tasks"]:
            icon = {"done": "✅", "partial": "⚠️", "failed": "❌", "pending": "⏳"}.get(t["status"], "⏳")
            lines.append(f"  {icon} {t['name']}")
    else:
        lines.append("【今日完成度】暂无记录，请补充今日 daily 记录")
    lines.append("")

    # 今日学习收获
    if progress["harvest"]:
        lines.append("【今日收获】")
        for h in progress["harvest"][:5]:
            lines.append(f"  - {h}")
        lines.append("")

    # 反思问题
    if plan["review_questions"]:
        lines.append("【复盘问题】")
        for q in plan["review_questions"][:5]:
            lines.append(f"  {q}")
    else:
        lines.append("【复盘问题】")
        lines.append("  1. 今天最大的收获是什么？")
        lines.append("  2. 有什么卡住的地方？")
        lines.append("  3. 明天最想优先做什么？")
    lines.append("")

    # 回复提示
    lines.append("【反馈格式】")
    lines.append("  在微信里回复以下关键词：")
    lines.append("  - 完成：XX课笔记写完了")
    lines.append("  - 卡住：XX概念不理解")
    lines.append("  - 调整：明天先做XX")
    lines.append("  - 心情：感觉不错 / 有点累")
    lines.append("")
    lines.append("  也可以用 /companion capture \"你的反馈\" 触发归档")

    body = "\n".join(lines)
    subject = f"[晚间复盘] {today} 今日回顾"

    if not getattr(args, "dry_run", False):
        state = load_state()
        if send_email(subject, body, dry_run=False):
            state["sent"]["evening"] = True
            save_state(state)
    else:
        send_email(subject, body, dry_run=True)


# ═══════════════════════════════════════════════════════
# 子命令：capture
# ═══════════════════════════════════════════════════════

def cmd_capture(args: argparse.Namespace) -> None:
    """解析微信反馈并写入 inbox 和 daily 记录"""
    text = args.text
    today = today_str()
    now = datetime.now().strftime("%H:%M")

    # 分类
    category = "其他"
    keywords = {
        "完成": "已完成",
        "做完": "已完成",
        "写完": "已完成",
        "搞定": "已完成",
        "卡住": "卡住",
        "不懂": "卡住",
        "不会": "卡住",
        "不理解": "卡住",
        "调整": "调整",
        "改到": "调整",
        "明天": "调整",
        "心情": "心情",
        "感觉": "心情",
        "累": "心情",
        "不错": "心情",
    }
    for kw, cat in keywords.items():
        if kw in text:
            category = cat
            break

    # 写入 inbox
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    inbox_path = INBOX_DIR / f"{today}.md"
    entry = f"- [{now}] [{category}] {text}\n"

    if inbox_path.exists():
        content = inbox_path.read_text("utf-8")
        content += entry
    else:
        content = f"# 微信反馈 — {today}\n\n{entry}"
    inbox_path.write_text(content, "utf-8")
    print(f"已写入 inbox：{inbox_path}")

    # 尝试写入 daily 记录的微信反馈区
    record_path = DAILY_RECORD_DIR / f"{today}.md"
    if record_path.exists():
        rec_text = record_path.read_text("utf-8")
        marker = "## 微信反馈"
        if marker not in rec_text:
            rec_text += f"\n\n{marker}\n\n{entry}"
        else:
            rec_text = rec_text.rstrip() + "\n" + entry
        record_path.write_text(rec_text, "utf-8")
        print(f"已追加到 daily 记录：{record_path}")
    else:
        print(f"daily 记录不存在（{record_path}），仅写入 inbox")

    # 如果是"调整"类，尝试更新 daily-plan.md
    if category == "调整":
        print("检测到调整类反馈，建议手动更新 daily-plan.md 或使用 /start-day 重新规划")


# ═══════════════════════════════════════════════════════
# 子命令：autostart
# ═══════════════════════════════════════════════════════

def cmd_autostart(args: argparse.Namespace) -> None:
    """凌晨自动运行 /start-day 生成今日计划"""
    today = today_str()
    print(f"[{datetime.now().isoformat()}] 开始自动执行 /start-day ...")

    # 重置当日 state（新的一天）
    new_state = {
        "date": today,
        "sent": {"morning": False, "midday": False, "evening": False, "sleep_review": False, "autostart": False},
    }

    result = subprocess.run(
        ["claude", "-p", "/start-day 自动生成今日计划",
         "--dangerously-skip-permissions"],
        cwd=str(REPO),
        capture_output=True, text=True, timeout=600
    )

    if result.returncode == 0:
        new_state["sent"]["autostart"] = True
        save_state(new_state)
        print(f"/start-day 执行完成，daily-plan.md 已更新")
    else:
        save_state(new_state)
        print(f"/start-day 执行失败：{result.stderr[:500]}", file=sys.stderr)


# ═══════════════════════════════════════════════════════
# 子命令：status
# ═══════════════════════════════════════════════════════

def cmd_status(args: argparse.Namespace) -> None:
    """查看系统状态"""
    cfg = load_config()
    state = load_state()

    print("=== 学习伴侣系统状态 ===")
    print(f"启用状态：{'是' if cfg.get('enabled', True) else '否'}")
    print(f"时区：{cfg.get('timezone', 'Asia/Shanghai')}")
    print(f"邮件收件人：{cfg.get('email_to', 'Suerzong@outlook.com')}")
    print()
    print("时间配置：")
    print(f"  自动规划：{cfg.get('autostart_time', '05:00')}")
    print(f"  晨间启动：{cfg.get('morning_time', '07:00')}")
    print(f"  午间重置：{cfg.get('midday_time', '12:30')}")
    print(f"  晚间复盘：{cfg.get('evening_time', '21:30')}")
    print(f"  睡前复习：{cfg.get('sleep_review_time', '23:00')}")
    print()
    print(f"当日发送状态（{state.get('date', today_str())}）：")
    for slot, sent in state.get("sent", {}).items():
        icon = "✅" if sent else "⏳"
        print(f"  {icon} {slot}")

    # 复习队列状态
    due = get_review_due_count()
    print(f"\n复习队列到期卡片：{due} 张")


# ═══════════════════════════════════════════════════════
# 子命令：tick
# ═══════════════════════════════════════════════════════

SLOT_COMMANDS = {
    "morning": cmd_morning,
    "midday": cmd_midday,
    "evening": cmd_evening,
}


def cmd_tick(args: argparse.Namespace) -> None:
    """定时检查：在各时间窗口内自动派发"""
    cfg = load_config()
    if not cfg.get("enabled", True):
        return

    state = load_state()
    now = datetime.now()
    current_minutes = now.hour * 60 + now.minute

    time_slots = {
        "autostart": cfg.get("autostart_time", "05:00"),
        "morning": cfg.get("morning_time", "07:00"),
        "midday": cfg.get("midday_time", "12:30"),
        "evening": cfg.get("evening_time", "21:30"),
        "sleep_review": cfg.get("sleep_review_time", "23:00"),
    }

    for slot, time_str in time_slots.items():
        h, m = map(int, time_str.split(":"))
        slot_minutes = h * 60 + m

        if abs(current_minutes - slot_minutes) > 5:
            continue

        if state["sent"].get(slot, False):
            continue

        print(f"[{now.isoformat()}] 到达 {slot} 时间窗口（{time_str}），开始执行...")

        if slot == "autostart":
            dummy_args = argparse.Namespace()
            cmd_autostart(dummy_args)
            # autostart 内部会重置 state 并设置 autostart=True
            state = load_state()
        elif slot == "sleep_review":
            # 委托给 review_system.py
            result = subprocess.run(
                [sys.executable, str(REVIEW_SCRIPT), "tick"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                state["sent"]["sleep_review"] = True
                print(f"睡前复习已委托 review_system.py 处理")
            else:
                print(f"review_system.py tick 失败：{result.stderr}", file=sys.stderr)
        else:
            dummy_args = argparse.Namespace(dry_run=False)
            SLOT_COMMANDS[slot](dummy_args)
            state = load_state()  # 重新读取子命令内部已保存的状态

        save_state(state)


# ═══════════════════════════════════════════════════════
# 主入口
# ═══════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(description="学习伴侣系统")
    sub = parser.add_subparsers(dest="command")

    # morning
    p_morning = sub.add_parser("morning", help="晨间启动")
    p_morning.add_argument("--dry-run", action="store_true", help="只打印不发送")

    # midday
    p_midday = sub.add_parser("midday", help="午间重置")
    p_midday.add_argument("--dry-run", action="store_true", help="只打印不发送")

    # evening
    p_evening = sub.add_parser("evening", help="晚间复盘")
    p_evening.add_argument("--dry-run", action="store_true", help="只打印不发送")

    # capture
    p_capture = sub.add_parser("capture", help="捕获微信反馈")
    p_capture.add_argument("text", help="反馈文本")
    p_capture.add_argument("--dry-run", action="store_true", help="只打印不写入")

    # status
    sub.add_parser("status", help="查看系统状态")

    # tick
    sub.add_parser("tick", help="定时检查并自动执行")

    # autostart
    sub.add_parser("autostart", help="凌晨自动运行 /start-day")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    {
        "autostart": cmd_autostart,
        "morning": cmd_morning,
        "midday": cmd_midday,
        "evening": cmd_evening,
        "capture": cmd_capture,
        "status": cmd_status,
        "tick": cmd_tick,
    }[args.command](args)


if __name__ == "__main__":
    main()
