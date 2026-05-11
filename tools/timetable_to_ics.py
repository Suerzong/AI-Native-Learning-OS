"""
课表转 ICS 工具 — 将 timetable.md 中的课程信息生成 .ics 日历文件。
用法：python tools/timetable_to_ics.py [--output path/to/output.ics]
"""

import argparse
import hashlib
from datetime import datetime, timedelta
from pathlib import Path

# ── 校历信息 ──────────────────────────────────────────────
# 第1周的周一日期
SEMESTER_START_MONDAY = datetime(2026, 3, 2)

# 节次 → (start_h, start_m, end_h, end_m)
PERIOD_TIMES = {
    1:  (8, 0,  8, 45),
    2:  (8, 50, 9, 35),
    3:  (9, 50, 10, 35),
    4:  (10, 40, 11, 25),
    5:  (11, 30, 12, 15),
    6:  (13, 0,  13, 45),
    7:  (13, 50, 14, 35),
    8:  (14, 45, 15, 30),
    9:  (15, 40, 16, 25),
    10: (16, 35, 17, 20),
    11: (17, 25, 18, 10),
    12: (18, 30, 19, 15),
    13: (19, 20, 20, 5),
    14: (20, 10, 20, 55),
}

# 星期几映射：周一=0 ... 周日=6
WEEKDAY_MAP = {"周一": 0, "周二": 1, "周三": 2, "周四": 3, "周五": 4, "周六": 5, "周日": 6}

# ── 课程数据 ──────────────────────────────────────────────
# (课程名, 教师, 周次列表, 星期, 节次元组, 教室)
COURSES = [
    ("数据结构与算法",           "刘娜",   list(range(1, 11)) + list(range(13, 19)), "周一", (1, 2),    "教学实验综合楼-N113"),
    ("大学物理E（上）",          "韩兴杰", list(range(1, 11)) + list(range(13, 19)), "周一", (3, 4),    "教学实验综合楼-N207"),
    ("电子测量与电子电路实验Ⅰ",  "张轶",   list(range(5, 9)),                       "周一", (6, 7, 8), "工程实验楼-209"),
    ("初级项目课",               "徐正山", list(range(9, 11)) + list(range(13, 19)),  "周一", (6, 7, 8), "工程实验楼-202"),
    ("电路辅助设计与仿真",       "俎云霄", list(range(1, 9)),                        "周一", (9, 10),   "教学实验综合楼-N209"),
    ("领导力与可持续发展",       "刘丹",   list(range(9, 11)) + list(range(13, 19)),  "周一", (10, 11),  "教学实验综合楼-N207"),
    ("公众英语表达与沟通(03)",   "李颖",   list(range(1, 11)) + list(range(13, 19)), "周二", (1, 2),    "智慧教学楼-109"),
    ("人工智能引论 A",           "刘巧莉", list(range(1, 11)) + list(range(13, 19)), "周二", (3, 4),    "智慧教学楼-406"),
    ("中国近现代史纲要",         "李晶",   list(range(1, 11)) + list(range(13, 17)), "周二", (9, 10, 11),"教学实验综合楼-N103"),
    ("中国写意画创作",           "郭艺涵", list(range(1, 17)),                       "周二", (13, 14),  "智慧教学楼-206"),
    ("形势与政策2",              "尚晨光", list(range(7, 10)),                        "周三", (1, 2),    "教学实验综合楼-N118"),
    ("电路分析基础",             "张勇",   list(range(1, 10)) + list(range(12, 19)), "周三", (3, 4),    "智慧教学楼-110"),
    ("数学分析(下)",             "江彦",   list(range(1, 10)) + list(range(12, 19)), "周三", (6, 7, 8), "教学实验综合楼-N108"),
    ("大学物理E（上）",          "韩兴杰", list(range(1, 10)) + list(range(12, 19)), "周四", (1, 2),    "教学实验综合楼-N111"),
    ("社会主义发展史",           "张传泉", list(range(1, 9)),                        "周四", (6, 7),    "教学实验综合楼-N119"),
    ("国家安全教育（下）",       "管晓婧", list(range(4, 8)),                         "周四", (10, 11),  "教学实验综合楼-N209"),
    ("数学分析(下)",             "江彦",   list(range(1, 10)) + list(range(12, 19)), "周五", (3, 4, 5), "教学实验综合楼-N206"),
]


