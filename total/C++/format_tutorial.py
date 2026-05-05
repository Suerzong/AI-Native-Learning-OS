#!/usr/bin/env python3
"""将抓取的原始HTML内容整理成精美的Markdown学习文档"""

import urllib.request
import re
import os
import time

BASE = "https://www.runoob.com/cplusplus/"

CHAPTERS = [
    # (章节标题, 路径, 所属分组)
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


def fetch_and_extract(url, title):
    """抓取页面并提取文章正文"""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html;charset=utf-8",
            "Accept-Language": "zh-CN,zh;q=0.9",
        })
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        # 提取 article-body 部分
        match = re.search(
            r'class="article-body"[^>]*>(.*?)<div\s+class="previous-next-links"',
            html, re.DOTALL
        )
        if not match:
            match = re.search(
                r'class="article-body"[^>]*>(.*?)</div>\s*</div>\s*</div>',
                html, re.DOTALL
            )
        if not match:
            return None

        content = match.group(1)

        # 移除不需要的区域
        content = re.sub(r'<div[^>]*class="[^"]*(?:ad|adsbygoogle)[^"]*"[^>]*>.*?</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        content = re.sub(r'<ins[^>]*>.*?</ins>', '', content, flags=re.DOTALL)
        content = re.sub(r'<iframe[^>]*>.*?</iframe>', '', content, flags=re.DOTALL)

        # 移除 "AI 思考中..." 之类的残留
        content = re.sub(r'AI\s*思考中\.\.\.', '', content)

        # 处理代码块 <pre> -> ```cpp
        def replace_pre(m):
            code = m.group(1)
            code = re.sub(r'<br\s*/?>', '\n', code)
            code = re.sub(r'<[^>]+>', '', code)
            code = decode_entities(code)
            return '\n\n```cpp\n' + code.strip() + '\n```\n\n'

        content = re.sub(r'<pre[^>]*>(.*?)</pre>', replace_pre, content, flags=re.DOTALL)

        # 处理 <div class="example"> 或 <div class="code"> 内的代码
        def replace_example(m):
            code = m.group(1)
            code = re.sub(r'<br\s*/?>', '\n', code)
            code = re.sub(r'<[^>]+>', '', code)
            code = decode_entities(code)
            if len(code.strip()) > 20:
                return '\n\n```cpp\n' + code.strip() + '\n```\n\n'
            return code
        content = re.sub(r'<div[^>]*class="[^"]*(?:example|code)[^"]*"[^>]*>(.*?)</div>', replace_example, content, flags=re.DOTALL)

        # 处理 inline code
        content = re.sub(r'<code>(.*?)</code>', lambda m: '`' + re.sub(r'<[^>]+>', '', m.group(1)) + '`', content, flags=re.DOTALL)

        # 处理标题
        for i in range(1, 7):
            content = re.sub(
                rf'<h{i}[^>]*>(.*?)</h{i}>',
                lambda m, lvl=i: '\n\n' + '#' * (lvl + 1) + ' ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + '\n',
                content, flags=re.DOTALL
            )

        # 处理段落
        content = re.sub(r'<p[^>]*>', '\n\n', content)
        content = re.sub(r'</p>', '', content)

        # 处理列表 - 保持列表结构
        content = re.sub(r'<li[^>]*>', '\n- ', content)
        content = re.sub(r'</li>', '', content)
        content = re.sub(r'</?[uo]l[^>]*>', '', content)

        # 处理粗体/斜体
        content = re.sub(r'<(strong|b)>(.*?)</\1>', r'**\2**', content, flags=re.DOTALL)
        content = re.sub(r'<(em|i)>(.*?)</\1>', r'*\2*', content, flags=re.DOTALL)

        # 处理链接 - 保留菜鸟教程内部链接
        def replace_link(m):
            href = m.group(1)
            text = re.sub(r'<[^>]+>', '', m.group(2))
            if 'runoob.com' in href or href.startswith('/'):
                return text  # 内部链接只保留文本
            if href.startswith('javascript'):
                return text
            return f'[{text}]({href})'
        content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', replace_link, content, flags=re.DOTALL)

        # 处理 <br>
        content = re.sub(r'<br\s*/?>', '\n', content)

        # 处理图片 - 保留 alt 文本
        content = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*/?>', r'[\1]', content)
        content = re.sub(r'<img[^>]*/?>', '', content)

        # 处理表格
        content = process_table(content)

        # 移除所有剩余HTML标签
        content = re.sub(r'<[^>]+>', '', content)

        # 解码HTML实体
        content = decode_entities(content)

        # 清理空白
        content = re.sub(r'[ \t]+', ' ', content)
        content = re.sub(r'\n[ \t]+', '\n', content)
        content = re.sub(r'\n{3,}', '\n\n', content)
        content = content.strip()

        return content

    except Exception as e:
        print(f"  ERROR: {e}")
        return None


def process_table(html):
    """将HTML表格转换为Markdown表格"""
    def convert_table(m):
        table_html = m.group(1)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
        if not rows:
            return table_html

        md_rows = []
        for i, row in enumerate(rows):
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL)
            cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
            cells = [decode_entities(c) for c in cells]
            if cells:
                md_rows.append('| ' + ' | '.join(cells) + ' |')
                if i == 0:
                    md_rows.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')

        return '\n\n' + '\n'.join(md_rows) + '\n\n'

    content = re.sub(r'<table[^>]*>(.*?)</table>', convert_table, html, flags=re.DOTALL)
    return content


