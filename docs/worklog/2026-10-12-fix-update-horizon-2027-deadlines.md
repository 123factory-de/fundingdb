---
title: "fix: update Horizon 2027 deadlines"
---

## Request

Run the scheduled weekly funding opportunity maintenance workflow. Review
Horizon Europe Pillar II, EUREKA/Eurostars, and KIAT/K-PASS bilateral sources
using official sources, and publish only evidence-backed corrections.

## Summary

Correct four Horizon Europe 2027 deadline records identified by the official
Funding & Tenders Portal bulk-data cross-check. No new opportunity was added:
current official Korean national funding confirmation was not established for
any new EUREKA or bilateral candidate.

## Key Changes

- Update HORIZON-HLTH-2027-01 to 2027-04-13.
- Update HORIZON-HLTH-2027-02-two-stage to 2027-04-13 and 2027-09-22.
- Update HORIZON-HLTH-2027-03 to 2027-09-22.
- Update HORIZON-MISS-2027-02 to 2027-09-21.
- Synchronize the four verification logs and their verification dates with the
  targeted Portal check.
- Do not change protected, generated, vendored, or unrelated files.

## Verification

- `python3 docs/skills/add-funding-program/scripts/validate_program.py` for
  all four changed pages: passed.
- `python3 docs/skills/crosscheck-horizon/check_horizon.py`: the four corrected
  calls match; nine pre-existing call identifiers remain absent from the current
  Portal bulk dataset and are recorded as unresolved coverage, so the command
  exits non-zero.
- `python3 docs/skills/crosscheck-horizon/check_eligibility.py`: completed;
  changed calls retain their established Korean-eligibility conclusions.
- `git diff --check`: passed.
- `hugo --gc --minify --destination /tmp/fundingdb-weekly-build`: passed.
- `gitleaks dir --config .gitleaks.toml --no-banner`: passed.

## Related Issues

None.

## Checklist

- [x] Follow repository documentation conventions.
- [x] Review focused source-backed changes.
- [x] Run the applicable validation and build checks.
- [x] Preserve protected, generated, vendored, and unrelated paths.
