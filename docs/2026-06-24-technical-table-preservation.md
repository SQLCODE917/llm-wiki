# Technical Table Preservation

## Context & Problem

Glossary:
- `TechnicalTable`: one preserved table from a `RawSource`.
- `TechnicalTableBlock`: one contiguous extracted block that belongs to a `TechnicalTable`.

The current `TechnicalAtom` builder emits one `table-row` atom per Markdown row.
That shape loses the table context that makes technical tables useful.
The current row atoms also cite the whole `SourceRange`.
That range can span many source pages.

## Goals

- Preserve each extracted technical table as one `TechnicalTable`.
- Render complete table content in the existing `TechnicalDetailsSection`.
- Cite each `TechnicalTableBlock` with the narrowest source locator.
- Rebuild stale PDF cache artifacts when they lack current table evidence.
- Keep all rules source-agnostic.

## Non-Goals & Forbidden Approaches

Non-goals:
- This design does not add a separate technical query flow.
- This design does not repair OCR mistakes in source text.
- This design does not hand-normalize domain-specific tables.
- This design does not change raw source files.
- This design does not preserve old generated wiki data.

Forbidden approaches:
- Do not add SwordWorld-specific rules.
- Do not add JavaScriptAllonge-specific rules.
- Do not preserve `table-row` atoms for rows inside a `TechnicalTable`.
- Do not cite a page-level `SourceRange` when a table block locator exists.
- Do not add compatibility parsing for old PDF cache shapes.
- Do not split one logical table into unrelated row atoms to fit the old schema.

## Requirements

- The domain object vocabulary adds `TechnicalTable` and `TechnicalTableBlock`.
- `TechnicalAtomCatalog` owns all `TechnicalTable` records for one source.
- `TechnicalAtomKind` includes `table`.
- The builder creates one `table` atom for each `TechnicalTable`.
- The builder does not create `table-row` atoms for rows inside a `TechnicalTable`.
- A `TechnicalTableBlock` preserves every extracted row and cell.
- A `TechnicalTableBlock` preserves its source order.
- A `TechnicalTableBlock` stores one narrow source citation.
- A `TechnicalTable` can contain multiple `TechnicalTableBlock` records.
- The renderer emits all blocks for a `TechnicalTable`.
- The renderer keeps table block order stable.
- The renderer does not summarize away cells.
- The artifact reuse check rebuilds a PDF cache that lacks `document_model.json`.
- The artifact reuse check rebuilds a PDF cache that lacks `source_sections.json`.
- The implementation keeps generated cache state disposable.

## Invariants

- `RawSource` remains immutable.
- `WikiPage` remains the only user-facing knowledge layer.
- Normal `query` reads wiki pages and uses table details at its discretion.
- `index.md` and `log.md` remain harness-maintained.
- `TechnicalAtomCatalog` remains rebuildable from source artifacts.
- `EvidenceRecord` remains the source support unit for audit checks.
- The system never treats generated cache files as source truth.

## Proposed Architecture

```text
+------------------+      +----------------+
| RawSource        | ---> | SourceText     |
+------------------+      +----------------+
                              |
                              v
+------------------+      +-------------------------+
| PagePlan         | ---> | TechnicalTableDetector  |
| EvidenceRegistry | ---> |                         |
+------------------+      +-------------------------+
                              |
                              v
                       +----------------------+
                       | TechnicalAtomCatalog |
                       +----------------------+
                              |
                              v
                       +-------------------------+
                       | TechnicalDetailsSection |
                       +-------------------------+
```

`RawSource` stores immutable source files.
`SourceText` stores generated, line-addressable source text.
`PagePlan` selects page placement and source claims.
`EvidenceRegistry` stores support records and locators.
`TechnicalTableDetector` creates `TechnicalTable` records.
`TechnicalAtomCatalog` stores technical atoms and technical tables.
`TechnicalDetailsSection` renders exact details on wiki pages.

## Key Interactions

### Fresh Ingest

```text
Ingest orchestrator -> PDF adapter: extract source artifacts
PDF adapter -> SourceText: write extracted text and document model
Ingest orchestrator -> PagePlan: plan page writes
Ingest orchestrator -> EvidenceRegistry: build support records
Ingest orchestrator -> TechnicalTableDetector: detect tables
TechnicalTableDetector -> TechnicalAtomCatalog: add table atoms and tables
TechnicalAtomCatalog -> TechnicalDetailsSection: render exact table content
TechnicalDetailsSection -> WikiPage: append normal technical details
```

### Cache Reuse

```text
Ingest orchestrator -> ArtifactReuseDecision: evaluate cache artifacts
ArtifactReuseDecision -> Ingest orchestrator: require rebuild for missing table artifacts
Ingest orchestrator -> PDF adapter: rebuild generated PDF cache
PDF adapter -> SourceText: write current artifacts
Ingest orchestrator -> TechnicalTableDetector: detect tables from current artifacts
```

