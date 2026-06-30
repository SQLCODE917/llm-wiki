"""Context relationships for technical atoms.

A technical atom preserves structured source material. A context relationship
explains why that atom belongs with nearby source claims or a topic page.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.topic_terms import content_terms, topic_field_matches

_CONTEXT_KINDS = {"paragraph", "list"}
_INTRO = re.compile(
    r":\s*$|\b(?:for example|for instance|e\.g\.|such as|following|as follows|"
    r"consider|suppose|try|use|using|we can|can use|initialize|declare|"
    r"demonstrat\w*|calculate|determine|roll|choose|show\w*|list\w*|"
    r"specif\w*|describ\w*|defin\w*)\b",
    re.IGNORECASE,
)
_FOLLOW = re.compile(
    r"\b(?:above|output|result|answer|this example|this code|this table|"
    r"because|therefore|that means)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class TechnicalAtomContext:
    technical_atom_context_id: str
    technical_atom_id: str
    context_role: str
    context_text: str
    context_entry_ids: tuple[str, ...]
    context_source_range_ids: tuple[str, ...]
    demonstrated_concept_keys: tuple[str, ...]
    evidence_ids: tuple[str, ...]
    confidence_basis: ConfidenceBasis


def build_technical_atom_contexts(
    *,
    source_hash: str,
    segments: tuple[SourceSegment, ...],
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
) -> tuple[TechnicalAtomContext, ...]:
    by_range = {segment.source_range_id: segment for segment in segments}
    index_by_range = {segment.source_range_id: index for index, segment in enumerate(segments)}
    entry_ids_by_range = _entry_ids_by_range(entries)
    contexts: list[TechnicalAtomContext] = []
    for atom in atoms:
        segment = by_range.get(atom.source_range_id)
        segment_index = index_by_range.get(atom.source_range_id)
        if segment is None or segment_index is None:
            continue
        context_segments, role = _context_segments(segment_index, segments)
        if not context_segments:
            continue
        context_text = _context_text(context_segments)
        terms = tuple(content_terms(context_text))
        if not terms:
            continue
        range_ids = tuple(segment.source_range_id for segment in context_segments)
        context_id = deterministic_id(
            "technical-atom-context",
            source_hash,
            atom.technical_atom_id,
            role,
            "|".join(range_ids),
        )
        contexts.append(
            TechnicalAtomContext(
                technical_atom_context_id=context_id,
                technical_atom_id=atom.technical_atom_id,
                context_role=role,
                context_text=context_text,
                context_entry_ids=_collect(entry_ids_by_range, range_ids),
                context_source_range_ids=range_ids,
                demonstrated_concept_keys=terms,
                evidence_ids=tuple(eid for item in context_segments for eid in item.evidence_ids),
                confidence_basis=ConfidenceBasis("source-adjacent-atom-context"),
            )
        )
    return tuple(contexts)


def atom_context_matches(
    contexts: tuple[TechnicalAtomContext, ...],
    matcher: re.Pattern[str],
    terms: tuple[str, ...] = (),
    required_terms: tuple[str, ...] | None = None,
) -> bool:
    return any(
        topic_field_matches(context.context_text, matcher, terms, required_terms)
        or topic_field_matches(
            " ".join(context.demonstrated_concept_keys), matcher, terms, required_terms
        )
        for context in contexts
    )


def best_atom_context(
    contexts: tuple[TechnicalAtomContext, ...], matcher: re.Pattern[str] | None = None
) -> TechnicalAtomContext | None:
    if not contexts:
        return None
    if matcher is None:
        return contexts[0]
    return next(
        (context for context in contexts if atom_context_matches((context,), matcher)),
        contexts[0],
    )


def _context_segments(
    atom_index: int, segments: tuple[SourceSegment, ...]
) -> tuple[tuple[SourceSegment, ...], str]:
    previous = _previous_context_segments(segments, atom_index)
    following = _following_context_segments(segments, atom_index)
    selected = previous + following
    if previous and following:
        return (selected, "introduced-and-explained-by-source-prose")
    if previous:
        return (selected, "introduced-by-source-prose")
    if following:
        return (selected, "explained-by-source-prose")
    return ((), "")


def _previous_context_segments(
    segments: tuple[SourceSegment, ...], atom_index: int
) -> tuple[SourceSegment, ...]:
    selected: list[SourceSegment] = []
    heading_path = segments[atom_index].heading_path
    for segment in reversed(segments[max(0, atom_index - 3) : atom_index]):
        if segment.heading_path != heading_path:
            break
        if segment.segment_kind not in _CONTEXT_KINDS:
            continue
        if _INTRO.search(segment.text):
            selected.append(segment)
            break
    return tuple(reversed(selected))


def _following_context_segments(
    segments: tuple[SourceSegment, ...], atom_index: int
) -> tuple[SourceSegment, ...]:
    selected: list[SourceSegment] = []
    heading_path = segments[atom_index].heading_path
    for segment in segments[atom_index + 1 : atom_index + 3]:
        if segment.heading_path != heading_path:
            break
        if segment.segment_kind not in _CONTEXT_KINDS:
            continue
        if _FOLLOW.search(segment.text):
            selected.append(segment)
            break
    return tuple(selected)


def _context_text(segments: tuple[SourceSegment, ...]) -> str:
    return " ".join(_clean(segment.text) for segment in segments if segment.text.strip())


def _entry_ids_by_range(entries: tuple[LedgerEntry, ...]) -> dict[str, tuple[str, ...]]:
    mapped: dict[str, list[str]] = {}
    for entry in entries:
        if entry.ledger_entry_kind == "technical-atom":
            continue
        mapped.setdefault(entry.source_range_id, []).append(entry.ledger_entry_id)
    return {key: tuple(values) for key, values in mapped.items()}


def _collect(mapping: dict[str, tuple[str, ...]], range_ids: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(value for range_id in range_ids for value in mapping.get(range_id, ()))


def _clean(text: str) -> str:
    return " ".join(text.strip().split())
