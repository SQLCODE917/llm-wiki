"""Preserved source technical detail objects and rendering."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from llmwiki.domain.technical_atom_detection import (
    MAX_TECHNICAL_PAYLOAD_CHARS,
    SUPPORT_STATUSES,
    TECHNICAL_ATOM_KINDS,
    SupportStatus,
    TechnicalAtomKind,
)


@dataclass(frozen=True)
class TechnicalAtom:
    technical_atom_id: str
    source_locator: str
    page_id: str
    atom_kind: TechnicalAtomKind
    title: str
    technical_payload: str
    normalized_fields: tuple[tuple[str, str], ...]
    source_claim_ids: tuple[str, ...]
    evidence_ids: tuple[str, ...]
    source_range_id: str
    support_status: SupportStatus = "supported"

    def __post_init__(self) -> None:
        if self.atom_kind not in TECHNICAL_ATOM_KINDS:
            raise ValueError(f"Unknown TechnicalAtomKind: {self.atom_kind!r}.")
        if self.support_status not in SUPPORT_STATUSES:
            raise ValueError(f"Unknown support_status: {self.support_status!r}.")
        if not self.source_locator or not self.page_id or not self.source_range_id:
            raise ValueError("TechnicalAtom requires source, page, and source range.")
        if not self.evidence_ids:
            raise ValueError("TechnicalAtom requires at least one evidence id.")
        if not self.technical_payload.strip():
            raise ValueError("TechnicalAtom requires a technical payload.")
        if len(self.technical_payload) > MAX_TECHNICAL_PAYLOAD_CHARS:
            raise ValueError("TechnicalAtom technical_payload exceeds bounded size.")
        if "```" in self.technical_payload:
            raise ValueError("TechnicalAtom payload must not include Markdown fences.")

    @property
    def source_citation(self) -> str:
        return dict(self.normalized_fields).get("source_citation", f"raw/{self.source_locator}")


@dataclass(frozen=True)
class TechnicalAtomCatalog:
    catalog_id: str
    source_locator: str
    artifact_fingerprint: str
    technical_atoms: tuple[TechnicalAtom, ...]

    def atoms_for_page(self, page_id: str) -> tuple[TechnicalAtom, ...]:
        return tuple(atom for atom in self.technical_atoms if atom.page_id == page_id)

    def counts_by_kind(self) -> tuple[tuple[str, int], ...]:
        counts = Counter(atom.atom_kind for atom in self.technical_atoms)
        return tuple((kind, counts[kind]) for kind in sorted(counts))


_RENDER_KIND_PRIORITY = {
    "code": 0,
    "formula": 1,
    "procedure": 2,
    "requirement": 3,
    "exception": 4,
    "worked-example": 5,
    "table-row": 6,
}


def render_technical_details_section(catalog: TechnicalAtomCatalog, page_id: str) -> str:
    atoms = _render_order(catalog.atoms_for_page(page_id))
    if not atoms:
        return ""
    return "\n\n".join(("## Technical details", *(_render_atom(atom) for atom in atoms)))


def _render_order(atoms: tuple[TechnicalAtom, ...]) -> tuple[TechnicalAtom, ...]:
    ordered = sorted(
        enumerate(atoms),
        key=lambda item: (_RENDER_KIND_PRIORITY.get(item[1].atom_kind, 99), item[0]),
    )
    return tuple(atom for _index, atom in ordered)


def _render_atom(atom: TechnicalAtom) -> str:
    header = f"### `{atom.technical_atom_id}` {atom.atom_kind}"
    citation = f"Citation: ({atom.source_citation})"
    if atom.atom_kind == "code":
        language = dict(atom.normalized_fields).get("language", "")
        return f"{header}\n\n{citation}\n\n```{language}\n{atom.technical_payload}\n```"
    return f"{header}\n\n{citation}\n\n{atom.technical_payload}"
