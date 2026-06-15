# Wiki Graph Export

## Context & Problem

The reference pattern highlights Obsidian graph view and interlinked markdown as
core strengths. Current M5 computes link findings but does not persist a
machine-readable graph. The backup had `_graph.json`; a flat-wiki M5 export
would help audits and future tools without changing the page schema.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "I browse the results in real time"
- "`index.md` is content-oriented"
- "Obsidian's graph view is the best way to see the shape of your wiki"
- "Updating cross-references ... makes a knowledge base actually useful"

## Goals

- Generate a deterministic graph artifact from current wiki pages.
- Include node metadata needed for curator review.
- Let maintenance check whether the graph is current.
- Keep `index.md` and `log.md` as the required navigation files.

## Non-Goals & Forbidden Approaches

Non-goals:

- No graph database.
- No Obsidian plugin.
- No model-authored graph JSON.
- No replacement for `index.md`.

Forbidden approaches:

- Do not store graph edges in page frontmatter.
- Do not make the model maintain `_graph.json`.
- Do not restore old type-directory node IDs.

## Requirements

- Graph export is derived entirely from `wiki/*.md` content and frontmatter.
- Nodes include page name, category, summary, sources, and outbound links.
- Missing link targets are represented or reported deterministically.
- The export is stable across runs when inputs do not change.
- Maintenance can report stale or missing graph export.

## Invariants

- Wiki pages remain the source of truth.
- `index.md` and `log.md` remain human/model navigation primitives.
- Graph export is harness-owned bookkeeping.

## Proposed Architecture

```
+---------+       +--------------+       +--------------+
| wiki/md |------>| graph builder|------>| graph artifact|
+---------+       +--------------+       +--------------+
                         |
                         v
                  maintenance check
```

Graph builder parses existing pages. The artifact is written by the harness.
Maintenance checks freshness by recomputing it.

## Key Interactions

Generate:

```
CLI -> graph builder: page texts
Builder -> artifact: deterministic JSON
CLI -> log.md: optional graph refresh entry
```

Check:

```
maintenance -> graph builder: recompute
maintenance -> report: current/stale/missing
```

Broken link:

```
Builder -> graph: edge to missing target marked unresolved
Lint    -> report: same broken link through existing findings
```

## Data Model

- Artifact path: `wiki/wiki-graph.json` or another harness-owned name chosen
  consistently with system pages.
- Node key: page name.
- Edge: source page name, target page name, resolved boolean.
- Metadata: generated date, schema version, generator name.

## APIs / Interfaces

- New CLI command: `llmwiki graph`.
- Option: `--check` fails if the artifact is stale.
- Maintenance report includes graph artifact status.

## Behavior & Domain Rules

- The same wiki state always renders the same graph JSON except generated date
  if the date is included in metadata.
- System pages may be included with a flag or excluded consistently; the choice
  must be documented in the graph metadata.
- Broken links are not hidden.

Examples:

- `array` links to `function` -> edge is resolved.
- `array` links to `ghost` -> edge is unresolved and lint still reports broken.
- No page changes since last graph -> `llmwiki graph --check` passes.

## Acceptance Criteria

- Tests prove deterministic graph output from sample pages.
- Tests prove broken links are represented or reported.
- Tests prove `--check` detects stale output.
- Curator status reports graph missing/stale/current.
- Graph artifact is exempt from page parsing and orphan checks.

## Cross-Cutting Concerns

Versioning: include a graph schema version so future tools can detect incompatible
changes.

## Reference Implementations

- Current link parsing: `harness/src/llmwiki/domain/links.py`.
- Current system pages: `harness/src/llmwiki/domain/system_pages.py`.
- Backup graph idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_graph.py`.

## Alternatives Considered

- Rely only on Obsidian graph view - rejected because tooling needs a file it can
  diff and validate.
- Store graph in SQLite - rejected because the wiki is markdown-first.

## Halt Conditions

- If the graph artifact name conflicts with Obsidian or existing wiki pages,
  stop and choose a different harness-owned filename.
