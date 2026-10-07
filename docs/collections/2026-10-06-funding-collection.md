# Funding collection — 2026-10-06

## Scope and result

Run the API-first funding collection procedure for open/forthcoming opportunities
for Korean companies, then reconcile with official websites, PDFs, and notices.
This run includes discovery, targeted corrections and a detailed review of all
29 previously pending EU calls (78 active topics). It does not claim coverage of
every available European funding opportunity.

- Saved **326 EU topic records across 63 Pillar II-classified calls** and **12 current
  Eureka-family call records** in [the normalized inventory](2026-10-06-funding-candidates.json).
- Found **32 EU calls absent from the original program list**: added one verified
  call, excluded two Space calls, and identified 29 calls for detailed review.
  The follow-up reviewed all 29: **21 added, 7 excluded, 1 withheld for contradictory
  official eligibility wording**. There are now **22 added program pages in total**.
  See the [detailed review](2026-10-06-detailed-call-review.md) and matching evidence.
- Added [HORIZON-CID-2027-01](../../content/programs/horizon-cid-2027-01.md)
  and its [verification log](../verifications/horizon-cid-2027-01.md): two IA topics,
  €265M combined indicative budget; application opening 2027-01-12 and deadline
  2027-09-15 at 17:00 Brussels local time.
- Corrected three existing Health call schedules, the ITEA opening wording, and
  the obsolete successor-call statement on the 2025 Spain page.
- Found Globalstars Japan 2026 as a new international candidate. Korea is listed
  and KIAT support is described, but the specific 2027 domestic notice remains
  an open item. No verified program page was created for it.

`pending` means not cleared for publication. Null eligibility flags mean unknown,
not eligible by default. Existing pages are not re-certified by their presence
in a candidate inventory. Cancelled records are retained with an exclusion note.

## API requests and coverage

### EU search and facets

[Search API documentation](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/support/apis).
POST endpoint used:

```text
https://api.tech.ec.europa.eu/search-api/prod/rest/search?apiKey=SEDIA&text=*&pageSize=100&pageNumber=1&language=en
```

Multipart `query` was a JSON file with type `1`, statuses `31094501`/`31094502`,
language `en`, programmePeriod `2021 - 2027`, and frameworkProgramme `43108390`.
The same query was sent to the `facet` endpoint. Facets confirmed Forthcoming
`31094501` and Open for submission `31094502`; topic details confirmed grant type
and Horizon programme identity. Broad search was intentionally followed by
Pillar II classification and detailed conditions, rather than a Korea keyword.

All **9 pages** responded with the same total of **820**. Raw result counts were
100 for pages 1–8 and 20 for page 9, but only **744 unique records** were returned.
A requested pageSize of 1000 was capped at 100. Some search records retained
open/forthcoming codes despite past deadlines. Per-call recovery requests also
encountered HTTP 500, so broad API coverage is explicitly **incomplete**.
The API-only count must not be reported as 820 distinct valid opportunities.

The first request omitted `text` and returned HTTP 400; adding `text=*` succeeded.
The default collection reference has been updated with these observations.

### Official bulk dataset fallback

