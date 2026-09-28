---
title: "feat: add autumn 2026 funding calls"
---

## Request

Research funding opportunities beyond the registered database and add verified current opportunities plus the required Horizon status refreshes.

## Changes

- Added the KIAT–CDTI KSSP 2026–2027 call, Eurostars Call 12, and two current Horizon Europe calls.
- Added matching verification logs for each new program.
- Updated seven existing Horizon pages and verification logs to match the current official Portal status and deadline data.

## Verification

- Ran the repository program validator.
- Ran the Horizon Portal status checker against the current official bulk dataset.
- Ran `git diff --check` and the Horizon Portal status checker against the current official bulk dataset.
- Hugo production build passed with Hugo extended v0.167.0.
- Gitleaks v8.30.1 scan passed with no leaks found.
