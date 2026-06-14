# PDF Ingestion for the Local LLM-Wiki — Design

## Context & Problem

The wiki ingests one markdown source at a time, capped at ~24K characters
(`docs/2026-06-10-local-llm-wiki-design.md`). PDFs fail immediately —
`read_source` decodes UTF-8 and raises `UnicodeDecodeError` on the first
binary byte (verified against `raw/javascriptallonge.pdf`). That test fixture
is also far beyond the single-pass design: 297 pages, ~343K characters
(~86K tokens) — about five times the model's entire 16K context — dense with
JavaScript code blocks. Extraction quality is not a given either: pypdf
produces run-together prose on this file ("namingPIisitsconcern") while
PyMuPDF extracts it cleanly, so the extractor is a load-bearing choice.

## Goals

- `llmwiki ingest <file>.pdf` works end to end for text-layer PDFs of
  book scale (hundreds of pages), producing the same artifacts as markdown
  ingest: source page(s), updated entity/concept pages, current index/log.
- Semantic chunking: chunk boundaries follow the document's own structure
  (TOC/headings), never split a paragraph, code block, or table.
- Bounded context per model run — no run may depend on emergency compaction;
  the book is processed as N independent, resumable runs.
- Wiki citations carry locators (`raw/javascriptallonge.pdf` + page range)
  so claims remain checkable against the immutable source.
- Scanned (image-only) PDFs are detected and routed to an OCR path rather
  than silently producing empty text.
- Extracted figures are OCR'd through a swappable recognizer interface;
  **an image with no recognizable text is a normal, silent outcome** — not
  a warning, not an error.
- Acceptance: `javascriptallonge.pdf` ingests to completion on this machine.
  Its 34 images are decorative photographs, which makes it the integration
  test for the empty-OCR path: the ingest must complete with zero figure
  text and zero noise.

## Non-Goals

- *Visual* interpretation of figures — describing a diagram's shape or a
  photo's content needs a multimodal model and is out of scope. OCR of
  figures (recovering text *in* images) is in scope; reading what isn't
  text is not.
- Perfect reproduction of code/math — the wiki summarizes and cites; it is
  not a typesetting round-trip.
- Whole-document OCR for scanned PDFs in the first implementation slice —
  detection plus a clean "scanned PDF, OCR pending" error ships first; the
  same recognizer port (below) serves it when enabled, so it's a wiring
  task, not a design change.
- Non-PDF binary formats (EPUB, DOCX) — same pipeline shape later, separate
  extractors.

## Requirements

- **Alignment (docs/llm-wiki.md)**: `raw/` stays immutable — extraction
  output is a derived, disposable cache, never a fourth layer; the model
  remains the only author of wiki content; index/log stay current per chunk,
  not just per document; the ingest remains supervisable (per-chunk reports).
- **Hardware/model reality**: 16K context, ~16 tok/s. A 297-page book is
  hours of model time; the pipeline must be resumable after interruption and
  must not redo finished chunks.
- **Determinism boundary** (carried from the system design): extraction,
  classification, chunking, budgeting, and progress tracking are
  deterministic code; only synthesis and integration belong to the model.
- **No root**: extraction and OCR dependencies must install into user space.

## Proposed Architecture

A deterministic **extraction pipeline** turns the PDF into a structured
markdown intermediate plus a **chunk manifest**; the existing forge-driven
ingest then runs once per chunk with a fresh context, followed by one
integration run. The key context-management decision: rather than one long
run kept alive by compaction, the harness owns an outer loop of bounded runs
— chunk state lives in the manifest on disk, not in the model's context
(the same "control flow is not memory" principle forge applies inside a run,
applied one level up).

