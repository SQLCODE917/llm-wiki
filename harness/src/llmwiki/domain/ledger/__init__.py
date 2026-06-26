"""Claim ledger domain objects and current-harness adapters.

This package owns pure claim-ledger domain objects and the source-agnostic
adapter that packages this repo's current ingest artifacts into portable ledger
artifacts. It performs no I/O and has no side effects: it receives typed input
records and returns typed output records. Adapters in ``llmwiki.runtime`` and
``llmwiki.store`` perform all I/O before or after the domain logic runs.

The authority chain is:

    RawSource -> EvidenceRegistry -> DocumentStructureArtifact
        -> ClaimLedgerArtifact

``ClaimLedger`` is generated beside the existing page-plan, source-summary, and
technical-atom artifacts. Wiki pages continue to use this repo's stronger
source-summary plus technical-detail renderer; ledger artifacts add audit,
quality, and portability without replacing page synthesis.
"""
