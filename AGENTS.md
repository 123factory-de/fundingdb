# AGENTS.md

Operating instructions for AI coding agents (Hermes, Claude Code, and any other AGENTS.md-compatible agent) working in this repository. This is the canonical, tool-agnostic source of truth. Tool-specific files (`CLAUDE.md`, `.agent/rules/general.md`) defer to this document.

**Read this file fully before making any change.**

---

## 🚦 Guardrails — non-negotiable

These rules are hard limits. If a task appears to require breaking one, **stop and ask a human** instead of proceeding.

1. **Never commit to `main`.** Always work on a branch and open a Pull Request. `main` is protected and deploys to production on merge.
2. **Never commit secrets or personal data.** No API keys, tokens, credentials, Korean resident registration numbers (주민등록번호), personal phone numbers, or private email addresses. Commits are scanned by gitleaks locally (`.githooks/pre-commit`) and in CI (`.github/workflows/pr-checks.yml`). Do not disable, bypass, or edit these scans.
3. **Never modify protected paths.** The following may only be changed by a trusted human maintainer via a reviewed PR — an agent must not touch them:
   - `.github/` (CI workflows)
   - `.gitleaks.toml` (secret/PII scan rules)
   - `.githooks/` (git hooks)
   - `.agent/` (agent rules)
   - `AGENTS.md`, `CLAUDE.md` (agent instructions — you may not rewrite your own guardrails)
   - `.gitmodules` (submodule config)

   CI enforces this (`protected-paths` job); a PR from a non-maintainer that touches these paths will fail.
4. **Never edit generated or vendored files.** Do not hand-edit `public/`, `resources/`, or the `themes/blowfish/` submodule.
5. **Keep changes atomic and in scope.** One task per branch/PR. If you discover unrelated work, note it — do not bundle it in.
6. **When uncertain about a destructive or irreversible action, ask.** Deleting content, force operations, history rewrites, and dependency changes warrant a human check.

---

## Project

- **Name**: `funding`
- **Owner**: 123 Factory
- **Objective**: Research, track, and maintain the funding database for Korean startups.
- **Live site**: https://funding.123factory.de/
- **Stack**: [Hugo](https://gohugo.io/) (extended) static site generator with the [Blowfish](https://github.com/nunocoracao/blowfish) theme (git submodule at `themes/blowfish`).
- **Languages**: Bilingual site — English (default) and Korean (`ko`).

## Repository layout

| Path | Purpose |
| :--- | :--- |
| `config/_default/` | Hugo configuration (`hugo.toml`, `params.toml`, `menus.*.toml`, `languages.*.toml`, `markup.toml`) |
| `content/` | Content pages and funding entries |
| `layouts/` | Custom Hugo templates overriding the theme |
| `assets/`, `static/` | Site assets and static files |
| `i18n/` | Translation strings |
| `themes/blowfish/` | Theme (git submodule — do not edit) |
| `docs/` | Workflow docs, references, agent skills, and PR worklogs |
| `.githooks/`, `.gitleaks.toml`, `.github/` | Safety guardrails (protected — see above) |
| `public/`, `resources/` | Generated output — do not edit |

## Setup & common commands

Requires Hugo **extended** (developed against `v0.153.x`) and `gitleaks` (for the commit hook).

```bash
git submodule update --init --recursive   # fetch the Blowfish theme
git config core.hooksPath .githooks       # enable the local secret-scan hook (once per clone)
brew install gitleaks                     # macOS; other platforms: gitleaks.io

hugo server -D                            # local dev server with drafts at http://localhost:1313
hugo --gc --minify                        # production build into ./public
```

Deployment is automated via GitHub Actions (`.github/workflows/deploy-pages.yml`) on merge to `main`. Do not commit changes to the generated `public/` directory as part of feature work.

## Git workflow — source of truth

Follow these documents exactly. They are authoritative:

- [docs/git-workflow/branching-strategy.md](docs/git-workflow/branching-strategy.md)
- [docs/git-workflow/commit-convention.md](docs/git-workflow/commit-convention.md)
- [docs/git-workflow/pr-convention.md](docs/git-workflow/pr-convention.md)

Key rules:

- **GitHub Flow.** Branch from `main` using prefixes: `feat/`, `fix/`, `docs/`, `refactor/`, `test/`, `chore/`.
- **Merge to `main` with `--no-ff`** (create a merge commit; never fast-forward, squash, or rebase-merge) to preserve branch history.
- **Conventional Commits.** Format `<type>[scope]: <description>`; imperative mood; subject ≤ 50 chars; no trailing period.
- **Pull Requests** follow the template and process in the PR convention doc; keep PRs atomic. All PR checks (secret scan, protected paths) must pass before merge.
- Delete feature branches after merge.

### Agent workflow for all tasks

When a user asks an agent to make any change in this repository — content, documentation, configuration, layouts, or anything else — the agent must:

1. **Branch automatically.** Before touching any file, create a branch from the latest `main` following the naming convention (e.g. `feat/add-company-acme`, `fix/update-program-dates`). Do not ask for permission to branch, and never work directly on `main`.
2. **Do the work and commit** on that branch following the commit convention. Validate the change (e.g. `hugo --gc --minify`) before reporting completion, and write the branch's worklog file (see "Worklog — mandatory for every PR" below).
3. **Ask before opening a PR, in plain language.** When the work is done, summarize what changed and ask the user whether to create a GitHub Pull Request. Do not push the branch or open a PR without the user's explicit confirmation.

   Phrase the question so a non-developer can understand it, in the user's language. Do not use bare jargon (branch, PR, merge, push); when a term is unavoidable, add a short everyday-language explanation next to it. The question must make three things clear:
   - The finished change is saved in a separate working copy (a "branch") and is **not yet visible on the live site**.
   - A Pull Request is a GitHub page that shows exactly what changed so the user can review and approve it before it goes live.
   - Approving and merging the Pull Request publishes the change to the live site (https://funding.123factory.de/).

   Example (translate naturally into the user's language): "The work is done, but it is saved in a separate workspace and is not on the live website yet. To publish it, I can open a Pull Request — a GitHub page where you can see exactly what changed and approve it. Once you approve and merge it, the change goes live. Shall I open the Pull Request?"

## Worklog — mandatory for every PR

- Every PR must include exactly one branch-specific worklog file named `docs/worklog/YYYY-MM-DD-<branch-slug>.md` (this count excludes [docs/worklog/_template.md](docs/worklog/_template.md)).
- Create the worklog on the same branch as the change and commit it **before opening the PR**.
- **The worklog file is the source of truth for the PR**: PR title = the worklog `title` field; PR description = the worklog body (from `## Request` down). Generate the PR from the file, never the other way around. If scope changes during review, update the worklog first, then sync the PR description.
- Record: the original request (summarized in the requester's intent), what changed and why, and how it was verified.
- The secret/personal-data rules apply to worklog files too — no personal names, handles, emails, or other personal data; refer to request sources by channel/system and date, not by name.
- Never modify another branch's worklog file.

## Content authoring

- Content and funding entries are Markdown with front matter. Each entry has an English file and a Korean counterpart (`*.ko.md`). Keep both language versions in sync when adding or editing content.
- Do not publish personal data. Only use approved public contact addresses (see the allowlist in `.gitleaks.toml`); adding a new one requires a human-reviewed change to that protected file.
- Reusable content tasks and skills can be documented in `docs/skills/` as the project evolves.

## Conventions

- **Language**: All documentation, code comments, commit messages, and PR text in **English**.
- **Style**: Be concise and technical.
- Proactively suggest best practices, but keep changes focused and atomic.
