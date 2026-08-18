---
title: "feat(analytics): add Google Analytics 4 tag support"
branch: "feat/add-google-tag"
date: "2026-08-18"
---

## Request
Provide support for Google Analytics 4 (Google tag) tracking across the website.

## Changes
- **config/_default/hugo.toml**: Added `googleTagId` parameter with the site's GA4 ID (`G-SC48CT0M8S`) to site parameters configuration.
- **layouts/_default/baseof.html**: Injected the Google tag tracking script block in `<head>` template, which conditionally renders only when `googleTagId` is set.

## Verification
- Verified Hugo build locally (`hugo --gc --minify`) outputting to `./public`.
- Verified gitleaks scan (`gitleaks dir --config .gitleaks.toml`) with zero leaks detected.
