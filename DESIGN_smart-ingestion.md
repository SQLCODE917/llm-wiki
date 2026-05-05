# Smart Ingestion: Managing Model Context for Large Documents

This document proposes improvements to the LLM-Wiki ingestion pipeline to handle large documents (30MB+ PDFs)
automatically, without human intervention, while respecting local model context limits.

## Problem Statement

The current ingestion pipeline has these failure modes with large documents:

1. **Phase 0 crash**: `marker_single` segfaults on large PDFs with many images/charts
2. **Unbounded normalized output**: A 30MB PDF can produce hundreds of pages of markdown
3. **Context overflow**: The full normalized source is read for evidence extraction, exceeding model limits
4. **No search infrastructure**: Evidence selection uses naive keyword matching, not retrieval-optimized search
5. **Manual intervention required**: User had to split the PDF into 50-page chunks, merge, and create outlines

## Current Architecture Analysis

### No Knowledge Base Drift Guarantee

**Core principle**: All search indices (SQLite FTS, vector embeddings) are **derived caches**, not sources of truth.

```
Source of truth (immutable after Phase 0):
  raw/normalized/<slug>/source.md

Derived caches (gitignored, rebuildable, auto-invalidated):
  raw/normalized/<slug>/.evidence.db      # SQLite FTS
  raw/normalized/<slug>/.embeddings/      # Vector index
```

**Drift prevention mechanisms**:

1. **Co-location**: Indices live next to their source file, not in a separate database
2. **Staleness detection**: Every index stores source file mtime; checked before every query
3. **Auto-rebuild**: If source is newer than index, rebuild transparently before returning results
4. **Read-only during synthesis**: Evidence retrieval never writes to indices
5. **Gitignore**: Indices are not committed; they're rebuilt on each machine
6. **Fallback**: If index is corrupt/missing, fall back to current `source_chunks()` scan

**Why this works**:
- Normalized source files are immutable after Phase 0 (enforced by existing tooling)
- Indices are only read during evidence retrieval (Phase 1/2)
- No user action can create drift because indices auto-validate on every access

### Conversation Knowledge → Wiki Filing

When new knowledge emerges from conversation (not document ingestion), it must flow through markdown first:

```
Conversation insight
       ↓
  Markdown file (source of truth)
       ↓
  SQLite/embedding index (derived, auto-rebuilds)
```

**Two paths for conversation-derived knowledge**:

| Path | When to use | Markdown location | Index scope |
|---|---|---|---|
| Curator note | Raw fact/observation to be synthesized later | `raw/inbox/curator-note-*.md` → ingest | Source index |
| Filed analysis | Reusable answer ready for wiki | `wiki/analyses/*.md` | Wiki index |

**Wiki-level index (H3b)**:

In addition to per-source indices, a wiki-wide index enables searching across all synthesized knowledge:

```
wiki/.wiki-index.db           # FTS over all wiki pages (gitignored)
wiki/.wiki-embeddings/        # Vector index over wiki (gitignored)
```

**Workflow for saving conversation knowledge**:

```python
def save_conversation_insight(
    insight: str,
    insight_type: Literal["curator_note", "analysis"],
    title: str,
    related_sources: list[str],
) -> Path:
    """Save conversation knowledge to markdown, then update indices."""
    
    if insight_type == "curator_note":
        # Path 1: Raw knowledge for later synthesis
        path = Path(f"raw/inbox/curator-note-{date.today()}-{slugify(title)}.md")
        path.write_text(f"# {title}\n\n{insight}\n")
        # Will be indexed when ingested via normal Phase 0-3
        
    else:
        # Path 2: Durable analysis ready for wiki
        path = Path(f"wiki/analyses/{date.today()}-{slugify(title)}.md")
        content = render_analysis_page(title, insight, related_sources)
        path.write_text(content)
        
        # Trigger wiki index rebuild (async-safe)
        invalidate_wiki_index()
    
    return path

def invalidate_wiki_index() -> None:
    """Mark wiki index as stale. Next query will rebuild."""
    wiki_index = Path("wiki/.wiki-index.db")
    if wiki_index.exists():
        # Touch a staleness marker instead of deleting
        # This allows concurrent reads to finish
        Path("wiki/.wiki-index.stale").touch()
```

