#!/usr/bin/env python3
"""Structured chunking for wiki ingestion.

This module implements token-aware structural packing as described in the
chunking improvement proposal. It chunks AFTER extraction into a structured
intermediate representation, preserving document structure, tables, code blocks,
and equations.

Pipeline:
    PDF/Markdown -> structured extraction -> block IR -> atomic units ->
    token-aware structural packing -> LLM wiki passes

Token budgets for qwen3-coder-30b:
    Hard context ceiling:        16,000 tokens
    Preferred total input:       8,000-12,000 tokens
    Reserve for output:          3,000 tokens
    Reserve for system prompt:   1,000-1,500 tokens
    Reserve for tool/task text:  1,000 tokens
    Safe source chunk target:    5,500-7,500 tokens

Usage:
    from wiki_structured_chunking import (
        BlockExtractor, StructuralChunker, ChunkConfig
    )
    
    # Extract blocks from markdown
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(source_path, doc_id="my-doc")
    
    # Pack into token-aware chunks
    config = ChunkConfig()
    chunker = StructuralChunker(config)
    chunks = chunker.pack(blocks)
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Iterator, Callable

# Token counting - try Qwen tokenizer, fall back to approximation
_tokenizer = None
_tokenizer_load_attempted = False


def _load_tokenizer():
    """Lazy-load the tokenizer."""
    global _tokenizer, _tokenizer_load_attempted
    if _tokenizer_load_attempted:
        return _tokenizer
    _tokenizer_load_attempted = True

    try:
        from transformers import AutoTokenizer
        # Try Qwen3 coder tokenizer
        for model_name in [
            "Qwen/Qwen2.5-Coder-32B-Instruct",  # Similar to Qwen3
            "Qwen/Qwen2.5-32B-Instruct",
            "Qwen/Qwen2-7B-Instruct",
        ]:
            try:
                _tokenizer = AutoTokenizer.from_pretrained(
                    model_name, trust_remote_code=True
                )
                print(f"Loaded tokenizer: {model_name}")
                return _tokenizer
            except Exception:
                continue
    except ImportError:
        pass

    print("WARN: No Qwen tokenizer available, using character approximation")
    return None


def count_tokens(text: str, safety_margin: float = 0.15) -> int:
    """Count tokens in text, with safety margin for approximation.

    Uses actual Qwen tokenizer if available, otherwise approximates
    at ~3.5 chars/token (conservative for technical text).
    """
    tokenizer = _load_tokenizer()
    if tokenizer:
        return len(tokenizer.encode(text, add_special_tokens=False))

    # Approximation with safety margin for technical text
    # Technical content has more tokens per character due to code, symbols
    base_estimate = len(text) / 3.5
    return int(base_estimate * (1 + safety_margin))


# ============================================================================
# Block Types and Data Structures
# ============================================================================

class BlockType(Enum):
    """Block types for document structure."""
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    CODE = "code"
    TABLE = "table"
    EQUATION = "equation"
    FIGURE = "figure"
    CAPTION = "caption"
    LIST = "list"
    FOOTNOTE = "footnote"
    PAGE_HEADER = "page_header"
    PAGE_FOOTER = "page_footer"
    TOC_ENTRY = "toc_entry"
    BIBLIOGRAPHY = "bibliography"
    BLOCKQUOTE = "blockquote"
    HTML = "html"
    UNKNOWN = "unknown"


@dataclass
class Block:
    """A structural block from a document.

    Each block represents an atomic unit of document content that should
    not be split unless absolutely necessary.
    """
    doc_id: str
    source_file: str
    page_start: int
    page_end: int
    section_path: list[str]
    block_id: str
    block_type: BlockType
    text: str
    raw_text: str = ""  # Original text before normalization
    normalized_text: str = ""  # Search-friendly normalization
    line_start: int = 0
    line_end: int = 0
    reading_order: int = 0
    char_count: int = 0
    token_count: int = 0
    heading_level: int = 0  # For headings: 1-6
    language: str = ""  # For code blocks
    assets: list[str] = field(default_factory=list)
    checksum: str = ""

    # Quality metadata
    quality_score: float = 1.0  # 0-1, lower means more issues
    quality_issues: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.raw_text:
            self.raw_text = self.text
        if not self.normalized_text:
            self.normalized_text = self._normalize_text(self.text)
        if not self.char_count:
            self.char_count = len(self.text)
        if not self.token_count:
            self.token_count = count_tokens(self.text)
        if not self.checksum:
            self.checksum = f"sha256:{hashlib.sha256(self.text.encode()).hexdigest()[:16]}"

    @staticmethod
    def _normalize_text(text: str) -> str:
        """Create search-friendly normalization."""
        # Common symbol replacements
        replacements = {
            "²": "^2", "³": "^3", "⁴": "^4",
            "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta",
            "Δ": "delta", "π": "pi", "Σ": "sum", "∑": "sum",
            "→": "->", "←": "<-", "↔": "<->",
            "≤": "<=", "≥": ">=", "≠": "!=",
            "∞": "infinity", "∈": "in", "∉": "not in",
            "×": "*", "÷": "/", "±": "+/-",
            "…": "...", "–": "-", "—": "-",
            "'": "'", "'": "'", """: '"', """: '"',
        }
        result = text
        for old, new in replacements.items():
            result = result.replace(old, new)
        return result

    def to_dict(self) -> dict:
        return {
            "doc_id": self.doc_id,
            "source_file": self.source_file,
            "page_start": self.page_start,
            "page_end": self.page_end,
            "section_path": self.section_path,
            "block_id": self.block_id,
            "type": self.block_type.value,
            "text": self.text,
            "raw_text": self.raw_text,
            "normalized_text": self.normalized_text,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "reading_order": self.reading_order,
            "char_count": self.char_count,
            "token_count": self.token_count,
            "heading_level": self.heading_level,
            "language": self.language,
            "assets": self.assets,
            "checksum": self.checksum,
            "quality_score": self.quality_score,
            "quality_issues": self.quality_issues,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Block":
        return cls(
            doc_id=d["doc_id"],
            source_file=d["source_file"],
            page_start=d["page_start"],
            page_end=d["page_end"],
            section_path=d["section_path"],
            block_id=d["block_id"],
            block_type=BlockType(d["type"]),
            text=d["text"],
            raw_text=d.get("raw_text", ""),
            normalized_text=d.get("normalized_text", ""),
            line_start=d.get("line_start", 0),
            line_end=d.get("line_end", 0),
            reading_order=d.get("reading_order", 0),
            char_count=d.get("char_count", 0),
            token_count=d.get("token_count", 0),
            heading_level=d.get("heading_level", 0),
            language=d.get("language", ""),
            assets=d.get("assets", []),
            checksum=d.get("checksum", ""),
            quality_score=d.get("quality_score", 1.0),
            quality_issues=d.get("quality_issues", []),
        )


@dataclass
class AtomicUnit:
    """An atomic unit that should not be split.

    Atomic units are groups of blocks that belong together semantically:
    - heading + following paragraph
    - complete list
    - complete code block
    - complete table
    - equation + context
    - figure + caption
    """
    blocks: list[Block]
    unit_type: str  # heading_group, paragraph, list, code, table, etc.
    section_path: list[str]
    token_count: int = 0
    splittable: bool = False  # Can this unit be split if too large?

    def __post_init__(self):
        if not self.token_count:
            self.token_count = sum(b.token_count for b in self.blocks)

    @property
    def text(self) -> str:
        return "\n\n".join(b.text for b in self.blocks)

    @property
    def line_start(self) -> int:
        return min(b.line_start for b in self.blocks) if self.blocks else 0

    @property
    def line_end(self) -> int:
        return max(b.line_end for b in self.blocks) if self.blocks else 0

    @property
    def pages(self) -> list[int]:
        pages = set()
        for b in self.blocks:
            for p in range(b.page_start, b.page_end + 1):
                pages.add(p)
        return sorted(pages)


@dataclass
class StructuredChunk:
    """A token-bounded chunk ready for LLM processing."""
    chunk_id: str
    doc_id: str
    pages: list[int]
    section_path: list[str]
    token_count: int
    block_ids: list[str]
    previous_chunk: str | None
    next_chunk: str | None
    contains: list[str]  # Block types in this chunk
    text: str
    context_header: str = ""  # Semantic overlap context
    line_start: int = 0
    line_end: int = 0

    # For continuation tracking
    continued_from: str | None = None
    continuation_type: str | None = None

    def to_dict(self) -> dict:
        return {
            "chunk_id": self.chunk_id,
            "doc_id": self.doc_id,
            "pages": self.pages,
            "section_path": self.section_path,
            "token_count": self.token_count,
            "block_ids": self.block_ids,
            "previous_chunk": self.previous_chunk,
            "next_chunk": self.next_chunk,
            "contains": self.contains,
            "text": self.text,
            "context_header": self.context_header,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "continued_from": self.continued_from,
            "continuation_type": self.continuation_type,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "StructuredChunk":
        return cls(
            chunk_id=d["chunk_id"],
            doc_id=d["doc_id"],
            pages=d["pages"],
            section_path=d["section_path"],
            token_count=d["token_count"],
            block_ids=d["block_ids"],
            previous_chunk=d.get("previous_chunk"),
            next_chunk=d.get("next_chunk"),
            contains=d["contains"],
            text=d["text"],
            context_header=d.get("context_header", ""),
            line_start=d.get("line_start", 0),
            line_end=d.get("line_end", 0),
            continued_from=d.get("continued_from"),
            continuation_type=d.get("continuation_type"),
        )

    def render_with_context(self) -> str:
        """Render chunk with context header for LLM."""
        parts = []
        if self.context_header:
            parts.append(self.context_header)
        parts.append(self.text)
        return "\n\n".join(parts)


# ============================================================================
# Chunk Configuration
# ============================================================================

@dataclass
class ChunkConfig:
    """Configuration for structural chunking.

    Token budgets calibrated for qwen3-coder-30b with 16K context.
    """
    # Target token counts for source content
    target_tokens: int = 6500
    soft_max_tokens: int = 7500
    hard_max_tokens: int = 9000
    emergency_max_tokens: int = 10500  # Only for indivisible material

    # Adjustments by content type
    code_target_tokens: int = 4500  # Dense code needs smaller chunks
    table_target_tokens: int = 4500
    math_target_tokens: int = 4000
    prose_target_tokens: int = 7500  # Narrative can be larger

    # Context header budget
    context_header_tokens: int = 300

    # Boundaries
    prefer_section_breaks: bool = True
    prefer_subsection_breaks: bool = True
    prefer_page_breaks: bool = False  # Pages are metadata, not split units

    # Overlap strategy
    use_context_headers: bool = True  # Semantic overlap via headers
    use_text_overlap: bool = False  # Avoid dumb text overlap

    # Quality thresholds
    min_quality_score: float = 0.5  # Flag chunks below this


# ============================================================================
# Block Extractor - Markdown AST to Block IR
# ============================================================================

class BlockExtractor:
    """Extract blocks from markdown into structured IR."""

    # Patterns for markdown parsing
    HEADING_RE = re.compile(r'^(#{1,6})\s+(.+)$')
    CODE_FENCE_RE = re.compile(r'^```(\w*)?(.*)$')
    TABLE_ROW_RE = re.compile(r'^\|.*\|$')
    TABLE_SEP_RE = re.compile(r'^\|[-:| ]+\|$')
    LIST_ITEM_RE = re.compile(r'^(\s*)[-*+]|\d+\.\s')
    BLOCKQUOTE_RE = re.compile(r'^>\s*')
    PAGE_MARKER_RE = re.compile(r'<!--\s*page\s*(\d+)\s*-->', re.IGNORECASE)
    EQUATION_RE = re.compile(r'^\$\$|^\\\[')

    def __init__(self):
        self.blocks: list[Block] = []
        self.current_section: list[str] = []
        self.current_page: int = 1
        self.reading_order: int = 0

    def extract_from_markdown(
        self,
        source: Path | str,
        doc_id: str,
        source_file: str = "",
    ) -> list[Block]:
        """Extract blocks from a markdown file or string."""
        if isinstance(source, Path):
            text = source.read_text()
            source_file = source_file or source.name
        else:
            text = source
            source_file = source_file or "inline"

        self.blocks = []
        self.current_section = []
        self.current_page = 1
        self.reading_order = 0

        lines = text.split('\n')
        i = 0

        while i < len(lines):
            line = lines[i]

            # Check for page marker
            page_match = self.PAGE_MARKER_RE.search(line)
            if page_match:
                self.current_page = int(page_match.group(1))
                i += 1
                continue

            # Skip empty lines (don't create blocks for them)
            if not line.strip():
                i += 1
                continue

            # Try to parse different block types
            block, consumed = self._parse_block(lines, i, doc_id, source_file)
            if block:
                self.blocks.append(block)
                i += consumed
            else:
                i += 1

        return self.blocks

    def _parse_block(
        self,
        lines: list[str],
        start: int,
        doc_id: str,
        source_file: str,
    ) -> tuple[Block | None, int]:
        """Parse a block starting at the given line."""
        line = lines[start]

        # Heading
        heading_match = self.HEADING_RE.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()

            # Update section path
            while len(self.current_section) >= level:
                self.current_section.pop()
            self.current_section.append(text)

            return self._make_block(
                doc_id, source_file,
                BlockType.HEADING, line,
                start + 1, start + 1,
                heading_level=level,
            ), 1

        # Code fence
        fence_match = self.CODE_FENCE_RE.match(line)
        if fence_match:
            language = fence_match.group(1) or ""
            code_lines = [line]
            end = start + 1
            while end < len(lines):
                code_lines.append(lines[end])
                if lines[end].startswith('```'):
                    end += 1
                    break
                end += 1

            return self._make_block(
                doc_id, source_file,
                BlockType.CODE, '\n'.join(code_lines),
                start + 1, end,
                language=language,
            ), len(code_lines)

        # Table
        if self.TABLE_ROW_RE.match(line):
            table_lines = []
            end = start
            while end < len(lines) and (
                self.TABLE_ROW_RE.match(lines[end]) or
                self.TABLE_SEP_RE.match(lines[end])
            ):
                table_lines.append(lines[end])
                end += 1

            if len(table_lines) >= 2:  # At least header + separator
                return self._make_block(
                    doc_id, source_file,
                    BlockType.TABLE, '\n'.join(table_lines),
                    start + 1, end,
                ), len(table_lines)

        # Equation block ($$...$$)
        if line.strip().startswith('$$') or line.strip().startswith('\\['):
            eq_lines = [line]
            end = start + 1
            while end < len(lines):
                eq_lines.append(lines[end])
                if lines[end].strip().endswith('$$') or lines[end].strip() == '\\]':
                    end += 1
                    break
                end += 1

            return self._make_block(
                doc_id, source_file,
                BlockType.EQUATION, '\n'.join(eq_lines),
                start + 1, end,
            ), len(eq_lines)

        # List
        if self.LIST_ITEM_RE.match(line):
            list_lines = []
            end = start
            base_indent = len(line) - len(line.lstrip())

            while end < len(lines):
                curr_line = lines[end]
                if not curr_line.strip():
                    # Empty line might continue list
                    if end + 1 < len(lines) and self.LIST_ITEM_RE.match(lines[end + 1]):
                        list_lines.append(curr_line)
                        end += 1
                        continue
                    break

                curr_indent = len(curr_line) - len(curr_line.lstrip())
                if self.LIST_ITEM_RE.match(curr_line) or curr_indent > base_indent:
                    list_lines.append(curr_line)
                    end += 1
                else:
                    break

            if list_lines:
                return self._make_block(
                    doc_id, source_file,
                    BlockType.LIST, '\n'.join(list_lines),
                    start + 1, end,
                ), len(list_lines)

        # Blockquote
        if self.BLOCKQUOTE_RE.match(line):
            quote_lines = []
            end = start
            while end < len(lines) and (
                self.BLOCKQUOTE_RE.match(lines[end]) or
                (lines[end].strip()
                 and quote_lines and not self.HEADING_RE.match(lines[end]))
            ):
                quote_lines.append(lines[end])
                end += 1

            return self._make_block(
                doc_id, source_file,
                BlockType.BLOCKQUOTE, '\n'.join(quote_lines),
                start + 1, end,
            ), len(quote_lines)

        # HTML block
        if line.strip().startswith('<') and not line.strip().startswith('<!--'):
            html_lines = [line]
            end = start + 1
            # Collect until we see a closing tag or blank line
            while end < len(lines) and lines[end].strip():
                html_lines.append(lines[end])
                end += 1

            return self._make_block(
                doc_id, source_file,
                BlockType.HTML, '\n'.join(html_lines),
                start + 1, end,
            ), len(html_lines)

        # Default: paragraph
        para_lines = []
        end = start
        while end < len(lines):
            curr_line = lines[end]
            # Stop at block-level elements
            if not curr_line.strip():
                break
            if self.HEADING_RE.match(curr_line):
                break
            if self.CODE_FENCE_RE.match(curr_line):
                break
            if self.TABLE_ROW_RE.match(curr_line):
                break
            if self.LIST_ITEM_RE.match(curr_line) and end > start:
                break

            para_lines.append(curr_line)
            end += 1

        if para_lines:
            return self._make_block(
                doc_id, source_file,
                BlockType.PARAGRAPH, '\n'.join(para_lines),
                start + 1, end,
            ), len(para_lines)

        return None, 1

    def _make_block(
        self,
        doc_id: str,
        source_file: str,
        block_type: BlockType,
        text: str,
        line_start: int,
        line_end: int,
        heading_level: int = 0,
        language: str = "",
    ) -> Block:
        """Create a block with all metadata."""
        self.reading_order += 1
        block_id = f"{doc_id}:p{self.current_page:03d}:b{self.reading_order:04d}"

        # Detect quality issues
        quality_score, issues = self._assess_quality(text, block_type)

        return Block(
            doc_id=doc_id,
            source_file=source_file,
            page_start=self.current_page,
            page_end=self.current_page,
            section_path=list(self.current_section),
            block_id=block_id,
            block_type=block_type,
            text=text,
            line_start=line_start,
            line_end=line_end,
            reading_order=self.reading_order,
            heading_level=heading_level,
            language=language,
            quality_score=quality_score,
            quality_issues=issues,
        )

    def _assess_quality(self, text: str, block_type: BlockType) -> tuple[float, list[str]]:
        """Assess extraction quality and detect issues."""
        issues = []
        score = 1.0

        # Replacement characters
        replacement_count = text.count('\ufffd')
        if replacement_count > 5:
            issues.append(f"replacement_chars:{replacement_count}")
            score -= 0.2

        # Broken ligatures
        for lig in ['ﬁ', 'ﬂ', 'ﬀ', 'ﬃ', 'ﬄ']:
            if lig in text:
                issues.append("broken_ligatures")
                score -= 0.1
                break

        # Excessive single-char lines (OCR artifacts)
        lines = text.split('\n')
        single_char_lines = sum(1 for line in lines if len(line.strip()) == 1)
        if single_char_lines > len(lines) * 0.2:
            issues.append("single_char_lines")
            score -= 0.2

        # Table detected as paragraph
        if block_type == BlockType.PARAGRAPH:
            if text.count('|') > 10:
                issues.append("possible_table_loss")
                score -= 0.3

        # Code indentation issues
        if block_type == BlockType.CODE:
            if not any(line.startswith(' ') or line.startswith('\t')
                       for line in lines[1:] if line.strip()):
                # No indentation in a code block is suspicious
                if len(lines) > 5:
                    issues.append("code_indentation_suspicious")
                    score -= 0.1

        return max(0.0, score), issues


# ============================================================================
# Atomic Unit Builder
# ============================================================================

class AtomicUnitBuilder:
    """Build atomic units from blocks."""

    def build(self, blocks: list[Block]) -> list[AtomicUnit]:
        """Group blocks into atomic units."""
        units = []
        i = 0

        while i < len(blocks):
            block = blocks[i]

            # Heading + following content
            if block.block_type == BlockType.HEADING:
                unit_blocks = [block]
                j = i + 1

                # Include following paragraph(s) until next heading
                while j < len(blocks):
                    next_block = blocks[j]
                    if next_block.block_type == BlockType.HEADING:
                        # Only include if lower level heading
                        if next_block.heading_level <= block.heading_level:
                            break
                        unit_blocks.append(next_block)
                    elif next_block.block_type in (
                        BlockType.PARAGRAPH, BlockType.LIST,
                        BlockType.BLOCKQUOTE
                    ):
                        unit_blocks.append(next_block)
                    else:
                        break
                    j += 1

                    # Don't make heading groups too large
                    if sum(b.token_count for b in unit_blocks) > 2000:
                        break

                units.append(AtomicUnit(
                    blocks=unit_blocks,
                    unit_type="heading_group",
                    section_path=block.section_path,
                    splittable=len(unit_blocks) > 1,
                ))
                i = j
                continue

            # Standalone blocks that are their own atomic units
            if block.block_type in (
                BlockType.CODE, BlockType.TABLE, BlockType.EQUATION,
                BlockType.FIGURE
            ):
                units.append(AtomicUnit(
                    blocks=[block],
                    unit_type=block.block_type.value,
                    section_path=block.section_path,
                    splittable=block.block_type == BlockType.TABLE,  # Tables can be split by rows
                ))
                i += 1
                continue

            # Lists are atomic
            if block.block_type == BlockType.LIST:
                units.append(AtomicUnit(
                    blocks=[block],
                    unit_type="list",
                    section_path=block.section_path,
                    splittable=True,  # Can split by items
                ))
                i += 1
                continue

            # Paragraphs can be grouped
            if block.block_type == BlockType.PARAGRAPH:
                para_blocks = [block]
                j = i + 1

                # Group consecutive paragraphs in same section
                while j < len(blocks):
                    next_block = blocks[j]
                    if next_block.block_type != BlockType.PARAGRAPH:
                        break
                    if next_block.section_path != block.section_path:
                        break
                    para_blocks.append(next_block)
                    j += 1

                    # Limit group size
                    if sum(b.token_count for b in para_blocks) > 1500:
                        break

                units.append(AtomicUnit(
                    blocks=para_blocks,
                    unit_type="paragraph_group",
                    section_path=block.section_path,
                    splittable=len(para_blocks) > 1,
                ))
                i = j
                continue

            # Everything else: single block unit
            units.append(AtomicUnit(
                blocks=[block],
                unit_type=block.block_type.value,
                section_path=block.section_path,
                splittable=False,
            ))
            i += 1

        return units


# ============================================================================
# Structural Chunker - Token-aware packing
# ============================================================================

class StructuralChunker:
    """Pack atomic units into token-bounded chunks."""

    def __init__(self, config: ChunkConfig | None = None):
        self.config = config or ChunkConfig()

    def pack(
        self,
        blocks: list[Block],
        doc_id: str | None = None,
    ) -> list[StructuredChunk]:
        """Pack blocks into structured chunks."""
        if not blocks:
            return []

        doc_id = doc_id or blocks[0].doc_id

        # Build atomic units
        builder = AtomicUnitBuilder()
        units = builder.build(blocks)

        # Group by section for structural packing
        chunks = []
        current_units: list[AtomicUnit] = []
        current_tokens = 0
        chunk_index = 0

        for unit in units:
            unit_tokens = unit.token_count
            target = self._get_target_tokens(unit)

            # Handle oversized units
            if unit_tokens > self.config.hard_max_tokens:
                # Finalize current chunk first
                if current_units:
                    chunks.append(self._finalize_chunk(
                        current_units, doc_id, chunk_index,
                        chunks[-1].chunk_id if chunks else None
                    ))
                    chunk_index += 1
                    current_units = []
                    current_tokens = 0

                # Split the oversized unit
                split_chunks = self._split_oversized(unit, doc_id, chunk_index)
                for sc in split_chunks:
                    # Link to previous
                    if chunks:
                        sc.previous_chunk = chunks[-1].chunk_id
                        chunks[-1].next_chunk = sc.chunk_id
                    chunks.append(sc)
                    chunk_index += 1
                continue

            # Check if adding this unit would exceed soft max
            if current_units and current_tokens + unit_tokens > self.config.soft_max_tokens:
                # Finalize current chunk
                chunks.append(self._finalize_chunk(
                    current_units, doc_id, chunk_index,
                    chunks[-1].chunk_id if chunks else None
                ))
                chunk_index += 1
                current_units = []
                current_tokens = 0

            # Add unit to current chunk
            current_units.append(unit)
            current_tokens += unit_tokens

            # Check if we've hit target at a good boundary
            if current_tokens >= target and self._is_good_boundary(unit, units):
                chunks.append(self._finalize_chunk(
                    current_units, doc_id, chunk_index,
                    chunks[-1].chunk_id if chunks else None
                ))
                chunk_index += 1
                current_units = []
                current_tokens = 0

        # Finalize remaining
        if current_units:
            chunks.append(self._finalize_chunk(
                current_units, doc_id, chunk_index,
                chunks[-1].chunk_id if chunks else None
            ))

        # Link next pointers
        for i, chunk in enumerate(chunks[:-1]):
            chunk.next_chunk = chunks[i + 1].chunk_id

        return chunks

    def _get_target_tokens(self, unit: AtomicUnit) -> int:
        """Get target tokens based on content type."""
        config = self.config

        # Check block types in unit
        types = {b.block_type for b in unit.blocks}

        if BlockType.CODE in types:
            return config.code_target_tokens
        if BlockType.TABLE in types:
            return config.table_target_tokens
        if BlockType.EQUATION in types:
            return config.math_target_tokens

        # Check for dense technical content
        text = unit.text
        if text.count('`') > 10:  # Inline code
            return config.code_target_tokens

        return config.target_tokens

    def _is_good_boundary(self, unit: AtomicUnit, all_units: list[AtomicUnit]) -> bool:
        """Check if this is a good place to end a chunk."""
        # Section ends are always good
        if unit.unit_type == "heading_group":
            return True

        # After standalone artifacts
        if unit.unit_type in ("code", "table", "equation"):
            return True

        return False

    def _finalize_chunk(
        self,
        units: list[AtomicUnit],
        doc_id: str,
        index: int,
        previous_chunk: str | None,
    ) -> StructuredChunk:
        """Create a StructuredChunk from atomic units."""
        # Collect all blocks
        all_blocks = []
        for unit in units:
            all_blocks.extend(unit.blocks)

        # Build text
        text_parts = []
        for unit in units:
            text_parts.append(unit.text)
        text = "\n\n".join(text_parts)

        # Collect metadata
        pages = set()
        block_ids = []
        contains = set()

        for block in all_blocks:
            for p in range(block.page_start, block.page_end + 1):
                pages.add(p)
            block_ids.append(block.block_id)
            contains.add(block.block_type.value)

        # Section path from first block
        section_path = units[0].section_path if units else []

        chunk_id = f"{doc_id}:c{index:04d}"

        # Build context header if enabled
        context_header = ""
        if self.config.use_context_headers and section_path:
            context_header = self._build_context_header(
                section_path, sorted(pages), all_blocks
            )

        return StructuredChunk(
            chunk_id=chunk_id,
            doc_id=doc_id,
            pages=sorted(pages),
            section_path=section_path,
            token_count=count_tokens(text),
            block_ids=block_ids,
            previous_chunk=previous_chunk,
            next_chunk=None,
            contains=sorted(contains),
            text=text,
            context_header=context_header,
            line_start=min(
                b.line_start for b in all_blocks) if all_blocks else 0,
            line_end=max(b.line_end for b in all_blocks) if all_blocks else 0,
        )

    def _build_context_header(
        self,
        section_path: list[str],
        pages: list[int],
        blocks: list[Block],
    ) -> str:
        """Build semantic context header for a chunk."""
        parts = ["<!-- chunk_context -->"]

        if section_path:
            parts.append(f"Section path: {' > '.join(section_path)}")

        if pages:
            if len(pages) == 1:
                parts.append(f"Page: {pages[0]}")
            else:
                parts.append(f"Pages: {pages[0]}-{pages[-1]}")

        # Extract definitions/terms from headings
        definitions = []
        for block in blocks:
            if block.block_type == BlockType.HEADING:
                definitions.append(block.text.lstrip('#').strip())

        if definitions:
            parts.append(f"Topics: {', '.join(definitions[:5])}")

        parts.append("<!-- /chunk_context -->")

        return '\n'.join(parts)

    def _split_oversized(
        self,
        unit: AtomicUnit,
        doc_id: str,
        start_index: int,
    ) -> list[StructuredChunk]:
        """Split an oversized atomic unit into multiple chunks."""
        chunks = []

        if unit.unit_type == "table" and unit.splittable:
            # Split table by rows
            chunks = self._split_table(unit, doc_id, start_index)
        elif unit.unit_type in ("paragraph_group", "heading_group") and unit.splittable:
            # Split by blocks
            chunks = self._split_by_blocks(unit, doc_id, start_index)
        elif unit.unit_type == "code":
            # Split code by functions/classes or lines
            chunks = self._split_code(unit, doc_id, start_index)
        else:
            # Emergency: split by token count
            chunks = self._split_by_tokens(unit, doc_id, start_index)

        # Mark continuations
        for i, chunk in enumerate(chunks[1:], 1):
            chunk.continued_from = chunks[i - 1].chunk_id
            chunk.continuation_type = unit.unit_type

        return chunks

    def _split_table(
        self,
        unit: AtomicUnit,
        doc_id: str,
        start_index: int,
    ) -> list[StructuredChunk]:
        """Split a table by row groups."""
        # Get table text
        table_block = unit.blocks[0]
        lines = table_block.text.split('\n')

        # Find header (first rows before data)
        header_lines = []
        data_lines = []
        in_header = True

        for line in lines:
            if in_header and self._is_table_separator(line):
                header_lines.append(line)
                in_header = False
            elif in_header:
                header_lines.append(line)
            else:
                data_lines.append(line)

        header_text = '\n'.join(header_lines)
        header_tokens = count_tokens(header_text)
        target = self.config.hard_max_tokens - header_tokens - 200

        chunks = []
        current_rows = []
        current_tokens = 0

        for row in data_lines:
            row_tokens = count_tokens(row)

            if current_tokens + row_tokens > target and current_rows:
                # Create chunk with header + rows
                chunk_text = header_text + '\n' + '\n'.join(current_rows)
                chunks.append(StructuredChunk(
                    chunk_id=f"{doc_id}:c{start_index + len(chunks):04d}",
                    doc_id=doc_id,
                    pages=unit.pages,
                    section_path=unit.section_path,
                    token_count=count_tokens(chunk_text),
                    block_ids=[table_block.block_id],
                    previous_chunk=None,
                    next_chunk=None,
                    contains=["table"],
                    text=chunk_text,
                    line_start=table_block.line_start,
                    line_end=table_block.line_end,
                ))
                current_rows = []
                current_tokens = 0

            current_rows.append(row)
            current_tokens += row_tokens

        # Final chunk
        if current_rows:
            chunk_text = header_text + '\n' + '\n'.join(current_rows)
            chunks.append(StructuredChunk(
                chunk_id=f"{doc_id}:c{start_index + len(chunks):04d}",
                doc_id=doc_id,
                pages=unit.pages,
                section_path=unit.section_path,
                token_count=count_tokens(chunk_text),
                block_ids=[table_block.block_id],
                previous_chunk=None,
                next_chunk=None,
                contains=["table"],
                text=chunk_text,
                line_start=table_block.line_start,
                line_end=table_block.line_end,
            ))

        return chunks if chunks else [self._unit_to_chunk(unit, doc_id, start_index)]

    def _is_table_separator(self, line: str) -> bool:
        """Check if line is a table separator (|---|---|)."""
        return bool(re.match(r'^\|[-:| ]+\|$', line.strip()))

    def _split_by_blocks(
        self,
        unit: AtomicUnit,
        doc_id: str,
        start_index: int,
    ) -> list[StructuredChunk]:
        """Split by individual blocks."""
        chunks = []
        current_blocks = []
        current_tokens = 0
        target = self.config.hard_max_tokens

        for block in unit.blocks:
            if current_tokens + block.token_count > target and current_blocks:
                chunks.append(self._blocks_to_chunk(
                    current_blocks, doc_id, start_index + len(chunks),
                    unit.section_path
                ))
                current_blocks = []
                current_tokens = 0

            current_blocks.append(block)
            current_tokens += block.token_count

        if current_blocks:
            chunks.append(self._blocks_to_chunk(
                current_blocks, doc_id, start_index + len(chunks),
                unit.section_path
            ))

        return chunks

    def _split_code(
        self,
        unit: AtomicUnit,
        doc_id: str,
        start_index: int,
    ) -> list[StructuredChunk]:
        """Split code by functions/classes or lines."""
        code_block = unit.blocks[0]
        lines = code_block.text.split('\n')

        # Try to find function/class boundaries
        boundaries = []
        for i, line in enumerate(lines):
            stripped = line.strip()
            if any(stripped.startswith(kw) for kw in [
                'def ', 'class ', 'function ', 'fn ', 'func ',
                'pub fn ', 'pub struct ', 'impl ', 'async fn ',
            ]):
                boundaries.append(i)

        if not boundaries or len(boundaries) < 2:
            # Fall back to line-based splitting
            return self._split_by_tokens(unit, doc_id, start_index)

        # Split at function boundaries
        chunks = []
        target = self.config.hard_max_tokens
        fence_start = lines[0] if lines[0].startswith('```') else '```'
        fence_end = '```'

        current_lines = [fence_start]
        current_tokens = count_tokens(fence_start)

        for i in range(len(boundaries)):
            start_line = boundaries[i]
            end_line = boundaries[i + 1] if i + \
                1 < len(boundaries) else len(lines) - 1

            segment = lines[start_line:end_line]
            segment_tokens = count_tokens('\n'.join(segment))

            if current_tokens + segment_tokens > target and len(current_lines) > 1:
                current_lines.append(fence_end)
                chunk_text = '\n'.join(current_lines)
                chunks.append(StructuredChunk(
                    chunk_id=f"{doc_id}:c{start_index + len(chunks):04d}",
                    doc_id=doc_id,
                    pages=unit.pages,
                    section_path=unit.section_path,
                    token_count=count_tokens(chunk_text),
                    block_ids=[code_block.block_id],
                    previous_chunk=None,
                    next_chunk=None,
                    contains=["code"],
                    text=chunk_text,
                    line_start=code_block.line_start,
                    line_end=code_block.line_end,
                ))
                current_lines = [fence_start]
                current_tokens = count_tokens(fence_start)

            current_lines.extend(segment)
            current_tokens += segment_tokens

        # Final chunk
        if len(current_lines) > 1:
            if not current_lines[-1].startswith('```'):
                current_lines.append(fence_end)
            chunk_text = '\n'.join(current_lines)
            chunks.append(StructuredChunk(
                chunk_id=f"{doc_id}:c{start_index + len(chunks):04d}",
                doc_id=doc_id,
                pages=unit.pages,
                section_path=unit.section_path,
                token_count=count_tokens(chunk_text),
                block_ids=[code_block.block_id],
                previous_chunk=None,
                next_chunk=None,
                contains=["code"],
                text=chunk_text,
                line_start=code_block.line_start,
                line_end=code_block.line_end,
            ))

        return chunks if chunks else [self._unit_to_chunk(unit, doc_id, start_index)]

    def _split_by_tokens(
        self,
        unit: AtomicUnit,
        doc_id: str,
        start_index: int,
    ) -> list[StructuredChunk]:
        """Emergency split by token count."""
        text = unit.text
        lines = text.split('\n')

        chunks = []
        current_lines = []
        current_tokens = 0
        target = self.config.emergency_max_tokens

        for line in lines:
            line_tokens = count_tokens(line)

            if current_tokens + line_tokens > target and current_lines:
                chunk_text = '\n'.join(current_lines)
                chunks.append(StructuredChunk(
                    chunk_id=f"{doc_id}:c{start_index + len(chunks):04d}",
                    doc_id=doc_id,
                    pages=unit.pages,
                    section_path=unit.section_path,
                    token_count=count_tokens(chunk_text),
                    block_ids=[b.block_id for b in unit.blocks],
                    previous_chunk=None,
                    next_chunk=None,
                    contains=[b.block_type.value for b in unit.blocks],
                    text=chunk_text,
                    line_start=unit.line_start,
                    line_end=unit.line_end,
                ))
                current_lines = []
                current_tokens = 0

            current_lines.append(line)
            current_tokens += line_tokens

        if current_lines:
            chunk_text = '\n'.join(current_lines)
            chunks.append(StructuredChunk(
                chunk_id=f"{doc_id}:c{start_index + len(chunks):04d}",
                doc_id=doc_id,
                pages=unit.pages,
                section_path=unit.section_path,
                token_count=count_tokens(chunk_text),
                block_ids=[b.block_id for b in unit.blocks],
                previous_chunk=None,
                next_chunk=None,
                contains=[b.block_type.value for b in unit.blocks],
                text=chunk_text,
                line_start=unit.line_start,
                line_end=unit.line_end,
            ))

        return chunks

    def _unit_to_chunk(
        self,
        unit: AtomicUnit,
        doc_id: str,
        index: int,
    ) -> StructuredChunk:
        """Convert a single unit to a chunk (fallback)."""
        return StructuredChunk(
            chunk_id=f"{doc_id}:c{index:04d}",
            doc_id=doc_id,
            pages=unit.pages,
            section_path=unit.section_path,
            token_count=unit.token_count,
            block_ids=[b.block_id for b in unit.blocks],
            previous_chunk=None,
            next_chunk=None,
            contains=[b.block_type.value for b in unit.blocks],
            text=unit.text,
            line_start=unit.line_start,
            line_end=unit.line_end,
        )

    def _blocks_to_chunk(
        self,
        blocks: list[Block],
        doc_id: str,
        index: int,
        section_path: list[str],
    ) -> StructuredChunk:
        """Convert blocks to a chunk."""
        text = '\n\n'.join(b.text for b in blocks)
        pages = set()
        for b in blocks:
            for p in range(b.page_start, b.page_end + 1):
                pages.add(p)

        return StructuredChunk(
            chunk_id=f"{doc_id}:c{index:04d}",
            doc_id=doc_id,
            pages=sorted(pages),
            section_path=section_path,
            token_count=count_tokens(text),
            block_ids=[b.block_id for b in blocks],
            previous_chunk=None,
            next_chunk=None,
            contains=list(set(b.block_type.value for b in blocks)),
            text=text,
            line_start=min(b.line_start for b in blocks),
            line_end=max(b.line_end for b in blocks),
        )


# ============================================================================
# Quality Assessment
# ============================================================================

@dataclass
class QualityReport:
    """Quality assessment for a document's extraction."""
    doc_id: str
    total_blocks: int
    total_chunks: int
    total_tokens: int
    quality_scores: dict[str, float]  # by page
    issues_by_type: dict[str, int]
    pages_needing_review: list[int]
    low_quality_blocks: list[str]  # block_ids

    def to_dict(self) -> dict:
        return {
            "doc_id": self.doc_id,
            "total_blocks": self.total_blocks,
            "total_chunks": self.total_chunks,
            "total_tokens": self.total_tokens,
            "quality_scores": self.quality_scores,
            "issues_by_type": self.issues_by_type,
            "pages_needing_review": self.pages_needing_review,
            "low_quality_blocks": self.low_quality_blocks,
        }


