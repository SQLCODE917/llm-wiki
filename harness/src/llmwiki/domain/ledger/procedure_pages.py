"""Render procedure guide pages from procedure domain objects."""

from __future__ import annotations

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
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
) -> tuple[WikiPage, ...]:
    guides = plan_procedure_guides(ledger, structure, source_page_id=source_page_id)
    pages: list[WikiPage] = []
    for guide in guides:
        body = render_procedure_page(guide, source_page_id)
        metadata = PageMetadata(
            page_id=guide.procedure_id,
            page_kind="procedure",
            page_family=PAGE_FAMILY_PROCEDURE_GUIDE,
            summary=(
                f"{guide.goal}: {len(guide.steps)} ordered step(s), "
                f"{len(guide.decision_points)} decision point(s), and "
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
    shown_claim_keys: set[tuple[str, str]] = set()
    for step in guide.steps:
        lines.append(
            f"{step.sequence}. **{step.title}** (`{step.action_type}`) - "
            f"evidence section [[{step.section_page_id}]]."
        )
        for claim in step.claims[:_MAX_STEP_CLAIMS]:
            shown_claim_keys.add(_entry_key(claim))
            lines.append(f"   - {_entry_text(claim)} _({_citation(claim)})_")
    lines.append("")
    decision_points = tuple(
        point for point in guide.decision_points if _entry_key(point.entry) not in shown_claim_keys
    )
    if decision_points:
        lines.extend(("## Decision Points", ""))
        for point in decision_points[:8]:
            lines.append(f"- {_decision_text(point)} _({_citation(point.entry)})_")
        lines.append("")
    if guide.technical_atoms:
        lines.extend(("## Tables And Formulas", ""))
        for atom in guide.technical_atoms[:12]:
            lines.append(
                f"- `{atom.technical_atom_kind}`: {atom_label(atom)} _({_atom_citation(atom)})_"
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
    return _entry_text(point.entry)


def _entry_key(entry: LedgerEntry) -> tuple[str, str]:
    return (entry.source_range_id, _entry_text(entry))


def _citation(entry: LedgerEntry) -> str:
    return f"{entry.source_locator} ({entry.source_range_id})"


def _atom_citation(atom: TechnicalAtom) -> str:
    return f"{atom.source_locator} ({atom.source_range_id})"