```
+-----------+    +------------+     +-------------+    +----------------+
| raw/*.pdf |--->| Extractor  |---->|  Chunker    |--->| Chunk manifest |
| immutable |    | (PyMuPDF)  |     | (TOC-aware) |    | + md cache     |
+-----------+    +-----+------+     +-------------+    +-------+--------+
                       |                                       |
              figures and scanned pages              one bounded run per chunk
                       v                                       |
                 +----------------+   +----------------+       |
                 | TextRecognizer |   | forge Runner / |<------+
                 | port (Apple    |   | Qwen3 workflows|---> wiki/ + index
                 | Vision first)  |   +----------------+     + log
                 +----------------+
```

- **Extractor** — opens the PDF (PyMuPDF/pymupdf4llm), emits markdown with
  the TOC's heading hierarchy, page anchors, font-aware code fencing
  (monospace spans), table detection, hyphenation repair, and header/footer
  stripping. Images are written to the cache as JPEG files via pymupdf4llm's
  `write_images` (deterministic `<file>-<page>-<index>` names, inline
  `![](...)` refs at the correct reading position), sized-filtered to skip
  decorations. The refs cost a few tokens each and keep figures locatable by
  page. Each extracted figure is then run through the TextRecognizer port
  (below): recognized text is folded into the intermediate beneath the ref,
  explicitly marked as machine-recognized; no text means the ref stands
  alone. `embed_images` (base64-in-markdown) is rejected on measurement —
  see Alternatives.
- **TextRecognizer port** — one narrow interface for all OCR: image in,
  recognized text spans with confidence out (a pure data contract, no
  engine types leaking through). Two callers share it: the Extractor runs
  every extracted figure through it, and the scanned-PDF path (when enabled)
  feeds it page rasters. Engine selection is a configuration choice — the
  same shape as forge's swappable `CompactStrategy`. First adapter: Apple
  Vision via pyobjc (on-device, no root, no model files to manage); future
  adapters (tesseract off-macOS, a multimodal model as "recognizer") are new
  classes behind the same port, not design changes. The contract makes
  "no text found" a first-class result distinct from engine failure: empty
  is **normal and silent** (most figures are decorative — the fixture's 34
  photos prove it); an engine *error* fails the extraction loudly, per the
  fail-fast rule.
- **Classifier** — text-layer coverage heuristic (median chars/page over a
  threshold ⇒ text PDF); below it, the document routes through the
  TextRecognizer page-by-page before re-entering the same pipeline; the
  first implementation slice ships detection with a clear "scanned PDF, OCR
  pending" error while figure OCR exercises the port.
- **Chunker** — packs whole TOC sections into token-budgeted chunks; splits
  oversized sections at paragraph boundaries only; records heading path and
  page range per chunk.
- **Chunk manifest + markdown cache** — derived artifacts under
  `harness/cache/<sha256>/`, keyed by file content hash; gitignored,
  reproducible, safely deletable. The manifest tracks per-chunk status, which
  makes the ingest resumable and idempotent.
- **forge Runner / workflows** — unchanged guardrail stack; two new workflow
  shapes (map and integrate) described next.

## Key Interactions

Chunked ingest (map phase — one bounded run per chunk; resumable):

```
Orchestrator         Extract/Chunk          Runner/Qwen3        Wiki store
 |--ingest pdf--------->|                       |                  |
 |<--manifest (N chunks,|                       |                  |
 |    or cache hit)     |                       |                  |
 |--for each pending chunk k--------------------+                  |
 |       (fresh context: chunk text + heading path + page range)   |
 |                      |                       |--search_wiki---->|
 |                      |                       |--write_page----->| (update
 |                      |                       |   ...            |  affected
 |<--finish_chunk(notes: claims, entities, new pages)--------------+  pages)
 |--mark chunk k done in manifest; append notes to digest          |
 |--next pending chunk (or resume here after interruption)         |
```

Integration (reduce phase — one final bounded run):

```
Orchestrator              Runner/Qwen3                Wiki store
 |--integrate(digest of all chunk notes)-->|              |
 |                                         |--read_page-->| (hub + chapters)
 |                                         |--write_page->| source hub page,
 |                                         |              | cross-links, contradiction
 |<-------------finish_ingest(report)------|              | flags
 |--append single log entry for the whole ingest--------->|
```

