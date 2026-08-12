#!/usr/bin/env python3
"""Cross-check Horizon Europe program pages against the EU Funding & Tenders portal.

For every content/programs/horizon-*.md page, this script reads the page's status
and deadline from the front matter, finds the call in the portal's official bulk
dataset (grantsTenders.json), and reports whether they match.

What is checked: page `status` (open/soon/planned/closed) and `deadline` against
the portal topics' status and deadline dates for the page's callIdentifier.
What is NOT checked: amounts/budgets, body text, and non-Horizon programs
(Eureka clusters and bilateral calls have no machine-readable source).

Usage:
    python3 docs/skills/crosscheck-horizon/check_horizon.py [--dump PATH]

The portal dump (~130 MB) is downloaded to a temp file on first run; pass --dump
to reuse a previously downloaded copy. Exit code 0 = all pages match, 1 = at
least one mismatch or a call missing from the dump.
"""

import argparse
import glob
import json
import os
import re
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone, timedelta

DUMP_URL = "https://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json"
# Brussels offset is close enough for date extraction: portal deadlines are
# 17:00 Brussels, so ±2h around midnight never flips the date.
BRUSSELS = timezone(timedelta(hours=2))

STATUS_MAP = {"Open": "open", "Forthcoming": "planned", "Closed": "closed"}


def repo_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def read_pages(root: str):
    pages = []
    for path in sorted(glob.glob(os.path.join(root, "content/programs/horizon-*.md"))):
        src = open(path, encoding="utf-8").read()
        fm = re.match(r"^---\n(.*?)\n---", src, re.S)
        if not fm:
            continue
        front = fm.group(1)

        def field(key):
            m = re.search(rf'^{key}:\s*"?([^"\n]*)"?\s*$', front, re.M)
            return m.group(1).strip() if m else ""

        call = ""
        m = re.search(r"callIdentifier=([A-Za-z0-9-]+)", front)
        if m:
            call = m.group(1)
        pages.append({
            "slug": os.path.basename(path)[:-3],
            "status": field("status"),
            "deadline": field("deadline"),
            "call": call,
        })
    return pages


def load_dump(path: str):
    data = json.load(open(path, encoding="utf-8"))
    by_call = {}
    for obj in data["fundingData"]["GrantTenderObj"]:
        ci = obj.get("callIdentifier")
        if ci:
            by_call.setdefault(ci, []).append(obj)
    return by_call


def to_date(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, BRUSSELS).strftime("%Y-%m-%d")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dump", help="path to a downloaded grantsTenders.json (downloaded if omitted)")
    args = ap.parse_args()

    dump_path = args.dump
    if not dump_path:
        dump_path = os.path.join(tempfile.gettempdir(), "grantsTenders.json")
        if not os.path.exists(dump_path):
            print(f"downloading portal dump (~130 MB) to {dump_path} ...", file=sys.stderr)
            urllib.request.urlretrieve(DUMP_URL, dump_path)

    by_call = load_dump(dump_path)
    pages = read_pages(repo_root())
    if not pages:
        print("no horizon-*.md pages found — run from within the repo", file=sys.stderr)
        return 1

    failures = 0
    for p in pages:
        topics = by_call.get(p["call"])
        if not p["call"] or not topics:
            print(f"MISSING   {p['slug']}: callIdentifier {p['call'] or '(none)'} not in portal dump")
            failures += 1
            continue

        statuses = {t["status"]["abbreviation"] for t in topics}
        deadlines = sorted({to_date(ms) for t in topics for ms in t.get("deadlineDatesLong", [])})
        if "Open" in statuses:
            portal_status = "open"
        elif "Forthcoming" in statuses:
            portal_status = "planned"
        else:
            portal_status = "closed"

        ok_status = p["status"] == portal_status or (p["status"] == "soon" and portal_status == "open")
        ok_deadline = (not p["deadline"]) or p["deadline"] in deadlines
        if ok_status and ok_deadline:
            print(f"OK        {p['slug']}")
        else:
            print(f"MISMATCH  {p['slug']}: page({p['status']}, {p['deadline']}) "
                  f"vs portal({portal_status}, deadlines {deadlines})")
            failures += 1

    print(f"\n{len(pages)} pages checked, {failures} problem(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
