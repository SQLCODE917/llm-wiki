#!/usr/bin/env python3
"""Deep extraction workflow for comprehensive wiki ingestion.

This module implements chunked extraction to achieve 100% source coverage.
It processes sources in chunks, extracts claims from each chunk, aggregates
claims by topic, and synthesizes wiki pages from the aggregated claims.

The workflow is resumable - progress is saved after each chunk, so long
extractions can be interrupted and resumed.

Usage:
    # Dry run - show chunks without processing
    python3 tools/wiki_deep_extract.py <slug> --dry-run
    
    # Full extraction
    python3 tools/wiki_deep_extract.py <slug>
    
    # Resume interrupted extraction
    python3 tools/wiki_deep_extract.py <slug> --resume
    
    # Limit chunks (for testing)
    python3 tools/wiki_deep_extract.py <slug> --max-chunks 5
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

from wiki_common import log_context_stats, parse_frontmatter, section
from wiki_fill_evidence import fill_evidence_in_page
from wiki_model_backend import get_backend, ModelConfig, ModelResponse

# Import extraction state management for new state file format
from wiki_extraction_state import (
    RawClaim,
    NormalizedClaim,
    NormalizedClaimsData,
    Candidate,
    GeneratedCandidatesData,
    append_raw_claims,
    save_normalized_claims,
    save_generated_candidates,
    get_raw_claims_path,
)
from wiki_candidate_tracker import (
    CandidatesData,
    load_candidates,
    normalize_candidate_name,
    save_candidates,
    register_candidate,
)

# Structured chunking support (optional import)
try:
    from wiki_structured_chunking import (
        BlockExtractor,
        StructuralChunker,
        ChunkConfig,
        StructuredChunk,
        count_tokens,
        assess_extraction_quality,
        save_blocks,
        save_chunks as save_structured_chunks,
    )
    HAS_STRUCTURED_CHUNKING = True
except ImportError:
    HAS_STRUCTURED_CHUNKING = False


# ============================================================================
# Data Structures
# ============================================================================


def normalize_claim_text(text: str) -> str:
    """Normalize claim text for hashing.

    Trim whitespace, collapse repeated spaces, normalize Unicode.
    Do NOT lowercase - code, symbols, and proper nouns may be case-sensitive.
    """
    import unicodedata
    # Normalize Unicode to NFC form
    text = unicodedata.normalize("NFC", text)
    # Collapse whitespace
    text = " ".join(text.split())
    return text.strip()


def generate_claim_id(slug: str, claim_text: str, locator: str, chunk_index: int) -> str:
    """Generate a stable, deterministic claim ID.

    Format: claim_<slug>_c<chunk-index>_<8-char-hash>

    The hash is derived from normalized claim text + primary evidence locator.
    This ensures:
    - Same input → same ID (reproducible)
    - Does not shift if earlier claims change (unlike sequence numbers)
    - Chunk index visible in ID for debugging
    """
    normalized = normalize_claim_text(claim_text)
    hash_input = f"{normalized}|{locator}"
    hash_bytes = hashlib.sha256(hash_input.encode("utf-8")).digest()
    hash_hex = hash_bytes[:4].hex()  # 8 hex chars

    # Handle empty slug (will be updated later when slug is known)
    slug_part = slug if slug else "unknown"
    return f"claim_{slug_part}_c{chunk_index:03d}_{hash_hex}"


@dataclass
class Chunk:
    """A chunk of source text to process."""
    index: int
    start_line: int
    end_line: int
    title: str = ""

    @property
    def line_count(self) -> int:
        return self.end_line - self.start_line + 1

    def to_dict(self) -> dict:
        return {
            "index": self.index,
            "start": self.start_line,
            "end": self.end_line,
            "lines": self.line_count,
            "title": self.title,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Chunk":
        return cls(
            index=d["index"],
            start_line=d["start"],
            end_line=d["end"],
            title=d.get("title", ""),
        )


@dataclass
class Claim:
    """An extracted claim with evidence."""
    topic: str
    claim: str
    evidence: str
    locator: str
    chunk_index: int
    claim_id: str = ""

    def __post_init__(self):
        """Generate claim_id if not set."""
        if not self.claim_id:
            self.claim_id = generate_claim_id(
                "", self.claim, self.locator, self.chunk_index)

    def to_dict(self) -> dict:
        return {
            "claim_id": self.claim_id,
            "topic": self.topic,
            "claim": self.claim,
            "evidence": self.evidence,
            "locator": self.locator,
            "chunk_index": self.chunk_index,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Claim":
        return cls(
            topic=d.get("topic", ""),
            claim=d.get("claim", ""),
            evidence=d.get("evidence", ""),
            locator=d.get("locator", ""),
            chunk_index=d.get("chunk_index", 0),
            claim_id=d.get("claim_id", ""),
        )


@dataclass
class ExtractionState:
    """State of an extraction run, persisted for resumability.
    
    CONSOLIDATION NOTE (2026-05):
    This class is still used during the extraction phase for:
    - Tracking which chunks have been processed
    - Accumulating claims in memory
    - Checkpoint saving to .tmp/deep-extract/<slug>/state.json
    
    After extraction completes, claims-normalized.json in .wiki-extraction-state/
    is the canonical source. load_extraction_state() now loads from there,
    constructing an ExtractionState for backward compatibility with synthesis code.
    
    The state.json in .tmp/ is ephemeral extraction checkpoint, not the source of truth.
    """
    slug: str
    source_path: str
    total_lines: int
    chunks: list[Chunk]
    processed_chunks: set[int] = field(default_factory=set)
    claims: list[Claim] = field(default_factory=list)
    topics: dict[str, list[Claim]] = field(default_factory=dict)
    pages_created: list[str] = field(default_factory=list)
    started_at: str = ""
    last_updated: str = ""

    def to_dict(self) -> dict:
        return {
            "slug": self.slug,
            "source_path": self.source_path,
            "total_lines": self.total_lines,
            "chunks": [c.to_dict() for c in self.chunks],
            "processed_chunks": list(self.processed_chunks),
            "claims": [c.to_dict() for c in self.claims],
            "topics": {k: [c.to_dict() for c in v] for k, v in self.topics.items()},
            "pages_created": self.pages_created,
            "started_at": self.started_at,
            "last_updated": self.last_updated,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "ExtractionState":
        state = cls(
            slug=d["slug"],
            source_path=d["source_path"],
            total_lines=d["total_lines"],
            chunks=[Chunk.from_dict(c) for c in d["chunks"]],
            processed_chunks=set(d.get("processed_chunks", [])),
            claims=[Claim.from_dict(c) for c in d.get("claims", [])],
            pages_created=d.get("pages_created", []),
            started_at=d.get("started_at", ""),
            last_updated=d.get("last_updated", ""),
        )
        # Rebuild topics from claims
        state._rebuild_topics()
        return state

    def _rebuild_topics(self):
        """Rebuild topics dict from claims list."""
        self.topics = {}
        for claim in self.claims:
            if claim.topic not in self.topics:
                self.topics[claim.topic] = []
            self.topics[claim.topic].append(claim)

    def save(self, path: Path):
        """Save state to disk."""
        self.last_updated = date.today().isoformat()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2))

    @classmethod
    def load(cls, path: Path) -> "ExtractionState":
        """Load state from disk."""
        return cls.from_dict(json.loads(path.read_text()))


# ============================================================================
# Chunking - Data-driven, works for any source
# ============================================================================

def create_chunks(source_path: Path, chunk_size: int = 400, overlap: int = 30) -> list[Chunk]:
    """Create overlapping chunks from source.

    Chunk size is tuned for ~1600 tokens (assuming 4 chars/token).
    This leaves room in a 16K context for:
    - Prompt overhead: ~800 tokens
    - Chunk content: ~1600 tokens  
    - Output: ~4000 tokens
    - Safety margin: ~9K tokens

    Chunks break at natural boundaries when possible (blank lines, page markers).
    """
    lines = source_path.read_text().splitlines()
    total_lines = len(lines)

    chunks = []
    start = 1
    chunk_index = 0

    while start <= total_lines:
        # Calculate tentative end
        end = min(start + chunk_size - 1, total_lines)

        # Only look for natural breaks in the last 20% of the chunk
        if end < total_lines:
            search_start = max(start + int(chunk_size * 0.8), end - 50)
            best_break = end
            for i in range(end, search_start, -1):
                line = lines[i - 1].strip()
                # Prefer breaking at page markers
                if '<!-- page' in line.lower():
                    best_break = i
                    break
                # Or at horizontal rules
                if line == '---':
                    best_break = i
                    break
                # Or at blank lines (but only as last resort)
                if not line and best_break == end:
                    best_break = i
            end = best_break

        # Extract a title from the chunk content
        title = extract_chunk_title(lines, start, end)

        chunks.append(Chunk(
            index=chunk_index,
            start_line=start,
            end_line=end,
            title=title,
        ))

        # Move to next chunk with overlap
        # Ensure we always make progress
        next_start = end - overlap + 1
        if next_start <= start:
            next_start = start + chunk_size // 2  # Force progress
        start = next_start
        chunk_index += 1

        # Safety: prevent runaway (allow up to 200 chunks for very large docs)
        if chunk_index > 200:
            print(f"WARN: Stopping at {chunk_index} chunks (safety limit)")
            break

    return chunks


def extract_chunk_title(lines: list[str], start: int, end: int) -> str:
    """Extract a descriptive title from chunk content."""
    # Look for headings or page titles
    for i in range(start - 1, min(start + 30, end)):
        if i >= len(lines):
            break
        line = lines[i].strip()

        # Skip empty, markers, TOC-style lines
        if not line:
            continue
        if line.startswith('<!--'):
            continue
        if line.startswith('---'):
            continue
        if re.match(r'^[\.\s]+$', line):
            continue
        if re.match(r'^\d+$', line):
            continue

        # Use headings
        if line.startswith('#'):
            return line.lstrip('#').strip()[:60]

        # Use substantive text
        if len(line) > 15 and len(line) < 80:
            # Clean up TOC remnants
            clean = line.split(' . . .')[0].strip()
            if len(clean) > 10:
                return clean[:60]

    return f"Chunk {start}-{end}"


def create_structured_chunks(
    source_path: Path,
    doc_id: str,
    target_tokens: int = 6500,
    soft_max_tokens: int = 7500,
    hard_max_tokens: int = 9000,
) -> tuple[list[Chunk], dict]:
    """Create chunks using token-aware structural packing.

    Returns:
        Tuple of (list of legacy Chunk objects, metadata dict)
    """
    if not HAS_STRUCTURED_CHUNKING:
        raise ImportError("Structured chunking not available")

    source_text = source_path.read_text()

    # Extract blocks
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(source_text, doc_id)

    # Pack into structured chunks
    config = ChunkConfig(
        target_tokens=target_tokens,
        soft_max_tokens=soft_max_tokens,
        hard_max_tokens=hard_max_tokens,
    )
    chunker = StructuralChunker(config)
    structured_chunks = chunker.pack(blocks, doc_id)

    # Assess quality
    quality = assess_extraction_quality(blocks, structured_chunks)

    # Convert to legacy Chunk format for compatibility
    legacy_chunks = []
    for i, sc in enumerate(structured_chunks):
        legacy_chunks.append(Chunk(
            index=i,
            start_line=sc.line_start,
            end_line=sc.line_end,
            title=' > '.join(
                sc.section_path) if sc.section_path else f"Chunk {i+1}",
        ))

    metadata = {
        "block_count": len(blocks),
        "chunk_count": len(structured_chunks),
        "total_tokens": quality.total_tokens,
        "avg_tokens_per_chunk": quality.total_tokens / len(structured_chunks) if structured_chunks else 0,
        "pages_needing_review": quality.pages_needing_review,
        "issues_by_type": quality.issues_by_type,
        "structured_chunks": structured_chunks,  # Keep for later use
        "blocks": blocks,
    }

    return legacy_chunks, metadata


def get_structured_chunk_text(
    source_path: Path,
    chunk: Chunk,
    metadata: dict,
    context_lines: int = 0,  # Not used with structured chunking
) -> str:
    """Get chunk text for a structured chunk.

    Uses the pre-packed structured chunk with context headers.
    """
    structured_chunks = metadata.get("structured_chunks", [])

    if chunk.index < len(structured_chunks):
        sc = structured_chunks[chunk.index]
        # Render with context header and line numbers
        lines = sc.text.split('\n')
        result = []

        # Add context header if present
        if sc.context_header:
            result.append(sc.context_header)
            result.append("")

        # Add content with line numbers
        for i, line in enumerate(lines):
            line_num = sc.line_start + i
            result.append(f"L{line_num}: {line}")

        return '\n'.join(result)

    # Fallback to original method
    return get_chunk_text(source_path, chunk, context_lines)


def get_chunk_text(source_path: Path, chunk: Chunk, context_lines: int = 10) -> str:
    """Extract chunk text with line numbers for evidence locators."""
    lines = source_path.read_text().splitlines()

    # Include a bit of context before/after
    ctx_start = max(0, chunk.start_line - 1 - context_lines)
    ctx_end = min(len(lines), chunk.end_line + context_lines)

    result = []
    for i in range(ctx_start, ctx_end):
        line_num = i + 1
        # Mark focus lines vs context
        if chunk.start_line <= line_num <= chunk.end_line:
            result.append(f"L{line_num}: {lines[i]}")
        else:
            result.append(f"L{line_num}: [ctx] {lines[i]}")

    return "\n".join(result)


# ============================================================================
# Claim Extraction - Per-chunk processing
# ============================================================================

def build_extraction_prompt(chunk: Chunk, chunk_text: str, slug: str, total_chunks: int) -> str:
    """Build prompt for extracting claims from a chunk."""
    return f"""You are extracting wiki-worthy claims from a source document.