The per-chunk run sees: the schema, one chunk (with its heading path and
page range), and the wiki via tools. It never sees the rest of the book —
the digest carries forward only the model's own distilled notes, and the
wiki itself accumulates the real knowledge between runs.

## Data Model

- **Markdown intermediate** — one file per source PDF in the cache; headings
  mirror the TOC; page anchors interleaved so chunk page-ranges and wiki
  citations can be derived mechanically. Sibling `images/` directory holds
  the extracted figures (JPEG; ~1.5 MB per 30 pages on the fixture vs ~8 MB
  as PNG), referenced relatively from the markdown. Figure-OCR results
  (including confirmed-empty ones) are cached per image, so re-extraction
  never re-runs recognition.
- **ChunkManifest** — per source-hash: ordered chunks with id, heading path,
  page range, token estimate, status (pending/done), and the digest of
  per-chunk notes. The resume cursor for interrupted ingests.
- **Chunk** — text plus locator metadata; sized by the context budget below.
- **WikiPage (extended convention)** — book-scale sources produce a hub
  source page (`javascriptallonge`) linking per-chapter source pages
  (`javascriptallonge-<chapter-slug>`); citations gain page ranges:
  `(raw/javascriptallonge.pdf p.28-41)`. SCHEMA.md is updated accordingly.

Context budget per map run (16K total): ~2.5K system prompt + schema,
~1K tool schemas and wire overhead, ≤6K chunk text, ~3K wiki reads during
integration, ~2.5K generation, ~1K headroom. Chunk target is therefore
**≤6K tokens (~24K chars)**; `javascriptallonge.pdf` at ~86K tokens packs
its 59 TOC sections into roughly 15–20 chunks.

## APIs / Interfaces

- `llmwiki ingest <file>` — unchanged entry point; dispatches by file type.
  New flags: `--resume` (continue a partial ingest from the manifest;
  default behavior when a manifest with pending chunks exists) and
  `--reextract` (invalidate the cache).
- Map workflow (per chunk): tools `search_wiki`, `read_page`, `write_page`,
  terminal `finish_chunk(notes)`; required steps `search_wiki`, `write_page`.
  The chunk text arrives in the user message — no `read_source` tool in this
  workflow, so the model cannot re-read the whole book into context.
- Integrate workflow: tools `search_wiki`, `read_page`, `write_page`,
  terminal `finish_ingest(report)` — the digest arrives in the user message.
- Extractor/Classifier/Chunker — internal `llmwiki` modules with pure-domain
  chunking logic (unit-testable data-in/data-out) and a thin PyMuPDF adapter.
- TextRecognizer — the OCR port: protocol plus adapters (`AppleVision` first)
  selected by configuration; recognition results are plain data
  (text spans + confidence), so tests use a fake recognizer and never touch
  the real engine.

## Cross-Cutting Concerns

- **Technical content fidelity.** Code: detected via monospace font flags
  and emitted as fenced blocks — observed pymupdf4llm artifacts on this very
  book (code rendered as italics/list items) mean the extractor must use
  span-level font inspection, not the library's markdown defaults, and the
  schema instructs the model to quote code verbatim or describe it — never
  repair it. Tables: extractor emits markdown tables, marking low-confidence
  extractions `[table: extraction uncertain]`; the model must not invent
  cell values. Formulas: text-layer math garbles ligatures and symbols —
  best-effort verbatim plus the same uncertainty marker; a 14B is never
  asked to reconstruct mathematics.
- **Figure OCR semantics.** Empty is normal, error is loud. A figure with
  no recognizable text adds nothing to the intermediate and emits nothing —
  decorative images (this fixture: all 34 of them) flow through silently. A
  confidence floor and minimum-length guard keep photo noise (a slogan on a
  coffee bag) from polluting the intermediate; what passes is marked as
  machine-recognized so the model treats it as evidence with a caveat, and
  the schema forbids citing OCR text as verbatim quotation. A recognizer
  *crash* is an extraction failure, not an empty result. The decorative
  fixture is the standing integration test for this contract: full ingest,
  zero figure text, zero warnings.
