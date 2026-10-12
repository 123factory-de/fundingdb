#!/usr/bin/env python3
"""Send fundingdb program pages to a Slack channel via an incoming webhook.

The webhook URL is read from the SLACK_WEBHOOK_URL environment variable and is
never stored in the repository (secret guardrail). One Slack message is posted
per program.

Usage:
    export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
    # send one or more programs by slug (filename without .md), in send order:
    python3 notify_slack.py eureka-lightweighting-call-2026
    # preview the payload without sending:
    python3 notify_slack.py --dry-run eureka-lightweighting-call-2026

Select programs automatically from the machine-readable feed
(https://fundingdb.123factory.de/programs/index.json) instead of naming slugs.
This is how another agent finds newly added/updated programs with no local state:
    # programs added on/after a date (nearest deadline first):
    python3 notify_slack.py --added-since 2026-09-01
    # programs changed on/after a date, open ones only, skipping expired calls:
    python3 notify_slack.py --updated-since 2026-10-01 --status open --skip-expired
    # point at the live feed explicitly (default is the local build, then the live URL):
    python3 notify_slack.py --added-since 2026-09-01 --feed https://fundingdb.123factory.de/programs/index.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


def _ssl_context() -> ssl.SSLContext:
    """Build a verifying SSL context, falling back to the certifi CA bundle.

    Some Python installs (notably python.org builds on macOS) ship without the
    system trust store wired in, which makes urllib raise CERTIFICATE_VERIFY_FAILED.
    Prefer certifi's bundle when available; never disable verification.
    """
    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()

ROOT = Path(__file__).resolve().parents[4]
PROGRAM_DIR = ROOT / "content" / "programs"
BASE_URL = "https://fundingdb.123factory.de"
LOCAL_FEED = ROOT / "public" / "programs" / "index.json"
LIVE_FEED = f"{BASE_URL}/programs/index.json"

STATUS_LABELS = {
    "open": "🟢 모집중",
    "planned": "🗓️ 예정",
    "closed": "🔴 마감",
}


def load_feed(source: str | None) -> list[dict]:
    """Load the program feed from an explicit source, else the local build, else live."""
    sources = [source] if source else [str(LOCAL_FEED), LIVE_FEED]
    last_err: Exception | None = None
    for src in sources:
        try:
            if re.match(r"^https?://", src):
                req = urllib.request.Request(src, headers={"User-Agent": "fundingdb-notify"})
                with urllib.request.urlopen(req, timeout=15, context=_ssl_context()) as resp:
                    raw = resp.read().decode("utf-8")
            else:
                raw = Path(src).read_text(encoding="utf-8")
            return json.loads(raw).get("programs", [])
        except (urllib.error.URLError, OSError, ValueError) as exc:
            last_err = exc
    raise RuntimeError(f"could not load feed ({sources}): {last_err}")


def select_from_feed(
    programs: list[dict],
    added_since: str | None,
    updated_since: str | None,
    statuses: set[str] | None,
    skip_expired: bool,
    today: str,
) -> list[str]:
    """Return slugs matching the filters, ordered by nearest deadline first."""
    chosen = []
    for p in programs:
        if added_since and p.get("date", "") < added_since:
            continue
        if updated_since and p.get("lastmod", "") < updated_since:
            continue
        if statuses and p.get("status", "") not in statuses:
            continue
        if skip_expired and p.get("deadline") and p["deadline"] < today:
            continue
        chosen.append(p)
    # nearest deadline first; programs without a deadline go last
    chosen.sort(key=lambda p: p.get("deadline") or "9999-99-99")
    return [p["slug"] for p in chosen]


def front_matter(text: str) -> str:
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError("missing YAML front matter")
    return parts[1]


def body(text: str) -> str:
    parts = text.split("---", 2)
    return parts[2] if len(parts) == 3 else ""


def section_bullets(md: str, heading: str) -> list[str]:
    """Return the bullet items under a `## <heading>` section, markdown-stripped."""
    items: list[str] = []
    capture = False
    for line in md.splitlines():
        if line.startswith("## "):
            if capture:
                break
            capture = line[3:].strip() == heading
            continue
        if capture:
            m = re.match(r"\s*[-*]\s+(.*)", line)
            if m:
                items.append(m.group(1).strip())
    return items


def strip_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # [label](url) -> label
    text = text.replace("**", "").replace("*", "")
    return text.strip()


def truncate(text: str, limit: int = 110) -> str:
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def scalar(fm: str, key: str) -> str | None:
    match = re.search(rf'^{re.escape(key)}:\s*["\']?([^"\'\n]+)', fm, re.M)
    return match.group(1).strip() if match else None


def links(fm: str) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    in_links = False
    name: str | None = None
    for line in fm.splitlines():
        if re.match(r"^links:\s*$", line):
            in_links = True
            continue
        if in_links:
            if re.match(r"^[a-z_]+:", line):  # next top-level key
                break
            n = re.search(r'-\s*name:\s*["\']?([^"\'\n]+)', line)
            if n:
                name = n.group(1).strip()
            u = re.search(r'url:\s*["\']?([^"\'\n]+)', line)
            if u and name:
                result.append((name, u.group(1).strip()))
                name = None
    return result


def build_message(slug: str) -> dict:
    path = PROGRAM_DIR / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    fm = front_matter(text)
    md = body(text)

    title = scalar(fm, "title") or slug
    subtitle = scalar(fm, "subtitle") or ""
    status = scalar(fm, "status") or ""
    deadline = scalar(fm, "deadline")
    amount = scalar(fm, "amount") or scalar(fm, "amount_short")
    target = scalar(fm, "target") or scalar(fm, "target_short")
    org_kr = scalar(fm, "org_kr")
    apply_via = scalar(fm, "apply_via")
    page_url = f"{BASE_URL}/programs/{slug}/"

    status_label = STATUS_LABELS.get(status, status)

    fields: list[dict] = []
    if status_label:
        fields.append({"type": "mrkdwn", "text": f"*상태*\n{status_label}"})
    if deadline:
        fields.append({"type": "mrkdwn", "text": f"*마감일*\n{deadline}"})
    if amount:
        fields.append({"type": "mrkdwn", "text": f"*지원 규모*\n{amount}"})
    if target:
        fields.append({"type": "mrkdwn", "text": f"*지원 대상*\n{target}"})
    if org_kr:
        fields.append({"type": "mrkdwn", "text": f"*국내 주관*\n{org_kr}"})
    if apply_via:
        fields.append({"type": "mrkdwn", "text": f"*신청 경로*\n{apply_via}"})

    blocks: list[dict] = [
        {"type": "header", "text": {"type": "plain_text", "text": title[:150], "emoji": True}},
    ]
    if subtitle:
        blocks.append(
            {"type": "context", "elements": [{"type": "mrkdwn", "text": subtitle}]}
        )
    # Slack allows at most 10 fields per section.
    if fields:
        blocks.append({"type": "section", "fields": fields[:10]})

    # 지원분야: summarize to the bold field labels on one line when present,
    # otherwise fall back to the first few short bullets.
    scope = section_bullets(md, "지원분야")
    if scope:
        labels = [re.match(r"\s*\*\*(.+?)\*\*", b) for b in scope]
        if all(labels):
            summary = " · ".join(m.group(1).strip() for m in labels)
        else:
            summary = "\n".join(f"• {truncate(strip_md(b), 90)}" for b in scope[:4])
        blocks.append(
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*지원분야*\n{summary}"}}
        )

    # 지원자격: short bullet summary (up to 4 items, each truncated).
    eligibility = section_bullets(md, "지원자격")
    if eligibility:
        summary = "\n".join(f"• {truncate(strip_md(b))}" for b in eligibility[:4])
        blocks.append(
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*지원자격*\n{summary}"}}
        )

    link_items = links(fm)
    if link_items:
        link_text = "  ·  ".join(f"<{url}|{name}>" for name, url in link_items[:5])
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": link_text}})

    blocks.append(
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "상세 페이지 열기", "emoji": True},
                    "url": page_url,
                }
            ],
        }
    )

    return {
        "text": f"{title} — 마감 {deadline or '미정'}",  # fallback / notification text
        "blocks": blocks,
    }


def post(webhook: str, payload: dict) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=15, context=_ssl_context()) as resp:
        body = resp.read().decode("utf-8", "replace")
        if resp.status != 200 or body.strip() != "ok":
            raise RuntimeError(f"Slack responded {resp.status}: {body}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Send program pages to Slack.")
    parser.add_argument(
        "slug", nargs="*",
        help="program filenames without .md, in send order (omit when using feed filters)",
    )
    parser.add_argument("--added-since", metavar="YYYY-MM-DD", help="select programs with date >= this")
    parser.add_argument("--updated-since", metavar="YYYY-MM-DD", help="select programs with lastmod >= this")
    parser.add_argument(
        "--status", help="comma-separated status filter for feed selection, e.g. open,planned",
    )
    parser.add_argument(
        "--skip-expired", action="store_true", help="drop programs whose deadline is before today",
    )
    parser.add_argument("--feed", help="feed path or URL (default: local build, then live site)")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the payload(s) instead of sending",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="seconds to wait between messages (default 1.0)",
    )
    args = parser.parse_args()

    use_feed = bool(args.added_since or args.updated_since or args.status or args.feed)
    if use_feed and args.slug:
        print("error: give either slugs or feed filters, not both", file=sys.stderr)
        return 1
    if not use_feed and not args.slug:
        parser.print_usage(sys.stderr)
        print("error: name at least one slug, or use a feed filter (e.g. --added-since)", file=sys.stderr)
        return 1

    if use_feed:
        from datetime import date as _date

        statuses = {s.strip() for s in args.status.split(",")} if args.status else None
        try:
            programs = load_feed(args.feed)
        except RuntimeError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        slugs = select_from_feed(
            programs, args.added_since, args.updated_since, statuses,
            args.skip_expired, _date.today().isoformat(),
        )
        if not slugs:
            print("no programs matched the feed filters; nothing to send")
            return 0
        print(f"feed selection: {len(slugs)} program(s)")
    else:
        slugs = args.slug

    args.slug = slugs
    missing = [s for s in args.slug if not (PROGRAM_DIR / f"{s}.md").is_file()]
    if missing:
        print(f"error: no such program(s): {', '.join(missing)}", file=sys.stderr)
        return 1

    if args.dry_run:
        for slug in args.slug:
            print(json.dumps(build_message(slug), ensure_ascii=False, indent=2))
        return 0

    webhook = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook:
        print(
            "error: SLACK_WEBHOOK_URL is not set. Export your Slack incoming "
            "webhook URL before running (do not hardcode it).",
            file=sys.stderr,
        )
        return 2

    total = len(args.slug)
    failed: list[str] = []
    for i, slug in enumerate(args.slug, 1):
        try:
            post(webhook, build_message(slug))
            print(f"[{i}/{total}] sent: {slug}")
        except (urllib.error.URLError, RuntimeError) as exc:
            print(f"[{i}/{total}] FAILED: {slug}: {exc}", file=sys.stderr)
            failed.append(slug)
        if i < total:
            time.sleep(args.delay)

    if failed:
        print(f"\ndone with {len(failed)} failure(s): {', '.join(failed)}", file=sys.stderr)
        return 3
    print(f"\ndone: {total} message(s) sent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
