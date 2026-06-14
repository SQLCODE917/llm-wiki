# Strict Citation Parser

## Context & Problem

The M5 schema asks pages to cite raw sources with simple text citations such as
`(raw/book.pdf p.28-41)`. The backup repo contains stronger locator and evidence
validation code, but it assumes normalized source state and old page directories.
Before writes or lint can enforce anything, the M5 harness needs a pure parser
that understands the current flat wiki citation style.

## Goals

- Parse citations from `wiki/*.md` page bodies without model calls.
- Support raw markdown citations, PDF page ranges, and normalized line ranges.
- Report malformed citations and missing raw sources deterministically.
- Preserve OCR caveat semantics from the M5 PDF pipeline.
- Provide findings that later write/lint gates can consume.

## Non-Goals & Forbidden Approaches

Non-goals:

- No write-time enforcement in this TDD.
- No LLM judging of citation quality.
- No stable evidence-ID requirement.
- No extraction-state database migration.

Forbidden approaches:

- Do not require old `.wiki-extraction-state/` files.
- Do not restore old page directories or page schemas.
- Do not parse citations with ad hoc logic spread through tools.
- Do not read or mutate `backup/reference/...` at runtime.

## Requirements

- Parser input is page name plus markdown body.
- Parser output is structured citations and findings.
- Raw source paths are confined to `raw/`.
- Missing source paths are findings.
- Malformed page ranges and line ranges are findings.
- OCR caveat text may be cited as caveated evidence but not as a verbatim quote.
- Parser functions are pure except for a small source-existence adapter.

## Invariants

- Citation parsing never modifies wiki or raw files.
- A page with no citations is valid parser input.
- Existing wiki pages do not need to change before parser adoption.
- Findings are deterministic for the same page text and source inventory.
- The parser does not decide whether an operation should fail.

## Proposed Architecture

Add a citation domain module and a thin validation adapter. The domain module
extracts citation-like spans from page text; the adapter checks those spans
against source inventory and optional PDF/cache metadata.

```
+------------+       +----------------+       +------------------+
| wiki page  |------>| Citation       |------>| Citation         |
| body       |       | parser         |       | findings         |
+------------+       +-------+--------+       +------------------+
                             |
                             v
                      +--------------+
                      | Source index |
                      +--------------+
```

Components: parser owns syntax; source index owns source existence/range facts;
findings are plain data passed to later gates.

## Key Interactions

Page scan:

```
Lint/test       Parser       Source index
 | page text      |             |
 |--------------->| extract     |
 |                |------------>|
 |                |<--facts-----|
 |<----citations + findings-----|
```

Malformed citation:

```
Parser          Finding
 | sees raw/book.pdf p.bad |
 |------------------------>|
 | malformed page range    |
```

## Data Model

- **Citation** — page name, source path, raw matched text, optional PDF page
  range, optional normalized line range, and caveat flags.
- **SourceInventory** — set of source paths under `raw/` plus optional metadata
  for cached PDF chunks.
- **CitationFinding** — page name, severity, citation text, finding code, and
  human-readable message.
- **FindingCode** initial values: `missing-source`, `malformed-page-range`,
  `malformed-line-range`, `path-outside-raw`, `ocr-verbatim-risk`.

Access pattern: lint and tests scan all pages; write-time gates later scan one
page at a time.

## APIs / Interfaces

- Domain module: parse page body into citations.
- Validation adapter: combine citations with source inventory into findings.
- Finding severity values: `info`, `warn`, `fail`.

The exact public contract is the finding fields above. Implementations may
choose dataclasses or Pydantic models, but callers must receive those fields.

## Behavior & Domain Rules

- `(raw/article.md)` is a source citation.
- `(raw/book.pdf p.28-41)` is a source citation with a PDF page range.
- `normalized:L12-L20` is a normalized line locator only when associated with a
  known source context.
- Paths escaping `raw/` are findings even if the file exists.
- OCR caveat findings are warnings unless a later strict gate upgrades them.

Examples:

- Page text cites `(raw/antikythera-mechanism.md)` and that file exists -> no
  missing-source finding.
- Page text cites `(raw/missing.md)` -> `missing-source`.
- Page text cites `(raw/book.pdf p.xx-41)` -> `malformed-page-range`.
- Page text quotes `[figure text (OCR, unverified)]` as exact evidence ->
  `ocr-verbatim-risk`.

## Acceptance Criteria

- Tests cover markdown source citations.
- Tests cover PDF page ranges.
- Tests cover malformed ranges.
- Tests cover missing sources.
- Tests cover path traversal attempts.
- Tests cover OCR caveat detection.
- Existing `uv run pytest harness/tests` passes.
- `uv run ruff check harness/src harness/tests` passes.
- `uv run mypy harness/src` passes.

## Cross-Cutting Concerns

Error handling: parser failures become findings, not exceptions, unless input
types are invalid.

Portability: no platform-specific dependencies.

Performance: parser must be cheap enough to run over every wiki page during
lint.

## Reference Implementations

- Current link parser pattern: `harness/src/llmwiki/domain/links.py`
- Current page parsing: `harness/src/llmwiki/domain/pages.py`
- Backup locator reference:
  `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_core/src/wiki_core/types/locator.py`
- Backup evidence validator:
  `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_io/src/wiki_io/evidence/validator.py`

## Alternatives Considered

- Restore stable evidence IDs now — rejected because the M5 wiki cites raw
  sources directly.
- Use model judging — rejected because syntax and source existence are
  deterministic.
- Enforce on writes immediately — rejected because parser correctness should
  ship independently first.

## Halt Conditions

- If useful citation validation requires old extraction state as a source of
  truth, stop and design a current M5 cache/index first.
- If citation syntax needs to change `SCHEMA.md`, stop and propose that schema
  change explicitly.
- If parser findings become subjective support judgments, stop and split LLM
  judging into a later TDD.
