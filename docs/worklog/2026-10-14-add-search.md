---
title: "feat: add full-text search to program list"
date: 2026-10-14
branch: feat/add-search
request-source: "Claude Code session, 2026-10-14"
---

## Request

The site had no search. The funding cards alone do not reveal which field/area
a program funds — that detail lives in the program body — so search should also
cover body text, not just card metadata. A follow-up noted that searching a
program's name (e.g. `eurogia`) surfaced unrelated pages that merely link to it,
which should not happen.

## Changes

Client-side full-text search, with no external libraries, layered onto the
existing tag-filter and "모집중만 보기" toggle on the home and programs-list
pages. Hugo emits a search index that the browser fetches once when the visitor
starts searching.

- `config/_default/hugo.toml` — enable a JSON output on the home page
  (`home = ["HTML", "JSON"]`) so the search index renders at `/index.json`.
- `layouts/index.json` (new) — one entry per program with `slug` plus a
  lowercased `text` blob combining card metadata (title, subtitle, tag/status
  labels, amount, target, organisations, apply route) and the full rendered
  body. The anchor text of links pointing to other program pages
  (`/programs/...`) is stripped from the indexed body.
- `layouts/partials/program-card.html` — add `data-slug` so the client maps
  index entries to rendered cards for show/hide.
- `layouts/index.html`, `layouts/programs/list.html` — add a search input above
  the filter chips and a "no results" message after the grid.
- `assets/js/main.js` — fetch `/index.json` once on first focus/input, match the
  query (space-separated terms, AND) against each card's indexed text, and
  combine with the existing tag and open-only filters. Falls back to the card's
  own visible text until the index loads; restores the query on reload / history
  navigation.
- `assets/css/main.css` — style the search input and no-results message using
  the existing design tokens.

Decisions:

- Full-text over the body (vs. searching only card fields) was chosen because
  the field/area a program funds appears only in the body. A no-dependency
  substring approach was chosen over a search library (e.g. Fuse.js) to match
  the site's existing minimal vanilla-JS style; Korean needs no stemming.
- The cross-reference noise (a program name matching every page that links to
  it) was fixed at the index layer by stripping internal `/programs/...` anchor
  text, rather than by deleting the reader-facing navigation sections (e.g.
  "관련 유레카 경로"). This keeps the navigation for readers and applies to
  every page automatically. Pre-extracting per-program keywords into front
  matter was rejected as it would require editing ~90 content files by hand.

## Verification

- `hugo --gc --minify`: builds cleanly; `/index.json` renders with 92 entries
  including body text; `node --check` passes on the JS.
- Search simulation over the built index: `기후`→36, `바이오`→35, `반도체`→24,
  `horizon health`→5, `양자협력`→6 programs.
- Cross-reference fix confirmed: `eurogia`→only `eurogia-call-2026`,
  `celtic`→only `celtic-next-autumn-2026`, `xecs`→only `xecs-call-6`,
  `itea`→only `itea4-call-2026` (previously each also matched the Eureka Open
  Call page). The remaining `smart` match on the Open Call page is the real body
  term "SmartSimple", not a cross-reference.
- Search markup (`#q`, `data-slug`, `.no-results`) present in the built HTML of
  both the home and `/programs/` pages.
- Live browser UI test skipped — the Chrome extension was not connected.