## Data Model

`TechnicalTable` is a second-level domain object owned by `TechnicalAtomCatalog`.

Required fields:
- `technical_table_id`
- `source_locator`
- `page_id`
- `title`
- `blocks`
- `source_claim_ids`
- `evidence_ids`

`TechnicalTableBlock` is a second-level domain object owned by `TechnicalTable`.

Required fields:
- `technical_table_block_id`
- `block_index`
- `source_citation`
- `page_range`
- `line_range`
- `markdown`
- `row_count`
- `column_count`

`TechnicalAtom` uses `atom_kind = "table"` for a preserved table.
The `technical_payload` stores a bounded label.
The `normalized_fields` include `technical_table_id`.

## APIs / Interfaces

- `build_technical_atom_catalog` returns `TechnicalTable` records in the catalog.
- `render_technical_details_section` renders `table` atoms from `TechnicalTable` records.
- `technical_atom_catalog_to_json` writes `TechnicalTable` records.
- `technical_atom_catalog_from_json` reads `TechnicalTable` records.
- `ArtifactReuseDecision` rejects PDF cache artifacts that lack current table inputs.

## Behavior & Domain Rules

Rule: The detector preserves one contiguous Markdown table as one `TechnicalTable`.

Example:
- Input: `| 2D | 2 | ** |` followed by `| 3 | 3 | 0 |`.
- Outcome: one `TechnicalTable` with one `TechnicalTableBlock`.

Rule: The detector groups adjacent continuation blocks into one `TechnicalTable`.

Example:
- Input: three nearby blocks with compatible row labels and adjacent column headings.
- Outcome: one `TechnicalTable` with three ordered `TechnicalTableBlock` records.

Rule: The renderer prints all blocks for a table atom.

Example:
- Input: a `TechnicalTable` with three blocks.
- Outcome: the wiki page shows three table blocks under one table atom heading.

Rule: The citation uses the narrowest known table block locator.

Example:
- Input: a table block that the document model places on page 43.
- Outcome: the block citation is `raw/source.pdf p.43`.

Rule: The artifact reuse check rejects stale PDF cache artifacts.

Example:
- Input: a PDF cache with `manifest.json` and no `document_model.json`.
- Outcome: the ingest run rebuilds the generated PDF cache.

Ugly edge case:
- Input: a table block spans two source pages.
- Outcome: the block citation uses `p.N-M` for the block only.

## Acceptance Criteria

Milestone 1:
- The domain vocabulary lists `TechnicalTable` and `TechnicalTableBlock`.
- Unit tests cover one contiguous Markdown table.
- Unit tests cover adjacent continuation blocks.
- Unit tests cover a table block that spans two source pages.
- Unit tests prove table rows inside a table do not become `table-row` atoms.
- Unit tests prove table atoms keep matching `EvidenceRecord` IDs.

Milestone 2:
- JSON round-trip tests cover `TechnicalTable` and `TechnicalTableBlock`.
- Renderer tests show a full table in `TechnicalDetailsSection`.
- Renderer tests show all continuation blocks in source order.
- Citation tests show table block citations do not use whole page `SourceRange` values.
- Cache tests show missing current PDF artifacts trigger rebuild.

Milestone 3:
- A small Antikythera ingest preserves at least one exact table when present.
- A JavaScriptAllonge ingest still preserves exact code examples.
- A SwordWorld ingest renders rating tables as table atoms, not row atoms.
- Claim support audit can sample table atoms.
- Ingest confidence reports include table counts and stale-cache rebuild decisions.

## Cross-Cutting Concerns

Observability:
The ingest report records table counts, block counts, skipped malformed tables, and rebuild decisions.

Error handling:
The detector skips malformed table blocks and records a `ValidationFinding`.

Copyright:
The renderer uses the same generated wiki layer policy as existing technical details.

## Reference Implementations

- Domain style: `harness/src/llmwiki/domain/technical_atoms.py`.
- Builder style: `harness/src/llmwiki/domain/technical_atom_builder.py`.
- Evidence style: `harness/src/llmwiki/domain/evidence_registry.py`.
- Artifact style: `harness/src/llmwiki/domain/ingest_confidence.py`.
- Renderer style: `harness/src/llmwiki/workflows/source_summary_write.py`.

## Alternatives Considered

- Keep row atoms: rejected because row atoms lose table context.
- Store whole tables only in Markdown pages: rejected because audits need catalog records.
- Add source-specific table profiles: rejected because universal extraction can cover this case.
- Support old PDF cache shapes: rejected because generated cache state is disposable.
- Cite only page-level `SourceRange`: rejected because table block locators give better evidence.

## Halt Conditions

- If table grouping needs source-specific rules, stop and ask.
- If the PDF adapter cannot provide table block page locators, stop and ask.
- If a table exceeds practical wiki rendering limits, stop and ask.
- If implementation requires a separate technical query flow, stop and ask.
