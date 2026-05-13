#!/usr/bin/env python3
"""
学习伴侣系统 — 自动规划 / 晨间启动 / 午间重置 / 晚间复盘 / 睡前复习

子命令：
  autostart         — 凌晨自动运行 /start-day 生成今日计划
  morning           — 生成并发送晨间启动邮件
  midday            — 生成并发送午间重置邮件
  evening           — 生成并发送晚间复盘邮件
  capture "<文本>"  — 解析微信反馈并写入 inbox 和 daily 记录
  update-schedule   — 更新课表临时调课记录
  status            — 查看配置和当日发送状态
  tick              — 定时检查，自动派发
"""

from __future__ import annotations

import argparse
import json
import os
import random
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
SCHOOL_CALENDAR = REPO / "plan" / "school-calendar.md"
DAILY_RECORD_DIR = REPO / "plan" / "record" / "daily"
REVIEW_QUEUE = REPO / "review" / "queue.json"

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

# ── 鼓励语（30+ 条，学习场景相关）─────────────────────
ENCOURAGEMENTS = [
    "今天也要加油，每一步都算数。",
    "稳扎稳打，比速度更重要的是方向。",
    "你已经在路上了，继续走就好。",
    "今天的努力是明天的底气。",
    "不求最快，只求不停。",
    "每天进步一点点，积累就是力量。",
    "专注当下，未来自来。",
    "学得慢没关系，停下来才可怕。",
    "把大目标拆成小步骤，今天只管今天。",
    "能坚持到现在，你已经很厉害了。",
    "累了就休息，休息完继续。",
    "比起昨天的自己进步一点就够了。",
    "不用和别人比，你的节奏刚刚好。",
    "困难是暂时的，成长是永久的。",
    "每一次不放弃都是在积累底气。",
    "今天搞懂了一个难点，明天它就变成你的优势。",
    "错题是最好的老师，每条都在帮你变得更扎实。",
    "能把学到的东西讲出来，说明你真的理解了。",
    "写代码不怕报错，怕的是不敢运行。",
    "调试过程本身就是学习。",
    "今天多理解一个概念，明天就少一个盲区。",
    "动手做比想十遍更有效。",
    "遇到不会的很正常，会了才需要学。",
    "坚持记录本身就是一种能力。",
    "每天回头看一眼进步，比闷头赶路更重要。",
    "你不是在赶进度，你是在建体系。",
    "慢一点没关系，方向对了就在靠近。",
    "今天的你比昨天多懂了一点。",
    "学累了就换个科目，换个思路。",
    "完成比完美更重要。",
    "先做完，再做好。",
    "别忘了你已经走了多远。",
]

# ── 休息提醒（30+ 条，分类轮换）──────────────────────
REST_TIPS_BODY = [
    "喝杯水，活动一下身体。",
    "站起来伸个懒腰，拉伸一下手臂。",
    "走动 2 分钟，活动活动腿脚。",
    "转转脖子，放松一下肩颈。",
    "做 10 个深蹲或开合跳，提提神。",
    "靠墙站 1 分钟，矫正一下坐姿。",
    "搓搓手，按摩一下太阳穴。",
    "伸展手指和手腕，保护它们。",
]
REST_TIPS_MIND = [
    "深呼吸三次，放松一下肩膀。",
    "闭眼冥想 2 分钟，清空一下思绪。",
    "看看窗外的天空，让眼睛休息一下。",
    "闭眼听一首轻音乐，给自己 3 分钟。",
    "想一件今天让你开心的小事。",
    "闭眼回想刚才学的内容，默念一遍关键点。",
    "做个白日梦，放空 1 分钟。",
]
REST_TIPS_FOOD = [
    "吃个水果补充能量。",
    "去洗把脸，清醒一下。",
    "泡杯茶或咖啡，换个心情。",
    "吃几颗坚果，补充点好脂肪。",
    "如果快到饭点了，先去吃饭吧。",
    "来杯酸奶或牛奶。",
    "吃块黑巧克力，提神又补脑。",
]
REST_TIPS_SOCIAL = [
    "给朋友发条消息，聊两句。",
    "整理一下桌面，清爽的环境有助于专注。",
    "看看有没有新消息需要回复。",
    "站起来倒杯水，顺便看看室友在干嘛。",
    "把手机翻面放 10 分钟。",
]
REST_TIPS_STUDY = [
    "回忆一下今天学到的最有意思的点。",
    "在纸上画一个刚才学的概念的思维导图。",
    "试着用一句话总结刚才学的内容。",
    "想想这个知识在实际项目中怎么用。",
    "默写一下刚才记住的关键公式或代码片段。",
]


