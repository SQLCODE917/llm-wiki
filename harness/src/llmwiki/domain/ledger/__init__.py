"""Claim-Ledger-First domain.

This package is the pure ``DomainModule`` from
docs/2026-06-25-claim-ledger-first-architecture.md. It owns the claim-ledger
domain objects and domain logic. It performs no I/O and has no side effects:
it receives typed input records and returns typed output records. Adapters in
``llmwiki.runtime`` and ``llmwiki.store`` perform all I/O before or after the
domain logic runs.

The authority chain is:

    RawSource -> EvidenceRegistry -> DocumentStructureArtifact
        -> ClaimLedgerArtifact -> WikiPage

``ClaimLedger`` is the first generated source-derived artifact. ``WikiPage``
records are projections of it, not independent summaries.
"""
