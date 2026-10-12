---
name: add-slack-notification-skill
description: Notify a Slack channel about fundingdb funding programs via an incoming webhook. Use when posting one or more program pages to Slack, announcing newly added or recently updated programs, or building an automated feed-driven alert. Reads program data from the site's machine-readable feed (/programs/index.json) so any agent can select programs by added/updated date without keeping local state.
---

# Send funding programs to Slack

Post `content/programs/` entries to a Slack channel, one message per program. Follow the repository `AGENTS.md`; never commit the webhook URL or any secret.

## Interface

- **Script**: `scripts/notify_slack.py` (Python 3, standard library; uses `certifi` for TLS if installed).
- **Secret**: the Slack incoming webhook URL is read from the `SLACK_WEBHOOK_URL` environment variable. Never hardcode it. A local `.env` (git-ignored) is the convention:
  ```bash
  echo 'SLACK_WEBHOOK_URL="https://hooks.slack.com/services/XXX/YYY/ZZZ"' > .env
  set -a; . ./.env; set +a
  ```
- **Feed**: the site publishes `https://fundingdb.123factory.de/programs/index.json`. Each entry has `slug`, `url`, `title`, `subtitle`, `status`, `tags`, `deadline`, `date` (added date), and `lastmod` (last change, git-derived). The feed is sorted newest-added first.

## Selecting which programs to send

Two ways:

1. **By slug** — name one or more program filenames (without `.md`), in send order:
   ```bash
   python3 scripts/notify_slack.py korea-germany-2plus2-2026 celtic-next-autumn-2026
   ```

2. **By feed filter** — let the script read the feed and pick programs. This is how another agent finds newly added/updated programs with no local snapshot:
   ```bash
   # programs added on/after a date:
   python3 scripts/notify_slack.py --added-since 2026-09-01
   # programs changed on/after a date, open only, skipping expired calls:
   python3 scripts/notify_slack.py --updated-since 2026-10-01 --status open --skip-expired
   ```
   Feed-selected programs are sent nearest-deadline first. By default the script reads the local build (`public/programs/index.json`) and falls back to the live URL; pass `--feed <path-or-url>` to override.

Options: `--dry-run` prints the Slack payload instead of sending; `--delay <seconds>` sets the gap between messages (default 1.0); `--skip-expired` drops programs whose `deadline` is before today.

## Message content

Each message is built from the program's front matter and body: title header, subtitle, and fields for status, deadline, amount, target, Korean administering org, and submission channel, plus a short summary of the body `## 지원분야` and `## 지원자격` sections, the source links, and a button to the detail page. Message text is Korean, matching the site.

## Scope and limits

- The script builds the rich message from the local `content/programs/*.md` files, so it must run inside a repository checkout. The feed is used only to decide *which* programs to send.
- Sending is irreversible once posted. For a large batch, preview with `--dry-run` first and confirm the selection count.
- The feed only reflects the live site after a change is merged to `main` and deployed. The `date` field is set once when a program is added (see the `add-funding-program` skill); do not change it on later edits.
