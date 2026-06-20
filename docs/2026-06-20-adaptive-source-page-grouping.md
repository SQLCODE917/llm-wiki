# Adaptive Source Page Grouping

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `ExtractedUnit` | Source-derived text unit with locator, heading path, and status. |
| `SourcePageGroup` | Ordered set of adjacent `ExtractedUnit` records for one source page. |
| `SourcePageGrouper` | Domain service that creates `SourcePageGroup` records. |
| `SourceHub` | Source page for the whole `RawSource`. |
| `SourceHubRenderer` | Domain service that adds `PageMap` links to `SourceHub`. |
| `PageMap` | Link list from `SourceHub` to source section pages. |
| `PageMapLink` | One link from `PageMap` to a grouped source page. |
| `PageLocatorCitation` | Citation string with `raw/` source path and page locator. |
| `SourceClaim` | Atomic statement extracted from one `ExtractedUnit`. |
| `ClaimEligibility` | Selection category for one `SourceClaim`. |
| `ClaimCentrality` | Score that compares a claim with an `ExtractedUnit.heading_path`. |
| `TopLevelHeading` | First heading segment in `ExtractedUnit.heading_path`. |
| `ParentHeading` | Heading segment that contains adjacent child headings. |
| `PagePlan` | Run-owned plan for page targets and serial writes. |
| `PlannedPageWrite` | One write, enrich, or defer action chosen by `PagePlan`. |
| `PageMetadata` | Page identity, summary, sources, and update date. |
| `PagePath` | Rendered location of one `WikiPage` inside `wiki/`. |
| `PageBody` | Markdown body of one `WikiPage`. |
| `WikiStructure` | Domain object that renders `PagePath` from `PageMetadata`. |
| `RawSource` | Immutable source file under `raw/`. |
| `Evidence` | Citation-backed support for a generated claim. |
| `IngestTopology` | Allowed write order for one ingest run. |
| `m5-wiki` | Sibling repo at `~/gits/llm-wiki-m5-24gb`. |

m5-wiki groups many extracted sections into source pages named with first and last headings.
That reduces page count, but it sometimes groups unrelated sections and weakens citations.
Our wiki keeps strong source-prefixed pages and `PageMap` navigation, but broad chunks mix claims.
This TDD adopts source page grouping as a `PagePlan` step and preserves locator citations.

## Goals

- Add `SourcePageGroup` as a planning object.
- Group only adjacent `ExtractedUnit` records from one `RawSource`.
- Prefer semantic section boundaries over fixed chunk counts.
- Preserve `PageLocatorCitation` values for grouped pages.
- Render `PageMap` on each `SourceHub`.
- Keep grouping code portable to m5-wiki.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not change PDF extraction.
- This TDD does not change claim classification.
- This TDD does not add a folder taxonomy.
- This TDD does not change source-summary body rendering.
- This TDD does not add parallel writes.

Forbidden approaches:

- Do not group units from different `RawSource` records.
- Do not group non-adjacent `ExtractedUnit` records.
- Do not use machine profile settings in grouping rules.
- Do not drop page locators from grouped source pages.
- Do not make `PagePath` an authority for grouping.

## Requirements

- `PagePlan` must create `SourcePageGroup` records before `PlannedPageWrite` records.
- Each `SourcePageGroup` must contain adjacent `ExtractedUnit` identifiers.
- Each `SourcePageGroup` must belong to one `RawSource`.
- Each `SourcePageGroup` must retain first heading, last heading, first locator, and last locator.
- The grouper must split when `TopLevelHeading` changes.
- The grouper must split when group token budget would exceed the configured limit.
- The grouper must split when group unit count would exceed the configured limit.
- The grouper must keep one-unit pages for existing section-specific pages.
- The grouper must keep one-unit pages for sections with eligible claims, `ClaimCentrality` greater than zero, and no shared `ParentHeading`.
- `PlannedPageWrite.page_metadata.sources` must include one `PageLocatorCitation` per unit in the group.
- `PlannedPageWrite.page_metadata.page_id` must include the source stem.
- Grouped page identifiers must use first heading and last heading.
- `SourceHub` must link every grouped source page through `PageMap`.
- `PageMap` labels must use human-readable heading text.
- `PageMap` must remain deterministic across cache-hit runs.

## Invariants

- `raw/` remains immutable.
- `Evidence` remains required for generated claims.
- `IngestTopology` remains `serial`.
- `PageMetadata.page_id` remains page identity.
- `WikiStructure` remains the only `PagePath` renderer.
- `index.md` and `log.md` remain harness-maintained files.
- Source page links remain Obsidian `[[page-id]]` links.

## Proposed Architecture

`SourcePageGrouper` creates `SourcePageGroup` records from ordered units.
`PagePlan` converts each `SourcePageGroup` into one source `PlannedPageWrite`.
`SourceHubRenderer` appends `PageMap` links after accepted hub summary content.

