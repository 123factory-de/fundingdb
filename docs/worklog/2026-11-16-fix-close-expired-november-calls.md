---
title: "fix: close expired November calls"
date: 2026-11-16
branch: fix/close-expired-november-calls
request-source: "scheduled maintenance, 2026-11-16"
---

## Request

Run the weekly funding opportunity discovery, official-source verification, Horizon Portal cross-check, and PR workflow for Korean startup applicants.

## Changes

- Marked ITEA Call 2026 closed to new applicants after the Project Outline deadline. The page now distinguishes the later Full Project Proposal stage as invitation-only.
- Marked the 2026 Korea-Germany 2+2 call closed after its joint application deadline and corrected the overview accordingly.
- Added targeted verification-log entries for both status updates.
- Did not add newly discovered Eureka or Horizon candidates: Call 12 Korean national funding remains unconfirmed, while the Horizon candidate sweep contained calls outside Korea's Pillar II association scope or calls with unconfirmed Korean funding eligibility.

## Verification

- Reviewed the official ITEA current-call schedule, KIAT/K-PASS and BMFTR notices, Eureka programme listing, and European Commission Korea association guidance.
- Ran `python3 docs/skills/crosscheck-horizon/check_horizon.py`: 76 pages checked, 0 problems.
- Ran `python3 docs/skills/crosscheck-horizon/check_eligibility.py --dump /tmp/fundingdb-grantsTenders.json` successfully to review current topic restrictions.
- Ran `python3 docs/skills/add-funding-program/scripts/validate_program.py` for each changed page: both passed.
- Ran `git diff --check`: passed.
- Ran `hugo --gc --minify --destination /tmp/fundingdb-build`: passed (one pre-existing Hugo `languageCode` deprecation warning).
- Ran `gitleaks dir --config .gitleaks.toml --no-banner`: passed; no leaks found.
