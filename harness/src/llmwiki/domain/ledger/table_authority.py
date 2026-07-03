"""Authority decisions for competing table atom representations."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TablePayload, TechnicalAtom
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.table_identity import normalize_table_name, raw_table_caption_lines


@dataclass(frozen=True)
class TableAuthorityDecision:
    table_candidate_id: str
    status: str
    canonical_atom_id: str
    variant_atom_ids: tuple[str, ...]
    diagnostics: tuple[str, ...] = ()


def table_authority_decisions(
    atoms: tuple[TechnicalAtom, ...],
) -> tuple[TableAuthorityDecision, ...]:
    groups: dict[str, list[TechnicalAtom]] = {}
    for atom in atoms:
        if atom.technical_atom_kind != "table" or not isinstance(atom.payload, TablePayload):
            continue
        groups.setdefault(_candidate_key(atom), []).append(atom)
    decisions: list[TableAuthorityDecision] = []
    for key, variants in groups.items():
        ordered = tuple(sorted(variants, key=_variant_sort_key))
        canonical = ordered[0]
        diagnostics = _diagnostics(ordered)
        status = "accepted" if not diagnostics else "needs-review"
        decisions.append(
            TableAuthorityDecision(
                table_candidate_id=deterministic_id("table-candidate", key),
                status=status,
                canonical_atom_id=canonical.technical_atom_id,
                variant_atom_ids=tuple(atom.technical_atom_id for atom in ordered),
                diagnostics=diagnostics,
            )
        )
    return tuple(sorted(decisions, key=lambda item: item.table_candidate_id))


def accepted_table_atom_ids(atoms: tuple[TechnicalAtom, ...]) -> frozenset[str]:
    return frozenset(
        decision.canonical_atom_id for decision in table_authority_decisions(atoms)
    )


def table_decision_by_atom_id(
    atoms: tuple[TechnicalAtom, ...],
) -> dict[str, TableAuthorityDecision]:
    result: dict[str, TableAuthorityDecision] = {}
    for decision in table_authority_decisions(atoms):
        for atom_id in decision.variant_atom_ids:
            result[atom_id] = decision
    return result


def _candidate_key(atom: TechnicalAtom) -> str:
    payload = atom.payload
    assert isinstance(payload, TablePayload)
    names = [payload.caption, *raw_table_caption_lines(payload)]
    normalized_name = next((name for raw in names if (name := normalize_table_name(raw))), "")
    return "|".join(
        (
            atom.source_locator,
            atom.source_range_id,
            normalized_name,
            _raw_fingerprint_basis(payload.raw_table_text),
        )
    )


def _variant_sort_key(atom: TechnicalAtom) -> tuple[int, int, str]:
    payload = atom.payload
    assert isinstance(payload, TablePayload)
    status_rank = {"parsed": 0, "partially-parsed": 1, "unparsed": 2}
    cell_count = len(payload.cells)
    return (status_rank.get(payload.parse_status, 9), -cell_count, atom.technical_atom_id)


def _diagnostics(variants: tuple[TechnicalAtom, ...]) -> tuple[str, ...]:
    if len(variants) <= 1:
        return ()
    parse_statuses = {
        atom.payload.parse_status
        for atom in variants
        if isinstance(atom.payload, TablePayload)
    }
    if len(parse_statuses) > 1:
        return ("competing table variants use different parse statuses",)
    return ("duplicate table variants share the same source range",)


def _raw_fingerprint_basis(raw: str) -> str:
    return " ".join(raw.split())[:160]
