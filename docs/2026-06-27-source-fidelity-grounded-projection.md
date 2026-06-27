# Source Fidelity And Grounded Projection - TDD (2026-06-27)

## Context & Problem

`RawSource` is the immutable source file in `raw/`.
`DocumentModel` is the structured PDF extraction result.
`ClaimLedger` is the durable source-derived artifact for claims and technical atoms.
`ProjectionCoverage` is the support map from one `PageBody` to ledger support.

The current harness preserves many technical tables after extraction.
It does not recover all missed PDF tables before chunking.
The current harness writes wiki pages before `ClaimLedger` controls projection.
Dense navigation needs deterministic promotion rules.

## Goals

- The PDF path recovers missed tables before `SourceChunk` creation.
- The harness preserves raw table text for every accepted table atom.
- The harness writes `ClaimLedger` artifacts for each ingest.
- The harness writes `ProjectionCoverage` artifacts for generated pages.
- The harness promotes pages by source evidence, category, and salience.
- The harness keeps cross-links deterministic and source-agnostic.
- Each stage supports test ingests of Sword World and JavaScript Allonge.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not add OCR for scanned PDFs.
- This design does not add a vector database.
- This design does not migrate old `wiki/` data.
- This design does not preserve old generated page shapes.

Forbidden approaches:

- Do not add source-specific trigger lists for Sword World or JavaScript Allonge.
- Do not add one-off page names as category rules.
- Do not let table rows create wiki pages by themselves.
- Do not render unsupported prose from `ClaimLedger` entries.
- Do not keep two active ingest pipelines after a stage replaces one.
- Do not use raw local paths as source authority.

## Requirements

- `raw/` stays read-only during each ingest.
- The PDF extractor writes cache artifacts only under `cache/`.
- The table importer runs before `build_source_sections`.
- The table importer uses source-neutral extraction stages.
- The table importer keeps extractor stage metadata in cache artifacts.
- The ledger stores source locators and evidence ids.
- The page renderer stores internal support ids outside visible `PageBody`.
- The index lists promoted pages and source hubs.
- The index does not list every low-salience section page.
- The source hub links to generated section and topic pages.
- The source hub records quality and review counts.
- The cross-source builder uses persisted topic indexes and ledgers.

## Invariants

- `RawSource` bytes never change.
- `index.md` remains harness-maintained.
- `log.md` remains append-only.
- `PageMetadata` remains the page identity authority.
- `WikiStructure` renders every `PagePath`.
- `ClaimLedger` records source-derived facts before page projection.
- `ProjectionCoverage` records every rendered support unit.
- A failed quality gate produces an artifact and withholds authoritative pages.

## Proposed Architecture

```
RawSource
  |
  v
PDF extractor -> Table importer -> DocumentModel -> SourceChunk
  |
  v
PagePlan + TechnicalAtomCatalog
  |
  v
ClaimLedger -> QualityReport
  |
  v
ProjectionPlanner -> ProjectionCoverage -> WikiPage
  |
  v
NavigationPolicy -> index.md + source hub links
  |
  v
CrossSourceBuilder -> canonical concept pages
```

The PDF extractor creates the first `DocumentModel`.
The table importer adds missed table elements to `DocumentModel`.
The page planner keeps current source planning until the ledger planner replaces it.
The ledger builder writes portable `ClaimLedger` artifacts.
The projection planner selects supported ledger entries for pages.
The navigation policy promotes pages by category and salience.
The cross-source builder writes canonical concept pages from topic indexes.

## Key Interactions

### PDF Ingest Stage

```
Session -> PDF extractor: extract RawSource
PDF extractor -> Table importer: enrich DocumentModel
Table importer -> PDF extractor: enriched DocumentModel
PDF extractor -> cache: write DocumentModel and chunks
Session -> PagePlan: build plan from chunks
Session -> WikiStore: write artifacts and pages
```

### Ledger Projection Stage

```
Session -> LedgerBuilder: build ClaimLedger
LedgerBuilder -> QualityReport: evaluate ledger
Session -> ProjectionPlanner: build page plans
ProjectionPlanner -> PageRenderer: render PageBody
PageRenderer -> WikiStore: write WikiPage and ProjectionCoverage
```

### Navigation Stage

```
Session -> NavigationPolicy: classify projected pages
NavigationPolicy -> WikiStore: write source hub
NavigationPolicy -> WikiStore: update index entries
Session -> log.md: append ingest summary
```

### Cross-Source Stage

```
Session -> WikiStore: load topic indexes and ledgers
CrossSourceBuilder -> ProjectionPlanner: build canonical concepts
ProjectionPlanner -> WikiStore: write concept pages
Session -> log.md: append synthesize summary
```

## Data Model

