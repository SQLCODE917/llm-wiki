"""Bounded existing-page text for ingest planning similarity checks."""

from __future__ import annotations

PAGE_MATCH_TEXT_CHAR_LIMIT = 6_000
GENERATED_MATCH_SECTION_HEADINGS = (
    "\n## Technical details",
    "\n## Related technical details",
    "\n## Page-Map Navigation",
)


def page_match_text(page_text: str) -> str:
    bounded = page_text
    for heading in GENERATED_MATCH_SECTION_HEADINGS:
        bounded = bounded.split(heading, 1)[0]
    return bounded[:PAGE_MATCH_TEXT_CHAR_LIMIT]
