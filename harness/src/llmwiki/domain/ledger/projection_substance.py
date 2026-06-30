"""Substance checks shared by ledger projection planners."""

from __future__ import annotations

from llmwiki.domain.ledger.entries import LedgerEntry


def entry_is_unresolved_context_pointer(entry: LedgerEntry) -> bool:
    scope = entry.spatial_scope
    return bool(
        entry.is_claim_like
        and scope is not None
        and scope.spatial_kind == "relative-location"
        and not scope.normalized_spatial_value
        and "identity" in entry.claim_role_tags
    )