**Query flow with wiki index**:

```python
def query_wiki(question: str) -> list[PageHit]:
    """Search wiki using index, with auto-rebuild on stale."""
    wiki_root = Path("wiki")
    index_path = wiki_root / ".wiki-index.db"
    stale_marker = wiki_root / ".wiki-index.stale"
    
    # Check staleness
    if stale_marker.exists() or not index_path.exists():
        rebuild_wiki_index(wiki_root, index_path)
        stale_marker.unlink(missing_ok=True)
    else:
        # Check if any wiki page is newer than index
        index_mtime = index_path.stat().st_mtime
        for page in wiki_root.rglob("*.md"):
            if page.stat().st_mtime > index_mtime:
                rebuild_wiki_index(wiki_root, index_path)
                break
    
    # Now safe to query
    return bm25_search_wiki(index_path, question)
```

### What Works

| Component | Status | Notes |
|---|---|---|
| Phased ingest | ✓ Good | Model sees one page at a time |
| Evidence bank | ✓ Good intent | Bounded snippets per candidate |
| Deterministic validation | ✓ Excellent | Model doesn't need to judge syntax |
| Range gating | ✓ Good | Evidence constrained to relevant sections |
| Atomic work units | ✓ Excellent | One source page or one synthesized page |

### What Doesn't Work

| Component | Status | Notes |
|---|---|---|
| Large PDF handling | ✗ Fails | marker_single segfaults on 30MB+ PDFs |
| Normalized source scanning | ✗ Unbounded | `source_chunks()` reads entire file |
| Evidence retrieval | ✗ Naive | Token overlap, not BM25/vector search |
| Context budgeting | ✗ Missing | No token tracking during prompt construction |
| Source outlining | ✗ Missing | Model must read whole source to extract structure |

### Deterministic Tools: Current vs. Needed

| Tool | Current | Needed |
|---|---|---|
| ripgrep | Not used | Section/heading extraction, fast text search |
| SQLite FTS | Not used | Index normalized source lines for BM25 retrieval |
| BM25 | Not used | Rank evidence snippets by relevance |
| Vector embeddings | Not used | Semantic search for concept matching |
| Hybrid search | Not used | BM25 + embeddings for best results |

---

## Hypotheses

### H1: Chunked PDF Normalization

**Hypothesis**: Large PDFs can be normalized reliably by splitting into page ranges before calling marker.

**Testable outcome**:
- Metric: A 30MB PDF normalizes without segfault
- Measurement: `marker_single` exit code 0 for each chunk
- Target: 100% normalization success for PDFs up to 100MB

**Implementation**:
```bash
# Phase 0 splits PDF into 30-page chunks
pdftk input.pdf burst output chunk_%03d.pdf
for chunk in chunk_*.pdf; do
  marker_single "$chunk" --output_format markdown --output_dir raw/normalized/<slug>/chunks/
done
# Merge normalized markdown preserving page numbers
python tools/wiki_merge_chunks.py raw/normalized/<slug>/chunks/ > raw/normalized/<slug>/source.md
```

**Validation**:
- Test with 10MB, 30MB, 100MB PDFs
- Compare merged output against single-pass output on successful small PDFs
- Measure memory usage during normalization

---

### H2: Source Outline Extraction (Deterministic)

**Hypothesis**: A source's structure (headings, sections, page boundaries) can be extracted deterministically
without reading the full content, reducing context needed for Phase 1.

**Testable outcome**:
- Metric: Source outline extracted in <100ms for any normalized source
- Measurement: Outline includes all H1-H3 headings with line numbers
- Target: Model receives 2KB outline instead of 200KB source for structure decisions

