# Global Ingest Planning

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `ExtractedUnit` | Source-derived text unit with `RawSource`, locator, heading path, and status. |
| `CandidateClaim` | Source-derived statement before wiki write. |
| `CandidateTopic` | Source-derived topic label with supporting `CandidateClaim` records. |
| `CandidateEntity` | Source-derived entity label with supporting `CandidateClaim` records. |
| `TopicCluster` | Related `CandidateClaim` records across one `SourceBundle`. |
| `WikiMatch` | Retrieved existing page with score, reason, and excerpt. |
| `ClaimComparison` | Relationship between one `CandidateClaim` and one existing claim. |
| `PagePlan` | Run-owned plan for page targets and serial writes. |
| `PlannedPageWrite` | One write, enrich, or defer action chosen by `PagePlan`. |
| `RawSource` | Immutable source loaded from `raw/`. |
| `SourceBundle` | Non-empty set of `RawSource` records for one run. |
| `WikiPage` | One page with `PageMetadata` and `PageBody`. |
| `PageMetadata` | Page identity, summary, sources, and update date. |
| `PagePath` | Rendered location of one `WikiPage` inside `wiki/`. |
| `WikiStructure` | Domain object that renders `PagePath` from `PageMetadata`. |
| `Evidence` | Citation-backed support for a generated claim. |
| `IngestRun` | One ingest operation over one `SourceBundle`. |
| `IngestTopology` | Allowed write order for one `IngestRun`. |
| `GeneratedWikiState` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |

Our wiki writes PDF pages from chunk-local decisions. m5-wiki plans across the
whole extracted source before any page write. This TDD adopts that planning
boundary so page targets, evidence, and paths come from one `PagePlan`.

## Goals

- Create `ExtractedUnit` records before writes.
- Create `CandidateClaim` records from bounded source text.
- Match `CandidateClaim` records against existing `WikiPage` records.
- Create `TopicCluster` records across the `SourceBundle`.
- Create one `PagePlan` before writes.
- Make `PagePlan` produce `PageMetadata`.
- Make `WikiStructure` render every planned `PagePath`.
- Preserve serial writes after planning.
- Keep planning code portable to m5-wiki.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not add parallel ingest.
- This TDD does not add human review gates.
- This TDD does not replace the PDF extractor.
- This TDD does not add page body contracts.
- This TDD does not require an external vector service.

Forbidden approaches:

- Do not write `WikiPage` during extraction.
- Do not put the full PDF and full wiki into one model context.
- Do not infer `PageMetadata` from `PagePath`.
- Do not create a folder classifier.
- Do not create pages without `Evidence`.
- Do not let source page writes bypass `PagePlan`.

## Requirements

- `IngestRun` must create `ExtractedUnit` records before `WikiPage` writes.
- Each `ExtractedUnit` must retain `RawSource`, locator, heading path, text, status, and source hash.
- Each `CandidateClaim` must retain `Evidence`.
- Planning must use lexical features from `ExtractedUnit.text` and existing `WikiPage` text.
- Planning must use nearest-neighbor matching over existing page text.
- Planning must use clustering over extracted units or claim groups.
- `WikiMatch` must retain score, reason, and excerpt.
- `ClaimComparison` must record at least `overlap`.
- `PagePlan` must emit `PlannedPageWrite` records.
- Each `PlannedPageWrite` must have action `enrich-existing`, `create-new`, or `defer`.
- `PagePlan` must persist under the source cache.
- `PagePlan` must include an observation report.

## Invariants

- `raw/` remains immutable.
- `GeneratedWikiState` remains disposable.
- `IngestTopology` remains `serial`.
- `PageMetadata.page_id` remains identity.
- `PagePath` remains derived by `WikiStructure`.
- `Evidence` remains required for generated claims.
- `WikiStore` writes only after planning.

## Proposed Architecture

The ingest pipeline becomes extract, plan, then write. The plan stage uses
deterministic retrieval and clustering before it asks the model to write pages.

```
+--------------+     +---------------+     +------------------+
| SourceBundle |---->| ExtractedUnit |---->| CandidateClaim   |
+--------------+     +-------+-------+     +---------+--------+
                             |                       |
                             v                       v
+--------------+     +-------+-------+     +---------+--------+
| WikiPage text|---->| WikiMatch     |---->| PagePlan         |
+--------------+     +---------------+     +---------+--------+
                                                     |
                                                     v
                                            +--------+---------+
                                            | PlannedPageWrite |
                                            +------------------+
```

`SourceBundle` selects sources.
`ExtractedUnit` records source material.
`CandidateClaim` records source-derived statements before wiki writes.
`WikiMatch` narrows existing wiki context.
`PagePlan` owns planned writes.
`PlannedPageWrite` records execute serially.