def week_to_date(week_num: int, weekday: int) -> datetime:
    """将周次+星期几转换为具体日期。"""
    return SEMESTER_START_MONDAY + timedelta(weeks=week_num - 1, days=weekday)


def make_uid(course_name: str, date: datetime, periods: tuple) -> str:
    """生成唯一的事件 UID。"""
    raw = f"{course_name}-{date.strftime('%Y%m%d')}-{periods}"
    return hashlib.md5(raw.encode()).hexdigest() + "@bupt-edge-ai"


def format_period_label(periods: tuple) -> str:
    """格式化节次标签，如 第1-2节 或 第6-8节。"""
    return f"第{min(periods)}-{max(periods)}节"


def escape_ics(text: str) -> str:
    """转义 ICS 特殊字符。"""
    return text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def fold_line(line: str) -> str:
    """RFC 5545 行折叠：每行不超过 75 字节。"""
    result = []
    encoded = line.encode("utf-8")
    while len(encoded) > 75:
        # 找一个不超过 75 字节的切割点（不截断多字节字符）
        cut = 75
        while cut > 0 and (encoded[cut] & 0xC0) == 0x80:
            cut -= 1
        result.append(encoded[:cut].decode("utf-8"))
        encoded = encoded[cut:]
    result.append(encoded.decode("utf-8"))
    return "\r\n ".join(result)


def generate_ics(courses: list) -> str:
    """生成完整的 ICS 文件内容。"""
    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//BUPTEdgeAI//Timetable//CN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:BUPT 2026春季课表 - 宋恩泽",
        "X-WR-TIMEZONE:Asia/Shanghai",
    ]

    for name, teacher, weeks, weekday_str, periods, location in courses:
        weekday = WEEKDAY_MAP[weekday_str]
        first_period = min(periods)
        last_period = max(periods)
        sh, sm, _, _ = PERIOD_TIMES[first_period]
        _, _, eh, em = PERIOD_TIMES[last_period]

        for week in weeks:
            date = week_to_date(week, weekday)
            dt_start = date.replace(hour=sh, minute=sm)
            dt_end = date.replace(hour=eh, minute=em)

            # 转换为 UTC（北京 = UTC+8，无夏令时）
            dt_start_utc = dt_start - timedelta(hours=8)
            dt_end_utc = dt_end - timedelta(hours=8)

            summary = escape_ics(f"{name} ({format_period_label(periods)})")
            description = escape_ics(
                f"教师：{teacher}\\n"
                f"周次：第{week}周\\n"
                f"节次：{format_period_label(periods)}\\n"
                f"教室：{location}"
            )

            lines.append("BEGIN:VEVENT")
            lines.append(fold_line(f"UID:{make_uid(name, date, periods)}"))
            lines.append(f"DTSTAMP:{now}")
            lines.append(f"DTSTART:{dt_start_utc.strftime('%Y%m%dT%H%M%SZ')}")
            lines.append(f"DTEND:{dt_end_utc.strftime('%Y%m%dT%H%M%SZ')}")
            lines.append(fold_line(f"SUMMARY:{summary}"))
            lines.append(fold_line(f"DESCRIPTION:{description}"))
            lines.append(fold_line(f"LOCATION:{escape_ics(location)}"))
            lines.append(f"STATUS:CONFIRMED")
            lines.append("END:VEVENT")

    lines.append("END:VCALENDAR")
    return "\r\n".join(lines) + "\r\n"


def main():
    parser = argparse.ArgumentParser(description="课表转 ICS 工具")
    parser.add_argument("--output", "-o", default="tools/bupt_2026_spring_timetable.ics",
                        help="输出 ICS 文件路径")
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    ics_content = generate_ics(COURSES)
    output_path.write_text(ics_content, encoding="utf-8")

    # 统计
    total_events = sum(len(c[2]) for c in COURSES)
    print(f"Done! ICS file: {output_path}")
    print(f"  Courses: {len(COURSES)}  |  Events: {total_events}")
    print(f"  Semester: 2026-03-02 ~ 2026-07-19")
    print(f"  Note: courses without fixed schedule are excluded.")


if __name__ == "__main__":
    main()
