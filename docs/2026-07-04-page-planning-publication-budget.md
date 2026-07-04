# TDD: Page Planning Publication Budget

## Context & Problem

The current projection path can turn many extraction artifacts into public pages.
This creates weak topic pages, malformed titles, and section reference floods.
Page planning must decide public wiki shape before any article exists.

Glossary:

- `PageCandidate`: one possible public wiki page.
- `PublicationBudget`: limits for public pages from one source.
- `PagePlan`: the accepted public page plan for one source.
- `RejectedPageCandidate`: a candidate that will not become a public page.
- `PageTitleFinding`: one title quality issue.
- `EvidenceRecordSet`: all typed evidence records for one source.

## Goals

- Plan public pages from accepted typed evidence records.
- Limit public page count with a source-level publication budget.
- Reject malformed page titles before article writing.
- Keep section reference material out of public pages by default.
- Improve wiki walkability with fewer, stronger pages.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not write article prose.
- This design does not build evidence packs.
- This design does not implement diagnostic questions.
- This design does not preserve old page ids.

Forbidden approaches:

- Do not create one public page per source section by default.
- Do not create public pages from fragmentary evidence records.
- Do not let a weak title pass because evidence exists.
- Do not add a compatibility mode for old page plans.

## Requirements

- The page planner reads accepted typed evidence records.
- The page planner creates page candidates before page plans.
- The title linter validates every page candidate.
- The publication budget sets page count limits by source profile.
- The page planner records rejected page candidates.
- The page planner records why each candidate was accepted or rejected.
- The source manifest reads the accepted page plan.
- Section reference pages require explicit page plan acceptance.

## Invariants

- Public wiki pages come from accepted page plans.
- Raw sources stay immutable.
- Generated wiki data remains disposable.
- `WikiStructure` renders page paths.
- `PageMetadata` remains the page identity authority.

## Proposed Architecture

```text
EvidenceRecordSet
        |
        v
PageCandidateBuilder
        |
        v
PageTitleLinter
        |
        v
PublicationBudget
        |
        v
PagePlan
        |
        +--> RejectedPageCandidate
```

`EvidenceRecordSet` stores accepted evidence records.
`PageCandidateBuilder` proposes public pages.
`PageTitleLinter` rejects malformed titles.
`PublicationBudget` limits public page count.
`PagePlan` stores accepted public pages.
`RejectedPageCandidate` stores rejected candidates and reasons.

## Key Interactions

Build candidates:

```text
page planner -> evidence record set: read accepted records
candidate builder -> page candidate: group records
title linter -> page candidate: validate title
candidate builder -> rejected candidate: record weak candidates
```

Apply budget:

```text
page planner -> publication budget: read limits
page planner -> page candidate: rank candidates
page planner -> page plan: accept candidates within budget
page planner -> rejected candidate: record over-budget candidates
```

Build source manifest:

```text
source manifest builder -> page plan: read accepted pages
source manifest builder -> rejected candidates: read counts
source manifest builder -> wiki page: render navigation
```

## Data Model

`PageCandidate` stores candidate id, source id, title, page kind, page family,
supporting evidence record ids, rank score, and title findings.

`PublicationBudget` stores source profile id, max public pages, max pages per
family, and minimum support counts.

`RejectedPageCandidate` stores candidate id, source id, title, rejection code,
supporting evidence record ids, and message.

`PagePlan` stores source id, accepted page metadata, source profile id,
publication budget id, and rejected page candidates.

## APIs / Interfaces

The article compiler accepts only pages from `PagePlan`.

The source manifest builder reads `PagePlan`.

The page planner writes `RejectedPageCandidate` records for all rejected
candidates.

## Behavior & Domain Rules

The title linter rejects weak titles.
Example: `Alway`, `Bonuse`, `Needn`, and `Double Sixe` fail title lint.

The page planner accepts supported topics.
Example: `Shade` can become a topic page when accepted evidence supports a full
article.

The page planner rejects section floods.
Example: a source with 700 sections does not create 700 public section pages.

The publication budget preserves walkability.
Example: a source profile can cap broad topic pages while allowing procedures.

## Acceptance Criteria

- A unit test rejects malformed candidate titles.
- A unit test rejects a page candidate with only fragmentary evidence.
- A unit test applies a publication budget to over-budget candidates.
- A unit test records rejection reasons for every rejected candidate.
- A Sword World fixture creates a bounded page plan below the budget.
- A Sword World fixture does not create public pages for every section.
- A JavaScript Allonge fixture accepts recipe and concept candidates.
- The source manifest fixture lists accepted pages from the page plan.
- A walkability report records public page count and rejected candidate count.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

The page plan is harness state.
It does not make claims about source truth.

The ingest log records page counts by page family and budget rejection count.

## Reference Implementations

- Page metadata: `harness/src/llmwiki/domain/pages.py`
- Projection policy: `harness/src/llmwiki/domain/ledger/projection_policy.py`
- Source manifest navigation: `harness/src/llmwiki/domain/ledger/source_manifest_navigation.py`

## Alternatives Considered

- Let article generation decide page count: rejected because page shape must be
  planned before model prose exists.
- Keep section pages as public coverage: rejected because coverage is not
  walkability.
- Use title cleanup after rendering: rejected because weak titles must not reach
  article writing.

## Halt Conditions

- Stop if implementation must preserve old page ids.
- Stop if a public page writer needs a rejected page candidate.
