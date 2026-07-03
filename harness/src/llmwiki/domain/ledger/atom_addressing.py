"""Stable wiki addresses for rendered technical atoms."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom

_ANCHOR_SAFE = re.compile(r"[^a-z0-9-]+")


@dataclass(frozen=True)
class TechnicalAtomAddress:
    source_locator: str
    technical_atom_id: str
    technical_atom_kind: str
    source_range_id: str
    anchor_id: str


def technical_atom_address(atom: TechnicalAtom) -> TechnicalAtomAddress:
    return TechnicalAtomAddress(
        source_locator=atom.source_locator,
        technical_atom_id=atom.technical_atom_id,
        technical_atom_kind=atom.technical_atom_kind,
        source_range_id=atom.source_range_id,
        anchor_id=technical_atom_anchor_id(atom.technical_atom_id),
    )


def technical_atom_anchor_id(atom_id: str) -> str:
    cleaned = _ANCHOR_SAFE.sub("-", atom_id.lower()).strip("-")
    return f"atom-{cleaned or 'technical-atom'}"


def technical_atom_anchor(atom_id: str) -> str:
    return f'<a id="{technical_atom_anchor_id(atom_id)}"></a>'


def technical_atom_link(page_id: str, atom: TechnicalAtom, label: str) -> str:
    anchor = technical_atom_anchor_id(atom.technical_atom_id)
    return f"[[{page_id}]]#{anchor} {label}".strip()
