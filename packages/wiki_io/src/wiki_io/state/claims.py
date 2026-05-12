"""Claims storage for wiki extraction pipeline.

Handles storage and retrieval of extracted claims:
- Raw claims: Append-only JSONL for crash recovery (Phase 1a)
- Normalized claims: Deduped JSON with stable IDs (Phase 1b)

Usage:
    from wiki_io.state.claims import (
        append_raw_claim,
        load_raw_claims,
        save_normalized_claims,
        load_normalized_claims,
    )
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

from wiki_io.state.paths import (
    get_raw_claims_path,
    get_normalized_claims_path,
    ensure_state_dir,
)


# ============================================================================
# Raw Claims (Phase 1a) - Append-only JSONL
# ============================================================================


@dataclass
class RawClaim:
    """A raw extracted claim before normalization.

    This is similar to wiki_core.types.RawClaim but is specifically
    for the I/O layer's storage format.
    """
    topic: str
    claim: str
    evidence: str
    locator: str
    chunk_index: int
    extracted_at: str = ""

    def __post_init__(self):
        if not self.extracted_at:
            self.extracted_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "topic": self.topic,
            "claim": self.claim,
            "evidence": self.evidence,
            "locator": self.locator,
            "chunk_index": self.chunk_index,
            "extracted_at": self.extracted_at,
        }

    @classmethod
    def from_dict(cls, d: dict) -> RawClaim:
        return cls(
            topic=d.get("topic", ""),
            claim=d.get("claim", ""),
            evidence=d.get("evidence", ""),
            locator=d.get("locator", ""),
            chunk_index=d.get("chunk_index", 0),
            extracted_at=d.get("extracted_at", ""),
        )


def append_raw_claim(slug: str, claim: RawClaim) -> None:
    """Append a raw claim to claims-raw.jsonl (resumable writes)."""
    ensure_state_dir(slug)
    path = get_raw_claims_path(slug)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(claim.to_dict()) + "\n")


def append_raw_claims(slug: str, claims: list[RawClaim]) -> None:
    """Append multiple raw claims to claims-raw.jsonl."""
    ensure_state_dir(slug)
    path = get_raw_claims_path(slug)
    with open(path, "a", encoding="utf-8") as f:
        for claim in claims:
            f.write(json.dumps(claim.to_dict()) + "\n")


def load_raw_claims(slug: str) -> list[RawClaim]:
    """Load all raw claims from claims-raw.jsonl."""
    path = get_raw_claims_path(slug)
    if not path.exists():
        return []

    claims = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    claims.append(RawClaim.from_dict(json.loads(line)))
                except json.JSONDecodeError:
                    continue
    return claims


def iter_raw_claims(slug: str) -> Iterator[RawClaim]:
    """Iterate over raw claims without loading all into memory."""
    path = get_raw_claims_path(slug)
    if not path.exists():
        return

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    yield RawClaim.from_dict(json.loads(line))
                except json.JSONDecodeError:
                    continue


def count_raw_claims(slug: str) -> int:
    """Count raw claims without loading all into memory."""
    path = get_raw_claims_path(slug)
    if not path.exists():
        return 0

    count = 0
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                count += 1
    return count


def get_processed_chunk_indices(slug: str) -> set[int]:
    """Derive processed chunk indices from claims-raw.jsonl.

    This replaces ExtractionState.processed_chunks by deriving the set
    from the chunk_index field of raw claims.
    """
    indices: set[int] = set()
    for claim in iter_raw_claims(slug):
        indices.add(claim.chunk_index)
    return indices


# ============================================================================
# Normalized Claims (Phase 1b) - Deduped with stable IDs
# ============================================================================


@dataclass
class NormalizedClaim:
    """A normalized claim with stable ID."""
    claim_id: str
    topic: str
    claim: str
    evidence: str
    locator: str
    chunk_index: int

    def to_dict(self) -> dict:
        return {
            "claim_id": self.claim_id,
            "topic": self.topic,
            "claim": self.claim,
            "evidence": self.evidence,
            "locator": self.locator,
            "chunk_index": self.chunk_index,
        }

    @classmethod
    def from_dict(cls, d: dict) -> NormalizedClaim:
        return cls(
            claim_id=d.get("claim_id", ""),
            topic=d.get("topic", ""),
            claim=d.get("claim", ""),
            evidence=d.get("evidence", ""),
            locator=d.get("locator", ""),
            chunk_index=d.get("chunk_index", 0),
        )


@dataclass
class NormalizedClaimsData:
    """Container for normalized claims with metadata."""
    slug: str
    claims: list[NormalizedClaim]
    topics: dict[str, list[str]]  # topic -> list of claim_ids
    normalized_at: str = ""
    raw_claims_count: int = 0
    deduped_count: int = 0

    def __post_init__(self):
        if not self.normalized_at:
            self.normalized_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "_meta": {
                "slug": self.slug,
                "normalized_at": self.normalized_at,
                "raw_claims_count": self.raw_claims_count,
                "deduped_count": self.deduped_count,
            },
            "claims": [c.to_dict() for c in self.claims],
            "topics": self.topics,
        }

    @classmethod
    def from_dict(cls, d: dict) -> NormalizedClaimsData:
        meta = d.get("_meta", {})
        return cls(
            slug=meta.get("slug", ""),
            claims=[NormalizedClaim.from_dict(c) for c in d.get("claims", [])],
            topics=d.get("topics", {}),
            normalized_at=meta.get("normalized_at", ""),
            raw_claims_count=meta.get("raw_claims_count", 0),
            deduped_count=meta.get("deduped_count", 0),
        )


def save_normalized_claims(slug: str, data: NormalizedClaimsData) -> Path:
    """Save normalized claims to claims-normalized.json."""
    ensure_state_dir(slug)
    path = get_normalized_claims_path(slug)
    path.write_text(json.dumps(data.to_dict(), indent=2) + "\n")
    return path


def load_normalized_claims(slug: str) -> NormalizedClaimsData | None:
    """Load normalized claims from claims-normalized.json."""
    path = get_normalized_claims_path(slug)
    if not path.exists():
        return None

    try:
        return NormalizedClaimsData.from_dict(json.loads(path.read_text()))
    except json.JSONDecodeError:
        return None


# ============================================================================
# Convenience functions for synthesis
# ============================================================================


@dataclass
class ExtractionDataForSynthesis:
    """Data needed for page synthesis, loaded from claims-normalized.json.

    This is a lightweight structure for synthesis workflows, providing
    claims organized by topic.
    """
    slug: str
    claims: list[NormalizedClaim]
    topics: dict[str, list[NormalizedClaim]]  # topic -> list of claims
    raw_claims_count: int = 0
    deduped_count: int = 0


def load_extraction_data_for_synthesis(slug: str) -> ExtractionDataForSynthesis | None:
    """Load extraction data from claims-normalized.json for synthesis workflows.

    This is the preferred way to load extraction results after Phase 1 completes.

    Returns:
        ExtractionDataForSynthesis with claims and topics, or None if not found.
    """
    normalized = load_normalized_claims(slug)
    if normalized is None:
        return None

    # Build topics dict with full claim objects (not just IDs)
    claim_by_id = {c.claim_id: c for c in normalized.claims}
    topics: dict[str, list[NormalizedClaim]] = {}

    for topic, claim_ids in normalized.topics.items():
        claims_for_topic = []
        for claim_id in claim_ids:
            if claim_id in claim_by_id:
                claims_for_topic.append(claim_by_id[claim_id])
        if claims_for_topic:
            topics[topic] = claims_for_topic

    return ExtractionDataForSynthesis(
        slug=normalized.slug,
        claims=normalized.claims,
        topics=topics,
        raw_claims_count=normalized.raw_claims_count,
        deduped_count=normalized.deduped_count,
    )
