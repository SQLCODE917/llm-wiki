# Deterministic Salience for Synthesis Runs — Design

## Context & Problem

The first book ingest produced a hub page whose "key concepts" were
front-matter trivia (leanpub: 7 occurrences in the source) while the book's
actual center of mass (iterator: 333, iterable: 199) went unlisted —
open question #11. The cause is architectural: the integrate run sees only
chunk notes in chunk order, and no global-importance signal exists anywhere
in the pipeline, so a 14B is being asked to *remember* salience across 20
runs. Meanwhile the wiki already encodes the answer deterministically: the
most central concept pages have the most inbound `[[links]]`, and the
harness can know exactly which pages each chunk run wrote.

## Goals

- Synthesis runs (integrate, lint) receive a code-computed salience report;
  the model draws "key entities/concepts" from it instead of from memory.
- Two deterministic signals, both already latent in the system: inbound-link
  counts from the wiki graph, and per-page write/update counts recorded
  during chunked ingest.
- The manifest records which pages each chunk actually wrote — ground truth
  replacing the model's self-reported notes (which over-claimed twice,
  questions #9/#11).
- A `--reintegrate` flag reruns the integrate pass for an already-ingested
  source, so existing hubs benefit without re-ingesting.
- Acceptance: re-integrating `javascriptallonge.pdf` yields hub key-lists
  drawn from the computed top ranks — `iterable`/`iterator`-family pages
  present, `leanpub` absent.

## Non-Goals

- Graph centrality beyond plain inbound counts (PageRank etc.) — overkill at
  ~70 pages; revisit alongside the qmd search upgrade if ranking quality
  disappoints.
- Term-frequency mining of the source text as a primary signal — fuzzy
  slug-to-text matching is brittle; inbound links capture the same
  centrality once pages exist (kept as a future secondary signal).
- Re-ranking search results or changing query behavior.
- Automatic hub regeneration on every wiki write.

## Requirements

- **Alignment (docs/llm-wiki.md)**: the wiki is the compounding artifact —
  using its own link graph as the salience source is the pattern working as
  intended; the model remains the only author of wiki content (salience
  arrives as input, never as harness-written pages); bookkeeping stays
  deterministic per the system design's determinism boundary.
- **No new dependencies; pure-domain computation** (data-in/data-out,
  unit-testable), mirroring `compute_findings`.
- **Backward compatible**: manifests written before this change must load
  (the new per-chunk field defaults to empty).
- **No model-behavior regressions**: prompts gain one instruction; budgets
  and guardrails unchanged.

## Proposed Architecture

One new pure module computes the report; one existing capture pattern
records writes; the orchestrator folds the report into the messages it
already builds. No new processes, components, or tools visible to the model.

```
+----------------+   page texts    +-------------------+
| wiki/ (pages)  |---------------->| domain/salience   |
+----------------+                 | inbound counts +  |
+----------------+  pages_written  | ingest writes ->  |
| ChunkManifest  |---------------->| ranked report     |
+----------------+                 +---------+---------+
        ^                                    | rendered block
        | write_log (per run)                v
+----------------+                 +-------------------+
| write_page tool|                 | Session: integrate|
| (capture)      |                 | / lint messages   |
+----------------+                 +-------------------+
```

- **domain/salience.py** — pure: inbound-link counts over page texts
  (reusing `extract_links`), merged with per-page write counts from the
  manifest, producing a ranked report and a rendered text block. Index and
  `wiki-health` excluded, mirroring lint's exemptions.
- **write_page capture** — the tool gains an optional write-log (same
  pattern as the read-tracker): each successful write appends the page
  name. The session drains it after each chunk run into the manifest's new
  `pages_written` field. Notes stay for human supervision; `pages_written`
  is the machine record.
