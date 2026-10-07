---
name: add-funding-program
description: Add or audit funding opportunity pages and matching verification logs in the fundingdb repository. Use when creating a new Horizon Europe, Eureka-family, or bilateral program; importing or translating official call data; adding Horizon topic tables, action types, funding rates, budgets, eligibility conditions, or source links; renaming a program to its official identifier; or preparing funding content for publication.
---

# Add a funding program

Follow the repository `AGENTS.md` and preserve unrelated worktree changes. Never edit generated output (`public/`, `resources/`) or protected paths.

## 1. Collect candidates: API first, official pages second

Read [references/collection-method.md](references/collection-method.md) before collecting or refreshing funding opportunities. This is the default collection method, including when the request does not specify a source.

1. Query the EU Funding & Tenders search API and Eureka's official WordPress API first, as applicable. Collect all result pages and record coverage, failures, and collection time.
2. Use the existing official-page, notice, PDF, and browser research method to fill API coverage gaps, recover from failures, and collect sources without a confirmed API (including cluster and bilateral calls).
3. Deduplicate by official topic/call identity, then verify detailed conditions. An API candidate is not an eligibility approval or an instruction to publish.

Use this procedure independently of any notification workflow. Broad notification feeds must not determine which programs qualify for this database.

## 2. Establish the official identity

1. Find the primary official call page or notice before writing.
2. Record the exact call identifier, status, opening date, deadline including timezone, budget, applicant type, submission channel, and eligibility constraints.
3. For Horizon calls, use the lowercase official call identifier as the filename and preserve suffixes such as `-two-stage`:
   - `HORIZON-CL6-2026-03-two-stage` → `horizon-cl6-2026-03-two-stage.md`
4. Give the verification log the identical basename and set its `program` field to that basename.
5. For non-Horizon calls without a formal identifier, choose a stable lowercase hyphenated slug based on the official program and call name.

Do not invent sequential filenames or omit parts of an official identifier. When renaming an existing page, update every live internal link and verification reference. Add a legacy alias only when the requester wants URL compatibility.

## 3. Use authoritative sources

Prefer sources in this order:

1. Official call page, government notice, or Funding & Tenders Portal record
2. Official work programme or call PDF
3. Official administering-agency guidance
4. Confirmed Korean support organization

Use the Portal for current Horizon call conditions, topic identifiers, action types, budgets, and deadlines. Use the Work Programme PDF for detailed scope, expected outcomes, and topic-specific conditions. Do not present an unofficial aggregator as an official source.

Read [references/page-and-verification.md](references/page-and-verification.md) before creating the page and its verification log. For Horizon calls, also read [references/horizon-topics.md](references/horizon-topics.md).

## 4. Create both synchronized artifacts

Create or update:

- `content/programs/<slug>.md`
- `docs/verifications/<slug>.md`

Keep claims, links, dates, identifiers, topic rows, and Korean translations synchronized. Write Korean reader-facing content; keep documentation, worklogs, and verification notes in concise English unless the existing artifact requires Korean labels.

For every material claim, record the official supporting source in the verification log. Preserve exact official English topic titles beside their Korean translations so reviewers can audit translation choices.

## 5. Apply Horizon-specific rules

Use exactly one `## 토픽` section and one detailed topic table:

```markdown
| 토픽 ID | 주제 | Action Type | EU 지원율 | 예산(€M) |
| :--- | :--- | :---: | :--- | ---: |
```

Do not retain a second summary table that overlaps the detailed rows. After the table, link the official Portal call page and the relevant Work Programme PDF. If no separate work-programme PDF exists for the call, link only the Portal and state that clearly.

Translate meaning rather than mechanically transliterating terminology. Preserve necessary acronyms and explain them on first use. Distinguish related terms such as `foodome` (식품 성분체) and `foodomics` (푸도믹스). Keep the official source string unchanged in verification.

State eligibility conclusions for Korean applicants first. Name restricted topic IDs, ownership/control tests, mandatory practitioner partners, multi-actor requirements, geographic mandates, consortium caps, or predecessor-project restrictions instead of writing only “some topics are restricted.”

## 6. Validate before handoff

Run the repository validator for the changed page, or without arguments for all programs:

```bash
python3 docs/skills/add-funding-program/scripts/validate_program.py \
  content/programs/<slug>.md
```

For Horizon data, also run the existing portal checks when network access or a current dump is available:

```bash
python3 docs/skills/crosscheck-horizon/check_horizon.py
python3 docs/skills/crosscheck-horizon/check_eligibility.py
```

Then run:

```bash
git diff --check
hugo --gc --minify --destination /tmp/fundingdb-build
gitleaks dir --config .gitleaks.toml --no-banner
```

Confirm that no protected, generated, or unrelated files changed. Update the current branch worklog with the request, changes, and verification performed. Follow the user's explicit instructions about committing or opening a pull request.
