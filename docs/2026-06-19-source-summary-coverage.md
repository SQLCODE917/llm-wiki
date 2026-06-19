# Source Summary Coverage

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `SourceClaim` | Atomic statement extracted from one `ExtractedUnit`. |
| `SourceClaimId` | Internal identity for one `SourceClaim`. |
| `ClaimRoleTag` | `Schema` label that describes a `SourceClaim` function. |
| `SourceClaimGroup` | Related `SourceClaim` records. |
| `SourceSummaryPlan` | Selected `SourceClaim` coverage for one source page. |
| `SourceSummaryDraft` | Model proposal before source `PageBody` rendering. |
| `SourceSummaryBullet` | One draft bullet with covered `SourceClaimId` values. |
| `SourceSummaryRenderer` | Interface that renders accepted `SourceSummaryDraft` into `PageBody`. |
| `Schema` | Wiki configuration for page kinds and role tags. |
| `ExtractedUnit` | Source-derived text unit with locator, heading path, and status. |
| `SourceBundle` | Non-empty set of raw sources for one run. |
| `IngestRun` | One ingest operation over one `SourceBundle`. |
| `Evidence` | Citation-backed support for a generated claim. |
| `PageBody` | Markdown body of one `WikiPage`. |
| `PageBodyValidator` | Domain service that checks content before `WikiStore.write_page`. |
| `PagePlan` | Run-owned plan for page targets and serial writes. |
| `PlannedPageWrite` | One write, enrich, or defer action chosen by `PagePlan`. |
| `CandidateClaim` | Source-derived statement before wiki write. |
| `TopicCluster` | Related `CandidateClaim` records across one `SourceBundle`. |
| `PageMetadata` | Page identity, summary, sources, and update date. |
| `PagePath` | Rendered location of one `WikiPage` inside `wiki/`. |
| `WikiStructure` | Domain object that renders `PagePath` from `PageMetadata`. |
| `GeneratedWikiState` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |

Page body contracts check shape and copying, but they do not choose source
claim coverage. m5-wiki adds source claim planning before source page writes.
This TDD adopts that layer so source pages cover important claims, uncertainty,
limitations, and negative evidence without copying source text.

## Goals

- Add `SourceClaim` inventory for each `IngestRun`.
- Add default `ClaimRoleTag` values through `Schema`.
- Add `SourceClaimGroup` records for coverage and planning.
- Add `SourceSummaryPlan` for source `PlannedPageWrite` records.
- Add `SourceSummaryDraft` validation.
- Render source summary `PageBody` from accepted drafts.
- Keep internal planning identifiers out of generated pages.
- Keep source coverage code portable to m5-wiki.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not create a universal ontology.
- This TDD does not replace `TopicCluster`.
- This TDD does not choose `PagePath`.
- This TDD does not add supervised training data.

Forbidden approaches:

- Do not require every `SourceClaim` to have a role.
- Do not tune role tags for one source.
- Do not write `SourceClaimId` values into `PageBody`.
- Do not let a source summary read the whole wiki.
- Do not make `SourceSummaryPlan` choose folders.
- Do not make `WikiStructure` depend on `SourceClaimGroup`.

## Requirements

- `IngestRun` must create `SourceClaim` records before source writes.
- Each `SourceClaim` must retain `Evidence`.
- Each `SourceClaim` must retain `extracted_unit_id`.
- Each `SourceClaim` must retain `source_span`.
- Each `SourceClaim` must allow zero or more `ClaimRoleTag` values.
- `Schema` must provide default `ClaimRoleTag` values.
- `Schema` must allow replacement role tag values.
- `SourceClaimGroup` must group related source claims.
- `SourceSummaryPlan` must select claims from source claim groups.
- `SourceSummaryPlan` must select highest `claim_salience` uncertainty claims.
- `SourceSummaryPlan` must select highest `claim_salience` limitation claims.
- `SourceSummaryPlan` must select highest `claim_salience` negative-evidence claims.
- Source summary tool must accept `SourceSummaryDraft`.
- `PageBodyValidator` must reject omitted selected claims.
- `PageBodyValidator` must reject long copied phrases.
- `SourceSummaryRenderer` must omit `SourceClaimId` values.

## Invariants

- `raw/` remains immutable.
- `Evidence` remains required for generated claims.
- `GeneratedWikiState` remains disposable.
- `IngestTopology` remains `serial`.
- `PageMetadata.page_id` remains identity.
- `WikiStructure` remains the only `PageMetadata` to `PagePath` interface.
- `PageBody` contains no internal planning identifiers.

## Proposed Architecture

The source claim layer sits between extracted units and source page writes.
`TopicCluster` also consumes claim groups for non-source page targets.

```
+---------------+     +-------------+     +------------------+
| ExtractedUnit |---->| SourceClaim |---->| SourceClaimGroup |
+---------------+     +------+------+     +--------+---------+
                              |                     |
                              v                     v
                     +------------------+   +----------------+
                     | SourceSummaryPlan|   | TopicCluster   |
                     +--------+---------+   +----------------+
                              |
                              v
                     +------------------+
                     | SourceSummaryDraft|
                     +------------------+
```

