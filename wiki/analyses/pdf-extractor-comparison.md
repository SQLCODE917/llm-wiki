---
title: PDF Extractor Comparison - js-allonge
type: analysis
tags: [pdf, extraction, pymupdf, pdfplumber]
status: complete
last_updated: 2026-05-08
sources: [js-allonge]
---

# PDF Extractor Comparison: js-allonge

## Summary

Tested three PDF extractors on `javascriptallonge.pdf` (297 pages, ~350KB) using the wiki ingestion pipeline with AWS Bedrock backend.

**Note**: Marker and Docling require NVIDIA GPU and were not tested in this container.

## Results with Structured Chunking (Recommended)

Using `--structured --target-tokens 3500` for token-aware structural chunking:

| Target Tokens | Chunks | Truncated | Claims | Topics |
| ------------- | ------ | --------- | ------ | ------ |
| 6500          | 15     | 5 (33%)   | 182    | 12     |
| **3500**      | 25     | 1 (4%)    | **396**| 14     |

**Recommendation**: Use 3500 target tokens to avoid `max_tokens` truncation.

### Extractor Comparison (6500 tokens)

| Extractor       | Chunks | Claims | Topics | Pages Created | Success Rate |
| --------------- | ------ | ------ | ------ | ------------- | ------------ |
| **PyMuPDF4LLM** | 15     | 143    | 8      | 8             | **100%**     |
| pdfplumber      | 13     | 130    | 9      | 7             | 78%          |
| PyMuPDF (basic) | 13     | 128    | 8      | 8             | 100%         |

### Quality Indicators

| Extractor       | Avg Tokens/Chunk | Quality Issues                                |
| --------------- | ---------------- | --------------------------------------------- |
| **PyMuPDF4LLM** | 6,679            | single_char_lines: 22                         |
| pdfplumber      | ~7,000           | (not reported)                                |
| PyMuPDF (basic) | 7,109            | single_char_lines: 46, possible_table_loss: 3 |

## Results with Line-Based Chunking (NOT Recommended)

Using default `wiki:ingest` with 400-line chunks:

| Extractor       | Chunks | Claims | Topics | Pages Adopted | Success Rate |
| --------------- | ------ | ------ | ------ | ------------- | ------------ |
| PyMuPDF (basic) | 29     | 274    | 10     | 5             | 50%          |
| pdfplumber      | 27     | 255    | 11     | 1             | 9%           |
| PyMuPDF4LLM     | 19     | 180    | 10     | 1             | 10%          |

## Key Findings

### 1. Structured Chunking is Critical

The same extractors that failed with line-based chunking achieved 78-100% success with structured chunking:

- **PyMuPDF4LLM**: 10% → 100% success
- **pdfplumber**: 9% → 78% success
- **PyMuPDF**: 50% → 100% success

### 2. PyMuPDF4LLM Produces Best Structural Data

- Preserves headings, tables, and code blocks as markdown
- Creates cleaner semantic units for chunking
- Fewer quality issues than basic PyMuPDF

### 3. All Extractors Work Well with Proper Chunking

With structured chunking, all three extractors achieved good results. The choice of extractor matters less than the chunking strategy.

### 4. Token Budget Compliance

Structured chunking kept most chunks within the 6,500-9,000 token target range, optimizing for the model's context window.

## Recommendations

1. **Always use `--structured --target-tokens 3500`** for deep extraction (default)
2. **PyMuPDF4LLM** is the best choice for documents with tables and code
3. **PyMuPDF (basic)** is a good fallback for simpler documents
4. **pdfplumber** works but may lose some structural information

## Pipeline Command

```bash
# Phase 0: Extract with best extractor
python3 tools/wiki_phase0_import.py raw/inbox/<file.pdf> <slug> --pdf-extractor pymupdf4llm

# Phase 1: Deep extract with structured chunking
pnpm wiki:deep-extract <slug> --structured --target-tokens 6500

# Phase 2+3: Synthesis and finalize
pnpm wiki:deep-extract <slug> --resume
```

## Environment

- Backend: AWS Bedrock (qwen3-coder-30b)
- Container: Debian 13 (trixie), no GPU
- Date: 2026-05-07
