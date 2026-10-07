---
program: "horizon-hlth-2027-03"
last_verified: "2026-08-18"
---

# Verification log — Horizon Europe 2027 · 보건 소규모

One dated section per verification pass, newest first. Key claims on the program
page (front matter, bold statements, and table rows) are mapped to the sources
that support them, so the page can be re-checked claim by claim.

## 2026-10-06 — targeted recheck

TOOL-08 title now reads “Towards the next generation of frontier Artificial Intelligence models for healthcare”; translated title updated. The portal public page is a JavaScript shell in this client; title confirmed against its official topic-data endpoint, not claimed as a browser rendering check.

Refreshed official English title references; historical translation tables are preserved. Whitespace normalized only.

| Topic ID | Official portal title | Korean translation |
| :--- | :--- | :--- |
| TOOL-02 | Advancing bio-printing of living cells for regenerative medicine | 재생의학용 생세포 바이오프린팅 고도화 |
| TOOL-04 | Virtual Human Twins (VHTs) for integrated clinical decision support in prevention and diagnosis | 예방·진단 통합 임상의사결정 지원용 가상 인간 트윈 |
| TOOL-08 | Towards the next generation of frontier Artificial Intelligence models for healthcare | 헬스케어를 위한 차세대 프런티어 인공지능 모델 |


Scope: targeted corrections only; historical full-verification dates are unchanged. See [_crosscheck-2026-10-06.md](_crosscheck-2026-10-06.md) for scope and limitations.

## 2026-10-06 — schedule refresh

Checked the official [Portal bulk dataset](https://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json), current topic JSON actions, and [Health Work Programme](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) call overview. Updated opening/deadline dates in front matter and body together.

Opening remains 2027-06-03; deadline: 2027-09-16, 17:00 Brussels local time.

This is a targeted date/wording check; prior full-verification dates are retained. Other claims were not re-certified by this update.

## Sources

| # | Source | Access note |
| :-- | :--- | :--- |
| [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | 공고 페이지 (Funding & Tenders Portal) | Official call page on the EU Funding & Tenders portal |
| [S2](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe/cluster-1-health_en) | 공식 사이트 (Cluster 1 Health) | — |
| [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) | Work Programme 2026–2027 (Part 4 · Health) | Work Programme PDF — search the call ID inside the document |
| [S4](https://k-erc.eu) | 한-EU 연구협력센터 (KERC) | — |

## 2026-08-18 — topic-level action types and funding rates

Every topic was checked against the portal topic-details data for its identifier, official title, action type, and budget. The Korean translation is recorded alongside the official portal title below for direct review. The applicable maximum funding rate was checked against General Annex G; topic-specific COFUND rates were checked against each topic's official conditions.

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 3 topic IDs, official titles, action types, funding rates, and budgets | [Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home) / [General Annex G](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-15-general-annexes_horizon-2026-2027_en.pdf) | Match — RIA 2, CSA 1; total €81.5M |

### Topic title translations

| Topic ID | Official portal title | Korean translation |
| :--- | :--- | :--- |
| TOOL-02 | Advancing bio-printing of living cells for regenerative medicine | 재생의학용 생세포 바이오프린팅 고도화 |
| TOOL-04 | Virtual Human Twins (VHTs) for integrated clinical decision support in prevention and diagnosis | 예방·진단 통합 임상의사결정 지원용 가상 인간 트윈 |
| TOOL-08 | Towards Artificial General Intelligence (AGI) for healthcare | 의료용 범용인공지능(AGI)을 향하여 |

## 2026-08-18 — topic-level eligibility check

Every topic of the call was checked against the portal topic-details data (`docs/skills/crosscheck-horizon/check_eligibility.py`) for (a) country restrictions, (b) the General Annexes Part 15 "restrictions on control in Innovation Actions in critical technology areas" (China-controlled entities), and (c) topic-specific additional eligibility criteria. The generic "일부 토픽 제한" bullet in 지원자격 was replaced by the specific, conclusion-first result.

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 참여국 제한 TOOL-08 — Member States and Associated Countries | [HORIZON-HLTH-2027-03-TOOL-08](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-hlth-2027-03-tool-08) | Match — Korea eligible |


## 2026-08-12 — claim-by-claim check

### Front matter

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| `status: planned` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |
| `deadline: 2027-09-22` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |
| `amount: 콜 총 €81.5M · 과제당 통상 100만~1,000만 유로` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) | Match |
| `target: 기업·대학·연구소` | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |
| `duration: 통상 3~4년` | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |
| `org_eu: EU 집행위원회` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |
| `org_kr: 한국연구재단(NRF) · KERC` | [S4](https://k-erc.eu) | Match |
| `apply_via: EU Funding & Tenders Portal` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |

### 개요

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| Cluster 1(보건) | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) | Match |
| 2027년 6월 3일 개시, 마감은 2027년 9월 22일 17:00(브뤼셀) | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf) | Match |

### 지원자격 · 지원율 (Pillar 2 공통)

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 주관기관(코디네이터) | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |
| 3개 이상 법인 | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |
| 100% | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |
| 70% | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |
| 25% 정률 | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-4-health_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-HLTH-2027-03&isExactMatch=true) | Match |

### Summary

- All claims match the sources listed above as of 2026-08-12; no corrections needed.
- Status and deadline were additionally machine-checked against the portal bulk dataset (grantsTenders.json, 2026-08-11) via `docs/skills/crosscheck-horizon/` — match.
