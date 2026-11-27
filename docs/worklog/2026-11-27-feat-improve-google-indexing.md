---
title: "feat: improve search indexing signals"
date: 2026-11-27
branch: feat/improve-google-indexing
request-source: "Claude Code session, 2026-11-27 (based on the 2026-11-27 site analytics review)"
---

## Request

Google Search Console reports 0 of 96 URLs indexed: the home page was crawled once (2026-08-19) and not indexed, and every other URL is "Discovered – currently not indexed". Audit the site against that analysis and fix the on-site causes that can be addressed in this repository.

## Changes

Audit findings that needed no change: the home page renders all 92 program cards and links in static HTML (no JS-only content), all URLs return HTTP 200 without `noindex`, the sitemap lists 96 URLs, alias redirects are correct, and internal linking between home, compare and program pages is in place.

Fixes:

1. **Canonical URL** — no page emitted `<link rel="canonical">`. Added it to every page via the new `layouts/partials/seo-meta.html`, included from `baseof.html`.
2. **Unique meta descriptions** — all 92 program pages fell back to the same site-wide description. Program pages without an explicit `description` now get one built from front matter: title, subtitle, deadline (or `deadline_note`), budget and eligibility. Generated rather than hand-written so it stays in sync with the data; an explicit front-matter `description` still takes precedence.
3. **Call ID in titles** — Horizon Europe program titles now append the official call identifier (first ` · ` segment of `subtitle`, upper-cased), e.g. `Horizon Europe 2026 · 에너지 (HORIZON-CL5-2026-11)`, matching how calls are searched.
4. **Duplicate titles** — three title pairs (single-stage vs two-stage calls sharing a Korean title) were identical; the call ID from item 3 makes them distinct.
5. **robots.txt** — added `layouts/robots.txt` with `Allow: /` and a `Sitemap:` line pointing at the absolute sitemap URL.

Housekeeping: added `/temp/` to `.gitignore` so local analysis notes used for this audit are never committed.

Out of scope (off-site): building external links (www menu, blog, LinkedIn) and requesting re-indexing in Search Console after deploy.

## Verification

- `hugo --gc --minify` builds without errors or warnings (100 pages).
- Every generated HTML page contains a canonical link pointing at its own permalink.
- No duplicate `<title>` and no duplicate meta description across generated pages.
- Spot-checked home, `/programs/`, a Horizon call, a two-stage call, a bilateral call with `deadline_note`, and a Eurostars call.
- Generated `robots.txt` contains `Sitemap: https://fundingdb.123factory.de/sitemap.xml`.
