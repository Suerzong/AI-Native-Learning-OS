#!/usr/bin/env python3
"""v2: 更精确的HTML到Markdown转换"""

import urllib.request
import re
import time
import html as html_mod

BASE = "https://www.runoob.com/cplusplus/"

CHAPTERS = [
    ("C++ 教程", "cpp-tutorial.html", "前言"),
    ("C++ 简介", "cpp-intro.html", "前言"),
    ("C++ 环境设置", "cpp-environment-setup.html", "前言"),
    ("C++ 基本语法", "cpp-basic-syntax.html", "C++ 基础"),
    ("C++ 注释", "cpp-comments.html", "C++ 基础"),
    ("C++ 数据类型", "cpp-data-types.html", "C++ 基础"),
    ("C++ 变量类型", "cpp-variable-types.html", "C++ 基础"),
    ("C++ 变量作用域", "cpp-variable-scope.html", "C++ 基础"),
    ("C++ 常量", "cpp-constants-literals.html", "C++ 基础"),
    ("C++ 修饰符类型", "cpp-modifier-types.html", "C++ 基础"),
    ("C++ 存储类", "cpp-storage-classes.html", "C++ 基础"),
    ("C++ 运算符", "cpp-operators.html", "C++ 基础"),
    ("C++ 循环", "cpp-loops.html", "C++ 流程控制"),
    ("C++ 判断", "cpp-decision.html", "C++ 流程控制"),
    ("C++ 函数", "cpp-functions.html", "C++ 函数与数据结构"),
    ("C++ 数字", "cpp-numbers.html", "C++ 函数与数据结构"),
    ("C++ 数组", "cpp-arrays.html", "C++ 函数与数据结构"),
    ("C++ 字符串", "cpp-strings.html", "C++ 函数与数据结构"),
    ("C++ 指针", "cpp-pointers.html", "C++ 函数与数据结构"),
    ("C++ 引用", "cpp-references.html", "C++ 函数与数据结构"),
    ("C++ 日期 & 时间", "cpp-date-time.html", "C++ 函数与数据结构"),
    ("C++ 基本的输入输出", "cpp-basic-input-output.html", "C++ 函数与数据结构"),
    ("C++ 结构体(struct)", "cpp-struct.html", "C++ 函数与数据结构"),
    ("C++ 类 & 对象", "cpp-classes-objects.html", "C++ 面向对象"),
    ("C++ 继承", "cpp-inheritance.html", "C++ 面向对象"),
    ("C++ 重载运算符和重载函数", "cpp-overloading.html", "C++ 面向对象"),
    ("C++ 多态", "cpp-polymorphism.html", "C++ 面向对象"),
    ("C++ 数据抽象", "cpp-data-abstraction.html", "C++ 面向对象"),
    ("C++ 数据封装", "cpp-data-encapsulation.html", "C++ 面向对象"),
    ("C++ 接口（抽象类）", "cpp-interfaces.html", "C++ 面向对象"),
    ("C++ 文件和流", "cpp-files-streams.html", "C++ 高级教程"),
    ("C++ 异常处理", "cpp-exceptions-handling.html", "C++ 高级教程"),
    ("C++ 动态内存", "cpp-dynamic-memory.html", "C++ 高级教程"),
    ("C++ 命名空间", "cpp-namespaces.html", "C++ 高级教程"),
    ("C++ 模板", "cpp-templates.html", "C++ 高级教程"),
    ("C++ 预处理器", "cpp-preprocessor.html", "C++ 高级教程"),
]


def decode(s):
    """解码HTML实体"""
    return html_mod.unescape(s)


def fetch_page(url):
    """抓取页面HTML"""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html;charset=utf-8",
        "Accept-Language": "zh-CN,zh;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_article(html):
    """从HTML中提取 article-body 部分"""
    m = re.search(r'class="article-body"[^>]*>(.*?)(?:<div\s+class="previous-next-links"|<div\s+class="article-footer")', html, re.DOTALL)
    if not m:
        return None
    return m.group(1)


