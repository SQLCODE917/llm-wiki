# Shared Object Boundaries

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `PageId` | Stable page identity independent of file location. |
| `PageKind` | Schema-approved page type. |
| `PageMetadata` | Page identity, summary, sources, and update date. |
| `PageMetadataField` | Schema-approved metadata key for one `WikiPage`. |
| `DomainFrontmatter` | Generated markdown metadata rendered from `PageMetadata`. |
| `PageBody` | Markdown body of one `WikiPage`. |
| `WikiPage` | One page with `PageMetadata` and `PageBody`. |
| `PagePath` | Rendered location of one `WikiPage` inside `wiki/`. |
| `WikiStructure` | Domain object that renders `PagePath` from `PageMetadata`. |
| `SourceLocator` | Raw source identity relative to `raw/`. |
| `RawSource` | Immutable source loaded from `raw/`. |
| `SourceBundle` | Non-empty set of `RawSource` records for one run. |
| `Schema` | Wiki configuration for page kinds and metadata fields. |
| `IngestRun` | One ingest operation over one `SourceBundle`. |
| `IndexEntry` | Deterministic index row for one `WikiPage`. |
| `PathTemplate` | Template that maps `PageMetadata` to `PagePath`. |
| `GeneratedWikiState` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |

Our wiki still exposes old page and source terms at core boundaries. m5-wiki has
stronger object boundaries around `PageMetadata`, `WikiStructure`, `WikiPage`,
`RawSource`, `SourceBundle`, `Schema`, and `IngestRun`. This TDD ports those
boundaries into our wiki first. Later TDDs build on this shared domain surface.

## Goals

- Make `PageMetadata` the page identity authority.
- Make `WikiStructure` the only `PageMetadata` to `PagePath` interface.
- Make `WikiPage` contain `PageMetadata` and `PageBody`.
- Make `RawSource.source_locator` the raw source identity.
- Make `SourceBundle` own source selection for `IngestRun`.
- Make `Schema` own `PageKind` and `PageMetadataField` values.
- Make generated frontmatter use domain code names.
- Keep domain files portable to m5-wiki.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not add global ingest planning.
- This TDD does not add page body contracts.
- This TDD does not add source claim coverage.
- This TDD does not add a database.
- This TDD does not preserve old generated frontmatter.

Forbidden approaches:

- Do not infer `PageKind` from `PagePath`.
- Do not store page identity as `name`.
- Do not store page kind as `category`.
- Do not store raw source identity as `path`.
- Do not keep old frontmatter adapters after rebuild.
- Do not add 4090 or M5 runtime logic to domain modules.

## Requirements

- `PageMetadata` must contain `page_id`, `page_kind`, `summary`, `sources`, and `updated`.
- `WikiPage` must contain `page_metadata` and `page_body`.
- `DomainFrontmatter` must render `page_id`, `page_kind`, `summary`, `sources`, and `updated`.
- `parse_page` must parse only `DomainFrontmatter` after `GeneratedWikiState` rebuild.
- `WikiStructure` must render `PagePath` from `PageMetadata`.
- `LOCAL_FLAT_STRUCTURE` must render `{PageId}.md`.
- `Schema` must define `PAGE_KINDS`.
- `Schema` must define `PAGE_METADATA_FIELDS`.
- `RawSource` must use `source_locator`.
- `SourceBundle` must reject an empty `raw_sources` tuple.
- `WikiStore.write_page` must accept `WikiPage`.
- `IndexEntry` updates must consume `PageMetadata`.

## Invariants

- `raw/` remains immutable.
- `GeneratedWikiState` remains disposable.
- `PageMetadata.page_id` remains page identity.
- `PagePath` remains derived state.
- `WikiStore` remains the only component that writes markdown pages.
- `index.md` remains deterministic.
- `log.md` remains operation history.

## Proposed Architecture

The implementation ports m5-wiki's page and source object shape. Runtime code
continues to arrange work around those domain objects.

```
+-------------+     +--------------+     +-------------+
| RawSource   |---->| SourceBundle |---->| IngestRun   |
+-------------+     +------+-------+     +------+------+
                            |                    |
                            v                    v
                     +------+-------+     +------+------+
                     | WikiPage     |---->| PageMetadata|
                     +------+-------+     +------+------+
                            |                    |
                            v                    v
                     +------+-------+     +------+------+
                     | PageBody     |     | WikiStructure|
                     +--------------+     +-------------+
```