**Implementation**:
```python
def extract_outline(source_path: Path) -> str:
    """Extract headings and page markers without reading full content."""
    outline = []
    with open(source_path) as f:
        for line_no, line in enumerate(f, 1):
            if line.startswith('#'):
                outline.append(f"L{line_no}: {line.strip()}")
            elif line.startswith('---') and 'page' in line.lower():
                outline.append(f"L{line_no}: [page break]")
    return "\n".join(outline)
```

**Validation**:
- Extract outline from 100KB, 1MB, 10MB normalized sources
- Compare outline completeness to human-created table of contents
- Verify Phase 1 can identify natural groupings from outline alone

---

### H3: SQLite FTS Evidence Index

**Hypothesis**: A SQLite FTS5 index over normalized source lines enables sub-second BM25 retrieval,
replacing the O(n) token overlap scan.

**Testable outcome**:
- Metric: Evidence retrieval <100ms for any query
- Measurement: Compare retrieval time vs. current `snippets_for_candidate()`
- Target: Same or better recall with 10x faster retrieval

**Critical design constraint: No knowledge base drift**

The SQLite index is a **read-only derived cache**, not a source of truth:

1. **Single source of truth**: `raw/normalized/<slug>/source.md` remains canonical
2. **Index is ephemeral**: Built fresh during Phase 0 or on first evidence query
3. **Index location**: `raw/normalized/<slug>/.evidence.db` (gitignored, co-located with source)
4. **Staleness detection**: Index stores source file mtime; rebuild if source is newer
5. **No writes to index during synthesis**: Evidence retrieval is read-only
6. **Fallback**: If index is missing/stale, fall back to current `source_chunks()` scan

```
raw/normalized/<slug>/
├── source.md          # Source of truth (immutable after Phase 0)
└── .evidence.db       # Derived index (gitignored, rebuildable)
```

**Implementation**:
```python
def get_or_build_index(source_path: Path) -> sqlite3.Connection:
    """Get existing index or build fresh one. Never stale."""
    db_path = source_path.parent / ".evidence.db"
    source_mtime = source_path.stat().st_mtime
    
    if db_path.exists():
        conn = sqlite3.connect(db_path)
        stored_mtime = conn.execute("SELECT mtime FROM meta").fetchone()
        if stored_mtime and stored_mtime[0] >= source_mtime:
            return conn  # Index is fresh
        conn.close()
        db_path.unlink()  # Stale, rebuild
    
    return build_evidence_index(source_path, db_path)

def build_evidence_index(source_path: Path, db_path: Path) -> sqlite3.Connection:
    """Build SQLite FTS5 index over source lines."""
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE meta (mtime REAL)")
    conn.execute("INSERT INTO meta VALUES (?)", (source_path.stat().st_mtime,))
    conn.execute("""
        CREATE VIRTUAL TABLE evidence USING fts5(
            line_no UNINDEXED, content, tokenize='porter unicode61'
        )
    """)
    with open(source_path) as f:
        for line_no, line in enumerate(f, 1):
            if len(line.strip()) >= 40:
                conn.execute("INSERT INTO evidence VALUES (?, ?)", (line_no, line.strip()))
    conn.commit()
    return conn

def bm25_search(source_path: Path, query: str, limit: int = 8) -> list[tuple[int, str, float]]:
    """BM25-ranked search over evidence index."""
    conn = get_or_build_index(source_path)
    rows = conn.execute("""
        SELECT line_no, content, bm25(evidence) as score
        FROM evidence
        WHERE evidence MATCH ?
        ORDER BY score
        LIMIT ?
    """, (query, limit)).fetchall()
    return rows
```

**Validation**:
- Benchmark current vs. FTS retrieval on 1000 candidate queries
- Measure recall@10 for evidence snippets
- Test with 10KB, 100KB, 1MB sources
- **Drift test**: Modify source.md, verify next query rebuilds index

---

### H4: Vector Embedding Index for Semantic Search

**Hypothesis**: Dense embeddings enable semantic evidence retrieval when exact keyword matches fail.

