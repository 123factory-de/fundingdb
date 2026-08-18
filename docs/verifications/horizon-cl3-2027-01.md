---
program: "horizon-cl3-2027-01"
last_verified: "2026-08-18"
---

# Verification log — Horizon Europe 2027 · 시민안전

One dated section per verification pass, newest first. Key claims on the program
page (front matter, bold statements, and table rows) are mapped to the sources
that support them, so the page can be re-checked claim by claim.

## Sources

| # | Source | Access note |
| :-- | :--- | :--- |
| [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | 공고 페이지 (Funding & Tenders Portal) | Official call page on the EU Funding & Tenders portal |
| [S2](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe/cluster-3-civil-security-society_en) | 공식 사이트 (Cluster 3) | — |
| [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf) | Work Programme 2026–2027 (Part 6 · Civil Security) | Work Programme PDF — search the call ID inside the document |
| [S4](https://k-erc.eu) | 한-EU 연구협력센터 (KERC) | — |

## 2026-08-18 — topic-level action types and funding rates

Every topic was checked against the portal topic-details data for its identifier, official title, action type, and budget. The Korean translation is recorded alongside the official portal title below for direct review. The applicable maximum funding rate was checked against General Annex G; topic-specific COFUND rates were checked against each topic's official conditions.

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 17 topic IDs, official titles, action types, funding rates, and budgets | [Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home) / [General Annex G](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-15-general-annexes_horizon-2026-2027_en.pdf) | Match — RIA 5, IA 10, CSA 1, PCP 1; total €129.5M |

### Topic title translations

| Topic ID | Official portal title | Korean translation |
| :--- | :--- | :--- |
| BM-01 | Open topic on research and innovation for effective management of EU external borders that promotes fundamental rights and EU values | 기본권과 EU 가치를 증진하는 EU 외부국경의 효과적 관리를 위한 R&I 오픈 토픽 |
| BM-02 | Trusted, secure, quality future digital travel credentials | 신뢰할 수 있고 안전한 고품질 미래 디지털 여행증명 |
| BM-03 | Detection and characterisation of threats or illegal/ smuggled goods in cargo | 화물 내 위협 또는 불법·밀수품 탐지와 특성 분석 |
| DRS-01 | Open Topic on advanced protective gear optimized for CBRN-E (Chemical, Biological, Radiological, Nuclear, Explosives) environments and new generation of smart protective equipment for disaster responders | CBRN-E(화학·생물·방사능·핵·폭발물) 환경에 최적화된 첨단 보호장비와 재난대응자용 차세대 스마트 보호장비 오픈 토픽 |
| DRS-02 | Societal resilience, engagement of the younger generations and digital innovation for disaster resilience | 사회 회복력·청년세대 참여·재난 회복력 디지털 혁신 |
| DRS-03 | Enhancing decision support system for disaster crises: leveraging emerging technologies for improved civil preparedness and crisis management | 신기술을 활용한 재난위기 의사결정 지원시스템과 시민 대비·위기관리 강화 |
| DRS-04 | Enhancing preparedness for large-scale cross-border disasters | 대규모 초국경 재난 대비 강화 |
| FCT-01 | Online harms detection and investigation tools using a short development cycle model | 단기 개발주기 모델을 활용한 온라인 위해 탐지·수사 도구 |
| FCT-02 | Community policing in diverse societies in Europe | 유럽의 다양성 사회를 위한 지역사회 경찰활동 |
| FCT-03 | Open topic on enhanced prevention, detection and deterrence of societal issues related to various forms of crime | 다양한 범죄 관련 사회문제의 예방·탐지·억제 강화 오픈 토픽 |
| FCT-04 | Open topic on increasing security of citizens against terrorism, including in public spaces | 공공장소를 포함한 테러로부터 시민 안전 강화 오픈 토픽 |
| FCT-05 | Effective and evidence-based responses to the increased availability and use of synthetic drugs and stimulants in Europe | 유럽 내 합성마약·각성제 접근성과 사용 증가에 대한 효과적·근거기반 대응 |
| INFRA-01 | Enhancing physical protection of critical infrastructures | 핵심 인프라의 물리적 보호 강화 |
| INFRA-02 | Impact of malicious use of Open-Source Intelligence on critical infrastructure business continuity | 공개출처정보(OSINT)의 악의적 이용이 핵심 인프라 사업연속성에 미치는 영향 |
| SSRI-01 | Accelerating uptake through open proposals for advanced SME innovation | 첨단 중소기업 혁신 오픈 제안을 통한 도입 가속 |
| SSRI-02 | Open grounds for future pre-commercial procurement of innovative security technologies | 미래 혁신 보안기술 상용화 전 조달을 위한 개방형 기반 |
| SSRI-03 | Demand-led innovation in security | 수요 주도 보안 혁신 |

## 2026-08-18 — topic-level eligibility check

Every topic of the call was checked against the portal topic-details data (`docs/skills/crosscheck-horizon/check_eligibility.py`) for (a) country restrictions, (b) the General Annexes Part 15 "restrictions on control in Innovation Actions in critical technology areas" (China-controlled entities), and (c) topic-specific additional eligibility criteria. The generic "일부 토픽 제한" bullet in 지원자격 was replaced by the specific, conclusion-first result.

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 중국 지배 법인 제한 DRS-03 | [HORIZON-CL3-2027-01-DRS-03](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-drs-03) | Match — "directly or indirectly controlled by China ... not eligible" (Art. 22(5), IA in critical technology areas per General Annexes Part 15) |
| 중국 지배 법인 제한 DRS-04 | [HORIZON-CL3-2027-01-DRS-04](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-drs-04) | Match — "directly or indirectly controlled by China ... not eligible" (Art. 22(5), IA in critical technology areas per General Annexes Part 15) |
| 중국 지배 법인 제한 FCT-01 | [HORIZON-CL3-2027-01-FCT-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-fct-01) | Match — "directly or indirectly controlled by China ... not eligible" (Art. 22(5), IA in critical technology areas per General Annexes Part 15) |
| 중국 지배 법인 제한 FCT-02 | [HORIZON-CL3-2027-01-FCT-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-fct-02) | Match — "directly or indirectly controlled by China ... not eligible" (Art. 22(5), IA in critical technology areas per General Annexes Part 15) |
| 중국 지배 법인 제한 FCT-04 | [HORIZON-CL3-2027-01-FCT-04](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-fct-04) | Match — "directly or indirectly controlled by China ... not eligible" (Art. 22(5), IA in critical technology areas per General Annexes Part 15) |
| 중국 지배 법인 제한 INFRA-01 | [HORIZON-CL3-2027-01-INFRA-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-infra-01) | Match — "directly or indirectly controlled by China ... not eligible" (Art. 22(5), IA in critical technology areas per General Annexes Part 15) |
| 중국 지배 법인 제한 INFRA-02 | [HORIZON-CL3-2027-01-INFRA-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-infra-02) | Match — "directly or indirectly controlled by China ... not eligible" (Art. 22(5), IA in critical technology areas per General Annexes Part 15) |
| 중국 지배 법인 제한 SSRI-01 | [HORIZON-CL3-2027-01-SSRI-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-ssri-01) | Match — "directly or indirectly controlled by China ... not eligible" (Art. 22(5), IA in critical technology areas per General Annexes Part 15) |
| 추가 자격요건 BM-01 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-BM-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-bm-01) | Match — "2 Border" |
| 추가 자격요건 BM-02 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-BM-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-bm-02) | Match — "2 Border or Coast Guard Authorities from at least 2 different EU Member States" |
| 추가 자격요건 BM-03 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-BM-03](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-bm-03) | Match — "2 Customs Authorities from at least 2 different EU Member States or Associated" |
| 추가 자격요건 DRS-01 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-DRS-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-drs-01) | Match — "2 Training Centres located in EU Member States or Associated Countries; 2 practitioners involved in training" |
| 추가 자격요건 DRS-02 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-DRS-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-drs-02) | Match — "2 Civil Society Organisation" |
| 추가 자격요건 DRS-03 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-DRS-03](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-drs-03) | Match — "2 authorities in charge of disaster risk or crisis communication and 2 representati" |
| 추가 자격요건 DRS-04 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-DRS-04](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-drs-04) | Match — "3 authorities in charge of disaster risk or crisis communication" |
| 추가 자격요건 FCT-02 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-FCT-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-fct-02) | Match — "3 Police Authorities and at least 2 Civil Society Organisations" |
| 추가 자격요건 FCT-03 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-FCT-03](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-fct-03) | Match — "2 Police Authorities and at least 2 Civil Society Organisations" |
| 추가 자격요건 FCT-05 — 실수요기관(practitioner) 필수 참여 | [HORIZON-CL3-2027-01-FCT-05](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl3-2027-01-fct-05) | Match — "3 Police Authorities and at least 2 Civil Society Organisations" |


