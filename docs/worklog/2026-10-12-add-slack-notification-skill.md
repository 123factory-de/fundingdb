---
title: "feat: add Slack notification skill and machine-readable program feed"
---

## Request

Direct maintainer request (session, 2026-10-12): send each funding program in
`content/programs/` to a Slack channel via an incoming webhook, one message per
program. Make the workflow reusable by other AI agents working from the live
site, with a reliable way to find programs added after a given date — which the
site did not previously expose.

## Summary

Add a Slack notification skill that posts program pages to a channel via an
incoming webhook, and publish a machine-readable JSON feed at
`/programs/index.json` so any agent can select programs by added (`date`) or
updated (`lastmod`) date without keeping local state. The webhook URL is read
only from the `SLACK_WEBHOOK_URL` environment variable and is never stored in
the repository.

## Key Changes

- Add `docs/skills/add-slack-notification-skill/` with `SKILL.md` and
  `scripts/notify_slack.py`. The script sends one Slack Block Kit message per
  program (Korean, matching the site): title, status/deadline/amount/target/
  Korean org/submission channel, short summaries of the body `## 지원분야` and
  `## 지원자격` sections, source links, and a detail-page button. It selects
  programs by slug or by feed filter (`--added-since`, `--updated-since`,
  `--status`, `--skip-expired`), sends nearest-deadline first, and supports
  `--dry-run` and `--delay`.
- Add the JSON feed: enable `enableGitInfo` and add `JSON` to the `programs`
  section outputs in `config/_default/hugo.toml`, plus `layouts/programs/list.json`
  emitting `slug`, `url`, `title`, `subtitle`, `status`, `tags`, `deadline`,
  `date` (added), and `lastmod` (git-derived).
- Introduce a `date` front-matter field (creation/added date) on all 92 program
  pages, backfilled once from each file's first-commit date in git history.
- Document `date` in the `add-funding-program` skill and require it in
  `validate_program.py`, so new entries always record their added date.
- Ignore `.env` / `.env.*` in `.gitignore` for local webhook configuration.
- Do not change protected, generated, vendored, or unrelated files.

## Verification

- `python3 docs/skills/add-funding-program/scripts/validate_program.py`: 92
  program pages passed (with `date` newly required).
- `hugo --gc --minify`: passed with no errors or warnings; feed renders at
  `public/programs/index.json` with `count` 92.
- Feed filtering exercised: `--added-since 2026-09-01` selects 26 programs;
  `--added-since 2026-09-28 --skip-expired` selects 24, ordered by nearest
  deadline.
- `notify_slack.py` exercised end to end via `--dry-run` and against a live
  webhook (supplied through the environment, not committed); messages render as
  intended.

## Related Issues

None.

## Checklist

- [x] Follow repository documentation conventions.
- [x] Keep the change atomic and in scope.
- [x] Run the applicable validation and build checks.
- [x] Keep secrets out of the repository (webhook via environment only).
- [x] Preserve protected, generated, vendored, and unrelated paths.
