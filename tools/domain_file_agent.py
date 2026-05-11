#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Domain File Agent

Search and download files under a specified domain.

Examples:
  python tools/domain_file_agent.py https://example.com --ext pdf,zip --keyword edge-ai --dry-run
  python tools/domain_file_agent.py https://example.com/docs/ --ext pdf,docx,pptx --output downloads/example
"""

from __future__ import annotations

import argparse
import hashlib
import html.parser
import os
import posixpath
import re
import sys
import time
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import ParseResult, unquote, urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen


DEFAULT_EXTENSIONS = {
    "pdf",
    "doc",
    "docx",
    "ppt",
    "pptx",
    "xls",
    "xlsx",
    "csv",
    "zip",
    "rar",
    "7z",
    "tar",
    "gz",
    "md",
    "txt",
}

HTML_TYPES = ("text/html", "application/xhtml+xml")
USER_AGENT = "DomainFileAgent/1.0 (+https://github.com/local-learning-workspace)"


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_names = ("href", "src") if tag in {"a", "link", "script", "img"} else ("href",)
        for name, value in attrs:
            if name.lower() in attr_names and value:
                self.links.append(value.strip())


@dataclass(frozen=True)
class CandidateFile:
    url: str
    source_page: str
    extension: str


def normalize_start_url(raw_url: str) -> str:
    parsed = urlparse(raw_url)
    if not parsed.scheme:
        raw_url = "https://" + raw_url
        parsed = urlparse(raw_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"Invalid URL: {raw_url}")
    return raw_url


def same_domain(url: str, root: ParseResult, include_subdomains: bool) -> bool:
    parsed = urlparse(url)
    host = parsed.hostname or ""
    root_host = root.hostname or ""
    if include_subdomains:
        return host == root_host or host.endswith("." + root_host)
    return host == root_host


def clean_url(url: str) -> str:
    return urldefrag(url)[0]


def fetch(url: str, timeout: int) -> tuple[bytes, str]:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=timeout) as resp:
        content_type = resp.headers.get("Content-Type", "")
        return resp.read(), content_type


def parse_links(html_bytes: bytes, page_url: str) -> list[str]:
    text = html_bytes.decode("utf-8", errors="replace")
    parser = LinkParser()
    parser.feed(text)
    return [clean_url(urljoin(page_url, link)) for link in parser.links]


def url_extension(url: str) -> str:
    path = urlparse(url).path
    suffix = posixpath.splitext(path)[1].lower().lstrip(".")
    return suffix


def text_matches(url: str, keywords: list[str]) -> bool:
    if not keywords:
        return True
    lowered = unquote(url).lower()
    return all(keyword.lower() in lowered for keyword in keywords)


def should_visit_page(url: str) -> bool:
    ext = url_extension(url)
    return not ext or ext in {"html", "htm", "php", "asp", "aspx", "jsp"}


def safe_filename(url: str, output_dir: Path) -> Path:
    parsed = urlparse(url)
    raw_name = unquote(posixpath.basename(parsed.path.rstrip("/")))
    if not raw_name:
        raw_name = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    raw_name = re.sub(r'[<>:"/\\|?*\x00-\x1f]+', "_", raw_name).strip(" ._")
    if not raw_name:
        raw_name = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]

    target = output_dir / raw_name
    if not target.exists():
        return target

    stem = target.stem
    suffix = target.suffix
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    return output_dir / f"{stem}-{digest}{suffix}"


def parse_extensions(raw: str) -> set[str]:
    if raw.strip().lower() in {"all", "*"}:
        return set()
    return {item.strip().lower().lstrip(".") for item in raw.split(",") if item.strip()}


def crawl(
    start_url: str,
    extensions: set[str],
    keywords: list[str],
    max_pages: int,
    timeout: int,
    delay: float,
    include_subdomains: bool,
) -> list[CandidateFile]:
    root = urlparse(start_url)
    queue: deque[str] = deque([start_url])
    visited_pages: set[str] = set()
    seen_files: set[str] = set()
    files: list[CandidateFile] = []

    while queue and len(visited_pages) < max_pages:
        page_url = queue.popleft()
        if page_url in visited_pages:
            continue
        if not same_domain(page_url, root, include_subdomains):
            continue
        if not should_visit_page(page_url):
            continue

        visited_pages.add(page_url)
        print(f"[scan] {len(visited_pages):04d} {page_url}")

        try:
            body, content_type = fetch(page_url, timeout)
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            print(f"  [skip] {exc}")
            continue

        if not any(kind in content_type.lower() for kind in HTML_TYPES):
            continue

        for link in parse_links(body, page_url):
            if not link or not same_domain(link, root, include_subdomains):
                continue

            ext = url_extension(link)
            if ext and (not extensions or ext in extensions) and text_matches(link, keywords):
                if link not in seen_files:
                    seen_files.add(link)
                    files.append(CandidateFile(link, page_url, ext))
                    print(f"  [file] {link}")
                continue

            if should_visit_page(link) and link not in visited_pages:
                queue.append(link)

        if delay > 0:
            time.sleep(delay)

    return files


def download_files(files: Iterable[CandidateFile], output_dir: Path, timeout: int, delay: float) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = output_dir / "download_manifest.tsv"

    with manifest.open("w", encoding="utf-8", newline="\n") as index:
        index.write("filename\turl\tsource_page\textension\n")
        for item in files:
            target = safe_filename(item.url, output_dir)
            print(f"[download] {item.url}")
            try:
                content, _ = fetch(item.url, timeout)
            except (HTTPError, URLError, TimeoutError, OSError) as exc:
                print(f"  [failed] {exc}")
                continue

            target.write_bytes(content)
            index.write(f"{target.name}\t{item.url}\t{item.source_page}\t{item.extension}\n")
            if delay > 0:
                time.sleep(delay)

    print(f"[done] manifest: {manifest}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Search and download files from a specified domain.",
    )
    parser.add_argument("url", help="Start URL or domain, for example https://example.com/docs/")
    parser.add_argument(
        "--ext",
        default=",".join(sorted(DEFAULT_EXTENSIONS)),
        help="Comma-separated extensions. Use 'all' to accept any file extension.",
    )
    parser.add_argument(
        "--keyword",
        action="append",
        default=[],
        help="Keyword that must appear in the file URL. Repeat this option for multiple required keywords.",
    )
    parser.add_argument("--output", default="downloads/domain-files", help="Directory for downloaded files.")
    parser.add_argument("--max-pages", type=int, default=300, help="Maximum HTML pages to scan.")
    parser.add_argument("--timeout", type=int, default=25, help="Request timeout in seconds.")
    parser.add_argument("--delay", type=float, default=0.3, help="Delay between requests in seconds.")
    parser.add_argument("--include-subdomains", action="store_true", help="Allow subdomains of the root domain.")
    parser.add_argument("--dry-run", action="store_true", help="Only list matching files; do not download.")
    return parser


def main(argv: list[str] | None = None) -> int:
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    args = build_parser().parse_args(argv)
    try:
        start_url = normalize_start_url(args.url)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    extensions = parse_extensions(args.ext)
    files = crawl(
        start_url=start_url,
        extensions=extensions,
        keywords=args.keyword,
        max_pages=args.max_pages,
        timeout=args.timeout,
        delay=args.delay,
        include_subdomains=args.include_subdomains,
    )

    print(f"\nFound {len(files)} matching file(s).")
    for item in files:
        print(f"- [{item.extension}] {item.url}")

    if args.dry_run:
        return 0

    download_files(files, Path(args.output), timeout=args.timeout, delay=args.delay)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