## 2026-08-12 — claim-by-claim check

### Front matter

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| `status: planned` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |
| `deadline: 2027-11-04` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |
| `amount: 콜 총 €129.5M · 과제당 통상 100만~1,000만 유로` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf) | Match |
| `target: 기업·대학·연구소` | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |
| `duration: 통상 3~4년` | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |
| `org_eu: EU 집행위원회` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |
| `org_kr: 한국연구재단(NRF) · KERC` | [S4](https://k-erc.eu) | Match |
| `apply_via: EU Funding & Tenders Portal` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |

### 개요

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| Cluster 3(시민안전) | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf) | Match |
| 2027년 5월 5일 개시, 마감은 2027년 11월 4일 17:00(브뤼셀) | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf) | Match |

### 지원자격 · 지원율 (Pillar 2 공통)

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 주관기관(코디네이터) | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |
| 3개 이상 법인 | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |
| 100% | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |
| 70% | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |
| 25% 정률 | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-6-civil-security-for-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL3-2027-01&isExactMatch=true) | Match |

### Summary

- All claims match the sources listed above as of 2026-08-12; no corrections needed.
- Status and deadline were additionally machine-checked against the portal bulk dataset (grantsTenders.json, 2026-08-11) via `docs/skills/crosscheck-horizon/` — match.
