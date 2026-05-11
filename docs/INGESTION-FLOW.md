# Wiki Ingestion Flow

## Pipeline Overview

```
                              pnpm wiki:ingest
                                    |
                                    v
+==============================================================================+
|                           wiki_ingest.py (orchestrator)                       |
+==============================================================================+
                                    |
        +---------------------------+---------------------------+
        |                           |                           |
        v                           v                           v
+----------------+        +------------------+        +------------------+
|    PHASE 0     |   -->  |     PHASE 1      |   -->  |     PHASE 2      |
|   Normalize    |        |  Deep Extract    |        |    Synthesize    |
+----------------+        +------------------+        +------------------+
        |                           |                           |
        v                           v                           v
+----------------+        +------------------+        +------------------+
| wiki_phase0_   |        | wiki_deep_       |        | Phase 2a:        |
| import.py      |        | extract.py       |        |  create_source_  |
+----------------+        +------------------+        |  page_from_topics|
                                                      +------------------+
                                                              |
                                                              v
                                                      +------------------+
                                                      | Phase 2b:        |
                                                      | wiki_phase2_     |
                                                      | single.py (loop) |
                                                      +------------------+
                                                              |
                                                              v
                                                      +------------------+
                                                      | wiki_adopt_      |
                                                      | phase2.py        |
                                                      +------------------+
                                                              |
        +-----------------------------------------------------+
        |
        v
+------------------+
|     PHASE 3      |
|    Finalize      |
+------------------+
        |
        v
+------------------+
| wiki_phase3_     |
| finalize.py      |
+------------------+
        |
        +---> wiki_index.py    (update wiki/index.md)
        +---> wiki_graph.py    (update wiki/_graph.json)
        +---> wiki_lint.py     (generate wiki/_linter-report.md)
        +---> wiki_log.py      (append to wiki/log.md)
```

---

## Detailed Phase Flow

### PHASE 0: Normalize Source

```
raw/inbox/<file.pdf>
        |
        v
+-----------------------------------------------+
|            wiki_phase0_import.py              |
+-----------------------------------------------+
        |
        +---[1]---> Copy original to raw/imported/<slug>/original.pdf
        |           (IMMUTABLE - never modify)
        |
        +---[2]---> PDF Extraction (--pdf-extractor flag)
        |                   |
        |       +-----------+-----------+-----------+
        |       |           |           |           |
        |       v           v           v           v
        |   [pymupdf4llm] [marker]  [pymupdf]  [pdfplumber]
        |       |           |           |           |
        |       +-----------+-----------+-----------+
        |                   |
        |                   v
        +---[3]---> raw/normalized/<slug>/source.md
                    (with line numbers, cleaned)
```

### PHASE 1: Deep Extract Claims

```
raw/normalized/<slug>/source.md
        |
        v
+-----------------------------------------------+
|            wiki_deep_extract.py               |
+-----------------------------------------------+
        |
        +---[1]---> Chunking (--structured flag determines method)
        |                   |
        |       +-----------+-----------+
        |       |                       |
        |       v                       v
        |   [Line-based]         [Structured/Token-aware]
        |   --chunk-size=400     --target-tokens=3500
        |   --overlap=30         wiki_structured_chunking.py
        |       |                       |
        |       +-----------+-----------+
        |                   |
        +---[2]---> For each chunk:
        |           +---> Build extraction prompt
        |           +---> LLM call (via wiki_model_backend.py)
        |           +---> Parse JSON claims
        |           +---> Save progress to state file
        |
        +---[3]---> Aggregate claims by topic
        |           +---> Normalize topic names (broad categories)
        |           +---> Deduplicate similar claims
        |
        +---[4]---> Save extraction state
                    .wiki-extraction-state/<slug>/state.json
```

### PHASE 2: Synthesize Pages

```
PHASE 2a: Source Page
+-----------------------------------------------+
|        create_source_page_from_topics()       |
+-----------------------------------------------+
        |
        +---[1]---> Build source page frontmatter
        +---[2]---> Generate ## Key claims table
        +---[3]---> Generate ## Major concepts (natural groupings)
        +---[4]---> Generate ## Related pages (candidates)
        +---[5]---> Write wiki/sources/<slug>.md
        +---[6]---> Validate: pnpm wiki:check-source <slug>

PHASE 2b: Synthesized Pages (per candidate)
+-----------------------------------------------+
|            wiki_phase2_single.py              |
+-----------------------------------------------+
        |
        +---[1]---> Build evidence bank from extraction state
        |           wiki_phase2_benchmark.py::build_evidence_bank()
        |
        +---[2]---> Select claims for candidate page
        |           (score by specificity, ensure heading coverage)
        |
        +---[3]---> Render synthesis prompt
        |           tools/prompts/phase2-synthesis.md (default)
        |           tools/prompts/phase2-reference-synthesis.md (references)
        |
        +---[4]---> LLM synthesis call
        |           +---> Parse response via WikiPageSchema
        |           +---> Expand evidence IDs (fill_evidence)
        |
        +---[5]---> Validation gate
        |           wiki_check_synthesis.py
        |           +---> Frontmatter checks
        |           +---> Section checks
        |           +---> Evidence checks
        |
        +---[6]---> Judge gate (--strict-judge for quality)
        |           wiki_judge_claims.py
        |           +---> Verify claims against source
        |           +---> Check evidence excerpts match
        |
        +---[7]---> Deterministic repair (if validation fails)
        |           wiki_deterministic_repair.py
        |           +---> Fix bad locators
        |           +---> Fix evidence excerpts
        |
        +---[8]---> Write to disposable worktree
        |
        v
+-----------------------------------------------+
|            wiki_adopt_phase2.py               |
+-----------------------------------------------+
        |
        +---> Copy passing page from worktree to wiki/
        +---> Update source page Related pages links
              wiki_link_related.py
```

