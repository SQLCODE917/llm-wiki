"""Tests for wiki_io.evidence.validator module."""
import pytest
from wiki_io.evidence.validator import (
    canonicalize_for_evidence_match,
    looks_like_code,
    validate_evidence_location,
)


class TestCanonicalize:
    """Tests for canonicalize_for_evidence_match()."""

    def test_basic_normalization(self):
        result = canonicalize_for_evidence_match("  Hello   World  ")
        assert result == "hello world"

    def test_unicode_dashes(self):
        # Unicode dashes are normalized to ASCII dash, then intra-word hyphens removed
        text = "en–dash and em—dash"
        result = canonicalize_for_evidence_match(text)
        # The dashes were replaced with "-", then intra-word hyphens removed
        assert "endash" in result
        assert "emdash" in result
        assert "–" not in result
        assert "—" not in result

    def test_smart_quotes(self):
        text = '\u201cHello\u201d and \u2018world\u2019'
        result = canonicalize_for_evidence_match(text)
        assert "\u2019" not in result
        assert "\u201c" not in result

    def test_line_wrap_hyphenation(self):
        text = "hyphen-\nated"
        result = canonicalize_for_evidence_match(text)
        assert "hyphenated" in result

    def test_page_break_removal(self):
        text = "Line one\n---\n<!-- page 42 -->\nLine two"
        result = canonicalize_for_evidence_match(text)
        assert "page" not in result
        assert "---" not in result

    def test_enclosing_quotes_stripped(self):
        result = canonicalize_for_evidence_match('"quoted text"')
        assert result == "quoted text"

    def test_intra_word_hyphens_removed(self):
        result = canonicalize_for_evidence_match("age-of-empires")
        assert result == "ageofempires"


class TestLooksLikeCode:
    """Tests for looks_like_code()."""

    def test_arrow_function(self):
        assert looks_like_code("const f = x => x + 1")

    def test_function_keyword(self):
        assert looks_like_code("function foo() {}")

    def test_brackets(self):
        assert looks_like_code("{ key: value }")

    def test_plain_text(self):
        assert not looks_like_code("The quick brown fox")

    def test_empty(self):
        assert not looks_like_code("")


class TestValidateEvidenceLocation:
    """Tests for validate_evidence_location()."""

    @pytest.fixture
    def source_lines(self):
        return [
            "Line 1 with some text",
            "Line 2 with more text",
            "Line 3: Evidence is here",
            "Line 4 continues",
            "Line 5 ends",
        ]

    def test_exact_match(self, source_lines):
        result = validate_evidence_location(
            "Evidence is here",
            locator_start=3,
            locator_end=3,
            source_lines=source_lines,
        )
        assert result.result == "exact_match"
        assert result.severity == "pass"
        assert result.confidence == "exact"

    def test_canonicalized_match(self, source_lines):
        result = validate_evidence_location(
            "EVIDENCE   IS   HERE",  # Different whitespace/case
            locator_start=3,
            locator_end=3,
            source_lines=source_lines,
        )
        assert result.result == "canonicalized_local"
        assert result.severity == "pass"

    def test_window_match(self, source_lines):
        # Search for line 3 text but cite line 4
        result = validate_evidence_location(
            "Evidence is here",
            locator_start=4,
            locator_end=4,
            source_lines=source_lines,
            window_size=2,
        )
        assert result.result == "canonicalized_window"
        assert result.severity == "warn"

    def test_global_match(self, source_lines):
        # Search for line 1 text but cite line 5
        result = validate_evidence_location(
            "Line 1 with some text",
            locator_start=5,
            locator_end=5,
            source_lines=source_lines,
        )
        assert result.result == "canonicalized_global"
        assert result.severity == "warn"

    def test_not_found(self, source_lines):
        result = validate_evidence_location(
            "This text is not in the source",
            locator_start=1,
            locator_end=5,
            source_lines=source_lines,
        )
        assert result.result == "not_found"
        assert result.severity == "fail"
        assert result.is_hard_failure

    def test_invalid_locator(self, source_lines):
        result = validate_evidence_location(
            "Text",
            locator_start=0,  # Invalid: 1-indexed
            locator_end=1,
            source_lines=source_lines,
        )
        assert result.is_hard_failure
        assert result.reason == "invalid_locator"

    def test_locator_out_of_bounds(self, source_lines):
        result = validate_evidence_location(
            "Text",
            locator_start=1,
            locator_end=100,  # Beyond source length
            source_lines=source_lines,
        )
        assert result.is_hard_failure
        assert result.reason == "locator_outside_source"
