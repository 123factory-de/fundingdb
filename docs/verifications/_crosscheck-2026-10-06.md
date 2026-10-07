# Cross-check report — 2026-10-06

## Request and source priority

Recheck the current program database once using `docs/verifications` as the starting point. Official public call webpages and their linked call documents take precedence in the review; APIs support discovery and systematic comparisons. Conflicting official sources remain explicit open items rather than being silently resolved in favour of an API.

## Scope and evidence

- All 92 program pages have matching verification logs and passed the content validator.
- 76 Horizon calls: status and front-matter deadline matched a fresh EU bulk dataset (Last-Modified: 2026-10-06 15:01:56 UTC). This check does not establish that every opening date or body sentence matches.
- 488 published Horizon topic rows: retrieved official topic JSON anew and compared identifiers, official titles, translation references, action types, action-based maximum rates and topic budgets. Opening dates were additionally compared against the bulk dataset. This found three stale Cluster 4 opening dates that the existing status/deadline checker does not test.
- 16 non-Horizon pages: revisited the sources in their logs and consulted current operator pages and 11 Eureka programme records. This is a targeted dates/participation review, not a fresh certification of every national funding term.
- The EU Portal public pages return JavaScript shells to the available web reader. Portal data was checked through the official endpoints; browser-rendered pages were not independently inspected. Changes to Cluster 4 were also checked against the freshly downloaded, publicly linked Work Programme Part 7 PDF, including its call-budget tables and topic conditions.
- Eligibility text was scanned using the repository helper. This is a heuristic inventory, not a proof of eligibility; previously documented exceptions remain in force. Cancelled rows do not become new published topics.

## Corrections applied

