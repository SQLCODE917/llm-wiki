# Local LLM-Wiki on Qwen3-14B — Design

## Context & Problem

`docs/llm-wiki.md` describes the target pattern: an LLM incrementally builds and
maintains a persistent wiki of interlinked markdown pages over a collection of
immutable raw sources, governed by a schema document, via three operations
(ingest, query, lint). Today this repo has the inference engine (llama.cpp,
built) and the reliability layer (forge, cloned) but no wiki, no schema, and no
harness connecting Qwen3-14B to the filesystem. A 14B model at Q4 cannot be
trusted with open-ended agency; without guardrails, tool-calling workflows
degrade badly (forge's evals: as low as 4% completion without its respond-tool
guardrail).

## Goals

- Instantiate all three layers from `docs/llm-wiki.md` on local disk: immutable
  `raw/`, LLM-maintained `wiki/` with `index.md` and `log.md`, and a `SCHEMA.md`
  conventions document.
- All three operations runnable from one CLI: `ingest <source>`, `query
  "<question>"`, `lint` — each completing reliably against local Qwen3-14B.
- Wiki maintenance is the model's job; bookkeeping correctness (index entries,
  log append, link integrity checks) is guaranteed by deterministic code, not
  model discipline.
- Use forge as a direct dependency (WorkflowRunner) — no re-implementation of
  retry, rescue parsing, step enforcement, or compaction.
- Everything in user space; runs in ~17 GB Metal budget (8.4 GB weights +
  16K-token KV cache).

## Non-Goals

- Embedding/vector search (index-first navigation suffices at this scale, per
  the alignment doc; revisit via qmd if the wiki outgrows it).
- Multi-user access, web UI, or daemonized serving (Obsidian or any editor is
  the read-side UI).
- Image ingestion, Marp decks, Dataview frontmatter queries (modular extras in
  the pattern; deferred).
