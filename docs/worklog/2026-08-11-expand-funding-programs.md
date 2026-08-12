---
title: "feat(programs): update and expand 2026 EU funding calls"
branch: "feat/expand-funding-programs"
date: "2026-08-11"
---

## Request
Verify and expand the funding programs database with granular European and bilateral R&D program calls.

## Changes
- **content/programs/**:
  - Decomposed Horizon Europe into individual cluster calls (Cluster 1 Health through Cluster 6 Food/Bioeconomy).
  - Added Eureka Cluster calls including CELTIC-NEXT, EUROGIA, ITEA4, SMART, and XECS.
  - Added thematic Eureka calls (Biotech, Lightweighting) and updated Eurostars to Call 11.
  - Updated bilateral R&D program calls (Germany, France, Spain, Switzerland) with round-specific information.
- **layouts/**:
  - Updated `program-card.html` and `single.html` to handle refined metadata and badges.
- **assets/js/main.js**:
  - Updated client-side filtering script.

## Verification
- Verified Hugo build locally (`hugo --gc --minify`).
- Verified secret scan with gitleaks (`gitleaks dir --config .gitleaks.toml`).
