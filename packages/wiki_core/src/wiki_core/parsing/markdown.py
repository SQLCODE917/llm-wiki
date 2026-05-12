"""Markdown text processing utilities.

Pure text transformations for normalizing and cleaning Markdown content.
No I/O or external dependencies.

Usage:
    from wiki_core.parsing import strip_markdown, normalize_for_search
    
    # Remove markdown formatting
    plain = strip_markdown("**bold** and [link](url)")  # "bold and link"
    
    # Normalize for fuzzy matching
    normalized = normalize_for_search("Some  Text")  # "some text"
"""
from __future__ import annotations

import re


def strip_markdown(text: str) -> str:
    """Remove Markdown formatting from text.

    Handles:
    - Links: [text](url) -> text
    - Inline code: `code` -> code
    - Bold/italic: **bold**, *italic*, _italic_ -> text

    Args:
        text: Markdown-formatted text

    Returns:
        Plain text with formatting removed
    """
    # Remove link syntax, keeping link text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Remove backticks, asterisks, underscores
    return text.replace("`", "").replace("*", "").replace("_", "")


# Unicode character replacements for normalize_for_search
_UNICODE_REPLACEMENTS = {
    "\u00a0": " ",   # Non-breaking space
    "\u2010": "-",   # Hyphen
    "\u2011": "-",   # Non-breaking hyphen
    "\u2012": "-",   # Figure dash
    "\u2013": "-",   # En dash
    "\u2014": "-",   # Em dash
    "\u2015": "-",   # Horizontal bar
    "\u2018": "'",   # Left single quote
    "\u2019": "'",   # Right single quote
    "\u201c": '"',   # Left double quote
    "\u201d": '"',   # Right double quote
    "\u2026": "...",  # Ellipsis
}


def normalize_for_search(text: str) -> str:
    """Normalize text for fuzzy matching.

    Performs multiple normalizations to improve matching between
    source text and extracted/paraphrased evidence:

    - Unicode normalization (dashes, quotes to ASCII)
    - PDF line-break hyphenation (subprob-\\nlems -> subproblems)
    - Parenthetical phrases removed (model may paraphrase without them)
    - Trailing ellipsis stripped (from truncated excerpts)
    - Trailing punctuation stripped (model may change colon to period)
    - Whitespace collapsed
    - Lowercased

    Args:
        text: Raw text to normalize

    Returns:
        Normalized lowercase text suitable for fuzzy matching

    Examples:
        >>> normalize_for_search("The quick—brown fox")
        'the quick-brown fox'
        >>> normalize_for_search("subprob-\\nlems")
        'subproblems'
        >>> normalize_for_search("expression (including typing) to create")
        'expression to create'
    """
    # Replace Unicode characters with ASCII equivalents
    for old, new in _UNICODE_REPLACEMENTS.items():
        text = text.replace(old, new)

    # Join PDF line-break hyphenation: subprob-\nlems -> subproblems
    # Also handles subprob- lems (space after hyphen)
    text = re.sub(r"([A-Za-z])-\s*\n?\s*([a-z])", r"\1\2", text)

    # Remove parenthetical phrases - model may quote without parentheticals
    # E.g., "expression (including typing) to create" -> "expression to create"
    text = re.sub(r'\s*\([^)]*\)\s*', ' ', text)

    # Strip trailing ellipsis from truncated evidence
    # Evidence bank truncates long excerpts with "..."
    text = re.sub(r'\.{3,}$', '', text)
    text = re.sub(r'\.{3,}\s*$', '', text)

    # Strip trailing punctuation for flexible matching
    # Model may change colon to period when extracting evidence
    text = re.sub(r'[.:;,!?]+$', '', text)

    return " ".join(text.lower().split())
