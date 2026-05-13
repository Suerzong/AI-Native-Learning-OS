#!/usr/bin/env python3
"""Send an email reminder without storing credentials in the repository."""

from __future__ import annotations

import argparse
from email.message import EmailMessage
import os
from pathlib import Path
import smtplib
import ssl
import sys
import time

DEFAULT_SMTP_HOST = "smtp.qq.com"
DEFAULT_SMTP_PORT = 465
DEFAULT_TO = "Suerzong@outlook.com"
DEFAULT_ENV_FILE = Path("~/.config/edge-ai/email.env").expanduser()


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(2)


def env_or_arg(value: str | None, env_names: tuple[str, ...], default: str | None = None) -> str:
    result = value
    if not result:
        for env_name in env_names:
            result = os.environ.get(env_name)
            if result:
                break
    if not result:
        result = default
    if not result:
        fail(f"missing one of {', '.join(env_names)}; pass an option or set an environment variable")
    return result


def env_port(value: int | None, env_names: tuple[str, ...], default: int) -> int:
    if value:
        return value
    for env_name in env_names:
        raw = os.environ.get(env_name)
        if raw:
            try:
                return int(raw)
            except ValueError:
                fail(f"{env_name} must be an integer port, got {raw!r}")
    return default


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


def read_body(args: argparse.Namespace) -> str:
    if args.body_file:
        return Path(args.body_file).read_text(encoding="utf-8").strip()
    if args.body:
        return args.body.strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return "Time for a short review."


def build_message(args: argparse.Namespace, smtp_user: str) -> EmailMessage:
    sender = args.sender or os.environ.get("SMTP_FROM") or os.environ.get("EMAIL_FROM") or smtp_user
    recipient = args.to or os.environ.get("TECH_INTEL_TO") or os.environ.get("EMAIL_TO") or DEFAULT_TO
    body = read_body(args)

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = args.subject or f"Edge-AI review reminder {time.strftime('%Y-%m-%d')}"
    msg.set_content(body)
    return msg


def main() -> int:
    parser = argparse.ArgumentParser(description="Send an email reminder through SMTP.")
    parser.add_argument("--host", help="SMTP host; env SMTP_HOST, defaults to smtp.qq.com")
    parser.add_argument("--port", type=int, help="SMTP port; env SMTP_PORT, defaults to 465")
    parser.add_argument("--user", help="SMTP username; env SMTP_USER")
    parser.add_argument("--password", help="SMTP password/app password; env SMTP_PASSWORD")
    parser.add_argument("--from", dest="sender", help="Sender address; env SMTP_FROM, defaults to SMTP_USER")
    parser.add_argument("--to", help="Recipient address; env TECH_INTEL_TO, defaults to Suerzong@outlook.com")
    parser.add_argument("--subject")
    parser.add_argument("--body")
    parser.add_argument("--body-file")
    parser.add_argument("--ssl", action="store_true", default=True, help="Use implicit TLS instead of STARTTLS.")
    parser.add_argument("--no-ssl", action="store_false", dest="ssl", help="Use STARTTLS instead of implicit TLS.")
    parser.add_argument("--starttls", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--env-file", default=str(DEFAULT_ENV_FILE), help="Private env file, defaults to ~/.config/edge-ai/email.env")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    load_env_file(Path(args.env_file).expanduser())

    host = env_or_arg(args.host, ("SMTP_HOST", "EMAIL_SMTP_HOST"), DEFAULT_SMTP_HOST)
    port = env_port(args.port, ("SMTP_PORT", "EMAIL_SMTP_PORT"), DEFAULT_SMTP_PORT)
    user = env_or_arg(args.user, ("SMTP_USER", "EMAIL_SMTP_USER"))
    password = env_or_arg(args.password, ("SMTP_PASSWORD", "EMAIL_SMTP_PASSWORD"))
    msg = build_message(args, user)

    if args.dry_run:
        print(f"SMTP: {host}:{port}")
        print(f"Transport: {'SSL' if args.ssl else 'STARTTLS'}")
        print(f"From: {msg['From']}")
        print(f"To: {msg['To']}")
        print(f"Subject: {msg['Subject']}")
        print()
        print(msg.get_content())
        return 0

    if args.ssl:
        with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context(), timeout=20) as server:
            server.login(user, password)
            server.send_message(msg)
    else:
        with smtplib.SMTP(host, port, timeout=20) as server:
            server.ehlo()
            server.starttls(context=ssl.create_default_context())
            server.login(user, password)
            server.send_message(msg)

    print("sent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
