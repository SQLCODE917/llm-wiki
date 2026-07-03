"""Render procedure guide pages from procedure domain objects."""

from __future__ import annotations

from llmwiki.domain.ledger.atom_addressing import technical_atom_link
from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.procedure_decisions import DecisionPoint
from llmwiki.domain.ledger.procedures import (
    PAGE_FAMILY_PROCEDURE_GUIDE,
    ProcedureGuide,
    atom_label,
    plan_procedure_guides,
    procedure_aliases,
)
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.pages import PageMetadata, WikiPage

_MAX_STEP_CLAIMS = 3


def build_procedure_pages(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    source_page_id: str,
    source_locator: str,
    today: str,
    shape_catalog: KnowledgeShapeCatalog | None = None,
) -> tuple[WikiPage, ...]:
    guides = plan_procedure_guides(
        ledger,
        structure,
        source_page_id=source_page_id,
        shape_catalog=shape_catalog,
    )
    pages: list[WikiPage] = []
    for guide in guides:
        body = render_procedure_page(guide, source_page_id)
        decision_point_count = len(_rendered_decision_points(guide))
        metadata = PageMetadata(
            page_id=guide.procedure_id,
            page_kind="procedure",
            page_family=PAGE_FAMILY_PROCEDURE_GUIDE,
            summary=(
                f"{guide.goal}: {len(guide.steps)} ordered step(s), "
                f"{decision_point_count} decision point(s), and "
                f"{len(guide.technical_atoms)} table/formula/example reference(s) "
                f"from raw/{source_locator}."
            ),
            sources=(f"raw/{source_locator}",),
            updated=today,
            domain=source_page_id,
            category_path=f"procedures/{source_page_id}",
            source_id=source_locator,
            aliases=procedure_aliases(guide),
            projection_coverage_pointer=f"procedure-{guide.procedure_id}@{short_digest(body, 32)}",
        )
        pages.append(WikiPage.from_metadata(metadata, body))
    return tuple(pages)


def render_procedure_page(guide: ProcedureGuide, source_page_id: str) -> str:
    lines = [f"# {guide.title}", "", f"From [[{source_page_id}]].", ""]
    lines.extend(("## Goal", "", f"- {guide.goal}.", ""))
    lines.extend(("## Procedure Steps", ""))
    for step in guide.steps:
        lines.append(
            f"{step.sequence}. **{step.title}** (`{step.action_type}`) - "
            f"evidence section [[{step.section_page_id}]]."
        )
        for claim in step.claims[:_MAX_STEP_CLAIMS]:
            lines.append(f"   - {_entry_text(claim)} _({_citation(claim)})_")
    lines.append("")
    decision_points = _rendered_decision_points(guide)
    if decision_points:
        lines.extend(("## Decision Points", ""))
        for point in decision_points[:8]:
            lines.append(f"- {_decision_text(point)} _({_decision_citation(point)})_")
        lines.append("")
    if guide.technical_atoms:
        lines.extend(("## Tables And Formulas", ""))
        for atom in guide.technical_atoms[:12]:
            target = technical_atom_link(guide.source_section_page_id, atom, atom_label(atom))
            lines.append(
                f"- `{atom.technical_atom_kind}`: {target} _({_atom_citation(atom)})_"
            )
        lines.append("")
    lines.extend(
        (
            "## Completion Check",
            "",
            "- The procedure is complete when every step output has been recorded or validated.",
            "",
            "## Source Trail",
            "",
            f"- Source manifest: [[{source_page_id}]]",
            f"- Source section: [[{guide.source_section_page_id}]]",
        )
    )
    return "\n".join(lines).strip() + "\n"


def _entry_text(entry: LedgerEntry) -> str:
    return (entry.normalized_text or entry.source_text).strip()


def _decision_text(point: DecisionPoint) -> str:
    return point.evidence_block.source_text


def _rendered_decision_points(guide: ProcedureGuide) -> tuple[DecisionPoint, ...]:
    shown_claim_keys = {
        _entry_key(claim) for step in guide.steps for claim in step.claims[:_MAX_STEP_CLAIMS]
    }
    supporting_context_range_ids = _supporting_context_range_ids(guide.decision_points)
    return tuple(
        point
        for point in guide.decision_points
        if _entry_key(point.entry) not in shown_claim_keys
        and point.entry.source_range_id not in supporting_context_range_ids
    )


def _supporting_context_range_ids(points: tuple[DecisionPoint, ...]) -> frozenset[str]:
    return frozenset(
        range_id
        for point in points
        for range_id in point.evidence_block.source_range_ids
        if range_id != point.entry.source_range_id
    )


def _entry_key(entry: LedgerEntry) -> tuple[str, str]:
    return (entry.source_range_id, _entry_text(entry))


def _decision_citation(point: DecisionPoint) -> str:
    ranges = ", ".join(point.evidence_block.source_range_ids)
    return f"{point.entry.source_locator} ({ranges})"


def _citation(entry: LedgerEntry) -> str:
    return f"{entry.source_locator} ({entry.source_range_id})"


def _atom_citation(atom: TechnicalAtom) -> str:
    return f"{atom.source_locator} ({atom.source_range_id})"
