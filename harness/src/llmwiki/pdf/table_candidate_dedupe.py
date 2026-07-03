"""Dedupe recovered PDF table candidates."""

from __future__ import annotations

import re

from llmwiki.pdf.document import DocumentModel
from llmwiki.pdf.table_candidate_model import TableCandidate
from llmwiki.pdf.table_candidate_quality import recovered_table_supersedes


def dedupe_table_candidates(
    candidates: tuple[TableCandidate, ...], model: DocumentModel
) -> tuple[TableCandidate, ...]:
    existing_tables = tuple(
        element for element in model.elements if element.element_kind == "table"
    )
    deduped: list[TableCandidate] = []
    seen: set[tuple[int, int, str]] = set()
    ordered = sorted(candidates, key=lambda item: _candidate_priority(item))
    for candidate in ordered:
        overlapping = tuple(
            element
            for element in existing_tables
            if not (
                element.page_end < candidate.page_start or candidate.page_end < element.page_start
            )
        )
        matching = tuple(
            element for element in overlapping if _same_table_text(candidate.raw_text, element.text)
        )
        if matching and not any(
            recovered_table_supersedes(candidate.raw_text, element.text) for element in matching
        ):
            continue
        key = (candidate.page_start, candidate.page_end, " ".join(candidate.raw_text.split())[:120])
        if key in seen or any(_same_table_candidate(candidate, kept) for kept in deduped):
            continue
        seen.add(key)
        deduped.append(candidate)
    return tuple(deduped)


def _candidate_priority(candidate: TableCandidate) -> tuple[int, int]:
    stage_rank = {
        "caption-layout": 0,
        "forward-cue-layout": 1,
        "heading-numbered-layout": 2,
    }.get(candidate.extractor_stage, 3)
    return stage_rank, -len(candidate.raw_text)


def _same_table_candidate(left: TableCandidate, right: TableCandidate) -> bool:
    if left.page_end < right.page_start or right.page_end < left.page_start:
        return False
    left_tokens = set(re.findall(r"[a-z0-9]+", left.raw_text.lower()))
    right_tokens = set(re.findall(r"[a-z0-9]+", right.raw_text.lower()))
    if not left_tokens or not right_tokens:
        return False
    overlap = len(left_tokens & right_tokens)
    return overlap / min(len(left_tokens), len(right_tokens)) >= 0.45


def _same_table_text(left: str, right: str) -> bool:
    left_tokens = set(re.findall(r"[a-z0-9]+", left.lower()))
    right_tokens = set(re.findall(r"[a-z0-9]+", right.lower()))
    if not left_tokens or not right_tokens:
        return False
    if max(len(left_tokens), len(right_tokens)) > min(len(left_tokens), len(right_tokens)) * 2:
        return False
    overlap = len(left_tokens & right_tokens)
    return overlap / min(len(left_tokens), len(right_tokens)) >= 0.45
