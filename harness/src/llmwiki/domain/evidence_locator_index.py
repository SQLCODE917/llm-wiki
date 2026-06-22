"""Stable evidence locator indexes for deterministic audits."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

LocatorKind = Literal["normalized-line", "page-range"]
LocatorSeverity = Literal["blocker", "warning", "info"]
LocatorCategory = Literal[
    "invalid-range", "missing-source-text", "locator-drift", "stale-artifact"
]
LOCATOR_ARTIFACT_VERSION = 1


@dataclass(frozen=True)
class EvidenceIdentity:
    evidence_identity_id: str
    source_locator: str
    source_hash: str
    locator_text: str
    canonical_excerpt_digest: str

    @classmethod
    def from_excerpt(
        cls, source_locator: str, source_hash: str, locator_text: str, excerpt: str
    ) -> EvidenceIdentity:
        canonical_excerpt_digest = _digest(canonicalize_evidence_text(excerpt))
        identity = "|".join(
            (source_locator, source_hash, locator_text, canonical_excerpt_digest)
        )
        return cls(
            evidence_identity_id=f"evidence-identity-{_digest(identity)[:16]}",
            source_locator=source_locator,
            source_hash=source_hash,
            locator_text=locator_text,
            canonical_excerpt_digest=canonical_excerpt_digest,
        )

    @property
    def evidence_id(self) -> str:
        return "evidence-" + self.evidence_identity_id.removeprefix("evidence-identity-")


@dataclass(frozen=True)
class EvidenceLocator:
    locator_id: str
    source_locator: str
    source_hash: str
    locator_text: str
    locator_kind: LocatorKind
    range_start: int
    range_end: int
    excerpt_digest: str
    canonical_excerpt_digest: str

    @classmethod
    def from_excerpt(
        cls,
        *,
        source_locator: str,
        source_hash: str,
        locator_text: str,
        locator_kind: LocatorKind,
        range_start: int,
        range_end: int,
        excerpt: str,
    ) -> EvidenceLocator:
        excerpt_digest = _digest(excerpt.strip())
        canonical_excerpt_digest = _digest(canonicalize_evidence_text(excerpt))
        identity = "|".join(
            (source_locator, source_hash, locator_text, canonical_excerpt_digest)
        )
        return cls(
            locator_id=f"evidence-locator-{_digest(identity)[:16]}",
            source_locator=source_locator,
            source_hash=source_hash,
            locator_text=locator_text,
            locator_kind=locator_kind,
            range_start=range_start,
            range_end=range_end,
            excerpt_digest=excerpt_digest,
            canonical_excerpt_digest=canonical_excerpt_digest,
        )


@dataclass(frozen=True)
class EvidenceLocatorFinding:
    finding_id: str
    severity: LocatorSeverity
    category: LocatorCategory
    source_locator: str
    page_id: str
    locator_id: str
    message: str


@dataclass(frozen=True)
class EvidenceLocatorIndex:
    index_id: str
    source_locator: str
    source_hash: str
    locator_artifact_fingerprint: str
    locators: tuple[EvidenceLocator, ...]
    findings: tuple[EvidenceLocatorFinding, ...] = ()

    @classmethod
    def from_locators(
        cls,
        source_locator: str,
        source_hash: str,
        locators: Sequence[EvidenceLocator],
        findings: Sequence[EvidenceLocatorFinding] = (),
    ) -> EvidenceLocatorIndex:
        deduped = tuple({locator.locator_id: locator for locator in locators}.values())
        fingerprint = locator_artifact_fingerprint(source_locator, source_hash)
        index_key = "|".join(
            (
                source_locator,
                source_hash,
                fingerprint,
                *sorted(locator.locator_id for locator in deduped),
            )
        )
        return cls(
            index_id=f"evidence-locator-index-{_digest(index_key)[:16]}",
            source_locator=source_locator,
            source_hash=source_hash,
            locator_artifact_fingerprint=fingerprint,
            locators=tuple(sorted(deduped, key=lambda locator: locator.locator_id)),
            findings=tuple(sorted(findings, key=lambda finding: finding.finding_id)),
        )

    @property
    def invalid_count(self) -> int:
        return sum(1 for finding in self.findings if finding.category == "invalid-range")


def locator_artifact_fingerprint(source_locator: str, source_hash: str) -> str:
    payload = {
        "artifact_version": LOCATOR_ARTIFACT_VERSION,
        "source_locator": source_locator,
        "source_hash": source_hash,
    }
    return _digest(json.dumps(payload, sort_keys=True))[:16]


def canonicalize_evidence_text(text: str) -> str:
    text = re.sub(r"\bPage\s+\d+\b", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"(?<=\w)-\s+(?=\w)", "", text)
    text = re.sub(r"[\u2010-\u2015\u2212]", "-", text)
    text = re.sub(r"[“”]", '"', text)
    text = re.sub(r"[‘’]", "'", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
