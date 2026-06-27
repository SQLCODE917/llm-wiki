"""PDF table candidate records."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TableCandidate:
    caption: str
    page_start: int
    page_end: int
    y0: float
    raw_text: str
    extractor_stage: str
    anchor_text: str = ""
    insert_after_anchor: bool = False
