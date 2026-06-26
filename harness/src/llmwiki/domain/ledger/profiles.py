"""Derive the source profile and emergent family assignment.

The profile aggregates unit profiles and accepted ledger records. The family
assignment is a calibrated multi-label score derived from that profile after
extraction. It is reporting only: it never adds or removes atom kinds, and it
is derived from reusable signals, never from one source's particular words.
"""

from __future__ import annotations

from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import FamilyLabelScore, SourceFamilyAssignment, SourceProfile

_REPORTING_THRESHOLD = 0.15


def build_source_profile(
    *,
    source_locator: str,
    unit_count: int,
    entries: tuple[LedgerEntry, ...],
    atom_kind_counts: dict[str, int],
    feature_means: dict[str, float],
) -> SourceProfile:
    accepted = [entry for entry in entries if entry.is_usable]
    return SourceProfile(
        source_locator=source_locator,
        unit_count=unit_count,
        accepted_entry_count=len(accepted),
        claim_count=_count(accepted, "claim"),
        event_count=_count(accepted, "event"),
        concept_count=_count(accepted, "concept"),
        relationship_count=_count(accepted, "relationship"),
        atom_kind_counts=dict(sorted(atom_kind_counts.items())),
        feature_signal_means={key: round(value, 4) for key, value in sorted(feature_means.items())},
    )


def assign_family(profile: SourceProfile) -> SourceFamilyAssignment:
    # Calibrated multi-label scores from per-entry ratios, so raw atom counts do
    # not saturate the labels and the assignment stays emergent across sources.
    means = profile.feature_signal_means
    atoms = profile.atom_kind_counts
    accepted = max(profile.accepted_entry_count, 1)
    scores = {
        "coding": _clamp(
            (atoms.get("code-block", 0) + atoms.get("formula", 0) * 0.5) / accepted * 2.0
            + means.get("code-density", 0.0)
        ),
        "rules-reference": _clamp(
            (atoms.get("rule", 0) + atoms.get("table", 0) + atoms.get("procedure", 0)) / accepted
            + means.get("rule-language-density", 0.0) * 0.5
        ),
        "history": _clamp(
            means.get("entity-date-density", 0.0) + profile.event_count / accepted * 2.0
        ),
        "general-prose": _clamp(0.2 + profile.claim_count / accepted * 0.3),
    }
    labels = tuple(
        FamilyLabelScore(label, round(score, 4))
        for label, score in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
        if score >= _REPORTING_THRESHOLD
    )
    confidence = round(max(scores.values()), 4)
    if confidence < _REPORTING_THRESHOLD or not labels:
        return SourceFamilyAssignment(
            labels=(FamilyLabelScore("unknown", confidence),), assignment_confidence=confidence
        )
    return SourceFamilyAssignment(labels=labels, assignment_confidence=confidence)


def _count(entries: list[LedgerEntry], kind: str) -> int:
    return sum(1 for entry in entries if entry.ledger_entry_kind == kind)


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, value))
