---
title: "feat: improve LLM discoverability"
date: 2026-11-27
branch: feat/improve-llm-discoverability
request-source: "Claude Code session, 2026-11-27"
---

## Request

Make the funding database easier for LLMs and AI agents to discover and read accurately. Six items were proposed and all were approved: `llms.txt`, per-program Markdown, `llms-full.txt`, JSON-LD structured data, a richer JSON feed, and discovery hints that point to all of them.

## Changes

1. **`/llms.txt`** (`layouts/index.llms.txt`, new `llms` home output format): site summary, data rules (official sources, `verified` date, status values, date format), links to the data files, open/planned programs sorted by deadline with status, deadline and budget, the guide pages, and closed programs under `## Optional` (llmstxt.org convention). Generated from content, so it never goes stale.
2. **Per-program Markdown** (`/programs/<slug>/index.md`): new `markdown` output format, enabled only for program pages via `cascade` in `content/programs/_index.md`. Contains key facts, the body and official links, without site chrome. Root-relative links are made absolute, and the CJK `**\ ` emphasis escape is normalized. Each HTML page advertises it with `<link rel="alternate" type="text/markdown">`.
3. **`/llms-full.txt`** (`layouts/index.llmsfull.txt`): all programs in one Markdown file. Open/planned programs include the full body; closed programs include facts and links only, which keeps the file at about 310 KB.
4. **JSON-LD** (`layouts/partials/jsonld.html`): the home page describes WebSite, Organization and a Dataset whose distributions are the JSON feed, `llms.txt` and `llms-full.txt`. Program pages describe a WebPage (`lastReviewed` = `verified`) about a MonetaryGrant (name, call ID, description, primary official URL, funders). schema.org has no grant-deadline property, so the deadline is carried in the description. Secondary links are not emitted as `sameAs`, because many are generic portal pages.
5. **JSON feed** (`/programs/index.json`): existing fields are unchanged. Added `markdown_url`, `call_id`, `status_label`, `description`, `open_date`, `deadline_note`, `amount`, `target`, `duration`, `org_eu`, `org_kr`, `apply_via`, `verified`, `links`, plus a top-level `docs` link to `llms.txt`. Missing values are `""`/`[]` so every record has the same shape.
6. **Discovery**: `robots.txt` comments point to `llms.txt`, `llms-full.txt` and the JSON feed. The home page head links the JSON feed as an alternate. The about page gains an "AI·개발자용 데이터" section.

Refactor: the program title and description logic moved from `seo-meta.html` into `layouts/partials/program-seo.html`, so the HTML head, JSON-LD, Markdown, `llms.txt` and the JSON feed share one source. Rendered titles, descriptions and canonicals are byte-identical to the previous build.

Not changed (noted for follow-up): `horizon-cl3-2026-01` (deadline 2026-11-05) and `horizon-cl6-2026-04` (deadline 2026-11-26) still have `status: open`, so they are listed as open in `llms.txt`. Closing them is a separate content task.

## Verification

- `hugo --gc --minify` builds without errors or warnings.
- Outputs exist: `/llms.txt` (24 KB), `/llms-full.txt` (312 KB), and 92 `/programs/*/index.md` files. `/about/` and `/compare/` get no Markdown output.
- All 93 JSON-LD blocks (home and 92 program pages) parse as valid JSON.
- `/programs/index.json` parses, `count` is 92, every record has a non-empty `markdown_url`, and the original fields are unchanged.
- Heading levels are correct: H1 title and H2 sections in per-page Markdown; H1 file title, H2 programs and H3 sections in `llms-full.txt`.
- `<title>`, meta description and canonical are identical to the previous build on every HTML page.
- The about page links resolve to the generated files.
