"""Quality report for the cross-source-projection scope.

Checks that a cross-source page draws on at least two sources, that every
source-backed position resolves to one support, that relationships use the
controlled vocabulary and relate at least two positions, and that no internal
ids leak into the page body.
"""

from __future__ import annotations

from llmwiki.domain.ledger.cross_source import CrossSourceTopic
from llmwiki.domain.ledger.pointers import PortableArtifactPointer
from llmwiki.domain.ledger.quality import FindingCollector, LedgerQualityReport
from llmwiki.domain.ledger.quality_catalog import (
    QualityCheckCatalog,
    QualityFindingSeverityPolicy,
)
from llmwiki.domain.ledger.vocab import CROSS_SOURCE_RELATIONSHIP_KINDS

_INTERNAL_ID_PREFIXES = ("ledger-entry-", "projection-coverage-entry-", "atom-candidate-")


def build_cross_source_quality_report(
    topic: CrossSourceTopic,
    page_body: str,
    *,
    catalog: QualityCheckCatalog,
    severity: QualityFindingSeverityPolicy,
    catalog_pointer: PortableArtifactPointer,
) -> LedgerQualityReport:
    finder = FindingCollector("cross-source-projection", catalog, severity)
    if len(set(topic.support_ids)) < 2:
        finder.add("ck-cross-source-min-support", "projection-coverage-artifact", topic.topic_key)
    for position in topic.positions:
        if not position.projection_source_support_id:
            finder.add(
                "ck-cross-source-position-traceable",
                "source-backed-position",
                position.source_backed_position_id,
            )
    for relationship in topic.relationships:
        if len(set(relationship.related_position_ids)) < 2:
            finder.add(
                "ck-cross-source-relationship-arity",
                "cross-source-relationship",
                relationship.cross_source_relationship_id,
            )
        if relationship.cross_source_relationship_kind not in CROSS_SOURCE_RELATIONSHIP_KINDS:
            finder.add(
                "ck-cross-source-relationship-vocabulary",
                "cross-source-relationship",
                relationship.cross_source_relationship_id,
            )
    if any(prefix in page_body for prefix in _INTERNAL_ID_PREFIXES):
        finder.add("ck-cross-source-page-no-internal-ids", "page-body", topic.topic_key)
    finder.add("ck-cross-source-metric", "projection-coverage-artifact", topic.topic_key)
    return LedgerQualityReport("cross-source-projection", catalog_pointer, tuple(finder.findings))
