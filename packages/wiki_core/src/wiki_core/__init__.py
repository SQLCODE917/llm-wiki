"""wiki_core — Pure domain types and parsing for the wiki ingestion pipeline.

This package contains shared domain types and parsing utilities with no I/O
or LLM dependencies. All types are immutable or have explicit serialization.

Usage:
    from wiki_core.types import Claim, Locator, Frontmatter
    from wiki_core.types import parse_locator, normalize_locator
    
    from wiki_core.parsing import (
        strip_markdown,
        normalize_for_search,
        split_table_row,
        clean_evidence_excerpt,
    )
"""
from wiki_core.types import (
    # Claim types
    Claim,
    RawClaim,
    NormalizedClaim,
    SynthesisClaim,
    SourceClaim,
    generate_claim_id,
    normalize_claim_text,
    # Locator types
    Locator,
    parse_locator,
    normalize_locator,
    # Frontmatter types
    Frontmatter,
    ParsedFrontmatter,
    PageType,
    PageStatus,
)

__all__ = [
    # Claim types
    "Claim",
    "RawClaim",
    "NormalizedClaim",
    "SynthesisClaim",
    "SourceClaim",
    "generate_claim_id",
    "normalize_claim_text",
    # Locator types
    "Locator",
    "parse_locator",
    "normalize_locator",
    # Frontmatter types
    "Frontmatter",
    "ParsedFrontmatter",
    "PageType",
    "PageStatus",
]
