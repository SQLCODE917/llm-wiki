#!/usr/bin/env python3
"""Tests for wiki_core types."""
from pathlib import Path

from wiki_core.types import (
    Claim,
    RawClaim,
    NormalizedClaim,
    SynthesisClaim,
    SourceClaim,
    Locator,
    Frontmatter,
    ParsedFrontmatter,
    parse_locator,
    normalize_locator,
    generate_claim_id,
)


def test_locator_parsing():
    """Test Locator parsing from strings."""
    # Basic format
    loc = Locator.parse("normalized:L100")
    assert loc is not None
    assert loc.start_line == 100
    assert loc.end_line == 100
    assert loc.source is None

    # Range format
    loc = Locator.parse("normalized:L100-L105")
    assert loc.start_line == 100
    assert loc.end_line == 105

    # Range format without L prefix on end
    loc = Locator.parse("normalized:L100-105")
    assert loc.start_line == 100
    assert loc.end_line == 105

    # With source prefix
    loc = Locator.parse("js-allonge:normalized:L50-L60")
    assert loc.source == "js-allonge"
    assert loc.start_line == 50
    assert loc.end_line == 60

    # Backtick wrapped
    loc = Locator.parse("`normalized:L100`")
    assert loc.start_line == 100

    # Invalid
    assert Locator.parse("invalid") is None
    assert Locator.parse("L100") is None

    print("✓ test_locator_parsing passed")


def test_locator_serialization():
    """Test Locator serialization to string."""
    loc = Locator(start_line=100, end_line=105)
    assert str(loc) == "normalized:L100-L105"

    # Single line uses range format
    loc = Locator(start_line=50, end_line=50)
    assert str(loc) == "normalized:L50-L50"
    assert loc.to_compact_str() == "normalized:L50"

    # With source
    loc = Locator(start_line=100, end_line=200, source="slug")
    assert str(loc) == "slug:normalized:L100-L200"

    print("✓ test_locator_serialization passed")


def test_locator_methods():
    """Test Locator helper methods."""
    loc = Locator(start_line=100, end_line=110)

    assert loc.line_count == 11
    assert loc.is_single_line is False
    assert loc.contains(100)
    assert loc.contains(105)
    assert loc.contains(110)
    assert not loc.contains(99)
    assert not loc.contains(111)

    other = Locator(start_line=105, end_line=115)
    assert loc.overlaps(other)

    non_overlapping = Locator(start_line=200, end_line=210)
    assert not loc.overlaps(non_overlapping)

    print("✓ test_locator_methods passed")


def test_parse_locator_compat():
    """Test parse_locator compatibility function."""
    result = parse_locator("normalized:L100-L105")
    assert result == (100, 105)

    result = parse_locator("normalized:L50")
    assert result == (50, 50)

    result = parse_locator("invalid")
    assert result is None

    print("✓ test_parse_locator_compat passed")


def test_normalize_locator():
    """Test normalize_locator function."""
    # Single line becomes range
    assert normalize_locator("normalized:L100") == "normalized:L100-L100"

    # Range stays range
    assert normalize_locator("normalized:L100-L105") == "normalized:L100-L105"

    # With source prefix
    assert normalize_locator(
        "slug:normalized:L50") == "slug:normalized:L50-L50"

    print("✓ test_normalize_locator passed")


def test_claim_creation():
    """Test Claim creation and serialization."""
    claim = Claim(
        topic="Functions",
        claim="Functions are first-class citizens",
        evidence="In JavaScript, functions are first-class...",
        locator="normalized:L100-L105",
        chunk_index=0,
    )

    assert claim.topic == "Functions"
    assert claim.claim_id.startswith("claim_")
    assert "_c000_" in claim.claim_id

    # Serialization round-trip
    data = claim.to_dict()
    claim2 = Claim.from_dict(data)
    assert claim2.topic == claim.topic
    assert claim2.claim_id == claim.claim_id

    print("✓ test_claim_creation passed")


