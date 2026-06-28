"""Materialize technical-atom payloads from a source segment.

Each builder preserves the exact source text and adds logical structure only
when reusable structural parsing succeeds. When parsing partially or fully
fails, the raw text is still preserved and a ``ReviewReason`` is attached — an
atom is never dropped because its structure could not be modeled.
"""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import (
    CodeBlockPayload,
    FigurePayload,
    FormulaPayload,
    ProcedurePayload,
    RulePayload,
    WorkedExamplePayload,
)
from llmwiki.domain.ledger.common import ReviewReason
from llmwiki.domain.ledger.notation import formula_candidate_line, is_symbolic_formula
from llmwiki.domain.ledger.rule_structure import materialize_rule_payload
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.table_materialize import materialize_table as materialize_table
from llmwiki.domain.prose_flow import structural_incompleteness_reason

_FENCE = re.compile(r"^[ \t]*(```|~~~)[ \t]*([A-Za-z0-9_+-]*)[ \t]*$")
_STEP = re.compile(
    r"^\s*(?:\d+[.)]\s|[-*]\s*\d+[.)\s]|step\b|then\b|next\b|finally\b)", re.IGNORECASE
)
_EXAMPLE = re.compile(
    r"\bfor example\b|\bexample[:.]|\be\.g\.|\bsuppose\b|\bconsider\b", re.IGNORECASE
)
_SENTENCE = re.compile(r"(?<=[.!?])\s+")


def materialize_code_block(segment: SourceSegment) -> tuple[CodeBlockPayload, str] | None:
    block = _fenced_block(segment.text)
    if block is None:
        return None
    raw_code_text, language_tag = block
    return (
        CodeBlockPayload(
            raw_code_text=raw_code_text,
            parse_status="parsed",
            source_locator=segment.source_locator,
            language_tag=language_tag,
            language_detected=False,
            code_fence="```",
            line_count=raw_code_text.count("\n") + 1 if raw_code_text else 0,
            surrounding_explanation_locator=segment.source_range_id,
        ),
        "parsed",
    )


def materialize_formula(segment: SourceSegment) -> FormulaPayload | None:
    line = formula_candidate_line(segment.text)
    if line is None:
        return None
    has_equation = "=" in line
    symbolic = is_symbolic_formula(line)
    return FormulaPayload(
        raw_formula_text=line.strip(),
        formula_subtype="symbolic-formula" if symbolic else "procedural-formula",
        formula_surface_form="equation" if has_equation else "prose",
        source_locator=segment.source_locator,
        notation_context_locator=segment.source_range_id,
    )


def materialize_figure(segment: SourceSegment) -> FigurePayload | None:
    if segment.segment_kind != "figure":
        return None
    return FigurePayload(
        raw_figure_text=segment.text.strip(),
        parse_status="unparsed",
        source_locator=segment.source_locator,
        figure_locator=segment.source_range_id,
    )


def materialize_rule(segment: SourceSegment) -> tuple[RulePayload, ReviewReason | None] | None:
    for sentence in _sentences(segment.text):
        payload = materialize_rule_payload(sentence, segment.source_locator)
        if payload is not None:
            reason = structural_incompleteness_reason(sentence)
            review = ReviewReason("fragmentary", reason, segment.evidence_ids) if reason else None
            return payload, review
    return None


def materialize_procedure(segment: SourceSegment) -> ProcedurePayload | None:
    steps = tuple(line.strip() for line in segment.text.splitlines() if _STEP.match(line))
    if len(steps) < 2:
        return None
    return ProcedurePayload(segment.text, segment.source_locator, steps=steps)


def materialize_worked_example(segment: SourceSegment) -> WorkedExamplePayload | None:
    if not _EXAMPLE.search(segment.text):
        return None
    return WorkedExamplePayload(segment.text, segment.source_locator)


# -- helpers ---------------------------------------------------------------


def _fenced_block(text: str) -> tuple[str, str] | None:
    lines = text.splitlines()
    opening: int | None = None
    language = ""
    for index, line in enumerate(lines):
        match = _FENCE.match(line)
        if match is None:
            continue
        if opening is None:
            opening = index
            language = match.group(2)
            continue
        body = "\n".join(lines[opening + 1 : index])
        return (body, language) if body.strip() else None
    return None


def _sentences(text: str) -> list[str]:
    flat = " ".join(text.split())
    return [s for s in _SENTENCE.split(flat) if len(s.split()) >= 3]
