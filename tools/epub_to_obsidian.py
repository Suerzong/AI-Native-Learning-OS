from __future__ import annotations

import argparse
import html
import re
import zipfile
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Tuple
import xml.etree.ElementTree as ET


INVALID_PATH_CHARS = r'<>:"/\|?*'


def clean_name(name: str) -> str:
    name = re.sub(r"\s*\(z-library\.sk, 1lib\.sk, z-lib\.sk\)", "", name)
    name = re.sub(r"^[#*_`\s]+|[#*_`\s]+$", "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return "".join("_" if ch in INVALID_PATH_CHARS else ch for ch in name).strip(" .")


def is_meaningful_title(title: str) -> bool:
    cleaned = clean_name(title)
    return bool(cleaned) and bool(re.search(r"[\w\u4e00-\u9fff]", cleaned))


def collapse_blank_lines(text: str) -> str:
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


class HtmlToMarkdown(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.parts: List[str] = []
        self.skip_depth = 0
        self.heading_level: Optional[int] = None
        self.in_li = False

    def emit(self, text: str) -> None:
        if self.skip_depth == 0:
            self.parts.append(text)

    def block(self) -> None:
        self.emit("\n\n")

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "nav"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = int(tag[1])
            self.block()
            self.emit("#" * self.heading_level + " ")
        elif tag in {"p", "div", "section", "article"}:
            self.block()
        elif tag == "br":
            self.emit("\n")
        elif tag == "li":
            self.block()
            self.emit("- ")
            self.in_li = True
        elif tag in {"em", "i"}:
            self.emit("*")
        elif tag in {"strong", "b"}:
            self.emit("**")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "nav"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = None
            self.block()
        elif tag in {"p", "div", "section", "article", "li", "ul", "ol"}:
            self.block()
            if tag == "li":
                self.in_li = False
        elif tag in {"em", "i"}:
            self.emit("*")
        elif tag in {"strong", "b"}:
            self.emit("**")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = html.unescape(data)
        text = re.sub(r"\s+", " ", text)
        if text.strip():
            self.emit(text)

    def handle_entityref(self, name: str) -> None:
        self.emit(html.unescape(f"&{name};"))

    def handle_charref(self, name: str) -> None:
        self.emit(html.unescape(f"&#{name};"))

    def markdown(self) -> str:
        text = "".join(self.parts)
        lines = []
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                lines.append(stripped)
            else:
                lines.append(re.sub(r" {2,}", " ", stripped))
        return collapse_blank_lines("\n".join(lines))


def xml_ns(root: ET.Element) -> Dict[str, str]:
    if root.tag.startswith("{"):
        uri = root.tag.split("}", 1)[0][1:]
        return {"ns": uri}
    return {}


def find_rootfile(zf: zipfile.ZipFile) -> str:
    container = ET.fromstring(zf.read("META-INF/container.xml"))
    ns = xml_ns(container)
    rootfile = container.find(".//ns:rootfile", ns) if ns else container.find(".//rootfile")
    if rootfile is None:
        raise ValueError("Cannot find EPUB rootfile.")
    full_path = rootfile.attrib["full-path"]
    return full_path


def read_spine(zf: zipfile.ZipFile, opf_path: str) -> List[str]:
    root = ET.fromstring(zf.read(opf_path))
    ns = xml_ns(root)
    manifest_query = ".//ns:manifest/ns:item" if ns else ".//manifest/item"
    spine_query = ".//ns:spine/ns:itemref" if ns else ".//spine/itemref"

    manifest: Dict[str, str] = {}
    base = PurePosixPath(opf_path).parent
    for item in root.findall(manifest_query, ns):
        href = item.attrib.get("href")
        item_id = item.attrib.get("id")
        media_type = item.attrib.get("media-type", "")
        if href and item_id and ("html" in media_type or href.lower().endswith((".html", ".xhtml", ".htm"))):
            manifest[item_id] = str(base / href)

    ordered: List[str] = []
    for itemref in root.findall(spine_query, ns):
        item_id = itemref.attrib.get("idref")
        if item_id in manifest:
            ordered.append(manifest[item_id])
    return ordered


def title_from_markdown(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            if is_meaningful_title(title):
                return clean_name(title)[:80]
    first = next((line.strip() for line in markdown.splitlines() if line.strip()), "")
    if is_meaningful_title(first):
        return clean_name(first[:40])
    return fallback


def convert_epub(epub_path: Path, output_root: Path) -> Tuple[str, int]:
    book_name = clean_name(epub_path.stem)
    book_dir = output_root / book_name
    chapters_dir = book_dir / "chapters"
    notes_dir = book_dir / "notes"
    questions_dir = book_dir / "questions"
    insights_dir = book_dir / "insights"
    summaries_dir = book_dir / "summaries"
    for directory in [chapters_dir, notes_dir, questions_dir, insights_dir, summaries_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    chapter_links: List[str] = []
    with zipfile.ZipFile(epub_path) as zf:
        opf_path = find_rootfile(zf)
        spine = read_spine(zf, opf_path)
        for idx, item_path in enumerate(spine, start=1):
            try:
                raw = zf.read(item_path)
            except KeyError:
                continue
            parser = HtmlToMarkdown()
            parser.feed(raw.decode("utf-8", errors="ignore"))
            markdown = parser.markdown()
            if len(markdown.strip()) < 80:
                continue
            title = title_from_markdown(markdown, f"chapter-{idx:03d}")
            filename = f"{idx:03d}-{title}.md"
            if len(filename) > 120:
                filename = f"{idx:03d}-{clean_name(title[:60])}.md"
            chapter_path = chapters_dir / filename
            chapter_path.write_text(markdown, encoding="utf-8", newline="\n")
            chapter_links.append(f"- [[chapters/{chapter_path.stem}|{chapter_path.stem}]]")

    (book_dir / "index.md").write_text(
        collapse_blank_lines(
            f"""# {book_name}

## 阅读方式

- 每次只读一个章节或一个自然段落组。
- 读完后先写自己的疑问和感悟，再让 AI 帮你澄清。
- AI 可以解释、追问、总结，但不要替你跳过原文。

## 章节目录

{chr(10).join(chapter_links)}

## 阅读工作区

- [[notes/读书笔记|读书笔记]]
- [[questions/疑问池|疑问池]]
- [[insights/感悟|感悟]]
- [[summaries/阶段总结|阶段总结]]
"""
        ),
        encoding="utf-8",
        newline="\n",
    )
    for path, text in {
        notes_dir / "读书笔记.md": f"# {book_name} 读书笔记\n\n## 今天读到哪里\n\n\n## 我认为重要的句子或段落\n\n\n## 我的理解\n\n\n## 还没想明白的地方\n",
        questions_dir / "疑问池.md": f"# {book_name} 疑问池\n\n| 日期 | 位置 | 疑问 | 我目前的理解 | AI 澄清 | 状态 |\n|---|---|---|---|---|---|\n",
        insights_dir / "感悟.md": f"# {book_name} 感悟\n\n## 触动我的地方\n\n\n## 和我自身经验的连接\n\n\n## 我想继续追问的问题\n",
        summaries_dir / "阶段总结.md": f"# {book_name} 阶段总结\n\n## 本阶段读了什么\n\n\n## 核心观点\n\n\n## 我的收获\n\n\n## 仍然模糊的地方\n\n\n## 下一次阅读目标\n",
    }.items():
        if not path.exists():
            path.write_text(text, encoding="utf-8", newline="\n")
    return book_name, len(chapter_links)


def write_library_files(output_root: Path, results: List[Tuple[str, int]]) -> None:
    links = "\n".join(f"- [[{name}/index|{name}]] ({count} 个章节文件)" for name, count in results)
    templates_dir = output_root / "templates"
    templates_dir.mkdir(parents=True, exist_ok=True)
    (output_root / "00-阅读导航.md").write_text(
        collapse_blank_lines(
            f"""# 阅读导航

## 书籍

{links}

## 推荐流程

1. 打开一本书的 `index`。
2. 每次只读一个章节或一个短段落组。
3. 在对应书籍的 `疑问池` 写下疑问，在 `感悟` 写下触动。
4. 用 [[Claudian-阅读导师提示词]] 让 AI 带你澄清、追问和总结。
5. 每次阅读结束更新 `阶段总结`。

## 模板

- [[templates/每日阅读记录|每日阅读记录]]
- [[templates/章节精读|章节精读]]
- [[templates/AI 对话记录|AI 对话记录]]
"""
        ),
        encoding="utf-8",
        newline="\n",
    )
    (output_root / "Claudian-阅读导师提示词.md").write_text(
        collapse_blank_lines(
            """# Claudian 阅读导师提示词

你是我的阅读导师。你的目标不是替我快速总结一本书，而是陪我慢慢读懂原文，帮助我解决疑惑、提出追问、整理感悟，并把阅读变成可积累的理解。

## 使用方式

我会给你一段原文、我的疑问、我的感悟或一条笔记。你必须先判断我处在以下哪种状态：

1. 没看懂字面意思
2. 看懂了字面，但不懂作者为什么这样说
3. 有感受，但说不清原因
4. 想把观点和自己的生活、学习、价值观连接起来
5. 想总结本章或阶段阅读

## 回答规则

- 不要直接替我下最终结论。
- 先解释我卡住的点，再提出 2-3 个能推动我继续思考的问题。
- 如果我理解错了，要说清楚我哪里对、哪里偏了、为什么容易这样误解。
- 如果涉及背景知识，先用简短语言补齐，不要展开成百科。
- 如果我只给感悟，请帮我把感悟变成更清楚的问题或主题。
- 如果我要求总结，按"作者在说什么 / 我如何理解 / 可继续追问什么"三段输出。

## 阅读记录模板

- 原文位置：
- 我的问题：
- 我现在的理解：
- 触动我的地方：
- AI 澄清：
- 下一步追问：
"""
        ),
        encoding="utf-8",
        newline="\n",
    )
    template_files = {
        "每日阅读记录.md": """# 每日阅读记录

日期：
书名：
阅读位置：

## 今天读了什么


## 我没想明白的问题


## 我自己的感悟


## 想让 AI 帮我做什么

- [ ] 解释难懂段落
- [ ] 追问我的理解
- [ ] 整理本章观点
- [ ] 把感悟变成问题
- [ ] 帮我做阶段总结
""",
        "章节精读.md": """# 章节精读

书名：
章节：

## 章节在说什么


## 关键概念或意象


## 我的问题


## 我的理解


## AI 追问后我补充的理解


## 本章一句话总结
""",
        "AI 对话记录.md": """# AI 对话记录

日期：
书名：
位置：

## 我给 AI 的材料


## 我的原始问题或感悟


## AI 的澄清


## AI 问我的问题


## 我新的理解


## 是否需要回到原文重读

- [ ] 是
- [ ] 否
""",
    }
    for filename, text in template_files.items():
        (templates_dir / filename).write_text(collapse_blank_lines(text), encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    results = []
    for epub in sorted(args.source.glob("*.epub")):
        results.append(convert_epub(epub, args.output))
    write_library_files(args.output, results)
    for name, count in results:
        print(f"{name}: {count} chapters")


if __name__ == "__main__":
    main()