### PHASE 3: Finalize

```
+-----------------------------------------------+
|           wiki_phase3_finalize.py             |
+-----------------------------------------------+
        |
        +---[1]---> wiki_index.py
        |           Update wiki/index.md with new pages
        |
        +---[2]---> wiki_graph.py
        |           Update wiki/_graph.json with nodes/edges
        |
        +---[3]---> wiki_lint.py
        |           Generate wiki/_linter-report.md
        |
        +---[4]---> wiki_log.py
                    Append ingest entry to wiki/log.md
```

---

## Functional Flags (Affect Processing Method)

### Phase 0 Flags

| Flag              | Values                                                   | Default | Effect                                                                               |
| ----------------- | -------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------ |
| `--pdf-extractor` | `auto`, `marker`, `pymupdf`, `pymupdf4llm`, `pdfplumber` | `auto`  | PDF-to-markdown converter. `auto` tries pymupdf4llm first, then marker, then pymupdf |
| `--torch-device`  | `cuda`, `cpu`, `mps`                                     | `cuda`  | GPU device for marker (only applies if marker is selected)                           |
| `--source-type`   | `auto`, `pdf`, `markdown`                                | `auto`  | Force source type detection                                                          |

### Phase 1 Flags (Chunking Strategy)

| Flag              | Values | Default | Effect                                                                  |
| ----------------- | ------ | ------- | ----------------------------------------------------------------------- |
| `--structured`    | (flag) | off     | **KEY FLAG**: Use token-aware structural chunking instead of line-based |
| `--target-tokens` | int    | 3500    | Target source tokens per chunk (structured chunking only)               |
| `--chunk-size`    | int    | 400     | Lines per chunk (line-based chunking only)                              |
| `--overlap`       | int    | 30      | Overlap lines between chunks (line-based chunking only)                 |

#### Line-based vs Structured Chunking

```
LINE-BASED (default, --chunk-size=400):
+----------------------------------------------------------+
| Chunk 1: Lines 1-400        | ~1600 tokens               |
| Chunk 2: Lines 370-770      | ~1600 tokens (30 overlap)  |
| Chunk 3: Lines 740-1140     | ~1600 tokens               |
| ...                                                       |
+----------------------------------------------------------+
Pros: Simple, predictable
Cons: May split tables, code blocks, related content

STRUCTURED (--structured --target-tokens=3500):
+----------------------------------------------------------+
| [BlockExtractor] -> Blocks (headings, tables, code, text)|
| [StructuralChunker] -> Token-aware packing               |
|                                                           |
| Chunk 1: Blocks 1-8 (~3500 tokens)                       |
|   - Preserves tables intact                              |
|   - Keeps code blocks whole                              |
|   - Adds context headers from section path               |
| Chunk 2: Blocks 9-15 (~3400 tokens)                      |
| ...                                                       |
+----------------------------------------------------------+
Pros: Preserves document structure, better for technical PDFs
Cons: Variable chunk count
```

### Phase 2 Flags (Synthesis Quality)

| Flag                     | Values                                    | Default                             | Effect                                                         |
| ------------------------ | ----------------------------------------- | ----------------------------------- | -------------------------------------------------------------- |
| `--candidate`            | profile name                              | `local-4090`                        | Model profile for synthesis                                    |
| `--phase2-candidate`     | profile name                              | (from --candidate)                  | Override model for synthesis only                              |
| `--judge-candidate`      | profile name                              | (from --candidate)                  | Override model for claim judging                               |
| `--strict-judge`         | (flag)                                    | off                                 | Fail on `too_broad` verdicts (default: soft-pass accepts them) |
| `--min-claims-per-topic` | int                                       | 3                                   | Minimum claims required to create a page                       |
| `--backend`              | `bedrock`, `codex`, `openai`, `anthropic` | env `WIKI_MODEL_BACKEND` or `codex` | LLM backend                                                    |
| `--timeout`              | int (ms)                                  | 900                                 | Timeout per synthesis call                                     |
| `--judge-timeout`        | int (ms)                                  | 900                                 | Timeout per judge call                                         |

---

## Preconditions

### Before Running `pnpm wiki:ingest`

