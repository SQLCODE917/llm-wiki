"""Projection Context system.

Projection Context sits between the Claim Ledger and page renderers. It keeps
ledger evidence atomic for audit while giving renderers coherent source
passages and technical records to display.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atom_frames import TechnicalAtomFrame, build_atom_frames
from llmwiki.domain.ledger.evidence_blocks import EvidenceBlock, build_evidence_blocks
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.structure import DocumentStructure


@dataclass(frozen=True)
class ProjectionContext:
    evidence_blocks: tuple[EvidenceBlock, ...]
    atom_frames: tuple[TechnicalAtomFrame, ...]

    def evidence_block(self, block_id: str) -> EvidenceBlock | None:
        return next(
            (block for block in self.evidence_blocks if block.evidence_block_id == block_id),
            None,
        )

    def blocks_for_entries(self, entry_ids: tuple[str, ...]) -> tuple[EvidenceBlock, ...]:
        wanted = set(entry_ids)
        return tuple(
            block for block in self.evidence_blocks if wanted.intersection(block.entry_ids)
        )

    def frames_for_atoms(self, atom_ids: tuple[str, ...]) -> tuple[TechnicalAtomFrame, ...]:
        wanted = set(atom_ids)
        return tuple(frame for frame in self.atom_frames if wanted.intersection(frame.atom_ids))


def build_projection_context(
    ledger: ClaimLedger, structure: DocumentStructure
) -> ProjectionContext:
    evidence_blocks = build_evidence_blocks(ledger, structure)
    atom_frames = build_atom_frames(ledger, structure, evidence_blocks)
    return ProjectionContext(evidence_blocks, atom_frames)
