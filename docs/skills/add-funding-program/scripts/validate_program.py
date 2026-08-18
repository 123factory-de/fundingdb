#!/usr/bin/env python3
"""Validate fundingdb program pages and their verification logs."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[4]
PROGRAM_DIR = ROOT / "content" / "programs"
VERIFICATION_DIR = ROOT / "docs" / "verifications"
TOPIC_HEADER = "| 토픽 ID | 주제 | Action Type | EU 지원율 | 예산(€M) |"
TRANSLATION_HEADER = "| Topic ID | Official portal title | Korean translation |"
ACTION_TYPES = {"RIA", "IA", "CSA", "PCP", "PPI", "COFUND"}
REQUIRED_KEYS = {
    "title",
    "subtitle",
    "weight",
    "tags",
    "status",
    "amount",
    "amount_short",
    "target",
    "target_short",
    "duration",
    "apply_via",
    "links",
    "verified",
}


def front_matter(text: str) -> str:
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError("missing YAML front matter")
    return parts[1]


def scalar(fm: str, key: str) -> str | None:
    match = re.search(rf'^{re.escape(key)}:\s*["\']?([^"\'\n]+)', fm, re.M)
    return match.group(1).strip() if match else None


def table_rows(lines: list[str], header: str) -> list[list[str]]:
    try:
        index = lines.index(header)
    except ValueError:
        return []
    rows: list[list[str]] = []
    for line in lines[index + 2 :]:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def validate_program(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    slug = path.stem

    try:
        fm = front_matter(text)
    except ValueError as exc:
        return [f"{path.relative_to(ROOT)}: {exc}"]

    missing = sorted(key for key in REQUIRED_KEYS if not re.search(rf"^{key}:", fm, re.M))
    if missing:
        errors.append(f"missing front-matter keys: {', '.join(missing)}")
    if not re.search(r"^deadline(?:_note)?:", fm, re.M):
        errors.append("missing deadline or deadline_note")

    verification = VERIFICATION_DIR / f"{slug}.md"
    if not verification.is_file():
        errors.append(f"missing verification log: {verification.relative_to(ROOT)}")
        verification_text = ""
    else:
        verification_text = verification.read_text(encoding="utf-8")
        program = scalar(front_matter(verification_text), "program")
        if program != slug:
            errors.append(f'verification program is "{program}", expected "{slug}"')

    for target in re.findall(r"\]\(/programs/([^/]+)/\)", text):
        if not (PROGRAM_DIR / f"{target}.md").is_file():
            errors.append(f"unresolved internal program link: /programs/{target}/")

    subtitle = scalar(fm, "subtitle") or ""
    identifier_match = re.match(r"(HORIZON-[^ ·]+)", subtitle, re.I)
    if not identifier_match:
        return [f"{path.relative_to(ROOT)}: {error}" for error in errors]

    identifier = identifier_match.group(1)
    expected_slug = identifier.lower()
    if slug != expected_slug:
        errors.append(f'filename does not match official identifier: expected "{expected_slug}.md"')

    portal_urls = re.findall(r'url:\s*"([^"]*callIdentifier=[^"]+)"', fm)
    if len(portal_urls) != 1:
        errors.append(f"expected one Portal callIdentifier URL, found {len(portal_urls)}")
    else:
        call_id = parse_qs(urlparse(portal_urls[0]).query).get("callIdentifier", [""])[0]
        if call_id.lower() != identifier.lower():
            errors.append(f'Portal callIdentifier "{call_id}" does not match "{identifier}"')

    if lines.count("## 토픽") != 1:
        errors.append(f'expected one "## 토픽" heading, found {lines.count("## 토픽")}')
    other_topic_headings = [line for line in lines if line.startswith("## ") and "토픽" in line and line != "## 토픽"]
    if other_topic_headings:
        errors.append(f"overlapping topic headings: {', '.join(other_topic_headings)}")
    if lines.count(TOPIC_HEADER) != 1:
        errors.append(f"expected one canonical topic table, found {lines.count(TOPIC_HEADER)}")

    rows = table_rows(lines, TOPIC_HEADER)
    topic_ids: list[str] = []
    for number, row in enumerate(rows, 1):
        if len(row) != 5:
            errors.append(f"topic row {number} has {len(row)} columns, expected 5")
            continue
        topic_id, title, action_type, rate, budget = row
        topic_ids.append(topic_id)
        if not all((topic_id, title, rate, budget)):
            errors.append(f"topic row {number} contains an empty required cell")
        if action_type not in ACTION_TYPES:
            errors.append(f'topic {topic_id} has unsupported Action Type "{action_type}"')
        try:
            float(budget)
        except ValueError:
            errors.append(f'topic {topic_id} has non-numeric budget "{budget}"')
    if not rows:
        errors.append("topic table has no rows")
    if len(topic_ids) != len(set(topic_ids)):
        errors.append("topic table contains duplicate topic IDs")

    if rows:
        table_end = lines.index(TOPIC_HEADER) + 2 + len(rows)
        following = lines[table_end:]
        while following and not following[0].strip():
            following = following[1:]
        source_line = following[0] if following else ""
        if "Funding & Tenders Portal" not in source_line:
            errors.append("topic table is not immediately followed by a Portal source link")
        has_pdf = bool(re.search(r'url:\s*"[^"]*/wp-[^"]+\.pdf"', fm))
        if has_pdf and "Work Programme PDF" not in source_line:
            errors.append("topic table is not immediately followed by its Work Programme PDF link")

    if verification_text:
        verification_lines = verification_text.splitlines()
        translation_rows = table_rows(verification_lines, TRANSLATION_HEADER)
        translated_ids = [row[0] for row in translation_rows if len(row) == 3]
        if not translation_rows:
            errors.append("verification log has no topic-title translation table")
        elif translated_ids != topic_ids:
            errors.append("verification translation topic IDs do not match the program topic table")
        for number, row in enumerate(translation_rows, 1):
            if len(row) != 3 or not all(row):
                errors.append(f"verification translation row {number} is incomplete")

    return [f"{path.relative_to(ROOT)}: {error}" for error in errors]


def main() -> int:
    if len(sys.argv) > 1:
        paths = [Path(arg).resolve() for arg in sys.argv[1:]]
    else:
        paths = sorted(PROGRAM_DIR.glob("*.md"))
    paths = [path for path in paths if path.name != "_index.md"]

    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            errors.append(f"{path}: file not found")
            continue
        errors.extend(validate_program(path))

    if errors:
        print(f"FAIL: {len(errors)} issue(s) across {len(paths)} program page(s)")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"OK: {len(paths)} program page(s) passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
