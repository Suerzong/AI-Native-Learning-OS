#!/usr/bin/env python3
"""Send Outlook mail through Microsoft Graph device-code OAuth."""

from __future__ import annotations

import argparse
from email.utils import parseaddr
import json
import os
from pathlib import Path
import sys
import time

import requests

DEFAULT_AUTHORITY = "https://login.microsoftonline.com/consumers"
DEFAULT_GRAPH_ROOT = "https://graph.microsoft.com/v1.0"
DEFAULT_ENV_FILE = Path("~/.config/edge-ai/ms-graph.env").expanduser()
DEFAULT_TOKEN_CACHE = Path("~/.config/edge-ai/ms_graph_token.json").expanduser()
DEFAULT_TO = "Suerzong@outlook.com"
DEFAULT_SCOPES = "offline_access User.Read Mail.Send"


def fail(message: str, code: int = 2) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(code)


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def env(name: str, default: str | None = None) -> str:
    value = os.environ.get(name, default)
    if not value:
        fail(f"missing {name}; set it in {DEFAULT_ENV_FILE}")
    return value


def read_body(args: argparse.Namespace) -> str:
    if args.body_file:
        return Path(args.body_file).read_text(encoding="utf-8").strip()
    if args.body:
        return args.body.strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return "Time for a short review."


def token_url(authority: str) -> str:
    return f"{authority.rstrip('/')}/oauth2/v2.0/token"


def device_code_url(authority: str) -> str:
    return f"{authority.rstrip('/')}/oauth2/v2.0/devicecode"


def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    try:
        path.chmod(0o600)
    except OSError:
        pass


def load_token_cache(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def token_is_fresh(token: dict) -> bool:
    return bool(token.get("access_token")) and int(token.get("expires_at", 0)) > int(time.time()) + 300


def request_token(authority: str, payload: dict) -> dict:
    response = requests.post(token_url(authority), data=payload, timeout=30)
    if response.status_code >= 400:
        fail(f"token request failed: HTTP {response.status_code} {response.text}", 1)
    token = response.json()
    token["expires_at"] = int(time.time()) + int(token.get("expires_in", 3600))
    return token


def refresh_token(authority: str, client_id: str, scopes: str, token: dict, cache_path: Path) -> dict | None:
    refresh = token.get("refresh_token")
    if not refresh:
        return None
    payload = {
        "client_id": client_id,
        "grant_type": "refresh_token",
        "refresh_token": refresh,
        "scope": scopes,
    }
    try:
        new_token = request_token(authority, payload)
    except SystemExit:
        return None
    if "refresh_token" not in new_token:
        new_token["refresh_token"] = refresh
    save_json(cache_path, new_token)
    return new_token


def device_login(authority: str, client_id: str, scopes: str, cache_path: Path) -> dict:
    response = requests.post(
        device_code_url(authority),
        data={"client_id": client_id, "scope": scopes},
        timeout=30,
    )
    if response.status_code >= 400:
        fail(f"device code request failed: HTTP {response.status_code} {response.text}", 1)
    device = response.json()
    print(device.get("message") or f"Open {device['verification_uri']} and enter code {device['user_code']}")
    print("Waiting for Microsoft authorization...")

    interval = int(device.get("interval", 5))
    expires_at = time.time() + int(device.get("expires_in", 900))
    while time.time() < expires_at:
        time.sleep(interval)
        payload = {
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "client_id": client_id,
            "device_code": device["device_code"],
        }
        response = requests.post(token_url(authority), data=payload, timeout=30)
        result = response.json()
        if response.status_code == 200:
            result["expires_at"] = int(time.time()) + int(result.get("expires_in", 3600))
            save_json(cache_path, result)
            print("Microsoft Graph authorization saved.")
            return result
        error = result.get("error")
        if error == "authorization_pending":
            continue
        if error == "slow_down":
            interval += 5
            continue
        fail(f"device login failed: {result}", 1)
    fail("device login timed out", 1)


def get_access_token(args: argparse.Namespace) -> str:
    authority = os.environ.get("MS_GRAPH_AUTHORITY", DEFAULT_AUTHORITY)
    client_id = env("MS_GRAPH_CLIENT_ID")
    scopes = os.environ.get("MS_GRAPH_SCOPES", DEFAULT_SCOPES)
    cache_path = Path(os.environ.get("MS_GRAPH_TOKEN_CACHE", str(DEFAULT_TOKEN_CACHE))).expanduser()

    if args.login:
        token = device_login(authority, client_id, scopes, cache_path)
        return token["access_token"]

    token = load_token_cache(cache_path)
    if token and token_is_fresh(token):
        return token["access_token"]
    if token:
        refreshed = refresh_token(authority, client_id, scopes, token, cache_path)
        if refreshed and token_is_fresh(refreshed):
            return refreshed["access_token"]
    fail("Microsoft Graph is not authorized yet; run this script with --login first", 1)


def validate_recipients(addresses: str) -> list[dict]:
    recipients: list[dict] = []
    for raw in addresses.split(","):
        name, address = parseaddr(raw.strip())
        if not address or "@" not in address:
            fail(f"invalid recipient address: {raw!r}")
        recipients.append({"emailAddress": {"address": address}})
    return recipients


def send_mail(access_token: str, to: str, subject: str, body: str, save_to_sent: bool) -> None:
    payload = {
        "message": {
            "subject": subject,
            "body": {"contentType": "Text", "content": body},
            "toRecipients": validate_recipients(to),
        },
        "saveToSentItems": save_to_sent,
    }
    response = requests.post(
        f"{DEFAULT_GRAPH_ROOT}/me/sendMail",
        headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
        json=payload,
        timeout=30,
    )
    if response.status_code not in (202, 200):
        fail(f"Graph sendMail failed: HTTP {response.status_code} {response.text}", 1)
    print("sent")


def main() -> int:
    parser = argparse.ArgumentParser(description="Send Outlook mail through Microsoft Graph OAuth.")
    parser.add_argument("--env-file", default=str(DEFAULT_ENV_FILE), help="Private env file, defaults to ~/.config/edge-ai/ms-graph.env")
    parser.add_argument("--login", action="store_true", help="Run Microsoft device-code login and save token cache.")
    parser.add_argument("--to", default=None, help="Recipient list; defaults to TECH_INTEL_TO or Suerzong@outlook.com")
    parser.add_argument("--subject", default="Edge-AI automatic reminder")
    parser.add_argument("--body")
    parser.add_argument("--body-file")
    parser.add_argument("--no-save-to-sent", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    load_env_file(Path(args.env_file).expanduser())
    to = args.to or os.environ.get("TECH_INTEL_TO") or DEFAULT_TO
    body = read_body(args)

    if args.dry_run:
        print("Transport: Microsoft Graph / OAuth")
        print(f"To: {to}")
        print(f"Subject: {args.subject}")
        print()
        print(body)
        return 0

    access_token = get_access_token(args)
    if args.login and not body:
        return 0
    send_mail(access_token, to, args.subject, body, not args.no_save_to_sent)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
