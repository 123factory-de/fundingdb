---
program: "horizon-hlth-2027-01"
last_verified: "2026-08-18"
---

# Verification log — Horizon Europe 2027 · 보건

One dated section per verification pass, newest first. Key claims on the program
page (front matter, bold statements, and table rows) are mapped to the sources
that support them, so the page can be re-checked claim by claim.

## 2026-10-06 — schedule refresh

Checked the official [Portal bulk dataset](https://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json), current topic JSON actions, and [Health Work Programme](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) call overview. Updated opening/deadline dates in front matter and body together.

Opening: 2026-10-29; deadline: 2027-02-17, 17:00 Brussels local time.

This is a targeted date/wording check; prior full-verification dates are retained. Other claims were not re-certified by this update.

## Sources

| # | Source | Access note |
| :-- | :--- | :--- |
| [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | 공고 페이지 (Funding & Tenders Portal) | Official call page on the EU Funding & Tenders portal |
| [S2](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe/cluster-1-health_en) | 공식 사이트 (Cluster 1 Health) | — |
| [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) | Work Programme 2026–2027 (Part 4 · Health) | Work Programme PDF — search the call ID inside the document |
| [S4](https://k-erc.eu) | 한-EU 연구협력센터 (KERC) | — |

## 2026-08-18 — topic-level action types and funding rates

Every topic was checked against the portal topic-details data for its identifier, official title, action type, and budget. The Korean translation is recorded alongside the official portal title below for direct review. The applicable maximum funding rate was checked against General Annex G; topic-specific COFUND rates were checked against each topic's official conditions.

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 10 topic IDs, official titles, action types, funding rates, and budgets | [Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home) / [General Annex G](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-15-general-annexes_horizon-2026-2027_en.pdf) | Match — RIA 9, PCP 1; total €341.6M |

### Topic title translations

| Topic ID | Official portal title | Korean translation |
| :--- | :--- | :--- |
| CARE-02 | Personalised approaches to reduce risks from Adverse Drug Reactions due to administration of multiple medications | 다중약물 투여에 따른 약물이상반응 위험을 줄이는 맞춤형 접근법 |
| DISEASE-05 | Development of novel small molecule antiviral therapeutics for pathogens with epidemic potential | 유행 가능성이 있는 병원체용 신규 저분자 항바이러스 치료제 개발 |
| DISEASE-06 | Development of monoclonal antibodies to prevent and treat infections from Flaviviruses | 플라비바이러스 감염 예방·치료용 단일클론항체 개발 |
| DISEASE-07 | Development of monoclonal antibodies to prevent and treat infections from Filo-, Nairo-, Phenui-, Picorna- and Toga viruses | 필로·나이로·페누이·피코르나·토가바이러스 감염 예방·치료용 단일클론항체 개발 |
| DISEASE-08 | Development of innovative antimicrobials against pathogens resistant to antimicrobials | 항균제 내성 병원체 대상 혁신 항균제 개발 |
| DISEASE-10 | Prevention and management of chronic non-communicable diseases in children and young people (GACD) | 아동·청년 만성 비감염성질환 예방·관리 |
| ENVHLTH-02 | Integrating climate-related exposures into the human exposome and characterising its changes in response to climate change | 기후 관련 노출을 인간 엑스포좀에 통합하고 기후변화에 따른 변화 특성 규명 |
| ENVHLTH-MISSCLIMA-03 | Tools and technologies to support health adaptation to climate change | 기후변화 건강 적응 지원 도구·기술 |
| IND-01 | Development of cell-free protein synthesis platforms for discovery and/or production of biologicals | 바이오의약품 발굴·생산용 무세포 단백질 합성 플랫폼 개발 |
| STAYHLTH-01 | Addressing disabilities through the life course to support independent living and inclusion | 자립생활과 포용을 지원하는 생애주기 장애 대응 |

## 2026-08-18 — topic-level eligibility check

Every topic of the call was checked against the portal topic-details data (`docs/skills/crosscheck-horizon/check_eligibility.py`) for (a) country restrictions, (b) the General Annexes Part 15 "restrictions on control in Innovation Actions in critical technology areas" (China-controlled entities), and (c) topic-specific additional eligibility criteria. The generic "일부 토픽 제한" bullet in 지원자격 was replaced by the specific, conclusion-first result.

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 참여국 제한 토픽 없음 (10개 토픽) | 포털 토픽별 "Conditions" | Match — no country or control clause in any topic |


## 2026-08-12 — claim-by-claim check

### Front matter

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| `status: planned` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |
| `deadline: 2027-04-13` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |
| `amount: 콜 총 €341.6M · 과제당 통상 100만~1,000만 유로` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) | Match |
| `target: 기업·대학·연구소` | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |
| `duration: 통상 3~4년` | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |
| `org_eu: EU 집행위원회` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |
| `org_kr: 한국연구재단(NRF) · KERC` | [S4](https://k-erc.eu) | Match |
| `apply_via: EU Funding & Tenders Portal` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |

### 개요

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| Cluster 1(보건) | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) | Match |
| 2027년 2월 10일 개시, 마감은 2027년 4월 13일 17:00(브뤼셀) | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) | Match |

### 지원자격 · 지원율 (Pillar 2 공통)

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 주관기관(코디네이터) | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |
| 3개 이상 법인 | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |
| 100% | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |
| 70% | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |
| 25% 정률 | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-01&isExactMatch=true) | Match |

### Summary

- All claims match the sources listed above as of 2026-08-12; no corrections needed.
- Status and deadline were additionally machine-checked against the portal bulk dataset (grantsTenders.json, 2026-08-11) via `docs/skills/crosscheck-horizon/` — match.
