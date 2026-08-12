# Skill: cross-check Horizon Europe pages against the EU portal

Machine-verifies every `content/programs/horizon-*.md` page against the EU Funding
& Tenders portal's official bulk dataset. Use it during any audit of program data,
or whenever portal deadlines may have shifted (extensions are common).

## Run

```bash
python3 docs/skills/crosscheck-horizon/check_horizon.py
# or, reusing an already-downloaded dump:
python3 docs/skills/crosscheck-horizon/check_horizon.py --dump /path/to/grantsTenders.json
```

Requires only the Python 3 standard library. The first run downloads the portal
dump (~130 MB) to the system temp directory; it is refreshed by the EU roughly
daily (check the file's `Last-Modified` header if freshness matters).

## What it checks

- Page `status` (`open`/`soon`/`planned`/`closed`) vs the portal status of the
  call's topics (Open/Forthcoming/Closed).
- Page `deadline` vs the set of topic deadline dates for the page's
  `callIdentifier` (taken from the portal link in the page's front matter).

`OK` per page means those facts match; exit code 0 means all pages pass.

## What it does not check

- Amounts, budgets, and body text — spot-check those manually.
- Non-Horizon programs (Eureka clusters, bilateral calls): their sources
  (eurekanetwork.org, cluster sites, KIAT/K-PASS boards) have no machine-readable
  data, and eurekanetwork.org blocks non-browser clients — verify those in a
  browser using the per-program logs in `docs/verifications/`.

## History

- 2026-08-12: first run — 53/53 pages matched the 2026-08-11 dump.