# ═══════════════════════════════════════════════════════
# 工具函数
# ═══════════════════════════════════════════════════════

def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text("utf-8"))
    return {
        "autostart_time": "05:00", "morning_time": "07:00",
        "midday_time": "12:30", "evening_time": "21:30",
        "sleep_review_time": "23:00", "timezone": "Asia/Shanghai",
        "enabled": True, "email_to": "Suerzong@outlook.com",
    }


def load_state() -> dict:
    today = date.today().isoformat()
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text("utf-8"))
        if state.get("date") == today:
            return state
    return {
        "date": today,
        "sent": {"morning": False, "midday": False, "evening": False, "sleep_review": False, "autostart": False},
        "used_encouragements": [], "used_tips": [],
    }


def save_state(state: dict) -> None:
    COMPANION_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), "utf-8")


def today_str() -> str:
    return date.today().isoformat()


def today_weekday() -> str:
    return WEEKDAYS[date.today().weekday()]


def send_email(subject: str, body: str, dry_run: bool = False) -> bool:
    if dry_run:
        print(f"[dry-run] 邮件主题：{subject}")
        print(f"[dry-run] 收件人：Suerzong@outlook.com")
        print(f"[dry-run] 正文：\n{body}")
        return True
    cmd = [sys.executable, str(EMAIL_SCRIPT), "--subject", subject, "--body", body]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"邮件已发送：{subject}")
        return True
    else:
        print(f"发送失败：{result.stderr}", file=sys.stderr)
        return False


def pick_unique(pool: list[str], used_indices: list[int]) -> tuple[str, int]:
    available = [(i, v) for i, v in enumerate(pool) if i not in used_indices]
    if not available:
        idx = random.randint(0, len(pool) - 1)
        return pool[idx], idx
    idx, val = random.choice(available)
    return val, idx


def pick_rest_tip(used_indices: list[int]) -> tuple[str, int]:
    """从分类池中选休息提醒，避免连续同类"""
    all_tips = REST_TIPS_BODY + REST_TIPS_MIND + REST_TIPS_FOOD + REST_TIPS_SOCIAL + REST_TIPS_STUDY
    return pick_unique(all_tips, used_indices)


def run_cmd(cmd: list[str], cwd: str | None = None) -> str:
    """运行命令，返回 stdout"""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=cwd)
        return r.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return ""


# ═══════════════════════════════════════════════════════
# 周次计算
# ═══════════════════════════════════════════════════════

def get_current_week() -> int:
    if not SCHOOL_CALENDAR.exists():
        return -1
    text = SCHOOL_CALENDAR.read_text("utf-8")
    today = date.today()
    for m in re.finditer(r"第(\d+)周\s*\|\s*(\d{4}-\d{2}-\d{2})\s*至\s*(\d{4}-\d{2}-\d{2})", text):
        week_num = int(m.group(1))
        start = date.fromisoformat(m.group(2))
        end = date.fromisoformat(m.group(3))
        if start <= today <= end:
            return week_num
    return -1


def parse_week_ranges(range_str: str) -> list[tuple[int, int]]:
    ranges = []
    for m in re.finditer(r"第(\d+)-(\d+)周", range_str):
        ranges.append((int(m.group(1)), int(m.group(2))))
    return ranges


def is_week_in_range(week: int, ranges: list[tuple[int, int]]) -> bool:
    return any(start <= week <= end for start, end in ranges)


# ═══════════════════════════════════════════════════════
# 真实活动检测
# ═══════════════════════════════════════════════════════

