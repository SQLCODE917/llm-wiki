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
   - Verifies lint outcomes with a deterministic post-pass so `wiki-health`
     and `log.md` never depend only on the model's self-report when the
     harness can measure the result.
   - Reports deterministic lint deltas so resolved and remaining findings are
     visible without trusting the model narrative.
   - Adds a deterministic orphan-link helper so lint can repair graph-only
     findings without rewriting whole pages.
   - Retires backup references for landed evidence features.

## Follow-On TDDs

These are deferred backup ideas that now have fresh M5-shaped designs. They are
not part of the completed 4090 synthesis chain, but they are aligned with the
REFERENCE pattern and can be implemented independently.

1. `docs/2026-06-14-maintenance-automation-curator-status.md`
   - Adds model-free curator status and filed maintenance reports.
   - Makes routine wiki health inspection cheap without invoking repair.

2. `docs/2026-06-14-contradiction-detection.md`
   - Adds bounded, model-assisted contradiction audits.
   - Files structured contradiction reports without auto-resolving conflicts.

## Global Constraints

- `raw/` remains immutable.
- Wiki content is written only through `write_page`.
- `index.md`, `log.md`, frontmatter, salience, chat windows, and transcripts
  remain deterministic harness-owned bookkeeping.
- Lint success is never only model-reported when the harness can recompute the
  affected fact. The model may repair pages, but link/index/orphan and citation
  evidence state must be measured before and after the model pass.
- For orphan repairs, the model chooses the relationship and the harness should
  perform the mechanical link insertion. Do not ask the model to rewrite a
  whole page merely to add one graph edge.
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

The synthesis is complete when the first three TDDs are implemented, the 4090
path can run at least one real wiki operation through Ollama and the harness,
evidence strictness is available as an opt-in gate, lint reports include
deterministic post-pass verification, and `AGENTS.md` no longer names backup
files as active porting targets except for explicitly deferred work.
