"""Evidence handling for wiki ingestion pipeline.

This module provides tools for:
- Resolving evidence IDs to source excerpts
- Validating evidence against source locators
- Parsing and manipulating source ranges
- Evidence bank utilities for synthesis prompts

Example:
    from wiki_io.evidence import (
        EvidenceResolver, ResolvedEvidence,
        validate_evidence_location, canonicalize_for_evidence_match,
        SourceRange, parse_locator_range, normalize_locator,
        source_chunks, snippets_for_candidate,
    )
    
    # Resolution
    resolver = EvidenceResolver.for_slug("js-allonge")
    evidence = resolver.resolve("js-allonge:claim_test_c000_abc123")
    
    # Validation
    result = validate_evidence_location(
        evidence="Some text from source",
        locator_start=12,
        locator_end=15,
        source_lines=source_lines,
    )
    if not result.passes:
        print(f"Evidence validation failed: {result.reason}")
    
    # Range parsing
    range_obj = parse_locator_range("normalized:L12-L34")
    if range_obj:
        print(f"Lines {range_obj.start} to {range_obj.end}")
    
    # Evidence bank
    chunks = source_chunks(source_text)
    snippets = snippets_for_candidate("aoe2-economy", chunks, limit=8)
"""
from wiki_io.evidence.resolver import (
    EvidenceResolver,
    ResolvedEvidence,
    stable_evidence_id,
    bracketed_evidence_id,
    evidence_id_aliases,
    extract_evidence_ids,
    EVIDENCE_ID_RE,
    LOCATOR_RE,
)

from wiki_io.evidence.validator import (
    validate_evidence_location,
    canonicalize_for_evidence_match,
    looks_like_code,
    EvidenceValidationResult,
    EvidenceLocationResult,
    MatchConfidence,
    HARD_FAIL_REASONS,
    normalize_for_search,
    is_evidence_too_short,
    should_fail_on_deterministic_flag,
    is_weak_evidence,
    WEAK_EVIDENCE_PATTERNS,
)

from wiki_io.evidence.ranges import (
    SourceRange,
    SourceRangeResult,
    SourceHeading,
    normalize_locator,
    parse_locator_range,
    locator_to_range,
    locator_within_ranges,
    locator_within_tolerance,
    ranges_overlap,
    merge_ranges,
    format_locator,
    format_ranges,
    format_range,
    source_ranges_for_page,
    source_ranges_for_candidate,
    declared_source_ranges,
    parse_source_range,
    canonicalize_locator,
    page_aliases,
    strip_domain_prefix,
    derive_ranges_from_headings,
    source_headings,
    clean_heading_title,
    canonical_key,
    RANGE_RE,
    SIMPLE_LINE_RE,
    HEADING_RE,
    MAX_LOCATOR_SLOP,
)

from wiki_io.evidence.bank import (
    SourceChunk,
    source_chunks,
    snippets_for_candidate,
    candidate_tokens,
    evidence_tokens,
    split_sentences,
    trim_chunk,
    render_evidence_bank,
    WEAK_SNIPPET_PATTERNS,
)


__all__ = [
    # Resolver
    "EvidenceResolver",
    "ResolvedEvidence",
    "stable_evidence_id",
    "bracketed_evidence_id",
    "evidence_id_aliases",
    "extract_evidence_ids",
    "EVIDENCE_ID_RE",
    "LOCATOR_RE",
    # Validator
    "validate_evidence_location",
    "canonicalize_for_evidence_match",
    "looks_like_code",
    "EvidenceValidationResult",
    "EvidenceLocationResult",
    "MatchConfidence",
    "HARD_FAIL_REASONS",
    "normalize_for_search",
    "is_evidence_too_short",
    "should_fail_on_deterministic_flag",
    "is_weak_evidence",
    "WEAK_EVIDENCE_PATTERNS",
    # Ranges
    "SourceRange",
    "SourceRangeResult",
    "SourceHeading",
    "normalize_locator",
    "parse_locator_range",
    "locator_to_range",
    "locator_within_ranges",
    "locator_within_tolerance",
    "ranges_overlap",
    "merge_ranges",
    "format_locator",
    "format_ranges",
    "format_range",
    "source_ranges_for_page",
    "source_ranges_for_candidate",
    "declared_source_ranges",
    "parse_source_range",
    "canonicalize_locator",
    "page_aliases",
    "strip_domain_prefix",
    "derive_ranges_from_headings",
    "source_headings",
    "clean_heading_title",
    "canonical_key",
    "RANGE_RE",
    "SIMPLE_LINE_RE",
    "HEADING_RE",
    "MAX_LOCATOR_SLOP",
    # Bank
    "SourceChunk",
    "source_chunks",
    "snippets_for_candidate",
    "candidate_tokens",
    "evidence_tokens",
    "split_sentences",
    "trim_chunk",
    "render_evidence_bank",
    "WEAK_SNIPPET_PATTERNS",
]
