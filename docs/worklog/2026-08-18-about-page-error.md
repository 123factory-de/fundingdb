---
title: "fix(about): update program categories to match actual site tags"
branch: "fix/about-page-error"
date: "2026-08-18"
---

## Request
Correct the program categories in the "이용 안내" (About) page to match the actual tags/filters used in the site (Horizon Europe, Eureka, Bilateral).

## Changes
- **content/about.md**: Replaced the outdated categories (EU 공동, 독일, 양자협력) with Horizon Europe, Eureka, and 양자협력 (Bilateral) to map 1:1 with the filters on the main page.

## Verification
- Verified Hugo build locally (`hugo --gc --minify`) outputting to `./public`.
- Verified gitleaks scan (`gitleaks dir --config .gitleaks.toml`) with zero leaks detected.
