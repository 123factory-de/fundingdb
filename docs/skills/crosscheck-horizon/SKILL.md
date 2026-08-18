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

## Participation restrictions (`check_eligibility.py`)

```bash
python3 docs/skills/crosscheck-horizon/check_eligibility.py --dump /path/to/grantsTenders.json
```

Reads every topic's official "Conditions" text from the portal topic-details
endpoint and reports, per page:

- `KR-OK` / `KR-EXCL` — the topic limits participation to a list of countries.
  `KR-OK` when Korea is covered (named explicitly, or via an open "associated
  countries" scope); `KR-EXCL` when it is not, e.g. Space topics limited to
  Member States + Norway/Iceland, or a *closed* list ("the following additional
  associated countries: Canada, New Zealand, UK, Switzerland") that omits Korea.
- `CN-CTRL` — the General Annexes Part 15 "restrictions on control in Innovation
  Actions in critical technology areas": entities directly or indirectly
  controlled by China are excluded (Art. 22(5); semiconductors, AI, quantum,
  biotech IAs). This is an ownership test, not a nationality test — an ordinary
  Korean company is unaffected, so say so on the page rather than listing it as
  a bare restriction.
- `EXTRA` — topic-specific "additional eligibility criteria". These often matter
  more in practice than the country rules: CL3 security topics requiring EU
  police / border-guard / disaster authorities as beneficiaries, CL6 topics
  requiring the multi-actor approach, geographic mandates (African Union,
  Ukraine, low-income countries), consortium size caps, and topics open only to a
  named predecessor consortium.

Use the output to keep the 지원자격 bullets on each page specific and
conclusion-first, instead of a generic "일부 토픽 제한" caveat.

## What it does not check

- Amounts, budgets, and body text — spot-check those manually.
- Non-Horizon programs (Eureka clusters, bilateral calls): their sources
  (eurekanetwork.org, cluster sites, KIAT/K-PASS boards) have no machine-readable
  data, and eurekanetwork.org blocks non-browser clients — verify those in a
  browser using the per-program logs in `docs/verifications/`.

## History

- 2026-08-12: first run — 53/53 pages matched the 2026-08-11 dump.
- 2026-08-18: added `check_eligibility.py`; first run over all 53 pages found
  Korean entities excluded from 7/8 topics of HORIZON-CL4-2026-03 and 7/7 of
  HORIZON-CL4-2027-03 (Space); 16 further topics across CL4/HLTH limit
  participation to lists that include Korea; 37 topics across CL3/CL4/CL5/CL6/HLTH
  carry the China-control restriction. Page bullets and verification logs updated;
  the CL4-2027-03 page was removed (no topic open to Korean entities), leaving 52
  Horizon pages.
- 2026-08-18 (second pass): extended the script to report `EXTRA` topic-specific
  additional eligibility criteria — 82 topics carry them. Most consequential for
  Korean applicants: 18 of 21 CL3-2026-01 topics and 10 of 17 CL3-2027-01 topics
  require EU Member State / Associated Country practitioner authorities (police,
  border guard, disaster response, public procurers) as beneficiaries, and
  CL6-2026-04's only topic is open solely to a named predecessor consortium's
  coordinator. Page 지원자격 bullets were rewritten conclusion-first.
