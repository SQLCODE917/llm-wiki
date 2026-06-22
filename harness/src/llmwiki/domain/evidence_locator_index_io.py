"""JSON mapping for generated evidence locator indexes."""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import cast

from llmwiki.domain.evidence_locator_index import (
    EvidenceLocator,
    EvidenceLocatorFinding,
    EvidenceLocatorIndex,
    LocatorCategory,
    LocatorKind,
    LocatorSeverity,
)


def evidence_locator_index_to_json(index: EvidenceLocatorIndex) -> str:
    return json.dumps(asdict(index), indent=2, ensure_ascii=False, sort_keys=True)


def evidence_locator_index_from_json(text: str) -> EvidenceLocatorIndex:
    data = json.loads(text)
    return EvidenceLocatorIndex(
        index_id=str(data["index_id"]),
        source_locator=str(data["source_locator"]),
        source_hash=str(data["source_hash"]),
        locator_artifact_fingerprint=str(data["locator_artifact_fingerprint"]),
        locators=tuple(_locator(item) for item in data["locators"]),
        findings=tuple(_finding(item) for item in data["findings"]),
    )


def _locator(payload: dict[str, object]) -> EvidenceLocator:
    return EvidenceLocator(
        locator_id=str(payload["locator_id"]),
        source_locator=str(payload["source_locator"]),
        source_hash=str(payload["source_hash"]),
        locator_text=str(payload["locator_text"]),
        locator_kind=cast(LocatorKind, str(payload["locator_kind"])),
        range_start=int(str(payload["range_start"])),
        range_end=int(str(payload["range_end"])),
        excerpt_digest=str(payload["excerpt_digest"]),
        canonical_excerpt_digest=str(payload["canonical_excerpt_digest"]),
    )


def _finding(payload: dict[str, object]) -> EvidenceLocatorFinding:
    return EvidenceLocatorFinding(
        finding_id=str(payload["finding_id"]),
        severity=cast(LocatorSeverity, str(payload["severity"])),
        category=cast(LocatorCategory, str(payload["category"])),
        source_locator=str(payload["source_locator"]),
        page_id=str(payload["page_id"]),
        locator_id=str(payload["locator_id"]),
        message=str(payload["message"]),
    )