`RawSource` owns `SourceLocator` and source format.
`SourceBundle` owns source selection.
`IngestRun` owns unattended run state.
`WikiPage` owns `PageMetadata` and `PageBody`.
`WikiStructure` renders `PagePath`.

## Key Interactions

### Write A Page

```
write_page tool -> PageMetadata -> WikiPage -> WikiStructure
WikiStructure -> PagePath -> WikiStore -> DomainFrontmatter
```

### Read A Page

```
WikiStore -> DomainFrontmatter -> PageMetadata
WikiStore -> PageBody -> WikiPage
```

### Select A Source

```
CLI source argument -> RawSource -> SourceBundle -> IngestRun
```

## Data Model

| Object | Required fields |
|---|---|
| `PageMetadata` | `page_id`, `page_kind`, `summary`, `sources`, `updated` |
| `WikiPage` | `page_metadata`, `page_body` |
| `DomainFrontmatter` | `page_metadata` |
| `PathTemplate` | `template_text`, `match_page_kinds`, `required_page_metadata_fields` |
| `WikiStructure` | `structure_id`, `default_path_template`, `path_templates` |
| `RawSource` | `source_locator`, `source_format`, `source_content`, `source_assets`, `immutable` |
| `SourceBundle` | `raw_sources` |
| `Schema` | `schema_id`, `page_kinds`, `page_metadata_fields` |

## APIs / Interfaces

- The `parse_page` interface accepts markdown text and returns `WikiPage`.
- The `render_page` interface accepts `WikiPage` and returns markdown text.
- `WikiStore.read_wiki_page` accepts `page_id` and returns `WikiPage`.
- `WikiStore.write_page` accepts `WikiPage`, writes markdown, and updates `index.md`.
- `WikiStore.raw_source` accepts `source_locator` and returns `RawSource`.
- `upsert_index_entry` accepts index text and `PageMetadata`, then returns updated index text.

## Behavior & Domain Rules

Rule: `PageMetadata` owns page identity.

Example: input `page_id = closure` -> expected `PagePath = closure.md`.

Example: input nested `WikiStructure` -> expected `page_id` stays `closure`.

Rule: `GeneratedWikiState` rebuilds after frontmatter change.

Example: input old `category: concept` frontmatter -> expected rebuild with `page_kind: concept`.

Ugliest edge case: input old page parser requires both `name` and markdown text.
Expected outcome: implementation deletes generated state.

## Acceptance Criteria

- `WikiPage` constructor uses `PageMetadata` and `PageBody`.
- `DomainFrontmatter` renders `page_id` and `page_kind`.
- `DomainFrontmatter` renders no `name` or `category` fields.
- `WikiStructure` renders local flat `PagePath`.
- A nested `WikiStructure` renders from `PageMetadata` fields.
- A `RawSource` built from `article.md` returns source format `markdown`.
- A `SourceBundle` with empty `raw_sources` raises a domain error.
- `IndexEntry` tests consume `PageMetadata`.
- Static tests reject `validate_page_name`, `validate_category`, and `PAGE_CATEGORIES`.
- `uv run pytest harness/tests/test_domain.py harness/tests/test_store.py` passes.

## Cross-Cutting Concerns

Observability: run transcripts remain valid historical records after generated state rebuild.

Error handling: page and source validation errors must use m5-wiki domain names.

Portability: copied m5-wiki tests must need only import-path adjustments.

## Reference Implementations

- m5 page objects: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/pages.py`.
- m5 domain objects: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/objects.py`.
- m5 store boundary: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/store/wiki_store.py`.
- our current page objects: `harness/src/llmwiki/domain/pages.py`.
- our current store boundary: `harness/src/llmwiki/store/wiki_store.py`.

## Alternatives Considered

- Chosen: port m5 object names, because shared code needs shared terms.
- Rejected: keep old tool names, because static tests must enforce one language.
- Rejected: parse both old and new frontmatter, because generated state is disposable.
- Rejected: add a database, because markdown remains the persistence boundary.

## Halt Conditions

- If implementation needs old frontmatter support, stop and rebuild generated state.
- If implementation changes raw source layout, stop and ask.
- If implementation gives `PagePath` domain meaning, stop and ask.
- If our class names diverge from m5-wiki names, stop and choose one shared name.
