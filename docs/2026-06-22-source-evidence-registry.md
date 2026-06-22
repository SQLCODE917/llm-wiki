# Source Evidence Registry

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `RawSource` | Immutable source file under `raw/`. |
| `SourceText` | Line-addressable text derived from one `RawSource`. |
| `SourceRange` | Valid source span for one planned wiki page. |
| `EvidenceRecord` | Stable audit record for one source excerpt. |
| `EvidenceRegistry` | Rebuildable collection of `SourceText`, `SourceRange`, and `EvidenceRecord` records. |
| `EvidenceBank` | Bounded snippet set derived from `EvidenceRecord` records. |
| `LocatorMatch` | Deterministic result for one evidence locator check. |
| `EvidencePolicy` | Domain service that checks citation evidence before writes and audits. |
| `PagePlan` | Run-owned plan for page targets and serial writes. |
| `GeneratedWikiState` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |

Current evidence checks validate citation syntax and some normalized locators.
They do not keep stable evidence records or page-scoped source ranges.
The backup had evidence IDs, source ranges, locator backfill, and stronger text matching.
This TDD adopts those ideas inside the current flat wiki and cache model.

## Goals

- Add `SourceText` for Markdown and PDF sources.
- Add `SourceRange` for source-scoped planned pages.
- Add stable `EvidenceRecord` records for selected source claims.
- Add `EvidenceBank` snippets for model prompts and audits.
- Enrich `EvidencePolicy` with stronger `LocatorMatch` results.
- Persist `EvidenceRegistry` as generated cache state.
- Keep `raw/` immutable.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not add a model judge.
- This TDD does not require evidence IDs on every citation.
- This TDD does not change `WikiStructure`.
- This TDD does not repair existing wiki pages.
- This TDD does not restore the old type-directory schema.

Forbidden approaches:

- Do not write normalized source text under `raw/`.
- Do not import backup packages into active code.
- Do not parse PDFs inside `EvidencePolicy`.
- Do not use `page_id` as evidence identity.
- Do not accept model-supplied `SourceRange` values without deterministic validation.

## Requirements

- The ingest pipeline must create `SourceText` for every `RawSource` in a `SourceBundle`.
- `SourceText` must record `source_locator`, `source_hash`, line count, and text kind.
- Markdown `SourceText` must read the raw Markdown file.
- PDF `SourceText` must read existing extraction cache artifacts.
- The PDF pipeline must create extraction cache artifacts before it creates PDF `SourceText`.
- `SourceRange` must bind one `page_id` to one `RawSource`.
- `SourceRange` must record page range, normalized line range, and heading path.
- `SourceRange` must derive from validated ingest artifacts, not from wiki prose.
- `EvidenceRecord` must retain `source_locator`, `source_hash`, normalized locator, excerpt, and excerpt digest.
- `EvidenceRecord` identity must stay stable when source hash, locator, and excerpt stay stable.
- `EvidenceRecord` must link to `SourceClaim.source_claim_id` when the evidence supports a source claim.
- `EvidenceBank` must include only snippets from validated `EvidenceRecord` records.
- `LocatorMatch` must distinguish exact match, canonicalized match, local-window match, global match, and no match.
- `LocatorMatch` must include a suggested normalized locator for global matches.
- `EvidencePolicy` must use `EvidenceRegistry` when strict evidence mode is `warn` or `fail`.
- The cache must store `evidence-registry.json` beside the related `PagePlan`.

## Invariants

- `raw/` remains immutable.
- `GeneratedWikiState` remains disposable.
- `WikiStructure` remains the only `PageMetadata` to `PagePath` renderer.
- `EvidenceRecord` never replaces the raw source as the source of truth.
- `EvidenceRegistry` is rebuildable from raw sources, extraction cache, and `PagePlan`.
- Existing page-range citations remain syntactically valid unless a later TDD changes citation policy.

## Proposed Architecture

```
+-----------+     +------------+     +-------------+
| RawSource |---->| SourceText |---->| SourceRange |
+-----------+     +-----+------+     +------+------+
                         |                   |
                         v                   v
                  +--------------+     +-------------+
                  | EvidenceRecord|---->| EvidenceBank|
                  +------+-------+     +------+------+
                         |                    |
                         v                    v
                  +----------------+   +---------------+
                  | EvidenceRegistry|-->| EvidencePolicy|
                  +----------------+   +---------------+
```

`RawSource` remains the immutable source file.
`SourceText` gives the source line addresses.
`SourceRange` defines valid source spans for planned pages.
`EvidenceRecord` stores one stable source excerpt.
`EvidenceBank` renders bounded snippets for prompts and audits.
`EvidenceRegistry` stores rebuildable generated evidence state.
`EvidencePolicy` enforces strict evidence modes.

## Key Interactions

Markdown ingest:

```
RawSource -> SourceText
PagePlan -> SourceRange
SourceClaim -> EvidenceRecord
EvidenceRecord -> EvidenceRegistry
```

PDF cache reuse:

```
RawSource -> PDF extraction cache
PDF extraction cache -> SourceText
SourcePageGroup -> SourceRange
```

Locator check:

```
Citation -> EvidencePolicy
EvidencePolicy -> EvidenceRegistry
EvidencePolicy -> LocatorMatch
```

Locator backfill:

```
EvidenceRecord -> EvidencePolicy
EvidencePolicy -> suggested normalized locator
```

## Data Model