def detect_activity(target_date: date | None = None) -> dict:
    """扫描真实学习活动信号。target_date=None 表示今天。"""
    if target_date is None:
        target_date = date.today()
    iso = target_date.isoformat()
    result: dict = {
        "courses_active": [],
        "mastery_changes": [],
        "new_mistakes": [],
        "resolved_mistakes": [],
        "new_files": [],
        "inbox_entries": [],
        "commits": [],
        "review_done": False,
        "files_changed": 0,
    }

    # 1. 课程文件修改（用 find -mtime 检测今天修改的课程 md 文件）
    today_start = target_date.strftime("%Y-%m-%d")
    find_out = run_cmd(
        ["find", "courses", "-name", "*.md", "-newermt", today_start],
        cwd=str(REPO)
    )
    active_courses: set[str] = set()
    for line in find_out.splitlines():
        line = line.strip()
        m = re.match(r"courses/([^/]+)/", line)
        if m:
            active_courses.add(m.group(1))
    result["courses_active"] = sorted(active_courses)
    result["files_changed"] = len(find_out.splitlines()) if find_out else 0

    # 2. mastery-tracker 变更（git diff）
    diff_out = run_cmd(
        ["git", "diff", "HEAD", "--", "courses/*/mastery-tracker.md"],
        cwd=str(REPO)
    )
    if diff_out:
        # 提取等级变化：| 技能 | ... | N | ... → | 技能 | ... | M |
        for line in diff_out.splitlines():
            if line.startswith("+") and "|" in line and not line.startswith("+++"):
                cells = [c.strip() for c in line.split("|") if c.strip()]
                if len(cells) >= 4 and re.match(r"\d+", cells[2] if len(cells) > 2 else ""):
                    skill = cells[0].strip("*").strip()
                    level = cells[2]
                    acc = cells[3] if len(cells) > 3 else ""
                    result["mastery_changes"].append(f"{skill}（等级 {level}，正确率 {acc}）")

    # 3. mistakes 变更
    diff_out = run_cmd(
        ["git", "diff", "HEAD", "--", "courses/*/mistakes.md"],
        cwd=str(REPO)
    )
    if diff_out:
        for line in diff_out.splitlines():
            if line.startswith("+") and "###" in line:
                title = line.lstrip("+").strip().lstrip("#").strip()
                result["new_mistakes"].append(title)
            if line.startswith("+") and "是否已复测通过：是" in line:
                result["resolved_mistakes"].append("（已复测通过）")

    # 4. 新建文件（git status 中的 ?? 行）
    status_out = run_cmd(["git", "status", "--porcelain"], cwd=str(REPO))
    for line in status_out.splitlines():
        if line.startswith("??"):
            path = line[3:].strip()
            if path.startswith("courses/") or path.startswith("plan/record/"):
                result["new_files"].append(path)

    # 5. inbox 反馈
    inbox_path = INBOX_DIR / f"{iso}.md"
    if inbox_path.exists():
        text = inbox_path.read_text("utf-8")
        for line in text.splitlines():
            m = re.match(r"-\s+\[\d{2}:\d{2}\]\s+\[(.+?)\]\s+(.+)", line)
            if m:
                result["inbox_entries"].append(f"[{m.group(1)}] {m.group(2)}")

    # 6. git commits
    git_log = run_cmd(
        ["git", "log", f"--since={iso}", "--oneline", "--all"],
        cwd=str(REPO)
    )
    if git_log:
        for line in git_log.splitlines():
            line = line.strip()
            if line:
                # 去掉 git commit hash 前缀，只保留描述
                cleaned = re.sub(r"^[0-9a-f]+\s+", "", line)
                if cleaned:
                    result["commits"].append(cleaned)

    # 7. 复习活动
    if REVIEW_QUEUE.exists():
        try:
            send_log = json.loads((REVIEW_QUEUE.parent / "send_log.json").read_text("utf-8"))
            result["review_done"] = iso in send_log and send_log[iso].get("status") == "sent"
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    return result


def format_activity_summary(activity: dict, prefix: str = "今日") -> list[str]:
    """将活动数据格式化为邮件段落行"""
    lines: list[str] = []
    has_any = False

    if activity["courses_active"]:
        has_any = True
        lines.append(f"  学习了：{', '.join(activity['courses_active'])}")

    if activity["mastery_changes"]:
        has_any = True
        lines.append(f"  技能变化：")
        for mc in activity["mastery_changes"][:5]:
            lines.append(f"    {mc}")

    if activity["new_mistakes"]:
        has_any = True
        lines.append(f"  新增错题 {len(activity['new_mistakes'])} 条：")
        for nm in activity["new_mistakes"][:3]:
            lines.append(f"    {nm}")

    if activity["resolved_mistakes"]:
        has_any = True
        lines.append(f"  已复测通过 {len(activity['resolved_mistakes'])} 条")

    if activity["new_files"]:
        has_any = True
        lines.append(f"  新建内容：{', '.join(activity['new_files'][:3])}")

    if activity["inbox_entries"]:
        has_any = True
        lines.append(f"  反馈记录：")
        for ie in activity["inbox_entries"][:3]:
            lines.append(f"    {ie}")

    if activity["commits"]:
        has_any = True
        lines.append(f"  提交记录：{len(activity['commits'])} 次")
        for c in activity["commits"][:3]:
            lines.append(f"    {c}")

    if activity["review_done"]:
        has_any = True
        lines.append(f"  睡前复习：已完成")

    if not has_any:
        return []

    return [f"【{prefix}活动】"] + lines