def assess_extraction_quality(
    blocks: list[Block],
    chunks: list[StructuredChunk],
    min_quality: float = 0.5,
) -> QualityReport:
    """Assess overall extraction quality."""
    doc_id = blocks[0].doc_id if blocks else "unknown"

    # Aggregate quality by page
    page_scores: dict[int, list[float]] = {}
    for block in blocks:
        for p in range(block.page_start, block.page_end + 1):
            if p not in page_scores:
                page_scores[p] = []
            page_scores[p].append(block.quality_score)

    quality_scores = {
        str(p): sum(scores) / len(scores)
        for p, scores in page_scores.items()
    }

    # Count issues by type
    issues_by_type: dict[str, int] = {}
    for block in blocks:
        for issue in block.quality_issues:
            issue_type = issue.split(':')[0]
            issues_by_type[issue_type] = issues_by_type.get(issue_type, 0) + 1

    # Find pages needing review
    pages_needing_review = [
        int(p) for p, score in quality_scores.items()
        if score < min_quality
    ]

    # Find low quality blocks
    low_quality_blocks = [
        block.block_id for block in blocks
        if block.quality_score < min_quality
    ]

    return QualityReport(
        doc_id=doc_id,
        total_blocks=len(blocks),
        total_chunks=len(chunks),
        total_tokens=sum(c.token_count for c in chunks),
        quality_scores=quality_scores,
        issues_by_type=issues_by_type,
        pages_needing_review=pages_needing_review,
        low_quality_blocks=low_quality_blocks,
    )


