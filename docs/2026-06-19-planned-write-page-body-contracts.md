# Planned Write Page Body Contracts

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `PageBodyContract` | `Schema` object that defines required `PageBody` shape. |
| `ResolvedPageBodyContract` | Run-owned contract bound to one `PlannedPageWrite`. |
| `PageBodyFinding` | One failed check for model-supplied content. |
| `PageBodyValidator` | Domain service that checks content before `WikiStore.write_page`. |
| `SourcePlan` | Source-specific plan data that can choose a body contract. |
| `SourcePlanContractSelection` | `SourcePlan` selection or override for one contract. |
| `Schema` | Wiki configuration for page kinds and contracts. |
| `WikiPage` | One page with `PageMetadata` and `PageBody`. |
| `PageBody` | Markdown body of one `WikiPage`. |
| `PageKind` | Schema-approved page type. |
| `PagePlan` | Run-owned plan for page targets and serial writes. |
| `PlannedPageWrite` | One write, enrich, or defer action chosen by `PagePlan`. |
| `PageMetadata` | Page identity, summary, sources, and update date. |
| `PagePath` | Rendered location of one `WikiPage` inside `wiki/`. |
| `WikiStructure` | Domain object that renders `PagePath` from `PageMetadata`. |
| `WikiStore` | File boundary that writes markdown pages. |
| `Evidence` | Citation-backed support for a generated claim. |
| `EvidencePolicy` | Domain service that checks claim support after body validation. |
| `GeneratedWikiState` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |

m5-wiki prevents source-copying and missing structure at the write boundary.
Our wiki has evidence gates but still lets `write_page` own too much target
choice. This TDD adopts planned write tools and `PageBodyContract` validation.
The model supplies content; the plan supplies page identity and metadata.

## Goals

- Make `PlannedPageWrite` authorize planned writes.
- Make planned write tools receive only model-authored content.
- Add default `PageBodyContract` values to `Schema`.
- Resolve one `ResolvedPageBodyContract` per `PlannedPageWrite`.
- Run `PageBodyValidator` before `WikiStore.write_page`.
- Report `PageBodyFinding` through forge tool errors.
- Preserve our evidence gate after body validation.
- Keep tool and contract names portable to m5-wiki.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not add source claim coverage.
- This TDD does not replace model-written `PageBody`.
- This TDD does not add a web UI.
- This TDD does not change `WikiStructure`.

Forbidden approaches:

- Do not put `PageBodyContract` on `RawSource`.
- Do not infer a contract from `PagePath`.
- Do not rely on prompt text alone.
- Do not let `PlannedPageWrite` duplicate contract definitions.
- Do not write after `PageBodyValidator` returns findings.
- Do not bypass our evidence policy.

## Requirements

- `Schema` must own `PageBodyContract` values.
- `Schema` must map `PageKind` to default `PageBodyContract`.
- Defaults must include `source-summary`, `entity-page`, `concept-page`, and `synthesis-page`.
- `SourcePlan` must expose `SourcePlanContractSelection`.
- `PagePlan` must resolve one `ResolvedPageBodyContract` for each `PlannedPageWrite`.
- `PlannedPageWrite` must carry target `PageMetadata`.
- `PlannedPageWrite` must carry target `PagePath`.
- Planned `write_page` must accept `page_body` for non-source pages.
- Planned `write_page` must reject invalid content with `PageBodyFinding`.
- Planned `write_page` must call our evidence policy after body validation.
- `docs/page-body-contracts.md` must document defaults and user-defined contracts.

## Invariants

- `raw/` remains immutable.
- `GeneratedWikiState` remains disposable.
- `Schema` remains wiki-level configuration.
- `WikiStore` remains the only markdown writer.
- `WikiStructure` remains the only `PageMetadata` to `PagePath` interface.
- `Evidence` remains required for generated claims.
- `PlannedPageWrite` remains run-owned.

## Proposed Architecture

`Schema` defines reusable contracts. `PagePlan` resolves them for planned
writes. The planned write tool validates content and then writes.

```
+--------+     +------------------+     +--------------------------+
| Schema |---->| PageBodyContract |---->| ResolvedPageBodyContract |
+--------+     +------------------+     +------------+-------------+
                                                   |
                                                   v
+------------------+     +------------------+     +----------+
| PlannedPageWrite |---->| PageBodyValidator|---->| WikiStore|
+------------------+     +------------------+     +----------+
```

