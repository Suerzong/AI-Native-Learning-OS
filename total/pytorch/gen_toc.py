#!/usr/bin/env python3
"""为 PyTorch完整教程.md 生成带锚点跳转的目录"""
import re

PATH = r"c:\Users\sez18\Desktop\pytorch\pytorch-pages\PyTorch完整教程.md"

with open(PATH, "r", encoding="utf-8") as f:
    text = f.read()
    lines = text.split('\n')

# 跳过代码块，提取真正的标题
in_code = False
headings = []  # (line_index, level, text)

for i, line in enumerate(lines):
    if line.strip().startswith('```'):
        in_code = not in_code
        continue
    if in_code:
        continue
    m = re.match(r'^(#{1,3})\s+(.+)', line.strip())
    if not m:
        continue
    level = len(m.group(1))
    title = m.group(2).strip()
    # 跳过文件标题和目录本身
    if title in ('PyTorch 完整教程', '目录'):
        continue
    # 跳过代码注释风格的（如 "# 最新稳定版本" 这种缩进后的）
    if level == 1 and i > 10:
        # 检查这行是否在代码块附近 — 如果前几行有未关闭的 ``` 就跳过
        pass
    headings.append((i, level, title))

# 生成 anchor 的函数
def make_anchor(title):
    a = title.lower()
    a = re.sub(r'[（(）)、，,：:。.！!？?/\\"\'「」『』【】\[\]<>]', '', a)
    a = re.sub(r'\s+', '-', a)
    a = a.strip('-')
    return a

# 只保留 level 1 和 level 2
chapters = []
current = None

for idx, level, title in headings:
    if level == 1:
        current = {"title": title, "anchor": make_anchor(title), "subs": [], "line": idx}
        chapters.append(current)
    elif level == 2 and current is not None:
        # 跳过 "实例" 这种纯代码示例标题
        if title == '实例':
            continue
        current["subs"].append((title, make_anchor(title), idx))

# 生成 TOC
toc = []
toc.append("# PyTorch 完整教程\n")
toc.append("> 来源：[菜鸟教程 PyTorch](https://www.runoob.com/pytorch/pytorch-tutorial.html)\n")
toc.append("## 目录\n")

for i, ch in enumerate(chapters, 1):
    toc.append(f"{i}. [{ch['title']}](#{ch['anchor']})")
    for j, (st, sa, _) in enumerate(ch['subs'], 1):
        toc.append(f"   - [{st}](#{sa})")

toc.append("")
toc.append("---")
toc.append("")

toc_str = '\n'.join(toc)

# 定位旧目录区域：从第1行 "# PyTorch 完整教程" 到第一个章节分隔 "---" 后
# 找到第二个 "---"（旧目录结束）
dash_positions = []
for i, line in enumerate(lines):
    if line.strip() == '---':
        dash_positions.append(i)

if len(dash_positions) >= 2:
    old_end = dash_positions[1] + 1  # 第二个 --- 之后
elif len(dash_positions) == 1:
    old_end = dash_positions[0] + 1
else:
    old_end = 50

# 拼接
new_text = toc_str + '\n' + '\n'.join(lines[old_end:])

# 清理：连续空行最多保留1个空行
new_text = re.sub(r'\n{3,}', '\n\n', new_text)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"已生成目录: {len(chapters)} 章")
for i, ch in enumerate(chapters, 1):
    print(f"  {i}. {ch['title']}" + (f" ({len(ch['subs'])}子节)" if ch['subs'] else ""))
