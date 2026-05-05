#!/usr/bin/env python3
"""最终清理：修复重复标题、图片残留、代码块等问题"""

import re

INPUT = r"c:\Users\sez18\Desktop\C++\C++教程_完整版.md"
OUTPUT = r"c:\Users\sez18\Desktop\C++\C++教程_完整版.md"

with open(INPUT, "r", encoding="utf-8") as f:
    content = f.read()

# 1. 移除图片残留标记如 [cpp-mini-logo]
content = re.sub(r'\[[-\w]*logo[-\w]*\]', '', content)
content = re.sub(r'\[图片\]', '', content)

# 2. 修复连续重复标题: "## C++ 教程\n\n## C++ 教程" -> "## C++ 教程"
content = re.sub(r'(##\s+[^\n]+)\n\n\1(\n)', r'\1\2', content)

# 3. 修复 "---\n\n---" 双分隔线
content = re.sub(r'---\s*\n\s*---', '---', content)

# 4. 清理多余空行（最多2个连续空行）
content = re.sub(r'\n{4,}', '\n\n\n', content)

# 5. 清理列表项中的空行（"- \n\n**" -> "- **"）
content = re.sub(r'- \n\n(\*\*)', r'- \1', content)
content = re.sub(r'- \n(\*\*)', r'- \1', content)

# 6. 修复代码块前后的空行
content = re.sub(r'\n{3,}```', '\n\n```', content)
content = re.sub(r'```\n{3,}', '```\n\n', content)

# 7. 清理 "运行实例 »" 等残留
content = re.sub(r'运行实例\s*»?\s*', '', content)

# 8. 清理页尾残留
content = re.sub(r'AI\s*思考中\.\.\.\s*$', '', content)

# 9. 清理行尾空格
content = re.sub(r'[ \t]+\n', '\n', content)

# 10. 清理孤立的 "> " 开头（不是引用的）
# (先不处理这个，避免影响引用块)

# 确保文件以单个换行结尾
content = content.rstrip() + '\n'

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(content)

# 统计
lines = content.count('\n')
chars = len(content)
print(f"清理完成!")
print(f"行数: {lines}")
print(f"字符数: {chars}")
print(f"输出: {OUTPUT}")
