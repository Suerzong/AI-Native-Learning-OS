#!/usr/bin/env python3
"""v3: 修复C++模板语法(<iostream>等)被误删的问题，以及代码块提取"""

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

# 我们需要保留的HTML标签（这些是安全的，不会包含C++代码）
SAFE_TAGS = {'p', 'br', 'strong', 'b', 'em', 'i', 'a', 'ul', 'ol', 'li',
             'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'thead', 'tbody',
             'tr', 'th', 'td', 'div', 'span', 'img', 'blockquote'}

# 需要保护的C++模板语法占位符
CPP_TEMPLATE_RE = re.compile(r'#include\s*<([a-zA-Z_][a-zA-Z0-9_.]*)>')
CPP_TEMPLATES = {}


def decode(s):
    return html_mod.unescape(s)


def protect_cpp_templates(s):
    """将 #include <xxx> 等C++模板语法替换为占位符，防止被当作HTML标签"""
    global CPP_TEMPLATES
    CPP_TEMPLATES = {}
    counter = [0]

    def replacer(m):
        placeholder = f"___CPP_INCLUDE_{counter[0]}___"
        CPP_TEMPLATES[placeholder] = m.group(0)
        counter[0] += 1
        return placeholder

    # 保护 #include <xxx> (decoded)
    s = re.sub(r'#include\s*<([a-zA-Z_][a-zA-Z0-9_.]*)>', replacer, s)
    # 保护 #include &lt;xxx&gt; (HTML encoded)
    s = re.sub(r'#include\s*&lt;([a-zA-Z_][a-zA-Z0-9_.]*)&gt;', replacer, s)
    return s


def restore_cpp_templates(s):
    """还原被保护的C++模板语法"""
    for placeholder, original in CPP_TEMPLATES.items():
        s = s.replace(placeholder, original)
    return s


