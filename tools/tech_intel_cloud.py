#!/usr/bin/env python
"""Cloud runner for Ethen's daily AI tech intelligence brief.

This script is designed for GitHub Actions. It fetches public sources,
generates Obsidian-friendly reports under tech-intel/YYYY-MM-DD/, and can
send the email brief through SMTP when secrets are configured.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import smtplib
import sys
import textwrap
import time
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import requests
import yaml
from bs4 import BeautifulSoup


WORKSPACE = Path(__file__).resolve().parents[1]
TECH_INTEL_DIR = WORKSPACE / "tech-intel"
SOURCES_PATH = TECH_INTEL_DIR / "sources.yaml"
TIMEZONE = ZoneInfo("Asia/Shanghai")

DEFAULT_TO = "Suerzong@outlook.com"
USER_AGENT = (
    "Edge-AI-Tech-Intel/1.0 "
    "(daily personal learning brief; contact via repository owner)"
)

EDGE_KEYWORDS = {
    "edge ai": 6,
    "on-device": 6,
    "端侧": 6,
    "embedded": 5,
    "tinyml": 5,
    "quantization": 5,
    "量化": 5,
    "compression": 4,
    "onnx": 5,
    "onnx runtime": 6,
    "executorch": 6,
    "tensorrt": 5,
    "openvino": 4,
    "liteRT": 4,
    "webgpu": 4,
    "risc-v": 5,
    "jetson": 5,
    "rk3588": 5,
    "npu": 4,
    "mcu": 4,
    "stm32": 4,
    "esp32": 4,
    "yolo": 4,
    "real-time": 4,
    "computer vision": 3,
    "local ai": 4,
    "llama.cpp": 4,
    "whisper.cpp": 4,
}

FOUNDATION_KEYWORDS = {
    "openai": 2,
    "anthropic": 2,
    "deepmind": 2,
    "google": 1,
    "meta ai": 2,
    "pytorch": 3,
    "cuda": 3,
    "nvidia": 3,
    "semiconductor": 2,
    "inference": 4,
    "deployment": 4,
    "release": 2,
    "paper": 2,
    "benchmark": 2,
}


@dataclass
class FetchStatus:
    source_id: str
    name: str
    method: str
    status: str
    count: int = 0
    note: str = ""


@dataclass
class Item:
    title: str
    url: str
    source: str
    source_type: str
    published_at: str = ""
    summary: str = ""
    body_digest: list[str] = field(default_factory=list)
    key_excerpt: str = ""
    tags: list[str] = field(default_factory=list)
    importance: int = 1
    relevance: int = 1
    confidence: str = "medium"
    action_value: list[str] = field(default_factory=list)
    student_readability: str = ""
    current_stage_relation: str = ""
    raw_text_hash: str = ""
    fetch_status: str = "success"


def now_date() -> str:
    return datetime.now(TIMEZONE).strftime("%Y-%m-%d")


def read_text(path: Path, limit: int = 6000) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    return text[:limit]


def load_sources() -> list[dict[str, Any]]:
    data = yaml.safe_load(SOURCES_PATH.read_text(encoding="utf-8"))
    return [s for s in data.get("sources", []) if s.get("enabled", True)]


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json, text/html;q=0.9, */*;q=0.8"})
    token = os.getenv("GITHUB_TOKEN", "").strip()
    if token:
        s.headers.update({"Authorization": f"Bearer {token}"})
    return s


def safe_get(s: requests.Session, url: str, *, timeout: int = 15, params: dict[str, Any] | None = None) -> requests.Response:
    resp = s.get(url, timeout=timeout, params=params)
    resp.raise_for_status()
    return resp


def clean(text: str, limit: int = 500) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def first_sentences(text: str, count: int = 2, limit: int = 420) -> str:
    text = clean(text, limit=2000)
    if not text:
        return ""
    parts = re.split(r"(?<=[。！？.!?])\s+", text)
    return clean(" ".join(parts[:count]), limit=limit)


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()[:16]


def parse_date(value: str) -> str:
    if not value:
        return ""
    value = value.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(value).astimezone(TIMEZONE).strftime("%Y-%m-%d")
    except ValueError:
        return value[:10]


def confidence_for(source: dict[str, Any]) -> str:
    tier = source.get("tier", "")
    method = source.get("method", "")
    if tier == "primary" or method in {"github_releases", "arxiv_api", "arxiv_recent"}:
        return "high"
    if tier == "secondary":
        return "medium"
    return "low"


def source_tags(source: dict[str, Any]) -> list[str]:
    tags = source.get("relevance_tags") or []
    return [str(t) for t in tags][:6]


def make_item(
    source: dict[str, Any],
    title: str,
    url: str,
    summary: str = "",
    published_at: str = "",
    body: str = "",
) -> Item:
    raw = "\n".join([title, url, summary, body])
    return Item(
        title=clean(title, 180),
        url=url,
        source=source.get("name", source.get("id", "unknown")),
        source_type=source.get("method", "unknown"),
        published_at=parse_date(published_at),
        summary=first_sentences(summary or body, count=2),
        body_digest=digest_points(summary or body),
        key_excerpt=clean(first_sentences(body or summary, count=1), 220),
        tags=source_tags(source),
        confidence=confidence_for(source),
        raw_text_hash=hash_text(raw),
    )


def digest_points(text: str) -> list[str]:
    text = clean(text, limit=1200)
    if not text:
        return []
    chunks = re.split(r"(?<=[。！？.!?])\s+", text)
    points = [clean(c, 180) for c in chunks if len(clean(c)) > 20]
    return points[:4]


def fetch_github_releases(s: requests.Session, source: dict[str, Any]) -> list[Item]:
    repo = source["repo"]
    url = f"https://api.github.com/repos/{repo}/releases"
    data = safe_get(s, url, params={"per_page": 4}).json()
    items = []
    for release in data[:4]:
        title = release.get("name") or release.get("tag_name") or repo
        body = release.get("body") or ""
        items.append(
            make_item(
                source,
                title=f"{repo}: {title}",
                url=release.get("html_url") or f"https://github.com/{repo}/releases",
                summary=body,
                published_at=release.get("published_at") or release.get("created_at") or "",
                body=body,
            )
        )
    return items


def fetch_github_search(s: requests.Session, source: dict[str, Any]) -> list[Item]:
    query = source.get("query", "")
    data = safe_get(
        s,
        "https://api.github.com/search/repositories",
        params={"q": query, "sort": "updated", "order": "desc", "per_page": 5},
    ).json()
    items = []
    for repo in data.get("items", [])[:5]:
        desc = repo.get("description") or ""
        stars = repo.get("stargazers_count", 0)
        summary = f"{desc} Stars: {stars}. Updated: {repo.get('updated_at', '')}."
        items.append(
            make_item(
                source,
                title=repo.get("full_name", "GitHub repository"),
                url=repo.get("html_url", ""),
                summary=summary,
                published_at=repo.get("updated_at", ""),
                body=summary,
            )
        )
    return items


def fetch_arxiv_api(s: requests.Session, source: dict[str, Any]) -> list[Item]:
    params = {
        "search_query": source.get("query", "cat:cs.LG"),
        "start": 0,
        "max_results": min(int(source.get("max_results", 10)), 10),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    resp = safe_get(s, source.get("url", "https://export.arxiv.org/api/query"), params=params, timeout=20)
    root = ET.fromstring(resp.content)
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    items = []
    for entry in root.findall("atom:entry", ns)[:10]:
        title = clean(entry.findtext("atom:title", default="", namespaces=ns), 220)
        summary = entry.findtext("atom:summary", default="", namespaces=ns)
        link = ""
        for link_el in entry.findall("atom:link", ns):
            if link_el.attrib.get("rel") == "alternate":
                link = link_el.attrib.get("href", "")
                break
        items.append(
            make_item(
                source,
                title=title,
                url=link,
                summary=summary,
                published_at=entry.findtext("atom:published", default="", namespaces=ns),
                body=summary,
            )
        )
    return items


def fetch_arxiv_recent(s: requests.Session, source: dict[str, Any]) -> list[Item]:
    resp = safe_get(s, source["url"], timeout=20)
    soup = BeautifulSoup(resp.text, "html.parser")
    items = []
    for dt in soup.select("dl dt")[:8]:
        dd = dt.find_next_sibling("dd")
        title_el = dd.select_one(".list-title") if dd else None
        abs_link = dt.find("a", title="Abstract")
        if not title_el or not abs_link:
            continue
        title = title_el.get_text(" ", strip=True).replace("Title:", "").strip()
        url = "https://arxiv.org" + abs_link.get("href", "")
        authors = dd.select_one(".list-authors").get_text(" ", strip=True) if dd.select_one(".list-authors") else ""
        summary = f"{title}. {authors}"
        items.append(make_item(source, title=title, url=url, summary=summary, body=summary))
    return items


def fetch_hf_papers(s: requests.Session, source: dict[str, Any]) -> list[Item]:
    urls = [source.get("url", ""), "https://huggingface.co/api/daily_papers?limit=20"]
    data = None
    last_error = None
    for url in [u for u in urls if u]:
        try:
            data = safe_get(s, url, timeout=15).json()
            break
        except Exception as exc:  # noqa: BLE001
            last_error = exc
    if data is None:
        raise RuntimeError(f"HF papers unavailable: {last_error}")
    rows = data if isinstance(data, list) else data.get("papers", [])
    items = []
    for row in rows[:8]:
        paper = row.get("paper") if isinstance(row, dict) else None
        record = paper if isinstance(paper, dict) else row
        title = record.get("title") or record.get("paperTitle") or "Hugging Face paper"
        paper_id = record.get("id") or record.get("paperId") or record.get("arxivId") or ""
        url = record.get("url") or (f"https://huggingface.co/papers/{paper_id}" if paper_id else "https://huggingface.co/papers")
        summary = record.get("summary") or record.get("abstract") or ""
        items.append(make_item(source, title=title, url=url, summary=summary, body=summary))
    return items


def fetch_hn_algolia(s: requests.Session, source: dict[str, Any]) -> list[Item]:
    data = safe_get(
        s,
        source.get("url", "https://hn.algolia.com/api/v1/search_by_date"),
        params={"query": source.get("query", "AI"), "tags": "story", "hitsPerPage": 8},
    ).json()
    items = []
    for hit in data.get("hits", [])[:8]:
        title = hit.get("title") or hit.get("story_title") or "Hacker News story"
        url = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
        points = hit.get("points", 0)
        comments = hit.get("num_comments", 0)
        summary = f"Hacker News discussion. Points: {points}; comments: {comments}."
        items.append(make_item(source, title=title, url=url, summary=summary, published_at=hit.get("created_at", ""), body=summary))
    return items


def fetch_html_links(s: requests.Session, source: dict[str, Any]) -> list[Item]:
    url = source.get("url")
    resp = safe_get(s, url, timeout=15)
    soup = BeautifulSoup(resp.text, "html.parser")
    page_title = clean(soup.title.get_text(" ", strip=True) if soup.title else source.get("name", "web page"), 160)
    meta = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
    meta_text = meta.get("content", "") if meta else ""
    items = [make_item(source, title=page_title, url=url, summary=meta_text, body=meta_text)]

    seen: set[str] = {url}
    base = requests.compat.urlparse(url)
    for a in soup.find_all("a", href=True)[:120]:
        title = clean(a.get_text(" ", strip=True), 150)
        href = requests.compat.urljoin(url, a["href"])
        if not title or len(title) < 12 or href in seen:
            continue
        parsed = requests.compat.urlparse(href)
        if parsed.netloc and parsed.netloc != base.netloc:
            continue
        if any(skip in href.lower() for skip in ["login", "privacy", "terms", "cookie", "#"]):
            continue
        seen.add(href)
        items.append(make_item(source, title=title, url=href, summary=f"来自 {source.get('name')} 的公开页面链接。"))
        if len(items) >= 5:
            break
    return items


def fetch_source(s: requests.Session, source: dict[str, Any]) -> tuple[list[Item], FetchStatus]:
    method = source.get("method", "html")
    start = time.time()
    try:
        if method == "github_releases":
            items = fetch_github_releases(s, source)
        elif method == "github_search":
            items = fetch_github_search(s, source)
        elif method == "arxiv_api":
            items = fetch_arxiv_api(s, source)
        elif method == "arxiv_recent":
            items = fetch_arxiv_recent(s, source)
        elif method == "hf_papers":
            items = fetch_hf_papers(s, source)
        elif method == "hn_algolia":
            items = fetch_hn_algolia(s, source)
        else:
            items = fetch_html_links(s, source)
        note = f"{time.time() - start:.1f}s"
        return items, FetchStatus(source.get("id", ""), source.get("name", ""), method, "success", len(items), note)
    except requests.HTTPError as exc:
        status = "rate_limited" if exc.response is not None and exc.response.status_code in {403, 429} else "failed"
        code = exc.response.status_code if exc.response is not None else "unknown"
        return [], FetchStatus(source.get("id", ""), source.get("name", ""), method, status, 0, f"HTTP {code}: {exc}")
    except Exception as exc:  # noqa: BLE001
        return [], FetchStatus(source.get("id", ""), source.get("name", ""), method, "failed", 0, str(exc)[:220])


def score_items(items: list[Item]) -> list[Item]:
    for item in items:
        text = " ".join([item.title, item.summary, " ".join(item.tags)]).lower()
        score = 0
        for key, weight in EDGE_KEYWORDS.items():
            if key.lower() in text:
                score += weight
        for key, weight in FOUNDATION_KEYWORDS.items():
            if key.lower() in text:
                score += weight
        if item.confidence == "high":
            score += 2
        elif item.confidence == "medium":
            score += 1
        item.relevance = max(1, min(5, 1 + score // 5))
        item.importance = max(1, min(5, 1 + score // 6))
        if item.importance >= 4:
            item.action_value = ["值得看", "可加入知识库"]
        elif item.importance == 3:
            item.action_value = ["了解即可"]
        else:
            item.action_value = ["低优先级"]
        item.student_readability = readability_note(item)
        item.current_stage_relation = stage_relation(item)
    return sorted(items, key=lambda x: (x.importance, x.relevance, confidence_rank(x.confidence), x.published_at), reverse=True)


def confidence_rank(conf: str) -> int:
    return {"high": 3, "medium": 2, "low": 1, "unverified": 0}.get(conf, 1)


def readability_note(item: Item) -> str:
    if item.relevance >= 4:
        return "本科生可以先读结论和例子，遇到部署、量化、推理引擎等术语时只需建立方向感。"
    if item.source_type in {"arxiv_api", "arxiv_recent"}:
        return "论文内容可能偏难，当前阶段先读标题、摘要和是否有代码即可。"
    return "可快速浏览，重点看它是否能转化为课程学习、项目实践或长期方向判断。"


def stage_relation(item: Item) -> str:
    text = " ".join([item.title, item.summary]).lower()
    if any(k in text for k in ["cnn", "vision", "yolo", "computer vision"]):
        return "和你正在学的神经网络/CNN 主线有关，适合收藏后在学完基础卷积网络后回看。"
    if any(k in text for k in ["onnx", "executorch", "tensorrt", "inference", "deployment", "quantization"]):
        return "对应 Edge AI 的模型部署与端侧优化阶段，现在先建立工具链地图，暂不急着复现。"
    if any(k in text for k in ["embedded", "risc-v", "mcu", "npu", "jetson"]):
        return "对应嵌入式 AI 与硬件平台方向，适合放入长期项目雷达。"
    return "作为 AI 前沿环境感知即可，不要打断今天的课程主线。"


def dedupe(items: list[Item]) -> list[Item]:
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    out = []
    for item in items:
        url_key = item.url.rstrip("/")
        title_key = re.sub(r"\W+", "", item.title.lower())[:90]
        if url_key in seen_urls or title_key in seen_titles:
            continue
        seen_urls.add(url_key)
        seen_titles.add(title_key)
        out.append(item)
    return out


def topic_line(top: list[Item]) -> str:
    text = " ".join([i.title + " " + i.summary for i in top[:5]]).lower()
    if any(k in text for k in ["onnx", "executorch", "tensorrt", "inference", "deployment", "quantization", "edge"]):
        return "端侧推理与部署工具链升温"
    if any(k in text for k in ["agent", "rag", "search"]):
        return "Agent 与检索系统继续演进"
    if any(k in text for k in ["nvidia", "amd", "intel", "tsmc", "asml", "semiconductor"]):
        return "AI 算力与半导体信号增强"
    if any(k in text for k in ["openai", "anthropic", "deepmind", "meta"]):
        return "大模型产品与研究继续更新"
    return "AI 工具链与开源生态继续演进"


def group_items(items: list[Item]) -> dict[str, list[Item]]:
    groups = {
        "官方源：模型、产品、API 与开发者生态": [],
        "论文与代码：技术趋势源头": [],
        "Edge AI / 嵌入式 AI 动态": [],
        "GitHub 开源项目与工程信号": [],
        "新产品、创业与产业信号": [],
        "中文信息源二次筛选": [],
    }
    for item in items:
        st = item.source_type
        src = item.source.lower()
        tags = " ".join(item.tags).lower()
        text = f"{item.title} {item.summary} {tags}".lower()
        if st in {"arxiv_api", "arxiv_recent", "hf_papers"} or "paper" in tags:
            groups["论文与代码：技术趋势源头"].append(item)
        elif any(k in text for k in ["edge", "on-device", "onnx", "executorch", "tensorrt", "embedded", "npu", "mcu", "jetson", "risc-v"]):
            groups["Edge AI / 嵌入式 AI 动态"].append(item)
        elif st in {"github_releases", "github_search"} or "github" in src:
            groups["GitHub 开源项目与工程信号"].append(item)
        elif any(k in src for k in ["product", "launch", "yc", "semianalysis", "stratechery", "information"]):
            groups["新产品、创业与产业信号"].append(item)
        elif any(k in src for k in ["机器", "量子", "36", "latepost", "ifanr", "半导体"]):
            groups["中文信息源二次筛选"].append(item)
        else:
            groups["官方源：模型、产品、API 与开发者生态"].append(item)
    return groups


def item_block(item: Item, idx: int) -> str:
    digest = "\n".join([f"  - {p}" for p in item.body_digest[:4]]) or "  - 暂无可稳定提取的正文要点，先保留标题、摘要与原始链接。"
    excerpt = item.key_excerpt or "无可安全摘录的短句。"
    return textwrap.dedent(
        f"""
        ### {idx}. {item.title}

        - 来源：{item.source}
        - 原始链接：{item.url}
        - 领域标签：{", ".join(item.tags) if item.tags else "未标注"}
        - 可信度：{item.confidence}
        - 重要性评分：{item.importance}/5
        - 相关性评分：{item.relevance}/5
        - 行动价值：{", ".join(item.action_value)}
        - 一句话结论：{item.summary or "这条信息值得保留原始链接，等待进一步核验。"}
        - 这是什么：来自 {item.source} 的公开信号，类型为 {item.source_type}。
        - 正文速读：
{digest}
        - 关键原文短摘：{excerpt}
        - 本科生可读解释：{item.student_readability}
        - 为什么重要：它有助于判断 AI 工具链、端侧部署、开源项目或产业方向的变化。
        - 和我当前阶段的关系：{item.current_stage_relation}
        - 建议行动：{item.action_value[0] if item.action_value else "收藏观察"}
        """
    ).strip()


def compact_item_line(item: Item) -> str:
    return f"- [{item.title}]({item.url})｜{item.source}｜重要性 {item.importance}/5｜{item.summary or '保留链接待回看'}"


def trend_analysis(top: list[Item]) -> str:
    text = " ".join([i.title + " " + i.summary for i in top[:8]]).lower()
    bullets = []
    if any(k in text for k in ["onnx", "executorch", "tensorrt", "inference", "deployment", "quantization", "edge"]):
        bullets.append("端侧推理正在从研究话题变成工程主线。未来岗位不只看会不会训练模型，还会看能否把模型部署到真实设备。")
    if any(k in text for k in ["risc-v", "npu", "mcu", "jetson", "webgpu", "semiconductor", "nvidia", "intel", "amd"]):
        bullets.append("硬件适配和系统理解会继续变重要。Edge AI 工程师需要逐步补上计算机系统、嵌入式硬件和推理框架的连接关系。")
    if any(k in text for k in ["agent", "rag", "search", "local ai", "llm"]):
        bullets.append("大模型应用正在向本地化、检索增强和 Agent 工程演进，但现在不宜压过神经网络与嵌入式基础。")
    if not bullets:
        bullets.append("今天的信号更偏生态更新，适合作为环境感知，不需要改变当前学习节奏。")
    bullets.append("未来 3-6 个月建议保持三条主线：CNN/PyTorch 基础、嵌入式硬件基础、ONNX/端侧部署工具链地图。")
    return "\n".join(f"- {b}" for b in bullets[:4])


def generate_report(date: str, items: list[Item], statuses: list[FetchStatus]) -> tuple[str, str, str]:
    top = items[:5]
    topic = topic_line(top)
    groups = group_items(items)
    today_summary = [
        f"今日核心趋势：{topic}。",
        f"共保留 {len(items)} 条候选信号，其中 Top 5 优先用于晨读。",
        "一手来源、论文代码和 GitHub 工程信号优先；中文源只作为二次筛选线索。",
        "今天行动仍要服务当前学习主线：神经网络基础、CNN、池化/stride 与 LeNet-5 维度计算。",
    ]
    failed = [s for s in statuses if s.status != "success"]
    if failed:
        today_summary.append(f"抓取异常 {len(failed)} 个，已放到文末附录。")

    frontmatter = textwrap.dedent(
        f"""\
        ---
        title: "Daily Tech Intelligence Report - {date}"
        date: {date}
        type: tech-intel
        tags:
          - tech-intel
          - edge-ai
          - ai-news
        aliases:
          - "{date} AI 科技情报"
        top_topics:
          - "{topic}"
        status: final
        ---
        """
    )

    top_blocks = "\n\n".join(item_block(item, idx + 1) for idx, item in enumerate(top))

    group_sections = []
    for title, group in groups.items():
        lines = [f"## {title}", ""]
        if group:
            lines.extend(compact_item_line(i) for i in group[:5])
        else:
            lines.append("- 今日未抓到高价值条目。")
        group_sections.append("\n".join(lines))

    actions = textwrap.dedent(
        """
        1. 先完成今天神经网络练习：池化输出尺寸、stride、LeNet-5 参数量与展平维度。
        2. 若还有 10 分钟，只浏览 Top 5 中最相关的一条原始链接，建立方向感即可。
        3. 把 ONNX Runtime、ExecuTorch、TensorRT、端侧量化这些词放入长期地图，不急着立刻复现。
        """
    ).strip()

    knowledge_entries = "\n".join(
        f"- [[{item.title}]]：{item.summary or item.source} 来源：{item.url}" for item in top[:3]
    )

    status_rows = "\n".join(
        f"| {s.name} | {s.method} | {s.status} | {s.count} | {s.note.replace('|', '/')} |" for s in statuses
    )
    primary_overview = "\n".join(compact_item_line(i) for i in items[:12]) or "- 今日没有可用信号。"
    low_value = "\n".join(compact_item_line(i) for i in items[-3:]) if len(items) > 8 else "- 今日不单独列出。"

    report = "\n\n".join(
        [
            frontmatter,
            "# Daily Tech Intelligence Report",
            f"日期：{date}",
            "## 今日摘要\n\n" + "\n".join(f"- {line}" for line in today_summary),
            "## 1. 今日最重要的 5 条信息\n\n" + (top_blocks or "- 今日没有足够的高价值信号。"),
            *group_sections,
            "## 9. 今日行动建议\n\n" + actions,
            "## 10. 可写入知识库的条目\n\n" + knowledge_entries,
            "## 11. 时代动向分析：对学习与就业方向的启发\n\n" + trend_analysis(top),
            "## 附录 A：抓取状态\n\n| 来源 | 方法 | 状态 | 条目数 | 备注 |\n| --- | --- | --- | ---: | --- |\n" + status_rows,
            "## 附录 B：一手信号总览\n\n" + primary_overview,
            "## 附录 C：低价值 / 不建议看的信息\n\n" + low_value,
            "",
        ]
    )

    email_subject = f"{date} AI晨报：{topic}"
    email_body = generate_email_body(date, topic, top, failed)
    email_file = "\n".join(
        [
            "<!-- EMAIL_SUBJECT -->",
            email_subject,
            "<!-- EMAIL_BODY_START -->",
            "",
            email_body,
            "",
            "<!-- EMAIL_BODY_END -->",
            "",
        ]
    )
    return report, email_file, email_subject


def generate_email_body(date: str, topic: str, top: list[Item], failed: list[FetchStatus]) -> str:
    summary_lines = [
        f"今天一句话：{topic}。",
        "一手来源和工程信号优先，中文源只做线索过滤。",
        "今天最值得注意的是端侧推理、模型部署、开源工具链和本地 AI 的组合趋势。",
        "对你当前阶段来说，先守住神经网络基础，不被新闻流带跑。",
        "高价值链接已保留在 Obsidian 全文，手机邮件只做晨读导读。",
    ]
    top_lines = []
    for idx, item in enumerate(top[:5], 1):
        top_lines.append(f"{idx}. **{item.title}**：{item.summary or '保留原始链接，适合稍后回看。'}")
    while len(top_lines) < 5:
        top_lines.append(f"{len(top_lines) + 1}. 今日暂无更多高价值条目，保持主线学习优先。")
    links = [f"- {item.title}：{item.url}" for item in top[:5]]
    exceptions = [f"- {s.name}：{s.status}，{s.note}" for s in failed[:5]] or ["- 今日没有影响结论的关键抓取异常。"]

    return "\n\n".join(
        [
            f"# {date} AI 科技情报",
            "Ethen，早上好！",
            "## 今日一句话总览\n\n" + f"今天最重要的信号是：{topic}。",
            "## 5 行摘要\n\n" + "\n".join(f"- {line}" for line in summary_lines),
            "## Top 5 简报\n\n" + "\n\n".join(top_lines),
            "## 今日时代动向\n\n" + trend_analysis(top),
            "## 今天建议\n\n1. 先完成池化、stride、LeNet-5 参数量和展平维度练习。\n2. 只挑 1 条 Top 链接浏览，不要让晨报压过今天主线。\n3. 把端侧部署工具链作为长期地图，等基础稳了再复现项目。",
            "## 关键链接\n\n" + "\n".join(links),
            "## 抓取异常\n\n" + "\n".join(exceptions),
            f"## Obsidian 全文\n\n`tech-intel/{date}/tech-intel-{date}.md`",
        ]
    )


def save_outputs(date: str, report: str, email_file: str, items: list[Item], statuses: list[FetchStatus], overwrite: bool) -> Path:
    day_dir = TECH_INTEL_DIR / date
    day_dir.mkdir(parents=True, exist_ok=True)
    report_path = day_dir / f"tech-intel-{date}.md"
    email_path = day_dir / f"email-{date}.md"
    raw_path = day_dir / f"raw-index-{date}.json"

    if not overwrite and report_path.exists() and email_path.exists() and raw_path.exists():
        print(f"Existing report found for {date}; keeping current files. Use --overwrite to regenerate.")
        return day_dir

    report_path.write_text(report, encoding="utf-8")
    email_path.write_text(email_file, encoding="utf-8")
    raw = {
        "date": date,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "timezone": "Asia/Shanghai",
        "items": [asdict(i) for i in items],
        "fetch_statuses": [asdict(s) for s in statuses],
    }
    raw_path.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {report_path}")
    print(f"Wrote {email_path}")
    print(f"Wrote {raw_path}")
    return day_dir


def parse_email_file(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    subject_match = re.search(r"<!-- EMAIL_SUBJECT -->\s*(.*?)\s*<!-- EMAIL_BODY_START -->", text, re.S)
    body_match = re.search(r"<!-- EMAIL_BODY_START -->\s*(.*?)\s*<!-- EMAIL_BODY_END -->", text, re.S)
    subject = clean(subject_match.group(1), 180) if subject_match else f"{now_date()} AI晨报"
    body = body_match.group(1).strip() if body_match else text
    return subject, body


def send_email(subject: str, body: str) -> bool:
    host = os.getenv("SMTP_HOST", "").strip()
    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USER", "").strip()
    password = os.getenv("SMTP_PASSWORD", "").strip()
    mail_to = os.getenv("TECH_INTEL_TO", "").strip() or DEFAULT_TO
    mail_from = os.getenv("SMTP_FROM", "").strip() or user

    if not host or not user or not password:
        print("SMTP secrets are not configured; generated files only, skipped email.")
        return False

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = mail_from
    msg["To"] = mail_to
    msg.set_content(body)

    with smtplib.SMTP(host, port, timeout=30) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)
    print(f"Sent email to {mail_to}")
    return True


def mark_email_sent(day_dir: Path, sent: bool) -> None:
    state_path = day_dir / "cloud-state.json"
    state = {
        "email_sent": sent,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "recipient": os.getenv("TECH_INTEL_TO", "").strip() or DEFAULT_TO,
    }
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def run(args: argparse.Namespace) -> int:
    date = args.date or now_date()
    if args.existing_only:
        day_dir = TECH_INTEL_DIR / date
        email_path = day_dir / f"email-{date}.md"
        if not email_path.exists():
            print(f"No existing email file for {date}: {email_path}", file=sys.stderr)
            return 2
        subject, body = parse_email_file(email_path)
        if args.send_email:
            sent = send_email(subject, body)
            mark_email_sent(day_dir, sent)
        return 0

    all_sources = load_sources()
    if args.max_sources:
        all_sources = all_sources[: args.max_sources]
    http = session()
    items: list[Item] = []
    statuses: list[FetchStatus] = []

    for idx, source in enumerate(all_sources, 1):
        print(f"[{idx}/{len(all_sources)}] Fetching {source.get('id')} ({source.get('method')})")
        got, status = fetch_source(http, source)
        items.extend(got)
        statuses.append(status)
        time.sleep(args.delay)

    items = score_items(dedupe(items))
    report, email_file, _email_subject = generate_report(date, items, statuses)
    if args.dry_run:
        print(f"Dry run collected {len(items)} items from {len(statuses)} sources.")
        print(f"Subject preview: {parse_subject_from_email_text(email_file)}")
        return 0

    day_dir = save_outputs(date, report, email_file, items, statuses, overwrite=args.overwrite)

    sent = False
    if args.send_email:
        subject, body = parse_email_file(day_dir / f"email-{date}.md")
        sent = send_email(subject, body)
        mark_email_sent(day_dir, sent)

    failures = [s for s in statuses if s.status == "failed"]
    if len(items) < args.min_items:
        print(f"Only {len(items)} items collected; below min-items={args.min_items}.", file=sys.stderr)
        if args.strict:
            return 3
    if len(failures) > max(8, len(statuses) // 2):
        print(f"Many sources failed: {len(failures)}/{len(statuses)}.", file=sys.stderr)
        if args.strict:
            return 4
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate and optionally email the daily tech-intel brief.")
    parser.add_argument("--date", help="Report date in YYYY-MM-DD. Defaults to Asia/Shanghai today.")
    parser.add_argument("--send-email", action="store_true", help="Send email via SMTP secrets after generation.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate files even if the date already exists.")
    parser.add_argument("--existing-only", action="store_true", help="Use existing email file for the date and optionally send it.")
    parser.add_argument("--max-sources", type=int, default=0, help="Limit sources for quick tests. 0 means all sources.")
    parser.add_argument("--min-items", type=int, default=5, help="Fail if fewer items are collected.")
    parser.add_argument("--delay", type=float, default=0.2, help="Delay between source requests.")
    parser.add_argument("--strict", action="store_true", help="Return non-zero when quality thresholds are not met.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and render previews without writing files or sending email.")
    return parser


def parse_subject_from_email_text(text: str) -> str:
    subject_match = re.search(r"<!-- EMAIL_SUBJECT -->\s*(.*?)\s*<!-- EMAIL_BODY_START -->", text, re.S)
    return clean(subject_match.group(1), 180) if subject_match else ""


if __name__ == "__main__":
    raise SystemExit(run(build_parser().parse_args()))