`TableCandidate` records one recovered table candidate.
It stores `caption`, `page_start`, `page_end`, `y0`, `raw_text`, and `extractor_stage`.

`ClaimLedger` records source claims, concepts, relationships, and technical atoms.
It stores `source_locator`, `source_hash`, entries, atoms, statements, decisions, and rejected candidates.

`ProjectionCoverage` records rendered support units.
It stores text ranges and support ids for claims, atoms, review items, and relationships.

`TopicIndex` records promoted source topics.
It stores topic keys, labels, entry ids, atom ids, and one representative claim.

## APIs / Interfaces

- `enrich_document_model_with_tables` returns a `DocumentModel`.
- `build_current_ledger_artifacts` returns portable ledger artifact files.
- `build_source_projection` returns `WikiPage` records and coverage artifacts.
- `build_topic_index` returns one source topic index.
- `build_cross_source_pages` returns canonical concept `WikiPage` records.
- `NavigationPolicy` returns promoted pages and hidden pages.

## Behavior & Domain Rules

The table importer accepts source-neutral table candidates.
It uses primary table detection, caption layout, forward cues, and geometry repair.
It dedupes against primary extraction and other candidates.

Example:
Input: a captioned table that the primary extractor missed.
Expected outcome: one fallback table `DocumentElement`.

Example:
Input: a paragraph that mentions "table of contents".
Expected outcome: no fallback table `DocumentElement`.

The ledger treats tables as technical atoms.
It renders a logical table when parsing succeeds.
It preserves raw table text when parsing fails.

Example:
Input: a pipe table with a separator row.
Expected outcome: parsed `TablePayload`.

Example:
Input: an aligned table with ambiguous columns.
Expected outcome: partially parsed `TablePayload` with raw text.

The navigation policy promotes pages by evidence.
It promotes source hubs, canonical concepts, durable syntheses, and high-salience source topics.
It hides low-salience section pages from the top index.

Example:
Input: a section page with only one source-local claim.
Expected outcome: source hub link only.

Example:
Input: a source topic with many claims and one table atom.
Expected outcome: top-level concept or source-topic promotion.

## Acceptance Criteria

Milestone 1: PDF table fidelity.

- Tests prove the importer recovers a missed captioned PDF table.
- Tests prove the importer recovers a forward-cue table.
- Tests prove the importer dedupes existing table elements.
- Tests prove JavaScript Allonge and Sword World extraction produce table-preserving artifacts
  before model synthesis.
- Tests prove raw table text reaches the technical atom catalog.

Milestone 2: Ledger artifacts.

- Tests prove each ingest writes `claim-ledger.json`.
- Tests prove every extracted unit has one disposition.
- Tests prove table atoms carry raw table text.
- Tests prove named table references produce quality findings when unresolved.

Milestone 3: Projection coverage.

- Tests prove generated page claims select usable ledger entries.
- Tests prove rendered table blocks have coverage entries.
- Tests prove internal support ids do not appear in `PageBody`.
- Tests prove blocking findings withhold authoritative page writes.

Milestone 4: Dense navigation.

- Tests prove the index omits hidden low-salience section pages.
- Tests prove the source hub links hidden section pages.
- Tests prove promoted pages link back to source hubs.
- Tests prove deterministic lint finds no graph orphan for promoted pages.

Milestone 5: Cross-source projection.

- Tests prove topic indexes persist per source.
- Tests prove shared source topics create canonical concept pages.
- Tests prove canonical concept pages keep source-backed positions separate.
- Tests prove cross-source pages have at least two source supports.

## Cross-Cutting Concerns

Observability:
Each stage writes a report artifact with counts and quality findings.

Error handling:
Each stage fails with corrective messages from the boundary component.

Runtime:
The harness uses Forge and Ollama runtime profiles for model calls.

## Reference Implementations

- M5 table importer: `/home/serdm/gits/llm-wiki-m5-24gb/harness/src/llmwiki/pdf/table_candidates.py`
- M5 section plan: `/home/serdm/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/ledger/section_planning.py`
- M5 topic index: `/home/serdm/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/ledger/topics.py`
- Current salience: `harness/src/llmwiki/domain/salience.py`
- Current ledger adapter: `harness/src/llmwiki/domain/ledger/current_artifacts.py`

## Alternatives Considered

- Use only Docling tables: rejected because primary extraction misses tables.
- Use only regex over chunks: rejected because layout geometry carries table structure.
- Promote all section pages: rejected because index navigation becomes noisy.
- Keep both projections active: rejected because quality rules diverge.

## Halt Conditions

- If OCR becomes required for either test source, stop and write an OCR TDD.
- If a new dependency needs network installation, stop and ask for approval.
- If the projection change removes current evidence gates, stop and split the stage.
- If a rule needs source-specific words, stop and replace it with source-neutral evidence.
