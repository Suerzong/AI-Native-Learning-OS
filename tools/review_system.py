#!/usr/bin/env python3
"""
睡前复习与遗忘曲线系统

子命令：
  ingest   — 从 mastery-tracker / mistakes / daily 复盘收集知识卡片
  generate — 生成当天 15 分钟复习报告
  send     — 通过邮件发送复习报告（自动提醒走 Outlook）
  tick     — 定时检查是否到达配置时间，避免重复发送
  set-time — 调整睡前推送时间
  status   — 查看下一次推送时间、到期卡片数、最近发送状态
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
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

# ── 默认配置 ──────────────────────────────────────────
DEFAULT_CONFIG = {
    "send_time": "23:00",
    "timezone": "Asia/Shanghai",
    "intensity": "standard",
    "enabled": True,
}

# ── 间隔复习天数（类艾宾浩斯）────────────────────────
INTERVALS = [0, 1, 3, 7, 14, 30]


# ═══════════════════════════════════════════════════════
# 数据模型
# ═══════════════════════════════════════════════════════

@dataclass
class ReviewCard:
    source: str          # mastery-tracker | mistakes | daily
    course: str          # 课程名
    module: str          # 技能/章节/模块
    content: str         # 知识点内容
    weakness: str = ""   # 主要弱点
    corrective: str = "" # 纠正任务（错题专用）
    retested: bool = False
    accuracy: str = "-"  # 正确率
    last_test: str = ""  # 最近测试日期 YYYY-MM-DD
    interval_idx: int = 0
    next_review: str = "" # YYYY-MM-DD
    review_count: int = 0
    added_date: str = ""

    @property
    def priority(self) -> int:
        """数字越小优先级越高"""
        # 错题未复测通过 → 最高
        if self.source == "mistakes" and not self.retested:
            return 0
        # 正确率低于 80%
        acc = self._parse_accuracy()
        if acc is not None and acc < 80:
            return 1
        # 新加入（间隔 idx 0-1）
        if self.interval_idx <= 1:
            return 2
        # 长期巩固
        return 3

    def _parse_accuracy(self) -> Optional[float]:
        if not self.accuracy or self.accuracy == "-":
            return None
        m = re.search(r"(\d+)", self.accuracy)
        return float(m.group(1)) if m else None


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


# ═══════════════════════════════════════════════════════
# 解析器
# ═══════════════════════════════════════════════════════

def parse_mastery_tracker(path: Path, course: str) -> list[ReviewCard]:
    """解析 mastery-tracker.md 中的表格行"""
    cards: list[ReviewCard] = []
    if not path.exists():
        return cards

    text = path.read_text("utf-8")
    current_section = ""

    for line in text.splitlines():
        # 检测章节标题
        if line.startswith("## "):
            current_section = line.lstrip("# ").strip()
            continue

        # 解析表格行（跳过表头和分隔线）
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        cells = [c for c in cells if c]  # 去掉首尾空串
        if len(cells) < 7:
            continue
        if cells[0] in ("技能", "---", ":---", ":---:"):
            continue
        # 跳过分隔行
        if all(c.startswith("-") or c.startswith(":") for c in cells):
            continue

        skill = cells[0].strip("*").strip()
        chapter = cells[1]
        level = cells[2]
        accuracy = cells[3]
        last_test = cells[4]
        weakness = cells[5]
        pushed = cells[6]

        # 只收集已开始学习的（等级 >= 1）
        try:
            if int(level) < 1:
                continue
        except ValueError:
            continue

        cards.append(ReviewCard(
            source="mastery-tracker",
            course=course,
            module=skill,
            content=f"{skill}（{current_section}，章节 {chapter}）",
            weakness=weakness,
            accuracy=accuracy,
            last_test=last_test,
            added_date=last_test or today_str(),
        ))

    return cards


def parse_mistakes(path: Path, course: str) -> list[ReviewCard]:
    """解析 mistakes.md 中的错题条目"""
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

        # 跳过模板占位符和空条目
        if not error and not correct:
            continue
        if re.search(r"\[日期\]|#编号|\[编号\]", title):
            continue

        cards.append(ReviewCard(
            source="mistakes",
            course=course,
            module=skill or title,
            content=f"错题：{title}\n错误：{error}\n正确：{correct}",
            weakness=error,
            corrective=task,
            retested=retested,
            added_date=today_str(),
        ))

    return cards


def _extract_field(text: str, field_name: str) -> str:
    m = re.search(rf"{field_name}[：:]\s*(.+)", text)
    return m.group(1).strip() if m else ""


def parse_daily_record(path: Path) -> list[str]:
    """从每日复盘中提取学习收获条目"""
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


# ═══════════════════════════════════════════════════════
# 子命令：ingest
# ═══════════════════════════════════════════════════════

def cmd_ingest(args: argparse.Namespace) -> None:
    """从数据源收集卡片，合并到 queue.json"""
    existing = load_queue()
    existing_keys = {card_key(c) for c in existing}
    new_cards: list[ReviewCard] = []

    # 1. 扫描所有课程的 mastery-tracker.md
    if COURSES_DIR.exists():
        for course_dir in sorted(COURSES_DIR.iterdir()):
            if not course_dir.is_dir():
                continue
            course = course_dir.name
            mt = course_dir / "mastery-tracker.md"
            new_cards.extend(parse_mastery_tracker(mt, course))

            mk = course_dir / "mistakes.md"
            new_cards.extend(parse_mistakes(mk, course))

    # 2. 扫描最近 3 天的 daily 复盘
    today = date.today()
    for i in range(3):
        d = today - timedelta(days=i)
        dp = DAILY_RECORD_DIR / f"{d.isoformat()}.md"
        harvests = parse_daily_record(dp)
        for h in harvests:
            card = ReviewCard(
                source="daily",
                course="daily-review",
                module=h[:30],
                content=h,
                added_date=d.isoformat(),
            )
            new_cards.append(card)

    # 3. 合并：新卡片追加，已有卡片更新 accuracy / retested
    merged_keys = {card_key(c) for c in existing}
    added = 0
    updated = 0

    for nc in new_cards:
        key = card_key(nc.__dict__) if isinstance(nc, ReviewCard) else card_key(nc)
        nc_dict = asdict(nc) if isinstance(nc, ReviewCard) else nc
        key = card_key(nc_dict)

        if key not in merged_keys:
            # 新卡片：设置 next_review 为今天
            nc_dict["next_review"] = nc_dict.get("last_test") or today_str()
            existing.append(nc_dict)
            merged_keys.add(key)
            added += 1
        else:
            # 已有：更新 accuracy、retested、weakness
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
# 子命令：generate
# ═══════════════════════════════════════════════════════

def cmd_generate(args: argparse.Namespace) -> str:
    """生成复习报告"""
    cards = load_queue()
    today = today_str()
    cfg = load_config()

    # 筛选今天到期的卡片
    due: list[dict] = []
    for c in cards:
        nr = c.get("next_review", "")
        if nr and nr <= today:
            due.append(c)

    # 如果到期不足 5 张，补充即将到期的（3 天内）
    if len(due) < 5:
        soon = date.today() + timedelta(days=3)
        for c in cards:
            nr = c.get("next_review", "")
            if nr and today < nr <= soon.isoformat() and c not in due:
                due.append(c)

    # 按优先级排序
    def sort_key(c: dict) -> tuple:
        # 未复测错题最优先
        is_unretested = 1 if (c.get("source") == "mistakes" and not c.get("retested")) else 0
        # 低正确率
        acc_str = c.get("accuracy", "-")
        acc_val = 100
        m = re.search(r"(\d+)", acc_str) if acc_str else None
        if m:
            acc_val = int(m.group(1))
        # 间隔索引
        idx = c.get("interval_idx", 0)
        return (0 if is_unretested else 1, acc_val, idx)

    due.sort(key=sort_key)

    # 限制 5-8 张（标准强度）
    limit = 8 if cfg.get("intensity") == "standard" else 5
    selected = due[:limit]

    # 生成报告
    lines = [
        "# 睡前复习报告",
        f"日期：{today}",
        f"到期卡片：{len(due)} 张（展示前 {len(selected)} 张）",
        "",
    ]

    # 今日新知识点（限制最多 10 条）
    new_today = [c for c in cards if c.get("added_date") == today]
    if new_today:
        lines.append("## 今日新进入复习系统的知识点")
        for c in new_today[:10]:
            lines.append(f"- [{c.get('course')}] {c.get('module')}：{c.get('content', '')[:60]}")
        lines.append("")

    # 到期复习卡片
    lines.append("## 今日到期复习")
    for i, c in enumerate(selected, 1):
        source_tag = "⚠️错题" if c.get("source") == "mistakes" else ""
        acc_tag = f"正确率 {c.get('accuracy', '-')}" if c.get("accuracy", "-") != "-" else ""
        tags = " | ".join(filter(None, [source_tag, acc_tag]))
        lines.append(f"### {i}. [{c.get('course')}] {c.get('module')} {tags}")
        lines.append(f"内容：{c.get('content', '')[:120]}")
        if c.get("weakness"):
            lines.append(f"弱点：{c.get('weakness', '')[:80]}")
        if c.get("corrective"):
            lines.append(f"纠正任务：{c.get('corrective', '')[:80]}")
        lines.append("")

    # 错题/误区回炉
    mistake_due = [c for c in selected if c.get("source") == "mistakes" and not c.get("retested")]
    if mistake_due:
        lines.append("## 错题回炉")
        for c in mistake_due:
            lines.append(f"- [{c.get('course')}] {c.get('module')}")
            lines.append(f"  任务：{c.get('corrective', '重做相关练习')[:80]}")
        lines.append("")

    # 主动回忆问题
    lines.append("## 主动回忆问题")
    recall_qs = _generate_recall_questions(selected)
    for i, q in enumerate(recall_qs, 1):
        lines.append(f"{i}. {q}")
    lines.append("")

    # 明日提醒
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    upcoming = [c for c in cards if c.get("next_review", "") == tomorrow]
    if upcoming:
        lines.append("## 明日继续")
        for c in upcoming[:5]:
            lines.append(f"- [{c.get('course')}] {c.get('module')}")
    else:
        lines.append("## 明日继续")
        lines.append("- 明天暂无新到期卡片，继续保持学习节奏")
    lines.append("")

    # 反馈格式
    lines.append("## 复习反馈")
    lines.append("完成复习后请回复格式：`复习反馈：知识点=评分，知识点=评分`")
    lines.append("评分标准：1=完全忘了，2=模糊，3=基本记得，4=清晰")

    report = "\n".join(lines)

    # 保存归档
    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    archive = DAILY_DIR / f"{today}.md"
    archive.write_text(report, "utf-8")
    print(f"报告已生成并归档：{archive}")

    if args.output:
        print(report)

    return report


def _generate_recall_questions(cards: list[dict]) -> list[str]:
    """根据卡片内容生成主动回忆问题"""
    qs: list[str] = []
    templates = {
        "neural-networks": [
            "用一句话解释 {0} 的核心思想",
            "{0} 的关键公式/结构是什么？",
            "{0} 在实际应用中解决什么问题？",
        ],
        "data-structures": [
            "{0} 的时间复杂度是多少？",
            "手写 {0} 的核心操作伪代码",
            "{0} 和类似结构的关键区别是什么？",
        ],
        "default": [
            "用自己的话解释 {0}",
            "{0} 的核心要点是什么？",
            "{0} 的常见误区有哪些？",
        ],
    }

    for c in cards[:5]:
        course = c.get("course", "default")
        module = c.get("module", "这个知识点")
        tpl = templates.get(course, templates["default"])
        q = tpl[hash(module) % len(tpl)].format(module)
        qs.append(q)

    if not qs:
        qs.append("回顾今天复习的内容，哪些还不太确定？")

    return qs


# ═══════════════════════════════════════════════════════
# 子命令：send
# ═══════════════════════════════════════════════════════

def cmd_send(args: argparse.Namespace) -> None:
    """发送复习报告"""
    today = today_str()
    archive = DAILY_DIR / f"{today}.md"

    if not archive.exists():
        print("今日报告尚未生成，先运行 generate")
        return

    report = archive.read_text("utf-8")

    # 去掉 markdown 标记，保留纯文本用于邮件
    plain = _md_to_plain(report)

    subject = f"[睡前复习] {today} 复习报告"

    if args.dry_run:
        print(f"[dry-run] 将发送邮件：{subject}")
        print(f"[dry-run] 收件人：Suerzong@outlook.com")
        print(f"[dry-run] 正文前 500 字：\n{plain[:500]}")
        return

    # 调用 email_push.py
    cmd = [
        sys.executable, str(EMAIL_SCRIPT),
        "--subject", subject,
        "--body", plain,
    ]
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
    """将 markdown 转为纯文本"""
    text = re.sub(r"^#{1,3}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    return text.strip()


# ═══════════════════════════════════════════════════════
# 子命令：tick
# ═══════════════════════════════════════════════════════

def cmd_tick(args: argparse.Namespace) -> None:
    """定时检查：如果到达发送时间且今天尚未发送，则执行 ingest → generate → send"""
    cfg = load_config()

    if not cfg.get("enabled", True):
        return

    send_time = cfg.get("send_time", "23:00")
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    # 检查是否在发送时间的 5 分钟窗口内
    send_h, send_m = map(int, send_time.split(":"))
    send_minutes = send_h * 60 + send_m
    current_minutes = now.hour * 60 + now.minute

    if abs(current_minutes - send_minutes) > 5:
        return

    # 检查今天是否已发送
    log = load_send_log()
    today = today_str()
    if today in log and log[today].get("status") == "sent":
        return

    print(f"[{now.isoformat()}] 到达发送时间 {send_time}，开始执行复习流程...")

    # 执行完整流程
    cmd_ingest(args)
    cmd_generate(argparse.Namespace(output=False))
    cmd_send(argparse.Namespace(dry_run=False))


# ═══════════════════════════════════════════════════════
# 子命令：set-time
# ═══════════════════════════════════════════════════════

def cmd_set_time(args: argparse.Namespace) -> None:
    """调整推送时间"""
    new_time = args.time
    # 验证格式
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
    """查看系统状态"""
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

    # 到期卡片
    due = [c for c in cards if c.get("next_review", "") <= today]
    print(f"队列卡片总数：{len(cards)}")
    print(f"今日到期：{len(due)} 张")

    # 未复测错题
    unretested = [c for c in cards if c.get("source") == "mistakes" and not c.get("retested")]
    print(f"未复测错题：{len(unretested)} 张")
    print()

    # 最近发送状态
    if today in log:
        entry = log[today]
        print(f"今日发送状态：{entry.get('status', '未知')}")
        print(f"发送时间：{entry.get('time', '-')}")
    else:
        print("今日尚未发送")

    # 最近 7 天发送记录
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

    # ingest
    sub.add_parser("ingest", help="从数据源收集知识卡片")

    # generate
    p_gen = sub.add_parser("generate", help="生成复习报告")
    p_gen.add_argument("--output", action="store_true", help="打印报告到终端")

    # send
    p_send = sub.add_parser("send", help="发送复习报告")
    p_send.add_argument("--dry-run", action="store_true", help="只打印不发送")

    # tick
    sub.add_parser("tick", help="定时检查并自动执行")

    # set-time
    p_time = sub.add_parser("set-time", help="调整推送时间")
    p_time.add_argument("time", help="HH:MM 格式")

    # status
    sub.add_parser("status", help="查看系统状态")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    {
        "ingest": cmd_ingest,
        "generate": cmd_generate,
        "send": cmd_send,
        "tick": cmd_tick,
        "set-time": cmd_set_time,
        "status": cmd_status,
    }[args.command](args)


if __name__ == "__main__":
    main()
