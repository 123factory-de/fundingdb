---
title: "fix: close expired autumn 2026 calls"
---

## Request

Run the weekly funding opportunity audit, verify official Horizon Europe, EUREKA/Eurostars, and KIAT/K-PASS sources, and publish only evidence-backed status updates.

## Changes

- Marked the expired 2026 EUREKA Advanced Biotech call, Korean EUREKA Network Projects cycle, and Eurostars Call 11 as closed.
- Updated Korean reader-facing status text and verification dates.
- Added dated verification entries that link each closure to its official EUREKA or KIAT source.
- Did not add calls whose Korean funding conditions are still pending confirmation.

## Verification

- Ran the repository program validator for the changed pages.
- Ran the Horizon Portal status checker against the current official bulk dataset.
- Ran `git diff --check`.
- Ran the Hugo production build to a temporary destination.
- Ran the repository Gitleaks scan.