# ═══════════════════════════════════════════════════════
# 数据解析
# ═══════════════════════════════════════════════════════

def parse_courses_from_plan() -> tuple[list[str], bool]:
    if not DAILY_PLAN.exists():
        return [], False
    text = DAILY_PLAN.read_text("utf-8")
    in_section = False
    courses: list[str] = []
    for line in text.splitlines():
        if "今日课程时间" in line and line.startswith("#"):
            in_section = True
            continue
        if in_section:
            if line.startswith("#"):
                break
            line_s = line.strip()
            if not line_s:
                continue
            if "无" in line_s and ("停课" in line_s or "无课" in line_s or line_s.startswith("- 无")):
                return [], True
            m = re.match(r"[-*]\s+(\d{2}:\d{2})\s*[-–]\s*(\d{2}:\d{2})\s+(.+)", line_s)
            if m:
                courses.append(f"{m.group(1)}-{m.group(2)} {m.group(3)}")
            elif line_s.startswith("-") and line_s != "-":
                courses.append(line_s.lstrip("- ").strip())
    return courses, False


def parse_timetable_today() -> tuple[list[str], bool]:
    courses, no_class = parse_courses_from_plan()
    if no_class:
        return [], True
    if courses:
        return courses, False
    if not TIMETABLE.exists():
        return [], False
    text = TIMETABLE.read_text("utf-8")
    weekday = today_weekday()
    current_week = get_current_week()
    cancelled_dates: set[str] = set()
    for m in re.finditer(r"(\d{4}-\d{2}-\d{2}).*?停课", text):
        cancelled_dates.add(m.group(1))
    result: list[str] = []
    for line in text.splitlines():
        if not re.match(r"^\d+\.\s", line):
            continue
        if weekday not in line:
            continue
        week_match = re.search(r"第([\d-]+周(?:[、,]第[\d-]+周)*)", line)
        if week_match and current_week > 0:
            week_ranges = parse_week_ranges(week_match.group(1))
            if not is_week_in_range(current_week, week_ranges):
                continue
        today_iso = today_str()
        if today_iso in cancelled_dates:
            course_name_m = re.match(r"^\d+\.\s*(.+?)，", line)
            if course_name_m:
                cname = course_name_m.group(1)
                for dc in cancelled_dates:
                    if cname in text[text.find(dc)-200:text.find(dc)+50]:
                        continue
        m = re.match(r"^\d+\.\s*(.+?)，(.+?)，.+?(\d{2}:\d{2}-\d{2}:\d{2})[，,](.+)", line)
        if m:
            name = m.group(1).strip()
            time_slot = m.group(3).strip()
            room = m.group(4).strip().rstrip("。")
            result.append(f"{time_slot} {name}（{room}）")
    return result, len(result) == 0


def get_available_time() -> str:
    if not DAILY_PLAN.exists():
        return ""
    text = DAILY_PLAN.read_text("utf-8")
    m = re.search(r"\*\*合计约\s*(\d+\.?\d*)\s*小时\*\*", text)
    if m:
        return f"约 {m.group(1)} 小时"
    times = re.findall(r"(\d{2}:\d{2})\s*[-–]\s*(\d{2}:\d{2})", text)
    if times:
        return f"{len(times)} 个时间段"
    return ""


def parse_daily_plan() -> dict:
    result: dict = {"tasks": [], "min_line": [], "review_questions": [], "bonus": []}
    if not DAILY_PLAN.exists():
        return result
    text = DAILY_PLAN.read_text("utf-8")
    lines = text.splitlines()
    current_section = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            current_section = line.lstrip("# ").strip()
            i += 1
            continue
        if line.startswith("#### 任务"):
            task_name = re.sub(r"^####\s*任务\s*\d+[：:]\s*", "", line).strip()
            task: dict = {"name": task_name, "module": "", "time": "", "actions": []}
            i += 1
            while i < len(lines):
                tl = lines[i].strip()
                if tl.startswith("#"):
                    break
                if tl.startswith("对应模块"):
                    task["module"] = tl.split("：", 1)[-1].strip().split("，")[0].strip()
                elif tl.startswith("预计时间"):
                    task["time"] = tl.split("：", 1)[-1].strip()
                elif re.match(r"^\d+\.\s", tl):
                    task["actions"].append(tl)
                i += 1
            result["tasks"].append(task)
            continue
        if "最低" in current_section and "完成" in current_section:
            ls = line.strip()
            if ls and re.match(r"^\d+[.)]\s", ls):
                result["min_line"].append(ls)
        if "复盘" in current_section or "反思" in current_section:
            ls = line.strip()
            if ls and re.match(r"^\d+[.)]\s", ls):
                result["review_questions"].append(ls)
        if "加分" in current_section or "额外" in current_section:
            ls = line.strip()
            if ls and re.match(r"^\d+[.)]\s", ls):
                result["bonus"].append(ls)
        i += 1
    return result


