# Spec Alignment Polish

## Context & Problem

`docs/llm-wiki.md` is now the only pattern source of truth, but several repo
documents still mention the deleted duplicate `docs/REFERENCE_llm-wiki-pattern.md`.
There are also small user-facing mismatches: the README says chunked ingest is
not built, and `search_wiki` tells the model to use `read_page` for the index.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "The schema ... tells the LLM how the wiki is structured"
- "`index.md` is content-oriented"
- "`log.md` is chronological"
- "The exact directory structure ... will depend on your domain"

## Goals

- Remove all live references to the deleted reference copy.
- Make README feature status match the current harness.
- Make tool guidance name the correct index tool.
- Keep this change documentation/tool-text only.

## Non-Goals & Forbidden Approaches

Non-goals:

- No workflow behavior changes.
- No new commands or reports.
- No migration of old backup docs.

Forbidden approaches:

- Do not recreate `docs/REFERENCE_llm-wiki-pattern.md`.
- Do not keep dual-source wording like "`docs/llm-wiki.md` / reference copy".
- Do not edit backup/reference material.

## Requirements

- A search for the deleted reference-doc name over active repo files returns no
  live-current references outside backup and this TDD.
- `README.md` lists `docs/llm-wiki.md` as the only pattern document.
- README describes PDF chunked ingest as implemented if the current harness still
  contains `pdf_map` and `pdf_integrate` workflows.
- `search_wiki` no-hit text must point to `read_index`, not `read_page`.

## Invariants

- `docs/llm-wiki.md` remains unchanged by this polish unless the curator asks.
- `backup/reference/` remains read-only reference material.
- User-facing commands remain the same.

## Proposed Architecture

```
+----------------+      +------------------+
| docs/llm-wiki  |----->| active repo docs |
+----------------+      +------------------+
          |                       |
          v                       v
   source of truth        tool/help wording
```

`docs/llm-wiki.md` is the only pattern reference. Active repo docs and tool
help align their wording with that single source.

## Key Interactions

Doc verification:

```
Agent -> repo: rg deleted reference names
repo  -> Agent: only backup hits allowed
Agent -> docs: update stale wording
Agent -> tests: run focused docs/tool checks
```

Tool no-hit flow:

```
Model -> search_wiki: query with no hits
Tool  -> Model: "No pages matched... check the index with read_index"
Model -> read_index: inspect catalog
```

## Data Model

No data model changes.

## APIs / Interfaces

- `search_wiki` no-hit response is user/model-facing contract text.
- README design-document table contains a single pattern row for
  `docs/llm-wiki.md`.

## Behavior & Domain Rules

- Deleted compatibility-doc names are treated as stale active-doc references.
- Backup references are allowed because they describe historical state.

Examples:

- `README.md` says `docs/REFERENCE_llm-wiki-pattern.md` -> replace with
  `docs/llm-wiki.md`.
- `docs/2026-06-14-contradiction-detection.md` names the deleted pattern doc ->
  replace with `docs/llm-wiki.md`.
- `search_wiki` returns no hits -> response names `read_index`.

## Acceptance Criteria

- Active-doc search finds no deleted reference-doc references outside this TDD.
- Unit test or snapshot covers the `search_wiki` no-hit message.
- README no longer says chunked ingest is unbuilt while PDF workflows exist.
- `uv run ruff check harness/src harness/tests` passes.
- Relevant tests pass.

## Implementation Notes

- Active docs now name `docs/llm-wiki.md` as the only pattern source; the only
  active reference to the deleted duplicate is this TDD's own historical
  problem statement.
- README and `docs/writing-tdds.md` now point TDD readers at AGENTS.md instead
  of the old Claude-oriented schema file name.
- Local-model wording replaced stale 14B-specific user-facing guidance in the
  live README, AGENTS.md, and workflow prompt docstring.
- Chat prompt and SCHEMA.md now distinguish ordinary read-only chat from the
  explicit `/file` synthesis path.
- `search_wiki` already returned the correct `read_index` no-hit guidance, and
  `harness/tests/test_domain.py` already covers that contract.

## Verification

- `rg -n --glob '!backup/**' "REFERENCE_llm-wiki-pattern" .` returns only this
  TDD's historical context.
- `uv run ruff check harness/src harness/tests` passed.
- `uv run mypy harness/src` passed.
- `uv run pytest harness/tests` passed: 244 tests.
- `uv run llmwiki curator-status` completed and reported the graph export as
  current.
- `uv run llmwiki graph --check` passed: 75 nodes, 107 edges, 0 unresolved
  edges.

## Cross-Cutting Concerns

Observability: no new logs; this is a wording-only correction.

## Reference Implementations

- Pattern source: `docs/llm-wiki.md`.
- Search text: `harness/src/llmwiki/domain/search.py`.
- Existing parser tests: `harness/tests/test_domain.py`.

## Alternatives Considered

- Restore the duplicate reference doc - rejected because it reintroduces naming
  drift.
- Leave stale references until implementation work touches those docs -
  rejected because future agents follow these docs.

## Halt Conditions

- If any current code imports or reads the deleted reference doc, stop and ask
  before changing runtime behavior.
