"""Topic candidate records and section-derived candidate builders."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.topic_terms import source_label_terms


@dataclass(frozen=True)
class TopicCandidate:
    topic_key: str
    label: str
    terms: tuple[str, ...]
    evidence_kind: str
    from_heading: bool = False
    structure_node_id: str = ""
    evidence_entry_ids: tuple[str, ...] = ()
    evidence_atom_ids: tuple[str, ...] = ()


def section_candidates(section_plan: SectionGroundedPlan | None) -> list[TopicCandidate]:
    if section_plan is None:
        return []
    return [
        TopicCandidate(
            topic_key=target.topic_key,
            label=target.label,
            terms=tuple(source_label_terms(target.label)),
            evidence_kind="section",
            from_heading=True,
            structure_node_id=target.structure_node_id,
            evidence_entry_ids=target.entry_ids,
            evidence_atom_ids=target.atom_ids,
        )
        for target in section_plan.page_targets
        if target.topic_key
    ]


def section_component_candidates(
    section_plan: SectionGroundedPlan | None,
) -> list[TopicCandidate]:
    if section_plan is None:
        return []
    grouped: dict[str, tuple[str, list[str], list[str]]] = {}
    for target in section_plan.page_targets:
        for key in target.concept_keys:
            label, entry_ids, atom_ids = grouped.get(key, (_label_for_key(key), [], []))
            entry_ids.extend(target.entry_ids)
            atom_ids.extend(target.atom_ids)
            grouped[key] = (label, entry_ids, atom_ids)
    return [
        TopicCandidate(
            topic_key=key,
            label=label,
            terms=tuple(key.split("-")),
            evidence_kind="section-component",
            from_heading=True,
            evidence_entry_ids=tuple(dict.fromkeys(entry_ids)),
            evidence_atom_ids=tuple(dict.fromkeys(atom_ids)),
        )
        for key, (label, entry_ids, atom_ids) in grouped.items()
    ]


def repeated_section_candidates(section_plan: SectionGroundedPlan | None) -> list[TopicCandidate]:
    if section_plan is None:
        return []
    grouped: dict[str, tuple[str, list[str], list[str], int]] = {}
    for target in section_plan.page_targets:
        if not target.topic_key:
            continue
        label, entry_ids, atom_ids, count = grouped.get(target.topic_key, (target.label, [], [], 0))
        entry_ids.extend(target.entry_ids)
        atom_ids.extend(target.atom_ids)
        grouped[target.topic_key] = (label, entry_ids, atom_ids, count + 1)
    return [
        TopicCandidate(
            topic_key=key,
            label=label,
            terms=tuple(key.split("-")),
            evidence_kind="section-repeat",
            from_heading=True,
            evidence_entry_ids=tuple(dict.fromkeys(entry_ids)),
            evidence_atom_ids=tuple(dict.fromkeys(atom_ids)),
        )
        for key, (label, entry_ids, atom_ids, count) in grouped.items()
        if count > 1 and len(key.split("-")) > 1 and (entry_ids or atom_ids)
    ]


def _label_for_key(key: str) -> str:
    return " ".join(part.title() for part in key.split("-"))
