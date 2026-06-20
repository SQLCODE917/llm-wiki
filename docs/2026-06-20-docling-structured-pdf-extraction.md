# Docling Structured PDF Extraction

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `RawSource` | Immutable source file under `raw/`. |
| `TextLayerPdf` | PDF with enough embedded text for deterministic extraction. |
| `ScannedPdf` | PDF without enough embedded text for deterministic extraction. |
| `ScannedPdfError` | Error that stops PDF ingest for `ScannedPdf`. |
| `DoclingExtractor` | PDF adapter that creates `DocumentModel`. |
| `DocumentModel` | Structured record for one extracted `RawSource`. |
| `DocumentElement` | One heading, paragraph, list item, table, code block, picture, or furniture item. |
| `SourceSectionBuilder` | Domain service that creates `SourceSection` records. |
| `SourceSection` | Heading-scoped group of body `DocumentElement` records. |
| `SourceChunker` | Domain service that creates `SourceChunk` records. |
| `SourceChunk` | Token-bounded part of one `SourceSection`. |
| `ExtractedUnit` | Source-derived text unit that feeds `PagePlan`. |
| `PdfIngestManifest` | Persistence model that records PDF cache state. |
| `PagePlan` | Run-owned plan for page targets and serial writes. |
| `Evidence` | Citation-backed support for a generated claim. |
| `PageMetadata` | Page identity, summary, sources, and update date. |
| `PagePath` | Rendered location of one `WikiPage` inside `wiki/`. |
| `WikiStructure` | Domain object that renders `PagePath` from `PageMetadata`. |
| `IngestTopology` | Allowed write order for one ingest run. |
| `m5-wiki` | Sibling repo at `~/gits/llm-wiki-m5-24gb`. |

The current PDF pipeline builds chunks from PyMuPDF page text and table of contents data.
That pipeline has mixed page furniture or later sections into early source pages.
m5-wiki uses Docling to preserve element kind, heading path, and page provenance.
This TDD adopts that extraction boundary while keeping `PagePlan` input as `ExtractedUnit`.

## Goals

- Use `DoclingExtractor` as the default PDF adapter for `TextLayerPdf`.
- Persist `DocumentModel`, `SourceSection`, and `SourceChunk` artifacts.
- Create `ExtractedUnit` records only from `SourceChunk`.
- Preserve page provenance from `DocumentElement` through `ExtractedUnit`.
- Exclude table of contents and furniture from `ExtractedUnit`.
- Keep code portable between our wiki and m5-wiki.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not add whole-document OCR.
- This TDD does not interpret pictures.
- This TDD does not change `PagePlan`.
- This TDD does not change `WikiStructure`.
- This TDD does not group source pages.

Forbidden approaches:

- Do not use exported Docling Markdown as the authority.
- Do not feed Docling chunker output directly into `ExtractedUnit`.
- Do not merge two `SourceSection` records into one `SourceChunk`.
- Do not create `ExtractedUnit` records from table of contents content.
- Do not require a remote Docling service.

## Requirements

- `DoclingExtractor` must retain `RawSource.source_locator`.
- `DoclingExtractor` must retain the source hash.
- `DoclingExtractor` must set `do_ocr` to false for `TextLayerPdf`.
- `DoclingExtractor` must refuse `ScannedPdf` with `ScannedPdfError`.
- `DocumentModel` must store `extractor_name` and `extractor_version`.
- `DocumentElement` must store element kind, body state, heading path, page span, text, and Markdown.
- `DocumentElement.body_state` must use `body`, `furniture`, or `table_of_contents`.
- `SourceSectionBuilder` must exclude `DocumentElement` records where `body_state` is not `body`.
- `SourceSectionBuilder` must start a new `SourceSection` when heading path changes.
- `SourceChunker` must split an oversized `SourceSection` without crossing the section boundary.
- `SourceChunker` must keep a fitting code block in one `SourceChunk`.
- `SourceChunker` must keep a fitting table in one `SourceChunk`.
- Each `ExtractedUnit` must map from exactly one `SourceChunk`.
- `ExtractedUnit.heading_path` must equal `SourceChunk.heading_path`.
- `ExtractedUnit.locator` must render from `SourceChunk.page_start` and `SourceChunk.page_end`.
- `PdfIngestManifest` must persist the extractor name.

## Invariants

- `raw/` remains immutable.
- `wiki/` remains generated knowledge.
- `ExtractedUnit` remains the only PDF extraction object that `PagePlan` consumes.
- `Evidence` remains required for generated claims.
- `IngestTopology` remains `serial`.
- `PageMetadata.page_id` remains page identity.
- `WikiStructure` remains the only `PagePath` renderer.

## Proposed Architecture

`DoclingExtractor` creates `DocumentModel` from a PDF `RawSource`.
`SourceSectionBuilder` creates `SourceSection` records from body elements.
`SourceChunker` creates `SourceChunk` records from one `SourceSection`.
The ingest orchestrator maps `SourceChunk` records into `ExtractedUnit` records.

```
+-----------+     +------------------+     +---------------+
| RawSource |---->| DoclingExtractor |---->| DocumentModel |
+-----------+     +------------------+     +-------+-------+
                                                   |
                                                   v
                                           +---------------+
                                           | SourceSection |
                                           +-------+-------+
                                                   |
                                                   v
                                           +---------------+
                                           | SourceChunk   |
                                           +-------+-------+
                                                   |
                                                   v
                                           +---------------+
                                           | ExtractedUnit |
                                           +---------------+
```

## Key Interactions

Text-layer PDF flow:

```
RawSource -> DoclingExtractor -> DocumentModel
DocumentModel -> SourceSectionBuilder -> SourceSection
SourceSection -> SourceChunker -> SourceChunk
SourceChunk -> ExtractedUnit -> PagePlan
```

Cache-hit flow:

```
PdfIngestManifest -> DocumentModel cache check
DocumentModel cache -> SourceChunk cache -> ExtractedUnit
```

Scanned PDF flow:

```
RawSource -> text coverage check -> ScannedPdfError
```

## Data Model

| Object | Required fields |
|---|---|
| `DocumentModel` | `source_locator`, `source_hash`, `extractor_name`, `extractor_version`, `elements` |
| `DocumentElement` | `element_id`, `element_kind`, `body_state`, `heading_path`, `page_start`, `page_end`, `text`, `markdown` |
| `SourceSection` | `section_id`, `heading_path`, `page_start`, `page_end`, `element_ids`, `text` |
| `SourceChunk` | `chunk_id`, `source_section_id`, `heading_path`, `page_start`, `page_end`, `text`, `token_estimate` |
| `ExtractedUnit` | `unit_id`, `raw_source`, `locator`, `heading_path`, `text`, `extraction_status`, `source_hash` |

`DocumentElement.element_kind` values are `heading`, `paragraph`, `list_item`, `table`, `code_block`, `picture`, and `furniture`.

## APIs / Interfaces

- `llmwiki ingest <source>.pdf` uses `DoclingExtractor` by default.
- `llmwiki ingest <source>.pdf --reextract` rebuilds PDF cache artifacts.
- `ensure_extracted` returns an extraction result with `PdfIngestManifest`.
- `chunk_file` returns the persisted text for one `SourceChunk`.
- The cache stores `document_model.json`.
- The cache stores `source_sections.json`.
- The cache stores one chunk file per `SourceChunk`.

## Behavior & Domain Rules

Rule: `SourceSection` controls semantic boundaries.

Example: input headings `Object.assign`, `Why?`, and `A Warm Cup`.
Expected outcome: `SourceSectionBuilder` creates three `SourceSection` records.

Example: input front matter pages from Sword World and later combat pages.
Expected outcome: the front matter `SourceSection` excludes combat rules.

Rule: `SourceChunk` preserves section identity.

Example: input one small `SourceSection`.
Expected outcome: `SourceChunker` emits one `SourceChunk`.

Example: input one oversized `SourceSection`.
Expected outcome: `SourceChunker` emits multiple chunks with one `source_section_id`.

Rule: body state filters evidence input.

Example: input table of contents entries under `Contents`.
Expected outcome: no `ExtractedUnit` contains those entries.

Example: input repeated page footer.
Expected outcome: no `ExtractedUnit` contains the footer.

Ugliest edge case: input code block exceeds the token budget.
Expected outcome: `SourceChunker` emits one oversized `SourceChunk` and records a warning.

## Acceptance Criteria

Milestone 1: pure extraction domain tests.

- Tests cover `DocumentModel`, `DocumentElement`, `SourceSection`, and `SourceChunk`.
- Tests prove `Object.assign`, `Why?`, and `A Warm Cup` create separate sections.
- Tests prove table of contents content does not reach `SourceSection`.
- Tests prove furniture content does not reach `SourceSection`.
- Tests prove `SourceChunker` does not merge adjacent sections.
- Tests prove oversized sections split without changing heading path.

Milestone 2: pipeline tests.

- Fake PDF pipeline test proves `PdfIngestManifest.extractor_name` equals `docling`.
- Fake PDF pipeline test proves `document_model.json` exists.
- Fake PDF pipeline test proves `source_sections.json` exists.
- Cache-hit test proves re-run keeps manifest progress.
- Reextract test proves `--reextract` rebuilds chunks.
- Scanned PDF test proves `ScannedPdfError` stops before planning.

Milestone 3: ingest quality tests.

- Clean JavaScript Allonge ingest separates `Object.assign`, `Why?`, and `A Warm Cup`.
- Clean Sword World ingest keeps front matter claims inside front matter pages.
- `uv run pytest harness/tests/test_pdf_document.py harness/tests/test_pdf_pipeline.py` passes.

## Cross-Cutting Concerns

Observability: the cache must retain source, extractor, section, chunk, and warning artifacts.

Error handling: the orchestrator must stop before `PagePlan` when `DoclingExtractor` fails.

Portability: extraction code must not import Ollama, 4090, or M5 runtime settings.

## Reference Implementations

- m5 TDD: `~/gits/llm-wiki-m5-24gb/docs/2026-06-19-docling-extraction-mapping.md`.
- m5 adapter: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/pdf/docling_extractor.py`.
- m5 document model: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/pdf/document.py`.
- m5 tests: `~/gits/llm-wiki-m5-24gb/harness/tests/test_pdf_document.py`.
- our pipeline: `harness/src/llmwiki/pdf/pipeline.py`.

## Alternatives Considered

- Chosen: `DocumentModel`, because both repos need one shared extraction boundary.
- Rejected: PyMuPDF table of contents chunks, because page text crosses topic boundaries.
- Rejected: Docling exported Markdown, because it hides element and page provenance.
- Rejected: whole-document OCR, because this work targets text-layer PDFs.

## Halt Conditions

- If Docling lacks page provenance for a PDF, stop and keep the old extractor for that source.
- If the design requires remote Docling services, stop and ask.
- If code needs a new wiki folder taxonomy, stop and keep `WikiStructure` unchanged.
- If our wiki and m5-wiki need different object names, stop and reconcile names.
