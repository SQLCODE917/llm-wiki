#!/usr/bin/env python3
"""Extraction state management for wiki ingestion pipeline.

This module implements the separated extraction/candidate state from
DESIGN_ingestion-improvements.md.

State files:
- claims-raw.jsonl: Append-only raw claims from extraction (Phase 1a)
- claims-normalized.json: Deduped claims with stable IDs (Phase 1b)
- candidates.generated.json: Machine-generated page proposals (Phase 1c)
- candidates.override.json: Human curator overrides (add/modify/remove)
- candidates.json: Merged candidates = generated + override

Usage:
    from wiki_extraction_state import (
        append_raw_claim,
        load_raw_claims,
        save_normalized_claims,
        load_normalized_claims,
        save_generated_candidates,
        merge_candidates,
    )
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator


# ============================================================================
# Paths
# ============================================================================


def get_state_dir(slug: str) -> Path:
    """Get the extraction state directory for a slug."""
    return Path(f".wiki-extraction-state/{slug}")


def get_raw_claims_path(slug: str) -> Path:
    """Get the path to claims-raw.jsonl."""
    return get_state_dir(slug) / "claims-raw.jsonl"


def get_normalized_claims_path(slug: str) -> Path:
    """Get the path to claims-normalized.json."""
    return get_state_dir(slug) / "claims-normalized.json"


def get_generated_candidates_path(slug: str) -> Path:
    """Get the path to candidates.generated.json."""
    return get_state_dir(slug) / "candidates.generated.json"


def get_override_path(slug: str) -> Path:
    """Get the path to candidates.override.json."""
    return get_state_dir(slug) / "candidates.override.json"


def get_candidates_path(slug: str) -> Path:
    """Get the path to candidates.json (merged)."""
    return get_state_dir(slug) / "candidates.json"


def get_legacy_state_path(slug: str) -> Path:
    """Get the path to legacy state.json for compatibility."""
    return get_state_dir(slug) / "state.json"


# ============================================================================
# Raw Claims (Phase 1a) - Append-only JSONL
# ============================================================================


@dataclass
class RawClaim:
    """A raw extracted claim before normalization."""
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
    path = get_raw_claims_path(slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(claim.to_dict()) + "\n")


def append_raw_claims(slug: str, claims: list[RawClaim]) -> None:
    """Append multiple raw claims to claims-raw.jsonl."""
    path = get_raw_claims_path(slug)
    path.parent.mkdir(parents=True, exist_ok=True)
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
    path = get_normalized_claims_path(slug)
    path.parent.mkdir(parents=True, exist_ok=True)
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
# Extraction Data for Synthesis (consolidates state.json functionality)
# ============================================================================


@dataclass
class ExtractionDataForSynthesis:
    """Data needed for page synthesis, loaded from claims-normalized.json.

    This replaces the old ExtractionState.load() pattern for synthesis workflows.
    ExtractionState is still used during the extraction phase itself for
    chunk tracking, but this lightweight structure is used afterwards.
    """
    slug: str
    claims: list[NormalizedClaim]
    topics: dict[str, list[NormalizedClaim]]  # topic -> list of claims
    raw_claims_count: int = 0
    deduped_count: int = 0


def load_extraction_data_for_synthesis(slug: str) -> ExtractionDataForSynthesis | None:
    """Load extraction data from claims-normalized.json for synthesis workflows.

    This is the preferred way to load extraction results after Phase 1 completes.
    It replaces the old pattern of loading state.json via ExtractionState.load().

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
# Candidates (Phase 1c) - Page proposals
# ============================================================================


