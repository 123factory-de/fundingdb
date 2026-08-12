---
title: "feat(programs): split multi-call pages into per-call-ID entries"
branch: "feat/update-funding-programs"
date: "2026-08-12"
---

## Request
Several program pages (the six Horizon Europe cluster pages) mixed multiple different calls in one entry. Restructure the database so each call ID gets exactly one entry, with the markdown filename equal to the call ID, to avoid duplication. Page titles should stay reader-friendly; the call ID is the filename/URL and is shown in the subtitle.

## Changes
- **Removed** the six mixed-call cluster pages: `horizon-cluster-1-health-2026.md`, `horizon-cluster-2-culture-2026.md`, `horizon-cluster-3-security-2026.md`, `horizon-cluster-4-digital-2026.md`, `horizon-cluster-5-climate-2026.md`, `horizon-cluster-6-food-2026.md`.
- **Added** one entry per call ID (filename = lowercased call ID, 53 files):
  - Cluster 1 (7): `horizon-hlth-2026-01…04`, `horizon-hlth-2027-01…03`
  - Cluster 2 (4): `horizon-cl2-2026-01`, `-02`, `horizon-cl2-2027-01`, `-02`
  - Cluster 3 (2): `horizon-cl3-2026-01`, `horizon-cl3-2027-01`
  - Cluster 4 (12): `horizon-cl4-2026-01…05` (incl. `-02-two-stage`), `horizon-cid-2026-01`, `horizon-cl4-2027-01…06` (incl. `-02-two-stage`)
  - Cluster 5 (16): `horizon-cl5-2026-03…11` (incl. `-04-`, `-06-`, `-08-two-stage`), `horizon-cl5-2027-01…07` (incl. `-04-two-stage`)
  - Cluster 6 (12): `horizon-cl6-2026-01…04` plus three `-two-stage`, `horizon-cl6-2027-01…03` plus two `-two-stage`
- Naming: page titles are reader-friendly (`Horizon Europe <year> · <field>`); the exact call ID appears in the subtitle and as the filename/URL. Titles carry no stage markers ("(2단계)" removed) — stage type lives in the call ID and body. Three title pairs are therefore identical and distinguished by their subtitle/call ID (기후과학 2026, 식품 시스템 2026, 보건 2027). Entries cross-link related/successor calls.
- Front matter conventions: every Horizon entry now carries an exact `deadline` date regardless of status — closed entries use their (1st-stage) deadline just like open ones, and only the status badge differs. `planned` entries additionally carry `open_date`. 2nd-stage deadlines of two-stage calls are stated in the body. COFUND partnership calls are flagged as targeting funding-agency consortia, not companies. (The four pre-existing `korea-*` entries still use `deadline_note`; untouched as out of scope.)
- **layouts/partials/sorted-programs.html**: since closed entries now have real (past) deadline dates, sorting was extended — upcoming deadlines ascending first, then undated entries by weight, then past calls most-recent-first. The client-side JS already renders past deadlines as "마감" and flips card status, so closed cards display correctly without rebuilds.
- Data sources: baseline carried over from the previous pages (verified 2026-08-11). All per-call details — exact opening dates, deadlines (1st/2nd stage), budgets, and thematic areas — were then verified against the official Work Programme 2026–2027 PDFs (Parts 4, 7, 8, 9, and 14 for the CID call) on 2026-08-12; closed calls carry the same level of detail as open ones. Corrections found during verification: `CL4-2026-01` deadline is 2026-04-21 (old page implied mid-April range); the 2nd-stage deadlines of `CL6-2026-01-two-stage` (2026-09-23) and `CL6-2026-02-two-stage` (2026-09-15) were swapped on the old page; `CL6-2027-03` deadline is exactly 2027-05-11 (€49.05M). Newly discovered call `HORIZON-CL4-2027-06` (industry FTRI, €35M) was added.
- Removed the Germany region category for consistency across bilateral entries: `korea-germany-12` regions reduced to `["bilateral"]`; the "독일" filter chip removed from the home and programs list pages; the `de` entry dropped from region label maps (card/single/compare templates) and the `.r-de` CSS rule deleted. All bilateral cards now show a single "양자협력" chip.
- **assets/css/main.css**: `.btn` now vertically centers its label (`inline-flex` + `align-items: center`) so the "상세 보기" button label stays centered when the sibling link button wraps to two lines.
- Note: the old cluster page URLs (`/programs/horizon-cluster-*-2026/`) are removed; no aliases were added.

## Verification
- Verified Hugo build locally (`hugo --gc --minify`), all new pages generated.
- Verified secret scan with gitleaks (`gitleaks dir --config .gitleaks.toml`).
- Checked internal cross-links resolve to existing entries.
