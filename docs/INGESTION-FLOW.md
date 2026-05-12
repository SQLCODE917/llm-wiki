# Wiki Ingestion Flow

This document describes how sources become wiki pages. It is structured to build understanding progressively:

1. **Core Concepts** - The foundational ideas you need first
2. **The Pipeline** - What happens when you run an ingest
3. **File I/O Reference** - Every file read or written

---

## Part 1: Core Concepts

Before diving into the pipeline, understand these foundational concepts:

### 1.1 The Three Artifacts

Every ingest produces three types of artifacts:

```
SOURCE ARTIFACTS          EXTRACTION STATE           WIKI PAGES
(immutable)               (intermediate)             (output)

raw/imported/             .wiki-extraction-        wiki/sources/
  <slug>/                   state/<slug>/            <slug>.md
  original.pdf            manifest.json            wiki/concepts/
                          claims-raw.jsonl           <topic>.md
raw/normalized/           claims-normalized.json   wiki/references/
  <slug>/                 candidates.json            <topic>.md
  source.md
```

**Source artifacts** are preserved forever. Once `original.pdf` is copied to `raw/imported/`, it is never modified.

**Extraction state** is intermediate data. Claims are extracted from the source, deduplicated, and prepared for synthesis.

**Wiki pages** are the output. They synthesize claims into readable, interlinked documentation.

### 1.2 Structured Chunking

The source is divided into chunks for claim extraction. Chunks are **token-bounded and structure-aware**:

```
SOURCE MARKDOWN
      |
      v
+-----------------+
| BlockExtractor  |  Parses markdown into typed blocks:
+-----------------+  - HEADING, PARAGRAPH, CODE, TABLE, LIST, EQUATION
      |
      v
+------------------+
| StructuralChunker|  Packs blocks into token-bounded chunks:
+------------------+  - Target: 6,500 tokens (configurable)
      |              - Keeps tables/code blocks intact
      v              - Preserves section context
+------------------+
| StructuredChunk  |  Each chunk has:
| chunk_id         |  - Section path (breadcrumb)
| section_path     |  - Line number range
| token_count      |  - Context header
| text             |
+------------------+
```

Why token-bounded? The LLM has a context window. Chunks are sized to leave room for the prompt and response.

### 1.3 Claims and Evidence

The LLM extracts **claims** from each chunk. A claim has four parts:

| Field    | Purpose                         | Example                                            |
| -------- | ------------------------------- | -------------------------------------------------- |
| claim    | Reusable knowledge statement    | "Functions are first-class values in JavaScript"   |
| evidence | Verbatim quote from source      | "JavaScript functions are first-class citizens..." |
| locator  | Line range in normalized source | `normalized:L45-L47`                               |
| topic    | Broad category for grouping     | "Functions"                                        |

Claims are grouped by topic, then deduplicated. Topics become candidate wiki pages.

### 1.4 Quality Gates

Synthesized pages pass through validation and judgment:

```
SYNTHESIS -> VALIDATION -> JUDGE -> ADOPT
               |             |
               v             v
            Checks:       Checks:
            - frontmatter  - claims supported?
            - sections     - evidence accurate?
            - locators     - too broad?
```

If validation fails, deterministic repair is attempted. If the judge finds unsupported claims, the page is quarantined for review.

---

## Part 2: The Pipeline

### 2.1 Overview

```
pnpm wiki:ingest raw/inbox/source.pdf --slug my-source

+--------+     +--------+     +--------+     +--------+
| PHASE 0|---->| PHASE 1|---->| PHASE 2|---->| PHASE 3|
|Normalize|    | Extract|    |Synthesize|   |Finalize|
+--------+     +--------+     +--------+     +--------+
    |              |              |              |
    v              v              v              v
 PDF->MD       Claims        Wiki Pages      Index/Graph
```

The orchestrator (`wiki_ingest.py`) runs all phases in sequence. Each phase can be run independently for debugging.

### 2.2 Phase 0: Normalize Source

**Goal**: Convert PDF to clean markdown with line numbers.

```
INPUT                           OUTPUT
raw/inbox/source.pdf   --->    raw/imported/<slug>/original.pdf  (copy, immutable)
                       --->    raw/normalized/<slug>/source.md   (extracted markdown)
```

**Process**:

```
wiki_phase0_import.py
       |
       v
+--------------+
| pymupdf4llm  |  <-- Default extractor (best structure recognition)
+--------------+
       |
       v
+------------------+
| clean_pdf_       |  Remove PDF artifacts:
| artifacts()      |  - Join soft-wrapped lines (\ followed by space)
+------------------+  - Fix backslash-newline continuations
       |
       v
raw/normalized/<slug>/source.md
```

**Key Point**: `pymupdf4llm` is the only extractor. It handles tables, code blocks, and document structure better than alternatives.

### 2.3 Phase 1: Extract Claims

