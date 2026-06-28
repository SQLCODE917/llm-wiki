"""Markdown helpers for Projection Context records."""

from __future__ import annotations

from llmwiki.domain.ledger.atom_frames import TechnicalAtomFrame
from llmwiki.domain.ledger.coverage import clean_statement
from llmwiki.domain.ledger.evidence_blocks import EvidenceBlock
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.renderer import atom_block


def evidence_block_line(block: EvidenceBlock) -> str:
    citation = f"{block.source_locator} ({block.source_range_id})"
    return f"- {clean_statement(block.source_text)} _({citation})_"


def atom_frame_markdown(
    frame: TechnicalAtomFrame,
    ledger: ClaimLedger,
    projection_context: ProjectionContext,
    index: int,
) -> str:
    lines = [f"### Technical frame {index}: {frame.label}", ""]
    context = projection_context.evidence_block(frame.context_block_id)
    if context is not None:
        lines.extend(
            (
                f"**Context:** _({context.source_locator} ({context.source_range_id}))_",
                "",
                f"> {clean_statement(context.source_text)[:500]}",
                "",
            )
        )
    label = "Atoms" if len(frame.atom_ids) > 1 else "Atom"
    citation = f"{frame.source_locator} ({', '.join(frame.source_range_ids)})"
    lines.extend((f"**{label}:** _({citation})_", ""))
    for atom_id in frame.atom_ids:
        atom = ledger.atom(atom_id)
        if atom is None:
            continue
        lines.extend((atom_block(atom.technical_atom_kind, atom.payload), ""))
    return "\n".join(lines).strip() + "\n"