# ============================================================================
# File I/O
# ============================================================================

def save_blocks(blocks: list[Block], path: Path):
    """Save blocks to JSONL file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w') as f:
        for block in blocks:
            f.write(json.dumps(block.to_dict()) + '\n')


def load_blocks(path: Path) -> list[Block]:
    """Load blocks from JSONL file."""
    blocks = []
    with path.open() as f:
        for line in f:
            if line.strip():
                blocks.append(Block.from_dict(json.loads(line)))
    return blocks


def save_chunks(chunks: list[StructuredChunk], path: Path):
    """Save chunks to JSONL file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w') as f:
        for chunk in chunks:
            f.write(json.dumps(chunk.to_dict()) + '\n')


def load_chunks(path: Path) -> list[StructuredChunk]:
    """Load chunks from JSONL file."""
    chunks = []
    with path.open() as f:
        for line in f:
            if line.strip():
                chunks.append(StructuredChunk.from_dict(json.loads(line)))
    return chunks


# ============================================================================
# CLI
# ============================================================================

def main():
    """CLI for testing structured chunking."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract and chunk a markdown file"
    )
    parser.add_argument("source", help="Markdown file to process")
    parser.add_argument("--doc-id", default=None, help="Document ID")
    parser.add_argument("--output-dir", default=None, help="Output directory")
    parser.add_argument("--target-tokens", type=int, default=6500)
    parser.add_argument("--show-stats", action="store_true")
    args = parser.parse_args()

    source = Path(args.source)
    if not source.exists():
        print(f"Error: {source} not found")
        return 1

    doc_id = args.doc_id or source.stem
    output_dir = Path(
        args.output_dir) if args.output_dir else source.parent / "extracted"

    # Extract blocks
    print(f"Extracting blocks from {source}...")
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(source, doc_id)
    print(f"  Extracted {len(blocks)} blocks")

    # Pack chunks
    print(f"Packing into chunks (target: {args.target_tokens} tokens)...")
    config = ChunkConfig(target_tokens=args.target_tokens)
    chunker = StructuralChunker(config)
    chunks = chunker.pack(blocks, doc_id)
    print(f"  Created {len(chunks)} chunks")

    # Quality assessment
    report = assess_extraction_quality(blocks, chunks)

    # Save outputs
    output_dir.mkdir(parents=True, exist_ok=True)
    save_blocks(blocks, output_dir / "blocks.jsonl")
    save_chunks(chunks, output_dir / "chunks.jsonl")
    (output_dir / "quality_report.json").write_text(
        json.dumps(report.to_dict(), indent=2)
    )

    print(f"\nOutputs saved to {output_dir}/")
    print(f"  blocks.jsonl: {len(blocks)} blocks")
    print(f"  chunks.jsonl: {len(chunks)} chunks")
    print(f"  quality_report.json")

    if args.show_stats:
        print(f"\nStatistics:")
        print(f"  Total tokens: {report.total_tokens}")
        print(f"  Avg tokens/chunk: {report.total_tokens / len(chunks):.0f}")
        print(f"  Pages needing review: {report.pages_needing_review}")
        print(f"  Issues: {report.issues_by_type}")

    return 0


if __name__ == "__main__":
    exit(main())