**Goal**: Extract all wiki-worthy claims from the source.

```
INPUT                                   OUTPUT
raw/normalized/<slug>/source.md  --->  .wiki-extraction-state/<slug>/
                                          claims-raw.jsonl    (append-only)
                                          claims-normalized.json (deduped)
                                          manifest.json       (progress)
```

**Process**:

```
wiki_deep_extract.py
       |
       v
+-------------------+
| create_structured_|  Chunk the source (token-aware)
| chunks()          |
+-------------------+
       |
       v (for each chunk)
+-------------------+
| extract_claims_   |  LLM call to extract claims
| from_chunk()      |  - Build prompt with chunk text
+-------------------+  - Parse JSON response
       |              - Generate stable claim IDs
       v
+-------------------+
| aggregate_claims_ |  Group by topic, deduplicate
| by_topic()        |
+-------------------+
       |
       v
.wiki-extraction-state/<slug>/claims-normalized.json
```

**Claim ID Format**: `claim_<slug>_c<chunk>_<hash>`

Example: `claim_js-allonge_c003_a1b2c3d4`

The hash is derived from the claim text and locator, making IDs stable across re-runs.

### 2.4 Phase 2: Synthesize Pages

**Goal**: Create wiki pages from extracted claims.

#### Phase 2a: Source Page

```
INPUT                                        OUTPUT
claims-normalized.json              --->     wiki/sources/<slug>.md
       |
       v
+---------------------------+
| create_source_page_from_  |  Build source page with:
| topics()                  |  - Key claims table
+---------------------------+  - Major concepts (groupings)
                              - Related pages (candidates)
```

#### Phase 2b: Synthesized Pages

```
For each topic with >= 3 claims:

+---------------------------+
| select_representative_    |  Pick claims for the page:
| claims()                  |  - Score by specificity
+---------------------------+  - Ensure section coverage
       |                      - Deduplicate
       v
+---------------------------+
| render_prompt()           |  Build synthesis prompt with:
+---------------------------+  - Evidence bank
       |                      - Page template
       v
+---------------------------+
| LLM synthesis call        |
+---------------------------+
       |
       v
+---------------------------+
| validate + judge + repair |  Quality gates:
+---------------------------+  - wiki_check_synthesis.py
       |                      - wiki_judge_claims.py
       v                      - wiki_deterministic_repair.py
+---------------------------+
| wiki_adopt_phase2.py      |  Copy passing pages to wiki/
+---------------------------+
```

**Disposable Worktrees**: Synthesis happens in a temporary git worktree. Only pages that pass quality gates are adopted into the main wiki.

### 2.5 Phase 3: Finalize

**Goal**: Update navigation and log the operation.

```
wiki_phase3_finalize.py
       |
       +---> wiki_index.py      Update wiki/index.md
       |
       +---> wiki_graph.py      Update wiki/_graph.json
       |
       +---> wiki_lint.py       Generate wiki/_linter-report.md
       |
       +---> wiki_log.py        Append to wiki/log.md
```

---

## Part 3: File I/O Reference

### 3.1 Complete File Map

```
PHASE 0 - Normalize
-----------------------------------------------------------------
READ:   raw/inbox/<file.pdf>              Source PDF
WRITE:  raw/imported/<slug>/original.pdf  Immutable copy
WRITE:  raw/normalized/<slug>/source.md   Extracted markdown

PHASE 1 - Extract
-----------------------------------------------------------------
READ:   raw/normalized/<slug>/source.md   Normalized source
WRITE:  .wiki-extraction-state/<slug>/
          manifest.json                   Pipeline status
          claims-raw.jsonl                Append-only raw claims
          claims-normalized.json          Deduped claims with IDs
          candidates.generated.json       Proposed pages

PHASE 2 - Synthesize
-----------------------------------------------------------------
READ:   .wiki-extraction-state/<slug>/claims-normalized.json
READ:   raw/normalized/<slug>/source.md   For evidence lookup
WRITE:  wiki/sources/<slug>.md            Source page
WRITE:  wiki/concepts/<topic>.md          Concept pages
WRITE:  wiki/references/<topic>.md        Reference pages
WRITE:  .tmp/synthesis-failures/<slug>/   Quarantined failures

PHASE 3 - Finalize
-----------------------------------------------------------------
READ:   wiki/**/*.md                      All wiki pages
WRITE:  wiki/index.md                     Updated catalog
WRITE:  wiki/_graph.json                  Updated graph
WRITE:  wiki/_linter-report.md            Health report
APPEND: wiki/log.md                       Operation log
```

### 3.2 State Directory Layout

```
.wiki-extraction-state/<slug>/
├── manifest.json              # Pipeline status, config, errors
├── claims-raw.jsonl           # Append-only extraction output
├── claims-normalized.json     # Source of truth for claims
├── candidates.generated.json  # Machine-proposed pages
├── candidates.override.json   # Human curator overrides
├── candidates.json            # Merged candidates
└── failures/                  # Quarantined synthesis failures
    └── <page-stem>.json
```

