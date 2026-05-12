"""Tests for wiki_io.evidence.ranges module."""
import pytest
from wiki_io.evidence.ranges import (
    normalize_locator,
    parse_locator_range,
    locator_to_range,
    locator_within_ranges,
    ranges_overlap,
    merge_ranges,
    format_locator,
    SourceRange,
)


class TestNormalizeLocator:
    """Tests for normalize_locator()."""

    def test_simple_line(self):
        assert normalize_locator("L12") == "normalized:L12"

    def test_shorthand_range(self):
        assert normalize_locator("L12-34") == "normalized:L12-L34"

    def test_full_format(self):
        assert normalize_locator("normalized:L12-L34") == "normalized:L12-L34"

    def test_backticks_stripped(self):
        assert normalize_locator("`normalized:L12`") == "normalized:L12"

    def test_with_prefix(self):
        result = normalize_locator("aoe2:normalized:L10-L20")
        assert result == "aoe2:normalized:L10-L20"

    def test_unrecognized_passthrough(self):
        assert normalize_locator("some-random-text") == "some-random-text"


class TestParseLocatorRange:
    """Tests for parse_locator_range()."""

    def test_simple_line(self):
        result = parse_locator_range("normalized:L42")
        assert result is not None
        assert result.start == 42
        assert result.end == 42

    def test_range(self):
        result = parse_locator_range("normalized:L10-L20")
        assert result is not None
        assert result.start == 10
        assert result.end == 20

    def test_shorthand(self):
        result = parse_locator_range("L5-10")
        assert result is not None
        assert result.start == 5
        assert result.end == 10

    def test_with_prefix(self):
        result = parse_locator_range("aoe2:normalized:L1-L5")
        assert result is not None
        assert result.start == 1
        assert result.end == 5
        assert "aoe2" in result.source

    def test_invalid(self):
        assert parse_locator_range("invalid") is None


class TestLocatorToRange:
    """Tests for locator_to_range()."""

    def test_returns_tuple(self):
        result = locator_to_range("normalized:L5-L10")
        assert result == (5, 10)

    def test_single_line(self):
        result = locator_to_range("L7")
        assert result == (7, 7)


class TestLocatorWithinRanges:
    """Tests for locator_within_ranges()."""

    def test_within_range(self):
        ranges = [SourceRange(start=10, end=50)]
        assert locator_within_ranges("normalized:L20-L30", ranges)

    def test_outside_range(self):
        ranges = [SourceRange(start=10, end=20)]
        assert not locator_within_ranges("normalized:L50", ranges)

    def test_partially_outside(self):
        ranges = [SourceRange(start=10, end=20)]
        # Start inside, end outside
        assert not locator_within_ranges("normalized:L15-L30", ranges)

    def test_multiple_ranges(self):
        ranges = [
            SourceRange(start=10, end=20),
            SourceRange(start=50, end=60),
        ]
        assert locator_within_ranges("normalized:L55", ranges)


class TestRangesOverlap:
    """Tests for ranges_overlap()."""

    def test_overlapping(self):
        a = SourceRange(start=10, end=20)
        b = SourceRange(start=15, end=25)
        assert ranges_overlap(a, b)

    def test_adjacent(self):
        a = SourceRange(start=10, end=20)
        b = SourceRange(start=20, end=30)
        assert ranges_overlap(a, b)

    def test_non_overlapping(self):
        a = SourceRange(start=10, end=20)
        b = SourceRange(start=30, end=40)
        assert not ranges_overlap(a, b)

    def test_different_sources(self):
        a = SourceRange(start=10, end=20, source="a")
        b = SourceRange(start=10, end=20, source="b")
        assert not ranges_overlap(a, b)


class TestMergeRanges:
    """Tests for merge_ranges()."""

    def test_empty(self):
        assert merge_ranges([]) == []

    def test_single(self):
        ranges = [SourceRange(start=10, end=20)]
        result = merge_ranges(ranges)
        assert len(result) == 1
        assert result[0].start == 10
        assert result[0].end == 20

    def test_overlapping_merge(self):
        ranges = [
            SourceRange(start=10, end=20),
            SourceRange(start=15, end=30),
        ]
        result = merge_ranges(ranges)
        assert len(result) == 1
        assert result[0].start == 10
        assert result[0].end == 30

    def test_adjacent_merge(self):
        ranges = [
            SourceRange(start=10, end=20),
            SourceRange(start=21, end=30),  # Adjacent
        ]
        result = merge_ranges(ranges)
        assert len(result) == 1

    def test_non_overlapping_preserved(self):
        ranges = [
            SourceRange(start=10, end=20),
            SourceRange(start=50, end=60),
        ]
        result = merge_ranges(ranges)
        assert len(result) == 2


class TestFormatLocator:
    """Tests for format_locator()."""

    def test_single_line(self):
        assert format_locator(42) == "normalized:L42"

    def test_range(self):
        assert format_locator(10, 20) == "normalized:L10-L20"

    def test_same_start_end(self):
        assert format_locator(10, 10) == "normalized:L10"

    def test_with_slug(self):
        assert format_locator(10, 20, slug="aoe2") == "aoe2:normalized:L10-L20"
