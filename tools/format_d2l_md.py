#!/usr/bin/env python3
"""Format D2L extracted Markdown for readability.

This script is intentionally conservative:
- Keeps chapter/section order (book architecture)
- Normalizes Unicode (NFKC) to fix compatibility CJK chars
- Removes obvious PDF page artifacts (page numbers/headers)
- Converts extracted TOC into Markdown nested list (no links)
- Promotes extracted headings into Markdown headings
- Reflows hard-wrapped prose paragraphs
- Fences #@save code blocks and obvious shell command blocks

Safety:
- By default writes to a side-by-side *.clean.md (does NOT overwrite).
- In-place overwrite requires --in-place.
- When overwriting, always creates a timestamped backup.
- Refuses to operate on suspiciously small on-disk files unless --allow-small.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass


def contains_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def is_cjk_char(ch: str) -> bool:
    return "\u4e00" <= ch <= "\u9fff"


def smart_join(prev: str, nxt: str) -> str:
    """Join two lines from the same paragraph.

    - If both boundaries are ASCII alnum, add a space.
    - Otherwise, join directly (Chinese paragraphs typically don't need spaces).
    """

    if not prev:
        return nxt
    if not nxt:
        return prev

    prev_last = prev[-1]
    nxt_first = nxt[0]
    if prev_last.isalnum() and nxt_first.isalnum():
        return prev + " " + nxt
    return prev + nxt


def looks_like_shell(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if s.startswith("#"):
        return True
    return bool(
        re.match(
            r"^(pip|conda|curl|wget|mkdir|cd|sh|bash|jupyter|python|sudo)\b", s
        )
        or s.startswith("~/")
        or s.startswith("./")
    )


def looks_like_title_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if s.startswith(("#", "-", "*", ">", "```")):
        return False
    if looks_like_shell(s):
        return False
    # Short-ish and not obviously a sentence continuation
    if len(s) > 60:
        return False
    # Avoid dot-leader lines from TOC
    if "..." in s or ". ." in s:
        return False
    return True


def heading_level(num: str) -> int:
    dots = num.count(".")
    # chapter -> ##, section -> ###, subsection -> ####
    return min(2 + dots, 4)


_RE_ROMAN = re.compile(r"^(?=[ivxlcdm]+$)[ivxlcdm]{1,6}$", re.IGNORECASE)
_RE_NUMBER_ONLY = re.compile(r"^\d{1,3}$")
_RE_NUMERIC_HEADING = re.compile(r"^(\d+(?:\.\d+)*)\s+$")
_RE_TOC_NUM_LINE = re.compile(
    r"^(\d+(?:\.\d+)*)\s+(.+?)\s*(?:\.{2,}|\.\s\.)?\s*\d+\s*$"
)
_RE_TOC_FRONTMATTER = re.compile(r"^([^\d\s].*?)(\d+)\s*$")


@dataclass
class Stats:
    removed_artifacts: int = 0
    normalized_nfkc: bool = False
    fenced_python_blocks: int = 0
    fenced_shell_blocks: int = 0
    promoted_headings: int = 0
    reflowed_paragraphs: int = 0
    toc_rewritten: bool = False


def normalize_nfkc(text: str, stats: Stats) -> str:
    normalized = unicodedata.normalize("NFKC", text)
    stats.normalized_nfkc = normalized != text
    return normalized


def strip_page_artifacts(lines: list[str], stats: Stats) -> list[str]:
    out: list[str] = []
    for line in lines:
        s = line.strip()
        if not s:
            out.append("")
            continue

        low = s.lower()
        if low in {
            "(continues on next page)",
            "(continued from previous page)",
            "continues on next page",
            "continued from previous page",
        }:
            stats.removed_artifacts += 1
            continue

        # Common PDF artifacts like "目录7" / "目录11" (after NFKC normalization)
        if re.match(r"^目录\d+$", s) or re.match(r"^目錄\d+$", s):
            stats.removed_artifacts += 1
            continue

        # "目录" repeated as standalone (page header)
        if s in {"目录", "目錄"}:
            out.append(s)
            continue

        # Roman numeral page number alone
        if _RE_ROMAN.match(s):
            stats.removed_artifacts += 1
            continue

        out.append(line.rstrip())

    # Remove stray single-number lines later, after heading promotion
    return out


def rewrite_toc(lines: list[str], stats: Stats) -> list[str]:
    """Rewrite the first TOC block near the top into nested Markdown list."""

    # Find the first occurrence of a TOC marker near the beginning.
    # D2L extraction often starts with metadata and then a "目录" block.
    max_scan = min(len(lines), 300)
    toc_start = None
    for i in range(max_scan):
        if lines[i].strip() in {"目录", "目錄"}:
            toc_start = i
            break
    if toc_start is None:
        return lines

    # Consume until we hit an empty line AFTER having seen some toc-like entries
    toc_end = None
    seen_entries = False
    for j in range(toc_start + 1, max_scan):
        s = lines[j].strip()
        if not s:
            if seen_entries:
                toc_end = j
                break
            continue
        # Accept both "2.1 数据操作.... 40" and "2.1 数据操作 . . . 40" forms
        s2 = re.sub(r"\s*\.\s*\.+\s*", " ", s)
        if _RE_TOC_NUM_LINE.match(s2) or _RE_TOC_FRONTMATTER.match(s2):
            seen_entries = True

    if toc_end is None or not seen_entries:
        return lines

    toc_lines = [l.rstrip() for l in lines[toc_start + 1 : toc_end] if l.strip()]

    new_toc: list[str] = []
    new_toc.append("## 目录")
    for raw in toc_lines:
        s = raw.strip()
        s2 = re.sub(r"\s*\.\s*\.+\s*", " ", s)
        s2 = re.sub(r"\s+", " ", s2).strip()

        m_num = _RE_TOC_NUM_LINE.match(s2)
        if m_num:
            num, title = m_num.group(1), m_num.group(2)
            title = re.sub(r"\s*\.{2,}\s*\d+\s*$", "", title).strip()
            level = num.count(".")
            indent = "  " * level
            new_toc.append(f"{indent}- {num} {title}")
            continue

        m_front = _RE_TOC_FRONTMATTER.match(s2)
        if m_front:
            name = m_front.group(1).strip()
            # Keep frontmatter as top-level bullet
            new_toc.append(f"- {name}")
            continue

        # Fallback: keep as top-level bullet
        new_toc.append(f"- {s}")

    # Replace original toc marker and toc content with rewritten one
    out = []
    out.extend(lines[:toc_start])
    out.append("")
    out.extend(new_toc)
    out.append("")
    out.extend(lines[toc_end + 1 :])
    stats.toc_rewritten = True
    return out


def promote_split_headings(lines: list[str], stats: Stats) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        cur = lines[i].strip()
        if _RE_NUMBER_ONLY.match(cur) or re.match(r"^\d+(?:\.\d+)*$", cur):
            # Look ahead for a title line
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and looks_like_title_line(lines[j]):
                num = cur
                title = lines[j].strip()
                lvl = heading_level(num)
                hashes = "#" * lvl
                out.append(f"{hashes} {num} {title}")
                stats.promoted_headings += 1
                i = j + 1
                continue

        out.append(lines[i].rstrip())
        i += 1
    return out


def remove_remaining_page_numbers(lines: list[str], stats: Stats) -> list[str]:
    out: list[str] = []
    for idx, line in enumerate(lines):
        s = line.strip()
        if not s:
            out.append("")
            continue

        if _RE_NUMBER_ONLY.match(s):
            # After heading promotion, remaining solitary numbers are almost always page numbers.
            stats.removed_artifacts += 1
            continue
        out.append(line.rstrip())
    return out


def convert_bullets(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        if line.lstrip().startswith("• "):
            out.append(re.sub(r"^\s*•\s+", "- ", line))
        else:
            out.append(line)
    return out


def fence_blocks(lines: list[str], stats: Stats) -> list[str]:
    out: list[str] = []
    i = 0
    in_python = False
    in_shell = False

    def close_fence(kind: str) -> None:
        nonlocal in_python, in_shell
        out.append("```")
        if kind == "python":
            in_python = False
        else:
            in_shell = False

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if in_python:
            # Close python fence when encountering a clearly narrative CJK line.
            if s and contains_cjk(s) and not s.startswith("#") and not line.startswith((" ", "\t")):
                close_fence("python")
                continue
            out.append(line.rstrip())
            i += 1
            continue

        if in_shell:
            if not s:
                close_fence("bash")
                out.append("")
                i += 1
                continue
            if not looks_like_shell(line):
                close_fence("bash")
                continue
            out.append(line.rstrip())
            i += 1
            continue

        # Start python fenced block at #@save
        if s.startswith("#@save"):
            out.append("```python")
            stats.fenced_python_blocks += 1
            in_python = True
            out.append(line.rstrip())
            i += 1
            continue

        # Start shell block for obvious consecutive command lines
        if looks_like_shell(line) and not s.startswith("#@save"):
            # Heuristic: only open a shell fence when we see at least 2 shell-like lines
            # (reduces risk of fencing a single sentence starting with 'python' etc.)
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if looks_like_shell(nxt):
                out.append("```bash")
                stats.fenced_shell_blocks += 1
                in_shell = True
                out.append(line.rstrip())
                i += 1
                continue

        out.append(line.rstrip())
        i += 1

    if in_python:
        close_fence("python")
    if in_shell:
        close_fence("bash")
    return out


def reflow_paragraphs(lines: list[str], stats: Stats) -> list[str]:
    out: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        if not buf:
            return
        combined = buf[0]
        for piece in buf[1:]:
            combined = smart_join(combined, piece)
        out.append(combined)
        if len(buf) > 1:
            stats.reflowed_paragraphs += 1
        buf.clear()

    def is_prose_line(line: str) -> bool:
        s = line.strip()
        if not s:
            return False
        if s.startswith(("#", "- ", "* ", ">", "```")):
            return False
        if s.startswith("Discussions"):
            return False
        if looks_like_shell(s):
            return False
        if s.startswith("#@save"):
            return False
        # Keep math-ish / symbol tables as-is
        if re.match(r"^[•\-]\s+", s):
            return False
        return True

    for line in lines:
        s = line.rstrip()
        if not s.strip():
            flush()
            out.append("")
            continue

        if not is_prose_line(s):
            flush()
            out.append(s)
            continue

        buf.append(s.strip())

    flush()
    return out


def ensure_top_title(lines: list[str]) -> list[str]:
    # Promote first non-empty line to H1 if it isn't already a heading.
    out = lines[:]
    for i, line in enumerate(out[:30]):
        if not line.strip():
            continue
        if line.lstrip().startswith("#"):
            return out
        out[i] = "# " + line.strip()
        return out
    return out


def format_file(input_path: str, in_place: bool = True) -> Stats:
    stats = Stats()
    if not os.path.exists(input_path):
        raise FileNotFoundError(input_path)

    size = os.path.getsize(input_path)
    if size < 1024 and not getattr(format_file, "_allow_small", False):
        raise RuntimeError(
            f"Refusing to format a very small file on disk ({size} bytes): {input_path}. "
            "If the file is open in VS Code with lots of content, save it to disk first. "
            "Then re-run, or pass --allow-small if you really intend this."
        )

    with open(input_path, "r", encoding="utf-8") as f:
        original = f.read()

    text = normalize_nfkc(original, stats)
    lines = text.splitlines()

    lines = strip_page_artifacts(lines, stats)
    lines = rewrite_toc(lines, stats)
    lines = promote_split_headings(lines, stats)
    lines = remove_remaining_page_numbers(lines, stats)
    lines = convert_bullets(lines)
    lines = fence_blocks(lines, stats)
    lines = reflow_paragraphs(lines, stats)
    lines = ensure_top_title(lines)

    # Normalize excessive blank lines (max 2)
    cleaned: list[str] = []
    blank_run = 0
    for line in lines:
        if not line.strip():
            blank_run += 1
            if blank_run <= 2:
                cleaned.append("")
            continue
        blank_run = 0
        cleaned.append(line.rstrip())

    new_text = "\n".join(cleaned).rstrip() + "\n"

    if in_place:
        ts = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_base = input_path + ".bak"
        backup = backup_base if not os.path.exists(backup_base) else backup_base + f".{ts}"
        shutil.copy2(input_path, backup)
        with open(input_path, "w", encoding="utf-8") as f:
            f.write(new_text)
    else:
        out_path = input_path + ".clean.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(new_text)

    return stats


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to D2L extracted markdown")
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite the input file (creates a timestamped .bak backup).",
    )
    parser.add_argument(
        "--allow-small",
        action="store_true",
        help="Allow formatting even if the on-disk file is very small.",
    )
    args = parser.parse_args(argv)

    t0 = _dt.datetime.now()
    setattr(format_file, "_allow_small", bool(args.allow_small))
    stats = format_file(args.path, in_place=bool(args.in_place))
    t1 = _dt.datetime.now()

    if args.in_place:
        print("Formatted (in-place):", args.path)
        print("Backup: created beside the file (*.bak*)")
    else:
        print("Formatted (side-by-side):", args.path + ".clean.md")
    print("Time:", f"{(t1 - t0).total_seconds():.2f}s")
    print("Stats:")
    print("  normalized_nfkc:", stats.normalized_nfkc)
    print("  toc_rewritten:", stats.toc_rewritten)
    print("  promoted_headings:", stats.promoted_headings)
    print("  fenced_python_blocks:", stats.fenced_python_blocks)
    print("  fenced_shell_blocks:", stats.fenced_shell_blocks)
    print("  reflowed_paragraphs:", stats.reflowed_paragraphs)
    print("  removed_artifacts:", stats.removed_artifacts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