def html_to_md(s):
    """将HTML片段转为Markdown"""

    # 1. 移除广告/脚本/样式
    s = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.DOTALL)
    s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.DOTALL)
    s = re.sub(r'<!--.*?-->', '', s, flags=re.DOTALL)
    s = re.sub(r'<ins[^>]*>.*?</ins>', '', s, flags=re.DOTALL)
    s = re.sub(r'<iframe[^>]*>.*?</iframe>', '', s, flags=re.DOTALL)

    # 2. <div class="example_code"> 代码块 —— 先处理
    def handle_example_code(m):
        inner = m.group(1)
        inner = re.sub(r'<br\s*/?>', '\n', inner)
        inner = re.sub(r'<[^>]+>', '', inner)
        inner = decode(inner).strip()
        inner = re.sub(r'^实例\s*\n?', '', inner)
        if not inner:
            return ''
        return '\n\n```cpp\n' + inner + '\n```\n\n'

    s = re.sub(r'<div[^>]*class="[^"]*example_code[^"]*"[^>]*>(.*?)</div>\s*(?:</div>)?', handle_example_code, s, flags=re.DOTALL)

    # 2b. <pre> 代码块
    def handle_pre(m):
        inner = m.group(1)
        inner = re.sub(r'<br\s*/?>', '\n', inner)
        inner = re.sub(r'<[^>]+>', '', inner)
        inner = decode(inner).strip()
        inner = re.sub(r'^实例\s*\n?', '', inner)
        if not inner:
            return ''
        return '\n\n```cpp\n' + inner + '\n```\n\n'

    s = re.sub(r'<pre[^>]*>(.*?)</pre>', handle_pre, s, flags=re.DOTALL)

    # 3. 标题 h2-h6 (h1留给章节标题)
    for i in range(2, 7):
        def handle_heading(m, lvl=i):
            text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            return '\n\n' + '#' * lvl + ' ' + text + '\n\n'
        s = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', handle_heading, s, flags=re.DOTALL)

    # 4. 表格
    def handle_table(m):
        tbl = m.group(1)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', tbl, re.DOTALL)
        if not rows:
            return m.group(0)
        lines = []
        for idx, row in enumerate(rows):
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL)
            cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
            cells = [decode(c) for c in cells]
            if cells:
                lines.append('| ' + ' | '.join(cells) + ' |')
                if idx == 0:
                    lines.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
        return '\n\n' + '\n'.join(lines) + '\n\n'

    s = re.sub(r'<table[^>]*>(.*?)</table>', handle_table, s, flags=re.DOTALL)

    # 5. 列表
    s = re.sub(r'<li[^>]*>', '\n- ', s)
    s = re.sub(r'</li>', '', s)
    s = re.sub(r'</?[uo]l[^>]*>', '', s)

    # 6. 粗体/斜体
    s = re.sub(r'<(strong|b)>(.*?)</\1>', r'**\2**', s, flags=re.DOTALL)
    s = re.sub(r'<(em|i)>(.*?)</\1>', r'*\2*', s, flags=re.DOTALL)

    # 7. 段落
    s = re.sub(r'<p[^>]*>', '\n\n', s)
    s = re.sub(r'</p>', '', s)

    # 8. 链接
    def handle_link(m):
        href = decode(m.group(1))
        text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        text = decode(text)
        if href.startswith('javascript') or not href:
            return text
        if 'runoob.com' in href:
            return text
        return f'[{text}]({href})'
    s = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', handle_link, s, flags=re.DOTALL)

    # 9. <code> 行内代码
    s = re.sub(r'<code>(.*?)</code>', lambda m: '`' + decode(re.sub(r'<[^>]+>', '', m.group(1))) + '`', s, flags=re.DOTALL)

    # 10. <br>
    s = re.sub(r'<br\s*/?>', '\n', s)

    # 10b. example div heading -> ## heading
    s = re.sub(r'<h2[^>]*class="example"[^>]*>(.*?)</h2>', lambda m: '\n\n### ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + '\n\n', s, flags=re.DOTALL)
    # Remove remaining example div wrappers
    s = re.sub(r'<div[^>]*class="[^"]*example[^"]*"[^>]*>', '', s)
    s = re.sub(r'</div>', '\n', s)

    # 11. 图片 (只保留alt)
    s = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*/?>', '', s)
    s = re.sub(r'<img[^>]*/?>', '', s)

    # 12. div等块级元素 -> 换行
    s = re.sub(r'</div>', '\n', s)
    s = re.sub(r'<div[^>]*>', '', s)
    s = re.sub(r'</?span[^>]*>', '', s)

    # 13. 移除所有剩余HTML
    s = re.sub(r'<[^>]+>', '', s)

    # 14. 最终解码
    s = decode(s)

    # 15. 清理
    s = re.sub(r'运行实例\s*»?\s*', '', s)
    s = re.sub(r'AI\s*思考中\.\.\.', '', s)
    s = re.sub(r'\[[-\w]*logo[-\w]*\]', '', s)

    # 清理空行
    s = re.sub(r'\n{3,}', '\n\n', s)
    # 清理行尾空格
    s = re.sub(r'[ \t]+\n', '\n', s)
    # 清理行首多余空格(但保留缩进代码)
    # s = re.sub(r'\n[ \t]+', '\n', s) # 不做，保留列表缩进

    return s.strip()


def main():
    output = r"c:\Users\sez18\Desktop\C++\C++教程_完整版.md"

    print(f"抓取并转换 {len(CHAPTERS)} 个页面...\n")

    pages = {}
    for i, (title, path, group) in enumerate(CHAPTERS):
        url = BASE + path
        print(f"[{i+1}/{len(CHAPTERS)}] {title}", end=" ")
        try:
            html_content = fetch_page(url)
            article = extract_article(html_content)
            if article:
                md = html_to_md(article)
                # 移除开头重复的标题
                md = re.sub(r'^' + re.escape(title) + r'\s*\n*', '', md)
                md = re.sub(r'^#\s+' + re.escape(title) + r'\s*\n*', '', md)
                pages[title] = md
                print(f"OK ({len(md)} chars)")
            else:
                print("FAILED (no article-body)")
        except Exception as e:
            print(f"ERROR: {e}")
        time.sleep(0.3)

    # 生成最终文档
    lines = []

    # 封面
    lines.append("# C++ 教程 —— 菜鸟教程整理版\n")
    lines.append("> 本文档整理自 [菜鸟教程 C++](https://www.runoob.com/cplusplus/cpp-tutorial.html)，便于离线学习阅读。\n")

    # 目录
    lines.append("## 目录\n")

    prev_group = ""
    for title, path, group in CHAPTERS:
        if group != prev_group:
            prev_group = group
            lines.append(f"\n**{group}**\n")
        lines.append(f"- {title}")

    lines.append("\n\n---\n")

    # 正文
    prev_group = ""
    for title, path, group in CHAPTERS:
        if group != prev_group:
            prev_group = group
            lines.append(f"\n---\n\n# {group}\n")

        if title in pages:
            lines.append(f"\n## {title}\n")
            lines.append(pages[title])
            lines.append("")

    result = "\n".join(lines)

    # 最终清理
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    result = result.rstrip() + '\n'

    with open(output, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\n完成! {len(pages)}/{len(CHAPTERS)} 个页面")
    print(f"总大小: {len(result)} 字符")
    print(f"输出: {output}")


if __name__ == "__main__":
    main()
