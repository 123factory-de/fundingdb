---
title: "chore: close expired Eureka calls"
date: 2026-11-02
branch: chore/close-expired-eureka-calls
request-source: "scheduled funding maintenance, 2026-11-02"
---

## Request

Run the weekly funding-opportunity discovery and verification audit for Korean startup applicants, including Horizon Europe Pillar II, Eureka/Eurostars, and Korea-European bilateral KIAT/K-PASS calls; apply only evidence-backed updates and open a pull request when changes are required.

## Changes

- Marked the CELTIC-NEXT Autumn Call 2026, Transnational Eureka Lightweighting Call 2026, and EUROGIA 2026 Call as closed because their official deadlines have passed.
- Replaced stale Korean overview text that described those calls as open, while retaining their original dates and Korean funding terms.
- Recorded a dated status-refresh entry in each matching verification log.
- Did not add a new opportunity: the official sources checked did not establish a newly announced call with confirmed Korean funding conditions.

## Verification

- Rechecked the three operator call pages: CELTIC-NEXT (26 October 2026), Eureka Lightweighting (8 October 2026), and EUROGIA (29 October 2026).
- Ran `python3 docs/skills/crosscheck-horizon/check_horizon.py`: 76 pages checked, 0 problems.
- Ran `python3 docs/skills/crosscheck-horizon/check_eligibility.py` against current portal data; completed successfully.
- Rechecked current ITEA 2026, Eurostars national-funding information, and K-PASS notices P3095 and P3108; no additional verified update was required.