### 3.3 Manifest Schema

```json
{
  "schema_version": 1,
  "slug": "js-allonge",
  "source_file": "raw/inbox/javascriptallonge.pdf",
  "source_kind": "pdf",
  "original_hash": "sha256:...",
  "normalized_hash": "sha256:...",
  "phases": {
    "phase0_import": "complete",
    "phase1a_extract": "complete",
    "phase2b_synthesize": "running"
  },
  "phase2_progress": {
    "total_candidates": 12,
    "synthesized": 8,
    "adopted": 7,
    "failed": 1,
    "pending": 4
  },
  "config": {
    "extractor": "pymupdf4llm",
    "structured": true,
    "target_tokens": 6500
  }
}
```

---

## Part 4: Configuration Reference

### 4.1 Environment Variables

| Variable             | Purpose                   | Example                |
| -------------------- | ------------------------- | ---------------------- |
| `AWS_PROFILE`        | AWS SSO profile           | `sdai-dev`             |
| `AWS_REGION`         | AWS region                | `us-east-1`            |
| `WIKI_MODEL_BACKEND` | LLM backend               | `bedrock`, `codex`     |
| `WIKI_APPROX_TOKENS` | Use approximate tokenizer | `1` (for faster tests) |

### 4.2 Command-Line Flags

**Phase 0 (Normalization)**:
| Flag | Default | Purpose |
| ------------------- | ------------- | ------------------------------ |
| `--pdf-extractor` | `pymupdf4llm` | PDF extraction library |
| `--reuse-imported` | off | Allow re-run if bytes match |
| `--overwrite-normalized` | off | Replace existing normalized |

**Phase 1 (Extraction)**:
| Flag | Default | Purpose |
| ------------------- | ------- | ----------------------------------- |
| `--structured` | on | Use token-aware chunking |
| `--target-tokens` | 6500 | Tokens per chunk |
| `--extract-timeout` | 120 | Timeout per chunk (seconds) |

**Phase 2 (Synthesis)**:
| Flag | Default | Purpose |
| ----------------------- | ------------- | ------------------------------ |
| `--candidate` | `local-4090` | Model for synthesis |
| `--judge-candidate` | (from above) | Model for judging |
| `--min-claims-per-topic`| 3 | Min claims to create page |
| `--strict-judge` | off | Fail on `too_broad` verdicts |
| `--timeout` | 900 | Synthesis timeout (seconds) |

**Skip Flags** (for debugging):
| Flag | Effect |
| ----------------- | ----------------------------------- |
| `--skip-phase0` | Skip normalization |
| `--skip-extract` | Skip extraction (use existing) |
| `--skip-source-page` | Skip source page creation |
| `--skip-phase2` | Skip synthesis |
| `--skip-phase3` | Skip finalization |
| `--dry-run` | Show what would happen |

---

## Part 5: Troubleshooting

### 5.1 Common Issues

**"Unable to locate credentials"**

```bash
aws configure sso --profile sdai-dev
aws sso login --profile sdai-dev
```

**"Slug already exists"**

```bash
# Either use a new slug, or if same source:
pnpm wiki:ingest ... --reuse-imported --overwrite-normalized
```

**"JSON parse error" in extraction**

- The LLM hit max_tokens mid-response
- Repair logic attempts recovery
- Check `.tmp/deep-extract/<slug>/` for raw responses

**Synthesis keeps failing**

```bash
# Check quarantine for failure details:
ls .tmp/synthesis-failures/<slug>/
cat .tmp/synthesis-failures/<slug>/<page>/FAILURE_SUMMARY.md
```

### 5.2 Debugging Commands

```bash
# Check extraction state
pnpm wiki:extraction-state <slug>

# Dry-run ingest to see what would happen
pnpm wiki:ingest raw/inbox/file.pdf --slug test --dry-run

# Run single phase 2 synthesis for debugging
pnpm wiki:phase2-single <slug> ../concepts/topic.md --report .tmp/debug.md

# Check validation without running full pipeline
pnpm wiki:check-source <slug>
pnpm wiki:check-synthesis <slug>

# View claim selection report
cat .tmp/synthesis/<slug>/<topic>/claim_selection.json
```

---

## Summary

The ingestion pipeline transforms a PDF into interlinked wiki pages:

1. **Phase 0**: `pymupdf4llm` extracts PDF to markdown
2. **Phase 1**: Structured chunking + LLM extracts claims
3. **Phase 2**: Claims are synthesized into wiki pages with quality gates
4. **Phase 3**: Index, graph, and log are updated

Key files:

- `raw/imported/` — immutable source copies
- `.wiki-extraction-state/` — extraction progress and claims
- `wiki/` — synthesized pages
