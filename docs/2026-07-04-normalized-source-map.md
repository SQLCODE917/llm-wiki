# TDD: Normalized Source Map

## Context & Problem

The current PDF path produces document elements, sections, and chunks.
Later ingest stages treat chunks as source truth.
This lets prompt windows shape evidence and page identity.

Glossary:

- `NormalizedSourceMap`: the durable source model for one `RawSource`.
- `SourceBlock`: one coherent source unit in a `NormalizedSourceMap`.
- `SourceAnchor`: a stable locator for one `SourceBlock` or source span.
- `SourceMapFinding`: one source map quality issue.
- `PromptWindow`: a derived text window for model prompts.

## Goals

- Make `NormalizedSourceMap` the first durable artifact after PDF extraction.
- Give every `SourceBlock` a stable `SourceAnchor`.
- Preserve source order, headings, page coordinates, and block type.
- Make `PromptWindow` derivation repeatable from `SourceBlock` records.
- Measure source map quality before evidence records exist.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not extract typed evidence records.
- This design does not plan public wiki pages.
- This design does not render wiki markdown.
- This design does not migrate old chunk artifacts.

Forbidden approaches:

- Do not make chunks the durable source authority.
- Do not let a page planner read raw chunk records.
- Do not infer source order from file write order.
- Do not mutate files in `raw/`.

## Requirements

- The PDF pipeline writes one `NormalizedSourceMap` per `RawSource`.
- Each `SourceBlock` has a `SourceAnchor`.
- Each `SourceBlock` stores source text, block type, page span, and section path.
- Each `SourceBlock` stores extraction confidence.
- The source map builder records header and footer candidates.
- The source map builder records table and code block candidates.
- The source map builder records OCR or layout findings.
- The prompt builder creates `PromptWindow` records from `SourceBlock` records.
- No downstream planning code consumes chunk records as source authority.

## Invariants

- Raw sources stay immutable.
- Generated artifacts stay disposable.
- The harness owns artifact writes.
- The wiki layer does not become the source authority.
- `index.md` and `log.md` stay harness-owned.

## Proposed Architecture

```text
RawSource
    |
    v
PdfExtractor
    |
    v
NormalizedSourceMap
    |
    +--> SourceMapFinding
    |
    v
PromptWindow
```

`RawSource` stores the immutable source file.
`PdfExtractor` reads the source file and emits structured extraction output.
`NormalizedSourceMap` stores ordered source blocks and anchors.
`SourceMapFinding` stores source map quality issues.
`PromptWindow` stores derived text for model calls.

## Key Interactions

Build source map:

```text
ingest compiler -> pdf extractor: read raw source
pdf extractor -> source map builder: emit document elements
source map builder -> normalized source map: write source blocks
source map builder -> source map finding: record quality issues
```

Build prompt windows:

```text
evidence extractor -> source map: request block range
prompt builder -> source map: read source blocks
prompt builder -> prompt window: group source blocks
evidence extractor -> prompt window: call model
```

## Data Model

`NormalizedSourceMap` stores source id, source fingerprint, extractor name,
extractor version, source blocks, and source map findings.

`SourceBlock` stores block id, source anchor, block type, source text, page span,
section path, parent block id, child block ids, and confidence.

`SourceAnchor` stores source id, page span, element path, text fingerprint, and
optional bounding boxes.

`SourceMapFinding` stores finding id, severity, source anchor, finding code, and
message.

`PromptWindow` stores window id, source block ids, token estimate, and text.

## APIs / Interfaces

`NormalizedSourceMap` is the only source artifact that evidence extraction reads.

`PromptWindow` is an input DTO for model calls.
It is not a source authority.

`SourceAnchor` is the citation address used by later evidence records.

## Behavior & Domain Rules

The source map builder preserves source order.
Example: a heading block appears before all body blocks in that section.

The source map builder keeps coherent table text together.
Example: a table row stays in one table block when the extractor marks it as a
single row.

The source map builder marks weak extraction.
Example: a block with broken word spacing records a layout finding.

The prompt builder derives prompt windows from source blocks.
Example: a prompt window for Shade includes the Shade heading and adjacent rule
text.

## Acceptance Criteria

- A unit test builds a source map from a small fixture with headings, prose, and
  a table.
- The fixture source map contains stable source block ids across two runs.
- The fixture source map stores page spans for every source block.
- The fixture source map stores section paths for every source block under a
  heading.
- A prompt window fixture contains only text from its listed source blocks.
- A test proves a page planner cannot read chunk records.
- A Sword World fixture exposes the Shade source block through a source anchor.
- A JavaScript Allonge fixture keeps a code example in a code block.
- A source map report counts low-confidence blocks.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

Artifact compatibility does not apply.
The implementation can delete old chunk authority artifacts.

The ingest log records source map counts and blocking source map findings.

## Reference Implementations

- PDF document model: `harness/src/llmwiki/pdf/document.py`
- PDF artifact writer: `harness/src/llmwiki/pdf/pipeline.py`
- Evidence locators: `harness/src/llmwiki/domain/evidence_locator_index.py`

## Alternatives Considered

- Keep chunks as source truth: rejected because chunks are prompt windows.
- Use markdown as the source map: rejected because markdown loses coordinates.
- Store only citations: rejected because later stages need block structure.

## Halt Conditions

- Stop if the extractor cannot return stable page spans.
- Stop if a downstream page planner needs chunk records to proceed.
