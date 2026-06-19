# Domain Language Consistency

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `DomainTerm` | Exact name of one domain concept. |
| `CodeName` | Snake-case Python field name for one `DomainTerm`. |
| `ForbiddenSynonym` | Old term that must not represent a domain concept. |
| `CoreBoundary` | Domain, store, workflow tool, runtime, prompt, or test file checked by static tests. |
| `PageId` | Stable page identity independent of file location. |
| `PageKind` | Schema-approved page type. |
| `PagePath` | Rendered location of one `WikiPage` inside `wiki/`. |
| `PageBody` | Markdown body of one `WikiPage`. |
| `PageMetadata` | Page identity, summary, sources, and update date. |
| `DomainFrontmatter` | Generated markdown metadata rendered from `PageMetadata`. |
| `SourceLocator` | Raw source identity relative to `raw/`. |
| `Schema` | Wiki configuration for page kinds and metadata fields. |
| `WikiStructure` | Domain object that renders `PagePath` from `PageMetadata`. |
| `LintFinding` | Deterministic wiki health finding. |
| `ToolDTO` | Pydantic tool payload that crosses the model boundary. |
| `GeneratedWikiState` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |

Object boundaries fail if code keeps old names for the same concepts. m5-wiki
uses static tests to reject old names after the rebuild. This TDD gives our wiki
the same language contract so shared code can move between repos.

## Goals

- Define one `DomainTerm` and one `CodeName` for core concepts.
- Make internal code use `CodeName`.
- Make prompts and docs use `DomainTerm`.
- Make generated frontmatter use `CodeName`.
- Add static tests that reject `ForbiddenSynonym` patterns.
- Keep the static tests portable to m5-wiki.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not add new domain behavior.
- This TDD does not preserve old generated page content.
- This TDD does not change CLI command names.
- This TDD does not add global planning.

Forbidden approaches:

- Do not use `name` for page identity.
- Do not use `category` for page kind.
- Do not use `path` for `SourceLocator`.
- Do not use `content` for `PageBody`.
- Do not duplicate page kind constants outside `Schema`.
- Do not whitelist a synonym without defining a new concept.

## Requirements

- `docs/domain-vocabulary.md` must contain the `DomainTerm` and `CodeName` table.
- Core code must use `page_id`.
- Core code must use `page_kind`.
- Core code must use `page_body`.
- Core code must use `source_locator`.
- Core code must use `lint_finding`.
- `ToolDTO` fields must use `CodeName`.
- Prompt text for planned writes must use `DomainTerm`.
- Static tests must scan `CoreBoundary` files.
- Static tests must reject listed `ForbiddenSynonym` patterns.
- Static tests must allow non-domain uses only through explicit path exclusions.

## Invariants

- `raw/` remains immutable.
- `GeneratedWikiState` remains disposable.
- Runtime profile names remain outside domain language tests.
- `PageMetadata.page_id` remains page identity.
- `WikiStructure` remains the `PagePath` authority.
- `Schema` remains the `PageKind` authority.

## Proposed Architecture

The test suite gains a static language gate. The gate runs beside domain tests
and fails before runtime workflows execute.

```
+------------------+     +------------------+
| Domain vocabulary|---->| Static tests     |
+------------------+     +--------+---------+
                                  |
                                  v
+------------------+     +--------+---------+
| CoreBoundary     |---->| shared language  |
+------------------+     +------------------+
```

`Domain vocabulary` owns approved terms.
`Static tests` enforce approved names.
`CoreBoundary` files expose shared domain language.
`shared language` is the tested term set shared by both repos.

## Key Interactions

### ToolDTO Check

```
Static test -> ReadPageParams: expect page_id
Static test -> WritePageParams: expect page_id, page_kind, page_body
Static test -> ReadSourceParams: expect source_locator
```

### Forbidden Synonym Check

```
Static test -> CoreBoundary text -> ForbiddenSynonym
ForbiddenSynonym -> test failure
```

