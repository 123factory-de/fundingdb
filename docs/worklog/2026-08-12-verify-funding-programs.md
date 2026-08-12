---
title: "fix(programs): verify funding details"
branch: "fix/verify-funding-programs"
date: "2026-08-12"
---

## Request

Verify the program information in `content/programs/` against the programs' official websites and correct inaccurate or unsupported details.

## Changes

- Rechecked 66 program pages against official European Commission work programmes and portal pages, Eureka call pages, cluster program sites, and national funding-body notices.
- Corrected submission deadlines and event dates for Celtic-Next Autumn 2026 and extended Horizon CL5 calls (CL5-2026-05, CL5-2026-07).
- Fixed the EU Funding & Tenders portal search URL for two-stage Horizon Health call (`HORIZON-HLTH-2027-02-two-stage`).
- Clarified that Korean entities participate in Horizon Europe Pillar II on nearly equal terms while topic-specific security and strategic-technology restrictions may still apply.
- Standardized the Korean funding-body name as Korea Institute for Advancement of Technology (KIAT) and updated all program verification dates.
- Updated bilateral funding status: added 2026 Korea-Germany 2+2 call opening notice and corrected bilateral evaluation mechanism for Korea-Spain.
- Clarified the Eureka open call 70% budget rule and confirmed Korea's participation in Xecs Call 6.
- Corrected internal links whose displayed call IDs did not match the generated page paths.

## Verification

- Built the site with `hugo --gc --minify` using Hugo `v0.153.3+extended`.
- Parsed and validated front matter for all 66 program pages.
- Checked all internal Markdown links against generated content routes.
- Scanned the repository with `gitleaks dir --config .gitleaks.toml --no-banner`; no leaks found.

## Checklist

- [x] Content matches the cited official sources as of 2026-08-12.
- [x] Internal links resolve to existing content routes.
- [x] The production build completes without errors.
- [x] Secret and personal-data scanning passes.