Downloaded the [official Portal dataset](https://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json)
with HTTP 200. Response Last-Modified: **2026-10-06 13:37:56 UTC**. Its current
Horizon Open/Forthcoming subset contained **378 unique topics**, 23 of which were
absent from the broad API results. The search index and bulk source are not
identical snapshots. Do not add their counts together.

Used this dataset to recover missing topic identities and dates, applied remaining
deadline and Pillar II classification checks, and fetched official topic detail
JSONs. **508 topic details** were retrieved for existing pages and new candidate
calls, including historical/cancelled records needed for comparison. A connection
reset and partial timeout were recovered by retry; the cached JSONs were parsed.
Topic details and Work Programme PDFs, rather than search labels alone, supported
published conclusions.

### Eureka WordPress API

Queried [taxonomy](https://www.eurekanetwork.org/wp-json/wp/v2/programmes-type?per_page=100)
and [programmes](https://www.eurekanetwork.org/wp-json/wp/v2/programmes?per_page=100&page=1).
Both returned HTTP 200. Pagination headers confirmed **92 records, one page**.
Taxonomy reconfirmed Eurostars 5, Clusters 7, Network Projects 8, and Globalstars 9.
The 92 records include events, introductions, libraries, and past calls; they are
not 92 current grants. Application dates were read from official detail pages.

## Second-pass official sources

- [Eureka open calls, page 1](https://www.eurekanetwork.org/programmes-and-calls/?status=open),
  [page 2](https://www.eurekanetwork.org/programmes-and-calls/page/2/?status=open),
  and [upcoming calls](https://www.eurekanetwork.org/programmes-and-calls/?status=upcoming)
  reconciled the current program-family calls in the inventory.
- [ITEA current call](https://itea4.org/current-call.html) confirmed the existing
  call is now open and its PO/FPP dates remain 2026-11-02 / 2027-02-11.
- [CELTIC operator call](https://www.celticnext.eu/celtic-next-autumn-call-2026/)
  uses 23:59 **CEST**, while the Eureka listing uses **CET**, for 2026-10-26.
  Retained the existing operator-sourced time; this discrepancy needs operator
  confirmation before relying on an exact UTC deadline.
- [KIAT 2026 integrated plan](https://www.kiat.or.kr/front/board/boardContentsView.do?contents_id=2afc980801cb4465861835970df2c9f0)
  supplied national funding context, including Globalstars Japan's pending domestic
  schedule. [KIAT multilateral notice](https://www.kiat.or.kr/front/board/boardContentsView.do?contents_id=0d95ab4b466b4e4f943b73468ebe4109)
  was also consulted; it does not establish a new Korean 2027 round for every
  international call.
- [KIAT Spain notice, 2026-09-21](https://kiat.or.kr/front/board/boardContentsView.do?contents_id=3254f8db3eb5477a923f7e1306fe71db)
  is the already-registered **KSSP 2026–2027** round; its attached English notice
  and Korean deadline matched the existing identity. It was not added twice.

## Existing Health schedule corrections

The [Health Work Programme](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)
call overviews, bulk dataset, and topic actions agree:

| Call | Opening | Deadline (17:00 Brussels local time) |
| :--- | :--- | :--- |
| HORIZON-HLTH-2027-01 | 2026-10-29 | 2027-02-17 |
| HORIZON-HLTH-2027-02-two-stage | 2026-10-29 | 2027-02-17; second stage 2027-09-16 |
| HORIZON-HLTH-2027-03 | 2027-06-03 | 2027-09-16 |

Updated front matter and body dates together. These targeted checks do not
advance the pages' full `verified` dates. Their verification logs record the
limited scope separately.

## New EU call inventory

Dates below are candidate deadline dates from the official bulk source.
The JSON inventory contains individual identifiers, titles, opening dates, action
types, reported budgets, restriction flags, source URLs, and review status.
Pillar II classification alone does not establish company or funding eligibility,
especially for cross-programme, institutional partnership, or doctoral actions.

| Call | Topics | Deadline dates | Review |
| :--- | ---: | :--- | :--- |
| [HORIZON-BRIDGING-2027-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-BRIDGING-2027-01&isExactMatch=true) | 4 | 2027-02-16 | verified |
| [HORIZON-BRIDGING-2027-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-BRIDGING-2027-02&isExactMatch=true) | 1 | 2027-01-28 | verified |
| [HORIZON-BRIDGING-2027-03](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-BRIDGING-2027-03&isExactMatch=true) | 3 | 2027-06-15 | verified |
| [HORIZON-BRIDGING-2027-04](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-BRIDGING-2027-04&isExactMatch=true) | 3 | 2027-02-16 | verified |
| [HORIZON-CID-2027-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CID-2027-01&isExactMatch=true) | 2 | 2027-09-15 | verified |
| [HORIZON-CL3-2027-02-CS-ECCC](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-02-CS-ECCC&isExactMatch=true) | 4 | 2027-09-15 | verified |
| [HORIZON-CL4-2027-03](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL4-2027-03&isExactMatch=true) | 7 | 2027-09-02 | excluded |
| [HORIZON-CL4-2027-07](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL4-2027-07&isExactMatch=true) | 2 | 2028-01-20 | excluded |
| [HORIZON-JU-EUROHPC-2026-NAPT-11](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-JU-EUROHPC-2026-NAPT-11&isExactMatch=true) | 1 | 2026-11-17 | excluded |
| [HORIZON-JU-EUROHPC-2026-NQKD-12](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-JU-EUROHPC-2026-NQKD-12&isExactMatch=true) | 1 | 2026-11-17 | excluded |
| [HORIZON-JU-EUROHPC-2026-QEXP-14](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-JU-EUROHPC-2026-QEXP-14&isExactMatch=true) | 1 | 2026-11-17 | excluded |
| [HORIZON-JU-EUROHPC-2026-QML-07](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-JU-EUROHPC-2026-QML-07&isExactMatch=true) | 1 | 2027-01-28 | reviewed_unresolved |
| [HORIZON-JU-EUROHPC-2026-QTI-13](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-JU-EUROHPC-2026-QTI-13&isExactMatch=true) | 1 | 2026-11-17 | excluded |
| [HORIZON-JU-EUROHPC-2026-SPT-10](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-JU-EUROHPC-2026-SPT-10&isExactMatch=true) | 1 | 2026-11-17 | excluded |
| [HORIZON-JU-EUROHPC-2026-TIPT-09](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-JU-EUROHPC-2026-TIPT-09&isExactMatch=true) | 1 | 2026-11-17 | excluded |
| [HORIZON-JU-IHI-2026-13-two-stage](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-JU-IHI-2026-13-two-stage&isExactMatch=true) | 3 | 2026-10-08, 2027-04-21 | verified |
| [HORIZON-MISS-2026-07](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-MISS-2026-07&isExactMatch=true) | 1 | 2027-01-13 | verified |
| [HORIZON-MISS-2027-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-MISS-2027-01&isExactMatch=true) | 2 | 2027-09-21 | verified |
| [HORIZON-MISS-2027-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-MISS-2027-02&isExactMatch=true) | 6 | 2027-09-16 | verified |
| [HORIZON-MISS-2027-03](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-MISS-2027-03&isExactMatch=true) | 5 | 2027-09-21 | verified |
| [HORIZON-MISS-2027-04](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-MISS-2027-04&isExactMatch=true) | 5 | 2027-10-07 | verified |
| [HORIZON-MISS-2027-05-two-stage](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-MISS-2027-05-two-stage&isExactMatch=true) | 6 | 2027-04-08, 2027-09-14 | verified |
| [HORIZON-MISS-2027-06](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-MISS-2027-06&isExactMatch=true) | 1 | 2027-09-21 | verified |
| [HORIZON-MISS-2027-07](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-MISS-2027-07&isExactMatch=true) | 2 | 2027-09-22 | verified |
| [HORIZON-NATURE-2027-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-NATURE-2027-01&isExactMatch=true) | 3 | 2027-01-14 | verified |
| [HORIZON-NATURE-2027-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-NATURE-2027-02&isExactMatch=true) | 5 | 2027-01-14 | verified |
| [HORIZON-NATURE-2027-03](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-NATURE-2027-03&isExactMatch=true) | 1 | 2027-09-16 | verified |
| [HORIZON-NATURE-2027-04](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-NATURE-2027-04&isExactMatch=true) | 1 | 2027-02-16 | verified |
| [HORIZON-NEB-2027-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-NEB-2027-01&isExactMatch=true) | 10 | 2027-12-01 | verified |
| [HORIZON-NEB-2027-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-NEB-2027-02&isExactMatch=true) | 1 | 2027-09-15 | verified |
| [HORIZON-RAISE-2026-01-MSCA](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-RAISE-2026-01-MSCA&isExactMatch=true) | 1 | 2026-11-24 | excluded |
| [HORIZON-RAISE-2027-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-RAISE-2027-01&isExactMatch=true) | 3 | 2027-02-02 | verified |

## Eureka decisions and remaining checks

| Candidate | Decision |
| :--- | :--- |
| Lightweighting; CELTIC Autumn; EUROGIA Call 31; ITEA 2026; Xecs Call 6; SMART Call 10; Eurostars Call 12 | Existing identities matched. International schedules/country lists collected; national funding remains subject to applicable domestic notices. |
| Globalstars Japan 2026 (`eureka:3018`) | New, pending domestic 2027 notice. International opening 2026-10-07, deadline date 2027-01-20; verify exact submission time. Japan mandatory, European partner optional. |
| Disaster resilience 2026 (`eureka:2491`) | Excluded from default Korean-funded results: Korea absent from call country list. |
| Xecs Quantum 2026 (`eureka:2711`) | Excluded from default Korean-funded results: Korea absent from call country list. |
| Canada call 8 (`eureka:2862`) | Pending: non-participating partners may join with secured funding, but Korean funding is unconfirmed; Canadian preliminary deadlines have passed. |
| Standing Network Projects call (`eureka:56`) | Existing international call remains open; the Korean 2026 domestic round remains closed. Do not reopen the page based on international status. |

All 29 EU reviews checked country/control rules, beneficiary types, funding,
consortium conditions, detailed scope, and relevant Work Programmes before page
creation. The QML call was fully reviewed but withheld for contradictory wording. Space calls 2027-03 and 2027-07 exclude Korean entities through explicit
country lists and were not published. EuroHPC participating-state restrictions and RAISE doctoral funding rules led to
seven exclusions. BRIDGING predecessor-project and strengthened consortium
requirements are documented on the added pages. No exhaustive bilateral-country or
cluster-operator audit is claimed by this run.

## Validation

- Program validator: the final whole-repository results are in the worklog.
- Horizon status/deadline checker: initial 54-page run identified the three Health
  mismatches; initial 55-page run passed; final expanded check results are in the worklog.
- Existing eligibility checker executed against the freshly fetched topic cache;
  its heuristic flags support review, not automatic funding approval.
- Final build, diff and secret scan results are recorded in the branch worklog.
- No commit, push, Pull Request, or live-site publication performed.
