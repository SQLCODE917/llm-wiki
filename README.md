# LLM-Wiki

A persistent, LLM-maintained knowledge base running entirely on this machine,
following Karpathy's LLM Wiki pattern (`docs/llm-wiki.md`): instead of
re-retrieving from raw documents on every question (RAG), a local model
**incrementally builds and maintains a wiki** of interlinked markdown pages.
Knowledge is compiled once and kept current — cross-references, contradiction
flags, and synthesis compound with every source added.

The maintainer model is **Qwen3-14B Q4_K_M** served by `llama-server`
(llama.cpp, Metal), driven through **forge**'s guardrailed `WorkflowRunner`
so a 14B model executes multi-step wiki maintenance reliably: step
enforcement, tool prerequisites, rescue parsing, retry nudges, and context
compaction.

This checkout was migrated onto the M5 foundation on 2026-06-14. The previous
repo is preserved as read-only reference material under
`backup/reference/llm-wiki-pre-m5-migration-2026-06-14/`; it is gitignored so
the backup is not accidentally committed.

Three layers (all invariants from the pattern hold by construction):

| Layer | Where | Who writes it |
|---|---|---|
| Raw sources (immutable) | `raw/` | You. The model can only read it. |
| The wiki | `wiki/` (+ `index.md`, `log.md`) | The model, via tools. Index/log bookkeeping is done deterministically by the harness, so they can never go stale. |
| The schema | `SCHEMA.md` | Conventions and workflows; rendered into the model's system prompt on every run. Co-evolves with usage. |

## How to Use it

Prerequisites (already satisfied on this machine — see the design doc for
how they were set up):

- `llama-server` on PATH (symlinked from `llama.cpp/build/bin/`).
- The Qwen3-14B Q4_K_M GGUF — auto-discovered in the Hugging Face hub cache
  (`~/.cache/huggingface/hub/models--Qwen--Qwen3-14B-GGUF/...`); override
  with `LLMWIKI_GGUF=/path/to/model.gguf`.
- The Python env: `uv` with the repo-root `.venv` (forge and the harness
  installed editable).

All commands run from the repo root. Each one boots `llama-server`, runs the
operation, appends to `wiki/log.md`, and shuts the server down.

**Ingest** — drop a source into `raw/`, then integrate it:

```bash
cp ~/Downloads/some-article.md raw/
uv run llmwiki ingest some-article.md
```

The model reads the source, searches the wiki for related pages, writes or
updates a `source` page plus affected `entity`/`concept` pages, and reports
what changed. Expect 5–10 minutes (~16 tok/s generation, thinking mode on).

**Query** — ask questions against the wiki:

```bash
uv run llmwiki query "Who studied the Antikythera mechanism, and how?"
```

Index-first navigation: search, read pages, answer with `[[page]]` and
`(raw/...)` citations. Answers worth keeping (comparisons, new syntheses)
are filed back into the wiki as `synthesis` pages before responding.

**Chat** — converse with the wiki, model loaded once for the whole session:

```bash
uv run llmwiki chat            # new conversation
uv run llmwiki chat --resume   # continue the most recent one
```

Follow-up questions work; `/new`, `/sessions`, and `/switch <id>` manage
multiple conversations; `/ingest` and `/lint` run inside chat on the warm
server; `/exit`, Ctrl-C, or Ctrl-D leave gracefully. Phase 1 is read-only —
answers cite the wiki but nothing is written back (filing is Phase 2).
History lives in `harness/chat.db` (verbatim, gitignored); conversations are
a throwaway playground, not a knowledge store.

**Lint** — periodic health check:

```bash
uv run llmwiki lint
```

Deterministic checks run first in code (broken `[[links]]`, orphan pages,
index drift); the model then reviews flagged pages, fixes what a page edit
can fix, and files its report as the `wiki-health` page.

**Reading the wiki**: it's just markdown — open `wiki/` in Obsidian (graph
view shows the link structure) or any editor. Recent activity:
`grep "^## \[" wiki/log.md | tail -5`. Every run writes a full conversation
transcript to `harness/runs/*.jsonl`, so any wiki edit is traceable to the
model turn that produced it.

**Knobs**: `LLMWIKI_GGUF` (model file), `LLMWIKI_PORT` (default 8080),
`LLMWIKI_CTX` (context tokens, default 16384). The previous repo's
`local-4090` Codex wiring is preserved in the migration reference and should
be ported as an explicit harness backend before use.

**Development**: `uv run pytest harness/tests` (51 tests, no network — a
scripted fake LLM client drives the real forge runner). Lint/typecheck:
`uv run ruff check harness/src harness/tests` and `uv run mypy harness/src`
(strict).

## Design documents by feature

Design docs live in `docs/`, dated `YYYY-MM-DD-<name>.md` so they sort
chronologically.

