"""Evidence handling for wiki ingestion pipeline.

This module provides tools for:
- Resolving evidence IDs to source excerpts
- Validating evidence against source locators
- Parsing and manipulating source ranges

Example:
    from wiki_io.evidence import (
        EvidenceResolver, ResolvedEvidence,
        validate_evidence_location, canonicalize_for_evidence_match,
        SourceRange, parse_locator_range, normalize_locator,
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
)

from wiki_io.evidence.ranges import (
    SourceRange,
    normalize_locator,
    parse_locator_range,
    locator_to_range,
    locator_within_ranges,
    ranges_overlap,
    merge_ranges,
    format_locator,
    RANGE_RE,
    SIMPLE_LINE_RE,
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
    # Ranges
    "SourceRange",
    "normalize_locator",
    "parse_locator_range",
    "locator_to_range",
    "locator_within_ranges",
    "ranges_overlap",
    "merge_ranges",
    "format_locator",
    "RANGE_RE",
    "SIMPLE_LINE_RE",
]