`Schema` owns contract definitions.
`ResolvedPageBodyContract` binds planned links, citations, and uncertainty terms.
`PlannedPageWrite` owns target metadata and path.
`PageBodyValidator` blocks invalid content.
`WikiStore` writes only accepted pages.

## Key Interactions

### Planned Non-Source Write

```
PlannedPageWrite -> planned write tool -> PageBody
PageBody -> PageBodyValidator -> EvidencePolicy -> WikiStore
```

### Contract Failure

```
Model -> write_page -> PageBodyFinding
PageBodyFinding -> tool error -> model retry
```

### Contract Selection

```
Schema -> PageBodyContract
SourcePlanContractSelection -> ResolvedPageBodyContract
```

## Data Model

| Object | Required fields |
|---|---|
| `PageBodyContract` | `contract_id`, `match_page_kinds`, `required_sections`, `required_markdown_shape`, `coverage_policy`, `max_words` |
| `ResolvedPageBodyContract` | `contract_id`, `required_sections`, `required_link_page_ids`, `required_source_citations`, `required_uncertainty_terms` |
| `PageBodyFinding` | `finding_type`, `detail` |
| `SourcePlanContractSelection` | `contract_id`, `match_page_kinds`, `page_ids`, override fields |
| `PlannedPageWrite` | `write_id`, `action`, `page_metadata`, `projection`, `evidence`, `resolved_page_body_contract` |

Default contracts:

- `source-summary` for `source`.
- `entity-page` for `entity`.
- `concept-page` for `concept`.
- `synthesis-page` for `synthesis`.

## APIs / Interfaces

- `validate_page_body` accepts `PageBody`, `ResolvedPageBodyContract`, and source text.
- `validate_page_body` returns `PageBodyFinding` records.
- `render_page_body_findings` accepts findings and `ResolvedPageBodyContract`.
- `render_page_body_findings` returns tool text.
- `planned_write_page_tool` creates the planned write `ToolDef`.
- Planned non-source tool field is `page_body`.
- Planned source summary tool is reserved for the source-summary coverage TDD.
- `EvidencePolicy` still checks `page_id`, `PageBody`, evidence inventory, and locator resolver.

## Behavior & Domain Rules

Rule: `Schema` owns contract definitions.

Example: input local schema -> expected four default contracts.

Rule: planned write owns target metadata.

Example: input model calls planned tool -> expected model cannot change `page_id`.

Rule: `PageBodyValidator` blocks copied source text.

Example: input page body copies source paragraphs -> expected `PageBodyFinding`.

Ugliest edge case: input body passes structure but fails evidence locator.
Expected outcome: evidence policy blocks write after body validation.

## Acceptance Criteria

- Unit tests cover `PageBodyContract`, `ResolvedPageBodyContract`, and `PageBodyFinding`.
- Unit tests prove `Schema` owns defaults.
- Unit tests prove `RawSource` has no contract selection.
- Unit tests prove `SourcePlan` selects contracts.
- Unit tests prove `PagePlan` resolves contracts.
- Tool tests prove invalid `page_body` stops before `WikiStore.write_page`.
- Tool tests prove retry succeeds after corrected `page_body`.
- Evidence tests still run after body validation.
- `docs/page-body-contracts.md` exists.
- `docs/page-body-contracts.md` includes local, architecture, and physics examples.
- `uv run pytest harness/tests/test_domain.py harness/tests/test_session_e2e.py` passes.

## Cross-Cutting Concerns

Observability: planned write prompts must show `ResolvedPageBodyContract` values.

Error handling: tool errors must include `PageBodyFinding` text.

Portability: planned write tool signatures must match m5-wiki except for runtime wiring.

## Reference Implementations

- m5 body TDD: `~/gits/llm-wiki-m5-24gb/docs/2026-06-19-page-body-contracts.md`.
- m5 body code: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/page_body_contracts.py`.
- m5 tools: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/workflows/tools.py`.
- our evidence policy: `harness/src/llmwiki/domain/evidence.py`.
- our write tool: `harness/src/llmwiki/workflows/tools.py`.

## Alternatives Considered

- Chosen: deterministic `PageBodyValidator`, because prompt text did not stop copying.
- Rejected: LLM judge, because writes need deterministic blocking.
- Rejected: contract on `RawSource`, because sources are immutable evidence.
- Rejected: unplanned write target changes, because `PagePlan` owns targets.

## Halt Conditions

- If validation needs a model call, stop and ask.
- If planned writes need to mutate target metadata, stop and redesign.
- If evidence gates conflict with body contracts, stop and preserve both gates.
- If m5-wiki tool names differ, stop and reconcile shared names.