@dataclass
class Candidate:
    """A candidate page proposal."""
    title: str
    path: str
    page_type: str  # concept, entity, procedure, reference
    priority: str   # must create, should create, could create, defer
    claim_ids: list[str]
    evidence_basis: str = ""
    group: str = ""  # Natural grouping from source
    status: str = "not created"  # not created, created, suppressed

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "path": self.path,
            "page_type": self.page_type,
            "priority": self.priority,
            "claim_ids": self.claim_ids,
            "evidence_basis": self.evidence_basis,
            "group": self.group,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, d: dict) -> Candidate:
        return cls(
            title=d.get("title", ""),
            path=d.get("path", ""),
            page_type=d.get("page_type", "concept"),
            priority=d.get("priority", "should create"),
            claim_ids=d.get("claim_ids", []),
            evidence_basis=d.get("evidence_basis", ""),
            group=d.get("group", ""),
            status=d.get("status", "not created"),
        )


@dataclass
class GeneratedCandidatesData:
    """Container for machine-generated candidates."""
    slug: str
    candidates: list[Candidate]
    generated_at: str = ""
    normalized_claims_hash: str = ""

    def __post_init__(self):
        if not self.generated_at:
            self.generated_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "_meta": {
                "slug": self.slug,
                "generated_at": self.generated_at,
                "normalized_claims_hash": self.normalized_claims_hash,
            },
            "candidates": [c.to_dict() for c in self.candidates],
        }

    @classmethod
    def from_dict(cls, d: dict) -> GeneratedCandidatesData:
        meta = d.get("_meta", {})
        return cls(
            slug=meta.get("slug", ""),
            candidates=[Candidate.from_dict(c)
                        for c in d.get("candidates", [])],
            generated_at=meta.get("generated_at", ""),
            normalized_claims_hash=meta.get("normalized_claims_hash", ""),
        )


def save_generated_candidates(slug: str, data: GeneratedCandidatesData) -> Path:
    """Save generated candidates to candidates.generated.json."""
    path = get_generated_candidates_path(slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data.to_dict(), indent=2) + "\n")
    return path


def load_generated_candidates(slug: str) -> GeneratedCandidatesData | None:
    """Load generated candidates from candidates.generated.json."""
    path = get_generated_candidates_path(slug)
    if not path.exists():
        return None

    try:
        return GeneratedCandidatesData.from_dict(json.loads(path.read_text()))
    except json.JSONDecodeError:
        return None


# ============================================================================
# Override Schema
# ============================================================================


@dataclass
class CandidateOverride:
    """A single candidate override entry."""
    path: str
    title: str = ""
    page_type: str = ""
    priority: str = ""
    reason: str = ""

    def to_dict(self) -> dict:
        d = {"path": self.path}
        if self.title:
            d["title"] = self.title
        if self.page_type:
            d["page_type"] = self.page_type
        if self.priority:
            d["priority"] = self.priority
        if self.reason:
            d["reason"] = self.reason
        return d

    @classmethod
    def from_dict(cls, d: dict) -> CandidateOverride:
        return cls(
            path=d.get("path", ""),
            title=d.get("title", ""),
            page_type=d.get("page_type", ""),
            priority=d.get("priority", ""),
            reason=d.get("reason", ""),
        )


@dataclass
class OverridesData:
    """Container for candidate overrides."""
    add: list[CandidateOverride] = field(default_factory=list)
    modify: list[CandidateOverride] = field(default_factory=list)
    remove: list[CandidateOverride] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "add": [o.to_dict() for o in self.add],
            "modify": [o.to_dict() for o in self.modify],
            "remove": [o.to_dict() for o in self.remove],
        }

    @classmethod
    def from_dict(cls, d: dict) -> OverridesData:
        return cls(
            add=[CandidateOverride.from_dict(o) for o in d.get("add", [])],
            modify=[CandidateOverride.from_dict(
                o) for o in d.get("modify", [])],
            remove=[CandidateOverride.from_dict(
                o) for o in d.get("remove", [])],
        )


def load_overrides(slug: str) -> OverridesData | None:
    """Load candidate overrides from candidates.override.json."""
    path = get_override_path(slug)
    if not path.exists():
        return None

    try:
        return OverridesData.from_dict(json.loads(path.read_text()))
    except json.JSONDecodeError:
        return None


