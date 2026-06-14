# 4090 Feature Synthesis Roadmap

## Context

The repo now uses the M5 foundation: a `uv` Python harness, `forge` workflows,
flat `wiki/*.md` pages, deterministic `index.md`/`log.md`, PDF chunking, and
persistent chat. The backup repo contains useful local 4090 wiring and strict
evidence/lint machinery, but copying it wholesale would restore the old
pipeline the migration intentionally left behind.

This document is the chain of independently shippable TDDs. It is not the TDD
for all work at once.

## Delivery Chain

1. `docs/2026-06-14-runtime-profiles-4090.md`
   - Standardizes on Ollama as the single active local LLM provider and makes
     `local-4090` a first-class target.
   - Keeps all operations inside `forge` workflows and harness tools.
   - Blocks later GPU work until runtime identity is explicit and tested.

2. `docs/2026-06-14-strict-citation-parser.md`
   - Ports the useful citation/locator ideas from the backup into the flat M5
     wiki model.
   - Produces deterministic findings only; it does not fail writes or lint yet.
   - Blocks evidence-aware writes until citation parsing is stable.

3. `docs/2026-06-14-evidence-gates-for-writes-and-lint.md`
   - Wires citation findings into `write_page` and `lint` behind
     `off|warn|fail` strictness.
   - Preserves normal wiki synthesis by defaulting strictness to `off`.
   - Retires backup references for landed evidence features.

## Global Constraints

- `raw/` remains immutable.
- Wiki content is written only through `write_page`.
- `index.md`, `log.md`, frontmatter, salience, chat windows, and transcripts
  remain deterministic harness-owned bookkeeping.
- The backup tree remains reference-only and ignored by git.
- The flat `wiki/*.md` page model remains canonical.
- Existing commands keep their names: `llmwiki ingest`, `llmwiki query`,
  `llmwiki chat`, and `llmwiki lint`.

## Rejected Restorations

- Do not restore the old `packages/wiki_core`, `packages/wiki_io`,
  `packages/wiki_llm`, or `tools/` layout as active architecture.
- Do not restore the old type-directory wiki schema.
- Do not make evidence IDs mandatory on every page.
- Do not use direct `codex exec` as the operation runner for wiki edits.
- Do not keep parallel active providers in the harness. Keep a swappable
  provider boundary, but implement Ollama first.

## Completion Signal

The synthesis is complete when the three TDDs are implemented, the 4090 path can
run at least one real wiki operation through Ollama and the harness, evidence
strictness is available as an opt-in gate, and `AGENTS.md` no longer names
backup files as active porting targets except for explicitly deferred work.