def test_claim_id_stability():
    """Test that claim IDs are deterministic."""
    claim1 = Claim(
        topic="Test",
        claim="Same claim text",
        evidence="Same evidence",
        locator="normalized:L100",
        chunk_index=5,
    )

    claim2 = Claim(
        topic="Test",
        claim="Same claim text",
        evidence="Different evidence",  # Evidence doesn't affect ID
        locator="normalized:L100",
        chunk_index=5,
    )

    # Same claim text + locator + chunk = same ID
    assert claim1.claim_id == claim2.claim_id

    # Different locator = different ID
    claim3 = Claim(
        topic="Test",
        claim="Same claim text",
        evidence="Same evidence",
        locator="normalized:L200",  # Different
        chunk_index=5,
    )
    assert claim1.claim_id != claim3.claim_id

    print("✓ test_claim_id_stability passed")


def test_raw_claim():
    """Test RawClaim with timestamp."""
    raw = RawClaim(
        topic="Test",
        claim="Test claim",
        evidence="Test evidence",
        locator="normalized:L50",
        chunk_index=1,
    )

    assert raw.extracted_at  # Should be auto-populated
    assert "T" in raw.extracted_at  # ISO format

    data = raw.to_dict()
    assert "extracted_at" in data

    raw2 = RawClaim.from_dict(data)
    assert raw2.extracted_at == raw.extracted_at

    print("✓ test_raw_claim passed")


def test_synthesis_claim():
    """Test SynthesisClaim with evidence IDs."""
    claim = SynthesisClaim(
        claim="Functions are first-class",
        evidence_ids=["E01", "E03"],
    )

    data = claim.to_dict()
    assert data["evidence_ids"] == ["E01", "E03"]

    claim2 = SynthesisClaim.from_dict(data)
    assert claim2.evidence_ids == claim.evidence_ids

    print("✓ test_synthesis_claim passed")


def test_source_claim():
    """Test SourceClaim with precomputed tokens."""
    claim = SourceClaim.from_row(
        page=Path("wiki/sources/test.md"),
        row=1,
        claim="Functions return values",
        evidence="A function returns the result",
        locator="normalized:L100",
    )

    assert "function" in claim.tokens
    assert "return" in claim.tokens
    assert claim.page == Path("wiki/sources/test.md")

    print("✓ test_source_claim passed")


def test_frontmatter_creation():
    """Test Frontmatter creation and YAML serialization."""
    fm = Frontmatter(
        title="Test Page",
        type="concept",
        tags=["javascript", "functions"],
        sources=["../sources/test.md"],
    )

    yaml = fm.to_yaml()
    assert "title: Test Page" in yaml
    assert "type: concept" in yaml
    # PyYAML formats list items without leading indent in our config
    assert "- javascript" in yaml
    assert "- ../sources/test.md" in yaml

    print("✓ test_frontmatter_creation passed")


def test_frontmatter_source_page():
    """Test Frontmatter for source pages."""
    fm = Frontmatter(
        title="Source: test",
        type="source",
        source_id="test",
        source_type="pdf",
        raw_path="../../raw/imported/test/",
        normalized_path="../../raw/normalized/test/",
    )

    yaml = fm.to_yaml()
    assert "source_id: test" in yaml
    assert "source_type: pdf" in yaml

    data = fm.to_dict()
    fm2 = Frontmatter.from_dict(data)
    assert fm2.source_id == "test"

    print("✓ test_frontmatter_source_page passed")


if __name__ == "__main__":
    test_locator_parsing()
    test_locator_serialization()
    test_locator_methods()
    test_parse_locator_compat()
    test_normalize_locator()
    test_claim_creation()
    test_claim_id_stability()
    test_raw_claim()
    test_synthesis_claim()
    test_source_claim()
    test_frontmatter_creation()
    test_frontmatter_source_page()

    print()
    print("All tests passed! ✓")
