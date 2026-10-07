# Default funding collection method

Use APIs for first-pass candidate discovery. Use official websites, notices, PDFs,
and browser research for second-pass coverage and verification. This procedure
requires no notification service or temporary research files.

For final verification, prioritise official public call webpages and their linked
call documents. APIs support discovery and comparison. When official sources
disagree, record the discrepancy and an open item; do not silently prefer the API.
A JavaScript shell or HTTP 200 response is not evidence that the visible webpage
was checked. State when only the underlying official data could be read.

## 1. Define the collection scope

Record the collection date, target programs, and requested period. By default,
look for open and forthcoming calls for companies incorporated in Korea that can
receive funding without establishing a European entity. Retain unresolved
candidates in research notes, separately from verified program pages.

For audits, also retrieve the closed calls needed to verify existing pages;
an open/forthcoming discovery query cannot verify closed status.

## 2. First pass: official APIs

### EU Funding & Tenders

Official documentation: [Portal APIs](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/support/apis).

Send a POST with a JSON **file attachment** in multipart field `query`. Do not
substitute an ordinary form string. A starting discovery request is:

```bash
cat > /tmp/funding-query.json <<'JSON'
{
  "bool": {
    "must": [
      {"terms": {"type": ["1"]}},
      {"terms": {"status": ["31094501", "31094502"]}},
      {"term": {"language": "en"}}
    ]
  }
}
JSON

curl --fail-with-body --max-time 60 -X POST \
  'https://api.tech.ec.europa.eu/search-api/prod/rest/search?apiKey=SEDIA&text=*&pageSize=25&pageNumber=1&language=en' \
  -F 'query=@/tmp/funding-query.json;type=application/json'
```

These type/status values were used in the 2026-10-06 research. Reconfirm their
meaning with the official documentation, Portal filters, or the corresponding
`https://api.tech.ec.europa.eu/search-api/prod/rest/facet?apiKey=SEDIA`
service before relying on them. `SEDIA` is the public Portal API parameter;
do not add private credentials to research files.

The example is a broad grant discovery query, **not a Pillar II or Korean
eligibility filter**. Configure and verify the Horizon Europe/Pillar II filters
using Portal requests or facets. Program code `43108390` was observed in a
successful Horizon query, but is not itself proof of Pillar II eligibility.
Do not search only for `Korea`: associated-country eligibility can be stated
without naming Korea.

The search service requires `text`; omitting it returned HTTP 400 during the
2026-10-06 collection. `text=*` returned broad discovery results in that run.

Check HTTP status and the JSON `totalResults`/`results` structure, retrieve every
result page, and compare **unique topic IDs** with the reported total. Matching
raw row counts is insufficient: the 2026-10-06 relevance-sorted search returned
820 rows but only 744 unique records across nine pages. Requested page sizes
above 100 were capped at 100. Record missing pages, duplicate coverage gaps, or
inconsistent totals as incomplete coverage and reconcile against official
call details or the current Portal bulk dataset. Keep topic IDs and parent
call IDs so topic-level results can be grouped into the repository's call pages.

### Eureka

Use the official site's public WordPress API:

```text
GET https://www.eurekanetwork.org/wp-json/wp/v2/programmes-type?per_page=100
GET https://www.eurekanetwork.org/wp-json/wp/v2/programmes?per_page=25&page=1
```

Reconfirm the taxonomy before filtering. The 2026-10-06 research observed
Eurostars `5`, Eureka Clusters `7`, Network Projects `8`, and Globalstars `9`.
Retrieve all pages using the WordPress pagination headers
(`X-WP-Total`, `X-WP-TotalPages`); if unavailable, establish coverage from the
official listing instead of assuming the first response is complete.

Useful fields include `id`, `slug`, `link`, `title.rendered`, `content.rendered`,
and `programmes-type`. The API includes program descriptions and events as well
as calls. `date` is publication time and `status=publish` means published
content; neither establishes application dates or open status.

