#!/usr/bin/env python3
"""批量抓取菜鸟教程C++所有页面并提取正文"""

import urllib.request
import re
import os
import time
from html.parser import HTMLParser

BASE = "https://www.runoob.com/cplusplus/"

URLS = [
    ("C++ 教程", "cpp-tutorial.html"),
    ("C++ 简介", "cpp-intro.html"),
    ("C++ 环境设置", "cpp-environment-setup.html"),
    ("C++ 基本语法", "cpp-basic-syntax.html"),
    ("C++ 注释", "cpp-comments.html"),
    ("C++ 数据类型", "cpp-data-types.html"),
    ("C++ 变量类型", "cpp-variable-types.html"),
    ("C++ 变量作用域", "cpp-variable-scope.html"),
    ("C++ 常量", "cpp-constants-literals.html"),
    ("C++ 修饰符类型", "cpp-modifier-types.html"),
    ("C++ 存储类", "cpp-storage-classes.html"),
    ("C++ 运算符", "cpp-operators.html"),
    ("C++ 循环", "cpp-loops.html"),
    ("C++ 判断", "cpp-decision.html"),
    ("C++ 函数", "cpp-functions.html"),
    ("C++ 数字", "cpp-numbers.html"),
    ("C++ 数组", "cpp-arrays.html"),
    ("C++ 字符串", "cpp-strings.html"),
    ("C++ 指针", "cpp-pointers.html"),
    ("C++ 引用", "cpp-references.html"),
    ("C++ 日期 & 时间", "cpp-date-time.html"),
    ("C++ 基本的输入输出", "cpp-basic-input-output.html"),
    ("C++ 结构体(struct)", "cpp-struct.html"),
    # 面向对象
    ("C++ 类 & 对象", "cpp-classes-objects.html"),
    ("C++ 继承", "cpp-inheritance.html"),
    ("C++ 重载运算符和重载函数", "cpp-overloading.html"),
    ("C++ 多态", "cpp-polymorphism.html"),
    ("C++ 数据抽象", "cpp-data-abstraction.html"),
    ("C++ 数据封装", "cpp-data-encapsulation.html"),
    ("C++ 接口（抽象类）", "cpp-interfaces.html"),
    # 高级教程
    ("C++ 文件和流", "cpp-files-streams.html"),
    ("C++ 异常处理", "cpp-exceptions-handling.html"),
    ("C++ 动态内存", "cpp-dynamic-memory.html"),
    ("C++ 命名空间", "cpp-namespaces.html"),
    ("C++ 模板", "cpp-templates.html"),
    ("C++ 预处理器", "cpp-preprocessor.html"),
]

OUTPUT_DIR = r"c:\Users\sez18\Desktop\C++\cpp_tutorial_pages"
os.makedirs(OUTPUT_DIR, exist_ok=True)


class ArticleExtractor(HTMLParser):
    """提取 article-body 内的文本和代码"""

    def __init__(self):
        super().__init__()
        self.in_article = False
        self.in_code = False
        self.in_pre = False
        self.in_heading = False
        self.heading_level = 0
        self.skip_depth = 0
        self.tag_stack = []
        self.result = []
        self.current_text = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # 进入 article-body
        if tag == "div" and "article-body" in attrs_dict.get("class", ""):
            self.in_article = True
            return

        if not self.in_article:
            return

        # 跳过广告等不需要的区域
        skip_classes = ["article-heading-ad", "ad", "adsbygoogle",
                        "previous-next-links", "article-intro-ad"]
        cls = attrs_dict.get("class", "")
        if any(s in cls for s in skip_classes):
            self.skip_depth += 1
            return

        if self.skip_depth > 0:
            self.skip_depth += 1
            return

        self.tag_stack.append(tag)

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.in_heading = True
            self.heading_level = int(tag[1])
            self.flush()
            self.result.append("\n" + "#" * self.heading_level + " ")

        elif tag == "pre":
            self.in_pre = True
            self.flush()
            self.result.append("\n```cpp\n")

        elif tag == "code" and not self.in_pre:
            self.in_code = True
            self.result.append("`")

        elif tag == "br":
            self.result.append("\n")

        elif tag == "p":
            self.flush()
            self.result.append("\n\n")

        elif tag == "li":
            self.flush()
            self.result.append("\n- ")

        elif tag == "strong" or tag == "b":
            self.result.append("**")

        elif tag == "em" or tag == "i":
            self.result.append("*")

        elif tag == "table":
            self.flush()
            self.result.append("\n\n")

        elif tag == "tr":
            self.flush()
            self.result.append("\n| ")

        elif tag == "th" or tag == "td":
            self.result.append(" | ")

        elif tag == "a":
            href = attrs_dict.get("href", "")
            if href and not href.startswith("javascript"):
                self.result.append("[")

    def handle_endtag(self, tag):
        if self.skip_depth > 0:
            self.skip_depth -= 1
            return

        if not self.in_article:
            return

        if tag == "div" and self.in_article:
            # check if we're exiting article-body
            pass

        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.flush()
            self.result.append("\n")
            self.in_heading = False

        elif tag == "pre":
            self.flush()
            self.result.append("\n```\n")
            self.in_pre = False

        elif tag == "code" and self.in_code:
            self.result.append("`")
            self.in_code = False

        elif tag == "strong" or tag == "b":
            self.result.append("**")

        elif tag == "em" or tag == "i":
            self.result.append("*")

        elif tag == "a":
            self.result.append("]")

    def handle_data(self, data):
        if self.in_article and self.skip_depth == 0:
            self.result.append(data)

    def flush(self):
        pass

    def get_text(self):
        text = "".join(self.result)
        # 清理多余空行
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()


