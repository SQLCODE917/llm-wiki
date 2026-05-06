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
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

from wiki_common import log_context_stats, section
from wiki_model_backend import get_backend, ModelConfig, ModelResponse


# ============================================================================
# Data Structures
# ============================================================================

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

    def to_dict(self) -> dict:
        return {
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
        )


@dataclass
class ExtractionState:
    """State of an extraction run, persisted for resumability."""
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

TASK: Extract 0-10 concrete, reusable claims from this chunk.

TOPIC GUIDELINES - Use BROAD topic categories like:
- "Functions" (not "Arrow Functions", "Function Values", etc.)
- "Arrays" (not "Array Methods", "Array Destructuring", etc.)  
- "Closures" (not "Closure Patterns", "Closure Examples", etc.)
- "Iterators" (not "Iterator Protocol", "Custom Iterators", etc.)
- "Objects" (not "Plain Objects", "Object Methods", etc.)
- "Recursion" (not "Tail Recursion", "Recursive Patterns", etc.)
- "Data Types" (not "Value Types", "Reference Types", etc.)
- "Control Flow" (not "Conditionals", "Loops", etc.)
- "ES6 Features" (for modern JavaScript syntax)
- "Functional Programming" (for FP concepts)

RULES:
1. Extract ONLY claims that teach something useful and reusable
2. Each claim must have an exact quote as evidence from the numbered lines
3. The locator must match an actual line number (e.g., "normalized:L{chunk.start_line}")
4. Use BROAD topic names from the guidelines above
5. Skip: TOC entries, copyright notices, page numbers, marketing text, author bios
6. If this chunk has no teachable content, return an empty array []

OUTPUT FORMAT - Return ONLY a JSON array:
```json
[
  {{
    "topic": "Broad topic name (e.g., 'Functions', 'Arrays', 'Closures')",
    "claim": "Concrete statement in your own words - what the reader should learn",
    "evidence": "Exact short quote from source (under 200 chars)",
    "locator": "normalized:L<line_number>"
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
) -> list[Claim]:
    """Extract claims from a single chunk using the model backend."""
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
    claims = parse_claims_response(response.output, chunk.index)
    return claims


def parse_claims_response(output: str, chunk_index: int) -> list[Claim]:
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
                claims.append(Claim(
                    topic=str(item['topic']).strip(),
                    claim=str(item['claim']).strip(),
                    evidence=str(item['evidence']).strip(),
                    locator=str(item['locator']).strip(),
                    chunk_index=chunk_index,
                ))
        return claims
    except json.JSONDecodeError as e:
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
    """Normalize topic names for consistent grouping."""
    # Remove common prefixes/suffixes
    topic = topic.strip()
    topic = re.sub(r'^(JavaScript\s+)?', '', topic, flags=re.IGNORECASE)
    topic = re.sub(r'\s+in\s+JavaScript$', '', topic, flags=re.IGNORECASE)

    # Title case
    topic = topic.title()
    lower = topic.lower()

    # Map detailed topics to broad categories
    # Each tuple: (keywords to match, normalized topic name)
    topic_mappings = [
        # Functions
        (['function', 'arrow', 'closure', 'call', 'apply',
         'bind', 'higher-order', 'higher order'], 'Functions'),
        # Arrays
        (['array', 'destructur', 'spread', 'rest parameter'], 'Arrays'),
        # Iterators/Generators
        (['iterator', 'generator', 'iterable', 'yield'], 'Iterators And Generators'),
        # Objects
        (['object', 'property', 'prototype', 'method'], 'Objects'),
        # Classes
        (['class', 'inherit', 'extends', 'constructor'], 'Classes'),
        # Recursion
        (['recursion', 'recursive', 'tail call', 'trampoline'], 'Recursion'),
        # Data types
        (['type', 'value', 'reference', 'number', 'string',
         'undefined', 'null', 'boolean'], 'Data Types'),
        # Control flow
        (['control', 'loop', 'condition', 'if', 'while', 'for'], 'Control Flow'),
        # ES6 features
        (['es6', 'es2015', 'ecmascript', 'let',
         'const', 'block scope'], 'ES6 Features'),
        # Functional programming
        (['functional', 'pure', 'immutable', 'compose',
         'curry', 'partial'], 'Functional Programming'),
        # Collections
        (['collection', 'map', 'set', 'weakmap', 'weakset'], 'Collections'),
        # Patterns
        (['pattern', 'decorator', 'mixin', 'module'], 'Patterns'),
    ]

    for keywords, normalized in topic_mappings:
        if any(kw in lower for kw in keywords):
            return normalized

    return topic


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
            backend, state.slug, topic, claims, timeout)
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
    timeout: int = 180,
) -> Path | None:
    """Synthesize a single wiki page from claims."""
    # Determine page type and path
    page_slug = topic.lower().replace(' ', '-').replace('/', '-')
    page_slug = re.sub(r'[^a-z0-9-]', '', page_slug)
    page_path = Path(f"wiki/concepts/{page_slug}.md")

    # Skip if exists
    if page_path.exists():
        print(f"    Skipping (exists): {page_path}")
        return page_path

    # Build claims table for prompt
    claims_table = []
    for c in claims:
        claims_table.append(f"- Topic: {c.topic}")
        claims_table.append(f"  Claim: {c.claim}")
        claims_table.append(f"  Evidence: \"{c.evidence}\"")
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

EXTRACTED CLAIMS:
{claims_text}

CREATE: wiki/concepts/{page_slug}.md

REQUIREMENTS:
1. Use this exact structure:

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

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| <Rewrite claim clearly> | "<exact evidence quote>" | `<locator>` | [Source](../sources/{slug}.md) |

## Why it matters

<Explain significance based on the claims>

## Source pages

- [Source](../sources/{slug}.md)
```