**Testable outcome**:
- Metric: Recall@10 improves by 15% for abstract concept candidates
- Measurement: Compare to BM25-only baseline
- Target: Evidence found for 90% of candidates (vs. current ~70%)

**Critical design constraint: No knowledge base drift**

Same principle as H3 - embeddings are a derived cache:

1. **Single source of truth**: `raw/normalized/<slug>/source.md` remains canonical
2. **Index location**: `raw/normalized/<slug>/.embeddings/` (gitignored, co-located)
3. **Staleness detection**: Store source mtime in index metadata
4. **Rebuild on stale**: If source newer than index, rebuild before query

**Implementation**:
```python
def get_or_build_embeddings(source_path: Path, model: str = "all-MiniLM-L6-v2"):
    """Get existing embedding index or build fresh one. Never stale."""
    from sentence_transformers import SentenceTransformer
    import chromadb
    
    index_dir = source_path.parent / ".embeddings"
    meta_file = index_dir / "meta.json"
    source_mtime = source_path.stat().st_mtime
    
    if index_dir.exists() and meta_file.exists():
        import json
        meta = json.loads(meta_file.read_text())
        if meta.get("mtime", 0) >= source_mtime:
            client = chromadb.PersistentClient(path=str(index_dir))
            return client.get_collection(name="evidence")
        # Stale, remove and rebuild
        shutil.rmtree(index_dir)
    
    # Build fresh
    index_dir.mkdir(exist_ok=True)
    embedder = SentenceTransformer(model)
    client = chromadb.PersistentClient(path=str(index_dir))
    collection = client.create_collection(name="evidence")
    
    chunks = source_chunks(source_path.read_text())
    texts = [chunk.text for chunk in chunks]
    embeddings = embedder.encode(texts)
    
    collection.add(
        documents=texts,
        embeddings=embeddings.tolist(),
        ids=[chunk.locator for chunk in chunks],
        metadatas=[{"locator": chunk.locator} for chunk in chunks]
    )
    
    # Store metadata for staleness check
    import json
    meta_file.write_text(json.dumps({"mtime": source_mtime, "model": model}))
    
    return collection
```

**Validation**:
- Measure embedding build time (should be <30s for 1MB source)
- Compare recall for candidates where keyword match fails
- Test on domain-specific vocabulary (game terms, acronyms)
- **Drift test**: Modify source.md, verify next query rebuilds embeddings

---

### H5: Hybrid BM25 + Vector Search

**Hypothesis**: Combining BM25 (precision) with vector search (recall) produces the best evidence bank.

**Testable outcome**:
- Metric: Evidence quality score (judge-assessed) improves by 20%
- Measurement: A/B test evidence banks: BM25-only vs. hybrid
- Target: <5% "not covered in sources" claims that should have been covered

**Implementation**:
```python
def hybrid_search(source_path: Path, query: str, k: int = 10) -> list[SourceChunk]:
    """Reciprocal rank fusion of BM25 and vector results."""
    fts_conn = get_or_build_index(source_path)
    vector_index = get_or_build_embeddings(source_path)
    
    bm25_results = bm25_search(source_path, query, limit=k*2)
    vector_results = vector_index.query(query_texts=[query], n_results=k*2)
    
    # Reciprocal rank fusion
    scores = defaultdict(float)
    for rank, (line_no, content, _) in enumerate(bm25_results):
        scores[line_no] += 1 / (60 + rank)
    for rank, doc_id in enumerate(vector_results['ids'][0]):
        line_no = int(doc_id.split(':L')[1])
        scores[line_no] += 1 / (60 + rank)
    
    # Return top k by fused score
    return sorted(scores.items(), key=lambda x: -x[1])[:k]
```

**Validation**:
- Benchmark retrieval quality on 100 curated candidate/evidence pairs
- Measure judge pass rate for synthesized pages using each method
- A/B test on real ingest with same source, different evidence banks

---

