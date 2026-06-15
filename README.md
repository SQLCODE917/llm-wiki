# LLM-Wiki

A persistent, LLM-maintained knowledge base running entirely on this machine,
following Karpathy's LLM Wiki pattern (`docs/llm-wiki.md`): instead of
re-retrieving from raw documents on every question (RAG), a local model
**incrementally builds and maintains a wiki** of interlinked markdown pages.
Knowledge is compiled once and kept current — cross-references, contradiction
flags, and synthesis compound with every source added.

The maintainer model is served by **Ollama**, driven through **forge**'s
guardrailed `WorkflowRunner` so local models execute multi-step wiki maintenance
reliably: step enforcement, tool prerequisites, rescue parsing, retry nudges,
and context compaction. The default runtime profile is `ollama-default`; the
4090 profile is `local-4090`, defaulting to `qwen3-coder:30b`.

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

Prerequisites:

- Ollama running locally.
- An Ollama model with tool support. `local-4090` defaults to
  `qwen3-coder:30b`; override with `LLMWIKI_4090_MODEL`.
- The Python env: `uv` with the repo-root `.venv` (forge and the harness
  installed editable).

All commands run from the repo root. Model-backed commands connect to Ollama,
run the operation, append to `wiki/log.md`, and unload the model through
forge's backend manager when the command exits. The deterministic status
commands below do not load a runtime or contact Ollama.

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
multiple conversations; `/file <page-name> [scope]` files the latest answer
through a dedicated synthesis workflow; `/ingest` and `/lint` run inside chat
on the warm server; `/exit`, Ctrl-C, or Ctrl-D leave gracefully. Ordinary chat
turns stay read-oriented. Filing is explicit, re-reads current wiki evidence,
and writes through `write_page` so `index.md` and `log.md` stay deterministic.
History lives in `harness/chat.db` (verbatim, gitignored); conversations are
continuity, not source evidence.

**Lint** — periodic health check:

```bash
uv run llmwiki lint
uv run llmwiki lint --strict-evidence warn
```

Deterministic checks run first in code (broken `[[links]]`, orphan pages,
index drift, citation evidence when enabled); the model then reviews flagged
pages, fixes what a page edit can fix, and files its report as the
`wiki-health` page. The final report includes a deterministic before/after
verification and delta, so lint success is never only the model's self-report.

**Curator status / maintenance** — model-free wiki dashboard:

```bash
uv run llmwiki curator-status
uv run llmwiki curator-status --strict-evidence warn
uv run llmwiki maintenance
```

`curator-status` prints deterministic wiki health without starting Ollama:
page counts, raw-source counts, link/index/orphan findings, citation evidence
findings, salience, recent log entries, and recommended next actions.
`maintenance` files the same report as `wiki-curator-status` and appends a
`maintenance` entry to `wiki/log.md`. Neither command repairs pages; use
`lint` when you want the model to inspect and edit.

**Contradictions** — bounded semantic audit:

```bash
uv run llmwiki contradictions
uv run llmwiki contradictions --max-pairs 20
```

The harness first selects candidate page pairs deterministically from shared
sources, direct links, shared raw citations, and keyword overlap. If candidates
exist, the model reads relevant pages from a small default audit batch and may
call `record_contradiction` for claims that cannot both be true as written. Use
`--max-pairs` for an explicitly larger sweep. The command files
`wiki-contradictions` and appends a `contradiction` log entry. It does not
rewrite pages or decide which source wins.

**Reading the wiki**: it's just markdown — open `wiki/` in Obsidian (graph
view shows the link structure) or any editor. Recent activity:
`grep "^## \[" wiki/log.md | tail -5`. Every run writes a full conversation
transcript to `harness/runs/*.jsonl`, so any wiki edit is traceable to the
model turn that produced it.

**Knobs**: `LLMWIKI_RUNTIME` (`ollama-default` or `local-4090`),
`LLMWIKI_OLLAMA_MODEL`, `LLMWIKI_4090_MODEL`, `LLMWIKI_OLLAMA_URL`, and
`LLMWIKI_CTX` (context tokens, default 16384). CLI `--runtime` overrides
`LLMWIKI_RUNTIME`. `LLMWIKI_STRICT_EVIDENCE` accepts `off`, `warn`, or
`fail`; CLI `--strict-evidence` overrides it for commands that support
evidence checks.