def parse_daily_record_progress() -> dict:
    result: dict = {"tasks": [], "harvest": [], "raw": ""}
    record_path = DAILY_RECORD_DIR / f"{today_str()}.md"
    if not record_path.exists():
        return result
    text = record_path.read_text("utf-8")
    result["raw"] = text
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        cells = [c for c in cells if c]
        if len(cells) < 3 or cells[0] in ("任务", ":---", "---") or all(c.startswith("-") or c.startswith(":") for c in cells):
            continue
        status = "pending"
        sc = cells[2] if len(cells) > 2 else ""
        if "✅" in sc:
            status = "done"
        elif "⚠️" in sc or "部分" in sc:
            status = "partial"
        elif "❌" in sc or "未完成" in sc:
            status = "failed"
        result["tasks"].append({"name": cells[0], "status": status, "notes": cells[-1] if len(cells) > 3 else ""})
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
    if not REVIEW_QUEUE.exists():
        return 0
    try:
        cards = json.loads(REVIEW_QUEUE.read_text("utf-8"))
        today = today_str()
        return sum(1 for c in cards if c.get("next_review", "") <= today)
    except (json.JSONDecodeError, KeyError):
        return 0


def auto_write_daily_record(tasks: list[dict]) -> None:
    record_path = DAILY_RECORD_DIR / f"{today_str()}.md"
    if not record_path.exists():
        return
    text = record_path.read_text("utf-8")
    if "✅" in text or "⚠️" in text or "❌" in text:
        return
    table_lines = ["| 任务 | 对应模块 | 状态 | 备注 |", "|:---|:---|:---:|:---|"]
    for t in tasks:
        module = t.get("module", "-")
        time_str = t.get("time", "")
        note = time_str.split("（")[0].strip() if time_str else ""
        table_lines.append(f"| {t['name']} | {module} | ⬜ 待执行 | {note} |")
    new_table = "\n".join(table_lines)
    text = re.sub(r"\| 任务 \|.*?\n\|:---.*?\n(?:\|.*?\n)*", new_table + "\n", text, flags=re.DOTALL)
    record_path.write_text(text, "utf-8")


# ═══════════════════════════════════════════════════════
# 子命令：autostart
# ═══════════════════════════════════════════════════════

def cmd_autostart(args: argparse.Namespace) -> None:
    today = today_str()
    print(f"[{datetime.now().isoformat()}] 开始自动执行 /start-day ...")
    new_state = {
        "date": today,
        "sent": {"morning": False, "midday": False, "evening": False, "sleep_review": False, "autostart": False},
        "used_encouragements": [], "used_tips": [],
    }
    result = subprocess.run(
        ["claude", "-p", "/start-day 自动生成今日计划", "--dangerously-skip-permissions"],
        cwd=str(REPO), capture_output=True, text=True, timeout=600
    )
    if result.returncode == 0:
        new_state["sent"]["autostart"] = True
        save_state(new_state)
        print("/start-day 执行完成，daily-plan.md 已更新")
    else:
        save_state(new_state)
        print(f"/start-day 执行失败：{result.stderr[:500]}", file=sys.stderr)


# ═══════════════════════════════════════════════════════
# 子命令：morning
# ═══════════════════════════════════════════════════════