- **Failure & resumability.** Fail-fast carries over: a failed chunk run
  marks the chunk failed-with-error in the manifest and stops; completed
  chunks' wiki writes stand (they are real knowledge, already indexed);
  re-running resumes at the failed chunk. The single log entry is written
  only when the whole ingest (map + integrate) completes.
- **Observability.** One transcript per run as today — a book ingest yields
  N+1 transcripts under `harness/runs/`, named with the chunk id.
- **Supervision.** Per-chunk `finish_chunk` notes stream to stdout, so the
  alignment doc's "stay involved" workflow survives book-scale sources: the
  human can stop, inspect the wiki, and resume.

## Alternatives Considered

- **One long run + TieredCompact** — rejected: 86K tokens through a 16K
  window guarantees phase-3 compaction (the design's emergency path) and
  unreviewable behavior; bounded runs keep every run inside budget.
- **pypdf for extraction** — rejected on evidence: run-together words on the
  test fixture; PyMuPDF extracts the same page cleanly (AGPL acceptable for
  this personal, local, undistributed tool).
- **pdfplumber** — viable for tables, weaker as the single extractor; kept
  as a fallback for table-heavy documents if PyMuPDF's table detection
  disappoints.
- **pymupdf4llm `embed_images` (base64 in markdown)** — rejected on
  measurement: one fixture page went from 258 tokens to ~165K tokens with
  its image embedded (the library also transcodes JPEG→PNG base64,
  compounding it). A single embedded image is ~10× the model's whole
  context, and base64 is opaque to a text-only model anyway. `write_images`
  gives the same placement information for a few tokens per ref.
- **Fixed-size sliding-window chunks** — rejected: splits mid-paragraph and
  mid-code-block; TOC-aware packing preserves semantic units this fixture
  demonstrably has (59 sections).
- **Tesseract for OCR** — deferred in favor of Apple Vision via pyobjc:
  on-device, no root, no model files to manage; tesseract becomes relevant
  only if the wiki must run off-macOS, and slots in as another
  TextRecognizer adapter when it does.
- **Embedding-based semantic chunking** — rejected for v1: structure-based
  chunking is deterministic, free, and this document class (technical books)
  carries explicit structure; revisit alongside the qmd search upgrade.

## Open Questions / Risks

- **Wiki churn at book scale.** 15–20 chunk runs each touching pages may
  produce noisy edit patterns (e.g. a concept page rewritten 5 times).
  Mitigation candidates: per-chapter source pages absorb most writes; lint
  after ingest. Needs observation on the real fixture.
- **Digest growth.** Chunk notes for 20 chunks could exceed the integrate
  run's budget; the orchestrator may need to cap note length per chunk or
  run a two-stage reduce. Decide empirically.
- **Extraction edge cases in this fixture.** Leanpub styling (code in boxes,
  margin notes) may defeat header/footer stripping or code fencing in
  places; the uncertainty markers bound the damage, but quality needs a
  human pass on the first chapters.
- **OCR quality bar.** Apple Vision returns plain text without layout;
  scanned technical books will lose code indentation — possibly unusable
  for code-dense sources. May require restricting OCR path to prose
  documents initially.
- **Figure-OCR thresholds need tuning — confirmed by live data.** On the
  first real extraction, 18 of 35 fixture images passed the filters: one
  genuine text-bearing figure (p.24) and seventeen photo-noise hits (shop
  signage, a newspaper). The `unverified` marker bounds the damage, so v1
  ships as-is; tuning waits for a screenshot/diagram-heavy second fixture.
  Tracked in `docs/open-questions.md`.
- **Wall-clock cost.** ~20 runs × several minutes ≈ 1–2 hours per book at
  16 tok/s. Acceptable for the supervised one-source-at-a-time workflow,
  but worth revisiting with the persistent-server improvement (README,
  future improvements) so the model loads once, not 21 times.