**Development**: `uv run pytest harness/tests` (no network — a scripted fake
LLM client drives the real forge runner). Lint/typecheck:
`uv run ruff check harness/src harness/tests` and `uv run mypy harness/src`
(strict).

## Design documents by feature

Design docs live in `docs/`, dated `YYYY-MM-DD-<name>.md` so they sort
chronologically.

| Feature | Document | Role |
|---|---|---|
| The pattern itself | `docs/llm-wiki.md` | Alignment document (Karpathy's LLM Wiki idea). The north star every task is checked against. |
| Local LLM-Wiki system | `docs/2026-06-10-local-llm-wiki-design.md` | The system design: three layers, three operations, forge harness, determinism boundary, data model. |
| PDF ingestion | `docs/2026-06-11-pdf-ingestion-design.md` | Book-scale PDF ingest: PyMuPDF extraction, text-vs-scanned detection (OCR path), TOC-aware semantic chunking, bounded map/integrate runs. Test fixture: `raw/javascriptallonge.pdf`. |
| Deterministic salience | `docs/2026-06-12-deterministic-salience-design.md` | Code-computed importance (wiki inbound links + per-ingest write counts) fed to synthesis runs so the model never ranks from memory. Implemented; `--reintegrate` rebuilds a hub with current salience. |
| Persistent chat | `docs/2026-06-12-persistent-chat-design.md` | `llmwiki chat`: warm-model REPL with follow-ups; SQLite session store, deterministic Q/A windowing (no model-curated memory). |
| Chat filing | `docs/2026-06-15-chat-phase2-file-synthesis.md` | Explicit `/file <page-name> [scope]` path for turning the latest chat answer into a durable `synthesis` page after re-reading wiki evidence. |
| M5 foundation migration | `docs/2026-06-14-m5-foundation-migration.md` | Records the replacement of the previous repo, the backup location, and which old safeguards to port selectively. |
| 4090 synthesis roadmap | `docs/2026-06-14-4090-feature-synthesis-roadmap.md` | Chain of independently shippable TDDs for 4090 runtime support and backup-feature synthesis. |
| Runtime profiles / 4090 | `docs/2026-06-14-runtime-profiles-4090.md` | First TDD in the chain: runtime selection and `local-4090` as a forge-compatible target. |
| Strict citation parser | `docs/2026-06-14-strict-citation-parser.md` | Second TDD in the chain: deterministic citation and locator findings for the flat M5 wiki. |
| Evidence write/lint gates | `docs/2026-06-14-evidence-gates-for-writes-and-lint.md` | Third TDD in the chain: opt-in `off|warn|fail` evidence behavior for writes and lint. |
| Maintenance automation / curator status | `docs/2026-06-14-maintenance-automation-curator-status.md` | Model-free `curator-status` report plus filed `maintenance` report/log entry. |
| Contradiction detection | `docs/2026-06-14-contradiction-detection.md` | Bounded model-assisted audits through `llmwiki contradictions`; files structured reports without auto-resolving conflicts. |
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
- **Non-PDF source size is capped.** `read_source` truncates plain text sources
  beyond ~24K characters with an explicit marker. PDFs use the chunked
  map/integrate ingest path.
- **One-shot commands load/connect to the model per run**.
  `llmwiki chat` covers the burst case — one boot per session, prompt cache
  reused across turns — so this now only costs occasional standalone
  `query`/`lint` invocations. `curator-status` and `maintenance` are
  model-free.
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
- **`wiki-curator-status` is rewritten each maintenance pass.** It is the
  current deterministic dashboard, while history lives in `log.md` and git.
- **`wiki-contradictions` is rewritten each contradiction audit.** The audit
  is bounded by candidate-pair selection and is not proof that no other
  contradictions exist.
- **Single-user, single-op.** One local Ollama-backed operation at a time.

## Future improvements

- **Chunked ingest hardening** — the PDF map-then-integrate flow is implemented;
  future work is improving source fidelity, code-block extraction, and
  normalized evidence support.
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
