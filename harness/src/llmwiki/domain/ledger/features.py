"""Source-neutral feature-signal detectors.

Each detector measures a reusable property of an extracted unit — table-like
layout, code-like syntax, formula notation, entity/date density, deontic rule
language, ordered-procedure shape, definition patterns, or relationship cues.
Detectors use linguistic, layout, syntactic, and notation categories that apply
to any source. Cue words contribute weak features; they never name a source,
book, author, character, API, or game term, and never accept an atom by
themselves.
"""

from __future__ import annotations

import re
from collections.abc import Callable

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.extraction import ExtractedUnitProfile, FeatureSignal
from llmwiki.domain.ledger.notation import is_formula_line
from llmwiki.domain.ledger.tabular import row_marker_count

_CODE_FENCE = re.compile(r"^\s*(```|~~~)")
# Tokens that are rare in natural-language prose. Bare words like "class",
# "return", or punctuation like ";"/"{}" appear in ordinary prose, so they are
# excluded to keep code-density from firing on narrative text.
_CODE_TOKEN = re.compile(
    r"=>|::=|:=|==|!=|\bfunc\s|\bfunction\s|\bdef\s|\bconst\s|\blet\s|\bvar\s"
    r"|\bimport\s|\bpackage\s|\)\s*\{|;\s*$|\}\s*$"
)
_YEAR = re.compile(r"\b\d{3,4}\b|\bBCE?\b|\bAD\b|\bcentur\w+\b")
_PROPER = re.compile(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3}\b")
_DEONTIC = re.compile(
    r"\b(must|shall|should|may|cannot|can not|required|prohibited|forbidden|permitted"
    r"|allowed|except|if|unless|when|whenever|always|never)\b",
    re.IGNORECASE,
)
_STEP = re.compile(
    r"^\s*(?:\d+[.)]\s|[-*]\s*\d+\s|step\b|then\b|next\b|finally\b|first\b)", re.IGNORECASE
)
_DEFINITION = re.compile(
    r"\b(is|are)\s+(a|an|the)\b|\bdefined as\b|\bmeans\b|\brefers to\b|\bis called\b",
    re.IGNORECASE,
)
_RELATION = re.compile(
    r"\b(because|therefore|thus|hence|after|before|while|during|between|located|within"
    r"|contains|caused|leads to|results in|compared|unlike|whereas)\b",
    re.IGNORECASE,
)
_TABLE_PIPE = re.compile(r"\|.*\|")
_SPACED_COLUMN = re.compile(r"\S.*?\s{2,}\S")
_FIGURE_PLACEHOLDER = re.compile(r"^\s*\[Figure\b", re.IGNORECASE)
_MAX_PROFILE_LINES = 5_000
_MAX_PROFILE_LINE_CHARS = 2_000


def profile_unit(
    *,
    extracted_unit_id: str,
    source_range_id: str,
    text: str,
    evidence_ids: tuple[str, ...],
) -> ExtractedUnitProfile:
    """Measure every feature signal kind for one extracted unit."""
    lines = _profile_lines(text)
    profile_text = "\n".join(lines)
    denom = max(len(lines), 1)
    measures = {
        "table-density": _table_density(lines, denom),
        "code-density": _code_density(profile_text, lines, denom),
        "formula-density": _fraction(lines, denom, is_formula_line),
        "figure-density": 1.0 if _FIGURE_PLACEHOLDER.search(profile_text) else 0.0,
        "entity-date-density": _entity_date_density(profile_text),
        "rule-language-density": _fraction(lines, denom, _DEONTIC.search),
        "procedure-density": _fraction(lines, denom, _STEP.match),
        "definition-density": _fraction(lines, denom, _DEFINITION.search),
        "relationship-density": _fraction(lines, denom, _RELATION.search),
    }
    signals = tuple(
        FeatureSignal(
            feature_signal_id=deterministic_id("feature-signal", source_range_id, kind),
            feature_signal_kind=kind,
            feature_signal_value=round(value, 4),
            feature_signal_confidence=_confidence(value),
            source_range_id=source_range_id,
            evidence_ids=evidence_ids,
        )
        for kind, value in measures.items()
    )
    return ExtractedUnitProfile(
        extracted_unit_id=extracted_unit_id,
        source_range_id=source_range_id,
        feature_signals=signals,
    )


def _profile_lines(text: str) -> list[str]:
    return [
        line[:_MAX_PROFILE_LINE_CHARS]
        for line in text.splitlines()[:_MAX_PROFILE_LINES]
        if line.strip()
    ]


def _fraction(lines: list[str], denom: int, predicate: Callable[[str], object]) -> float:
    hits = sum(1 for line in lines if predicate(line))
    return min(hits / denom, 1.0)


def _table_density(lines: list[str], denom: int) -> float:
    # Tab runs are layout whitespace in many extractors, so they are not a
    # reliable table signal. Pipe rows, aligned space-separated columns, and
    # runs of enumerated rows are.
    pipe = sum(1 for line in lines if _TABLE_PIPE.search(line))
    spaced = sum(1 for line in lines if _SPACED_COLUMN.search(line))
    sequence_run = row_marker_count("\n".join(lines))
    return min((pipe * 2 + spaced + sequence_run) / denom, 1.0)


def _code_density(text: str, lines: list[str], denom: int) -> float:
    if _CODE_FENCE.search(text):
        fenced = sum(1 for line in lines if _CODE_FENCE.search(line))
        if fenced:
            return min(0.6 + fenced / denom, 1.0)
    token_lines = sum(1 for line in lines if _CODE_TOKEN.search(line))
    indented = sum(1 for line in lines if line.startswith(("    ", "\t")) and line.strip())
    return min((token_lines + indented * 0.5) / denom, 1.0)


def _entity_date_density(text: str) -> float:
    years = len(_YEAR.findall(text))
    propers = len(_PROPER.findall(text))
    words = max(len(text.split()), 1)
    return min((years * 3 + propers) / words, 1.0)


def _confidence(value: float) -> str:
    if value >= 0.5:
        return "high"
    if value >= 0.15:
        return "medium"
    return "low"