def cmd_morning(args: argparse.Namespace) -> None:
    plan = parse_daily_plan()
    courses, no_class = parse_timetable_today()
    due_count = get_review_due_count()
    weekday = today_weekday()
    today = today_str()
    state = load_state()

    lines = [f"早安，Ethen！今天是 {today}（{weekday}）", ""]

    # 昨日回顾（真实活动检测）
    yesterday_activity = detect_activity(date.today() - timedelta(days=1))
    yesterday_summary = format_activity_summary(yesterday_activity, "昨日回顾")
    if yesterday_summary:
        lines.extend(yesterday_summary)
        lines.append("")

    # 今日课程
    lines.append("【今日课程】")
    if no_class:
        avail = get_available_time()
        lines.append(f"  今日无课，全天可用学习时间 {avail}" if avail else "  今日无课，全天可用")
    elif courses:
        for c in courses:
            lines.append(f"  {c}")
    else:
        lines.append("  （未读取到课程信息）")
    lines.append("")

    # 今日三件事
    lines.append("【今日三件事】")
    if plan["tasks"]:
        for i, t in enumerate(plan["tasks"][:3], 1):
            module_tag = f"（{t['module']}）" if t["module"] else ""
            time_tag = f"，{t['time'].split('（')[0].strip()}" if t["time"] else ""
            lines.append(f"  {i}. {t['name']}{module_tag}{time_tag}")
    else:
        lines.append("  （daily-plan.md 中未找到任务，请手动规划今日重点）")
    lines.append("")

    if plan["min_line"]:
        lines.append("【最低完成线】")
        for t in plan["min_line"]:
            lines.append(f"  {t}")
        lines.append("")

    if due_count > 0:
        lines.append(f"【复习提醒】今日有 {due_count} 张卡片到期，睡前复习时处理")
        lines.append("")

    enc, enc_idx = pick_unique(ENCOURAGEMENTS, state.get("used_encouragements", []))
    state.setdefault("used_encouragements", []).append(enc_idx)
    lines.append(f"【今日一句】{enc}")

    body = "\n".join(lines)
    subject = f"[晨间启动] {today} {weekday} 今日三件事"

    if not getattr(args, "dry_run", False):
        if send_email(subject, body, dry_run=False):
            state["sent"]["morning"] = True
            save_state(state)
            if plan["tasks"]:
                auto_write_daily_record(plan["tasks"])
    else:
        send_email(subject, body, dry_run=True)


# ═══════════════════════════════════════════════════════
# 子命令：midday
# ═══════════════════════════════════════════════════════

def cmd_midday(args: argparse.Namespace) -> None:
    plan = parse_daily_plan()
    progress = parse_daily_record_progress()
    activity = detect_activity()
    today = today_str()
    weekday = today_weekday()
    state = load_state()

    lines = [f"午间重置 — {today}（{weekday}）", ""]

    # 上午进度（优先读 daily 记录状态表，fallback 到真实活动检测）
    lines.append("【上午进度】")
    has_progress = False
    if progress["tasks"]:
        done = [t for t in progress["tasks"] if t["status"] == "done"]
        partial = [t for t in progress["tasks"] if t["status"] == "partial"]
        if done or partial:
            has_progress = True
            if done:
                lines.append(f"  已完成 {len(done)} 项：")
                for t in done:
                    lines.append(f"    ✅ {t['name']}")
            if partial:
                lines.append(f"  进行中 {len(partial)} 项：")
                for t in partial:
                    lines.append(f"    ⚠️ {t['name']}")

    if not has_progress:
        # 用真实活动信号
        if activity["courses_active"]:
            lines.append(f"  今天上午你主要在学 {', '.join(activity['courses_active'])}（修改了 {activity['files_changed']} 个文件）")
            if activity["new_files"]:
                lines.append(f"  还新建了：{', '.join(activity['new_files'][:3])}")
            if activity["inbox_entries"]:
                for ie in activity["inbox_entries"][:2]:
                    lines.append(f"  {ie}")
        elif activity["inbox_entries"]:
            lines.append(f"  收到反馈：")
            for ie in activity["inbox_entries"][:3]:
                lines.append(f"    {ie}")
        else:
            lines.append("  上午暂无学习活动记录，下午加油")
    lines.append("")

    # 下午重点（基于真实活动推荐）
    lines.append("【下午重点】")
    afternoon_task = None
    if activity["courses_active"]:
        # 如果上午在学某个课程，建议继续
        active_course = activity["courses_active"][0]
        for t in plan["tasks"]:
            if active_course in t.get("module", "").lower() or active_course in t.get("name", "").lower():
                afternoon_task = t
                break
    if not afternoon_task and plan["tasks"]:
        # 从计划中找下午时间段的任务
        for t in plan["tasks"]:
            if re.search(r"1[3-9]:\d{2}", t.get("time", "")):
                afternoon_task = t
                break
        if not afternoon_task and len(plan["tasks"]) > 2:
            afternoon_task = plan["tasks"][2]
    if afternoon_task:
        module_tag = f"（{afternoon_task['module']}）" if afternoon_task.get("module") else ""
        time_tag = afternoon_task.get("time", "").split("（")[0].strip()
        lines.append(f"  优先处理：{afternoon_task['name']}{module_tag} {time_tag}")
    else:
        lines.append("  按计划继续推进下午的学习任务")
    lines.append("")

    # 休息提醒（分类轮换去重）
    tip, tip_idx = pick_rest_tip(state.get("used_tips", []))
    state.setdefault("used_tips", []).append(tip_idx)
    lines.append("【休息提醒】")
    lines.append(f"  {tip}")

    body = "\n".join(lines)
    subject = f"[午间重置] {today} 下午加油"

    if not getattr(args, "dry_run", False):
        if send_email(subject, body, dry_run=False):
            state["sent"]["midday"] = True
            save_state(state)
    else:
        send_email(subject, body, dry_run=True)


