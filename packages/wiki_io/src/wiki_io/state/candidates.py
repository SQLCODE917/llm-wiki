"""Candidate page management for wiki extraction pipeline.

Handles storage and merging of page candidates:
- Generated candidates: Machine-proposed pages from claims (Phase 1c)
- Override candidates: Human curator modifications
- Merged candidates: Final list after applying overrides

Usage:
    from wiki_io.state.candidates import (
        Candidate,
        save_generated_candidates,
        load_generated_candidates,
        merge_candidates,
    )
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from wiki_io.state.paths import (
    get_generated_candidates_path,
    get_override_path,
    get_candidates_path,
    ensure_state_dir,
)


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


# ============================================================================
# Generated Candidates (Phase 1c)
# ============================================================================


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
    ensure_state_dir(slug)
    path = get_generated_candidates_path(slug)
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
    ensure_state_dir(slug)
    path = get_override_path(slug)
    path.write_text(json.dumps(data.to_dict(), indent=2) + "\n")
    return path


# ============================================================================
# Merged Candidates
# ============================================================================


def _compute_content_hash(content: str) -> str:
    """Compute a short hash of content for cache invalidation."""
    return hashlib.sha256(content.encode()).hexdigest()[:12]


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


def save_merged_candidates(slug: str, data: MergedCandidatesData) -> Path:
    """Save merged candidates to candidates.json."""
    ensure_state_dir(slug)
    path = get_candidates_path(slug)
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


def merge_candidates(slug: str) -> MergedCandidatesData | None:
    """Merge generated candidates with overrides.

    Returns None if there are no generated candidates.
    """
    generated = load_generated_candidates(slug)
    if generated is None:
        return None

    overrides = load_overrides(slug)

    # Start with generated candidates
    candidates_by_path = {c.path: c for c in generated.candidates}

    if overrides:
        # Apply removals
        remove_paths = {o.path for o in overrides.remove}
        candidates_by_path = {
            path: c for path, c in candidates_by_path.items()
            if path not in remove_paths
        }

        # Apply modifications
        for mod in overrides.modify:
            if mod.path in candidates_by_path:
                existing = candidates_by_path[mod.path]
                candidates_by_path[mod.path] = Candidate(
                    title=mod.title or existing.title,
                    path=existing.path,
                    page_type=mod.page_type or existing.page_type,
                    priority=mod.priority or existing.priority,
                    claim_ids=existing.claim_ids,
                    evidence_basis=existing.evidence_basis,
                    group=existing.group,
                    status=existing.status,
                )

        # Apply additions
        for add in overrides.add:
            candidates_by_path[add.path] = Candidate(
                title=add.title,
                path=add.path,
                page_type=add.page_type or "concept",
                priority=add.priority or "should create",
                claim_ids=[],
                evidence_basis="",
                group="",
                status="not created",
            )

    # Compute hashes for cache invalidation
    generated_path = get_generated_candidates_path(slug)
    override_path = get_override_path(slug)

    generated_hash = ""
    if generated_path.exists():
        generated_hash = _compute_content_hash(generated_path.read_text())

    override_hash = ""
    if override_path.exists():
        override_hash = _compute_content_hash(override_path.read_text())

    candidates = list(candidates_by_path.values())
    merged_content = json.dumps([c.to_dict()
                                for c in candidates], sort_keys=True)
    merged_hash = _compute_content_hash(merged_content)

    merged = MergedCandidatesData(
        slug=slug,
        candidates=candidates,
        generated_hash=generated_hash,
        override_hash=override_hash,
        merged_hash=merged_hash,
    )

    save_merged_candidates(slug, merged)
    return merged
