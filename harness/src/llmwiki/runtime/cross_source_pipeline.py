"""Canonical concept synthesis pipeline.

Loads stored per-source topic indexes and claim ledgers, groups recurring
topics, and renders one canonical concept page per shared topic plus a
synthesis overview. Deterministic: no model is called.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.artifacts import build_quality_check_catalog_artifact
from llmwiki.domain.ledger.canonical_concept import (
    CanonicalConceptPage,
    ConceptAtomBlock,
    ConceptEvidenceItem,
    ConceptRelationship,
    ConceptSourceSection,
    render_canonical_concept_page,
)
from llmwiki.domain.ledger.cross_source import CrossSourceTopic, plan_cross_source_topics
from llmwiki.domain.ledger.cross_source_quality import build_cross_source_quality_report
from llmwiki.domain.ledger.pointers import PortableArtifactPointer, quality_check_catalog_pointer
from llmwiki.domain.ledger.quality import page_write_decision
from llmwiki.domain.ledger.quality_catalog import (
    QualityCheckCatalog,
    QualityFindingSeverityPolicy,
    default_quality_check_catalog,
    default_reason_applicability_policy,
    default_severity_policy,
)
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify
from llmwiki.runtime.cross_source_load import (
    LoadedLedger,
    LoadedSources,
    LoadedTopic,
    load_sources,
)

_SYNTHESIS_PAGE = "cross-source-synthesis"
_RELATION_KINDS = ("agrees-with", "conflicts-with", "qualifies", "supersedes")


@dataclass(frozen=True)
class CrossSourceResult:
    pages: tuple[WikiPage, ...]
    topics: tuple[CrossSourceTopic, ...]
    blocked: tuple[str, ...]
    summary: str


def build_cross_source_pages(
    topic_index_jsons: tuple[str, ...], claim_ledger_jsons: tuple[str, ...], *, today: str
) -> CrossSourceResult:
    loaded = load_sources(topic_index_jsons, claim_ledger_jsons)
    topics = plan_cross_source_topics(loaded.positions)
    topics_by_key = _loaded_topics_by_key(loaded)
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    catalog_pointer = _catalog_pointer(catalog, severity)

    pages: list[WikiPage] = []
    written_topics: list[CrossSourceTopic] = []
    blocked: list[str] = []
    for topic in topics:
        page_id = slugify(topic.topic_key)
        concept = _canonical_concept(topic, topics_by_key[topic.topic_key], loaded)
        rendered = render_canonical_concept_page(concept, page_id)
        report = build_cross_source_quality_report(
            topic,
            rendered.page_body,
            catalog=catalog,
            severity=severity,
            catalog_pointer=catalog_pointer,
        )
        if page_write_decision(report) == "block-authoritative-write":
            blocked.append(topic.topic_key)
            continue
        pages.append(
            _topic_page(concept, page_id, rendered.page_body, rendered.page_body_hash, today)
        )
        written_topics.append(topic)
    pages.append(_synthesis_page(written_topics, len(loaded.sources), today))
    summary = (
        f"Canonical concept synthesis over {len(loaded.sources)} source(s): "
        f"{len(written_topics)} concept page(s), {len(blocked)} blocked. "
        f"Relations: {_relation_summary(written_topics)}."
    )
    return CrossSourceResult(tuple(pages), tuple(written_topics), tuple(blocked), summary)


def _topic_page(
    concept: CanonicalConceptPage, page_id: str, body: str, body_hash: str, today: str
) -> WikiPage:
    sources = tuple(sorted(f"raw/{section.source_locator}" for section in concept.source_sections))
    metadata = PageMetadata(
        page_id=page_id,
        page_kind=concept.page_kind,
        summary=(
            f"Canonical concept '{concept.label}': {len(concept.source_sections)} source(s), "
            f"{concept.statement_count} statement(s), {concept.atom_count} atom(s), "
            f"{len(concept.relationships)} relation(s)."
        ),
        sources=sources,
        updated=today,
        category_path=f"{concept.page_kind}s",
        projection_coverage_pointer=f"canonical-concept-{page_id}@{body_hash}",
    )
    return WikiPage.from_metadata(metadata, body)


def _synthesis_page(topics: list[CrossSourceTopic], source_count: int, today: str) -> WikiPage:
    lines = [
        "# Cross-Source Synthesis",
        "",
        f"Canonical concept pages built from {source_count} ingested source ledger(s).",
        "",
        "## Topics",
        "",
    ]
    for topic in topics:
        lines.append(
            f"- [[{slugify(topic.topic_key)}]] - {topic.page_kind}, "
            f"{len(topic.support_ids)} sources, {len(topic.relationships)} relation(s)"
        )
    lines.extend(["", "## Relation summary", ""])
    counts = _relation_counts(topics)
    lines.extend(f"- {kind}: {counts.get(kind, 0)}" for kind in _RELATION_KINDS)
    metadata = PageMetadata(
        page_id=_SYNTHESIS_PAGE,
        page_kind="synthesis",
        summary=f"Cross-source synthesis index: {len(topics)} shared topics.",
        updated=today,
    )
    return WikiPage.from_metadata(metadata, "\n".join(lines) + "\n")


def _relation_counts(topics: list[CrossSourceTopic]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for topic in topics:
        for relationship in topic.relationships:
            kind = relationship.cross_source_relationship_kind
            counts[kind] = counts.get(kind, 0) + 1
    return counts


def _relation_summary(topics: list[CrossSourceTopic]) -> str:
    counts = _relation_counts(topics)
    return ", ".join(f"{kind}={counts.get(kind, 0)}" for kind in _RELATION_KINDS)


def _loaded_topics_by_key(loaded: LoadedSources) -> dict[str, tuple[LoadedTopic, ...]]:
    grouped: dict[str, list[LoadedTopic]] = {}
    for source in loaded.sources:
        for topic in source.topics:
            grouped.setdefault(topic.topic_key, []).append(topic)
    return {key: tuple(value) for key, value in grouped.items()}


def _canonical_concept(
    topic: CrossSourceTopic, source_topics: tuple[LoadedTopic, ...], loaded: LoadedSources
) -> CanonicalConceptPage:
    by_source = {position.source_locator: position for position in topic.positions}
    sections = tuple(
        _source_section(source_topic, loaded.ledgers[source_topic.source_locator])
        for source_topic in source_topics
        if source_topic.source_locator in by_source
        and source_topic.source_locator in loaded.ledgers
    )
    return CanonicalConceptPage(
        topic_key=topic.topic_key,
        label=topic.label,
        page_kind=topic.page_kind,
        source_sections=sections,
        relationships=_relationships(topic),
        support_ids=topic.support_ids,
    )


def _source_section(topic: LoadedTopic, ledger: LoadedLedger) -> ConceptSourceSection:
    source_page_id = slugify(topic.source_locator.rsplit(".", 1)[0])
    match_terms = tuple(term for term in topic.topic_key.split("-") if term)
    return ConceptSourceSection(
        source_locator=topic.source_locator,
        source_page_id=source_page_id,
        topic_page_id=slugify(f"{source_page_id}-{topic.topic_key}"),
        label=topic.label,
        evidence_items=tuple(
            _evidence_item(entry)
            for entry_id in topic.entry_ids
            if (entry := ledger.entries.get(entry_id)) is not None
        ),
        atom_blocks=tuple(
            _atom_block(atom, _context(ledger.atom_contexts.get(atom_id, ()), match_terms))
            for atom_id in topic.atom_ids
            if (atom := ledger.atoms.get(atom_id)) is not None
        ),
    )


def _evidence_item(entry: dict[str, object]) -> ConceptEvidenceItem:
    source_locator = str(entry.get("source_locator") or "")
    source_range_id = str(entry.get("source_range_id") or "")
    text = str(entry.get("normalized_text") or entry.get("source_text") or "")
    return ConceptEvidenceItem(
        ledger_entry_id=str(entry["ledger_entry_id"]),
        text=text,
        citation_label=f"{source_locator} ({source_range_id})",
    )


def _atom_block(atom: dict[str, object], context: dict[str, object] | None) -> ConceptAtomBlock:
    source_range_ids: tuple[str, ...] = ()
    context_text = ""
    if context is not None:
        context_text = str(context.get("context_text") or "")
        source_range_ids = _string_tuple(context.get("context_source_range_ids"))
    payload = atom.get("payload")
    return ConceptAtomBlock(
        technical_atom_id=str(atom["technical_atom_id"]),
        technical_atom_kind=str(atom["technical_atom_kind"]),
        payload=payload if isinstance(payload, dict) else {},
        source_locator=str(atom.get("source_locator") or ""),
        source_range_id=str(atom.get("source_range_id") or ""),
        context_text=context_text,
        context_source_range_ids=source_range_ids,
    )


def _context(
    contexts: tuple[dict[str, object], ...], match_terms: tuple[str, ...]
) -> dict[str, object] | None:
    if not contexts:
        return None
    lowered_terms = tuple(term.lower() for term in match_terms)
    for context in contexts:
        text = str(context.get("context_text") or "").lower()
        keys = tuple(
            item.lower() for item in _string_tuple(context.get("demonstrated_concept_keys"))
        )
        if any(term in text or term in keys for term in lowered_terms):
            return context
    return contexts[0]


def _relationships(topic: CrossSourceTopic) -> tuple[ConceptRelationship, ...]:
    by_id = {position.source_backed_position_id: position for position in topic.positions}
    relationships: list[ConceptRelationship] = []
    for relationship in topic.relationships:
        positions = tuple(
            by_id[position_id]
            for position_id in relationship.related_position_ids
            if position_id in by_id
        )
        relationships.append(
            ConceptRelationship(
                cross_source_relationship_id=relationship.cross_source_relationship_id,
                relationship_kind=relationship.cross_source_relationship_kind,
                source_page_ids=tuple(
                    slugify(position.source_locator.rsplit(".", 1)[0]) for position in positions
                ),
                texts=tuple(position.text for position in positions),
            )
        )
    return tuple(relationships)


def _string_tuple(value: object) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(str(item) for item in value)


def _catalog_pointer(
    catalog: QualityCheckCatalog, severity: QualityFindingSeverityPolicy
) -> PortableArtifactPointer:
    artifact = build_quality_check_catalog_artifact(
        catalog, default_reason_applicability_policy(), severity
    )
    return quality_check_catalog_pointer(
        artifact.quality_check_catalog_artifact_id, artifact.quality_check_catalog_fingerprint
    )