- **Session** — prepends the rendered salience block to the integrate
  message (and the lint message, where it doubles as "most-load-bearing
  pages to protect"); the integrate prompt instructs that key-lists must be
  drawn from it.
- **CLI `--reintegrate`** — reruns only the integrate workflow from an
  existing completed manifest, with current salience.

## Key Interactions

Integrate with salience (replaces the digest-only message):

```
Session                domain/salience           Runner/Qwen3
 |--page_texts + manifest---->|                      |
 |<--ranked report + block----|                      |
 |--integrate msg: salience block + digest---------->|
 |                            |        (key lists drawn from block,
 |                            |         hub written via read/write tools)
 |<-------------------finish_ingest(report)----------|
```

Chunk-run write capture (during map, unchanged flow plus one record):

```
Runner/Qwen3            write_page tool          Session/manifest
 |--write_page(name)------->| store write            |
 |                          | append to write_log    |
 |<--result-----------------|                        |
 |  (finish_chunk)          |   drain write_log----->| pages_written
```

## Data Model

- **SalienceEntry** — page name, category, inbound-link count, ingest write
  count. **SalienceReport** — ranked entries plus a `render()` producing the
  prompt block (top N per category, counts shown so the model sees *why*).
- **ChunkRecord (extended)** — gains `pages_written: tuple[str, ...]`
  (default empty; absent in old JSON ⇒ empty on load). The digest may
  append the deterministic list per chunk alongside the model's notes.
- Ranking: combined score (inbound links + ingest writes) descending,
  inbound as tiebreaker. Revised from inbound-first during implementation:
  the first live preview showed a freshly ingested wiki is still
  under-linked (chapter pages mention concepts in prose), so write counts
  carry the salience signal until lint converges the orphans. Top N = 8
  per category (entities/concepts), constant in code, awaiting tuning.

## APIs / Interfaces

- `domain/salience.py` — `compute_salience(page_texts, manifest?) ->
  SalienceReport`; pure, no I/O.
- `write_page_tool(..., write_log: list[str] | None)` — capture hook, same
  shape as `read_tracker`.
- `Session` — integrate and lint messages gain the rendered block; no
  signature changes beyond plumbing.
- `llmwiki ingest <file> --reintegrate` — requires a completed manifest;
  reruns integrate only; appends a fresh log entry.
- Prompts — integrate template: "the hub's key-entity/key-concept lists
  MUST be chosen from the salience report"; lint template: one line naming
  the block as the pages whose content matters most.

## Cross-Cutting Concerns

- **Testing** — domain tests for counting/ranking/rendering (including the
  measured failure as a fixture: a graph where front-matter pages have few
  inbound links must rank below iterable-like pages); e2e asserts the
  integrate message contains the block and that `pages_written` lands in
  the manifest; manifest roundtrip with and without the new field.
- **Observability** — the salience block appears verbatim in the integrate
  transcript (it is part of the user message), so ranking inputs are
  auditable per run.
- **Failure handling** — salience computation is pure and total; an empty
  wiki yields an empty report and the block is omitted. No new failure
  modes in the loop.

## Alternatives Considered

- **Status quo (model remembers)** — measured failure; open question #11.
- **PageRank / weighted centrality** — premature at this scale; plain
  inbound counts already separate iterable (many inbound) from leanpub.
- **Source term frequency as primary signal** — brittle slug↔text matching;
  deferred to secondary-signal status if link counts prove insufficient.
- **Mining write counts from transcripts** — fragile JSONL parsing of an
  observability artifact; the write-log capture is explicit and tested.
- **Harness writes the key-lists into the hub itself** — rejected at design
  time as violating "the model is the only author of wiki content"; **the
  decision was REVERSED on live evidence** (reintegrate #3): the
  read-before-rewrite contract and the choose-from-the-report rule collided
  and the model merged stale and fresh lists. Resolution: key-lists are
  *derived navigation with a single computed value* — bookkeeping, not
  content, in the same class as index.md entries and frontmatter, which the
  harness has always owned. After every integrate the harness reconciles
  the hub's key-list lines from the report (pure text transform, mentions
  floor applied); the model is told not to author them and keeps full
  ownership of the hub's prose, links, and synthesis.

## Open Questions / Risks

- **Signal weighting** — unweighted sum, chosen after the first live
  preview (inbound-first buried the book's center of mass behind
  front-matter pages because the fresh graph is under-linked); revisit
  after two more sources (fits the no-premature-tuning rule).
- **Top-N cap** — 8 per category is a constant pending evidence; too small
  hides mid-tier concepts, too large reintroduces model judgment.
- **Will the 14B obey "MUST be chosen from"?** — resolved: it didn't
  (merged stale and fresh lists under the read-before-rewrite contract);
  the key-lists moved behind the determinism boundary (see Alternatives,
  reversed entry). The model no longer makes this choice at all.
- **Mentions floor for key-lists** — `KEY_LIST_MIN_MENTIONS = 10` keeps
  barely-mentioned pages (foreword authors) off computed key-lists even
  when the eligible pool is tiny; constant awaiting tuning across sources.
- **Lint usage** — handing lint the same block may bias it toward popular
  pages and away from orphans; the findings section still leads, but watch
  the first runs.