def decode_entities(text):
    """解码HTML实体"""
    entities = {
        '&lt;': '<', '&gt;': '>', '&amp;': '&', '&quot;': '"',
        '&#039;': "'", '&nbsp;': ' ', '&#8212;': '—', '&#8211;': '–',
        '&#123;': '{', '&#125;': '}', '&#40;': '(', '&#41;': ')',
        '&#59;': ';', '&#35;': '#', '&#39;': "'",
    }
    for k, v in entities.items():
        text = text.replace(k, v)
    # 处理数字实体
    text = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), text)
    return text


def main():
    output_path = r"c:\Users\sez18\Desktop\C++\C++教程_完整版.md"

    print(f"开始抓取并整理 {len(CHAPTERS)} 个页面...\n")

    all_content = {}  # title -> content
    for i, (title, path, group) in enumerate(CHAPTERS):
        url = BASE + path
        print(f"[{i+1}/{len(CHAPTERS)}] {title}")
        content = fetch_and_extract(url, title)
        if content:
            all_content[title] = content
            print(f"  OK ({len(content)} chars)")
        else:
            print(f"  FAILED")
        time.sleep(0.3)

    # 生成目录
    toc_lines = ["# C++ 教程 —— 菜鸟教程整理版\n"]
    toc_lines.append("> 本文档整理自 [菜鸟教程 C++](https://www.runoob.com/cplusplus/cpp-tutorial.html)，便于离线学习。\n")
    toc_lines.append("## 目录\n")

    current_group = ""
    chapter_num = 0
    for title, path, group in CHAPTERS:
        if group != current_group:
            current_group = group
            toc_lines.append(f"\n### {group}\n")
        chapter_num += 1
        anchor = title.replace(' ', '-').replace('&', '').replace('(', '').replace(')', '').replace('（', '').replace('）', '').lower()
        toc_lines.append(f"- [{title}](#{anchor})")

    toc = "\n".join(toc_lines)

    # 生成正文
    body_lines = []
    current_group = ""
    for title, path, group in CHAPTERS:
        if group != current_group:
            current_group = group
            body_lines.append(f"\n\n---\n\n# {group}\n")

        if title in all_content:
            # 跳过重复标题（内容中已经包含了标题）
            content = all_content[title]
            # 移除开头的重复标题
            content = re.sub(r'^#\s+' + re.escape(title) + r'\s*\n+', '', content)
            body_lines.append(f"\n## {title}\n")
            body_lines.append(content)
            body_lines.append("\n")

    body = "\n".join(body_lines)

    # 合并
    final = toc + "\n\n---\n" + body

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final)

    print(f"\n完成!")
    print(f"成功: {len(all_content)}/{len(CHAPTERS)} 个页面")
    print(f"输出: {output_path}")
    print(f"总大小: {len(final)} 字符")


if __name__ == "__main__":
    main()