# ═══════════════════════════════════════════════════════
# 子命令：evening
# ═══════════════════════════════════════════════════════

def cmd_evening(args: argparse.Namespace) -> None:
    plan = parse_daily_plan()
    progress = parse_daily_record_progress()
    activity = detect_activity()
    today = today_str()
    weekday = today_weekday()

    lines = [f"晚间复盘 — {today}（{weekday}）", ""]

    # 今日活动总结（真实信号）
    activity_summary = format_activity_summary(activity, "今日")
    if activity_summary:
        lines.extend(activity_summary)
        lines.append("")

    # 任务完成概况（daily 记录状态表）
    if progress["tasks"]:
        done = sum(1 for t in progress["tasks"] if t["status"] == "done")
        total = len(progress["tasks"])
        lines.append(f"【任务完成度】{done}/{total}")
        for t in progress["tasks"]:
            icon = {"done": "✅", "partial": "⚠️", "failed": "❌", "pending": "⏳"}.get(t["status"], "⏳")
            lines.append(f"  {icon} {t['name']}")
    elif activity["courses_active"]:
        lines.append("【任务完成度】检测到学习活动，但任务状态表未更新")
        lines.append("  （可通过 /companion capture 报告进展）")
    lines.append("")

    if progress["harvest"]:
        lines.append("【今日收获】")
        for h in progress["harvest"][:5]:
            lines.append(f"  - {h}")
        lines.append("")

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

    lines.append("【反馈格式】")
    lines.append("  在微信里回复：")
    lines.append("  - 完成：XX课笔记写完了")
    lines.append("  - 卡住：XX概念不理解")
    lines.append("  - 调整：明天先做XX")
    lines.append("  - 心情：感觉不错 / 有点累")
    lines.append("")
    lines.append("  或用 /companion capture \"你的反馈\"")

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
    text = args.text
    today = today_str()
    now = datetime.now().strftime("%H:%M")
    category = "其他"
    keywords = {
        "完成": "已完成", "做完": "已完成", "写完": "已完成", "搞定": "已完成",
        "卡住": "卡住", "不懂": "卡住", "不会": "卡住", "不理解": "卡住",
        "调整": "调整", "改到": "调整", "明天": "调整",
        "心情": "心情", "感觉": "心情", "累": "心情", "不错": "心情",
    }
    for kw, cat in keywords.items():
        if kw in text:
            category = cat
            break
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    inbox_path = INBOX_DIR / f"{today}.md"
    entry = f"- [{now}] [{category}] {text}\n"
    if inbox_path.exists():
        content = inbox_path.read_text("utf-8") + entry
    else:
        content = f"# 微信反馈 — {today}\n\n{entry}"
    inbox_path.write_text(content, "utf-8")
    print(f"已写入 inbox：{inbox_path}")
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
    if category == "调整":
        print("检测到调整类反馈，建议手动更新 daily-plan.md 或使用 /start-day 重新规划")

    # 检测复习反馈，自动调用 review_system.py feedback
    if "复习反馈" in text or re.search(r"=\d", text):
        feedback_text = re.sub(r".*复习反馈[：:]?\s*", "", text)
        if feedback_text and re.search(r"=", feedback_text):
            print(f"检测到复习反馈，自动处理：{feedback_text}")
            result = subprocess.run(
                [sys.executable, str(REVIEW_SCRIPT), "feedback", feedback_text],
                capture_output=True, text=True, cwd=str(REPO)
            )
            print(result.stdout)
            if result.stderr:
                print(result.stderr, file=sys.stderr)


# ═══════════════════════════════════════════════════════
# 子命令：update-schedule
# ═══════════════════════════════════════════════════════