| Feature | Document | Role |
|---|---|---|
| The pattern itself | `docs/llm-wiki.md` / `docs/REFERENCE_llm-wiki-pattern.md` | Alignment document (Karpathy's LLM Wiki idea). The north star every task is checked against. |
| Local LLM-Wiki system | `docs/2026-06-10-local-llm-wiki-design.md` | The system design: three layers, three operations, forge harness, determinism boundary, data model. |
| PDF ingestion | `docs/2026-06-11-pdf-ingestion-design.md` | Book-scale PDF ingest: PyMuPDF extraction, text-vs-scanned detection (OCR path), TOC-aware semantic chunking, bounded map/integrate runs. Test fixture: `raw/javascriptallonge.pdf`. |
| Deterministic salience | `docs/2026-06-12-deterministic-salience-design.md` | Code-computed importance (wiki inbound links + per-ingest write counts) fed to synthesis runs so the model never ranks from memory. Implemented; `--reintegrate` rebuilds a hub with current salience. |
| Persistent chat | `docs/2026-06-12-persistent-chat-design.md` | `llmwiki chat`: warm-model REPL with follow-ups; SQLite session store, deterministic Q/A windowing (no model-curated memory). Phase 1 (read-only) implemented; Phase 2 (filing answers) designed. |
| M5 foundation migration | `docs/2026-06-14-m5-foundation-migration.md` | Records the replacement of the previous repo, the backup location, and which old safeguards to port selectively. |
| Wiki conventions (live) | `SCHEMA.md` (repo root) | The pattern's "schema" layer — page categories, link/citation rules, per-operation workflows. Fed to the model verbatim; revised as usage teaches us. |
| Dev environment | `docs/vim-tmux-unified-lsp-setup.md` | Replication guide for the no-root vim/tmux/LSP setup used to work on this repo. |
| TDD conventions | `docs/writing-tdds.md` | How design docs in this repo are written: sizing gate, required sections, style constraints. Referenced from CLAUDE.md; read before writing any TDD. |

Decisions deferred pending more sources live in `docs/open-questions.md` —
each with the experiment that would resolve it.

Supporting reference (not ours, load-bearing): `forge/docs/` —
ARCHITECTURE.md, USER_GUIDE.md, WORKFLOW.md, and the ADRs, especially
ADR-013 (the synthetic respond tool), which predicted the one live failure
mode we hit.

## Known limitations

- **One source per ingest, supervised.** No batch mode; the alignment doc's
  recommended flow is one-at-a-time with a human reading the results, and
  that's all the CLI offers.
- **Source size is capped.** `read_source` truncates beyond ~24K characters
  with an explicit marker; a long PDF-dump won't be fully ingested. Chunked
  ingest is designed but not built.
- **One-shot commands load the model per run** (~20–30 s for 8.4 GB).
  `llmwiki chat` covers the burst case — one boot per session, prompt cache
  reused across turns — so this now only costs occasional standalone
  `query`/`lint` invocations.
- **Search is naive.** Term-frequency scoring over page text plus the index —
  no embeddings, no BM25. Right answer at ~tens of pages; will degrade as
  the wiki grows (the design names qmd as the upgrade path).
- **It's a 14B at Q4.** Even with forge's guardrails, expect occasional
  mis-filed pages, thin summaries, or missed cross-references — that's what
  `lint` is for, and `raw/` remains the immutable source of truth.
- **Query runs with `/no_think`.** Fast factual lookups; complex multi-hop
  questions get less reasoning than ingest/lint do.
- **`wiki-health` is rewritten each lint.** Point-in-time reports live only
  in `log.md` and git history, not as dated pages.
- **Single-user, single-op.** One llama-server on one port; no concurrent
  operations.

## Future improvements

- **Chat Phase 2** — filing answers back into the wiki mid-conversation
  (`write_page` returns to the chat workflow, per the pattern doc's "good
  answers can be filed back" guidance).
- **Chunked ingest** — map-then-integrate flow for sources beyond the read
  budget; designed (see the PDF ingestion design doc), not yet implemented.
- **Real search** — swap the naive scorer for qmd (local hybrid BM25/vector
  with CLI + MCP) once the index outgrows flat scanning.
- **Batch ingest** — lower-supervision mode for backfilling many sources,
  per the pattern's "develop the workflow that fits your style" note.
- **Schema co-evolution** — fold lint learnings back into `SCHEMA.md` as
  logged revisions; the schema is meant to be a living document.
- **Richer outputs** — the pattern's optional modules: image handling in
  `raw/assets/`, Marp slide generation from wiki content, Dataview-friendly
  frontmatter.
- **Guardrail evals** — use forge's eval harness to measure and tune the
  wiki workflows (sampling, retry budgets, compaction thresholds) instead of
  relying on defaults.
- **Obsidian workflow** — Web Clipper for capturing sources into `raw/`,
  graph view as the lint companion.
