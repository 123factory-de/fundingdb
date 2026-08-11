---
title: "feat: build fundingdb site with EU R&D programs"
branch: "feat/funding-db-site"
date: "2026-08-11"
---

## Request

Build a Korean-language funding database site (fundingdb.123factory.de) that delivers European and German R&D grant opportunities open to Korean companies. Requested via Slack on 2026-08-11 (company leadership request). Requirements: cover Horizon Europe, Eureka, Eurostars, the Korea-Germany ZIM-linked program, and other bilateral programs (Korea-Switzerland, Korea-France); show key facts (timing, eligibility, conditions) at a glance; link official sources; cross-check all crawled information. Design direction chosen during the session: Toss-style card grid (mockup A) with a comparison-table subpage.

## Changes

- **Hugo site scaffold** (no theme; custom layouts to avoid touching the protected `.gitmodules`):
  - `config/_default/hugo.toml` — baseURL `https://fundingdb.123factory.de/`, Korean default language
  - `layouts/` — base template, card-grid home with region filter chips and an "open only" toggle, program detail template with key-facts grid and official-source link box, comparison-table layout
  - `assets/css/main.css` — Toss-style design system (Pretendard, white cards, status badges, D-day) per the approved mockup
  - `assets/js/main.js` — client-side D-day calculation and card filtering
  - `static/CNAME` — custom domain for GitHub Pages
- **Content** (`content/programs/`, all in Korean, each with eligibility, funding conditions, schedule, application route, and official source links):
  - Horizon Europe (Pillar 2 association since 2025, RIA 100%/IA 70%)
  - Eurostars 3 (Call 11 open until 2026-09-10)
  - EUREKA Network open call (open until 2026-10-01 domestic deadline; includes clusters/Globalstars/topical calls)
  - Korea-Germany (KIAT × ZIM/AiF), Korea-Switzerland (KIAT × Innosuisse), Korea-France (KIAT × Bpifrance via Eureka), Korea-Spain (KIAT × CDTI) — 12th/2026 rounds closed, marked "next call pending"
- **Pages**: home (card grid), compare (deadline-sorted table), about (data policy and disclaimer)

## Verification

- `hugo --gc --minify` builds cleanly (13 pages); compare-table sort order verified (deadline ascending, then rolling/pending programs).
- All program facts researched from official sources (ec.europa.eu, eurekanetwork.org, zim.de, innosuisse.admin.ch, bpifrance.fr, KIAT/K-PASS 2026 integrated call notice No. 2026-165) and cross-checked with at least two sources per key fact; unverifiable dates are marked "차기 공고 대기" instead of invented.
- Cross-checked against prior internal research (startup-database repo, 2026-08 funding longlist) — figures match.
- Notable correction: the KIAT international cooperation program accepts new applications via **K-PASS (k-pass.kr), not IRIS** — confirmed in the 2026 integrated call notice and partner-agency documents; the site links K-PASS accordingly.
- Local preview verified via `hugo server` (HTTP 200).

## Notes / follow-ups

- Deployment workflow (`.github/workflows/`) is a protected path and must be added by a human maintainer; DNS record for `fundingdb.123factory.de` also needs to be set up.
- Language is Korean-only per the request; the bilingual (EN) structure described in AGENTS.md can be added later.