| Program | Correction | Evidence |
| :--- | :--- | :--- |
| CL4 2027-01 | Opening 22 September → 13 October 2026; MAT-PROD-49 €5M → €4.7M; call total €224M → €224.7M | [Official Part 7 PDF](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-7-digital-industry-and-space_horizon-2026-2027_en.pdf), printed pages 17–19 and 86; official topic data |
| CL4 2027-02 two-stage | Opening → 13 October; MAT-PROD-32 RIA → IA, maximum rate 70% for profit-making / 100% for non-profit entities | Same PDF, printed page 20 and topic conditions; General Annex G |
| CL4 2027-06 | Opening → 13 October; MAT-PROD-62 €15M → €13.6M; call total €35M → €33.6M; project maximum €2.5M | Same PDF, printed page 22 and topic conditions; official topic data |
| HLTH 2027-03 TOOL-08 | Official title now refers to next-generation frontier AI models for healthcare; Korean translation updated | [Official topic data](https://ec.europa.eu/info/funding-tenders/opportunities/data/topicDetails/horizon-hlth-2027-03-tool-08.json) |
| ITEA Call 2026 | Stored status planned → open | [Official current-call webpage](https://itea4.org/current-call.html): opened 15 September 2026 |
| CELTIC Autumn 2026 | Flagged conflicting deadline timezones and launch-event dates; removed unqualified claims | [Operator call webpage](https://www.celticnext.eu/celtic-next-autumn-call-2026/) vs [Eureka record](https://www.eurekanetwork.org/wp-json/wp/v2/programmes/2784); operator launch page |
| Eurostars Call 11 | Flagged historical timezone disagreement: event header CEST, body CET; date/closed status unchanged | [Official call webpage](https://www.eurekanetwork.org/programmes-and-calls/eurostars/eurostars-call-for-projects-september-2026/) |
| Xecs Call 6 | Replaced unconfirmed Korean amount/rates/duration with a domestic-notice confirmation requirement | [Eureka record](https://www.eurekanetwork.org/wp-json/wp/v2/programmes/2725): South Korea listed, funding modalities “will be added soon”; [operator call webpage](https://eureka-xecs.com/calls/) |

Translation-reference logs for CL2 2026-01, MISS 2026-04 and NEB 2026-01 were also refreshed. Some older “Official portal title” cells contained Korean translations; the new tables record the official English titles and preserve the historical tables.

## Reviewed exceptions — retained

- CL3 2027-01 FCT-01: €7.833M in the source is displayed as €7.83M; rounding, not a changed budget.
- IHI Call 13: the API repeats the €53.2M call-wide amount against all three topics. Retained the official topic-document amounts €35M / €9M / €9.2M. [Official published topic text](https://www.ihi.europa.eu/sites/default/files/uploads/Documents/Calls/IHI%20Call%2013_TOPIC%20TEXT%20final%20for%20publication.pdf).
- RAISE 2027-01-04: API budget-year data is empty; retained the €1M value supported by the published horizontal Work Programme and the prior detailed-review log.
- The earlier 29-candidate detailed review remains 21 published, seven excluded and one reviewed but unresolved. EuroHPC QML country wording is not treated as newly confirmed by this audit.

## Open items and limits

- CELTIC operator page says 23:59 CEST; Eureka says 23:59 CET for 26 October. The dedicated launch page says 10 July while the overview table says 12 July. The visible page now identifies both discrepancies.
- Xecs Korean participation is confirmed; Call-6-specific Korean financial conditions remain unpublished in the Eureka record. Generic historical KIAT conditions are not sufficient to certify them.
- K-PASS P3095 and P3108 were readable as HTML: confirmed the German 2+2 deadline 4 November and Spanish deadline 28 January. Their financial attachments were not fully reverified. Other KIAT/K-PASS notice readers can return blocked, incomplete or JavaScript-driven responses. An HTTP 200 response alone is not verification. National financial terms and domestic deadlines that could not be retrieved independently retain their earlier evidence and are not newly certified.
- Lightweighting has two different deadlines already distinguished in the page: central submission 8 October and Korean domestic submission 12 October. The card uses the domestic date; applicants must meet the earlier central deadline too. France similarly distinguishes the French 8 July and Korean 9 July submissions.
- Old dated verification sections are historical evidence, not current blanket approval. Targeted recheck sections were added to affected logs without advancing a page’s full-verification date.

## Program checklist

A checked box below means the stated audit layer was completed; it does not certify every sentence or unresolved national condition.

### Horizon — 76 calls / 488 published topic rows

- [x] [horizon-bridging-2027-01](horizon-bridging-2027-01.md): 4 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-bridging-2027-02](horizon-bridging-2027-02.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-bridging-2027-03](horizon-bridging-2027-03.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-bridging-2027-04](horizon-bridging-2027-04.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cid-2026-01](horizon-cid-2026-01.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cid-2027-01](horizon-cid-2027-01.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl2-2026-01](horizon-cl2-2026-01.md): 26 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl2-2026-02](horizon-cl2-2026-02.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl2-2027-01](horizon-cl2-2027-01.md): 24 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl2-2027-02-two-stage](horizon-cl2-2027-02-two-stage.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl3-2026-01](horizon-cl3-2026-01.md): 21 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl3-2027-01](horizon-cl3-2027-01.md): 17 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl3-2027-02-cs-eccc](horizon-cl3-2027-02-cs-eccc.md): 4 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2026-01](horizon-cl4-2026-01.md): 15 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2026-02-two-stage](horizon-cl4-2026-02-two-stage.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2026-03](horizon-cl4-2026-03.md): 8 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2026-04](horizon-cl4-2026-04.md): 15 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2026-05](horizon-cl4-2026-05.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2027-01](horizon-cl4-2027-01.md): 10 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2027-02-two-stage](horizon-cl4-2027-02-two-stage.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2027-04](horizon-cl4-2027-04.md): 11 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2027-05](horizon-cl4-2027-05.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl4-2027-06](horizon-cl4-2027-06.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2026-03](horizon-cl5-2026-03.md): 10 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2026-04-two-stage](horizon-cl5-2026-04-two-stage.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2026-05](horizon-cl5-2026-05.md): 6 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2026-06-two-stage](horizon-cl5-2026-06-two-stage.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2026-07](horizon-cl5-2026-07.md): 5 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2026-08-two-stage](horizon-cl5-2026-08-two-stage.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2026-09](horizon-cl5-2026-09.md): 8 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2026-10](horizon-cl5-2026-10.md): 8 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2026-11](horizon-cl5-2026-11.md): 5 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2027-01](horizon-cl5-2027-01.md): 7 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2027-02](horizon-cl5-2027-02.md): 10 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2027-03](horizon-cl5-2027-03.md): 11 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2027-04-two-stage](horizon-cl5-2027-04-two-stage.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2027-05](horizon-cl5-2027-05.md): 5 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2027-06](horizon-cl5-2027-06.md): 5 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl5-2027-07](horizon-cl5-2027-07.md): 8 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2026-01-two-stage](horizon-cl6-2026-01-two-stage.md): 7 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2026-01](horizon-cl6-2026-01.md): 20 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2026-02-two-stage](horizon-cl6-2026-02-two-stage.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2026-02](horizon-cl6-2026-02.md): 17 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2026-03-two-stage](horizon-cl6-2026-03-two-stage.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2026-03](horizon-cl6-2026-03.md): 10 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2026-04](horizon-cl6-2026-04.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2027-01-two-stage](horizon-cl6-2027-01-two-stage.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2027-01](horizon-cl6-2027-01.md): 23 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2027-02-two-stage](horizon-cl6-2027-02-two-stage.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2027-02](horizon-cl6-2027-02.md): 15 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-cl6-2027-03](horizon-cl6-2027-03.md): 7 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-hlth-2026-01](horizon-hlth-2026-01.md): 18 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-hlth-2026-02](horizon-hlth-2026-02.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-hlth-2026-03](horizon-hlth-2026-03.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-hlth-2026-04](horizon-hlth-2026-04.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-hlth-2027-01](horizon-hlth-2027-01.md): 10 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-hlth-2027-02-two-stage](horizon-hlth-2027-02-two-stage.md): 4 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-hlth-2027-03](horizon-hlth-2027-03.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-ju-ihi-2026-13-two-stage](horizon-ju-ihi-2026-13-two-stage.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-miss-2026-04](horizon-miss-2026-04.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-miss-2026-07](horizon-miss-2026-07.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-miss-2027-01](horizon-miss-2027-01.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-miss-2027-02](horizon-miss-2027-02.md): 6 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-miss-2027-03](horizon-miss-2027-03.md): 5 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-miss-2027-04](horizon-miss-2027-04.md): 5 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-miss-2027-05-two-stage](horizon-miss-2027-05-two-stage.md): 6 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-miss-2027-06](horizon-miss-2027-06.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-miss-2027-07](horizon-miss-2027-07.md): 2 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-nature-2027-01](horizon-nature-2027-01.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-nature-2027-02](horizon-nature-2027-02.md): 5 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-nature-2027-03](horizon-nature-2027-03.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-nature-2027-04](horizon-nature-2027-04.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-neb-2026-01](horizon-neb-2026-01.md): 9 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-neb-2027-01](horizon-neb-2027-01.md): 10 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-neb-2027-02](horizon-neb-2027-02.md): 1 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.
- [x] [horizon-raise-2027-01](horizon-raise-2027-01.md): 3 topic rows; status/deadline, titles, actions/rates and budgets reviewed with the exceptions above.