- Batch ingestion of many sources in one run (one source per ingest, per the
  alignment doc's recommended supervised flow).

## Requirements

- **Alignment**: raw sources are never modified; every ingest/query/lint leaves
  `index.md` and `log.md` current; answers worth keeping can be filed back into
  the wiki. These are the load-bearing invariants of `docs/llm-wiki.md`.
- **Hardware**: M5 / 24 GB unified memory; no root. Model + KV must stay inside
  the ~17–18 GB Metal allocation.
- **Model reality**: Qwen3-14B Q4_K_M needs forge's full guardrail stack —
  synthetic respond tool, step enforcement, prerequisites, tiered compaction,
  card-recommended sampling (already keyed as `Qwen3-14B-Q4_K_M` in forge).
  Live testing added one refinement: per-operation retry nudges that name the
  terminal tool, because the model's dominant failure mode is reporting
  completion in bare text instead of calling it (forge ADR-013).
- **Determinism boundary**: the model authors content (pages, summaries,
  cross-references); the harness performs filesystem effects and bookkeeping.

## Proposed Architecture

The harness (`harness/`, package `llmwiki`) is the orchestrator. It loads
`SCHEMA.md` into the system prompt, exposes a small set of wiki tools to the
model, and drives each operation as a forge `Workflow` with required steps and
a terminal tool. Forge owns the loop (validation, rescue, nudges, compaction);
llama-server serves Qwen3-14B; the wiki store adapter is the only component
that touches disk, and it refuses writes outside `wiki/`.

This serves the alignment doc directly: the wiki layer is written exclusively
by the model through `write_page`; `raw/` is mounted read-only behind
`read_source`; index and log updates happen deterministically on every write
and workflow completion, so navigation files can never go stale.

```
+--------+   ingest/query/lint   +-----------------+
|  User  |---------------------->|  llmwiki CLI /  |
| (CLI)  |<---answers/reports----|  orchestrator   |
+--------+                       +--------+--------+
                                          | workflows + tools
                                          v
+-----------+  conventions   +------------------------+
| SCHEMA.md |--------------->|  forge WorkflowRunner  |
+-----------+ system prompt  |  (guardrails, compact) |
                             +-----------+------------+
                                         | OpenAI-compat API
                                         v
+-----------+  read_source   +------------------------+
|   raw/    |· · · · · · · ·>|  llama-server          |
| immutable |    (via tools) |  Qwen3-14B Q4_K_M      |
+-----------+                +------------------------+
                                         |
                             tool effects v (wiki store adapter)
                             +------------------------+
                             |  wiki/  + index.md     |
                             |  + log.md              |
                             +------------------------+
```

Component responsibilities, one line each:

- **llmwiki CLI / orchestrator** — parses commands, boots the backend via
  forge `setup_backend`, selects the workflow, appends the log entry on
  completion.
- **forge WorkflowRunner** — runs the agentic loop with rescue parsing, retry
  nudges, step enforcement, prerequisites, and TieredCompact.
- **llama-server / Qwen3-14B** — local inference, native function calling
  (`--jinja`), card-recommended sampling via forge.
- **Wiki store adapter** — validated filesystem boundary: page read/write,
  search, deterministic index maintenance; rejects paths outside `wiki/`.
- **SCHEMA.md** — page conventions, linking rules, and per-operation workflow
  instructions; rendered into the model's system prompt.
- **raw/** — immutable source documents, read-only to the model.
- **wiki/ + index.md + log.md** — the compounding artifact the user reads.

## Key Interactions

Ingest (touches the most surface — required steps, prerequisites, index/log):

```
User          Orchestrator        Runner/Qwen3           Wiki store
 |--ingest s--->|                     |                     |
 |              |--run(ingest, s)---->|                     |
 |              |                     |--read_source(s)---->| (raw/, read-only)
 |              |                     |<---source text------|
 |              |                     |--search/read pages->| (find related)
 |              |                     |--write_page(p,sum)->| writes wiki/p.md
 |              |                     |                     | + index entry
 |              |                     |  (repeat for affected pages)
 |              |<--finish_ingest(s)--|                     |
 |              |--append log entry------------------------>|
 |<--summary----|                     |                     |
```

Query (index-first navigation; answers can be filed back):

```
User          Orchestrator        Runner/Qwen3           Wiki store
 |--query q---->|                     |                     |
 |              |--run(query, q)----->|                     |
 |              |                     |--search_wiki(q)---->| index + page hits
 |              |                     |--read_page(...)---->| drill into pages
 |              |                     |--write_page(...)--->| (only if worth
 |              |                     |                     |  keeping, per
 |              |<----respond(ans)----|                     |  SCHEMA.md)
 |              |--append log entry------------------------>|
 |<--answer+cites|                    |                     |
```

Lint runs deterministic checks first (broken `[[links]]`, orphan pages, index
drift — pure code, no model), then hands the findings to the model to review
flagged pages for contradictions and missing cross-references, terminating in a
`finish_lint` report that is filed as the harness-maintained `wiki-health`
synthesis page (rewritten each pass and exempt from orphan checks, since
nothing links to it by construction) and logged.

## Data Model

- **Source** — file in `raw/`; identity is its relative path; never mutated.
- **WikiPage** — markdown file in `wiki/`; frontmatter (`category`,
  `summary`, `sources`, `updated`) composed by the harness, never written by
  the model; body uses `[[page-name]]` links. Name is a kebab-case slug,
  unique.
- **IndexEntry** — one line per page in `index.md`, grouped by category
  (sources, entities, concepts, syntheses): link + one-line summary.
- **LogEntry** — append-only line group in `log.md` with grep-able prefix
  `## [YYYY-MM-DD] <op> | <subject>`.

Access patterns: query reads `index.md` first, then drills into pages (no
embeddings); lint walks the `[[link]]` graph from page bodies; `write_page`
upserts the page's IndexEntry in the same operation.

## APIs / Interfaces

CLI (the only human-facing interface):

- `llmwiki ingest <path-in-raw>` — integrate one source into the wiki.
- `llmwiki query "<question>"` — answer from the wiki with citations.
- `llmwiki lint` — health-check; deterministic checks + model review.

Tools exposed to the model (per-workflow subsets, kept small for a 14B):

- `read_source(path)` — return raw source text (ingest only).
- `search_wiki(query)` — index + full-text hits with snippets.
- `read_page(name)` — full page text.
- `write_page(name, summary, content)` — write page; harness upserts index.
- `finish_ingest(summary)` / `finish_lint(report)` — terminal tools.
- `respond(message)` — forge's synthetic respond tool; terminal for query.

Workflow contracts: ingest requires `read_source` and at least one
`write_page` before `finish_ingest`, with `write_page` gated on a prior
`read_source`; query requires `search_wiki` before `respond`.

## Cross-Cutting Concerns

- **Error handling** — forge's fail-fast philosophy carries through: typed
  exceptions (`ToolCallError`, `StepEnforcementError`) surface to the CLI with
  context; no silent fallbacks. A failed ingest writes no log entry and reports
  partial page writes honestly.
- **Observability** — `on_message` callback streams the full conversation to a
  per-run transcript file under `harness/runs/`, so any wiki edit is traceable
  to the model turn that produced it.
- **Context budget** — 16K context via llama-server `-c`; forge TieredCompact
  with recent-iteration protection. Sources larger than the per-tool read
  budget are truncated with an explicit marker (chunked ingest is an open
  question below).
- **Auth** — none; single local user, server bound to localhost.

## Alternatives Considered

- **forge proxy + Claude Code as maintainer** — rejected: wiki workflows need
  step enforcement and prerequisites, which only WorkflowRunner carries.
- **Re-implementing guardrails in the harness** — rejected: CLAUDE.md treats
  re-implementation of a maintained library as a workaround.
- **Embedding-based RAG search** — rejected: alignment doc's index-first
  navigation works at this scale; qmd is the upgrade path.
- **Ollama backend** — rejected: llama.cpp is already built from source here;
  one fewer runtime.
- **Bigger model (27B+)** — rejected: doesn't fit the ~17 GB Metal budget with
  useful context headroom.

## Open Questions / Risks

- **Large sources** — single-pass ingest is bounded by the 16K context;
  sources beyond the read budget need a chunked map-then-integrate flow.
  Deferred until a real source hits the limit.
- **Thinking mode cost** — Qwen3 reasoning improves integration quality but
  burns context; default is thinking on for ingest/lint, `/no_think` for
  query. Needs tuning against real usage.
- **Index scaling** — at hundreds of pages the flat index may exceed what the
  model can scan; qmd (BM25/vector, local) is the designated escape hatch.
- **Schema co-evolution** — SCHEMA.md is meant to be revised as usage reveals
  what works; revisions are logged in `log.md` like any other operation.