def save_overrides(slug: str, data: OverridesData) -> Path:
    """Save candidate overrides to candidates.override.json."""
    path = get_override_path(slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data.to_dict(), indent=2) + "\n")
    return path


# ============================================================================
# Merged Candidates
# ============================================================================


@dataclass
class MergedCandidatesData:
    """Container for merged candidates with tracking metadata."""
    slug: str
    candidates: list[Candidate]
    generated_hash: str = ""
    override_hash: str = ""
    merged_hash: str = ""
    merged_at: str = ""

    def __post_init__(self):
        if not self.merged_at:
            self.merged_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "_meta": {
                "slug": self.slug,
                "generated_hash": self.generated_hash,
                "override_hash": self.override_hash,
                "merged_hash": self.merged_hash,
                "merged_at": self.merged_at,
            },
            "candidates": [c.to_dict() for c in self.candidates],
        }

    @classmethod
    def from_dict(cls, d: dict) -> MergedCandidatesData:
        meta = d.get("_meta", {})
        return cls(
            slug=meta.get("slug", ""),
            candidates=[Candidate.from_dict(c)
                        for c in d.get("candidates", [])],
            generated_hash=meta.get("generated_hash", ""),
            override_hash=meta.get("override_hash", ""),
            merged_hash=meta.get("merged_hash", ""),
            merged_at=meta.get("merged_at", ""),
        )


def compute_file_hash(path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def merge_candidates(slug: str) -> MergedCandidatesData:
    """Merge generated candidates with overrides.

    Merge semantics:
    - Override `add` entries are appended
    - Override `modify` entries update matching paths
    - Override `remove` entries filter out matching paths

    Validates that merged result has unique paths.
    """
    generated_data = load_generated_candidates(slug)
    overrides = load_overrides(slug)

    # Start with generated candidates
    if generated_data:
        candidates_by_path = {c.path: c for c in generated_data.candidates}
    else:
        candidates_by_path = {}

    # Apply overrides
    if overrides:
        # Remove first
        remove_paths = {o.path for o in overrides.remove}
        candidates_by_path = {
            path: c for path, c in candidates_by_path.items()
            if path not in remove_paths
        }

        # Modify existing
        for mod in overrides.modify:
            if mod.path in candidates_by_path:
                existing = candidates_by_path[mod.path]
                # Update only specified fields
                if mod.title:
                    existing.title = mod.title
                if mod.page_type:
                    existing.page_type = mod.page_type
                if mod.priority:
                    existing.priority = mod.priority

        # Add new
        for add in overrides.add:
            if add.path not in candidates_by_path:
                candidates_by_path[add.path] = Candidate(
                    title=add.title or Path(
                        add.path).stem.replace("-", " ").title(),
                    path=add.path,
                    page_type=add.page_type or "concept",
                    priority=add.priority or "should create",
                    claim_ids=[],
                    evidence_basis=add.reason,
                )

    # Compute hashes for tracking
    generated_hash = compute_file_hash(get_generated_candidates_path(slug))
    override_hash = compute_file_hash(get_override_path(slug))

    candidates = list(candidates_by_path.values())
    merged_content = json.dumps([c.to_dict()
                                for c in candidates], sort_keys=True)
    merged_hash = hashlib.sha256(merged_content.encode()).hexdigest()[:16]

    return MergedCandidatesData(
        slug=slug,
        candidates=candidates,
        generated_hash=generated_hash,
        override_hash=override_hash,
        merged_hash=merged_hash,
    )


def save_merged_candidates(slug: str, data: MergedCandidatesData) -> Path:
    """Save merged candidates to candidates.json."""
    path = get_candidates_path(slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data.to_dict(), indent=2) + "\n")
    return path


def load_merged_candidates(slug: str) -> MergedCandidatesData | None:
    """Load merged candidates from candidates.json."""
    path = get_candidates_path(slug)
    if not path.exists():
        return None

    try:
        return MergedCandidatesData.from_dict(json.loads(path.read_text()))
    except json.JSONDecodeError:
        return None