### Eureka and bilateral — 16 pages

- [x] [celtic-next-autumn-2026](celtic-next-autumn-2026.md): Date confirmed; timezone/launch-date conflicts flagged.
- [x] [eureka-biotech-call-2026](eureka-biotech-call-2026.md): Eureka record confirms 28 September 2026, closed.
- [x] [eureka-lightweighting-call-2026](eureka-lightweighting-call-2026.md): Eureka record confirms central 8 October; domestic 12 October retained with earlier notice evidence.
- [x] [eureka-open-call-2026](eureka-open-call-2026.md): Standing international call is distinct from the closed domestic 1 October round; domestic notice not newly certified.
- [x] [eurogia-call-2026](eurogia-call-2026.md): Operator confirms 29 October 2026, 17:00 CET.
- [x] [eurostars-call-11](eurostars-call-11.md): Eureka webpage confirms 10 September 2026, closed; its conflicting CEST/CET labels are flagged.
- [x] [eurostars-call-12](eurostars-call-12.md): Eureka record confirms opening 17 December 2026 and deadline 4 March 2027, forthcoming.
- [x] [itea4-call-2026](itea4-call-2026.md): Current-call webpage confirms opening and both deadlines; stored status corrected.
- [x] [korea-france-2026](korea-france-2026.md): Eureka record distinguishes French 8 July and Korean 9 July deadlines; both closed.
- [x] [korea-germany-12](korea-germany-12.md): ZIM country page and notice references revisited; historical call-specific domestic terms not newly certified.
- [x] [korea-germany-2plus2-2026](korea-germany-2plus2-2026.md): German ministry and K-PASS P3095 confirm 4 November; attachment financial terms not newly certified.
- [x] [korea-spain-2025](korea-spain-2025.md): Historical KIAT source and existing successor link reviewed; closed historical page retained.
- [x] [korea-spain-kssp-2026-2027](korea-spain-kssp-2026-2027.md): K-PASS P3108 confirms 28 January; CDTI call document revisited; attachment financial terms not newly certified.
- [x] [korea-switzerland-12](korea-switzerland-12.md): Innosuisse embedded webpage table confirms 30 June; closed; financial terms not freshly certified.
- [x] [smart-call-10](smart-call-10.md): Operator confirms PO 26 January 2027, 11:00 CET and FPP 15 April 2027, 11:00 CEST.
- [x] [xecs-call-6](xecs-call-6.md): PO/FPP dates and Korean participation confirmed; Korean financial terms unresolved.

## Validation

- Program validator: 92/92 passed.
- Horizon status/deadline checker: 76/76 matched.
- Topic audit after corrections: five remaining flags, all the documented budget rounding/source exceptions above; no unexplained title, action or topic-budget mismatch.
- Hugo production build: passed, 98 generated pages, output/cache under `/tmp`.
- `git diff --check`: passed.
- Gitleaks repository scan: passed, no leaks.
- No branch creation, commit, push or deployment.
