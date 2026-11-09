---
title: "feat: add Globalstars Japan 2026"
date: 2026-11-09
branch: feat/add-globalstars-japan-2026
request-source: "scheduled weekly maintenance, 2026-11-09"
---

## Request

Run the weekly official-source audit of Horizon Europe Pillar II, EUREKA/Eurostars, and Korea-European bilateral funding opportunities for Korean startup applicants; add only verified opportunities and refresh confirmed status or deadline changes.

## Changes

- Added the EUREKA Globalstars Call with Japan 2026 program page and matching verification log.
- The KIAT notice confirms that Korean entities are eligible for national funding, the annual Korean funding ceiling is KRW 500 million per project for up to three years, and the domestic application deadline is 2027-01-21 16:00 KST.
- The EUREKA call page confirms the international call identity, the 2027-01-20 central deadline, Japan-mandatory consortium participation, and international project conditions.
- No Horizon Europe page changes were required: the official portal cross-check matched all tracked pages. No other candidate met the publication threshold in this run.

## Verification

- Read the repository safeguards and the local add-funding-program and crosscheck-horizon skills before changes.
- Retrieved and reviewed KIAT and EUREKA official notices for the new call.
- Ran `python3 docs/skills/crosscheck-horizon/check_horizon.py`: 76 pages checked, 0 problems.
- Ran `python3 docs/skills/add-funding-program/scripts/validate_program.py content/programs/eureka-globalstars-japan-2026.md`.
- Ran `git diff --check`.
- Ran `hugo --gc --minify --destination /tmp/fundingdb-build`.
- Ran `gitleaks dir --config .gitleaks.toml --no-banner`.
