# Program verification logs

One file per program page, mirroring `content/programs/`:
`content/programs/<slug>.md` ↔ `docs/verifications/<slug>.md`.

Each file is an append-only log of verification passes for that program — what was
checked, against which official sources, the result, and any items that could not be
confirmed. This directory is documentation only; it is not published to the site.

Each log lists the page's sources as a numbered table (S1, S2, …) and maps the
page's key claims — front matter fields, bold statements, and table rows — to the
source that supports each one, so a reviewer can click straight through.

Audit-wide checklists live in dated `_crosscheck-YYYY-MM-DD.md` files (one per
audit): every program with its key facts, source links, and a task-list checkbox.
Horizon pages can be machine-checked first via `docs/skills/crosscheck-horizon/`.

## Rules

- Whenever a program page's `verified:` front-matter date is updated, add a new dated
  section (newest first) to its log file here in the same branch/PR.
- Record the sources actually consulted, not just the page's link list, and note
  source quirks that affect re-verification (e.g. sites that block non-browser
  clients, pages that no longer show a needed detail).
- Keep unresolved checks under an explicit "Open item" note so the next pass starts
  there.
- When a new program page is added to `content/programs/`, create its log file here.
- The repo-wide secret/personal-data rules apply — no personal names or contacts.