def fetch_page(url, title, filename):
    """抓取单个页面并提取内容"""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        # 用正则提取 article-body 中的内容
        match = re.search(
            r'<div\s+class="article-body"[^>]*>(.*?)</div>\s*<!--\s*article-body\s*-->',
            html, re.DOTALL
        )
        if not match:
            # fallback: try broader match
            match = re.search(
                r'<div\s+class="article-body"[^>]*>(.*?)</div>\s*</div>\s*</div>',
                html, re.DOTALL
            )

        if not match:
            # simplest: grab between article-body and previous-next
            match = re.search(
                r'(?:class="article-body")[^>]*>(.*?)<div\s+class="previous-next-links"',
                html, re.DOTALL
            )

        if not match:
            print(f"  [WARN] Could not extract content from {filename}")
            return None

        content_html = match.group(1)

        # Simple HTML to text conversion for this content
        text = content_html

        # Remove script/style blocks
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

        # Handle code blocks
        text = re.sub(r'<pre[^>]*>(.*?)</pre>', lambda m: '\n```cpp\n' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + '\n```\n', text, flags=re.DOTALL)

        # Handle inline code
        text = re.sub(r'<code>(.*?)</code>', r'`\1`', text, flags=re.DOTALL)

        # Handle headings
        for i in range(1, 7):
            text = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', lambda m, lvl=i: '\n\n' + '#' * lvl + ' ' + m.group(1).strip() + '\n', text, flags=re.DOTALL)

        # Handle paragraphs
        text = re.sub(r'<p[^>]*>', '\n\n', text)
        text = re.sub(r'</p>', '', text)

        # Handle list items
        text = re.sub(r'<li[^>]*>', '\n- ', text)
        text = re.sub(r'</li>', '', text)

        # Handle bold/italic
        text = re.sub(r'<(strong|b)>(.*?)</\1>', r'**\2**', text, flags=re.DOTALL)
        text = re.sub(r'<(em|i)>(.*?)</\1>', r'*\2*', text, flags=re.DOTALL)

        # Handle links
        text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL)

        # Handle <br>
        text = re.sub(r'<br\s*/?>', '\n', text)

        # Handle tables
        text = re.sub(r'<th[^>]*>', '| ', text)
        text = re.sub(r'<td[^>]*>', '| ', text)
        text = re.sub(r'</th>', ' ', text)
        text = re.sub(r'</td>', ' ', text)
        text = re.sub(r'<tr[^>]*>', '\n', text)

        # Remove <img> tags but keep alt text
        text = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*/?>', r'[\1]', text)
        text = re.sub(r'<img[^>]*/?>', '', text)

        # Remove all remaining HTML tags
        text = re.sub(r'<[^>]+>', '', text)

        # Decode HTML entities
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&amp;', '&')
        text = text.replace('&quot;', '"')
        text = text.replace('&#039;', "'")
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&#8212;', '—')
        text = text.replace('&#8211;', '–')

        # Clean up whitespace
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = text.strip()

        return text

    except Exception as e:
        print(f"  [ERROR] {filename}: {e}")
        return None


def main():
    print(f"开始抓取 {len(URLS)} 个页面...\n")

    results = {}
    for i, (title, path) in enumerate(URLS):
        url = BASE + path
        filename = path.replace(".html", "")
        print(f"[{i+1}/{len(URLS)}] {title} -> {path}")

        content = fetch_page(url, title, filename)
        if content:
            results[title] = content
            # Save individual page
            with open(os.path.join(OUTPUT_DIR, f"{filename}.md"), "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n{content}")
            print(f"  OK ({len(content)} chars)")
        else:
            print(f"  FAILED")

        # Be polite
        time.sleep(0.3)

    # Combine all into one file
    combined_path = r"c:\Users\sez18\Desktop\C++\cpp_tutorial_combined.md"
    with open(combined_path, "w", encoding="utf-8") as f:
        for title, path in URLS:
            if title in results:
                f.write(f"\n\n{'='*60}\n")
                f.write(f"# {title}\n")
                f.write(f"{'='*60}\n\n")
                f.write(results[title])
                f.write("\n")

    print(f"\n完成! 共抓取 {len(results)}/{len(URLS)} 个页面")
    print(f"单独页面: {OUTPUT_DIR}")
    print(f"合并文件: {combined_path}")


if __name__ == "__main__":
    main()
