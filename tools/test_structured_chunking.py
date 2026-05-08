#!/usr/bin/env python3
"""Tests for structured chunking module.

Usage:
    python3 tools/test_structured_chunking.py
    pytest tools/test_structured_chunking.py -v
"""
from __future__ import annotations
from wiki_structured_chunking import (
    BlockExtractor,
    StructuralChunker,
    ChunkConfig,
    Block,
    BlockType,
    AtomicUnit,
    AtomicUnitBuilder,
    StructuredChunk,
    count_tokens,
    assess_extraction_quality,
)

import sys
from pathlib import Path

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent))


def test_block_extraction_heading():
    """Test extraction of heading blocks."""
    md = """# Chapter 1

Introduction text.

## Section 1.1

More text here.
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    headings = [b for b in blocks if b.block_type == BlockType.HEADING]
    assert len(headings) == 2
    assert headings[0].heading_level == 1
    assert headings[1].heading_level == 2
    print("✓ test_block_extraction_heading")


def test_block_extraction_code():
    """Test extraction of code blocks."""
    md = """# Code Example

```javascript
function hello() {
    return "world";
}
```

Done.
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    code_blocks = [b for b in blocks if b.block_type == BlockType.CODE]
    assert len(code_blocks) == 1
    assert "function hello()" in code_blocks[0].text
    assert code_blocks[0].language == "javascript"
    print("✓ test_block_extraction_code")


def test_block_extraction_table():
    """Test extraction of table blocks."""
    md = """# Data

| Column A | Column B |
|----------|----------|
| Value 1  | Value 2  |
| Value 3  | Value 4  |

End.
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    tables = [b for b in blocks if b.block_type == BlockType.TABLE]
    assert len(tables) == 1
    assert "Column A" in tables[0].text
    assert tables[0].text.count("|") >= 8
    print("✓ test_block_extraction_table")


def test_block_extraction_list():
    """Test extraction of list blocks."""
    md = """# Items

- First item
- Second item
  - Nested item
- Third item

Done.
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    lists = [b for b in blocks if b.block_type == BlockType.LIST]
    assert len(lists) == 1
    assert "First item" in lists[0].text
    assert "Nested item" in lists[0].text
    print("✓ test_block_extraction_list")


def test_section_path_tracking():
    """Test that section paths are tracked correctly."""
    md = """# Chapter 1

Text.

## Section 1.1

More text.

### Subsection 1.1.1

Details.

## Section 1.2

Final.
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    # Find the subsection heading
    subsection = next(b for b in blocks if "Subsection 1.1.1" in b.text)
    assert subsection.section_path == [
        "Chapter 1", "Section 1.1", "Subsection 1.1.1"]

    # After going to Section 1.2, section path should reset
    section_12 = next(b for b in blocks if "Section 1.2" in b.text)
    assert section_12.section_path == ["Chapter 1", "Section 1.2"]
    print("✓ test_section_path_tracking")


def test_atomic_unit_builder():
    """Test atomic unit grouping."""
    md = """# Overview

This is the introduction.

Another paragraph.

```python
def example():
    pass
```
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    builder = AtomicUnitBuilder()
    units = builder.build(blocks)

    # Should have: heading_group (heading + paragraphs), code
    assert len(units) >= 2

    # First unit should be heading group
    assert units[0].unit_type == "heading_group"
    assert any(b.block_type == BlockType.HEADING for b in units[0].blocks)

    # Should have a code unit
    code_units = [u for u in units if u.unit_type == "code"]
    assert len(code_units) == 1
    print("✓ test_atomic_unit_builder")


def test_structural_chunking_basic():
    """Test basic structural chunking."""
    # Create a document with multiple sections
    md = """# Chapter 1

This is the first chapter with some content.

## Section 1.1

Details about section 1.1.

## Section 1.2

More details here.

# Chapter 2

Second chapter content.
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    config = ChunkConfig(
        target_tokens=100, soft_max_tokens=150, hard_max_tokens=200)
    chunker = StructuralChunker(config)
    chunks = chunker.pack(blocks, "test-doc")

    # Should create multiple chunks
    assert len(chunks) >= 1

    # Check chunk linking
    for i, chunk in enumerate(chunks):
        if i > 0:
            assert chunk.previous_chunk == chunks[i-1].chunk_id
        if i < len(chunks) - 1:
            assert chunk.next_chunk == chunks[i+1].chunk_id
    print("✓ test_structural_chunking_basic")


def test_token_counting():
    """Test token counting function."""
    text = "Hello, this is a test sentence."
    tokens = count_tokens(text)

    # Should be reasonable (not zero, not huge)
    assert tokens > 0
    assert tokens < 100
    print("✓ test_token_counting")


def test_quality_assessment():
    """Test quality assessment."""
    md = """# Test

Normal text here.

More normal text.
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    config = ChunkConfig()
    chunker = StructuralChunker(config)
    chunks = chunker.pack(blocks, "test-doc")

    report = assess_extraction_quality(blocks, chunks)

    assert report.total_blocks == len(blocks)
    assert report.total_chunks == len(chunks)
    assert len(report.pages_needing_review) == 0  # Clean doc
    print("✓ test_quality_assessment")


def test_quality_issues_detection():
    """Test that quality issues are detected via extractor."""
    # Create markdown with replacement characters
    md = """# Test

This has many problems: \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd and more \ufffd\ufffd
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    # Find the paragraph with replacement characters
    para_blocks = [b for b in blocks if b.block_type == BlockType.PARAGRAPH]
    assert len(para_blocks) > 0

    # The block should have quality issues
    problem_block = para_blocks[0]
    assert problem_block.quality_score < 1.0
    assert any(
        "replacement_chars" in issue for issue in problem_block.quality_issues)
    print("✓ test_quality_issues_detection")


def test_text_normalization():
    """Test text normalization for search."""
    block = Block(
        doc_id="test",
        source_file="test.md",
        page_start=1,
        page_end=1,
        section_path=[],
        block_id="test:p001:b0001",
        block_type=BlockType.PARAGRAPH,
        text="O(n²), α ≤ β, x → y",
    )

    assert "^2" in block.normalized_text
    assert "alpha" in block.normalized_text
    assert "->" in block.normalized_text
    print("✓ test_text_normalization")


def test_page_marker_parsing():
    """Test page marker parsing."""
    md = """# Start

<!-- page 1 -->

Content on page 1.

<!-- page 2 -->

Content on page 2.
"""
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(md, "test-doc")

    # Check that page numbers are tracked
    page1_blocks = [b for b in blocks if b.page_start == 1]
    page2_blocks = [b for b in blocks if b.page_start == 2]

    assert len(page1_blocks) > 0
    assert len(page2_blocks) > 0
    print("✓ test_page_marker_parsing")


def run_all_tests():
    """Run all tests."""
    print("\nRunning structured chunking tests...\n")

    test_block_extraction_heading()
    test_block_extraction_code()
    test_block_extraction_table()
    test_block_extraction_list()
    test_section_path_tracking()
    test_atomic_unit_builder()
    test_structural_chunking_basic()
    test_token_counting()
    test_quality_assessment()
    test_quality_issues_detection()
    test_text_normalization()
    test_page_marker_parsing()

    print("\n✓ All tests passed!\n")


if __name__ == "__main__":
    run_all_tests()