### H5b: Wiki-Level Search Index

**Hypothesis**: A wiki-wide search index enables fast retrieval across all synthesized knowledge,
including conversation-derived analyses.

**Testable outcome**:
- Metric: Query page selection <50ms for wikis with 500+ pages
- Measurement: Compare to current `iter_content_pages()` + token overlap scan
- Target: Same recall with 20x faster selection

**Critical design constraint: Conversation knowledge flows through markdown first**

When new knowledge emerges from conversation:
1. **Save to markdown** (curator note or analysis) - this is the source of truth
2. **Invalidate wiki index** - mark as stale
3. **Next query rebuilds** - index auto-updates before returning results

```
User discovers insight in conversation
       ↓
Agent writes wiki/analyses/2026-05-05-insight.md
       ↓
Agent calls invalidate_wiki_index()
       ↓
Next query triggers rebuild_wiki_index()
       ↓
Insight is now searchable
```

**Implementation**:
```python
def rebuild_wiki_index(wiki_root: Path, index_path: Path) -> None:
    """Rebuild wiki-wide FTS index from all markdown files."""
    import sqlite3
    
    if index_path.exists():
        index_path.unlink()
    
    conn = sqlite3.connect(index_path)
    conn.execute("""
        CREATE VIRTUAL TABLE wiki_pages USING fts5(
            path, title, page_type, content, tokenize='porter'
        )
    """)
    conn.execute("CREATE TABLE meta (rebuilt_at REAL)")
    conn.execute("INSERT INTO meta VALUES (?)", (time.time(),))
    
    for page in wiki_root.rglob("*.md"):
        if page.name.startswith(".") or page.name.startswith("_"):
            continue
        fm = parse_frontmatter(page)
        title = fm.data.get("title", page.stem)
        page_type = fm.data.get("type", "unknown")
        content = page.read_text(errors="ignore")
        conn.execute(
            "INSERT INTO wiki_pages VALUES (?, ?, ?, ?)",
            (str(page.relative_to(wiki_root)), title, page_type, content)
        )
    
    conn.commit()
    conn.close()

def search_wiki(question: str, max_results: int = 10) -> list[dict]:
    """BM25 search over wiki pages."""
    wiki_root = Path("wiki")
    index_path = wiki_root / ".wiki-index.db"
    
    # Ensure index is fresh
    ensure_wiki_index_fresh(wiki_root, index_path)
    
    conn = sqlite3.connect(index_path)
    rows = conn.execute("""
        SELECT path, title, page_type, bm25(wiki_pages) as score
        FROM wiki_pages
        WHERE wiki_pages MATCH ?
        ORDER BY score
        LIMIT ?
    """, (question, max_results)).fetchall()
    
    return [{"path": r[0], "title": r[1], "type": r[2], "score": r[3]} for r in rows]
```

**Validation**:
- Benchmark current `select_pages()` vs. FTS-based selection
- Test with 100, 500, 1000 wiki pages
- **Conversation flow test**: File an analysis, verify it's immediately searchable

---

### H6: Context Budget Tracking

**Hypothesis**: Tracking token budget during prompt construction prevents context overflow.

**Testable outcome**:
- Metric: Zero context overflow failures
- Measurement: Log prompt token count before each codex invocation
- Target: Prompt + expected response < 80% of model context window

**Implementation**:
```python
@dataclass
class ContextBudget:
    """Track context budget during prompt construction."""
    max_tokens: int = 24000  # Conservative for 32K models
    reserved_for_response: int = 4000
    
    def __init__(self, model_context: int = 32000):
        self.max_tokens = int(model_context * 0.75)
        self.reserved_for_response = int(model_context * 0.125)
        self.used = 0
        self.components: list[tuple[str, int]] = []
    
    @property
    def available(self) -> int:
        return self.max_tokens - self.reserved_for_response - self.used
    
    def add(self, label: str, text: str) -> bool:
        """Add a component if it fits. Return False if it doesn't."""
        tokens = estimate_tokens(text)
        if tokens > self.available:
            return False
        self.used += tokens
        self.components.append((label, tokens))
        return True
    
    def report(self) -> str:
        lines = [f"Context budget: {self.used:,}/{self.max_tokens:,} tokens"]
        for label, tokens in self.components:
            lines.append(f"  {label}: {tokens:,}")
        return "\n".join(lines)
```

