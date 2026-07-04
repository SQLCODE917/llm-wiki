# TDD: Evidence Pack Contract

## Context & Problem

Page drafting currently risks using summaries and clipped statements as factual
input.
A planned page needs a non-lossy support bundle before article writing starts.
The support bundle must show exactly what evidence an article can cite.

Glossary:

- `EvidencePack`: the selected source support for one planned page.
- `EvidencePackItem`: one selected support item in an evidence pack.
- `EvidencePackCoverage`: the relationship between page purpose and support.
- `SupportRef`: a stable reference to selected support.
- `EvidenceRecordSet`: all typed evidence records for one source.
- `NormalizedSourceMap`: the durable source model for one `RawSource`.

## Goals

- Build one `EvidencePack` for each accepted planned page.
- Include full source text or full structured payload text.
- Exclude summaries from factual draft input.
- Make support references validatable before article writing.
- Improve article authority with explicit source-backed support.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not write article prose.
- This design does not generate navigation summaries.
- This design does not repair missing evidence.
- This design does not keep old `DraftEvidenceCard.summary` behavior.

Forbidden approaches:

- Do not put renderable summaries in evidence pack items.
- Do not build evidence packs from rejected page candidates.
- Do not cite evidence outside the evidence pack.
- Do not publish fallback pages when evidence pack construction fails.

## Requirements

- The evidence pack builder reads one accepted page plan item.
- The evidence pack builder reads accepted typed evidence records.
- Each evidence pack item has one support ref.
- Each evidence pack item stores full source text or full payload text.
- Each evidence pack item stores source anchors.
- Each evidence pack records coverage for page purpose.
- The evidence pack validator rejects missing support text.
- The article writer receives the evidence pack, not summaries.

## Invariants

- `NormalizedSourceMap` remains the source text authority.
- `EvidenceRecordSet` remains the factual evidence authority.
- Public article claims cite evidence pack items.
- Navigation summaries are not factual evidence.
- Raw sources stay immutable.

## Proposed Architecture

```text
PagePlan
   |
   v
EvidencePackBuilder
   |
   +--> EvidenceRecordSet
   |
   +--> NormalizedSourceMap
   |
   v
EvidencePack
   |
   v
ArticleWriter
```

`PagePlan` selects the public page target.
`EvidencePackBuilder` selects evidence for one page.
`EvidenceRecordSet` provides accepted typed evidence records.
`NormalizedSourceMap` provides full source text.
`EvidencePack` stores selected support.
`ArticleWriter` uses only the evidence pack for factual claims.

## Key Interactions

Build evidence pack:

```text
pack builder -> page plan: read page target
pack builder -> evidence records: read accepted records
pack builder -> source map: read source text
pack builder -> evidence pack: write items
```

Validate support refs:

```text
article writer -> evidence pack: cite support refs
validator -> evidence pack: verify support refs
validator -> finding: reject unknown support ref
```

Reject missing evidence:

```text
pack builder -> evidence records: no accepted records
pack builder -> finding: record missing evidence
pack builder -> article compiler: omit page
```

## Data Model

`EvidencePack` stores page id, source id, evidence pack items, coverage records,
and findings.

`EvidencePackItem` stores support ref, evidence record id, source anchors,
source text, payload text, citation label, and section path.

`EvidencePackCoverage` stores page id, page purpose, support ref, coverage kind,
and coverage status.

`SupportRef` stores support kind and stable support id.

## APIs / Interfaces

The article writer receives one `EvidencePack`.

The article validator accepts only support refs from the evidence pack.

The renderer receives article claims that cite support refs.

## Behavior & Domain Rules

The pack builder includes full source text.
Example: a Shade pack item includes the full source block that describes the
darkness rule.

The pack builder includes full payload text.
Example: a spell pack item includes `Distance=20 meters`.

The pack validator rejects summary-only support.
Example: `Shade creates darkness` alone is not valid support text.

The compiler rejects pages without evidence.
Example: a planned topic with no accepted evidence pack does not publish.

## Acceptance Criteria

- A unit test builds an evidence pack for an accepted planned page.
- A unit test rejects an evidence pack item without source text or payload text.
- A unit test proves no evidence pack JSON contains a `summary` field.
- A unit test rejects article support refs outside the evidence pack.
- A Sword World Shade fixture includes full Shade support text.
- A JavaScript Allonge fixture includes full code example support text.
- A fixture renders payload text in diagnostic output.
- A page with no evidence pack is omitted from staged publication.
- A coverage report records support refs for each planned article section.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

Evidence pack artifacts can contain source text.
The artifact writer stores them in the ingest cache, not as public wiki pages.

The ingest log records missing evidence pack counts.

## Reference Implementations

- Page synthesis: `harness/src/llmwiki/domain/ledger/page_synthesis.py`
- Evidence blocks: `harness/src/llmwiki/domain/ledger/evidence_blocks.py`
- Summary boundary TDD: `docs/2026-07-03-summary-boundary-refactor.md`

## Alternatives Considered

- Pass evidence records directly to the article writer: rejected because the
  page needs a selected support set.
- Use navigation summaries as compact evidence: rejected because summaries are
  lossy.
- Publish extractive support when drafting fails: rejected because failed
  article writing must not publish public prose.

## Halt Conditions

- Stop if a model prompt requires summary text as factual support.
- Stop if a planned page cannot build at least one evidence pack item.
