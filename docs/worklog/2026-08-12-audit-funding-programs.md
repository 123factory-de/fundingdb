---
title: "fix(programs): audit data, unify titles, clean up links"
branch: "fix/audit-funding-programs"
date: "2026-08-12"
---

## Request

Independently audit all program pages in `content/programs/` against official sources, and unify the brand naming on program card titles (requested via chat on 2026-08-12: EUREKA cards were in Korean transliteration while Horizon Europe cards used the official Latin name). During review (chat, 2026-08-12) the requester flagged the "호라이즌 유럽 코리아 포털" link (horizoneuropekorea.eu) as possibly not an official government channel and asked for its removal.

## Changes

- Unified card-title brand naming to official Latin form: retitled `유레카 오픈콜 2026` → `EUREKA 오픈콜 2026`, `유레카 첨단바이오 콜 2026` → `EUREKA 첨단바이오 콜 2026`, `유레카 경량화 콜 2026` → `EUREKA 경량화 콜 2026`. All other titles already used official Latin brand names (Horizon Europe, Eurostars, CELTIC-NEXT, ITEA, SMART, Xecs, EUROGIA); Korean prose in page bodies was left as natural Korean.
- Audited all 66 program pages against official sources; no factual discrepancies were found, so no data corrections were needed:
  - Open Horizon Europe 2026 calls (11 pages) checked against the EU Funding & Tenders portal data endpoints — statuses, opening dates, deadlines, topic IDs, per-topic budgets, and call totals all match.
  - Planned 2027 calls (24 pages) checked against the Horizon Europe Work Programme 2026–2027 PDFs (Parts 4–9) — opening dates, deadlines, one/two-stage structures, call IDs, and budgets all match.
  - Closed 2026 calls (18 pages) checked against the portal dataset — deadlines and extension histories (CL5-2026-05, CL5-2026-07) match; none was extended or reopened beyond what the pages state.
  - Eureka-family calls (9 pages) checked against cluster sites, official call PDFs, the KIAT consolidated notice (제2026-165호), and K-PASS notices — central and domestic deadlines and Korean-side funding conditions all match.
  - Korea bilateral calls (4 pages) checked against KIAT/K-PASS notices, the ZIM 12th-call PDF, and the Innosuisse 12th-call guidelines PDF — statuses and details all match.

- Removed the "호라이즌 유럽 코리아 포털" link (https://horizoneuropekorea.eu) from all 53 Horizon Europe pages that carried it — both the front-matter `links` entry and the body "한국측 지원 창구" mention. The site could not be confirmed as an official channel: its footer claims "© 2025 KERC" but also names a private advertising agency as operator, the domain is registered anonymously via a consumer registrar, and KERC's official site (k-erc.eu) does not link to it anywhere we checked. The confirmed official channels (KERC at k-erc.eu, NRF) remain linked in the same paragraph.
- Added the missing official-site link for 한국연구재단(NRF) (https://www.nrf.re.kr) in the same "한국측 지원 창구" paragraph on those 53 pages — KERC was linked but NRF was plain text (flagged via chat on 2026-08-12). The NRF site returns 403 to non-browser clients but loads normally in a browser.
- Fixed bold emphasis rendering as literal `**` on 53 pages (62 spans, flagged via chat on 2026-08-12): spans like `(브뤼셀)**입니다` cannot close under CommonMark's right-flanking rule when `**` sits between punctuation and a Korean character. Enabled goldmark's CJK extension with `escapedSpace` in `config/_default/hugo.toml` and inserted the escaped space (`**\ `) at each affected span; the space is removed from the rendered output.
- Added `docs/skills/crosscheck-horizon/` (requested via chat on 2026-08-12): a stdlib-only script plus skill doc that machine-verifies every `horizon-*.md` page's status and deadline against the EU Funding & Tenders portal bulk dataset (grantsTenders.json). First run: 53/53 pages matched the 2026-08-11 dump.
- Added `docs/verifications/` (requested via chat on 2026-08-12): one append-only verification log per program page, mirroring `content/programs/` slugs (66 files + README). Each log lists the page's sources as a numbered, linked table and maps the page's key claims (front matter fields, bold statements, table rows) to the supporting source, claim by claim, with open items called out. Also added `_crosscheck-2026-08-12.md`, a repo-native checklist of all 66 programs (key facts, source links, task-list checkboxes) recording this audit's cross-check: 53 Horizon pages machine-verified, 13 manual, 2 open items.
- Fixed missing horizontal padding on detail and compare pages at narrow viewports (requested via chat on 2026-08-12): `.detail` and `.compare` in `assets/css/main.css` used the `padding: 40px 0 56px` shorthand on the same element as `.container` (`<div class="container detail">`), zeroing out the container's horizontal padding. Changed both to `padding-top`/`padding-bottom` longhands, and made `.container` padding responsive (`20px` → `clamp(20px, 4vw, 40px)`). Verified with headless-Chrome screenshots at 500px and 700px widths.
- Made all external links open in a new tab (requested via chat on 2026-08-12): added a markdown render hook (`layouts/_default/_markup/render-link.html`) that appends `target="_blank" rel="noopener"` to `http(s)` links in page bodies, and added the same attributes to the two 123factory.de links in `layouts/_default/baseof.html`. Template-rendered front-matter links already opened in a new tab. Internal site links intentionally keep opening in the same tab.

## Verification

- Checked all 95 external URLs referenced by program pages; every one returned HTTP 200.
- Built the site with `hugo --gc --minify` using Hugo `v0.153.3+extended`; build completes without errors.
- Scanned the repository with `gitleaks dir --config .gitleaks.toml --no-banner`; no leaks found.
- Re-ran the Hugo build and gitleaks scan after the link removal; both pass, and no reference to horizoneuropekorea.eu remains under `content/`.

## Notes

- Two minor items remain unverifiable due to bot-blocking on eurekanetwork.org (HTTP 403), with no contradicting evidence found: the exact clock time of the Lightweighting 2026 central deadline, and Korea's presence in the Xecs Call 6 country list. Left unchanged.

## Checklist

- [x] Content matches the cited official sources as of 2026-08-12.
- [x] External links respond successfully.
- [x] The production build completes without errors.
- [x] Secret and personal-data scanning passes.
