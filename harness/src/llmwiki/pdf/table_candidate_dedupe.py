"""Dedupe recovered PDF table candidates."""

from __future__ import annotations

import re

from llmwiki.pdf.document import DocumentModel
from llmwiki.pdf.table_candidate_model import TableCandidate


def dedupe_table_candidates(
    candidates: tuple[TableCandidate, ...], model: DocumentModel
) -> tuple[TableCandidate, ...]:
    existing_pages = {
        page
        for element in model.elements
        if element.element_kind == "table"
        for page in range(element.page_start, element.page_end + 1)
    }
    deduped: list[TableCandidate] = []
    seen: set[tuple[int, int, str]] = set()
    ordered = sorted(candidates, key=lambda item: _candidate_priority(item))
    for candidate in ordered:
        pages = range(candidate.page_start, candidate.page_end + 1)
        if any(page in existing_pages for page in pages):
            continue
        key = (candidate.page_start, candidate.page_end, " ".join(candidate.raw_text.split())[:120])
        if key in seen or any(_same_table_candidate(candidate, kept) for kept in deduped):
            continue
        seen.add(key)
        deduped.append(candidate)
    return tuple(deduped)


def _candidate_priority(candidate: TableCandidate) -> tuple[int, int]:
    layout_stage = candidate.extractor_stage in {"caption-layout", "forward-cue-layout"}
    return (0 if layout_stage else 1), -len(candidate.raw_text)


def _same_table_candidate(left: TableCandidate, right: TableCandidate) -> bool:
    if left.page_end < right.page_start or right.page_end < left.page_start:
        return False
    left_tokens = set(re.findall(r"[a-z0-9]+", left.raw_text.lower()))
    right_tokens = set(re.findall(r"[a-z0-9]+", right.raw_text.lower()))
    if not left_tokens or not right_tokens:
        return False
    overlap = len(left_tokens & right_tokens)
    return overlap / min(len(left_tokens), len(right_tokens)) >= 0.45
