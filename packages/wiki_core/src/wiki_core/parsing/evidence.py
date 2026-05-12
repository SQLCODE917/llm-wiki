"""Evidence text processing utilities.

Pure text transformations for cleaning and normalizing evidence excerpts.
No I/O or external dependencies.

Usage:
    from wiki_core.parsing import clean_evidence_excerpt
    
    # Clean up evidence text
    clean = clean_evidence_excerpt('"quoted text"')  # "quoted text"
"""
from __future__ import annotations


def clean_evidence_excerpt(text: str) -> str:
    """Clean an evidence excerpt for comparison.

    Performs the following normalizations:
    - Strip leading/trailing whitespace
    - Unescape quotes (\\" -> ")
    - Remove surrounding quotes (single or double)
    - Collapse whitespace

    This is useful for comparing evidence excerpts that may have been
    quoted differently in different contexts.

    Args:
        text: Raw evidence excerpt

    Returns:
        Cleaned excerpt with quotes and whitespace normalized

    Examples:
        >>> clean_evidence_excerpt('"quoted text"')
        'quoted text'
        >>> clean_evidence_excerpt("'single quoted'")
        'single quoted'
        >>> clean_evidence_excerpt('  extra   spaces  ')
        'extra spaces'
    """
    cleaned = text.strip().replace('\\"', '"')

    # Remove surrounding quotes (may be nested)
    while (
        (cleaned.startswith('"') and cleaned.endswith('"')) or
        (cleaned.startswith("'") and cleaned.endswith("'"))
    ):
        cleaned = cleaned[1:-1].strip()

    # Collapse whitespace
    return " ".join(cleaned.split())