2. Include ALL provided claims in the evidence table
3. Rewrite claims to be clear and self-contained
4. Keep evidence quotes short and exact
5. Use ASCII characters only (no smart quotes)
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
    """Get the state file path for a slug."""
    return Path(f".tmp/deep-extract/{slug}/state.json")


def load_extraction_state(slug: str) -> ExtractionState | None:
    """Load extraction state for a slug if it exists."""
    state_path = get_state_path(slug)
    if state_path.exists():
        return ExtractionState.load(state_path)
    return None


def create_source_page_from_topics(
    slug: str,
    state: ExtractionState,
    source_path: Path,
    min_claims_per_topic: int = 3,
) -> Path:
    """Create a source page from extracted topics/claims.

    This is used by the unified ingest flow to create the source page
    after claim extraction, listing topics as Related pages candidates.
    """
    today = date.today().isoformat()

    # Read source for summary
    source_text = source_path.read_text()
    source_lines = source_text.splitlines()

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

    # Build key claims table from top claims across all topics
    key_claims = []
    for topic, claims in sorted(viable_topics.items(), key=lambda x: -len(x[1])):
        for claim in claims[:3]:  # Top 3 from each topic
            key_claims.append(claim)
    key_claims = key_claims[:15]  # Limit total

    claims_table = "| Claim | Evidence | Locator |\n|---|---|---|\n"
    for c in key_claims:
        # Clean claim and evidence for table - escape pipes in both
        claim = c.claim.replace('|', '\\|').replace('\n', ' ')[:100]
        evidence = c.evidence.replace('|', '\\|').replace('\n', ' ')[:150]
        claims_table += f"| {claim} | \"{evidence}\" | `{c.locator}` |\n"

    # Build Related pages candidate table
    related_rows = []
    for topic in sorted(viable_topics.keys()):
        claims = viable_topics[topic]
        page_slug = topic.lower().replace(' ', '-').replace('/', '-')
        page_slug = re.sub(r'[^a-z0-9-]', '', page_slug)
        page_path = f"../concepts/{page_slug}.md"

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
            # Extract key terms from claim text
            words = re.findall(r'\b[a-z]{4,}\b', c.claim.lower())
            keywords.update(words[:2])
        keyword_summary = ', '.join(sorted(keywords)[:3]) if keywords else 'various concepts'
        evidence_basis = f"{count} claims covering {keyword_summary}"

        related_rows.append(
            f"| {topic} | `{page_path}` | Deep extraction | {priority} | {evidence_basis} | not created yet |"
        )

    related_table = "| Candidate page | Intended path | Group | Priority | Evidence basis | Status |\n|---|---|---|---|---|---|\n"
    related_table += "\n".join(related_rows)

    # Build topics list
    topics_list = []
    for topic, claims in sorted(viable_topics.items(), key=lambda x: -len(x[1])):
        topics_list.append(f"- **{topic}** ({len(claims)} claims)")

    # Determine source type and filename
    imported_dir = Path(f"raw/imported/{slug}")
    if (imported_dir / "original.pdf").exists():
        source_type = "pdf"
        source_file = f"../../raw/imported/{slug}/original.pdf"
    elif (imported_dir / "original.md").exists():
        source_type = "markdown"
        source_file = f"../../raw/imported/{slug}/original.md"
    else:
        source_type = "unknown"
        source_file = ""

    # Build sources list
    sources_yaml = f"  - {source_file}" if source_file else ""

    content = f"""---
title: {slug}
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

# {slug}

## Summary

{summary}

Extracted {len(state.claims)} claims from {len(state.processed_chunks)} chunks, organized into {len(viable_topics)} viable topics.

## Key claims

{claims_table}

## Major concepts

### Natural groupings

{chr(10).join(topics_list)}

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
) -> int:
    """Run the complete deep extraction workflow."""
    source_path = Path(f"raw/normalized/{slug}/source.md")
    state_path = Path(f".tmp/deep-extract/{slug}/state.json")

    if not source_path.exists():
        print(f"FAIL: {source_path} not found", file=sys.stderr)
        return 1

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
        "WIKI_MODEL_BACKEND", "bedrock")
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
            claims = extract_claims_from_chunk(
                backend, state, chunk, source_path, timeout)
            elapsed = time.time() - start_time

            print(f"    Extracted {len(claims)} claims in {elapsed:.1f}s")

            # Add claims to state
            state.claims.extend(claims)
            state.processed_chunks.add(chunk.index)

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

    if skip_synthesis:
        print("\nSkipping synthesis (--skip-synthesis)")
    else:
        # Synthesize pages
        print("\n" + "=" * 60)
        print("PHASE 3: Synthesize Wiki Pages")
        print("=" * 60)

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
                        help="Lines per chunk (default: 400)")
    parser.add_argument("--overlap", type=int, default=30,
                        help="Overlap between chunks (default: 30)")
    parser.add_argument("--backend", type=str, default="",
                        help="Model backend (default: WIKI_MODEL_BACKEND or bedrock)")
    parser.add_argument("--timeout", type=int, default=120,
                        help="Timeout per chunk in seconds")
    parser.add_argument("--skip-synthesis", action="store_true",
                        help="Skip page synthesis (extraction only)")
    parser.add_argument("--skip-finalize", action="store_true",
                        help="Skip finalization (index/graph/log)")
    parser.add_argument("--extract-only", action="store_true",
                        help="Extract claims only, no synthesis or finalization (alias for --skip-synthesis --skip-finalize)")
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

        chunks = create_chunks(
            source_path, chunk_size=args.chunk_size, overlap=args.overlap)
        total_lines = len(source_path.read_text().splitlines())

        est_time = len(chunks) * 30  # ~30 sec per chunk
        est_min = est_time // 60
        est_sec = est_time % 60

        print(f"Source: {source_path}")
        print(f"Total lines: {total_lines}")
        print(f"Chunks: {len(chunks)}")
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
    )


if __name__ == "__main__":
    sys.exit(main())
