#!/usr/bin/env python
"""Extract UCloud auth cookies from browser and save as JSON.

Supported browsers: Chrome, Chromium, Edge, Brave (Chromium-based).

Usage:
  python tools/ucloud_cookie_helper.py              # auto-detect browser
  python tools/ucloud_cookie_helper.py --browser chrome
  python tools/ucloud_cookie_helper.py --manual     # paste token manually

The saved cookie file (~/.config/edge-ai/ucloud-cookies.json) is used by
ucloud_task_scraper.py to call the UCloud API.
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
import sqlite3
import sys
from pathlib import Path
from typing import Any

COOKIE_FILE = Path.home() / ".config" / "edge-ai" / "ucloud-cookies.json"

# Chromium cookie DB paths by OS
if sys.platform == "win32":
    CHROME_PATHS = {
        "chrome": Path.home() / "AppData/Local/Google/Chrome/User Data/Default/Cookies",
        "edge": Path.home() / "AppData/Local/Microsoft/Edge/User Data/Default/Cookies",
        "brave": Path.home() / "AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Cookies",
    }
elif sys.platform == "darwin":
    CHROME_PATHS = {
        "chrome": Path.home() / "Library/Application Support/Google/Chrome/Default/Cookies",
        "edge": Path.home() / "Library/Application Support/Microsoft Edge/Default/Cookies",
        "brave": Path.home() / "Library/Application Support/BraveSoftware/Brave-Browser/Default/Cookies",
    }
else:  # Linux
    CHROME_PATHS = {
        "chrome": Path.home() / ".config/google-chrome/Default/Cookies",
        "chromium": Path.home() / ".config/chromium/Default/Cookies",
        "edge": Path.home() / ".config/microsoft-edge/Default/Cookies",
        "brave": Path.home() / ".config/BraveSoftware/Brave-Browser/Default/Cookies",
    }

TARGET_DOMAIN = "ucloud.bupt.edu.cn"
NEEDED_COOKIES = ["token", "refresh_token", "identity"]


def read_chrome_cookies(browser: str, profile_dir: str | None = None) -> list[dict[str, Any]]:
    """Read cookies from a Chromium-based browser's SQLite DB."""
    if profile_dir:
        db_path = Path(profile_dir) / "Cookies"
    else:
        if browser not in CHROME_PATHS:
            print(f"Unknown browser '{browser}'. Known: {list(CHROME_PATHS)}", file=sys.stderr)
            sys.exit(1)
        db_path = CHROME_PATHS[browser]

    if not db_path.exists():
        print(f"Cookie DB not found at {db_path}", file=sys.stderr)
        sys.exit(1)

    # Copy the DB because Chrome locks it while running
    import shutil
    import tempfile

    tmp_db = Path(tempfile.mktemp(suffix=".sqlite"))
    shutil.copy2(db_path, tmp_db)

    try:
        conn = sqlite3.connect(str(tmp_db))
        conn.row_factory = sqlite3.Row
        cur = conn.execute(
            "SELECT host_key, name, value, encrypted_value FROM cookies WHERE host_key LIKE ?",
            (f"%{TARGET_DOMAIN}%",),
        )
        rows = [dict(r) for r in cur.fetchall()]
        conn.close()
    finally:
        tmp_db.unlink()

    return rows


