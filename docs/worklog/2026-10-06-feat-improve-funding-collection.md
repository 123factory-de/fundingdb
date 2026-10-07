---
title: "feat: collect funding through official APIs"
---

## Request

Improve the default funding collection procedure using research supplied through
chat on 2026-10-06. Use APIs first and the existing official-source research
method second. Preserve the current branch and leave changes uncommitted.
The procedure must remain usable after temporary research files are removed.
Follow-up requests: execute collection using the funding-authoring skill, then
complete detailed verification of the 29 remaining EU calls. The previous
discovery-only stopping point did not satisfy the collection request.

## Summary

Make official APIs the first step of funding collection, execute the procedure,
save normalized candidate evidence, and apply verified additions and corrections.

## Key Changes

- Document multipart EU search, Eureka taxonomy discovery, pagination, and limits.
- Require official-page/PDF research for gaps, failures, cluster and bilateral
  sources, and detailed eligibility verification.
- Preserve source identities, call grouping, pending candidates, and evidence
  records without introducing new Hugo fields.
- Correct the audit skill's blanket claim that Eureka has no machine-readable data.
- Keep the supplied temporary files intact; the new procedure does not depend on them.
- Collected EU search/facet results and all 92 Eureka API items. Reconciled EU
  pagination duplicates and source discrepancies against the current official
  bulk dataset and fetched 508 topic-detail records.
- Saved 326 Pillar II-classified topic records and 12 current Eureka-family calls
  in `docs/collections/`, with sources and pending/excluded review states.
- Identified 32 previously unregistered EU calls: one initial addition and two Space
  exclusions, followed by detailed review of all 29 remaining calls (78 topics).
  Added 21 further calls / 70 topics, excluded 7 calls / 7 topics, and withheld
  one fully reviewed QML call for contradictory official eligibility wording.
- Added HORIZON-CID-2027-01 and a matching claim-by-claim verification log.
- Corrected dates/opening dates for three 2027 Health calls, ITEA opening wording,
  and the old Spain page's successor-call reference. Kept prior full-verification
  dates on these five targeted updates and added dated verification entries.
- Recorded unresolved Globalstars Japan domestic funding notice, Canadian partner
  funding, QML eligibility ambiguity, and a CELTIC deadline timezone discrepancy.
- Corrected the collection example's required `text` parameter and documented
  observed pagination duplicates and page-size cap.
- No dependencies, notification workflows, or protected files changed.

## Verification

- `git diff --check`: passed.
- `hugo --gc --minify --destination /tmp/fundingdb-api-first-build --cacheDir /tmp/fundingdb-api-first-cache`: passed, 76 pages.
- `gitleaks dir docs/skills --config .gitleaks.toml --no-banner`: passed.
- Reviewed relative reference links and confirmed the durable procedure does not
  link to temporary research files.
- Follow-up live collection executed EU search/facets, Eureka taxonomy/list,
  official bulk/topic details, official listings, Work Programmes, and KIAT notices.
- `python3 docs/skills/add-funding-program/scripts/validate_program.py` with the
  six changed/new program pages: passed.
- `check_horizon.py --dump /tmp/funding-current-dump.json`: final 55 pages passed,
  zero mismatches after correcting three detected Health date discrepancies.
- `check_eligibility.py --dump /tmp/funding-current-dump.json --cache /tmp/funding-collection-topics`:
  completed; heuristic restriction flags reviewed as evidence, not automatic approval.
- Normalized inventory JSON parsed; 326 unique EU topic IDs, all with reported
  budget entries; the 29-call follow-up is fully reviewed and synchronized with
  separate detailed decision evidence. Only non-EU Eureka items remain unreviewed.
- `hugo --gc --minify --destination /tmp/fundingdb-collection-build --cacheDir /tmp/fundingdb-collection-cache`:
  passed, 77 pages.
- `gitleaks dir --config .gitleaks.toml --no-banner`: passed, no leaks.
- API errors, duplicate coverage gaps, recovered detail-download failures, and
  remaining scope limits documented in the collection report. No automatic
  eligibility decisions, exhaustive country audit, or live publication claimed.

### Detailed-review validation

- Added 21 program pages and 21 matching verification logs; total new pages for
  this collection are 22, including the prior CID call.
- Reviewed all 78 topics against current Portal details and official Work
  Programmes; recovered EuroHPC Amendment 5 from the official document listing.
- Documented missing EuroHPC API restrictions, QML 50% funding exception and
  country-wording conflict, IHI topic allocations and 30%/45% private-contribution
  rules, RAISE missing budget, Cancer budget inconsistency and NEB cancellation.
- `validate_program.py`: all 92 program pages passed.
- `check_horizon.py --dump /tmp/funding-current-dump.json`: 76 Horizon pages
  checked, zero status/deadline mismatches.
- `check_eligibility.py` executed with the current cache; heuristic output was
  manually checked against the source-specific decisions.
- Production Hugo build to temporary destination/cache: passed, 98 pages.
- Final financial/identity/synchronization audit: all 29 call decisions and 78
  topic decisions match the inventory; all 70 published titles, translations,
  action rates, allocations and practical conditions match the pages and logs.
- `git diff --check`: passed after final edits.
- Whole-repository `gitleaks dir --config .gitleaks.toml --no-banner`: passed,
  zero leaks (2.26 MB scanned).
- No protected/generated/vendor files changed; all durable references work
  without the removed temporary folder. No new branch or commit created.

### Listing filter follow-up

- Chat follow-up on 2026-10-06 reported that the open-only checkbox did not
  filter the listing. The script handled changes but did not apply the current
  checkbox state on startup or browser history restoration.
- Apply filters once at initialization and on `pageshow`, preserving combined
  category/status filtering and inclusion of approaching-deadline calls.
- Node regression checks passed for restored checked startup, unchecked startup,
  checkbox changes, category combinations and history restoration. Browser
  interaction was not directly tested.
- Production Hugo build to a temporary destination/cache passed (98 pages);
  `git diff --check` passed. Changes remain uncommitted on the existing branch.

## Related Issues

None.

## Checklist

- [x] Follow repository documentation conventions.
- [x] Review the changes and run relevant validation.
- [x] Preserve the existing branch and do not commit, push, or open a Pull Request.

## Follow-up: one-pass recheck (2026-10-06)

Request: recheck the current database once from its verification logs, using official public webpages as the review authority and APIs as supporting comparisons.

Reviewed 92 pages, including 76 Horizon calls / 488 published topic rows and the sources referenced by 16 non-Horizon logs. Corrected three Cluster 4 opening dates, two topic budgets and corresponding call totals, an IA classification/rate, one healthcare title and ITEA's stored status. Flagged conflicting CELTIC timezones/event dates and Eurostars Call 11 timezone labels and replaced unconfirmed Xecs Korean financial terms with a notice-confirmation requirement. Refreshed translation-reference evidence without rewriting historical passes.

The [dated audit report](../verifications/_crosscheck-2026-10-06.md) records coverage, per-program results, five explained budget exceptions, public-page rendering limits and unresolved national notices. This is not a fresh blanket certification of every page claim. Validation: 92-page validator, 76-call status/deadline check, 488-row topic audit, eligibility text scan, Hugo build (98 pages), diff whitespace and Gitleaks passed as described in the report. No commit or deployment.