```
+---------------+     +-------------------+     +------------------+
| ExtractedUnit |---->| SourcePageGrouper |---->| SourcePageGroup  |
+---------------+     +-------------------+     +--------+---------+
                                                        |
                                                        v
                                               +-------------------+
                                               | PlannedPageWrite  |
                                               +---------+---------+
                                                         |
                                                         v
                                               +-------------------+
                                               | SourceHub PageMap |
                                               +-------------------+
```

## Key Interactions

Grouping flow:

```
ExtractedUnit order -> SourcePageGrouper -> SourcePageGroup
SourcePageGroup -> PageMetadata -> PlannedPageWrite
```

Existing page flow:

```
ExtractedUnit -> existing section page match -> one-unit SourcePageGroup
```

Hub navigation flow:

```
SourcePageGroup records -> SourceHubRenderer -> PageMap links
```

## Data Model

| Object | Required fields |
|---|---|
| `SourcePageGroup` | `source_page_group_id`, `raw_source`, `extracted_units`, `first_heading`, `last_heading`, `first_locator`, `last_locator`, `token_estimate` |
| `PageMap` | `source_id`, `links` |
| `PageMapLink` | `page_id`, `label`, `source_page_group_id` |

`SourcePageGroup.extracted_units` stores identifiers in source order.
`PageMap.links` stores links in source order.

## APIs / Interfaces

- `PagePlan` exposes `source_page_groups`.
- `PlannedPageWrite` records source-group membership through `extracted_units`.
- `observation_report` lists source page groups and planned source pages.
- `SourceHubRenderer` receives `PageMap` and accepted hub `PageBody`.
- `SourceHubRenderer` returns hub `PageBody` with `PageMap` links.

## Behavior & Domain Rules

Rule: source page groups preserve source order.

Example: input units 1, 2, and 3 from one source.
Expected outcome: the grouper emits one group containing 1, 2, and 3 in that order.

Example: input units 1 and 3 without unit 2.
Expected outcome: no group contains units 1 and 3 together.

Rule: semantic breaks beat throughput.

Example: input headings `Object.assign`, `Why?`, and `A Warm Cup` with no shared parent heading.
Expected outcome: the grouper emits separate groups.

Example: input Sword World front matter followed by character creation.
Expected outcome: the grouper emits separate groups.

Rule: grouped pages keep locator citations.

Example: input group has locators `p.30-31` and `p.31-33`.
Expected outcome: `PageMetadata.sources` contains both `PageLocatorCitation` values.

Rule: source hubs remain navigable.

Example: input source produces 20 grouped pages.
Expected outcome: `SourceHub` contains 20 `PageMap` links.

Ugliest edge case: input source has many short furniture sections at the end.
Expected outcome: the grouper groups adjacent furniture sections without dropping locators.

## Acceptance Criteria

Milestone 1: grouping tests.

- Tests cover `SourcePageGroup` creation from adjacent units.
- Tests prove groups do not cross `RawSource`.
- Tests prove groups do not skip units.
- Tests prove top-level heading changes split groups.
- Tests prove budget limits split groups.
- Tests prove existing section pages create one-unit groups.

Milestone 2: planning tests.

- Tests prove grouped source page identifiers include source stem.
- Tests prove grouped source page identifiers use first and last headings.
- Tests prove `PageMetadata.sources` includes locator citations for every grouped unit.
- Tests prove `PagePlan` persists `source_page_groups`.
- Tests prove observation report lists group counts.

Milestone 3: navigation tests.

- Tests prove `SourceHub` includes one `PageMap` link per source page group.
- Tests prove `PageMap` labels use heading text.
- Tests prove repeated cache-hit runs keep `PageMap` order.
- `uv run pytest harness/tests/test_planning.py harness/tests/test_pdf_session_e2e.py` passes.

## Cross-Cutting Concerns

Observability: the cache must retain `SourcePageGroup` records inside `PagePlan`.

Error handling: the planner must defer a group when `PageMetadata` cannot satisfy citation requirements.

Portability: grouping rules must use source structure and claim quality, not local hardware settings.

## Reference Implementations

- m5 grouping code: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/planning.py`.
- m5 grouped pages: `~/gits/llm-wiki-m5-24gb/wiki/javascriptallonge-*.md`.
- our page map behavior: `harness/src/llmwiki/workflows/fixed_page_tools.py`.
- our planning writes: `harness/src/llmwiki/domain/planning_writes.py`.
- our graph tests: `harness/tests/test_maintenance.py`.

## Alternatives Considered

- Chosen: adaptive grouping, because it balances page count and semantic focus.
- Rejected: one page per `ExtractedUnit`, because large books create noisy page sets.
- Rejected: fixed five-unit grouping, because unrelated sections share a page.
- Rejected: hub-only source pages, because readers need section-level navigation.

## Halt Conditions

- If grouping needs final `PagePath` values, stop and use `PageMetadata`.
- If grouping drops a unit locator, stop and fix citation construction.
- If JavaScript Allonge passes but Sword World fails, stop and add cross-source fixtures.
- If our wiki and m5-wiki need different group object names, stop and reconcile names.