**Validation**:
- Instrument all codex invocations with budget tracking
- Log failures that would have been prevented
- Measure correlation between prompt size and success rate

---

### H7: Incremental Source Reading

**Hypothesis**: Phase 1 can extract structure from source outline + sampled sections instead of full source.

**Testable outcome**:
- Metric: Phase 1 success rate unchanged
- Measurement: Compare source page quality (claims, groupings, candidates)
- Target: Phase 1 context reduced by 80%

**Implementation**:
```python
def bounded_source_context(source_path: Path, budget: ContextBudget) -> str:
    """Build source context that fits budget."""
    outline = extract_outline(source_path)
    budget.add("outline", outline)
    
    sections = []
    for heading in parse_outline_headings(outline):
        section_text = read_section(source_path, heading.start_line, heading.end_line)
        if budget.add(f"section:{heading.title}", section_text):
            sections.append(section_text)
        else:
            # Add truncated sample instead
            sample = truncate_to_tokens(section_text, 500)
            if budget.add(f"sample:{heading.title}", sample):
                sections.append(sample)
    
    return f"{outline}\n\n---\n\n" + "\n\n---\n\n".join(sections)
```

**Validation**:
- Compare Phase 1 output (claims, groupings) using full vs. bounded context
- Measure context size reduction
- Test on sources with 50+, 100+, 500+ page equivalents

---

### H8: Parallel Chunk Processing

**Hypothesis**: Independent source sections can be processed in parallel for Phase 2.

**Testable outcome**:
- Metric: Wall-clock time for 10-page synthesis reduced by 60%
- Measurement: Compare sequential vs. parallel Phase 2
- Target: Multiple GPU utilization if available

**Implementation**:
```python
async def parallel_phase2(slug: str, candidates: list[str], max_parallel: int = 3):
    """Process independent Phase 2 candidates in parallel."""
    semaphore = asyncio.Semaphore(max_parallel)
    
    async def process_one(candidate: str):
        async with semaphore:
            return await run_phase2_single(slug, candidate)
    
    tasks = [process_one(c) for c in candidates]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

**Validation**:
- Benchmark sequential vs. parallel for 5, 10, 20 candidates
- Verify no resource contention issues
- Test with single GPU (sequential model calls)

---

## Implementation Priority

### Phase A: Reliability (High impact, low complexity)

1. **H1: Chunked PDF normalization** - Unblocks large PDF ingestion
2. **H6: Context budget tracking** - Prevents silent context overflow
3. **H2: Source outline extraction** - Reduces Phase 1 context

### Phase B: Search Quality (High impact, medium complexity)

4. **H3: SQLite FTS evidence index** - Faster, better evidence retrieval
5. **H5: Hybrid search** - Best-of-both-worlds evidence selection
6. **H5b: Wiki-level search index** - Fast query page selection, conversation knowledge searchable

### Phase C: Scalability (Medium impact, higher complexity)

7. **H7: Incremental source reading** - Handle 1000+ page sources
8. **H4: Vector embedding index** - Semantic search for edge cases
9. **H8: Parallel chunk processing** - Speed improvement

---

## Success Metrics

| Metric | Current | Target | Measurement |
|---|---|---|---|
| Large PDF normalization | Fails (segfault) | 100% success | marker exit code |
| Evidence retrieval time | ~2s for 100KB | <100ms | wall clock |
| Phase 1 context size | ~200KB | <40KB | token estimate |
| Context overflow failures | Unknown | 0 | log analysis |
| Evidence recall | ~70% | >90% | judge pass rate |
| Ingest automation | Manual split needed | Full automation | human intervention count |
| Wiki query page selection | ~500ms for 50 pages | <50ms for 500 pages | wall clock |
| Conversation→searchable latency | N/A (not indexed) | <1s | time from save to query hit |

---

## Testing Protocol

### Baseline Measurement

```bash
# Create test corpus
cp /path/to/small.pdf raw/inbox/test-small.pdf      # 5MB
cp /path/to/medium.pdf raw/inbox/test-medium.pdf    # 30MB
cp /path/to/large.pdf raw/inbox/test-large.pdf      # 100MB