SOURCE: {slug}
CHUNK: {chunk.index + 1} of {total_chunks} (Lines {chunk.start_line}-{chunk.end_line})
TITLE: {chunk.title}

CONTENT (lines starting with L### are line numbers, [ctx] marks context):
{chunk_text}

TASK: Extract the most important concrete, reusable claims from this chunk (up to 25 claims maximum). Prioritize claims that teach concepts, patterns, or techniques. If this chunk is dense with many potential claims, focus on the most foundational and widely applicable ones.

TOPIC GUIDELINES - Derive topics from the source material, using BROAD categories:
- Prefer parent concepts over sub-variants (e.g., "Memory Management" not "Stack vs Heap")
- Group related techniques under one umbrella (e.g., "Search Algorithms" not "Binary Search")
- Use domain-appropriate terminology from the source itself
- Aim for 5-15 distinct topics across the entire document

Examples of the BROAD vs NARROW pattern (adapt to your domain):
- Programming: "Functions" not "Arrow Functions", "Data Structures" not "Linked Lists"
- Strategy games: "Economy" not "Wood Gathering", "Military Units" not "Archer Rush"  
- Science: "Thermodynamics" not "Heat Transfer", "Cell Biology" not "Mitochondria"
- History: "Political Systems" not "Roman Senate", "Trade Routes" not "Silk Road"

RULES:
1. Extract ONLY claims that teach something useful and reusable
2. Each claim must have a VERBATIM quote as evidence from the numbered lines
3. The locator must be a line range (e.g., "normalized:L100-L100" for one line, "normalized:L100-L102" for multiple)
4. Use BROAD topic names from the guidelines above
5. Skip: TOC entries, copyright notices, page numbers, marketing text, author bios
6. If this chunk has no teachable content, return an empty array []

EVIDENCE RULES (CRITICAL):
- Evidence must be EXACT TEXT from the source - copy character-for-character
- Do NOT add comments, annotations, or explanations to evidence
- Do NOT paraphrase, summarize, or modify evidence text
- For code snippets: copy ONLY the code that appears in the source
- WRONG: "for (const ee of tree(e)) {{ yield ee; }} // yields all elements"
- RIGHT: "for (const ee of tree(e)) {{ yield ee; }}"

OUTPUT FORMAT - Return ONLY a JSON array:
```json
[
  {{
    "topic": "Broad topic name derived from source domain",
    "claim": "Concrete statement in your own words - what the reader should learn",
    "evidence": "VERBATIM quote from source (under 200 chars, no modifications)",
    "locator": "normalized:L<start>-L<end>"
  }}
]
```

IMPORTANT:
- Return valid JSON only, no other text
- Use double quotes for JSON strings
- Escape special characters in evidence
- If no claims, return: []"""


def extract_claims_from_chunk(
    backend,
    state: ExtractionState,
    chunk: Chunk,
    source_path: Path,
    timeout: int = 120,
    chunk_text: str = "",
) -> list[Claim]:
    """Extract claims from a single chunk using the model backend."""
    if not chunk_text:
        chunk_text = get_chunk_text(source_path, chunk)
    prompt = build_extraction_prompt(
        chunk, chunk_text, state.slug, len(state.chunks))

    log_context_stats(
        prompt, label=f"Chunk {chunk.index + 1}/{len(state.chunks)}")

    config = ModelConfig(
        worktree=Path.cwd(),
        prefix=f"deep-chunk-{chunk.index}",
        timeout=timeout,
        system_prompt_style="extract",
    )

    response = backend.run(prompt, config)
    if not response.success:
        print(f"    Model error: {response.error}")
        return []

    # Parse JSON response
    claims = parse_claims_response(response.output, chunk.index, state.slug)
    return claims


def repair_truncated_json(json_str: str) -> str:
    """Attempt to repair truncated JSON arrays from max_tokens cutoff.

    When a model hits max_tokens, the JSON array may be truncated mid-object.
    This function tries to recover the complete claims by:
    1. Removing the last incomplete object
    2. Closing the array properly

    Returns the repaired JSON string, or original if repair not applicable.
    """
    # Check if it looks like a truncated array
    if not json_str.strip().startswith('['):
        return json_str

    # If it already ends with ], nothing to repair
    if json_str.rstrip().endswith(']'):
        return json_str

    # Find the last complete object by looking for }, followed by potential whitespace
    # Work backwards from end
    last_complete = -1
    depth = 0
    in_string = False
    escape_next = False

    for i, char in enumerate(json_str):
        if escape_next:
            escape_next = False
            continue
        if char == '\\' and in_string:
            escape_next = True
            continue
        if char == '"' and not escape_next:
            in_string = not in_string
            continue
        if in_string:
            continue
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0:
                # Found complete object at top level of array
                last_complete = i

    if last_complete > 0:
        # Truncate after last complete object and close the array
        repaired = json_str[:last_complete + 1].rstrip()
        # Remove trailing comma if present
        if repaired.endswith(','):
            repaired = repaired[:-1]
        repaired += ']'
        return repaired

    return json_str


def parse_claims_response(output: str, chunk_index: int, slug: str = "") -> list[Claim]:
    """Parse model output into Claim objects."""
    # Try to extract JSON from response
    json_match = re.search(r'```(?:json)?\s*\n?(.*?)```', output, re.DOTALL)
    if json_match:
        json_str = json_match.group(1).strip()
    else:
        # Try to find raw JSON array
        json_match = re.search(r'\[\s*\{.*\}\s*\]', output, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
        else:
            # Maybe it's just []
            if '[]' in output:
                return []
            print(f"    Could not find JSON in response")
            return []

    try:
        data = json.loads(json_str)
        if not isinstance(data, list):
            print(f"    Response is not a list")
            return []

        claims = []
        for item in data:
            if isinstance(item, dict) and all(k in item for k in ['topic', 'claim', 'evidence', 'locator']):
                claim_text = str(item['claim']).strip()
                locator = str(item['locator']).strip()
                claim_id = generate_claim_id(
                    slug, claim_text, locator, chunk_index)
                claims.append(Claim(
                    topic=str(item['topic']).strip(),
                    claim=claim_text,
                    evidence=str(item['evidence']).strip(),
                    locator=locator,
                    chunk_index=chunk_index,
                    claim_id=claim_id,
                ))
        return claims
    except json.JSONDecodeError as e:
        # Try to repair truncated JSON (common with max_tokens cutoff)
        repaired = repair_truncated_json(json_str)
        if repaired != json_str:
            try:
                data = json.loads(repaired)
                if isinstance(data, list):
                    claims = []
                    for item in data:
                        if isinstance(item, dict) and all(k in item for k in ['topic', 'claim', 'evidence', 'locator']):
                            claim_text = str(item['claim']).strip()
                            locator = str(item['locator']).strip()
                            claim_id = generate_claim_id(
                                slug, claim_text, locator, chunk_index)
                            claims.append(Claim(
                                topic=str(item['topic']).strip(),
                                claim=claim_text,
                                evidence=str(item['evidence']).strip(),
                                locator=locator,
                                chunk_index=chunk_index,
                                claim_id=claim_id,
                            ))
                    print(
                        f"    Recovered {len(claims)} claims from truncated JSON")
                    return claims
            except json.JSONDecodeError:
                pass
        print(f"    JSON parse error: {e}")
        return []


# ============================================================================
# Claim Aggregation - Group by topic, deduplicate
# ============================================================================

def aggregate_claims_by_topic(claims: list[Claim]) -> dict[str, list[Claim]]:
    """Group claims by topic and deduplicate."""
    topics: dict[str, list[Claim]] = {}

    for claim in claims:
        # Normalize topic name
        topic = normalize_topic_name(claim.topic)

        if topic not in topics:
            topics[topic] = []

        # Check for duplicates (same claim text or very similar)
        is_duplicate = False
        for existing in topics[topic]:
            if is_similar_claim(claim, existing):
                is_duplicate = True
                break

        if not is_duplicate:
            topics[topic].append(claim)

    return topics


def normalize_topic_name(topic: str) -> str:
    """Normalize topic names for consistent grouping.
    
    Performs basic cleanup without domain-specific mappings.
    The extraction prompt now guides the model to choose broad topics upfront.
    """
    # Remove common prefixes/suffixes that add no information
    topic = topic.strip()
    
    # Remove "Introduction to", "Basics of", etc.
    topic = re.sub(r'^(Introduction to|Basics of|Overview of|Guide to)\s+', '', topic, flags=re.IGNORECASE)
    
    # Remove trailing qualifiers
    topic = re.sub(r'\s+(Basics|Overview|Introduction|Guide)$', '', topic, flags=re.IGNORECASE)
    
    # Title case for consistency
    topic = topic.title()
    
    # Collapse multiple spaces
    topic = re.sub(r'\s+', ' ', topic)
    
    return topic.strip()


def is_similar_claim(a: Claim, b: Claim) -> bool:
    """Check if two claims are similar enough to be duplicates."""
    # Exact match
    if a.claim.lower() == b.claim.lower():
        return True

    # Same locator (likely same source line)
    if a.locator == b.locator:
        return True

    # High word overlap
    words_a = set(a.claim.lower().split())
    words_b = set(b.claim.lower().split())
    if len(words_a) > 3 and len(words_b) > 3:
        overlap = len(words_a & words_b) / min(len(words_a), len(words_b))
        if overlap > 0.8:
            return True

    return False


# ============================================================================
# Page Synthesis - Turn aggregated claims into wiki pages
# ============================================================================

def synthesize_pages(
    backend,
    state: ExtractionState,
    min_claims_per_page: int = 3,
    max_claims_per_page: int = 12,
    timeout: int = 180,
) -> list[Path]:
    """Synthesize wiki pages from aggregated claims."""
    created_pages = []

    # Filter topics with enough claims
    viable_topics = {
        topic: claims
        for topic, claims in state.topics.items()
        if len(claims) >= min_claims_per_page
    }

    print(
        f"\nSynthesizing {len(viable_topics)} pages from {len(state.topics)} topics")
    print(f"(Topics with < {min_claims_per_page} claims are skipped)")

    for i, (topic, claims) in enumerate(viable_topics.items(), 1):
        print(f"\n[{i}/{len(viable_topics)}] {topic} ({len(claims)} claims)")

        # Limit claims if too many
        if len(claims) > max_claims_per_page:
            # Take claims from different chunks for diversity
            claims = select_diverse_claims(claims, max_claims_per_page)

        page_path = synthesize_single_page(
            backend, state.slug, topic, claims, Path(state.source_path), timeout)
        if page_path:
            created_pages.append(page_path)
            print(f"    Created: {page_path}")

    return created_pages


def select_diverse_claims(claims: list[Claim], max_count: int) -> list[Claim]:
    """Select diverse claims from different parts of the source."""
    # Sort by chunk index
    sorted_claims = sorted(claims, key=lambda c: c.chunk_index)

    # Take evenly spaced claims
    step = len(sorted_claims) / max_count
    selected = []
    for i in range(max_count):
        idx = int(i * step)
        if idx < len(sorted_claims):
            selected.append(sorted_claims[idx])

    return selected


def synthesize_single_page(
    backend,
    slug: str,
    topic: str,
    claims: list[Claim],
    normalized_source: Path,
    timeout: int = 180,
) -> Path | None:
    """Synthesize a single wiki page from claims.

    The LLM writes a 3-column table (Claim | Locator | Source).
    Evidence cells are filled deterministically from the normalized source.
    """
    # Determine page type and path
    page_slug = topic.lower().replace(' ', '-').replace('/', '-')
    page_slug = re.sub(r'[^a-z0-9-]', '', page_slug)
    page_path = Path(f"wiki/concepts/{page_slug}.md")

    # Skip if exists
    if page_path.exists():
        print(f"    Skipping (exists): {page_path}")
        return page_path

    # Build claims table for prompt (include locators, LLM doesn't write evidence)
    claims_table = []
    for c in claims:
        claims_table.append(f"- Topic: {c.topic}")
        claims_table.append(f"  Claim: {c.claim}")
        claims_table.append(f"  Locator: {c.locator}")
        claims_table.append("")

    prompt = build_synthesis_prompt(slug, topic, page_slug, claims_table)
    log_context_stats(prompt, label=f"Synthesis: {topic}")

    config = ModelConfig(
        worktree=Path.cwd(),
        prefix=f"deep-synth-{page_slug}",
        timeout=timeout,
        system_prompt_style="synthesis",
    )

    response = backend.run(prompt, config)
    if not response.success:
        print(f"    Model error: {response.error}")
        return None

    # Extract markdown
    content = extract_markdown(response.output)
    if not content:
        print(f"    Could not extract markdown from response")
        return None

    # Post-process
    content = postprocess_page(content)

    # Fill evidence cells deterministically from locators
    if normalized_source.exists():
        source_lines = normalized_source.read_text(
            errors="ignore").splitlines()
        content, changes = fill_evidence_in_page(content, source_lines)
        if changes:
            print(f"    Filled {len(changes)} evidence cells")

    # Write page
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text(content)

    return page_path


def build_synthesis_prompt(slug: str, topic: str, page_slug: str, claims_table: list[str]) -> str:
    """Build prompt for synthesizing a wiki page."""
    today = date.today().isoformat()
    claims_text = "\n".join(claims_table)

    return f"""Create a wiki concept page from these extracted claims.

TOPIC: {topic}
SOURCE: {slug}

EXTRACTED CLAIMS (with locators):
{claims_text}

CREATE: wiki/concepts/{page_slug}.md

REQUIREMENTS:
1. Use this exact structure with a **3-column table** (no Evidence column):

```markdown
---
title: {topic}
type: concept
tags: []
status: draft
last_updated: {today}
sources:
  - ../sources/{slug}.md
---

# {topic}

<One paragraph definition/summary synthesized from the claims>

## Source-backed details

| Claim | Locator | Source |
|---|---|---|
| <Synthesize the claim in your own words> | `<locator>` | [Source](../sources/{slug}.md) |

## Why it matters

<Explain significance based on the claims>

## Source pages

- [Source](../sources/{slug}.md)
```

2. Include ALL provided claims in the table
3. Synthesize claims in YOUR OWN WORDS (do not copy verbatim)
4. Use the locators exactly as provided
5. Do NOT write an Evidence column - it is filled automatically
6. Do NOT invent claims not in the provided list

OUTPUT: Return ONLY the markdown content."""


def extract_markdown(output: str) -> str | None:
    """Extract markdown from model response."""
    # Try fenced code block
    match = re.search(r'```(?:markdown|md)?\s*\n(.*?)```', output, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Try to find frontmatter
    if output.strip().startswith('---'):
        return output.strip()

    match = re.search(r'(---\n.*?---\n.*)', output, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Fall back to whole response if substantial
    if len(output) > 200 and '# ' in output:
        return output.strip()

    return None


def postprocess_page(content: str) -> str:
    """Clean up generated page content."""
    # Normalize ASCII
    replacements = {
        '"': '"', '"': '"', ''': "'", ''': "'",
        '—': '--', '–': '-', '…': '...',
    }
    for old, new in replacements.items():
        content = content.replace(old, new)

    # Fix locator format
    content = re.sub(r"'(normalized:L\d+(?:-L\d+)?)'", r'`\1`', content)

    return content


# ============================================================================
# Finalization - Update source page, index, graph
# ============================================================================

def finalize_extraction(state: ExtractionState) -> int:
    """Finalize extraction: update source page, index, graph, log."""
    import subprocess

    print("\n" + "=" * 60)
    print("PHASE 4: Finalize")
    print("=" * 60)

    # Update source page Related pages section
    source_page = Path(f"wiki/sources/{state.slug}.md")
    if source_page.exists():
        update_source_related_pages(source_page, state)
        print(f"Updated: {source_page}")

    # Run link-related to convert candidates to links
    print("\nUpdating related page links...")
    subprocess.run(["python3", "tools/wiki_link_related.py",
                   state.slug], cwd=Path.cwd())

    # Update index
    print("Updating index...")
    subprocess.run(["python3", "tools/wiki_index.py"], cwd=Path.cwd())

    # Update graph
    print("Updating graph...")
    subprocess.run(["python3", "tools/wiki_graph.py"], cwd=Path.cwd())

    # Add log entry
    print("Adding log entry...")
    pages_list = ", ".join(Path(p).stem for p in state.pages_created[:5])
    if len(state.pages_created) > 5:
        pages_list += f", +{len(state.pages_created) - 5} more"

    subprocess.run([
        "python3", "tools/wiki_log.py",
        "ingest",
        f"Deep extraction of {state.slug}",
        "-d", f"Chunks: {len(state.processed_chunks)}, Claims: {len(state.claims)}, Topics: {len(state.topics)}, Pages: {len(state.pages_created)}. Created: {pages_list}",
    ], cwd=Path.cwd())

    return 0


def update_source_related_pages(source_page: Path, state: ExtractionState):
    """Add synthesized pages to source page's Related pages section."""
    content = source_page.read_text()

    # Find or create Related pages section
    if "## Related pages" not in content:
        content += "\n\n## Related pages\n\n"
        content += "| Candidate page | Intended path | Group | Priority | Evidence basis | Status |\n"
        content += "|---|---|---|---|---|---|\n"

    # Add entries for created pages
    for page_path_str in state.pages_created:
        page_path = Path(page_path_str)
        page_name = page_path.stem.replace('-', ' ').title()
        rel_path = f"../{page_path.parent.name}/{page_path.name}"

        # Check if already in table
        if rel_path in content:
            continue

        # Find the topic for this page
        topic = page_name
        for t in state.topics:
            if t.lower().replace(' ', '-') in page_path.stem:
                topic = t
                break

        # Add as a link (not candidate)
        row = f"| {page_name} | [{rel_path}]({rel_path}) | Deep extraction | must create | {len(state.topics.get(topic, []))} claims | created |\n"

        # Insert before last row or at end of table
        lines = content.splitlines()
        insert_idx = len(lines)
        for i, line in enumerate(lines):
            if line.startswith("| ") and "## " not in line and i > 0:
                insert_idx = i + 1

        lines.insert(insert_idx, row.strip())
        content = "\n".join(lines)

    source_page.write_text(content)


# ============================================================================
# API for unified ingest
# ============================================================================

def get_state_path(slug: str) -> Path:
    """Get the legacy state file path for a slug.
    
    DEPRECATED: State is now stored in claims-normalized.json.
    This path is only used for backward compatibility during migration.
    """
    return Path(f".tmp/deep-extract/{slug}/state.json")


def load_extraction_state(slug: str) -> ExtractionState | None:
    """Load extraction state for a slug.
    
    This now loads from claims-normalized.json (the canonical source)
    and constructs an ExtractionState object for backward compatibility.
    
    The old .tmp/deep-extract/<slug>/state.json is no longer used as
    the primary source - claims-normalized.json in .wiki-extraction-state/
    is the source of truth after extraction completes.
    """
    # Import here to avoid circular dependency
    from wiki_extraction_state import (
        load_normalized_claims,
        get_processed_chunk_indices,
        get_normalized_claims_path,
    )
    
    # Try to load from normalized claims (new canonical location)
    normalized = load_normalized_claims(slug)
    if normalized is None:
        # Fall back to legacy state.json for backward compatibility
        state_path = get_state_path(slug)
        if state_path.exists():
            return ExtractionState.load(state_path)
        return None
    
    # Convert NormalizedClaim to Claim objects
    claims = [
        Claim(
            topic=nc.topic,
            claim=nc.claim,
            evidence=nc.evidence,
            locator=nc.locator,
            chunk_index=nc.chunk_index,
            claim_id=nc.claim_id,
        )
        for nc in normalized.claims
    ]
    
    # Build topics dict with Claim objects
    claim_by_id = {c.claim_id: c for c in claims}
    topics: dict[str, list[Claim]] = {}
    for topic, claim_ids in normalized.topics.items():
        claims_for_topic = [claim_by_id[cid] for cid in claim_ids if cid in claim_by_id]
        if claims_for_topic:
            topics[topic] = claims_for_topic
    
    # Get processed chunks from raw claims
    processed_chunks = get_processed_chunk_indices(slug)
    
    # Determine source path
    source_path = Path(f"raw/normalized/{slug}/source.md")
    total_lines = 0
    if source_path.exists():
        total_lines = len(source_path.read_text().splitlines())
    
    # Create ExtractionState with derived data
    # Note: chunks list is empty as it's only needed during extraction, not synthesis
    state = ExtractionState(
        slug=slug,
        source_path=str(source_path),
        total_lines=total_lines,
        chunks=[],  # Not needed for synthesis
        processed_chunks=processed_chunks,
        claims=claims,
        topics=topics,
        pages_created=[],  # Can be derived from wiki/ if needed
        started_at=normalized.normalized_at,
        last_updated=normalized.normalized_at,
    )
    
    return state


def score_claim_specificity(claim: Claim) -> float:
    """Score a claim for specificity (higher = more concrete/useful).

    Used for High-Signal Claims ranking in source pages.
    """
    score = 0.0
    text = claim.claim.lower()
    evidence = claim.evidence.lower() if claim.evidence else ""

    # Contains numbers (concrete)
    if re.search(r'\d+', text):
        score += 0.15

    # Contains code (concrete)
    if re.search(r'`[^`]+`', claim.claim):
        score += 0.15

    # Technical terms
    if any(term in text for term in ['function', 'returns', 'parameter', 'argument', 'closure', 'scope']):
        score += 0.10

    # Substantial evidence
    if len(evidence) > 50:
        score += 0.10

    # Evidence contains code
    if re.search(r'`[^`]+`', evidence):
        score += 0.10

    return min(score, 1.0)


def extract_source_locator_map(source_lines: list[str]) -> list[tuple[int, int, str]]:
    """Extract heading ranges from normalized source.

    Returns list of (start_line, end_line, heading_text) tuples.
    """
    headings = []
    current_heading = None
    current_start = 1

    for i, line in enumerate(source_lines, start=1):
        # Check for markdown headings (# or ##)
        if line.startswith('#'):
            # Close previous heading range
            if current_heading:
                headings.append((current_start, i - 1, current_heading))

            # Start new heading
            current_heading = line.lstrip('#').strip()[:60]
            current_start = i

    # Close final heading
    if current_heading:
        headings.append((current_start, len(source_lines), current_heading))

    return headings


def get_heading_for_line(line_num: int, locator_map: list[tuple[int, int, str]]) -> str:
    """Find the heading that contains a given line number."""
    for start, end, heading in locator_map:
        if start <= line_num <= end:
            return heading
    return "unknown"


def count_sections_for_topic(claims: list[Claim], locator_map: list[tuple[int, int, str]]) -> int:
    """Count distinct source sections covered by claims for a topic."""
    sections = set()
    for claim in claims:
        # Parse locator to get line number
        match = re.match(r'normalized:L(\d+)', claim.locator)
        if match:
            line_num = int(match.group(1))
            heading = get_heading_for_line(line_num, locator_map)
            sections.add(heading)
    return len(sections)


def _infer_namespace(slug: str) -> str | None:
    """Infer ecosystem namespace from source slug.

    Used to prevent cross-ecosystem naming collisions.
    e.g., js-allonge -> "js", python-decorators -> "python"
    """
    # Known namespace prefixes
    prefixes = ["js", "javascript", "python", "ruby",
                "scheme", "aoe2", "typescript", "node"]
    slug_lower = slug.lower()
    for prefix in prefixes:
        if slug_lower.startswith(f"{prefix}-") or slug_lower.startswith(f"{prefix}_"):
            return prefix
    # Check if slug contains namespace hints
    if "javascript" in slug_lower or "js" in slug_lower:
        return "js"
    if "python" in slug_lower:
        return "python"
    return None


def page_slug_for_topic(topic: str, source_slug: str) -> str:
    """Return the canonical synthesized-page slug for a source topic."""
    return normalize_candidate_name(topic, _infer_namespace(source_slug))


def page_belongs_to_source(page_path: Path, source_slug: str) -> bool:
    """Return True when an existing wiki page already cites this source."""
    if not page_path.exists():
        return False
    try:
        sources = parse_frontmatter(page_path).data.get("sources")
    except Exception:
        return False
    if not isinstance(sources, list):
        return False
    expected = f"../sources/{source_slug}.md"
    return expected in {str(source) for source in sources}


def create_source_page_from_topics(
    slug: str,
    state: ExtractionState,
    source_path: Path,
    min_claims_per_topic: int = 3,
) -> Path:
    """Create a source page from extracted topics/claims.

    This is used by the unified ingest flow to create the source page
    after claim extraction, with the v3 structure including:
    - generation: frontmatter marking LLM vs deterministic sections
    - Major Concepts table with Status column
    - Extracted Topics table
    - High-Signal Claims with score
    - Candidate Concepts table
    - Source Locator Map
    """
    today = date.today().isoformat()

    # Read source for summary and locator map
    source_text = source_path.read_text()
    source_lines = source_text.splitlines()
    locator_map = extract_source_locator_map(source_lines)

    # Get first meaningful lines for summary
    summary_lines = []
    for line in source_lines[:100]:
        if line.strip() and not line.startswith('#') and not line.startswith('<!--'):
            summary_lines.append(line.strip())
            if len(summary_lines) >= 3:
                break
    summary = ' '.join(summary_lines)[
        :300] if summary_lines else 'No summary available.'

    # Filter viable topics
    viable_topics = {
        topic: claims
        for topic, claims in state.topics.items()
        if len(claims) >= min_claims_per_topic
    }

    # All topics (including non-viable) for Extracted Topics section
    all_topics = state.topics

    # Determine source type
    imported_dir = Path(f"raw/imported/{slug}")
    if (imported_dir / "original.pdf").exists():
        source_type = "pdf"
    elif (imported_dir / "original.md").exists():
        source_type = "markdown"
    else:
        source_type = "unknown"

    # Build Major Concepts table (viable topics only, with status)
    major_concepts_rows = []
    for topic in sorted(viable_topics.keys()):
        claims = viable_topics[topic]
        page_slug = page_slug_for_topic(topic, slug)
        page_path = f"../concepts/{page_slug}.md"
        full_page_path = Path(f"wiki/concepts/{page_slug}.md")

        # Determine status
        if page_belongs_to_source(full_page_path, slug):
            status = "draft"  # Will be updated after validation
        else:
            status = "not_started"

        # Calculate section coverage
        sections_covered = count_sections_for_topic(claims, locator_map)
        total_sections = len(locator_map) if locator_map else 1
        section_coverage = f"{sections_covered}/{total_sections} headings"

        if status == "not_started":
            major_concepts_rows.append(
                f"| {topic} | `{page_path}` | {status} | - | {len(claims)} | - |"
            )
        else:
            major_concepts_rows.append(
                f"| {topic} | [{page_path}]({page_path}) | {status} | - | {len(claims)} | {section_coverage} |"
            )

    major_concepts_table = "| Concept | Page | Status | Claims Used | Claims Available | Section Coverage |\n|---|---|---|---|---|---|\n"
    major_concepts_table += "\n".join(major_concepts_rows)

    # Build Extracted Topics table (all topics)
    extracted_topics_rows = []
    for topic, claims in sorted(all_topics.items(), key=lambda x: -len(x[1])):
        sections = count_sections_for_topic(claims, locator_map)
        if len(claims) >= min_claims_per_topic:
            page_slug = page_slug_for_topic(topic, slug)
            page_path = Path(f"wiki/concepts/{page_slug}.md")
            status = "created" if page_belongs_to_source(page_path, slug) else "not_started"
        else:
            status = "deferred"

        notes = ""
        if len(claims) < min_claims_per_topic:
            notes = f"Too few claims ({len(claims)} < {min_claims_per_topic})"
        elif sections == 1:
            notes = "Single section"

        extracted_topics_rows.append(
            f"| {topic} | {len(claims)} | {sections} | {status} | {notes} |"
        )

    extracted_topics_table = "| Topic | Claims | Sections | Status | Notes |\n|---|---|---|---|---|\n"
    extracted_topics_table += "\n".join(extracted_topics_rows)

    # Build High-Signal Claims table (top 10 by specificity score)
    all_claims_scored = [(score_claim_specificity(c), c) for c in state.claims]
    all_claims_scored.sort(reverse=True, key=lambda x: x[0])
    high_signal_claims = all_claims_scored[:10]

    high_signal_rows = []
    for score, c in high_signal_claims:
        claim_text = c.claim.replace('|', '\\|').replace('\n', ' ')[:80]
        evidence_text = c.evidence.replace('|', '\\|').replace('\n', ' ')[:100]
        # Use 3-column format required by source page validator
        high_signal_rows.append(
            f"| {claim_text} | \"{evidence_text}\" | `{c.locator}` |"
        )

    high_signal_table = "| Claim | Evidence | Locator |\n|---|---|---|\n"
    high_signal_table += "\n".join(high_signal_rows)

    # Build Concept Pages Generated list
    concept_pages = []
    for topic in sorted(viable_topics.keys()):
        page_slug = page_slug_for_topic(topic, slug)
        page_path = Path(f"wiki/concepts/{page_slug}.md")
        if page_belongs_to_source(page_path, slug):
            concept_pages.append(f"- [{topic}](../concepts/{page_slug}.md)")

    concept_pages_list = "\n".join(
        concept_pages) if concept_pages else "None yet."

    # Build Candidate Concepts table (viable topics not yet created)
    # Also register candidates with the tracker
    candidates_data = load_candidates()

    candidate_rows = []
    for topic in sorted(viable_topics.keys()):
        claims = viable_topics[topic]
        page_slug = page_slug_for_topic(topic, slug)
        page_path = Path(f"wiki/concepts/{page_slug}.md")

        if not page_belongs_to_source(page_path, slug):
            # Determine priority
            count = len(claims)
            if count >= 8:
                priority = "must create"
            elif count >= 5:
                priority = "should create"
            else:
                priority = "could create"

            sections = count_sections_for_topic(claims, locator_map)

            # Register with candidate tracker (v3: Task 4)
            claim_ids = [f"E{i+1:02d}" for i in range(count)]
            register_candidate(
                name=topic,
                source=slug,
                claims=claim_ids,
                priority=priority,
                candidates_data=candidates_data,
                namespace=_infer_namespace(slug),
                sections=sections,
            )

            candidate_rows.append(
                f"| {topic} | {page_slug} | {priority} | {count} | {sections} | 1 | discovered |"
            )

    # Save candidate tracking data
    if candidate_rows:
        save_candidates(candidates_data)

    candidate_table = "| Candidate | Canonical Slug | Priority | Claims | Sections | Sources | Status |\n|---|---|---|---|---|---|---|\n"
    candidate_table += "\n".join(candidate_rows) if candidate_rows else "None."

    # Build Source Locator Map table
    locator_map_rows = []
    for start, end, heading in locator_map[:20]:  # Limit to first 20
        # Find which topics have claims in this range
        topics_in_range = set()
        for topic, claims in all_topics.items():
            for claim in claims:
                match = re.match(r'normalized:L(\d+)', claim.locator)
                if match:
                    line_num = int(match.group(1))
                    if start <= line_num <= end:
                        topics_in_range.add(topic)
                        break

        topics_str = ", ".join(sorted(topics_in_range)[
                               :2]) if topics_in_range else "-"
        locator_map_rows.append(
            f"| {start}-{end} | {topics_str} | {heading} |")

    locator_map_table = "| Lines | Topic | Source Heading |\n|---|---|---|\n"
    locator_map_table += "\n".join(locator_map_rows)

    # Build Related pages candidate table (for backwards compatibility)
    related_rows = []
    for topic in sorted(viable_topics.keys()):
        claims = viable_topics[topic]
        page_slug = page_slug_for_topic(topic, slug)
        page_path = f"../concepts/{page_slug}.md"
        full_page_path = Path(f"wiki/concepts/{page_slug}.md")

        # Determine priority based on claim count
        count = len(claims)
        if count >= 8:
            priority = "must create"
        elif count >= 5:
            priority = "should create"
        else:
            priority = "could create"

        # Generate rich evidence basis (3+ words required by validator)
        sample_claims = claims[:3]
        keywords = set()
        for c in sample_claims:
            words = re.findall(r'\b[a-z]{4,}\b', c.claim.lower())
            keywords.update(words[:2])
        keyword_summary = ', '.join(
            sorted(keywords)[:3]) if keywords else 'various concepts'
        evidence_basis = f"{count} claims covering {keyword_summary}"

        if page_belongs_to_source(full_page_path, slug):
            related_rows.append(
                f"| {topic} | [{page_path}]({page_path}) | Deep extraction | {priority} | {evidence_basis} | created |"
            )
        else:
            related_rows.append(
                f"| {topic} | `{page_path}` | Deep extraction | {priority} | {evidence_basis} | not created yet |"
            )

    related_table = "| Candidate page | Intended path | Group | Priority | Evidence basis | Status |\n|---|---|---|---|---|---|\n"
    related_table += "\n".join(related_rows)

    # Build sources list for frontmatter
    sources_list = []
    if source_type == "pdf":
        sources_list.append(f"../../raw/imported/{slug}/original.pdf")
    elif source_type == "markdown":
        sources_list.append(f"../../raw/imported/{slug}/original.md")

    sources_yaml = "\n".join(
        f"  - {s}" for s in sources_list) if sources_list else "  - ../../raw/imported/{slug}/"

    content = f"""---
title: "Source: {slug}"
type: source
source_id: {slug}
source_type: {source_type}
raw_path: ../../raw/imported/{slug}/
normalized_path: ../../raw/normalized/{slug}/
status: draft
last_updated: {today}
tags: []
sources:
{sources_yaml}
---

# Source: {slug}

## Summary

{summary}

Extracted {len(state.claims)} claims from {len(state.processed_chunks)} chunks, organized into {len(viable_topics)} viable topics.

### Extraction Metadata

- Claim count: {len(state.claims)}
- Topic count: {len(viable_topics)}
- Generation: summary (llm), tables (deterministic)

## Key claims

{high_signal_table}

## Major concepts

### Extracted Topics

{extracted_topics_table}

{major_concepts_table}

### Candidate Concepts

{candidate_table}

### Source Locator Map

{locator_map_table}

## Entities

None identified.

## Procedures

None identified.

## References

None identified.

## Open questions

- Additional topics may emerge from deeper analysis

## Related pages

{related_table}
"""

    source_page = Path(f"wiki/sources/{slug}.md")
    source_page.parent.mkdir(parents=True, exist_ok=True)
    source_page.write_text(content)

    return source_page


# ============================================================================
# Main Workflow
# ============================================================================

def run_deep_extraction(
    slug: str,
    resume: bool = False,
    max_chunks: int = 0,
    chunk_size: int = 400,
    overlap: int = 30,
    backend_name: str = "",
    timeout: int = 120,
    skip_synthesis: bool = False,
    skip_finalize: bool = False,
    use_structured_chunking: bool = False,
    target_tokens: int = 6500,
    soft_max_tokens: int = 7500,
    hard_max_tokens: int = 9000,
) -> int:
    """Run the complete deep extraction workflow."""
    source_path = Path(f"raw/normalized/{slug}/source.md")
    state_path = Path(f".tmp/deep-extract/{slug}/state.json")

    if not source_path.exists():
        print(f"FAIL: {source_path} not found", file=sys.stderr)
        return 1

    # Track structured chunking metadata
    structured_metadata = None

    # Load or create state
    if resume and state_path.exists():
        print(f"Resuming from {state_path}")
        state = ExtractionState.load(state_path)
        print(
            f"  Previously processed: {len(state.processed_chunks)}/{len(state.chunks)} chunks")
        print(f"  Claims extracted: {len(state.claims)}")
        print(f"  Topics found: {len(state.topics)}")
    else:
        print(f"Starting fresh extraction for {slug}")

        if use_structured_chunking:
            if not HAS_STRUCTURED_CHUNKING:
                print(
                    "WARN: Structured chunking not available, falling back to line-based chunking")
                chunks = create_chunks(
                    source_path, chunk_size=chunk_size, overlap=overlap)
            else:
                print(
                    f"Using structured chunking (target: {target_tokens} tokens)")
                chunks, structured_metadata = create_structured_chunks(
                    source_path,
                    doc_id=slug,
                    target_tokens=target_tokens,
                    soft_max_tokens=soft_max_tokens,
                    hard_max_tokens=hard_max_tokens,
                )
                print(f"  Blocks: {structured_metadata['block_count']}")
                print(
                    f"  Total tokens: {structured_metadata['total_tokens']:,}")
                print(
                    f"  Avg tokens/chunk: {structured_metadata['avg_tokens_per_chunk']:.0f}")
                if structured_metadata['issues_by_type']:
                    print(
                        f"  Quality issues: {structured_metadata['issues_by_type']}")

                # Save structured chunks for reference
                struct_dir = Path(f".tmp/deep-extract/{slug}/structured")
                struct_dir.mkdir(parents=True, exist_ok=True)
                save_blocks(
                    structured_metadata['blocks'], struct_dir / "blocks.jsonl")
                save_structured_chunks(
                    structured_metadata['structured_chunks'], struct_dir / "chunks.jsonl")
        else:
            chunks = create_chunks(
                source_path, chunk_size=chunk_size, overlap=overlap)

        state = ExtractionState(
            slug=slug,
            source_path=str(source_path),
            total_lines=len(source_path.read_text().splitlines()),
            chunks=chunks,
            started_at=date.today().isoformat(),
        )
        state.save(state_path)

    print(f"\nSource: {source_path}")
    print(f"Total lines: {state.total_lines}")
    print(f"Total chunks: {len(state.chunks)}")

    # Limit chunks if requested
    chunks_to_process = [
        c for c in state.chunks if c.index not in state.processed_chunks]
    if max_chunks > 0:
        chunks_to_process = chunks_to_process[:max_chunks]

    print(f"Chunks to process: {len(chunks_to_process)}")

    # Initialize backend
    backend_name = backend_name or os.environ.get(
        "WIKI_MODEL_BACKEND", "codex")
    print(f"\nUsing backend: {backend_name}")

    try:
        backend = get_backend(backend_name)
    except Exception as e:
        print(f"FAIL: Could not initialize backend: {e}", file=sys.stderr)
        return 1

    if chunks_to_process:
        # Process chunks
        print("\n" + "=" * 60)
        print("PHASE 1: Extract Claims from Chunks")
        print("=" * 60)

        total_claims_before = len(state.claims)

        for i, chunk in enumerate(chunks_to_process, 1):
            print(
                f"\n[{i}/{len(chunks_to_process)}] Chunk {chunk.index + 1}: {chunk.title[:50]}")
            print(
                f"    Lines {chunk.start_line}-{chunk.end_line} ({chunk.line_count} lines)")

            start_time = time.time()

            # Use structured chunk text if available
            if structured_metadata:
                chunk_text = get_structured_chunk_text(
                    source_path, chunk, structured_metadata)
            else:
                chunk_text = get_chunk_text(source_path, chunk)

            claims = extract_claims_from_chunk(
                backend, state, chunk, source_path, timeout, chunk_text=chunk_text)
            elapsed = time.time() - start_time

            print(f"    Extracted {len(claims)} claims in {elapsed:.1f}s")

            # Add claims to state
            state.claims.extend(claims)
            state.processed_chunks.add(chunk.index)

            # Also write to claims-raw.jsonl for new state format (resumable)
            if claims:
                raw_claims = [
                    RawClaim(
                        topic=c.topic,
                        claim=c.claim,
                        evidence=c.evidence,
                        locator=c.locator,
                        chunk_index=chunk.index,
                    )
                    for c in claims
                ]
                append_raw_claims(state.slug, raw_claims)

            # Save progress after each chunk
            state._rebuild_topics()
            state.save(state_path)

            # Show running totals
            print(
                f"    Total claims: {len(state.claims)}, Topics: {len(state.topics)}")

        new_claims = len(state.claims) - total_claims_before
        print(
            f"\nExtracted {new_claims} new claims from {len(chunks_to_process)} chunks")
    else:
        print("\nAll chunks already processed!")

    # Aggregate claims
    print("\n" + "=" * 60)
    print("PHASE 2: Aggregate Claims by Topic")
    print("=" * 60)

    state.topics = aggregate_claims_by_topic(state.claims)
    state.save(state_path)

    print(f"\nTopics found: {len(state.topics)}")
    for topic, claims in sorted(state.topics.items(), key=lambda x: -len(x[1])):
        print(f"  {topic}: {len(claims)} claims")

    # Write claims-normalized.json (new state format)
    if state.claims:
        normalized_claims = []
        topic_claim_ids: dict[str, list[str]] = {}
        for claim in state.claims:
            claim_id = claim.claim_id or generate_claim_id(
                state.slug, claim.chunk_index, claim.claim)
            nc = NormalizedClaim(
                claim_id=claim_id,
                topic=claim.topic,
                claim=claim.claim,
                evidence=claim.evidence,
                locator=claim.locator,
                chunk_index=claim.chunk_index,
            )
            normalized_claims.append(nc)
            if claim.topic not in topic_claim_ids:
                topic_claim_ids[claim.topic] = []
            topic_claim_ids[claim.topic].append(claim_id)

        raw_claims_path = get_raw_claims_path(state.slug)
        raw_count = 0
        if raw_claims_path.exists():
            with open(raw_claims_path, "r") as f:
                raw_count = sum(1 for line in f if line.strip())

        normalized_data = NormalizedClaimsData(
            slug=state.slug,
            claims=normalized_claims,
            topics=topic_claim_ids,
            raw_claims_count=raw_count,
            deduped_count=len(normalized_claims),
        )
        save_normalized_claims(state.slug, normalized_data)
        print(
            f"\nWrote claims-normalized.json ({len(normalized_claims)} claims)")

    if skip_synthesis:
        print("\nSkipping synthesis (--skip-synthesis)")
    else:
        # Synthesize pages
        print("\n" + "=" * 60)
        print("PHASE 3: Synthesize Wiki Pages")
        print("=" * 60)

        # Generate candidates.generated.json before synthesis
        min_claims_per_page = 3
        viable_topics = {
            topic: claims
            for topic, claims in state.topics.items()
            if len(claims) >= min_claims_per_page
        }

        # Build candidates list
        generated_candidates = []
        for topic, claims in viable_topics.items():
            page_slug = topic.lower().replace(' ', '-').replace('/', '-')
            page_slug = re.sub(r'[^a-z0-9-]', '', page_slug)
            page_path = f"../concepts/{page_slug}.md"

            # Get claim IDs for this topic
            claim_ids = [c.claim_id or generate_claim_id(
                state.slug, c.chunk_index, c.claim) for c in claims]

            # Determine priority based on claim count
            if len(claims) >= 8:
                priority = "must create"
            elif len(claims) >= 5:
                priority = "should create"
            else:
                priority = "could create"

            generated_candidates.append(Candidate(
                title=topic,
                path=page_path,
                page_type="concept",
                priority=priority,
                claim_ids=claim_ids,
                evidence_basis=f"{len(claims)} claims from extraction",
            ))

        # Write candidates.generated.json
        if generated_candidates:
            candidates_data = GeneratedCandidatesData(
                slug=state.slug,
                candidates=generated_candidates,
            )
            save_generated_candidates(state.slug, candidates_data)
            print(
                f"\nWrote candidates.generated.json ({len(generated_candidates)} candidates)")

        created_pages = synthesize_pages(backend, state, timeout=timeout)
        state.pages_created = [str(p) for p in created_pages]
        state.save(state_path)

    if skip_finalize:
        print("\nSkipping finalization (--skip-finalize)")
    else:
        finalize_extraction(state)

    # Summary
    print("\n" + "=" * 60)
    print("EXTRACTION COMPLETE")
    print("=" * 60)
    print(f"Source: {source_path}")
    print(
        f"Chunks processed: {len(state.processed_chunks)}/{len(state.chunks)}")
    print(f"Claims extracted: {len(state.claims)}")
    print(f"Topics found: {len(state.topics)}")
    print(f"Pages created: {len(state.pages_created)}")
    print(f"State saved to: {state_path}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deep extraction workflow for comprehensive wiki ingestion")
    parser.add_argument(
        "slug", help="Source slug (must have raw/normalized/<slug>/source.md)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show chunks without processing")
    parser.add_argument("--resume", action="store_true",
                        help="Resume interrupted extraction")
    parser.add_argument("--max-chunks", type=int, default=0,
                        help="Limit chunks to process (0 = all)")
    parser.add_argument("--chunk-size", type=int, default=400,
                        help="Lines per chunk for line-based chunking (default: 400)")
    parser.add_argument("--overlap", type=int, default=30,
                        help="Overlap between chunks for line-based chunking (default: 30)")
    parser.add_argument("--backend", type=str, default="",
                        help="Model backend (default: WIKI_MODEL_BACKEND or codex)")
    parser.add_argument("--timeout", type=int, default=120,
                        help="Timeout per chunk in seconds")
    parser.add_argument("--skip-synthesis", action="store_true",
                        help="Skip page synthesis (extraction only)")
    parser.add_argument("--skip-finalize", action="store_true",
                        help="Skip finalization (index/graph/log)")
    parser.add_argument("--extract-only", action="store_true",
                        help="Extract claims only, no synthesis or finalization (alias for --skip-synthesis --skip-finalize)")

    # Structured chunking options
    parser.add_argument("--structured", action="store_true",
                        help="Use token-aware structural chunking instead of line-based")
    parser.add_argument("--target-tokens", type=int, default=3500,
                        help="Target source tokens per chunk (default: 3500)")
    parser.add_argument("--soft-max-tokens", type=int, default=7500,
                        help="Soft max source tokens per chunk (default: 7500)")
    parser.add_argument("--hard-max-tokens", type=int, default=9000,
                        help="Hard max source tokens per chunk (default: 9000)")

    args = parser.parse_args()

    # --extract-only is shorthand for --skip-synthesis --skip-finalize
    if args.extract_only:
        args.skip_synthesis = True
        args.skip_finalize = True

    if args.dry_run:
        # Just show chunks
        source_path = Path(f"raw/normalized/{args.slug}/source.md")
        if not source_path.exists():
            print(f"FAIL: {source_path} not found", file=sys.stderr)
            return 1

        if args.structured:
            if not HAS_STRUCTURED_CHUNKING:
                print("FAIL: Structured chunking not available", file=sys.stderr)
                return 1

            chunks, metadata = create_structured_chunks(
                source_path,
                doc_id=args.slug,
                target_tokens=args.target_tokens,
                soft_max_tokens=args.soft_max_tokens,
                hard_max_tokens=args.hard_max_tokens,
            )
            total_lines = len(source_path.read_text().splitlines())

            print(f"Source: {source_path}")
            print(f"Total lines: {total_lines}")
            print(f"Chunking: STRUCTURED (token-aware)")
            print(f"  Target tokens: {args.target_tokens}")
            print(f"  Blocks: {metadata['block_count']}")
            print(f"  Chunks: {len(chunks)}")
            print(f"  Total tokens: {metadata['total_tokens']:,}")
            print(
                f"  Avg tokens/chunk: {metadata['avg_tokens_per_chunk']:.0f}")
            if metadata['issues_by_type']:
                print(f"  Quality issues: {metadata['issues_by_type']}")
            if metadata['pages_needing_review']:
                print(
                    f"  Pages needing review: {metadata['pages_needing_review']}")
        else:
            chunks = create_chunks(
                source_path, chunk_size=args.chunk_size, overlap=args.overlap)
            total_lines = len(source_path.read_text().splitlines())

            est_time = len(chunks) * 30  # ~30 sec per chunk
            est_min = est_time // 60
            est_sec = est_time % 60

            print(f"Source: {source_path}")
            print(f"Total lines: {total_lines}")
            print(f"Chunking: LINE-BASED")
            print(f"  Chunk size: {args.chunk_size} lines")
            print(f"  Overlap: {args.overlap} lines")
            print(f"  Chunks: {len(chunks)}")
            print(f"Estimated time: {est_min}m {est_sec}s")
        print()
        print("Chunks:")
        for c in chunks[:30]:
            print(
                f"  {c.index + 1:3}. [{c.start_line:5}-{c.end_line:5}] ({c.line_count:3} lines) {c.title[:50]}")
        if len(chunks) > 30:
            print(f"  ... and {len(chunks) - 30} more chunks")

        # Save index
        index_path = Path(f".tmp/deep-extract/{args.slug}/chunks.json")
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(json.dumps({
            "slug": args.slug,
            "total_lines": total_lines,
            "chunk_count": len(chunks),
            "chunks": [c.to_dict() for c in chunks],
        }, indent=2))
        print(f"\nChunk index saved to: {index_path}")

        return 0

    return run_deep_extraction(
        slug=args.slug,
        resume=args.resume,
        max_chunks=args.max_chunks,
        chunk_size=args.chunk_size,
        overlap=args.overlap,
        backend_name=args.backend,
        timeout=args.timeout,
        skip_synthesis=args.skip_synthesis,
        skip_finalize=args.skip_finalize,
        use_structured_chunking=args.structured,
        target_tokens=args.target_tokens,
        soft_max_tokens=args.soft_max_tokens,
        hard_max_tokens=args.hard_max_tokens,
    )


if __name__ == "__main__":
    sys.exit(main())
