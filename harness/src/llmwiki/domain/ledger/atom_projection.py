"""Projection eligibility for technical atoms on topic pages."""

from __future__ import annotations

from llmwiki.domain.ledger.atoms import (
    ProcedurePayload,
    RulePayload,
    TechnicalAtom,
    WorkedExamplePayload,
)
from llmwiki.domain.ledger.ledger import SourceProfile

_INHERENTLY_TECHNICAL = {"code-block", "table", "formula"}
_TECHNICAL_DENSITY_MIN = 0.05


def atom_is_topic_projectable(
    atom: TechnicalAtom, source_profile: SourceProfile | None = None
) -> bool:
    """Return whether an atom has enough structure for concept-page rendering."""
    if atom.technical_atom_kind in _INHERENTLY_TECHNICAL:
        return True
    if source_profile is not None and not _source_supports_prose_atoms(source_profile):
        return False
    payload = atom.payload
    if isinstance(payload, RulePayload):
        return any((payload.scope, payload.trigger, payload.effect, payload.exception))
    if isinstance(payload, ProcedurePayload):
        return len(payload.steps) >= 2
    if isinstance(payload, WorkedExamplePayload):
        return any(
            (
                payload.inputs,
                payload.operations,
                payload.outputs,
                payload.explanation,
                payload.referenced_atom_ids,
            )
        )
    return False


def _source_supports_prose_atoms(profile: SourceProfile) -> bool:
    technical_count = sum(profile.atom_kind_counts.values())
    accepted = max(profile.accepted_entry_count, 1)
    return technical_count / accepted >= _TECHNICAL_DENSITY_MIN