# Measure current state
pnpm wiki:ingest raw/inbox/test-small.pdf --slug test-small --dry-run 2>&1 | tee baseline-small.log
pnpm wiki:ingest raw/inbox/test-medium.pdf --slug test-medium --dry-run 2>&1 | tee baseline-medium.log
```

### A/B Testing Per Hypothesis

For each hypothesis:
1. Implement behind a feature flag
2. Run 5 ingests with flag off (control)
3. Run 5 ingests with flag on (test)
4. Compare metrics
5. Statistical significance test (if applicable)

### Regression Suite

Add to `pnpm wiki:maintenance`:
```bash
# Context budget assertions
assert_prompt_tokens_under 24000
assert_evidence_retrieval_under 100ms
assert_phase0_success_rate 100%
```

---

## Appendix: Detailed Implementation Notes

### A1: PDF Chunking with pdftk

```bash
# Split into 30-page chunks
pdftk input.pdf cat 1-30 output chunk_001.pdf
pdftk input.pdf cat 31-60 output chunk_002.pdf
# ...

# Or use burst mode and recombine
pdftk input.pdf burst output page_%04d.pdf
for i in $(seq 1 30 $total_pages); do
  end=$((i + 29))
  pdftk page_*.pdf cat $i-$end output chunk_$(printf "%03d" $((i/30+1))).pdf
done
```

### A2: SQLite FTS5 Schema

**Per-source evidence index** (`raw/normalized/<slug>/.evidence.db`):
```sql
CREATE TABLE meta (mtime REAL);
CREATE VIRTUAL TABLE evidence USING fts5(
    line_no UNINDEXED,
    content,
    tokenize='porter unicode61'
);
```

**Wiki-wide search index** (`wiki/.wiki-index.db`):
```sql
CREATE TABLE meta (rebuilt_at REAL);
CREATE VIRTUAL TABLE wiki_pages USING fts5(
    path,           -- relative path from wiki/
    title,          -- from frontmatter
    page_type,      -- source, concept, entity, procedure, reference, analysis
    content,        -- full page text
    tokenize='porter unicode61'
);
CREATE INDEX idx_wiki_type ON wiki_pages(page_type);
```

The wiki index includes all content types, so conversation-derived analyses are immediately searchable alongside ingested source knowledge.

### A3: Embedding Model Selection

| Model | Size | Speed | Quality |
|---|---|---|---|
| all-MiniLM-L6-v2 | 80MB | Fast | Good |
| all-mpnet-base-v2 | 420MB | Medium | Better |
| bge-base-en-v1.5 | 440MB | Medium | Best |

For 4090 with VRAM constraints, prefer MiniLM for embedding during ingestion.

### A4: Hybrid Search Weights

Default reciprocal rank fusion constant k=60 works well for mixed queries.
Tune per domain if needed:
- Technical/precise queries: weight BM25 higher (k=40)
- Conceptual/semantic queries: weight vector higher (k=80)

### A5: Gitignore for Derived Indices

Add to `.gitignore` to prevent committing derived caches:

```gitignore
# Derived evidence indices (rebuildable from source)
raw/normalized/**/.evidence.db
raw/normalized/**/.embeddings/
```

These are intentionally not tracked because:
1. They're machine-specific (different sqlite versions, embedding models)
2. They're large (embeddings can be 10x source size)
3. They're rebuildable in seconds from the canonical source
4. Drift is impossible if they don't exist in git
