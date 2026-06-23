"""JSON mapping for generated source evidence registries."""

from __future__ import annotations

import json
from collections.abc import Sequence
from typing import cast

from llmwiki.domain.evidence_registry import (
    EvidenceKind,
    EvidenceRecord,
    EvidenceRegistry,
    SourceRange,
    SourceText,
    SourceTextKind,
)


def registry_to_json(registry: EvidenceRegistry) -> str:
    return json.dumps(_registry_payload(registry), indent=2, ensure_ascii=False, sort_keys=True)


def registry_from_json(text: str) -> EvidenceRegistry:
    data = json.loads(text)
    return EvidenceRegistry(
        registry_id=data["registry_id"],
        source_texts=tuple(_source_text_from_payload(item) for item in data["source_texts"]),
        source_ranges=tuple(_source_range_from_payload(item) for item in data["source_ranges"]),
        evidence_records=tuple(
            _evidence_record_from_payload(item) for item in data["evidence_records"]
        ),
    )


def _source_text_from_payload(payload: dict[str, object]) -> SourceText:
    return SourceText(
        source_locator=str(payload["source_locator"]),
        source_hash=str(payload["source_hash"]),
        source_text_kind=cast(SourceTextKind, str(payload["source_text_kind"])),
        lines=tuple(str(line) for line in cast(Sequence[object], payload["lines"])),
    )


def _source_range_from_payload(payload: dict[str, object]) -> SourceRange:
    return SourceRange(
        source_range_id=str(payload["source_range_id"]),
        page_id=str(payload["page_id"]),
        source_locator=str(payload["source_locator"]),
        page_range=_optional_range(payload["page_range"]),
        line_range=_optional_range(payload["line_range"]),
        heading_path=str(payload["heading_path"]),
    )


def _evidence_record_from_payload(payload: dict[str, object]) -> EvidenceRecord:
    return EvidenceRecord(
        evidence_id=str(payload["evidence_id"]),
        source_locator=str(payload["source_locator"]),
        source_hash=str(payload["source_hash"]),
        source_range_id=str(payload["source_range_id"]),
        line_range=_optional_range(payload["line_range"]),
        excerpt=str(payload["excerpt"]),
        excerpt_digest=str(payload["excerpt_digest"]),
        evidence_kind=cast(EvidenceKind, str(payload["evidence_kind"])),
        evidence_identity_id=str(payload["evidence_identity_id"]),
        source_claim_id=str(payload.get("source_claim_id", "")),
    )


def _optional_range(value: object) -> tuple[int, int] | None:
    if value is None:
        return None
    items = tuple(int(item) for item in cast(Sequence[str | int], value))
    return (items[0], items[1])


def _registry_payload(registry: EvidenceRegistry) -> dict[str, object]:
    return {
        "registry_id": registry.registry_id,
        "source_texts": [_source_text_payload(item) for item in registry.source_texts],
        "source_ranges": [_source_range_payload(item) for item in registry.source_ranges],
        "evidence_records": [
            _evidence_record_payload(item) for item in registry.evidence_records
        ],
    }


def _source_text_payload(source_text: SourceText) -> dict[str, object]:
    return {
        "source_locator": source_text.source_locator,
        "source_hash": source_text.source_hash,
        "source_text_kind": source_text.source_text_kind,
        "lines": list(source_text.lines),
    }


def _source_range_payload(source_range: SourceRange) -> dict[str, object]:
    return {
        "source_range_id": source_range.source_range_id,
        "page_id": source_range.page_id,
        "source_locator": source_range.source_locator,
        "page_range": source_range.page_range,
        "line_range": source_range.line_range,
        "heading_path": source_range.heading_path,
    }


def _evidence_record_payload(record: EvidenceRecord) -> dict[str, object]:
    return {
        "evidence_id": record.evidence_id,
        "source_locator": record.source_locator,
        "source_hash": record.source_hash,
        "source_range_id": record.source_range_id,
        "line_range": record.line_range,
        "excerpt": record.excerpt,
        "excerpt_digest": record.excerpt_digest,
        "evidence_kind": record.evidence_kind,
        "evidence_identity_id": record.evidence_identity_id,
        "source_claim_id": record.source_claim_id,
    }
