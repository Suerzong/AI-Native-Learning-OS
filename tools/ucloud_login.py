#!/usr/bin/env python
"""Auto-login to BUPT UCloud via CAS and extract Blade-Auth cookies.

Usage:
  python tools/ucloud_login.py
  python tools/ucloud_login.py --username 2025210827

Credentials are read from environment variables or prompted interactively.
Never stored on disk.

Environment variables:
  BUPT_USERNAME   BUPT student ID
  BUPT_PASSWORD   BUPT CAS password
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import requests

AUTH_BASE = "https://auth.bupt.edu.cn"
UCLASS_URL = "https://ucloud.bupt.edu.cn/uclass/"
COOKIE_FILE = Path.home() / ".config" / "edge-ai" / "ucloud-cookies.json"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)


def build_session() -> requests.Session:
    s = requests.Session()
    s.headers["User-Agent"] = USER_AGENT
    return s


def get_login_page(session: requests.Session) -> str:
    """GET the CAS login page, return HTML body."""
    resp = session.get(
        f"{AUTH_BASE}/authserver/login",
        params={"service": UCLASS_URL},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.text


def extract_execution(html: str) -> str:
    """Extract the 'execution' hidden input value from CAS login form."""
    match = re.search(r'name="execution"\s+value="([^"]+)"', html)
    if not match:
        raise ValueError("Cannot find execution parameter in CAS login page")
    return match.group(1)


def has_captcha(html: str) -> bool:
    """Check if the page is showing captcha (after failed login)."""
    # Captcha div is visible when id="captchaParent" lacks display:none
    return "captchaDiv" in html and 'style="display: none;"' not in html.split("captchaParent")[1][:200] if "captchaParent" in html else False


def get_captcha_image(session: requests.Session) -> bytes:
    """Download the captcha image from CAS."""
    # CAS captcha URL pattern
    resp = session.get(
        f"{AUTH_BASE}/authserver/captcha",
        params={"ts": str(int(os.times().elapsed * 1000))},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.content


def do_login(
    session: requests.Session,
    username: str,
    password: str,
    execution: str,
    captcha: str | None = None,
) -> requests.Response:
    """POST login form to CAS. Returns the response (expecting 302 on success)."""
    data: dict[str, str] = {
        "username": username,
        "password": password,
        "type": "username_password",
        "execution": execution,
        "_eventId": "submit",
    }
    if captcha:
        data["captcha"] = captcha

    return session.post(
        f"{AUTH_BASE}/authserver/login",
        params={"service": UCLASS_URL},
        data=data,
        allow_redirects=False,
        timeout=30,
    )


def extract_error(html: str) -> str | None:
    """Extract error message from CAS login page."""
    match = re.search(r'<div[^>]*id="errorDiv"[^>]*>\s*<p[^>]*>(.*?)</p>', html, re.S)
    if match:
        return match.group(1).strip()
    match = re.search(r'<span[^>]*id="errorMsg"[^>]*>(.*?)</span>', html, re.S)
    if match:
        return match.group(1).strip()
    return None


def follow_to_ucloud(session: requests.Session, cas_response: requests.Response) -> dict[str, str]:
    """Follow CAS redirect chain to UCloud and extract Blade-Auth cookies."""
    # CAS redirects to UCloud with a ticket parameter
    redirect_url = cas_response.headers.get("Location", "")
    if not redirect_url:
        raise RuntimeError(f"No redirect after login. Status: {cas_response.status_code}")

    # Follow the redirect (UCloud will set cookies)
    resp = session.get(redirect_url, allow_redirects=True, timeout=30)
    resp.raise_for_status()

    # Extract cookies
    cookies: dict[str, str] = {}
    for cookie in session.cookies:
        domain = cookie.domain or ""
        if "ucloud" in domain or "bupt" in domain:
            if cookie.name in ("token", "refresh_token", "identity"):
                cookies[cookie.name] = cookie.value

    return cookies


def save_cookies(cookies: dict[str, str]) -> None:
    COOKIE_FILE.parent.mkdir(parents=True, exist_ok=True)
    COOKIE_FILE.write_text(json.dumps(cookies, ensure_ascii=False, indent=2))
    os.chmod(COOKIE_FILE, 0o600)
    print(f"Saved to {COOKIE_FILE}")


def run_login(username: str, password: str) -> int:
    session = build_session()

    # Step 1: Get login page + execution
    print("Fetching CAS login page...")
    html = get_login_page(session)
    execution = extract_execution(html)
    print(f"  Got execution token")

    # Step 2: Attempt login
    print("Logging in...")
    resp = do_login(session, username, password, execution)

    # Step 3: Check result
    if resp.status_code in (302, 301, 303, 307, 308):
        print("  Login successful, following redirect...")
        cookies = follow_to_ucloud(session, resp)
        if not cookies:
            print("ERROR: No Blade-Auth cookies found after redirect.", file=sys.stderr)
            return 1
        save_cookies(cookies)
        print(f"  Got cookies: {list(cookies.keys())}")
        return 0

    # Login failed
    print(f"  Login failed (HTTP {resp.status_code})")

    # Check for error message
    error = extract_error(resp.text)
    if error:
        print(f"  Error: {error}")

    # Check for captcha
    if has_captcha(resp.text):
        print("  Captcha required! Downloading captcha image...")
        img_data = get_captcha_image(session)
        img_path = Path("/tmp/ucloud_captcha.png")
        img_path.write_bytes(img_data)
        print(f"  Captcha saved to {img_path}")
        print(f"  Please view the image and re-run with --captcha <code>")
        # Store the session cookies for retry context
        _save_session_state(session, execution)
        return 2

    return 1


def run_retry_with_captcha(username: str, password: str, captcha_code: str) -> int:
    """Retry login with captcha code using saved session state."""
    session = build_session()
    state = _load_session_state()
    if state:
        for name, value in state.get("cookies", {}).items():
            session.cookies.set(name, value)
        execution = state.get("execution", "")
    else:
        print("No saved session state. Starting fresh...")
        html = get_login_page(session)
        execution = extract_execution(html)

    print("Retrying with captcha...")
    resp = do_login(session, username, password, execution, captcha=captcha_code)

    if resp.status_code in (302, 301, 303, 307, 308):
        print("  Login successful!")
        cookies = follow_to_ucloud(session, resp)
        if not cookies:
            print("ERROR: No Blade-Auth cookies found.", file=sys.stderr)
            return 1
        save_cookies(cookies)
        print(f"  Got cookies: {list(cookies.keys())}")
        return 0

    error = extract_error(resp.text)
    if error:
        print(f"  Error: {error}")
    print(f"  Login still failed (HTTP {resp.status_code})", file=sys.stderr)
    return 1


def _save_session_state(session: requests.Session, execution: str) -> None:
    state_path = Path("/tmp/ucloud_session.json")
    state = {
        "cookies": {c.name: c.value for c in session.cookies},
        "execution": execution,
    }
    state_path.write_text(json.dumps(state))


def _load_session_state() -> dict[str, Any] | None:
    state_path = Path("/tmp/ucloud_session.json")
    if state_path.exists():
        return json.loads(state_path.read_text())
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Auto-login to BUPT UCloud via CAS for Blade-Auth cookies."
    )
    parser.add_argument("--username", help="BUPT student ID (env: BUPT_USERNAME)")
    parser.add_argument("--password", help="BUPT CAS password (env: BUPT_PASSWORD)")
    parser.add_argument("--captcha", help="Captcha code for retry after failed login")
    args = parser.parse_args()

    username = args.username or os.getenv("BUPT_USERNAME")
    password = args.password or os.getenv("BUPT_PASSWORD")

    if not username:
        username = input("BUPT username (student ID): ").strip()
    if not password:
        password = getpass.getpass("BUPT password: ").strip()

    if not username or not password:
        print("Username and password are required.", file=sys.stderr)
        return 1

    if args.captcha:
        return run_retry_with_captcha(username, password, args.captcha)

    return run_login(username, password)


if __name__ == "__main__":
    raise SystemExit(main())
