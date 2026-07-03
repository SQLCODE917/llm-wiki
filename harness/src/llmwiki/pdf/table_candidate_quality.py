"""Source-neutral quality checks for recovered table candidates."""

from __future__ import annotations

import re

_TOKEN = re.compile(r"[a-z0-9]+", re.IGNORECASE)
_ROW_MARKER = re.compile(r"^\s*\d{1,3}(?:[-–]\d{1,3})?\b", re.MULTILINE)
_PUNCT_ONLY_LINE = re.compile(r"^\s*[\W_]+\s*$", re.MULTILINE)
_SPACED_PAREN = re.compile(r"\(\s+|\s+\)")
_SPACE_BEFORE_PUNCT = re.compile(r"\s+[,.!?;:]")


def table_extraction_artifact_score(text: str) -> int:
    """Higher means the text looks more like a damaged extraction artifact."""
    return (
        len(_PUNCT_ONLY_LINE.findall(text)) * 4
        + len(_SPACED_PAREN.findall(text)) * 2
        + len(_SPACE_BEFORE_PUNCT.findall(text))
    )


def recovered_table_supersedes(candidate_text: str, existing_text: str) -> bool:
    if _token_overlap(candidate_text, existing_text) < 0.35:
        return False
    if _row_marker_count(candidate_text) < max(2, int(_row_marker_count(existing_text) * 0.75)):
        return False
    candidate_score = table_extraction_artifact_score(candidate_text)
    existing_score = table_extraction_artifact_score(existing_text)
    return candidate_score + 2 < existing_score


def _token_overlap(left: str, right: str) -> float:
    left_tokens = set(_TOKEN.findall(left.lower()))
    right_tokens = set(_TOKEN.findall(right.lower()))
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / min(len(left_tokens), len(right_tokens))


def _row_marker_count(text: str) -> int:
    return len(_ROW_MARKER.findall(text))
