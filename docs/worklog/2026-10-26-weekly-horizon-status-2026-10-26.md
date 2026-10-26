---
title: "fix: refresh Horizon portal status and dates"
date: 2026-10-26
branch: fix/weekly-horizon-status-2026-10-26
request-source: "scheduled maintenance, 2026-10-26"
---

## Request

Run the weekly funding-opportunity maintenance workflow: discover and verify official Horizon Europe, Eureka/Eurostars, and Korea-European bilateral opportunities; update confirmed records; and prepare a reviewable pull request when changes are required.

## Changes

- Synced 16 Horizon Europe program pages and their matching verification logs to the official Funding & Tenders Portal bulk dataset.
- Marked eight 2027 calls open, four 2026 calls closed, and corrected four 2027 deadline schedules, including the two-stage Health call's second-stage deadline.
- Updated reader-facing schedule text when a deadline or closed status changed. No new program was published: the reviewed Eureka/Eurostars and KIAT sources did not establish a new, currently addable Korea-European opportunity with confirmed Korean funding.

## Verification

- Ran `docs/skills/crosscheck-horizon/check_horizon.py` against the official Portal bulk dataset before the update; it reported 16 mismatches out of 76 pages.
- Reviewed the official Eureka France–South Korea and Eurostars Call 12 pages, KIAT notices, and the Commission Korea-association page; no new eligible Korea-European call was added.
- Ran the repository program validator, the Horizon cross-check after updates, `git diff --check`, `hugo --gc --minify --destination /tmp/fundingdb-build`, and `gitleaks dir --config .gitleaks.toml --no-banner`.
