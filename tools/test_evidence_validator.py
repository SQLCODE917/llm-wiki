#!/usr/bin/env python3
"""Regression tests for evidence validation.

These tests ensure the evidence validator handles:
- Code snippets as valid evidence (programming books)
- Hyphenated PDF text (line breaks)
- Off-by-one locator mismatches
- Fabricated evidence detection
"""
import pytest

# Import from refactored packages
from wiki_io.evidence import (
    looks_like_code,
    validate_evidence_location,
    EvidenceValidationResult,
    normalize_for_search,
    is_evidence_too_short,
)


class TestLooksLikeCode:
    """Test code snippet detection."""

    def test_arrow_function_simple(self):
        assert looks_like_code("() => 0") is True

    def test_arrow_function_with_param(self):
        assert looks_like_code("x => x") is True

    def test_arrow_function_body(self):
        assert looks_like_code("(x) => x + 1") is True

    def test_function_declaration(self):
        assert looks_like_code("function () {}") is True

    def test_function_call(self):
        assert looks_like_code("foo.bar(baz)") is True

    def test_array_literal(self):
        assert looks_like_code("[1, 2, 3]") is True

    def test_object_literal(self):
        assert looks_like_code("{ a: 1 }") is True

    def test_conditional(self):
        assert looks_like_code("if (x) y()") is True

    def test_return_statement(self):
        assert looks_like_code("return x + 1") is True

    def test_repl_output(self):
        assert looks_like_code("//=> 42") is True

    def test_const_declaration(self):
        assert looks_like_code("const x = 5") is True

    def test_plain_prose_false(self):
        assert looks_like_code("hello world") is False

    def test_empty_string_false(self):
        assert looks_like_code("") is False

    def test_whitespace_only_false(self):
        assert looks_like_code("   ") is False


class TestNormalizeForSearch:
    """Test text normalization for matching."""

    def test_hyphenation_joined(self):
        """PDF hyphenation should be joined: indepen-\\ndent -> independent"""
        text = "Working with small, indepen-\ndent entities"
        assert "independent" in normalize_for_search(text)

    def test_hyphenation_with_space(self):
        """Hyphenation with space: indepen- dent -> independent"""
        text = "Working with small, indepen- dent entities"
        assert "independent" in normalize_for_search(text)

    def test_unicode_quotes_normalized(self):
        text = "\u201csmart quotes\u201d"
        assert '"smart quotes"' in normalize_for_search(text)

    def test_unicode_dashes_normalized(self):
        text = "en–dash and em—dash"
        normalized = normalize_for_search(text)
        assert "en-dash" in normalized
        assert "em-dash" in normalized

    def test_trailing_ellipsis_stripped(self):
        text = "truncated evidence..."
        assert normalize_for_search(text) == "truncated evidence"

    def test_trailing_punctuation_stripped(self):
        text = "ends with colon:"
        assert normalize_for_search(text) == "ends with colon"


class TestValidateEvidenceLocation:
    """Test evidence-in-locator validation."""

    def test_exact_match_passes(self):
        """Evidence found exactly in locator span."""
        evidence = "() => 0"
        source_lines = ["line 1", "() => 0", "line 3"]
        result = validate_evidence_location(evidence, 2, 2, source_lines)
        assert result.severity == "pass"
        assert result.result == "exact_match"

    def test_hyphenated_pdf_text_passes(self):
        """Hyphenated PDF text should match after normalization."""
        evidence = "Working with small, independent entities"
        source_lines = [
            "line 1",
            "Working with small, indepen-",
            "dent entities that compose",
            "line 4",
        ]
        result = validate_evidence_location(evidence, 2, 3, source_lines)
        assert result.severity == "pass"

    def test_off_by_one_locator_warns(self):
        """Off-by-one locator should warn, not fail."""
        evidence = "independent entities that compose together"
        source_lines = [
            "line 1",
            "JavaScript: It was written to describe certain ideas in programming: Working with small, indepen-",
            "dent entities that compose together to make bigger programs.",
            "line 4",
        ]
        # Locator points to line 2 but evidence is on lines 2-3
        result = validate_evidence_location(evidence, 2, 2, source_lines)
        # Should find in window and warn
        assert result.severity in ("pass", "warn")
        assert result.result in (
            "exact_match", "normalized_match", "window_match", "prefix_match")

    def test_fabricated_evidence_fails(self):
        """Evidence not found anywhere should fail."""
        evidence = "JavaScript was designed by Alan Turing in 1942"
        source_lines = [
            "JavaScript is a programming language",
            "created by Brendan Eich in 1995",
            "at Netscape Communications",
        ]
        result = validate_evidence_location(evidence, 1, 1, source_lines)
        assert result.severity == "fail"
        assert result.is_hard_failure is True

    def test_invalid_locator_fails(self):
        """Invalid locator range should fail."""
        source_lines = ["line 1", "line 2"]
        result = validate_evidence_location("anything", 3, 5, source_lines)
        assert result.severity == "fail"
        assert result.is_hard_failure is True

    def test_evidence_elsewhere_warns(self):
        """Evidence found elsewhere in source should warn with suggested locator."""
        evidence = "correct evidence text"
        source_lines = [
            "line 1",
            "wrong content here",
            "correct evidence text here",
            "line 4",
        ]
        # Locator points to wrong place
        result = validate_evidence_location(evidence, 2, 2, source_lines)
        assert result.severity == "warn"
        assert result.result == "source_match"
        assert result.suggested_locator is not None


class TestIsEvidenceTooShort:
    """Test evidence length validation."""

    def test_code_snippet_not_too_short(self):
        """Code snippets should not be rejected for being short."""
        assert is_evidence_too_short("() => 0") is False

    def test_short_prose_is_too_short(self):
        """Short prose without code signals should be flagged."""
        assert is_evidence_too_short("hi") is True

    def test_longer_prose_ok(self):
        """Longer prose should pass."""
        assert is_evidence_too_short(
            "This is a longer piece of evidence text") is False

    def test_short_code_with_keywords_ok(self):
        """Short text with code keywords should pass."""
        assert is_evidence_too_short("return x") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