def fetch_page(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html;charset=utf-8",
        "Accept-Language": "zh-CN,zh;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_article(html):
    m = re.search(
        r'class="article-body"[^>]*>(.*?)(?:<div\s+class="previous-next-links"|<div\s+class="article-footer")',
        html, re.DOTALL
    )
    return m.group(1) if m else None


def clean_code(text):
    """清理代码块中的HTML标签，只保留纯文本"""
    # <br> -> \n
    text = re.sub(r'<br\s*/?>', '\n', text)
    # 移除 <span> 语法高亮标签（保留内容）
    text = re.sub(r'</?span[^>]*>', '', text)
    # 移除 <div> 等其他标签
    text = re.sub(r'<div[^>]*>', '', text)
    text = re.sub(r'</div>', '', text)
    # 保护C++模板语法（在HTML实体解码前，用编码形式匹配）
    global CPP_TEMPLATES
    counter = [len(CPP_TEMPLATES)]
    def replacer(m):
        placeholder = f"___CPP_INCLUDE_{counter[0]}___"
        CPP_TEMPLATES[placeholder] = m.group(0)
        counter[0] += 1
        return placeholder
    # 匹配编码形式: #include &lt;xxx&gt;
    text = re.sub(r'#include\s*&lt;([a-zA-Z_][a-zA-Z0-9_.]*)&gt;', replacer, text)
    # 移除所有剩余HTML标签（此时不会有 C++ <xxx> 被误删）
    text = re.sub(r'<[^>]+>', '', text)
    # 还原C++模板语法
    for placeholder, original in CPP_TEMPLATES.items():
        text = text.replace(placeholder, original)
    # 解码HTML实体（在标签移除后）
    text = decode(text)
    # 清理 &nbsp; -> space
    text = text.replace('\xa0', ' ')
    # 清理多余空行
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def html_to_md(s):
    """HTML片段转Markdown"""

    # 1. 移除广告/脚本/样式
    s = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.DOTALL)
    s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.DOTALL)
    s = re.sub(r'<!--.*?-->', '', s, flags=re.DOTALL)
    s = re.sub(r'<ins[^>]*>.*?</ins>', '', s, flags=re.DOTALL)
    s = re.sub(r'<iframe[^>]*>.*?</iframe>', '', s, flags=re.DOTALL)

    # 2. 保护C++模板语法
    s = protect_cpp_templates(s)

    # 3. <div class="example_code">...</div></div> —— 语法高亮代码块
    def handle_example_code(m):
        code_html = m.group(1)
        code = clean_code(code_html)
        code = re.sub(r'^实例\s*\n?', '', code)
        if not code:
            return ''
        return '\n\n```cpp\n' + code + '\n```\n\n'

    # Match: <div class="example_code"> ... </div> </div>
    # The first </div> closes the inner <div class="hl-main">,
    # the second </div> closes example_code.
    # So capture everything up to the LAST </div></div> pair.
    s = re.sub(
        r'<div[^>]*class="[^"]*example_code[^"]*"[^>]*>(.*?)</div>\s*</div>\s*(?:</div>)?',
        handle_example_code, s, flags=re.DOTALL
    )

    # 3b. <pre>...</pre> —— 预格式化代码块
    def handle_pre(m):
        code = clean_code(m.group(1))
        code = re.sub(r'^实例\s*\n?', '', code)
        if not code:
            return ''
        return '\n\n```cpp\n' + code + '\n```\n\n'

    s = re.sub(r'<pre[^>]*>(.*?)</pre>', handle_pre, s, flags=re.DOTALL)

    # 4. <h2 class="example"> 实例标题
    s = re.sub(
        r'<h2[^>]*class="example"[^>]*>(.*?)</h2>',
        lambda m: '\n\n### ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + '\n\n',
        s, flags=re.DOTALL
    )

    # 5. 标题 h2-h6
    for i in range(2, 7):
        def make_heading_handler(lvl=i):
            def handler(m):
                text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
                return '\n\n' + '#' * lvl + ' ' + text + '\n\n'
            return handler
        s = re.sub(rf'<h{i}[^>]*>(.*?)</{i}>', make_heading_handler(), s, flags=re.DOTALL)

    # 6. 表格
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

    # 7. 列表
    s = re.sub(r'<li[^>]*>', '\n- ', s)
    s = re.sub(r'</li>', '', s)
    s = re.sub(r'</?[uo]l[^>]*>', '', s)

    # 8. 粗体/斜体
    s = re.sub(r'<(strong|b)>(.*?)</\1>', r'**\2**', s, flags=re.DOTALL)
    s = re.sub(r'<(em|i)>(.*?)</\1>', r'*\2*', s, flags=re.DOTALL)

    # 9. 段落
    s = re.sub(r'<p[^>]*>', '\n\n', s)
    s = re.sub(r'</p>', '', s)

    # 10. 链接
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

    # 11. <code> 行内代码
    s = re.sub(r'<code>(.*?)</code>', lambda m: '`' + decode(re.sub(r'<[^>]+>', '', m.group(1))) + '`', s, flags=re.DOTALL)

    # 12. <br>
    s = re.sub(r'<br\s*/?>', '\n', s)

    # 13. 图片
    s = re.sub(r'<img[^>]*/?>', '', s)

    # 14. 移除 div / span（在代码块之后处理）
    s = re.sub(r'</?div[^>]*>', '', s)
    s = re.sub(r'</?span[^>]*>', '', s)

    # 15. 移除所有剩余HTML标签
    s = re.sub(r'<[^>]+>', '', s)

    # 16. 还原C++模板语法
    s = restore_cpp_templates(s)

    # 17. 解码HTML实体
    s = decode(s)

    # 18. 清理
    s = re.sub(r'运行实例\s*»?\s*', '', s)
    s = re.sub(r'AI\s*思考中\.\.\.', '', s)
    s = re.sub(r'\[[-\w]*logo[-\w]*\]', '', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    s = re.sub(r'[ \t]+\n', '\n', s)

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
    lines.append("# C++ 教程 —— 菜鸟教程整理版\n")
    lines.append("> 本文档整理自 [菜鸟教程 C++](https://www.runoob.com/cplusplus/cpp-tutorial.html)，便于离线学习阅读。\n")
    lines.append("## 目录\n")

    prev_group = ""
    for title, path, group in CHAPTERS:
        if group != prev_group:
            prev_group = group
            lines.append(f"\n**{group}**\n")
        lines.append(f"- {title}")

    lines.append("\n\n---\n")

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
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    result = result.rstrip() + '\n'

    with open(output, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\n完成! {len(pages)}/{len(CHAPTERS)} 个页面")
    print(f"总大小: {len(result)} 字符")
    print(f"输出: {output}")


if __name__ == "__main__":
    main()
