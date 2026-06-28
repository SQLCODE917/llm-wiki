"""Evidence-backed walkability checks for generated related-page links."""

from __future__ import annotations

from dataclasses import dataclass, replace

from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.coverage import clean_statement
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink

_STRUCTURAL_RELATIONS = frozenset(
    {
        "broader source section",
        "narrower source section",
        "topic hub",
        "same source heading",
    }
)
_EXCERPT_LIMIT = 180


@dataclass(frozen=True)
class RelationSupport:
    entries: tuple[LedgerEntry, ...]
    atoms: tuple[TechnicalAtom, ...]
    structural_relation: bool = False

    @property
    def is_supported(self) -> bool:
        return bool(self.entries or self.atoms or self.structural_relation)


@dataclass(frozen=True)
class WalkabilityFinding:
    page_id: str
    target_page_id: str
    finding_type: str
    message: str


@dataclass(frozen=True)
class WalkabilityReport:
    page_id: str
    accepted_links: tuple[RelatedTopicLink, ...]
    rejected_links: tuple[RelatedTopicLink, ...]
    findings: tuple[WalkabilityFinding, ...]

    @property
    def accepted_count(self) -> int:
        return len(self.accepted_links)

    @property
    def rejected_count(self) -> int:
        return len(self.rejected_links)

    def render_summary(self) -> str:
        return (
            f"Walkability: {self.accepted_count} accepted link(s), "
            f"{self.rejected_count} rejected link(s) for [[{self.page_id}]]."
        )


def audit_related_links(
    page_id: str,
    links: tuple[RelatedTopicLink, ...],
    ledger: ClaimLedger,
    *,
    projection_context: ProjectionContext | None = None,
) -> WalkabilityReport:
    """Resolve planned related links against source support before rendering."""
    accepted: list[RelatedTopicLink] = []
    rejected: list[RelatedTopicLink] = []
    findings: list[WalkabilityFinding] = []
    for link in links:
        support, missing = _relation_support(link, ledger)
        if missing:
            rejected.append(link)
            findings.append(
                WalkabilityFinding(
                    page_id,
                    link.page_id,
                    "missing-support",
                    f"Related link references missing support id(s): {', '.join(missing)}.",
                )
            )
            continue
        if not support.is_supported:
            rejected.append(link)
            findings.append(
                WalkabilityFinding(
                    page_id,
                    link.page_id,
                    "unsupported-link",
                    "Related link has no shared evidence or source-structure relation.",
                )
            )
            continue
        explanation = explain_relation(link, support, projection_context)
        accepted.append(replace(link, explanation=explanation))
    return WalkabilityReport(page_id, tuple(accepted), tuple(rejected), tuple(findings))


def related_link_markdown(link: RelatedTopicLink) -> str:
    detail = link.relation
    if link.explanation:
        detail = f"{detail}: {link.explanation}"
    return f"- [[{link.page_id}]] - {detail}{_evidence_note(link)}"


def explain_relation(
    link: RelatedTopicLink,
    support: RelationSupport,
    projection_context: ProjectionContext | None,
) -> str:
    parts: list[str] = []
    if support.entries:
        parts.append(_entry_explanation(link, support.entries, projection_context))
    if support.atoms:
        parts.append(_atom_explanation(link, support.atoms, projection_context))
    if parts:
        return "; ".join(part for part in parts if part)
    return _structural_explanation(link)


def _relation_support(
    link: RelatedTopicLink, ledger: ClaimLedger
) -> tuple[RelationSupport, tuple[str, ...]]:
    entries: list[LedgerEntry] = []
    atoms: list[TechnicalAtom] = []
    missing: list[str] = []
    for entry_id in link.shared_entry_ids:
        entry = ledger.entry(entry_id)
        if entry is None:
            missing.append(entry_id)
        else:
            entries.append(entry)
    for atom_id in link.shared_atom_ids:
        atom = ledger.atom(atom_id)
        if atom is None:
            missing.append(atom_id)
        else:
            atoms.append(atom)
    structural = link.relation in _STRUCTURAL_RELATIONS and not link.shared_entry_ids
    return RelationSupport(tuple(entries), tuple(atoms), structural), tuple(missing)


def _entry_explanation(
    link: RelatedTopicLink,
    entries: tuple[LedgerEntry, ...],
    projection_context: ProjectionContext | None,
) -> str:
    entry_ids = tuple(entry.ledger_entry_id for entry in entries)
    if projection_context is not None:
        blocks = projection_context.blocks_for_entries(entry_ids)
        if blocks:
            block = blocks[0]
            section = f" from {block.section_label}" if block.section_label else ""
            return (
                f"{_target_label(link)} shares source evidence{section}: "
                f"{_excerpt(block.source_text)}"
            )
    text = entries[0].normalized_text or entries[0].source_text
    return f"{_target_label(link)} shares source evidence: {_excerpt(text)}"


def _atom_explanation(
    link: RelatedTopicLink,
    atoms: tuple[TechnicalAtom, ...],
    projection_context: ProjectionContext | None,
) -> str:
    atom_ids = tuple(atom.technical_atom_id for atom in atoms)
    if projection_context is not None:
        frames = projection_context.frames_for_atoms(atom_ids)
        if frames:
            frame = frames[0]
            return (
                f"{_target_label(link)} shares technical record from {frame.label}: "
                f"{_atom_excerpt(atoms[0])}"
            )
    return (
        f"{_target_label(link)} shares technical {atoms[0].technical_atom_kind}: "
        f"{_atom_excerpt(atoms[0])}"
    )


def _structural_explanation(link: RelatedTopicLink) -> str:
    label = _target_label(link)
    if link.relation == "topic hub":
        return f"opens the topic page for {label}"
    if link.relation == "same source heading":
        return f"another source section with the same heading, {label}"
    return label


def _target_label(link: RelatedTopicLink) -> str:
    return link.label.strip() or link.page_id


def _atom_excerpt(atom: TechnicalAtom) -> str:
    return _excerpt(atom_raw_text(atom.payload))


def _excerpt(text: str) -> str:
    cleaned = clean_statement(" ".join(line.strip() for line in text.splitlines()).strip())
    if len(cleaned) <= _EXCERPT_LIMIT:
        return cleaned
    return cleaned[: _EXCERPT_LIMIT - 15].rstrip() + " ... [truncated]"


def _evidence_note(link: RelatedTopicLink) -> str:
    parts: list[str] = []
    if link.shared_entry_count:
        parts.append(f"{link.shared_entry_count} shared statement(s)")
    if link.shared_atom_count:
        parts.append(f"{link.shared_atom_count} shared atom(s)")
    return f" ({', '.join(parts)})" if parts else ""
