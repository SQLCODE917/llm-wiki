"""Section-grounded page planning.

Authored source sections are the primary signal for page targets. Claims,
tables, code blocks, formulas, rules, and examples attach to those targets as
evidence; they do not become pages merely because they are rows or snippets.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.atom_projection import atom_is_topic_projectable
from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.canonical import content_fingerprint, deterministic_id
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_substance import entry_is_unresolved_context_pointer
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.table_identity import (
    has_matching_table_name,
    normalize_table_name,
    table_identity_names_by_atom_id,
)
from llmwiki.domain.ledger.topic_entry_index import (
    TopicEntryIndex,
    entry_is_concept_or_definition,
    topic_entry_index,
    topic_entry_index_strongly_supports_topic,
    topic_entry_index_supports_topic,
)
from llmwiki.domain.ledger.topic_terms import (
    required_topic_terms,
    source_label_terms,
    topic_matcher,
    topic_term_role,
)

_SECTION_NODE_KINDS = {"chapter", "section", "heading"}
_HEADING_NUMBER = re.compile(
    r"^(?:chapter|part|section|appendix|book)\s+[\dIVXLC]+\s*[-:.]?\s*", re.IGNORECASE
)
_GENERIC_TABLE_CUE = re.compile(
    r"\b(?:table below|following table|roll on the table|table above)\b", re.IGNORECASE
)
_COORDINATED_LABEL_SPLIT = re.compile(r"\s+(?:and|or)\s+|/+", re.IGNORECASE)


@dataclass(frozen=True)
class AttachedEvidence:
    evidence_kind: str
    evidence_role: str
    ledger_entry_id: str = ""
    technical_atom_id: str = ""


@dataclass(frozen=True)
class SectionEvidenceBundle:
    structure_node_id: str
    heading_text: str
    topic_key: str
    label: str
    entry_ids: tuple[str, ...]
    atom_ids: tuple[str, ...]


@dataclass(frozen=True)
class PageTarget:
    page_target_id: str
    topic_key: str
    label: str
    page_kind: str
    structure_node_id: str
    source_range_id: str
    concept_keys: tuple[str, ...]
    entry_ids: tuple[str, ...]
    atom_ids: tuple[str, ...]
    attached_evidence: tuple[AttachedEvidence, ...]


@dataclass(frozen=True)
class SourceCoverageMapEntry:
    structure_node_id: str
    page_target_ids: tuple[str, ...]
    ledger_entry_ids: tuple[str, ...]
    technical_atom_ids: tuple[str, ...]


@dataclass(frozen=True)
class SectionGroundedPlan:
    section_grounded_plan_id: str
    section_grounded_plan_fingerprint: str
    source_locator: str
    source_hash: str
    page_targets: tuple[PageTarget, ...]
    source_coverage_map: tuple[SourceCoverageMapEntry, ...]


@dataclass(frozen=True)
class SectionPlanningContext:
    table_names_by_atom_id: dict[str, tuple[str, ...]]
    entry_indexes_by_node: dict[str, tuple[TopicEntryIndex, ...]]


def build_section_grounded_plan(
    ledger: ClaimLedger, structure: DocumentStructure
) -> SectionGroundedPlan:
    context = SectionPlanningContext(
        table_names_by_atom_id=table_identity_names_by_atom_id(ledger, structure),
        entry_indexes_by_node=_entry_indexes_by_node(ledger),
    )
    targets: list[PageTarget] = []
    for node in _section_nodes(structure):
        target = _target_for_node(ledger, structure, context, node)
        if target is not None:
            targets.append(target)
    target_tuple = tuple(targets)
    coverage = tuple(
        SourceCoverageMapEntry(
            target.structure_node_id,
            (target.page_target_id,),
            target.entry_ids,
            target.atom_ids,
        )
        for target in targets
    )
    fingerprint = content_fingerprint(
        (ledger.source_locator, ledger.source_hash, target_tuple, coverage)
    )
    return SectionGroundedPlan(
        section_grounded_plan_id=deterministic_id(
            "section-grounded-plan", ledger.source_hash, fingerprint
        ),
        section_grounded_plan_fingerprint=fingerprint,
        source_locator=ledger.source_locator,
        source_hash=ledger.source_hash,
        page_targets=target_tuple,
        source_coverage_map=coverage,
    )


def section_bundle_for_target(target: PageTarget) -> SectionEvidenceBundle:
    return SectionEvidenceBundle(
        structure_node_id=target.structure_node_id,
        heading_text=target.label,
        topic_key=target.topic_key,
        label=target.label,
        entry_ids=target.entry_ids,
        atom_ids=target.atom_ids,
    )


def _section_nodes(structure: DocumentStructure) -> tuple[StructureNode, ...]:
    return tuple(
        node
        for node in sorted(structure.structure_nodes, key=lambda item: item.source_order)
        if node.structure_node_kind in _SECTION_NODE_KINDS
    )


def _target_for_node(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    context: SectionPlanningContext,
    node: StructureNode,
) -> PageTarget | None:
    label = _clean_heading(node.heading_text)
    if not label or _generic_heading(label):
        return None
    terms = tuple(source_label_terms(label))
    if not terms or len(terms) > 8:
        return None
    matcher = topic_matcher(terms)
    if matcher is None:
        return None
    entry_indexes = context.entry_indexes_by_node.get(node.structure_node_id, ())
    entries = tuple(index.entry for index in entry_indexes)
    atoms = _atoms_for_node(ledger, context, node)
    atom_ids = tuple(atom.technical_atom_id for atom in atoms)
    accepted = _heading_topic_accepted(
        terms,
        entry_indexes,
        atom_ids,
        matcher,
        required_topic_terms(terms),
    )
    if not accepted:
        return None
    topic_key = "-".join(terms)
    attached = tuple(evidence for entry in entries for evidence in _entry_evidence(entry)) + tuple(
        _atom_evidence(atom) for atom in atoms
    )
    target_id = deterministic_id(
        "page-target", ledger.source_hash, node.structure_node_id, topic_key
    )
    return PageTarget(
        page_target_id=target_id,
        topic_key=topic_key,
        label=label,
        page_kind="concept",
        structure_node_id=node.structure_node_id,
        source_range_id=node.source_range_id,
        concept_keys=_component_topic_keys(label, topic_key),
        entry_ids=tuple(entry.ledger_entry_id for entry in entries),
        atom_ids=tuple(atom.technical_atom_id for atom in atoms),
        attached_evidence=attached,
    )


def _clean_heading(text: str) -> str:
    return _HEADING_NUMBER.sub("", text).strip()


def _generic_heading(text: str) -> bool:
    lowered = text.lower()
    return bool(_GENERIC_TABLE_CUE.search(lowered)) or lowered.endswith(".pdf")


def _component_topic_keys(label: str, topic_key: str) -> tuple[str, ...]:
    parts = [part.strip() for part in _COORDINATED_LABEL_SPLIT.split(label) if part.strip()]
    if len(parts) < 2:
        return ()
    keys: list[str] = []
    for part in parts:
        terms = tuple(source_label_terms(part))
        if not terms:
            continue
        if len(terms) == 1 and topic_term_role(terms[0]) != "domain":
            continue
        key = "-".join(terms)
        if key and key != topic_key:
            keys.append(key)
    return tuple(dict.fromkeys(keys))


def _entry_indexes_by_node(ledger: ClaimLedger) -> dict[str, tuple[TopicEntryIndex, ...]]:
    grouped: dict[str, list[TopicEntryIndex]] = {}
    for entry in ledger.usable_entries:
        if entry.ledger_entry_kind not in ("claim", "event", "concept"):
            continue
        if len((entry.normalized_text or entry.source_text).split()) > 45:
            continue
        index = topic_entry_index(entry)
        for node_id in entry.structure_node_ids:
            grouped.setdefault(node_id, []).append(index)
    return {node_id: tuple(indexes) for node_id, indexes in grouped.items()}


def _heading_topic_accepted(
    terms: tuple[str, ...],
    entry_indexes: tuple[TopicEntryIndex, ...],
    atom_ids: tuple[str, ...],
    matcher: re.Pattern[str],
    required_terms: tuple[str, ...],
) -> bool:
    evidence = tuple(
        index
        for index in entry_indexes
        if topic_entry_index_supports_topic(index, matcher, terms, required_terms)
    )
    strong = tuple(
        index
        for index in evidence
        if topic_entry_index_strongly_supports_topic(index, matcher, terms, required_terms)
    )
    concept = tuple(index for index in evidence if entry_is_concept_or_definition(index.entry))
    if not evidence and not atom_ids:
        return False
    if (
        entry_indexes
        and not atom_ids
        and all(entry_is_unresolved_context_pointer(index.entry) for index in entry_indexes)
    ):
        return False
    return not (_all_container_terms(terms) and not (concept or len(strong) >= 2 or atom_ids))


def _all_container_terms(terms: tuple[str, ...]) -> bool:
    return all(
        topic_term_role(term) in ("discourse-container", "structural-container") for term in terms
    )


def _atoms_for_node(
    ledger: ClaimLedger, context: SectionPlanningContext, node: StructureNode
) -> tuple[TechnicalAtom, ...]:
    atom_ids = {
        entry.technical_atom_id
        for entry in ledger.usable_entries
        if entry.ledger_entry_kind == "technical-atom"
        and entry.technical_atom_id
        and node.structure_node_id in entry.structure_node_ids
    }
    section_name = normalize_table_name(node.heading_text)
    if section_name:
        for atom_id, names in context.table_names_by_atom_id.items():
            if has_matching_table_name(section_name, names):
                atom_ids.add(atom_id)
    return tuple(
        atom
        for atom in ledger.technical_atoms
        if atom.technical_atom_id in atom_ids
        and atom_raw_text(atom.payload).strip()
        and atom_is_topic_projectable(atom, ledger.source_profile)
    )


def _entry_evidence(entry: LedgerEntry) -> tuple[AttachedEvidence, ...]:
    return (
        AttachedEvidence(
            evidence_kind="ledger-entry",
            evidence_role=_entry_role(entry),
            ledger_entry_id=entry.ledger_entry_id,
        ),
    )


def _entry_role(entry: LedgerEntry) -> str:
    if entry.ledger_entry_kind == "concept" or "definition" in entry.claim_role_tags:
        return "definition"
    if entry.ledger_entry_kind == "event" or entry.temporal_scope is not None:
        return "event"
    text = f"{entry.normalized_text} {entry.object_value}".lower()
    if any(cue in text for cue in ("because", "therefore", "caused", "results in")):
        return "cause-effect"
    if entry.claim_force in {"required", "forbidden", "permitted"}:
        return "rule"
    if any(tag in entry.claim_role_tags for tag in ("example", "procedure")):
        return "example"
    return "property"


def _atom_evidence(atom: TechnicalAtom) -> AttachedEvidence:
    return AttachedEvidence(
        evidence_kind="technical-atom",
        evidence_role=_atom_role(atom),
        technical_atom_id=atom.technical_atom_id,
    )


def _atom_role(atom: TechnicalAtom) -> str:
    if atom.technical_atom_kind == "table":
        return "structured-table"
    if atom.technical_atom_kind == "code-block":
        return "example"
    if atom.technical_atom_kind == "formula":
        return "formula"
    if atom.technical_atom_kind == "procedure":
        return "procedure"
    if atom.technical_atom_kind == "rule":
        return "rule"
    if atom.technical_atom_kind == "worked-example":
        return "example"
    return "technical-atom"
