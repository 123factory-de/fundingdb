---
title: "feat(theme): add site favicon and apple-touch-icon"
branch: "feat/add-favicon"
date: "2026-08-18"
---

## Request
Add custom favicons and apple-touch-icon copied from openinnovation.123factory.de.

## Changes
- **static/**: Downloaded and added `apple-touch-icon.png`, `favicon-16x16.png`, `favicon-32x32.png`, and `favicon.ico` to the static directory.
- **layouts/_default/baseof.html**: Linked the new favicon and apple-touch-icon files in the `<head>` tag.

## Verification
- Verified Hugo build locally (`hugo --gc --minify`) outputting to `./public`.
- Verified gitleaks scan (`gitleaks dir --config .gitleaks.toml`) with zero leaks detected.