| Requirement                  | Location                                        | Purpose                                |
| ---------------------------- | ----------------------------------------------- | -------------------------------------- |
| Source file                  | `raw/inbox/<file.pdf>` or `raw/inbox/<file.md>` | Input document to ingest               |
| Model backend configured     | `WIKI_MODEL_BACKEND` env var                    | e.g., `bedrock`, `codex`               |
| AWS credentials (if bedrock) | `AWS_PROFILE`, `AWS_REGION`                     | Authenticate to Bedrock                |
| Slug available               | `raw/imported/<slug>/` must not exist           | Prevents overwriting immutable imports |

### Directory Structure Required

```
llm-wiki/
├── raw/
│   ├── inbox/           # User drops source files here
│   ├── imported/        # IMMUTABLE originals (auto-created)
│   └── normalized/      # Extracted markdown (auto-created)
├── wiki/
│   ├── sources/         # Source pages (auto-created)
│   ├── concepts/        # Concept pages (auto-created)
│   ├── entities/        # Entity pages (auto-created)
│   ├── procedures/      # Procedure pages (auto-created)
│   ├── references/      # Reference pages (auto-created)
│   ├── index.md         # Content catalog (updated)
│   ├── log.md           # Operation history (appended)
│   └── _graph.json      # Dependency graph (updated)
└── .wiki-extraction-state/  # Extraction state (auto-created)
```

---

## Postconditions

### Files Created/Modified After Successful Ingest

| File/Directory                             | Purpose             | Content Summary                          |
| ------------------------------------------ | ------------------- | ---------------------------------------- |
| `raw/imported/<slug>/original.pdf`         | Immutable original  | Byte-for-byte copy of inbox file         |
| `raw/normalized/<slug>/source.md`          | Normalized markdown | Line-numbered, cleaned text from PDF     |
| `.wiki-extraction-state/<slug>/state.json` | Extraction state    | Chunks, claims, topics, progress         |
| `wiki/sources/<slug>.md`                   | Source page         | Summary, key claims table, related pages |
| `wiki/concepts/<name>.md`                  | Concept pages       | Synthesized explanations with evidence   |
| `wiki/entities/<name>.md`                  | Entity pages        | Named things (people, orgs, tools)       |
| `wiki/procedures/<name>.md`                | Procedure pages     | How-tos with steps                       |
| `wiki/references/<name>.md`                | Reference pages     | Tables, formulas, lookup facts           |
| `wiki/index.md`                            | Updated catalog     | Links to all new pages                   |
| `wiki/_graph.json`                         | Updated graph       | Nodes for new pages, edges for links     |
| `wiki/_linter-report.md`                   | Lint results        | Validation status of wiki health         |
| `wiki/log.md`                              | Appended entry      | Ingest operation record                  |

### Source Page Structure

```markdown
---
title: <Source Title>
type: source
source_id: <slug>
source_type: pdf
raw_path: ../../raw/imported/<slug>/
normalized_path: ../../raw/normalized/<slug>/
status: draft
last_updated: YYYY-MM-DD
tags: []
sources: []
---

# <Title>

## Summary

<Auto-generated from extraction topics>

## Key claims

| Claim               | Evidence           | Locator              |
| ------------------- | ------------------ | -------------------- |
| Concrete claim text | "Verbatim excerpt" | `normalized:L12-L14` |

## Major concepts

### Natural groupings

| Group | Scope | Evidence basis | Candidate page types |
| ----- | ----- | -------------- | -------------------- |

## Related pages

| Candidate page | Intended path                              | Group | Priority    | Evidence basis | Status  |
| -------------- | ------------------------------------------ | ----- | ----------- | -------------- | ------- |
| Page Name      | [../concepts/name.md](../concepts/name.md) | Group | must create | basis          | created |
```

### Synthesized Page Structure

```markdown
---
title: <Page Title>
type: concept | entity | procedure | reference
tags: []
status: draft
last_updated: YYYY-MM-DD
sources:
  - ../sources/<slug>.md
source_ranges:
  - <slug>:normalized:L100-L200
---

# <Title>

<Definition/summary>

## Source-backed details

| Claim              | Evidence        | Locator          | Source                         |
| ------------------ | --------------- | ---------------- | ------------------------------ |
| Claim in own words | "Exact excerpt" | `normalized:L12` | [Source](../sources/<slug>.md) |

## Why it matters

## Common mistakes

## Examples

## Related pages
```

---

## Quick Reference Commands

```bash
# Full ingest (recommended)
pnpm wiki:ingest raw/inbox/<file.pdf> --slug <slug> --structured

# Dry run first
pnpm wiki:ingest raw/inbox/<file.pdf> --slug <slug> --structured --dry-run

# Resume interrupted ingest
pnpm wiki:ingest --slug <slug> --skip-phase0 --skip-extract

# Manual phases
pnpm wiki:phase0 raw/inbox/<file.pdf> <slug>
pnpm wiki:deep-extract <slug> --structured --target-tokens 3500
pnpm wiki:phase2-single <slug> ../concepts/example.md
pnpm wiki:phase3 <slug>
```
