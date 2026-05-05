# Chunked Extraction Strategy for Comprehensive Wiki Ingestion

## Problem Statement

A 10,070 line source (350K chars, ~87K tokens) cannot fit in a 16K context window.
Current approach: Sample 10 sections × 30 lines = 300 lines (~3% coverage).
Result: Shallow extraction missing 90%+ of content.

## Quality Metrics

| Metric             | Definition                            | Current | Target |
| ------------------ | ------------------------------------- | ------- | ------ |
| Topic Coverage     | pages created / topics in source      | 10%     | 80%+   |
| Source Coverage    | unique lines cited / total lines      | 0.15%   | 5%+    |
| Evidence Density   | evidence rows per synthesized page    | 5-7     | 5-8    |
| Claim Grounding    | % locators that verify against source | ~50%    | 90%+   |
| Cross-link Density | wiki links per page                   | 1       | 3+     |

## Strategy: Multi-Pass Chunked Extraction

### Phase 1A: Topic Discovery (Single Pass)

- Input: TOC + evenly distributed samples
- Output: Comprehensive topic list with line ranges
- Validation: Compare topics found vs TOC entries

### Phase 1B: Section Boundary Detection

- Input: Full source
- Process: Detect natural section breaks (page markers, headings, blank runs)
- Output: Section index: `{ "topic": "Closures", "start": 1200, "end": 1450 }`

### Phase 2: Section-by-Section Extraction

For each section:

1. Extract section text (with 50-line overlap for context)
2. Build focused prompt with section context
3. Extract claims and evidence
4. Aggregate into page drafts

### Phase 3: Page Assembly

- Group claims by topic
- Deduplicate overlapping evidence
- Generate coherent page structure
- Validate evidence locators

## Implementation: Chunk Processing

```
Source: 10,070 lines
Chunk size: 400 lines (~1600 tokens)
Overlap: 50 lines
Chunks: ~28 chunks

Per chunk:
- Context budget: 2000 tokens (chunk + overlap)
- Prompt overhead: 500 tokens
- Output budget: 4000 tokens
- Total: ~6500 tokens (fits in 16K)
```

### Chunk Processing Prompt Template

```
TASK: Extract wiki-worthy claims from this source section.

SOURCE SECTION: Lines {start}-{end} of {total}
PREVIOUS SECTION SUMMARY: {prev_summary}

CONTENT:
{chunk_text}

EXTRACT:
1. Key concepts introduced in this section
2. Concrete claims with evidence (exact quotes)
3. Code examples worth preserving
4. Connections to other sections

OUTPUT FORMAT:
| Topic | Claim | Evidence | Locator |
|---|---|---|---|
```

## Orchestration Flow

```
wiki:ingest:deep <source> --slug <slug>
  │
  ├─ Phase 0: Normalize PDF
  │
  ├─ Phase 1A: Topic discovery
  │     └─ Identify ~30 topics with line ranges
  │
  ├─ Phase 1B: Section boundary detection
  │     └─ Build section index (deterministic)
  │
  ├─ Phase 2A: Chunk extraction (parallel-safe)
  │     └─ For each chunk: extract claims → .tmp/chunks/{slug}/chunk-{n}.json
  │
  ├─ Phase 2B: Claim aggregation
  │     └─ Group claims by topic → page drafts
  │
  ├─ Phase 2C: Page synthesis
  │     └─ For each topic: generate wiki page from aggregated claims
  │
  └─ Phase 3: Finalize (index, graph, log)
```

## Time Estimates

With Qwen3-Coder-30b on single 4090:

- Chunk processing: ~30 seconds per chunk
- 28 chunks × 30s = ~14 minutes for chunk extraction
- Page synthesis: ~30 seconds per page
- 30 pages × 30s = ~15 minutes for synthesis
- **Total: ~30 minutes for comprehensive extraction**

vs. current shallow extraction: ~3 minutes

## Verification Commands

```bash
# After ingestion, verify coverage
pnpm wiki:coverage-report <slug>

# Output:
# Topics found: 32
# Topics with pages: 28 (87.5%)
# Source lines cited: 512 / 10070 (5.1%)
# Evidence rows: 186 (avg 6.6/page)
# Grounding rate: 94.2%
```

## Configuration

```json
{
  "deep_ingest": {
    "chunk_size": 400,
    "chunk_overlap": 50,
    "max_topics": 50,
    "min_evidence_per_page": 3,
    "max_evidence_per_page": 12
  }
}
```

## Fallback: Evidence-First Search

If chunk extraction is too slow, use FTS-powered targeted extraction:

1. Build FTS index of source
2. For each candidate topic from Phase 1A:
   - Query: `{topic_keywords}`
   - Retrieve top-20 relevant passages
   - Extract claims from passages only

This reduces model calls from 28 chunks to N topics × 1 call.
