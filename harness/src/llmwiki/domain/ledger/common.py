"""Small shared value objects used across ledger entries and atoms."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewReason:
    """Structured reason an entry, atom, or candidate needs review or failed.

    ``reason_kind`` is a reusable category (e.g. ``fragmentary``,
    ``ambiguous-reference``, ``unresolved-anchor``, ``exact-wording-unpreserved``,
    ``partial-parse``, ``unparsed``, ``dropped-local-context``,
    ``schema-incomplete``, ``low-confidence``), never a source-specific phrase.
    """

    reason_kind: str
    detail: str
    evidence_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class ConfidenceBasis:
    """Structured reason for one extraction confidence value."""

    basis: str
    contributing_signals: tuple[str, ...] = ()


@dataclass(frozen=True)
class TemporalScope:
    """Source-derived time scope for a claim-like ledger entry."""

    temporal_text: str
    temporal_kind: str
    temporal_confidence: str
    normalized_temporal_value: str = ""
    temporal_anchor_entry_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class SpatialScope:
    """Source-derived place scope for a claim-like ledger entry."""

    spatial_text: str
    spatial_kind: str
    spatial_confidence: str
    normalized_spatial_value: str = ""
    spatial_anchor_entry_ids: tuple[str, ...] = ()