def is_candidates_stale(slug: str) -> bool:
    """Check if candidates.json needs to be regenerated.

    Returns True if:
    - candidates.json doesn't exist
    - generated or override files have changed since merge
    """
    merged = load_merged_candidates(slug)
    if merged is None:
        return True

    current_generated_hash = compute_file_hash(
        get_generated_candidates_path(slug))
    current_override_hash = compute_file_hash(get_override_path(slug))

    return (
        merged.generated_hash != current_generated_hash or
        merged.override_hash != current_override_hash
    )


# ============================================================================
# Validation
# ============================================================================


def validate_override_schema(data: dict) -> list[str]:
    """Validate candidates.override.json schema.

    Returns list of validation errors (empty if valid).
    """
    errors = []
    allowed_keys = {"add", "modify", "remove"}

    for key in data:
        if key not in allowed_keys:
            errors.append(f"Unknown key: {key}")

    for entry in data.get("add", []):
        if not isinstance(entry, dict):
            errors.append(f"add entry is not a dict: {entry}")
        elif "path" not in entry:
            errors.append(f"add entry missing 'path': {entry}")

    for entry in data.get("modify", []):
        if not isinstance(entry, dict):
            errors.append(f"modify entry is not a dict: {entry}")
        elif "path" not in entry:
            errors.append(f"modify entry missing 'path': {entry}")

    for entry in data.get("remove", []):
        if not isinstance(entry, dict):
            errors.append(f"remove entry is not a dict: {entry}")
        elif "path" not in entry:
            errors.append(f"remove entry missing 'path': {entry}")

    return errors


def validate_merged_candidates(data: MergedCandidatesData) -> list[str]:
    """Validate merged candidates have unique paths.

    Returns list of validation errors (empty if valid).
    """
    errors = []
    paths = [c.path for c in data.candidates]
    seen = set()
    for path in paths:
        if path in seen:
            errors.append(f"Duplicate candidate path: {path}")
        seen.add(path)
    return errors


if __name__ == "__main__":
    # Simple CLI for testing
    import argparse

    parser = argparse.ArgumentParser(description="Extraction state utilities")
    parser.add_argument("slug", help="Source slug")
    parser.add_argument("--raw-count", action="store_true",
                        help="Count raw claims")
    parser.add_argument("--merge", action="store_true",
                        help="Merge candidates")
    parser.add_argument("--check-stale", action="store_true",
                        help="Check if candidates are stale")
    args = parser.parse_args()

    if args.raw_count:
        count = count_raw_claims(args.slug)
        print(f"Raw claims: {count}")
    elif args.merge:
        data = merge_candidates(args.slug)
        save_merged_candidates(args.slug, data)
        print(f"Merged {len(data.candidates)} candidates")
        errors = validate_merged_candidates(data)
        if errors:
            for err in errors:
                print(f"  ERROR: {err}")
            sys.exit(1)
    elif args.check_stale:
        stale = is_candidates_stale(args.slug)
        print(f"Candidates stale: {stale}")
        sys.exit(0 if not stale else 1)
    else:
        # Show state summary
        state_dir = get_state_dir(args.slug)
        if not state_dir.exists():
            print(f"No extraction state for {args.slug}")
            sys.exit(1)

        print(f"Extraction state for {args.slug}:")
        print(f"  State dir: {state_dir}")
        print(f"  Raw claims: {count_raw_claims(args.slug)}")

        normalized = load_normalized_claims(args.slug)
        if normalized:
            print(f"  Normalized claims: {len(normalized.claims)}")
            print(f"  Topics: {len(normalized.topics)}")

        generated = load_generated_candidates(args.slug)
        if generated:
            print(f"  Generated candidates: {len(generated.candidates)}")

        merged = load_merged_candidates(args.slug)
        if merged:
            print(f"  Merged candidates: {len(merged.candidates)}")
            print(f"  Stale: {is_candidates_stale(args.slug)}")