| Object | Required fields |
|---|---|
| `SourceText` | `source_locator`, `source_hash`, `source_text_kind`, `lines`, `line_count` |
| `SourceRange` | `source_range_id`, `page_id`, `source_locator`, `page_range`, `line_range`, `heading_path` |
| `EvidenceRecord` | `evidence_id`, `source_locator`, `source_hash`, `source_range_id`, `line_range`, `excerpt`, `excerpt_digest`, `evidence_kind`, `source_claim_id` |
| `EvidenceBank` | `source_range_id`, `evidence_ids`, `snippets`, `token_estimate` |
| `EvidenceRegistry` | `registry_id`, `source_texts`, `source_ranges`, `evidence_records` |
| `LocatorMatch` | `locator`, `confidence`, `finding_code`, `suggested_locator` |

`source_text_kind` values are `markdown` and `pdf-cache`.
`evidence_kind` values are `source-claim`, `citation`, and `table-cell`.
`confidence` values are `exact`, `canonicalized-local`, `local-window`, `canonicalized-global`, and `none`.

## APIs / Interfaces

- `EvidencePolicy` accepts an `EvidenceRegistry`.
- `PagePlan` exposes enough data to build `SourceRange` and `EvidenceRecord`.
- The page-plan cache stores `evidence-registry.json`.
- `curator-status` reports evidence registry counts and fatal evidence findings.
- `lint --strict-evidence warn` reports `LocatorMatch` warnings.
- `lint --strict-evidence fail` treats fatal `LocatorMatch` results as blocking findings.

## Behavior & Domain Rules

Rule: `SourceText` owns line addresses.

Example: input Markdown source with three lines.
Expected outcome: `SourceText.line_count` equals three.

Example: input PDF source with an existing chunk cache.
Expected outcome: `SourceText` uses the cache and records `pdf-cache`.

Rule: `SourceRange` bounds page evidence.

Example: input page cites a locator inside its `SourceRange`.
Expected outcome: `EvidencePolicy` accepts the range.

Example: input page cites a locator outside its `SourceRange`.
Expected outcome: `EvidencePolicy` records a source-range finding.

Rule: `LocatorMatch` gives deterministic repair data.

Example: input excerpt matches cited lines exactly.
Expected outcome: `LocatorMatch.confidence` is `exact`.

Example: input excerpt appears on different lines.
Expected outcome: `LocatorMatch` includes a suggested normalized locator.

Ugliest edge case: input excerpt only matches after hyphenation and page-header cleanup.
Expected outcome: `LocatorMatch.confidence` is `canonicalized-local`.

## Acceptance Criteria

Milestone 1: domain tests.

- `docs/domain-vocabulary.md` records `SourceText`, `SourceRange`, `EvidenceRecord`, `EvidenceRegistry`, `EvidenceBank`, and `LocatorMatch`.
- Tests cover `SourceText`, `SourceRange`, `EvidenceRecord`, `EvidenceBank`, `EvidenceRegistry`, and `LocatorMatch`.
- Tests prove Markdown `SourceText` uses raw Markdown.
- Tests prove PDF `SourceText` uses extraction cache artifacts.
- Tests prove `EvidenceRecord` identity stays stable across registry rebuilds.
- Tests prove source-range violations produce findings.
- Tests prove exact, canonicalized-local, local-window, global, and no-match results.

Milestone 2: policy and cache tests.

- Tests prove `EvidencePolicy` reads `EvidenceRegistry` in `warn` and `fail` modes.
- Tests prove `lint --strict-evidence warn` reports locator suggestions.
- Tests prove `lint --strict-evidence fail` blocks fatal locator findings.
- Tests prove the page-plan cache stores `evidence-registry.json`.
- Tests prove no active code imports backup paths.

Milestone 3: ingest smoke tests.

- Antikythera ingest creates an `EvidenceRegistry` from `raw/antikythera-mechanism.md`.
- Antikythera ingest reuses a valid page-plan cache when the source hash matches.
- JavaScript Allonge ingest creates PDF `SourceText` from PDF cache artifacts.
- JavaScript Allonge ingest rebuilds stale evidence cache artifacts.
- The implementation fixes each smoke-test issue and reruns the failing smoke test.

## Cross-Cutting Concerns

Observability: reports must show registry counts, source-range violations, and locator suggestions.

Error handling: cache corruption must produce a clear finding and trigger registry rebuild.

Performance: registry builders must load one `SourceText` once per policy run.

## Reference Implementations

- Current evidence policy: `harness/src/llmwiki/domain/evidence.py`.
- Current locator resolver: `harness/src/llmwiki/domain/evidence_resolver.py`.
- Current source claims: `harness/src/llmwiki/domain/source_claims.py`.
- Backup resolver idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_io/src/wiki_io/evidence/resolver.py`.
- Backup validator idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_io/src/wiki_io/evidence/validator.py`.
- Backup range idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_io/src/wiki_io/evidence/ranges.py`.
- Backup evidence bank idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_io/src/wiki_io/evidence/bank.py`.
- Backup locator backfill idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_add_evidence_locators.py`.

## Alternatives Considered

- Chosen: generated `EvidenceRegistry`, because audits need stable source evidence.
- Rejected: mandatory evidence IDs in wiki prose, because lightweight citations remain useful.
- Rejected: raw normalized directory, because the current cache layer already owns generated source text.
- Rejected: model-only evidence checks, because locator checks are deterministic.

## Halt Conditions

- If PDF `SourceText` cannot be built from cache artifacts, stop and write a PDF cache contract TDD.
- If `EvidenceRecord` identity changes on unchanged source input, stop and fix identity before audits.
- If implementation needs a new wiki folder structure, stop and keep `WikiStructure` unchanged.
