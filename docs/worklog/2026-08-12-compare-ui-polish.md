---
title: "fix(compare): improve compare table styles and clean up link labels"
branch: "fix/compare-ui-polish"
date: "2026-08-12"
---

## Request
Polish the compare table and program card UI:
1. Prevent the "모집중" status badge from breaking into one character per line in narrow columns.
2. Prevent 지원규모, 지원대상, 접수마감 cells from wrapping mid-phrase, allowing the program name column to take the remaining width.
3. Standardize deadline display in the compare table to show clean dates.
4. Clean up redundant deadline suffixes from program link names.

## Changes
- **assets/css/main.css**:
  - `.badge`: added `display: inline-block; white-space: nowrap` so badge labels never wrap.
  - Compare table: `td.name` takes remaining width (`width: 100%`); `td.amount`, `td.target`, `td.deadline` set to `white-space: nowrap`.
- **layouts/_default/compare.html**:
  - Added cell styling classes (`amount`, `target`, `deadline`) and extracted clean date string for deadline display.
- **content/programs/** (10 files):
  - Removed duplicate `(마감 …)` / `(국내 마감 …)` suffixes from link `name` fields.

## Verification
- Verified Hugo build locally (`hugo --gc --minify`).
- Verified secret scan with gitleaks (`gitleaks dir --config .gitleaks.toml`).
- Verified rendered compare table and badges on local dev server.
