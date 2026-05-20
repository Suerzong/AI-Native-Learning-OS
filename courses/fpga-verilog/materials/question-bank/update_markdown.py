#!/usr/bin/env python3
"""将生成的答案整合到 Markdown 文件中。"""
import json

data = json.load(open("/home/ubuntu/Edge-AI/temp/zzfpga-question-bank/raw_data.json", encoding="utf-8"))
answers = json.load(open("/home/ubuntu/Edge-AI/temp/zzfpga-question-bank/answers.json", encoding="utf-8"))

# 按类型分组
groups = {"choice": [], "judge": [], "code": [], "hardware": []}
for q in data:
    t = q.get("type", "code")
    if t in groups: groups[t].append(q)
    else: groups["code"].append(q)

DIFF = {"easy": "简单", "medium": "中等", "difficult": "困难"}
TYPE = {("choice","multiple"): "多选题", ("choice","single"): "单选题",
        ("judge",None): "判断题", ("code",None): "编程题", ("hardware",None): "硬件题"}

from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d %H:%M")
stats = {k: len(v) for k, v in groups.items()}
total = sum(stats.values())

md = []
md.append("# F学社 FPGA 题库")
md.append(f"> 共 {total} 道题目（选择题 {stats['choice']}，判断题 {stats['judge']}，"
          f"编程题 {stats['code']}，硬件题 {stats['hardware']}）")
md.append(f"> 数据来源: https://www.zzfpga.com/StudentPlatform/Sheet/QuestionBank")
md.append(f"> 抓取时间: {now}")
md.append("")
md.append("---")
md.append("")

CN = ["一", "二", "三", "四"]
sections = [("选择题", "choice"), ("判断题", "judge"), ("编程题", "code"), ("硬件题", "hardware")]
num = 0

for idx, (sec_name, qtype) in enumerate(sections):
    items = groups[qtype]
    if not items: continue

    md.append(f"## {CN[idx]}、{sec_name} ({len(items)} 道)")
    md.append("")

    for q in items:
        num += 1
        detail = q.get("detail")
        title = q.get("title", "未知")
        diff = DIFF.get(q.get("difficulty",""), "未知")

        if not detail:
            md.append(f"### {num}. {title}")
            md.append(f"*（详情获取失败）*")
            md.append("")
            md.append("---")
            md.append("")
            continue

        if qtype == "choice":
            ctype = TYPE.get(("choice", detail.get("type","single")), "选择题")
            tags = ", ".join(t.get("value","") for t in (q.get("tagList") or []))
            cats = ", ".join(c.get("name","") for c in (q.get("categoryList") or []))

            md.append(f"### {num}. {title}")
            md.append(f"- **类型**: {ctype}　**难度**: {diff}")
            if cats: md.append(f"- **分类**: {cats}")
            if tags: md.append(f"- **标签**: {tags}")
            md.append("")

            qc = detail.get("questionContent", "")
            if qc: md.append(qc); md.append("")

            labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for j, opt in enumerate(detail.get("optionContent") or []):
                lbl = labels[j] if j < len(labels) else str(j+1)
                marker = " **[正确]**" if opt.get("isAnswer") else ""
                md.append(f"{lbl}. {opt.get('content','')}{marker}")

        elif qtype == "judge":
            md.append(f"### {num}. {title}")
            md.append(f"- **类型**: 判断题　**难度**: {diff}")
            md.append("")
            qc = detail.get("questionContent", "")
            if qc: md.append(qc); md.append("")
            ic = detail.get("isCorrect")
            if ic is not None:
                md.append(f"**答案**: {'正确' if ic else '错误'}")

        else:  # code, hardware
            tlabel = "硬件题" if qtype == "hardware" else "编程题"
            tags = ", ".join(t.get("value","") for t in (q.get("tagList") or []))
            cats = ", ".join(c.get("name","") for c in (q.get("categoryList") or []))

            md.append(f"### {num}. {title}")
            md.append(f"- **类型**: {tlabel}　**难度**: {diff}")
            if cats: md.append(f"- **分类**: {cats}")
            if tags: md.append(f"- **标签**: {tags}")
            md.append("")

            # 参考答案
            qid = str(q["questionID"])
            answer = answers.get(qid, "")
            if answer:
                md.append("**参考答案**:")
                md.append("")
                md.append("```verilog")
                md.append(answer.strip())
                md.append("```")
            else:
                md.append("**参考答案**: 暂无")

        md.append("")
        md.append("---")
        md.append("")

result = "\n".join(md)
out_path = "/home/ubuntu/Edge-AI/temp/zzfpga-question-bank/fpga-question-bank.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(result)

print(f"Done! {num} questions, {len(result)} bytes")
