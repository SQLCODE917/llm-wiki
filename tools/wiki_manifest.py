#!/usr/bin/env python3
"""Artifact manifest for wiki ingestion pipeline.

This module provides manifest creation and tracking for the ingestion pipeline,
implementing the schema from DESIGN_ingestion-improvements.md.

The manifest tracks:
- Source file metadata and hashes
- Configuration used for ingest
- Phase status and progress
- Error information for debugging

Usage:
    from wiki_manifest import Manifest, PhaseStatus

    manifest = Manifest.create(slug, source_file, ...)
    manifest.set_phase_status("phase0_import", PhaseStatus.RUNNING)
    manifest.set_phase_status("phase0_import", PhaseStatus.COMPLETE)
    manifest.record_error("phase2b_synthesize", "Validation failed", artifact_path)
    manifest.save()
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1


class PhaseStatus(str, Enum):
    """Status values for ingest phases."""
    INITIALIZED = "initialized"  # Phase created but not started
    PENDING = "pending"          # Waiting for prerequisites
    RUNNING = "running"          # Currently executing
    COMPLETE = "complete"        # Finished successfully
    PARTIAL = "partial"          # Partially complete
    FAILED = "failed"            # Failed with error
    SKIPPED = "skipped"          # Explicitly skipped


PHASE_NAMES = [
    "phase0_import",
    "phase0_normalize",
    "phase1a_extract",
    "phase1b_dedupe",
    "phase1c_candidates",
    "phase2a_source",
    "phase2b_synthesize",
    "phase2c_adopt",
    "phase3a_index",
    "phase3b_graph",
    "phase3c_lint",
    "phase3d_log",
]


@dataclass
class ErrorInfo:
    """Compact error pointer for debugging."""
    phase: str
    message: str
    artifact: str | None = None
    occurred_at: str = ""

    def __post_init__(self):
        if not self.occurred_at:
            self.occurred_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "phase": self.phase,
            "message": self.message,
            "artifact": self.artifact,
            "occurred_at": self.occurred_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ErrorInfo:
        return cls(
            phase=data["phase"],
            message=data["message"],
            artifact=data.get("artifact"),
            occurred_at=data.get("occurred_at", ""),
        )


@dataclass
class Phase2Progress:
    """Progress tracking for Phase 2b synthesis."""
    total_candidates: int = 0
    synthesized: int = 0
    adopted: int = 0
    failed: int = 0
    pending: int = 0

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Phase2Progress:
        return cls(**data)


@dataclass
class Manifest:
    """Artifact manifest for wiki ingestion pipeline."""
    slug: str
    source_file: str | None
    source_kind: str
    command: str
    git_commit: str | None
    original_sha256: str | None
    normalized_sha256: str | None
    extractor: str
    structured: bool
    target_tokens: int
    render_pages: str
    model_backend: str
    candidate: str
    allow_partial_pages: bool
    partial_success_reason: str | None
    created_at: str
    updated_at: str
    paths: dict[str, str]
    phase_status: dict[str, str]
    phase2b_progress: Phase2Progress
    last_error: ErrorInfo | None = None

    # Internal state
    _state_dir: Path = field(default=Path("."), repr=False)

    @classmethod
    def create(
        cls,
        slug: str,
        source_file: Path | None = None,
        source_kind: str = "unknown",
        command: str = "",
        extractor: str = "pymupdf4llm",
        structured: bool = False,
        target_tokens: int = 3500,
        render_pages: str = "auto",
        model_backend: str = "bedrock",
        candidate: str = "local-4090",
        allow_partial_pages: bool = False,
    ) -> Manifest:
        """Create a new manifest for an ingest."""
        now = datetime.now(timezone.utc).isoformat()
        state_dir = Path(f".wiki-extraction-state/{slug}")

        # Initialize phase status
        phase_status = {
            name: PhaseStatus.PENDING.value for name in PHASE_NAMES}

        # Compute paths
        source_ext = source_file.suffix if source_file else ".pdf"
        paths = {
            "imported_original": f"raw/imported/{slug}/original{source_ext}",
            "normalized_source": f"raw/normalized/{slug}/source.md",
            "state_dir": str(state_dir),
            "source_page": f"wiki/sources/{slug}.md",
        }

        manifest = cls(
            slug=slug,
            source_file=str(source_file) if source_file else None,
            source_kind=source_kind,
            command=command,
            git_commit=get_git_commit(),
            original_sha256=None,
            normalized_sha256=None,
            extractor=extractor,
            structured=structured,
            target_tokens=target_tokens,
            render_pages=render_pages,
            model_backend=model_backend,
            candidate=candidate,
            allow_partial_pages=allow_partial_pages,
            partial_success_reason=None,
            created_at=now,
            updated_at=now,
            paths=paths,
            phase_status=phase_status,
            phase2b_progress=Phase2Progress(),
            last_error=None,
            _state_dir=state_dir,
        )
        return manifest

    @classmethod
    def load(cls, slug: str) -> Manifest | None:
        """Load an existing manifest from disk."""
        state_dir = Path(f".wiki-extraction-state/{slug}")
        manifest_path = state_dir / "manifest.json"

        if not manifest_path.exists():
            return None

        try:
            data = json.loads(manifest_path.read_text())
            return cls.from_dict(data, state_dir)
        except (json.JSONDecodeError, KeyError) as e:
            print(f"WARN: Failed to load manifest: {e}", file=sys.stderr)
            return None

    @classmethod
    def from_dict(cls, data: dict, state_dir: Path) -> Manifest:
        """Reconstruct manifest from dictionary."""
        phase2b_data = data.get("phase2b_progress", {})
        error_data = data.get("last_error")

        return cls(
            slug=data["slug"],
            source_file=data.get("source_file"),
            source_kind=data.get("source_kind", "unknown"),
            command=data.get("command", ""),
            git_commit=data.get("git_commit"),
            original_sha256=data.get("original_sha256"),
            normalized_sha256=data.get("normalized_sha256"),
            extractor=data.get("extractor", "unknown"),
            structured=data.get("structured", False),
            target_tokens=data.get("target_tokens", 3500),
            render_pages=data.get("render_pages", "auto"),
            model_backend=data.get("model_backend", "bedrock"),
            candidate=data.get("candidate", "local-4090"),
            allow_partial_pages=data.get("allow_partial_pages", False),
            partial_success_reason=data.get("partial_success_reason"),
            created_at=data.get("created_at", ""),
            updated_at=data.get("updated_at", ""),
            paths=data.get("paths", {}),
            phase_status=data.get("phase_status", {}),
            phase2b_progress=Phase2Progress.from_dict(
                phase2b_data) if phase2b_data else Phase2Progress(),
            last_error=ErrorInfo.from_dict(error_data) if error_data else None,
            _state_dir=state_dir,
        )

    def to_dict(self) -> dict:
        """Serialize manifest to dictionary."""
        return {
            "schema_version": SCHEMA_VERSION,
            "slug": self.slug,
            "source_file": self.source_file,
            "source_kind": self.source_kind,
            "command": self.command,
            "git_commit": self.git_commit,
            "original_sha256": self.original_sha256,
            "normalized_sha256": self.normalized_sha256,
            "extractor": self.extractor,
            "structured": self.structured,
            "target_tokens": self.target_tokens,
            "render_pages": self.render_pages,
            "model_backend": self.model_backend,
            "candidate": self.candidate,
            "allow_partial_pages": self.allow_partial_pages,
            "partial_success_reason": self.partial_success_reason,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "paths": self.paths,
            "phase_status": self.phase_status,
            "phase2b_progress": self.phase2b_progress.to_dict(),
            "last_error": self.last_error.to_dict() if self.last_error else None,
        }

    def save(self) -> Path:
        """Write manifest to disk."""
        self.updated_at = datetime.now(timezone.utc).isoformat()
        self._state_dir.mkdir(parents=True, exist_ok=True)
        manifest_path = self._state_dir / "manifest.json"
        manifest_path.write_text(json.dumps(self.to_dict(), indent=2) + "\n")
        return manifest_path

    def set_phase_status(self, phase: str, status: PhaseStatus) -> None:
        """Update status for a phase."""
        if phase not in PHASE_NAMES:
            raise ValueError(f"Unknown phase: {phase}")
        self.phase_status[phase] = status.value
        self.updated_at = datetime.now(timezone.utc).isoformat()

    def get_phase_status(self, phase: str) -> PhaseStatus:
        """Get current status for a phase."""
        return PhaseStatus(self.phase_status.get(phase, PhaseStatus.PENDING.value))

    def record_error(
        self,
        phase: str,
        message: str,
        artifact: str | None = None,
    ) -> None:
        """Record an error for debugging."""
        self.last_error = ErrorInfo(
            phase=phase,
            message=message,
            artifact=artifact,
        )
        self.set_phase_status(phase, PhaseStatus.FAILED)

    def clear_error(self) -> None:
        """Clear the last error."""
        self.last_error = None

    def update_phase2_progress(
        self,
        total: int | None = None,
        synthesized: int | None = None,
        adopted: int | None = None,
        failed: int | None = None,
        pending: int | None = None,
    ) -> None:
        """Update Phase 2b progress counters."""
        if total is not None:
            self.phase2b_progress.total_candidates = total
        if synthesized is not None:
            self.phase2b_progress.synthesized = synthesized
        if adopted is not None:
            self.phase2b_progress.adopted = adopted
        if failed is not None:
            self.phase2b_progress.failed = failed
        if pending is not None:
            self.phase2b_progress.pending = pending

    def set_original_hash(self, path: Path) -> None:
        """Compute and store hash of original file."""
        if path.exists():
            self.original_sha256 = compute_sha256(path)

    def set_normalized_hash(self, path: Path) -> None:
        """Compute and store hash of normalized source."""
        if path.exists():
            self.normalized_sha256 = compute_sha256(path)

    def is_phase_complete(self, phase: str) -> bool:
        """Check if a phase is complete."""
        status = self.get_phase_status(phase)
        return status in (PhaseStatus.COMPLETE, PhaseStatus.SKIPPED)

    def next_pending_phase(self) -> str | None:
        """Get the next phase that needs to run."""
        for phase in PHASE_NAMES:
            status = self.get_phase_status(phase)
            if status not in (PhaseStatus.COMPLETE, PhaseStatus.SKIPPED):
                return phase
        return None

    def all_phases_complete(self) -> bool:
        """Check if all phases are complete or skipped."""
        return all(
            self.is_phase_complete(phase)
            for phase in PHASE_NAMES
        )


def get_git_commit() -> str | None:
    """Get current git commit hash."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()[:12]
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def compute_sha256(path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def load_or_create_manifest(
    slug: str,
    source_file: Path | None = None,
    **kwargs,
) -> Manifest:
    """Load existing manifest or create a new one."""
    manifest = Manifest.load(slug)
    if manifest is not None:
        refresh_manifest_config(manifest, source_file, kwargs)
        return manifest
    return Manifest.create(slug, source_file, **kwargs)


def refresh_manifest_config(manifest: Manifest, source_file: Path | None, kwargs: dict) -> None:
    """Refresh rerun-sensitive manifest metadata without resetting phase state."""
    if source_file is not None:
        manifest.source_file = str(source_file)
        source_ext = source_file.suffix
        manifest.paths["imported_original"] = f"raw/imported/{manifest.slug}/original{source_ext}"
    for key in (
        "source_kind",
        "command",
        "extractor",
        "structured",
        "target_tokens",
        "render_pages",
        "model_backend",
        "candidate",
        "allow_partial_pages",
    ):
        if key in kwargs:
            setattr(manifest, key, kwargs[key])


def get_manifest_path(slug: str) -> Path:
    """Get the path to a manifest file."""
    return Path(f".wiki-extraction-state/{slug}/manifest.json")


if __name__ == "__main__":
    # Simple CLI for testing
    import sys
    if len(sys.argv) < 2:
        print("Usage: wiki_manifest.py <slug>")
        print("       wiki_manifest.py <slug> --create")
        sys.exit(1)

    slug = sys.argv[1]
    create = "--create" in sys.argv

    if create:
        manifest = Manifest.create(slug, command=" ".join(sys.argv))
        manifest.save()
        print(f"Created manifest: {get_manifest_path(slug)}")
    else:
        manifest = Manifest.load(slug)
        if manifest:
            print(json.dumps(manifest.to_dict(), indent=2))
        else:
            print(f"No manifest found for {slug}")
            sys.exit(1)
