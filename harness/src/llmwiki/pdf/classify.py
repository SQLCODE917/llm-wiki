"""Text-vs-scanned classification from per-page text-layer sizes.

A text PDF has a healthy text layer on most pages; a scanned PDF has
(near-)empty text on most pages. Median chars/page is robust against
covers, dividers, and a few image-only pages — the fixture has 34 such
pages and still classifies as TEXT.
"""

from __future__ import annotations

from enum import Enum
from statistics import median

# Awaiting experimentation across more sources (docs/open-questions.md):
# threshold chosen so the 297-page fixture (~1,150 chars/page median)
# classifies TEXT with a wide margin.
SCANNED_MEDIAN_CHARS_PER_PAGE = 200


class PdfKind(Enum):
    TEXT = "text"
    SCANNED = "scanned"


def classify_pdf(page_char_counts: list[int]) -> PdfKind:
    """Classify from the character count of each page's text layer."""
    if not page_char_counts:
        return PdfKind.SCANNED
    if median(page_char_counts) < SCANNED_MEDIAN_CHARS_PER_PAGE:
        return PdfKind.SCANNED
    return PdfKind.TEXT