def cmd_update_schedule(args: argparse.Namespace) -> None:
    text = args.text
    today = date.today()
    date_m = re.search(r"(\d{1,2})/(\d{1,2})", text)
    if not date_m:
        print("无法解析日期，请使用格式如 '5/20'", file=sys.stderr)
        return
    month, day = int(date_m.group(1)), int(date_m.group(2))
    change_date = date(today.year, month, day)
    week_num = -1
    if SCHOOL_CALENDAR.exists():
        cal = SCHOOL_CALENDAR.read_text("utf-8")
        for m in re.finditer(r"第(\d+)周\s*\|\s*(\d{4}-\d{2}-\d{2})\s*至\s*(\d{4}-\d{2}-\d{2})", cal):
            start = date.fromisoformat(m.group(2))
            end = date.fromisoformat(m.group(3))
            if start <= change_date <= end:
                week_num = int(m.group(1))
                break
    weekday_name = WEEKDAYS[change_date.weekday()]
    is_cancel = "停课" in text or "取消" in text
    course_m = re.match(r"(.+?)\s+\d{1,2}/\d{1,2}", text)
    course_name = course_m.group(1).strip() if course_m else "未知课程"
    week_tag = f"（第{week_num}周{weekday_name}）" if week_num > 0 else f"（{change_date.isoformat()} {weekday_name}）"
    record = f"- {course_name}，{change_date.isoformat()}{week_tag}"
    if is_cancel and "补" in text:
        makeup_m = re.search(r"补[到至]?\s*(\d{1,2}/\d{1,2})\s*(.+)", text)
        if makeup_m:
            md2 = int(makeup_m.group(1).split("/")[0]), int(makeup_m.group(1).split("/")[1])
            makeup_date = date(today.year, md2[0], md2[1])
            makeup_wday = WEEKDAYS[makeup_date.weekday()]
            extra = makeup_m.group(2).strip()
            record += f"停课一次；补至 {makeup_date.isoformat()}（{makeup_wday}）{extra}"
        else:
            record += "停课一次"
    elif is_cancel:
        record += "停课一次"
    if TIMETABLE.exists():
        text_content = TIMETABLE.read_text("utf-8")
        if record not in text_content:
            if "临时调课" in text_content:
                lines = text_content.rstrip().split("\n")
                insert_idx = len(lines)
                for j in range(len(lines) - 1, -1, -1):
                    if lines[j].strip().startswith("-") and j > text_content.index("临时调课"):
                        insert_idx = j + 1
                        break
                lines.insert(insert_idx, record)
                text_content = "\n".join(lines) + "\n"
            else:
                text_content += f"\n\n临时调课：\n{record}\n"
            TIMETABLE.write_text(text_content, "utf-8")
            print(f"已更新 timetable.md 临时调课记录：\n  {record}")
        else:
            print("该记录已存在，无需重复添加")


# ═══════════════════════════════════════════════════════
# 子命令：status
# ═══════════════════════════════════════════════════════

def cmd_status(args: argparse.Namespace) -> None:
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
            cmd_autostart(argparse.Namespace())
            state = load_state()
        elif slot == "sleep_review":
            result = subprocess.run(
                [sys.executable, str(REVIEW_SCRIPT), "tick"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                state["sent"]["sleep_review"] = True
                print("睡前复习已委托 review_system.py 处理")
            else:
                print(f"review_system.py tick 失败：{result.stderr}", file=sys.stderr)
        else:
            SLOT_COMMANDS[slot](argparse.Namespace(dry_run=False))
        save_state(state)
        return  # 每轮只处理一个 slot，防止重复发送


# ═══════════════════════════════════════════════════════
# 主入口
# ═══════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(description="学习伴侣系统")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("autostart", help="凌晨自动运行 /start-day")
    p_morning = sub.add_parser("morning", help="晨间启动")
    p_morning.add_argument("--dry-run", action="store_true")
    p_midday = sub.add_parser("midday", help="午间重置")
    p_midday.add_argument("--dry-run", action="store_true")
    p_evening = sub.add_parser("evening", help="晚间复盘")
    p_evening.add_argument("--dry-run", action="store_true")
    p_capture = sub.add_parser("capture", help="捕获微信反馈")
    p_capture.add_argument("text", help="反馈文本")
    p_capture.add_argument("--dry-run", action="store_true")
    p_update = sub.add_parser("update-schedule", help="更新课表临时调课")
    p_update.add_argument("text", help="调课描述")
    sub.add_parser("status", help="查看系统状态")
    sub.add_parser("tick", help="定时检查并自动执行")
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    {
        "autostart": cmd_autostart, "morning": cmd_morning,
        "midday": cmd_midday, "evening": cmd_evening,
        "capture": cmd_capture, "update-schedule": cmd_update_schedule,
        "status": cmd_status, "tick": cmd_tick,
    }[args.command](args)


if __name__ == "__main__":
    main()
