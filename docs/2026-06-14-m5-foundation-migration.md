# M5 Foundation Migration

## Context

The previous `llm-wiki` repo had a strong evidence-first ingestion pipeline:
typed packages, normalized raw sources, extraction state, stable evidence IDs,
claim judging, graph generation, and strict page schemas. That system was
valuable but heavy. It drifted toward a claim compiler rather than the lighter
LLM-maintained wiki pattern described in `docs/llm-wiki.md`.

The M5 repo proved a smaller foundation: flat Obsidian-friendly pages, `[[links]]`,
deterministic `index.md` and `log.md`, a `SCHEMA.md` prompt layer, `uv` package
management, `forge` workflows, persistent chat, and a PDF chunking pipeline
tested against `javascriptallonge.pdf`.

## Decision

Use the M5 repo as the foundation for this checkout.

The previous working tree is preserved at:

`backup/reference/llm-wiki-pre-m5-migration-2026-06-14/`

That folder is reference material only. Do not edit it and do not ingest from
it. Copy out specific ideas intentionally.

## Keep From The Previous Repo

- Local 4090/Codex wiring:
  - `packages/wiki_llm/src/wiki_llm/backends/codex.py`
  - `tools/wiki_model_defaults.json`
- Optional strict evidence gates for high-stakes or technical ingests:
  - locator parsing
  - stable evidence IDs
  - evidence excerpt validation
  - grounding checks
- Deterministic repair and lint ideas where they protect the M5 harness without
  reintroducing the old schema as the default.

## Do Not Restore By Default

- The old type-directory wiki layout (`wiki/sources`, `wiki/concepts`,
  `wiki/entities`, `wiki/procedures`, `wiki/references`, `wiki/analyses`).
- Mandatory evidence ID tables on every synthesized page.
- The pnpm-scripted multi-phase pipeline as the primary user interface.

## Current Foundation

- `SCHEMA.md` defines the live wiki conventions.
- `harness/src/llmwiki/` owns CLI workflows, stores, chat, PDF extraction, and
  deterministic bookkeeping.
- `uv run llmwiki ingest <source>` is the ingest path.
- `uv run llmwiki query "<question>"` is the one-shot query path.
- `uv run llmwiki chat` is the warm-model conversational path.
- `uv run llmwiki lint` is the health-check path.

## Next Port

The first serious migration follow-up should be an explicit backend design for
the 4090 environment. It should preserve the old `local-4090` Codex profile
behavior while keeping the M5 harness boundary: model operations go through
workflows and tools, and deterministic code owns bookkeeping.