## Data Model

| DomainTerm | CodeName |
|---|---|
| `PageId` | `page_id` |
| `PageKind` | `page_kind` |
| `PagePath` | `page_path` |
| `PageBody` | `page_body` |
| `PageMetadata` | `page_metadata` |
| `DomainFrontmatter` | `domain_frontmatter` |
| `GeneratedWikiState` | `generated_wiki_state` |
| `SourceLocator` | `source_locator` |
| `RawSource` | `raw_source` |
| `SourceBundle` | `source_bundle` |
| `Schema` | `schema` |
| `WikiStructure` | `wiki_structure` |
| `IngestRun` | `ingest_run` |
| `PagePlan` | `page_plan` |
| `SourcePlan` | `source_plan` |
| `PlannedPageWrite` | `planned_page_write` |
| `Evidence` | `evidence` |
| `IndexEntry` | `index_entry` |
| `LogEntry` | `log_entry` |
| `LintRun` | `lint_run` |
| `LintFinding` | `lint_finding` |

Forbidden synonyms:

- `name` for `PageId`.
- `category` for `PageKind`.
- `content` for `PageBody`.
- `path` for `SourceLocator`.
- `source_path` for `SourceLocator`.

## APIs / Interfaces

- `ReadPageParams` exposes `page_id`.
- `WritePageParams` exposes `page_id`, `page_kind`, `summary`, `sources`, and `page_body`.
- `ReadSourceParams` exposes `source_locator`.
- `render_page` emits `DomainFrontmatter`.
- `compute_findings` returns `LintRun`.
- `docs/domain-vocabulary.md` records all approved terms.

## Behavior & Domain Rules

Rule: tool DTOs use `CodeName`.

Example: input `ReadPageParams.model_fields` -> expected `{"page_id"}`.

Example: input `WritePageParams.model_fields` -> expected no `name`, `category`, or `content`.

Rule: core files reject old synonyms.

Example: input `params.category` in `tools.py` -> expected static test failure.

Ugliest edge case: input docs say `page name` while code says `page_id` -> expected docs change or explicit new concept.

## Acceptance Criteria

- `harness/tests/test_domain_language_consistency.py` exists.
- Static tests scan domain, store, workflow, runtime, and prompt files.
- Static tests reject `PAGE_CATEGORIES`.
- Static tests reject `validate_page_name`.
- Static tests reject `validate_category`.
- Static tests reject `params.name`.
- Static tests reject `params.category`.
- Static tests reject `params.content`.
- Static tests reject `params.path` for raw source reads.
- DTO field tests match m5-wiki assertions.
- `docs/domain-vocabulary.md` contains the `DomainTerm` and `CodeName` table.
- `uv run pytest harness/tests/test_domain_language_consistency.py` passes.

## Cross-Cutting Concerns

Testing: static tests enforce language before model workflows run.

Documentation: prompts and TDDs use `DomainTerm` when they describe behavior.

Portability: the static test file must keep the same test names and forbidden synonym table as m5-wiki.

## Reference Implementations

- m5 static tests: `~/gits/llm-wiki-m5-24gb/harness/tests/test_domain_language_consistency.py`.
- m5 language TDD: `~/gits/llm-wiki-m5-24gb/docs/2026-06-19-domain-language-consistency.md`.
- our vocabulary: `docs/domain-vocabulary.md`.
- our current tools: `harness/src/llmwiki/workflows/tools.py`.

## Alternatives Considered

- Chosen: static tests, because reviewer discipline does not stop drift.
- Rejected: comments only, because comments cannot fail CI.
- Rejected: broad regex over all files, because prose examples need exclusions.
- Rejected: allow old tool field aliases, because generated state is disposable.

## Halt Conditions

- If a forbidden synonym is needed for a new concept, stop and define it.
- If m5-wiki uses a different `CodeName`, stop and reconcile the shared table.
- If a static test blocks runtime-only code, stop and narrow the checked files.
