# Workflow Guardrails for Index-First Wiki Maintenance

## Context & Problem

`docs/llm-wiki.md` says ingest integrates a source into the existing wiki and
query reads the index, then drills into relevant pages. Current workflows mostly
prompt for that behavior, but their enforced steps allow plain ingest to skip
wiki search and allow query to answer from search snippets without reading a
full page.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "updates relevant entity and concept pages across the wiki"
- "The LLM searches for relevant pages, reads them"
- "When answering a query, the LLM reads the index first"
- "then drills into them"

## Goals

- Enforce current-wiki consultation during ingest.
- Enforce page reading before query answers.
- Preserve the useful index-first path for questions about wiki coverage.
- Keep chat behavior unchanged in this TDD.

## Non-Goals & Forbidden Approaches

Non-goals:

- No qmd or embedding search.
- No changes to chat Phase 1.
- No changes to page schema.

Forbidden approaches:

- Do not rely only on prompt wording for required navigation steps.
- Do not force `read_page("index")`; `index.md` is not a normal page.
- Do not make `read_index` mandatory for every query if `search_wiki` already
  found and the model read a content page.

## Requirements

- Plain ingest cannot call `write_page` until `read_source` and `search_wiki`
  have both completed.
- Query cannot call `respond` until either `read_page` or `read_index` has
  completed after the user question is received.
- Query answers about wiki coverage can satisfy the drill-down requirement with
  `read_index`.
- Existing PDF map/integrate guardrails keep their current semantics unless a
  test proves they need the same stricter rule.

## Invariants

- Raw sources remain read-only.
- `write_page` remains the only model-write tool for content pages.
- The harness still owns `index.md` and `log.md`.
- The model can still file synthesis pages from `query`.

## Proposed Architecture

```
+---------+       +----------------+       +-------------+
| CLI op  |------>| Forge workflow |------>| Wiki tools  |
+---------+       +----------------+       +-------------+
                         |
                         v
                  required steps
```

The CLI remains thin. Workflow definitions own operation guardrails. Tools keep
their existing contracts.

## Key Interactions

Plain ingest:

```
Model -> read_source: raw/article.md
Model -> search_wiki: related terms
Model -> write_page: source/concept updates
Model -> finish_ingest: report
```

Query with content pages:

```
Model -> search_wiki: question terms
Model -> read_page: relevant page
Model -> respond: cited answer
```

Query about wiki coverage:

```
Model -> read_index: catalog
Model -> respond: coverage answer
```

## Data Model

No persistent data model changes.

## APIs / Interfaces

- `build_ingest_workflow` required steps include `read_source`, `search_wiki`,
  and `write_page`.
- `build_query_workflow` enforces a pre-response read of either `read_page` or
  `read_index`.
- Query does not force `search_wiki` after a successful `read_index`: coverage
  answers should be able to follow the pattern document's index-first path
  without a corrective nudge that sends the model into tangential search.
- `SCHEMA.md` mirrors this contract so the standing workflow instructions do
  not contradict the harness guardrail.
- Tool names remain unchanged.
- Forge only supports conjunctive prerequisite lists, so the query disjunction
  is implemented as a harness-owned `respond` wrapper that keeps the public
  tool name and schema unchanged while rejecting snippet-only answers.

## Behavior & Domain Rules

- Searching the wiki is part of ingest, not an optional courtesy.
- A search snippet is not sufficient evidence for a final query answer.
- The index can answer questions about catalog/coverage but not detailed source
  claims.

Examples:

- Ingest script calls `read_source`, then `write_page` -> write is blocked until
  `search_wiki`.
- Query script calls `search_wiki`, then `respond` -> response is blocked until
  `read_page` or `read_index`.
- Query asks "what is this wiki about?", calls `read_index`, then `respond` ->
  allowed.
- Query asks "what is this wiki about?", reads the index, then writes a new
  topical synthesis page -> discouraged by prompt because catalog/status
  answers are not durable syntheses.

## Acceptance Criteria

- Tests prove ingest write is blocked before `search_wiki`.
- Tests prove query response is blocked before `read_page` or `read_index`.
- Tests prove query can answer from `read_index` for coverage questions.
- Existing ingest/query happy-path tests still pass after adding required reads.
- `uv run pytest harness/tests/test_session_e2e.py harness/tests/test_domain.py`
  passes.

## Cross-Cutting Concerns

Error handling: rely on forge step/prerequisite errors so the local model can
self-correct in the next tool turn.

Implementation note: ingest uses Forge prerequisites directly
(`write_page` requires `read_source` and `search_wiki`). Query tracks successful
`read_page` and `read_index` calls in the run and lets `respond` succeed only
after one of them has happened.

## Reference Implementations

- Workflow definitions: `harness/src/llmwiki/workflows/definitions.py`.
- Query prompt: `harness/src/llmwiki/workflows/prompts.py`.
- E2E guardrail tests: `harness/tests/test_session_e2e.py`.

## Alternatives Considered

- Prompt-only instruction - rejected because live local-model behavior already
  proved prompts are weaker than tool contracts.
- Always require `read_index` first - rejected because search-first content
  questions are already useful and cheaper.

## Halt Conditions

- If forge cannot express "read_page OR read_index" as a required pre-response
  condition, stop and design a small wrapper tool or enforcement extension
  before implementing a workaround.

Resolved: Forge prerequisites are conjunctive only. The selected enforcement
extension is `respond_after_wiki_read_tool`, a narrow wrapper around Forge's
synthetic `respond` tool.
