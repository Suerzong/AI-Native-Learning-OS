#!/usr/bin/env python3
"""Send a WeChat Official Account template message.

This tool is designed for private reminders from the Edge-AI workspace.
It reads credentials from environment variables by default:

  WECHAT_MP_APPID
  WECHAT_MP_SECRET
  WECHAT_MP_OPENID
  WECHAT_MP_TEMPLATE_ID

No credential is stored in this repository.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API_BASE = os.environ.get("WECHAT_MP_API_BASE", "https://api.weixin.qq.com").rstrip("/")
CACHE_PATH = Path(os.environ.get("WECHAT_MP_TOKEN_CACHE", "~/.cache/edge-ai/wechat_mp_token.json")).expanduser()


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(2)


def env_or_arg(arg_value: str | None, env_name: str) -> str:
    value = arg_value or os.environ.get(env_name)
    if not value:
        fail(f"missing {env_name}; pass an option or set the environment variable")
    return value


def request_json(url: str, payload: dict | None = None) -> dict:
    data = None
    headers = {"User-Agent": "edge-ai-wechat-template-push/1.0"}
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json; charset=utf-8"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if payload is not None else "GET")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        fail(f"HTTP {exc.code}: {raw}")
    except urllib.error.URLError as exc:
        fail(f"request failed: {exc}")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        fail(f"non-JSON response: {raw[:300]}")


def load_cached_token() -> str | None:
    try:
        cached = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
    if cached.get("expires_at", 0) > time.time() + 300:
        return cached.get("access_token")
    return None


def save_cached_token(token: str, expires_in: int) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {"access_token": token, "expires_at": int(time.time()) + int(expires_in)}
    CACHE_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    try:
        CACHE_PATH.chmod(0o600)
    except OSError:
        pass


def get_access_token(appid: str, secret: str, force_refresh: bool) -> str:
    if not force_refresh:
        token = load_cached_token()
        if token:
            return token
    query = urllib.parse.urlencode({"grant_type": "client_credential", "appid": appid, "secret": secret})
    result = request_json(f"{API_BASE}/cgi-bin/token?{query}")
    if result.get("errcode"):
        fail(f"token API error: {result}")
    token = result.get("access_token")
    if not token:
        fail(f"token API returned no access_token: {result}")
    save_cached_token(token, int(result.get("expires_in", 7200)))
    return token


def parse_fields(items: list[str]) -> dict[str, dict[str, str]]:
    data: dict[str, dict[str, str]] = {}
    for item in items:
        if "=" not in item:
            fail(f"invalid --field {item!r}; expected name=value")
        key, value = item.split("=", 1)
        key = key.strip()
        if not key:
            fail("field name cannot be empty")
        data[key] = {"value": value}
    return data


def read_content(args: argparse.Namespace) -> str:
    if args.content_file:
        return Path(args.content_file).read_text(encoding="utf-8").strip()
    if args.content:
        return args.content.strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return "Time for a short review."


def build_payload(args: argparse.Namespace, openid: str, template_id: str) -> dict:
    content = read_content(args)
    fields = parse_fields(args.field)
    if not fields:
        fields = {
            "title": {"value": args.title},
            "time": {"value": args.time or time.strftime("%Y-%m-%d %H:%M")},
            "content": {"value": content},
            "remark": {"value": args.remark},
        }
    payload = {"touser": openid, "template_id": template_id, "data": fields}
    template_url = args.template_url or os.environ.get("WECHAT_MP_TEMPLATE_URL")
    if template_url:
        payload["url"] = template_url
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a WeChat Official Account template message.")
    parser.add_argument("--appid")
    parser.add_argument("--secret")
    parser.add_argument("--openid")
    parser.add_argument("--template-id")
    parser.add_argument("--template-url")
    parser.add_argument("--title", default="Evening review")
    parser.add_argument("--time")
    parser.add_argument("--content")
    parser.add_argument("--content-file")
    parser.add_argument("--remark", default="Reply in WeChat when you are ready to review.")
    parser.add_argument("--field", action="append", default=[], help="Template field as name=value; repeatable.")
    parser.add_argument("--force-token-refresh", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    appid = env_or_arg(args.appid, "WECHAT_MP_APPID")
    secret = env_or_arg(args.secret, "WECHAT_MP_SECRET")
    openid = env_or_arg(args.openid, "WECHAT_MP_OPENID")
    template_id = env_or_arg(args.template_id, "WECHAT_MP_TEMPLATE_ID")
    payload = build_payload(args, openid, template_id)

    if args.dry_run:
        redacted = dict(payload)
        redacted["touser"] = openid[:6] + "..." if len(openid) > 6 else "***"
        print(json.dumps(redacted, ensure_ascii=False, indent=2))
        return 0

    token = get_access_token(appid, secret, args.force_token_refresh)
    query = urllib.parse.urlencode({"access_token": token})
    result = request_json(f"{API_BASE}/cgi-bin/message/template/send?{query}", payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("errcode") not in (0, None):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())