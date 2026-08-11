---
title: "ci: add GitHub Pages deploy and PR check workflows"
branch: "ci/setup-github-pages"
date: "2026-08-11"
---

## Request
Set up GitHub Pages deployment automation and PR verification workflows.

## Changes
- **.github/workflows/deploy-pages.yml**: Added workflow to build the Hugo site and deploy automatically to GitHub Pages on pushes to `main` and via workflow dispatch.
- **.github/workflows/pr-checks.yml**: Added PR check workflow for secret/PII scanning using gitleaks and protected path enforcement.
- **.gitleaks.toml**: Added gitleaks configuration including rules for PII (Korean resident numbers, phone numbers, email allowlists).

## Verification
- Verified Hugo build locally (`hugo --gc --minify`) outputting to `./public`.
- Verified gitleaks scan (`gitleaks dir --config .gitleaks.toml`) with zero leaks detected.