## Key Interactions

### Planned PDF Ingest

```
RawSource -> ExtractedUnit records -> CandidateClaim records -> TopicCluster records
TopicCluster records + WikiMatch records -> PagePlan -> PlannedPageWrite records
```

### Existing Wiki Match

```
CandidateClaim records -> page text retrieval -> WikiMatch
WikiMatch -> PagePlan action
```

### Path Projection

```
TopicCluster -> PageMetadata -> WikiStructure -> PagePath
```

## Data Model

| Object | Required fields |
|---|---|
| `ExtractedUnit` | `unit_id`, `raw_source`, `locator`, `heading_path`, `text`, `extraction_status`, `source_hash` |
| `CandidateClaim` | `claim_id`, `statement`, `evidence`, `confidence` |
| `CandidateTopic` | `topic_id`, `label`, `candidate_claims` |
| `CandidateEntity` | `entity_id`, `label`, `candidate_claims` |
| `TopicCluster` | `cluster_id`, `label`, `extracted_units`, `candidate_claims`, `candidate_topics`, `candidate_entities` |
| `WikiMatch` | `page_id`, `score`, `match_reason`, `page_excerpt` |
| `ClaimComparison` | `candidate_claim`, `existing_claim`, `relation`, `page_id` |
| `PagePlan` | `plan_id`, `source_bundle`, `extracted_units`, `topic_clusters`, `wiki_matches`, `planned_writes` |
| `PlannedPageWrite` | `write_id`, `action`, `page_metadata`, `evidence`, `wiki_matches`, `claim_comparisons` |

## APIs / Interfaces

- `build_page_plan` creates `PagePlan` from source units, existing pages, and schema.
- `build_markdown_page_plan` creates `PagePlan` for one markdown source.
- `page_plan_to_json` serializes `PagePlan` to persisted JSON.
- `observation_report` renders `PagePlan` as markdown.
- `llmwiki ingest <source_locator>` writes no page before `PagePlan`.
- `WikiStructure` remains the only `PageMetadata` to `PagePath` interface.

## Behavior & Domain Rules

Rule: extraction precedes all writes.

Example: input `raw/javascriptallonge.pdf` -> expected `PagePlan` exists before `write_page`.

Rule: exact source-section identity beats semantic similarity.

Example: input heading `Self-Similarity` and existing page `javascriptallonge-self-similarity`.
Expected outcome: route to that page.

Rule: existing pages beat duplicates.

Example: input candidate about closures and existing `closure` -> expected `enrich-existing`.

Ugliest edge case: input candidate matches a generic page and a section-specific page.
Expected outcome: section-specific page wins.

## Acceptance Criteria

- Unit tests cover `ExtractedUnit`, `PagePlan`, `PlannedPageWrite`, and `WikiMatch`.
- A fake PDF ingest proves no write occurs before `PagePlan`.
- Existing page match tests enrich existing pages.
- Section identity tests beat semantic similarity.
- Nested `WikiStructure` tests render from `PageMetadata`.
- Local flat tests render `{PageId}.md`.
- `PagePlan` JSON persists under source cache.
- Observation report lists extracted unit count, topic cluster count, write counts,
  contradictions, deferrals, and final paths.
- `uv run pytest harness/tests/test_planning.py` passes.
- `uv run llmwiki ingest javascriptallonge.pdf` completes after generated state rebuild.

## Cross-Cutting Concerns

Observability: source cache must retain `ExtractedUnit`, `WikiMatch`, `PagePlan`, and observation report artifacts.

Error handling: extraction failures stop before planning, and planning failures stop before writes.

Portability: planning code must not import Ollama, llama-server, 4090, or M5 settings.

## Reference Implementations

- m5 planning TDD: `~/gits/llm-wiki-m5-24gb/docs/2026-06-18-global-ingest-planning.md`.
- m5 planning code: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/planning.py`.
- m5 planning tests: `~/gits/llm-wiki-m5-24gb/harness/tests/test_planning.py`.
- our PDF pipeline: `harness/src/llmwiki/pdf/pipeline.py`.
- our session orchestration: `harness/src/llmwiki/runtime/session.py`.

## Alternatives Considered

- Chosen: bounded deterministic planning, because it keeps source and wiki context small.
- Rejected: chunk-immediate writes, because page choice is local.
- Rejected: full-source model context, because context limits break large sources.
- Rejected: external vector service, because both repos must stay local.

## Halt Conditions

- If implementation needs an external service, stop and ask.
- If implementation writes pages during extraction, stop and redesign.
- If implementation gives folders independent meaning, stop and use `PageMetadata`.
- If m5-wiki and our wiki need different planning object names, stop and reconcile names.
