---
title: "feat(programs): migrate regions to tags and refine call IDs"
branch: "feat/update-programs"
date: "2026-08-12"
---

## Request
1. Replace the legacy `regions` taxonomy with a flexible `tags` taxonomy (`horizon`, `eureka`, `bilateral`) across all program entries, templates, filter chips, and client-side scripts.
2. Normalize two-stage Horizon Europe call filenames to standard continuous numbers instead of `-two-stage` suffixes (e.g. `horizon-cl6-2026-05`, `horizon-cl6-2026-06`, etc.).

## Changes
- **content/programs/**:
  - Migrated `regions: [...]` front matter to `tags: [...]` (`horizon`, `eureka`, `bilateral`) in all 70+ markdown files.
  - Renamed two-stage call files:
    - `horizon-cl4-2026-02-two-stage.md` → `horizon-cl4-2026-02.md`
    - `horizon-cl4-2027-02-two-stage.md` → `horizon-cl4-2027-02.md`
    - `horizon-cl5-2026-04-two-stage.md` → `horizon-cl5-2026-04.md`
    - `horizon-cl5-2026-06-two-stage.md` → `horizon-cl5-2026-06.md`
    - `horizon-cl5-2026-08-two-stage.md` → `horizon-cl5-2026-08.md`
    - `horizon-cl5-2027-04-two-stage.md` → `horizon-cl5-2027-04.md`
    - `horizon-cl6-2026-01-two-stage.md` → `horizon-cl6-2026-05.md`
    - `horizon-cl6-2026-02-two-stage.md` → `horizon-cl6-2026-06.md`
    - `horizon-cl6-2026-03-two-stage.md` → `horizon-cl6-2026-07.md`
    - `horizon-cl6-2027-01-two-stage.md` → `horizon-cl6-2027-04.md`
    - `horizon-cl6-2027-02-two-stage.md` → `horizon-cl6-2027-05.md`
- **layouts/**:
  - Updated `index.html`, `programs/list.html`, `_default/compare.html`, `partials/program-card.html`, `programs/single.html` to render and filter using `tags`.
  - Added filter chips for `Horizon Europe`, `Eureka`, and `양자협력`.
- **assets/css/main.css**:
  - Updated tag badge color classes (`.t-horizon`, `.t-eureka`, `.t-bilateral`).
- **assets/js/main.js**:
  - Updated client-side filter logic to read `data-tags` and filter by selected tag.

## Verification
- Verified Hugo build locally (`hugo --gc --minify`), all 72 pages generated without errors.
- Verified secret scan with gitleaks (`gitleaks dir --config .gitleaks.toml`).
- Verified tag filter chips on local dev server.
