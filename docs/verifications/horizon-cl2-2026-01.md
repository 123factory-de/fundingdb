---
program: "horizon-cl2-2026-01"
last_verified: "2026-09-28"
---

# Verification log — Horizon Europe 2026 · 문화·창의·포용사회

One dated section per verification pass, newest first. Key claims on the program
page (front matter, bold statements, and table rows) are mapped to the sources
that support them, so the page can be re-checked claim by claim.

## Sources

| # | Source | Access note |
| :-- | :--- | :--- |
| [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | 공고 페이지 (Funding & Tenders Portal) | Official call page on the EU Funding & Tenders portal |
| [S2](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe/cluster-2-culture-creativity-and-inclusive-society_en) | 공식 사이트 (Cluster 2) | — |
| [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Work Programme 2026–2027 (Part 5 · Culture) | Work Programme PDF — search the call ID inside the document |
| [S4](https://k-erc.eu) | 한-EU 연구협력센터 (KERC) | — |

## 2026-08-18 — topic-level eligibility check

Every topic of the call was checked against the portal topic-details data (`docs/skills/crosscheck-horizon/check_eligibility.py`) for (a) country restrictions, (b) the General Annexes Part 15 "restrictions on control in Innovation Actions in critical technology areas" (China-controlled entities), and (c) topic-specific additional eligibility criteria. The generic "일부 토픽 제한" bullet in 지원자격 was replaced by the specific, conclusion-first result.

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 참여국 제한 토픽 없음 (26개 토픽) | 포털 토픽별 "Conditions" | Match — no country or control clause in any topic |

## 2026-08-18 — topic-level action types and funding rates

Every topic was checked against the portal topic-details data for its identifier, official title, action type, and budget. The Korean translation is recorded alongside the official portal title below for direct review. The applicable maximum funding rate was checked against General Annex G; topic-specific COFUND rates were checked against each topic's official conditions.

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 26 individual topic IDs, titles, action types, and budgets | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) / [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match — RIA 20, IA 3, CSA 3; total €298.5M |
| RIA and CSA 100%; IA 70% for-profit and 100% non-profit | [General Annex G](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-15-general-annexes_horizon-2026-2027_en.pdf) | Match |
| Lump-sum grant model and indirect costs calculated at 25% of qualifying direct costs | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) / [General Annex G](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-15-general-annexes_horizon-2026-2027_en.pdf) | Match |

### Topic title translations

| Topic ID | Official portal title | Korean translation |
| :--- | :--- | :--- |
| DEMOCRACY-01 | Tackling gender-based violence against politically active women and LGBTIQ people | 정치활동 여성·LGBTIQ 대상 젠더 기반 폭력 대응 |
| DEMOCRACY-02 | Understanding the forms of local democracy in low-income and low-middle income countries | 저소득·중저소득국의 지방 민주주의 형태 연구 |
| DEMOCRACY-03 | Government in transition – how governments change the way they work and prepare the civil service for the future | 정부 업무방식 전환과 미래 공무원 역량 |
| DEMOCRACY-04 | Sustainable paths to media viability | 지속가능한 미디어 산업 모델 |
| DEMOCRACY-05 | Research and Innovation Network for a Union of Equality | 평등 연합을 위한 연구혁신 네트워크 |
| DEMOCRACY-06 | Governing global commons sustainably | 글로벌 공유재의 지속가능한 거버넌스 |
| DEMOCRACY-07 | Supporting post-conflict democracy and reconstruction | 분쟁 후 민주주의와 재건 지원 |
| DEMOCRACY-08 | Electoral integrity in the digital context | 디지털 환경의 선거 공정성 |
| DEMOCRACY-09 | Citizenship education as part of lifelong learning | 평생학습으로서의 시민교육 |
| DEMOCRACY-10 | Digital and media literacy as drivers for democratic and civic resilience | 민주적 회복력을 위한 디지털·미디어 리터러시 |
| HERITAGE-01 | “Artistic intelligence” : harnessing the power of the arts to address complex challenges, enhance soft skills and boost innovation and competitiveness | "예술적 지능": 복합 난제 해결에 예술 활용 |
| HERITAGE-02 | Boosting creative startups for disruptive innovation | 크리에이티브 스타트업의 파괴적 혁신 육성 |
| HERITAGE-03 | AI integration in CCSI work practice: catalysing innovation and competitiveness | 문화창의산업 실무에의 AI 통합 |
| HERITAGE-04 | Towards a fair and transparent market for cultural and creative content in the era of generative AI | 생성형 AI 시대의 공정·투명한 문화콘텐츠 시장 |
| HERITAGE-05 | Creative alliances: Fostering global partnerships in cultural policies and CCI innovation | 문화정책·CCI 글로벌 파트너십 |
| HERITAGE-06 | Safeguarding linguistic diversity in Europe | 유럽 언어 다양성 보호 |
| HERITAGE-07 | Preventing and fighting illicit trafficking of cultural goods | 문화재 불법 거래 방지 |
| TRANSFO-02 | Open topic: Strengthen Europe's social model and sustainable competitiveness through productivity | 생산성을 통한 유럽 사회모델·경쟁력 강화 |
| TRANSFO-03 | Tackling child poverty and ensuring disadvantaged children's access to Early Childhood Education and Care | 아동빈곤 대응과 취약아동의 영유아 교육·돌봄 접근 |
| TRANSFO-04 | The impact of the use of digital tools outside school and for communication on educational outcomes and mental health | 교외 디지털 도구 사용이 교육·정신건강에 미치는 영향 |
| TRANSFO-05 | Contribution of basic skills to productivity, innovation, competitiveness and economic growth | 기초역량이 생산성·혁신·경제성장에 미치는 기여 |
| TRANSFO-06 | Making Europe a global magnet for talent - Attracting and retaining students, researchers and high-skilled workers from outside the EU | 비EU 학생·연구자·고급인재 유치와 유지 |
| TRANSFO-07 | Fostering competences for the green transition | 녹색전환 역량 육성 |
| TRANSFO-08 | Strengthened implementation of the EU Pact on Migration and Asylum and a focus on inclusion, integration, and health | EU 이주·망명 협약 이행과 포용·통합·보건 |
| TRANSFO-09 | Rethinking long-term care policy in the face of EU demographic shifts | 인구변화에 대응한 장기요양정책 재설계 |
| TRANSFO-10 | Fostering cooperation and integration between SSH and STEM research and innovation in the EU | EU 내 SSH·STEM 연구혁신 협력·통합 |

## 2026-08-12 — claim-by-claim check

### Front matter

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| `status: open` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |
| `deadline: 2026-09-23` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |
| `amount: 콜 총 €298.5M · 과제당 통상 100만~1,000만 유로` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| `target: 기업·대학·연구소` | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |
| `duration: 통상 3~4년` | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |
| `org_eu: EU 집행위원회` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |
| `org_kr: 한국연구재단(NRF) · KERC` | [S4](https://k-erc.eu) | Match |
| `apply_via: EU Funding & Tenders Portal` | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |

### 개요

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| Cluster 2(문화·창의·포용사회) | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| 마감은 2026년 9월 23일 17:00(브뤼셀) | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |

### 토픽 (HORIZON-CL2-2026-01-…)

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 토픽 ID — 주제 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| HERITAGE-02 — 크리에이티브 스타트업의 파괴적 혁신 육성 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| HERITAGE-03 — 문화창의산업 실무에의 AI 통합 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| HERITAGE-04 — 생성형 AI 시대의 공정·투명한 문화콘텐츠 시장 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| HERITAGE-01 — "예술적 지능": 복합 난제 해결에 예술 활용 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| HERITAGE-05 — 문화정책·CCI 글로벌 파트너십 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| HERITAGE-06 — 유럽 언어 다양성 보호 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| HERITAGE-07 — 문화재 불법 거래 방지 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| DEMOCRACY-04 — 지속가능한 미디어 산업 모델 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| DEMOCRACY-08 — 디지털 환경의 선거 공정성 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| DEMOCRACY-10 — 민주적 회복력을 위한 디지털·미디어 리터러시 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| DEMOCRACY-01~03, 05~07, 09 — 민주주의·거버넌스 관련 7개 토픽 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |
| TRANSFO-02~10 — 사회·경제 전환(생산성, 교육·돌봄, 인재 유치, 이주, 녹색 전환 역량 등) 9개 토픽 | [S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true)/[S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf) | Match |

### 지원자격 · 지원율 (Pillar 2 공통)

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| 주관기관(코디네이터) | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |
| 3개 이상 법인 | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |
| 100% | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |
| 70% | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |
| 25% 정률 | [S3](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-5-culture-creativity-and-inclusive-society_horizon-2026-2027_en.pdf)/[S1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=HORIZON-CL2-2026-01&isExactMatch=true) | Match |

### Summary

- All claims match the sources listed above as of 2026-08-12; no corrections needed.
- Status and deadline were additionally machine-checked against the portal bulk dataset (grantsTenders.json, 2026-08-11) via `docs/skills/crosscheck-horizon/` — match.


## 2026-09-28 — Portal status refresh

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| Status and deadline | [Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?callIdentifier=CL2-2026-01&isExactMatch=true) | Updated to match current official topic data |