Read the official call detail for application dates and participating countries.
No separate structured deadline/country fields were confirmed in the research.
Do not treat a Korea mention in generic text or a newsletter selector as proof
of eligibility. Korea's inclusion in the call's participating-country list is
evidence of international participation, not confirmation of Korean funding.
Check the corresponding KIAT notice as well.

This is an observed public content API, not a confirmed dedicated funding API
with guaranteed stability or complete cluster coverage.

## 3. Second pass: existing official-source research

Perform this pass even when API discovery succeeds, for sources and details the
APIs do not cover. Use it immediately if a request fails, pagination is incomplete,
response fields cannot be interpreted, or a known call is absent.

| Scope | Second-pass sources |
| :--- | :--- |
| Horizon Europe | Portal call/topic pages, Work Programme PDFs, administering-agency guidance; existing bulk-dataset checks for page audits |
| Eureka / Eurostars / Globalstars / Network Projects | [Official calls](https://www.eurekanetwork.org/programmes-and-calls/), call details, KIAT and K-PASS notices |
| Cluster calls | Official CELTIC-NEXT, EUROGIA, ITEA, SMART, and Xecs sites, plus Korean funding notices |
| Bilateral calls | Official partner-country agencies, KIAT and K-PASS notices |

Use browser access when non-browser requests are blocked. Search engines and
aggregators may identify candidates, but official sources must support published
claims. Log the failing source, time, missing scope, and fallback sources used;
an API failure or empty result is not proof that no calls exist. Keep successful
results from other sources while marking unresolved coverage explicitly.

## 4. Deduplicate and verify eligibility

Use EU topic IDs and parent call IDs, or Eureka IDs (`eureka:<id>`), for source
identity. Match cross-source duplicates by official call identifier and detail
URL. Group EU topics under the correct official call; do not merge separate
rounds or discard `-two-stage` suffixes. Update an existing page when dates or
conditions change instead of treating the unchanged ID as already processed.

Before including a candidate in the default verified results, establish:

- Companies can apply as beneficiaries, rather than only researchers or public bodies.
- A Korean entity can participate **and receive funding**.
- A European entity does not need to be established.
- Country, ownership/control, security, and topic-specific rules do not exclude it.
- Consortium requirements, submission channels, and current dates are known.

Korea's Horizon association must be checked against the applicable Pillar II
scope and call conditions; do not extend it to every Horizon program. Exclude
EIC Accelerator from the default Korean-entity results when European
establishment is required. For Eureka-family programs, distinguish international
participation from national funding approval and verify the Korean procedure.

Consult the current [Korea cooperation guidance](https://research-and-innovation.ec.europa.eu/strategy/strategy-research-and-innovation/europe-world/international-cooperation/association-horizon-europe/korea_en),
[participating-country list](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/list-3rd-country-participation_horizon-euratom_en.pdf),
and applicable General Annexes and topic conditions during each eligibility review.
Uncertain candidates stay pending; do not infer a positive result from API status.

## 5. Record evidence and hand off

In research notes and the relevant verification log, record source/API URL,
topic/call/source ID, collection time, status, opening date, deadline and timezone,
program/action type, and the official eligibility evidence consulted. Separately
record Korean participation, funding eligibility, local-entity requirements,
consortium rules, verification date, unresolved conditions, and collection gaps.
These are evidence requirements, not new Hugo front-matter fields.

Use [page-and-verification.md](page-and-verification.md) for the existing artifact
schema and [horizon-topics.md](horizon-topics.md) for topic-level content. Only
update `verified` after the claimed facts have actually been checked. API-first
discovery does not replace detailed source verification or the existing validators.

## Provenance and limits

Promoted from API research dated 2026-10-06: EU multipart search and Eureka
WordPress responses were reported as successful in small requests. This procedure
does not claim a newly tested collector, live automation, exhaustive coverage, or
automatic eligibility decisions. Reconfirm API contracts and current conditions
when executing a collection run.
