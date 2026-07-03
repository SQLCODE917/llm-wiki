"""Normalize table cell text without changing raw source preservation."""

from __future__ import annotations

import re

_SPACE_BEFORE_PUNCT = re.compile(r"\s+([,.;:!?])")
_SPACE_AFTER_OPEN = re.compile(r"([([{])\s+")
_SPACE_BEFORE_CLOSE = re.compile(r"\s+([])}])")
_MULTISPACE = re.compile(r"\s+")


def normalize_table_cell_text(text: str) -> str:
    normalized = _MULTISPACE.sub(" ", text.replace("\t", " ")).strip()
    normalized = _SPACE_AFTER_OPEN.sub(r"\1", normalized)
    normalized = _SPACE_BEFORE_CLOSE.sub(r"\1", normalized)
    normalized = _SPACE_BEFORE_PUNCT.sub(r"\1", normalized)
    return normalized
