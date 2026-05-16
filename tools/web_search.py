#!/usr/bin/env python
"""
Small web search adapter for local agents.

Supported backends:
- Brave Search API: set BRAVE_SEARCH_API_KEY
- Bing Web Search API: set BING_SEARCH_API_KEY
- Tavily Search API: set TAVILY_API_KEY
- SerpAPI Google Search: set SERPAPI_API_KEY
- DuckDuckGo Lite HTML fallback: no key, best-effort only
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from typing import Any


USER_AGENT = "Edge-AI-TechIntel/0.1 (+local web_search.py)"


def request_json(url: str, headers: dict[str, str] | None = None, data: bytes | None = None) -> Any:
    req_headers = {"User-Agent": USER_AGENT}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers, data=data)
    with urllib.request.urlopen(req, timeout=25) as resp:
        body = resp.read().decode("utf-8", errors="replace")
    return json.loads(body)


def request_text(url: str, headers: dict[str, str] | None = None, data: bytes | None = None) -> str:
    req_headers = {"User-Agent": USER_AGENT}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers, data=data)
    with urllib.request.urlopen(req, timeout=25) as resp:
        return resp.read().decode("utf-8", errors="replace")


def normalize(items: list[dict[str, Any]], backend: str) -> dict[str, Any]:
    results = []
    for item in items:
        title = (item.get("title") or "").strip()
        url = (item.get("url") or "").strip()
        snippet = (item.get("snippet") or "").strip()
        if title and url:
            results.append(
                {
                    "title": title,
                    "url": url,
                    "snippet": snippet,
                    "source": backend,
                }
            )
    return {"backend": backend, "results": results}


def brave_search(query: str, limit: int) -> dict[str, Any]:
    key = os.environ.get("BRAVE_SEARCH_API_KEY")
    if not key:
        raise RuntimeError("BRAVE_SEARCH_API_KEY 环境变量未设置")
    params = urllib.parse.urlencode({"q": query, "count": min(limit, 20)})
    data = request_json(
        f"https://api.search.brave.com/res/v1/web/search?{params}",
        headers={"Accept": "application/json", "X-Subscription-Token": key},
    )
    items = []
    for result in data.get("web", {}).get("results", []):
        items.append(
            {
                "title": result.get("title"),
                "url": result.get("url"),
                "snippet": result.get("description"),
            }
        )
    return normalize(items, "brave")


def bing_search(query: str, limit: int) -> dict[str, Any]:
    key = os.environ.get("BING_SEARCH_API_KEY")
    if not key:
        raise RuntimeError("BING_SEARCH_API_KEY 环境变量未设置")
    params = urllib.parse.urlencode({"q": query, "count": min(limit, 50), "responseFilter": "Webpages"})
    data = request_json(
        f"https://api.bing.microsoft.com/v7.0/search?{params}",
        headers={"Ocp-Apim-Subscription-Key": key},
    )
    items = []
    for result in data.get("webPages", {}).get("value", []):
        items.append(
            {
                "title": result.get("name"),
                "url": result.get("url"),
                "snippet": result.get("snippet"),
            }
        )
    return normalize(items, "bing")


def tavily_search(query: str, limit: int) -> dict[str, Any]:
    key = os.environ.get("TAVILY_API_KEY")
    if not key:
        raise RuntimeError("TAVILY_API_KEY 环境变量未设置")
    payload = json.dumps(
        {
            "api_key": key,
            "query": query,
            "max_results": min(limit, 20),
            "search_depth": "basic",
        }
    ).encode("utf-8")
    data = request_json(
        "https://api.tavily.com/search",
        headers={"Content-Type": "application/json"},
        data=payload,
    )
    items = []
    for result in data.get("results", []):
        items.append(
            {
                "title": result.get("title"),
                "url": result.get("url"),
                "snippet": result.get("content"),
            }
        )
    return normalize(items, "tavily")


def serpapi_search(query: str, limit: int) -> dict[str, Any]:
    key = os.environ.get("SERPAPI_API_KEY")
    if not key:
        raise RuntimeError("SERPAPI_API_KEY 环境变量未设置")
    params = urllib.parse.urlencode({"engine": "google", "q": query, "num": min(limit, 10), "api_key": key})
    data = request_json(f"https://serpapi.com/search.json?{params}")
    items = []
    for result in data.get("organic_results", []):
        items.append(
            {
                "title": result.get("title"),
                "url": result.get("link"),
                "snippet": result.get("snippet"),
            }
        )
    return normalize(items, "serpapi")


def duckduckgo_lite_search(query: str, limit: int) -> dict[str, Any]:
    params = urllib.parse.urlencode({"q": query})
    text = request_text(
        "https://lite.duckduckgo.com/lite/",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=params.encode("utf-8"),
    )
    items = []
    pattern = re.compile(r'<a rel="nofollow" href="([^"]+)"[^>]*>(.*?)</a>', re.I | re.S)
    for match in pattern.finditer(text):
        url = html.unescape(re.sub(r"^//duckduckgo.com/l/\?uddg=", "", match.group(1)))
        if "uddg=" in url:
            parsed = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
            url = parsed.get("uddg", [url])[0]
        title = re.sub(r"<.*?>", "", match.group(2))
        title = html.unescape(title).strip()
        if title and url.startswith(("http://", "https://")):
            items.append({"title": title, "url": url, "snippet": ""})
        if len(items) >= limit:
            break
    return normalize(items, "duckduckgo_lite")


def choose_backend(explicit: str | None) -> str:
    if explicit:
        return explicit
    if os.getenv("BRAVE_SEARCH_API_KEY"):
        return "brave"
    if os.getenv("BING_SEARCH_API_KEY"):
        return "bing"
    if os.getenv("TAVILY_API_KEY"):
        return "tavily"
    if os.getenv("SERPAPI_API_KEY"):
        return "serpapi"
    return "duckduckgo_lite"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Search the web and return normalized JSON results.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--backend", choices=["brave", "bing", "tavily", "serpapi", "duckduckgo_lite"])
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    backend = choose_backend(args.backend)
    try:
        if backend == "brave":
            output = brave_search(args.query, args.limit)
        elif backend == "bing":
            output = bing_search(args.query, args.limit)
        elif backend == "tavily":
            output = tavily_search(args.query, args.limit)
        elif backend == "serpapi":
            output = serpapi_search(args.query, args.limit)
        else:
            output = duckduckgo_lite_search(args.query, args.limit)
    except Exception as exc:
        output = {"backend": backend, "error": str(exc), "results": []}

    indent = 2 if args.pretty else None
    print(json.dumps(output, ensure_ascii=False, indent=indent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