`SourceClaim` records source statements.
`SourceClaimGroup` groups related claims.
`SourceSummaryPlan` selects coverage.
`TopicCluster` uses groups for page planning.
`SourceSummaryDraft` carries model-authored summary text.

## Key Interactions

### Claim Inventory

```
ExtractedUnit -> SourceClaim -> ClaimRoleTag
SourceClaim -> SourceClaimGroup
```

### Source Page Write

```
SourceSummaryPlan -> source-summary tool -> SourceSummaryDraft
SourceSummaryDraft -> PageBodyValidator -> SourceSummaryRenderer -> WikiPage
```

### Non-Source Planning

```
SourceClaimGroup -> TopicCluster -> PageMetadata
```

## Data Model

| Object | Required fields |
|---|---|
| `SourceClaim` | `source_claim_id`, `statement`, `evidence`, `extracted_unit_id`, `source_span`, `claim_role_tags`, `claim_salience`, `claim_certainty` |
| `ClaimRoleTag` | `tag_name` |
| `SourceClaimGroup` | `source_claim_group_id`, `label`, `source_claims`, `extracted_units`, `claim_role_tags`, `claim_salience` |
| `SourceSummaryPlan` | `source_summary_plan_id`, `page_id`, `selected_source_claims`, `required_claim_role_tags`, `required_source_claim_groups`, `required_source_citations` |
| `SourceSummaryBullet` | `bullet_text`, `covered_source_claims` |
| `SourceSummaryDraft` | `source_record_text`, `claim_bullets` |

Default role tags:

- `identity`, `definition`, `attribute`, `function`, `mechanism`, `method`.
- `evidence`, `provenance`, `temporal`, `quantitative`, `relationship`.
- `comparison`, `requirement`, `procedure`, `limitation`.
- `uncertainty`, `negative-evidence`, `open-question`.

## APIs / Interfaces

- `PagePlan` exposes `source_claims`.
- `PagePlan` exposes `source_claim_groups`.
- Source `PlannedPageWrite` carries `source_summary_plan`.
- Planned source-summary tool accepts `source_record_text` and `claim_bullets`.
- `validate_source_summary_draft` accepts `SourceSummaryDraft` and source text.
- `validate_source_summary_draft` returns `PageBodyFinding` records.
- `SourceSummaryRenderer` accepts `SourceSummaryDraft` and returns `PageBody`.

## Behavior & Domain Rules

Rule: `SourceClaim` is the shared claim inventory.

Example: input paragraph with three statements -> expected three `SourceClaim` records.

Rule: role tags support coverage.

Example: input claim says `possibly` -> expected `uncertainty` tag.

Rule: selected claims must appear in draft coverage.

Example: input omitted selected claim -> expected `PageBodyFinding`.

Ugliest edge case: input draft bullet copies eight source words and covers a claim.
Expected outcome: copied phrase finding blocks write.

## Acceptance Criteria

- Unit tests cover `SourceClaim`, `ClaimRoleTag`, `SourceClaimGroup`, `SourceSummaryPlan`, and `SourceSummaryDraft`.
- Tests prove `SourceClaim` accepts zero, one, or many role tags.
- Tests prove `Schema` replaces default role tags.
- Tests prove `SourceSummaryPlan` selects uncertainty and negative-evidence claims.
- Tests prove `SourceSummaryPlan` selects claims across high-salience groups.
- Tests prove copied phrase validation blocks one bad bullet.
- Tests prove rendered source pages omit `SourceClaimId` values.
- Tests prove `TopicCluster` consumes `SourceClaimGroup`.
- Markdown ingest test proves source summary coverage works without source-specific prompts.
- Fake PDF ingest test proves source claims exist before source writes.
- `uv run pytest harness/tests/test_planning.py harness/tests/test_domain.py` passes.

## Cross-Cutting Concerns

Observability: source cache must retain `SourceClaim`, `SourceClaimGroup`,
`SourceSummaryPlan`, and accepted draft artifacts.

Error handling: source summary validation errors must use `PageBodyFinding`.

Portability: source coverage objects must keep m5-wiki class and field names.

## Reference Implementations

- m5 source coverage TDD: `~/gits/llm-wiki-m5-24gb/docs/2026-06-19-source-summary-coverage-planning.md`.
- m5 domain objects: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/objects.py`.
- m5 planning: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/planning.py`.
- m5 body contracts: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/page_body_contracts.py`.
- our grounding audit: `harness/src/llmwiki/domain/grounding.py`.

## Alternatives Considered

- Chosen: source claim inventory, because source summaries need selected coverage.
- Rejected: prompt-only coverage, because models omit claim types.
- Rejected: universal ontology, because wikis need different subjects.
- Rejected: global copy threshold only, because one copied bullet can pass.

## Halt Conditions

- If `SourceClaimId` values appear in generated pages, stop and fix `SourceSummaryRenderer`.
- If role tags become source-specific, stop and move them to schema configuration.
- If source coverage chooses `PagePath`, stop and use `PageMetadata`.
- If m5-wiki names differ, stop and reconcile shared object names.
