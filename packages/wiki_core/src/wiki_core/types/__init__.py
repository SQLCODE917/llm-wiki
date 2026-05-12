"""Domain types for the wiki ingestion pipeline."""
from wiki_core.types.claim import (
    Claim,
    RawClaim,
    NormalizedClaim,
    SynthesisClaim,
    SourceClaim,
    generate_claim_id,
    normalize_claim_text,
)
from wiki_core.types.locator import (
    Locator,
    parse_locator,
    normalize_locator,
)
from wiki_core.types.frontmatter import (
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
