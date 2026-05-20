"""Prepare math PDFs for visual LaTeX transcription.

This script does not OCR. It renders PDF pages to images and creates
Markdown/LaTeX transcription stubs that can be filled by visual reading.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
MATH_DIR = ROOT / "temp" / "math"
OUT_DIR = MATH_DIR / "visual-latex"
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"}


PDFS = [
    "工科数学分析基础 上册.pdf",
    "工科数学分析基础 下册.pdf",
    "bump-1.3.2 (1).pdf",
]


def safe_name(name: str) -> str:
    name = name.replace("–", "-").replace("—", "-")
    name = re.sub(r"[\\/:*?\"<>|]+", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT.resolve())).replace("\\", "/")
    except ValueError:
        return str(path.resolve()).replace("\\", "/")


def md_rel(from_file: Path, target: Path) -> str:
    return os.path.relpath(target.resolve(), from_file.parent.resolve()).replace("\\", "/")


def render_pdf(pdf_path: Path, start: int, end: int, zoom: float) -> list[Path]:
    doc = fitz.open(pdf_path)
    page_count = doc.page_count
    start = max(1, start)
    end = min(page_count, end)

    folder = OUT_DIR / safe_name(pdf_path.stem)
    pages_dir = folder / "pages"
    trans_dir = folder / "transcribed"
    pages_dir.mkdir(parents=True, exist_ok=True)
    trans_dir.mkdir(parents=True, exist_ok=True)

    rendered: list[Path] = []
    matrix = fitz.Matrix(zoom, zoom)
    for page_no in range(start, end + 1):
        page = doc.load_page(page_no - 1)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        image_path = pages_dir / f"page-{page_no:04d}.png"
        pix.save(image_path)
        rendered.append(image_path)

        stub_path = trans_dir / f"page-{page_no:04d}.md"
        if not stub_path.exists():
            stub_path.write_text(
                "\n".join(
                    [
                        f"# {pdf_path.stem} - Page {page_no}",
                        "",
                        f"- 源文件：`{rel(pdf_path)}`",
                        f"- 页码：{page_no}",
                        f"- 页图：`{rel(image_path)}`",
                        f"- 转写方式：视觉阅读 + LaTeX 手工整理",
                        f"- 状态：待转写",
                        "",
                        f"![page-{page_no:04d}]({md_rel(stub_path, image_path)})",
                        "",
                        "## LaTeX Markdown",
                        "",
                        "<!-- 在这里填入视觉转写内容。公式使用 `$...$` 或 `$$...$$`。 -->",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
    doc.close()
    write_index(folder, pdf_path, page_count)
    return rendered


def create_stub(stub_path: Path, title: str, source_path: Path, image_path: Path, page_label: str) -> None:
    if stub_path.exists():
        return
    stub_path.write_text(
        "\n".join(
            [
                f"# {title}",
                "",
                f"- 源文件：`{rel(source_path)}`",
                f"- 页码/序号：{page_label}",
                f"- 页图：`{rel(image_path)}`",
                "- 转写方式：视觉阅读 + LaTeX 手工整理",
                "- 状态：待转写",
                "",
                f"![{image_path.stem}]({md_rel(stub_path, image_path)})",
                "",
                "## LaTeX Markdown",
                "",
                "<!-- 在这里填入视觉转写内容。公式使用 `$...$` 或 `$$...$$`。不确定内容标记 `[待核对]`。 -->",
                "",
            ]
        ),
        encoding="utf-8",
    )


def ingest_image_dir(image_dir: Path, batch_name: str | None) -> list[Path]:
    if not image_dir.exists():
        raise FileNotFoundError(image_dir)

    folder_name = safe_name(batch_name or image_dir.name)
    folder = OUT_DIR / "manual-batches" / folder_name
    pages_dir = folder / "pages"
    trans_dir = folder / "transcribed"
    pages_dir.mkdir(parents=True, exist_ok=True)
    trans_dir.mkdir(parents=True, exist_ok=True)

    images = sorted(p for p in image_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS)
    copied: list[Path] = []
    for idx, source in enumerate(images, start=1):
        target = pages_dir / f"page-{idx:04d}{source.suffix.lower()}"
        if not target.exists() or target.stat().st_size != source.stat().st_size:
            shutil.copy2(source, target)
        copied.append(target)
        create_stub(
            trans_dir / f"page-{idx:04d}.md",
            f"{folder_name} - Image {idx}",
            source,
            target,
            str(idx),
        )

    write_image_batch_index(folder, image_dir, copied)
    return copied


def write_image_batch_index(folder: Path, image_dir: Path, images: list[Path]) -> None:
    transcribed = sorted((folder / "transcribed").glob("page-*.md"))
    trans_map = {p.stem: p for p in transcribed}
    lines = [
        f"# {folder.name} 视觉转写索引",
        "",
        f"- 图片来源目录：`{rel(image_dir)}`",
        f"- 图片数量：{len(images)}",
        f"- 更新时间：{now()}",
        "- 转写方式：视觉阅读 + LaTeX 手工整理，不使用 OCR",
        "",
        "| 序号 | 页图 | 转写稿 |",
        "|---:|---|---|",
    ]
    for image in images:
        key = image.stem
        md = trans_map.get(key)
        md_link = f"[{md.name}]({md_rel(folder / 'index.md', md)})" if md else "待生成"
        image_link = md_rel(folder / "index.md", image)
        lines.append(f"| {int(key.split('-')[1])} | [{image.name}]({image_link}) | {md_link} |")
    lines.append("")
    (folder / "index.md").write_text("\n".join(lines), encoding="utf-8")


def write_index(folder: Path, pdf_path: Path, page_count: int) -> None:
    pages = sorted((folder / "pages").glob("page-*.png"))
    transcribed = sorted((folder / "transcribed").glob("page-*.md"))
    lines = [
        f"# {pdf_path.stem} 视觉转写索引",
        "",
        f"- 源文件：`{rel(pdf_path)}`",
        f"- PDF 页数：{page_count}",
        f"- 更新时间：{now()}",
        "- 转写方式：视觉阅读 + LaTeX 手工整理，不使用 OCR",
        "",
        "| 页码 | 页图 | 转写稿 |",
        "|---:|---|---|",
    ]
    trans_map = {p.stem: p for p in transcribed}
    for image in pages:
        key = image.stem
        md = trans_map.get(key)
        md_link = f"[{md.name}]({md_rel(folder / 'index.md', md)})" if md else "待生成"
        image_link = md_rel(folder / "index.md", image)
        lines.append(f"| {int(key.split('-')[1])} | [{image.name}]({image_link}) | {md_link} |")
    lines.append("")
    (folder / "index.md").write_text("\n".join(lines), encoding="utf-8")


def write_root_index() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 数学资料视觉 LaTeX 转写",
        "",
        f"- 更新时间：{now()}",
        "- 原则：不使用 OCR；先渲染页图，再由视觉阅读整理为 LaTeX Markdown。",
        "- 不确定的公式、页码、题号统一标记 `[待核对]`。",
        "",
        "## PDF 资料目录",
        "",
    ]
    for folder in sorted(p for p in OUT_DIR.iterdir() if p.is_dir()):
        if folder.name == "manual-batches":
            continue
        index = folder / "index.md"
        if index.exists():
            lines.append(f"- [{folder.name}]({md_rel(OUT_DIR / 'README.md', index)})")
    manual_root = OUT_DIR / "manual-batches"
    if manual_root.exists():
        lines.extend(["", "## 照片批次目录", ""])
        for folder in sorted(p for p in manual_root.iterdir() if p.is_dir()):
            index = folder / "index.md"
            if index.exists():
                lines.append(f"- [{folder.name}]({md_rel(OUT_DIR / 'README.md', index)})")
    lines.extend(
        [
            "",
            "## 使用方式",
            "",
            "```powershell",
            "python tools\\math_visual_latex_pipeline.py --pdf '工科数学分析基础 上册.pdf' --start 18 --end 24 --zoom 2.0",
            "python tools\\math_visual_latex_pipeline.py --image-dir 'temp\\math\\new-photos' --batch-name '2026-05-20-绪论'",
            "```",
            "",
        ]
    )
    (OUT_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_exam_filters() -> None:
    items_path = MATH_DIR / "bump_items.json"
    if not items_path.exists():
        return
    data = json.loads(items_path.read_text(encoding="utf-8"))
    lines = [
        "# 试卷筛选清单（视觉转写用）",
        "",
        f"- 来源：`{rel(items_path)}`",
        f"- 更新时间：{now()}",
        "",
    ]
    for key, title in [("highmath", "高等数学"), ("engmath", "工科数学分析 / 数学分析")]:
        papers = data.get(key, [])
        lines.extend(
            [
                f"## {title}",
                "",
                "| 编号 | 标题 | PDF 页码 |",
                "|---:|---|---:|",
            ]
        )
        for item in papers:
            number = str(item["title"]).split(" ", 1)[0]
            pages = f"{item['page_start']}-{item['page_end']}"
            lines.append(f"| {number} | {item['title']} | {pages} |")
        lines.append("")
    (OUT_DIR / "exam-filter-index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", choices=PDFS + ["all"], default="all")
    parser.add_argument("--image-dir", type=Path)
    parser.add_argument("--batch-name")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=1)
    parser.add_argument("--zoom", type=float, default=2.0)
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if args.image_dir:
        ingest_image_dir(args.image_dir, args.batch_name)
    else:
        selected = PDFS if args.pdf == "all" else [args.pdf]
        for name in selected:
            path = MATH_DIR / name
            if path.exists():
                render_pdf(path, args.start, args.end, args.zoom)
    write_exam_filters()
    write_root_index()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