def try_decrypt(encrypted_value: bytes) -> str | None:
    """Try to decrypt Chromium-encrypted cookie values.

    On Linux, Chrome uses either GNOME keyring or KWallet (or basic AES if no keyring).
    On macOS, it uses Keychain.
    On Windows, it uses DPAPI.

    We try the following strategies, in order:
    1. If no encryption (v10 cookies with plaintext) — return raw value
    2. Try pycryptodome AES-GCM with hardcoded key ("Peanuts" fallback from Chromium)
    3. Try to use system keyring via secretstorage
    """
    import base64

    if not encrypted_value:
        return None

    # v10 cookies may be unencrypted in some Chrome builds
    try:
        raw = encrypted_value.decode("utf-8")
        if raw and all(32 <= ord(c) < 127 or c in "-_." for c in raw[:50]):
            return raw
    except UnicodeDecodeError:
        pass

    # Chromium on Linux without keyring uses a fixed key ("Peanuts")
    # v10 format: "v10" prefix + 12-byte nonce + ciphertext + 16-byte tag
    if encrypted_value.startswith(b"v10"):
        try:
            from hashlib import pbkdf2_hmac

            # Chromium's fallback key when no system keyring
            key = pbkdf2_hmac("sha1", b"peanuts", b"saltysalt", 1, dklen=16)
            nonce = encrypted_value[3:15]
            ciphertext = encrypted_value[15:]

            from Crypto.Cipher import AES
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            plain = cipher.decrypt_and_verify(ciphertext[:-16], ciphertext[-16:])
            return plain.decode("utf-8")
        except Exception:
            pass

    # v10 with system keyring
    if encrypted_value.startswith(b"v10"):
        try:
            import secretstorage

            bus = secretstorage.dbus_init()
            collection = secretstorage.get_default_collection(bus)
            items = list(collection.search_items({"application": "chrome"}))
            if items:
                item = items[0]
                key = item.get_secret()
                nonce = encrypted_value[3:15]
                ciphertext = encrypted_value[15:]
                from Crypto.Cipher import AES
                cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
                plain = cipher.decrypt_and_verify(ciphertext[:-16], ciphertext[-16:])
                return plain.decode("utf-8")
        except Exception:
            pass

    return None


def find_cookies(rows: list[dict[str, Any]]) -> dict[str, str]:
    """Extract needed cookie values from DB rows."""
    found: dict[str, str] = {}

    for row in rows:
        name = row.get("name", row.get("name_", ""))
        if name not in NEEDED_COOKIES:
            continue

        # Try plain value first
        value = row.get("value", "")
        if value:
            found[name] = value
            continue

        # Try encrypted value
        enc = row.get("encrypted_value", b"")
        if enc:
            decrypted = try_decrypt(enc)
            if decrypted:
                found[name] = decrypted

    return found


def manual_input() -> dict[str, str]:
    """Prompt user to paste cookie values manually."""
    print("Paste each cookie value (from browser DevTools > Application > Cookies):\n")
    result = {}
    for name in NEEDED_COOKIES:
        val = getpass.getpass(f"  {name}: ").strip()
        if val:
            result[name] = val
    return result


def save(data: dict[str, str]) -> None:
    COOKIE_FILE.parent.mkdir(parents=True, exist_ok=True)
    COOKIE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    os.chmod(COOKIE_FILE, 0o600)
    print(f"Saved cookies to {COOKIE_FILE}")
    print(f"Found keys: {list(data.keys())}")
    missing = [n for n in NEEDED_COOKIES if n not in data]
    if missing:
        print(f"Warning: missing cookies: {missing}")
        print("You can re-run with --manual to paste them.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract UCloud auth cookies from browser for ucloud_task_scraper.py"
    )
    parser.add_argument(
        "--browser",
        choices=list(CHROME_PATHS),
        help="Browser to extract from (default: auto-detect first available)",
    )
    parser.add_argument(
        "--profile-dir",
        help="Chrome profile directory (overrides --browser)",
    )
    parser.add_argument(
        "--manual",
        action="store_true",
        help="Manually paste cookie values instead of extracting from browser",
    )
    args = parser.parse_args()

    if args.manual:
        data = manual_input()
    else:
        browser = args.browser
        if not browser:
            for name in CHROME_PATHS:
                if CHROME_PATHS[name].exists():
                    browser = name
                    print(f"Auto-detected browser: {browser}")
                    break
            if not browser:
                print("No Chromium browser cookie DB found.", file=sys.stderr)
                print("Use --manual to paste cookies, or --profile-dir to specify path.",
                      file=sys.stderr)
                return 1

        rows = read_chrome_cookies(browser, args.profile_dir)
        data = find_cookies(rows)

        if not data:
            print("Could not extract cookies from browser DB.", file=sys.stderr)
            print("The cookies may be encrypted with a system keyring.", file=sys.stderr)
            print("Try --manual to paste values from DevTools instead.", file=sys.stderr)
            return 1

    if not data:
        print("No cookies provided.", file=sys.stderr)
        return 1

    save(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
