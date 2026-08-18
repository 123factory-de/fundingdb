# Program and verification structure

## Program page

Follow the schema already used in `content/programs/`. At minimum, keep these front-matter fields complete and source-backed:

```yaml
---
title: "Reader-facing Korean title"
subtitle: "OFFICIAL-CALL-ID · Program family"
weight: 100
tags: ["horizon"]
status: "open"
deadline: "YYYY-MM-DD"
amount: "Detailed funding summary"
amount_short: "Card summary"
target: "Eligible applicant summary"
target_short: "Card summary"
duration: "Expected project duration"
org_eu: "Administering organization"
org_kr: "Approved Korean support organization"
apply_via: "Official submission channel"
links:
  - name: "Official call page"
    url: "https://official.example/call"
verified: "YYYY-MM-DD"
---
```

Use the organization field names already established for the program family. Never publish personal contact data.

Recommended body order:

1. `## 개요` — what the call funds, current status, exact deadline, and why it matters to Korean applicants
2. `## 토픽` — Horizon calls only; use the required five-column table
3. `## 지원자격 · 지원율` — conclusions first, then consortium and topic-specific constraints
4. `## 신청방법 · 한국측 지원` — official submission path and approved public support channels

Keep the overview concise. Do not repeat the topic table as an earlier “major topics” table.

## Verification log

Create `docs/verifications/<slug>.md` with the same slug:

```markdown
---
program: "<slug>"
last_verified: "YYYY-MM-DD"
---

# Verification log — Program title

## Sources

| # | Source | Access note |
| :-- | :--- | :--- |
| [S1](https://official.example/call) | Official call page | What it proves |

## YYYY-MM-DD — claim-by-claim check

| Claim on the page | Source | Result |
| :--- | :--- | :--- |
| Deadline and status | [S1](https://official.example/call) | Match |
```

For Horizon topic translations, add:

```markdown
### Topic title translations

| Topic ID | Official portal title | Korean translation |
| :--- | :--- | :--- |
| TOPIC-01 | Exact official English title | 검토된 한국어 번역 |
```

Keep the official title exact. If a translation changes, update the program table and the Korean translation column together; do not alter the official-title column.

## Link consistency

- Internal program links use `/programs/<actual-slug>/`.
- A Markdown filename label and its target must match: `[call.md](call.md)`.
- Portal links must contain the page's exact `callIdentifier`.
- Source names must describe what the linked page actually is.
