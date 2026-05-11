#!/usr/bin/env python3
"""Failure artifact management for wiki ingestion pipeline.

This module implements structured failure tracking from DESIGN_ingestion-improvements.md.
Failed synthesis attempts are preserved for debugging and retry.

Location: `.wiki-extraction-state/<slug>/failures/<page-slug>.json`

Usage:
    from wiki_failure_artifacts import FailureArtifact, save_failure, list_failures

    failure = FailureArtifact.create(
        slug="javascriptallonge",
        candidate_page="../concepts/closures.md",
        draft_path=worktree / "wiki/concepts/closures.md",
    )
    failure.set_validation_result(passed=False, errors=[...])
    failure.set_judge_result(passed=False, verdicts=[...])
    save_failure(failure)

Commands:
    pnpm wiki:phase2-failures <slug>                    # List failed pages
    pnpm wiki:phase2-retry <slug> <page-slug>           # Retry one failed page
    pnpm wiki:phase2-clean-failures <slug> --older-than 30d
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any


# ============================================================================
# Data Structures
# ============================================================================


@dataclass
class ValidationError:
    """A single validation error."""
    type: str
    section: str = ""
    locator: str = ""
    claim_row: int = 0
    message: str = ""

    def to_dict(self) -> dict:
        d = {"type": self.type}
        if self.section:
            d["section"] = self.section
        if self.locator:
            d["locator"] = self.locator
        if self.claim_row:
            d["claim_row"] = self.claim_row
        if self.message:
            d["message"] = self.message
        return d

    @classmethod
    def from_dict(cls, d: dict) -> ValidationError:
        return cls(
            type=d.get("type", "unknown"),
            section=d.get("section", ""),
            locator=d.get("locator", ""),
            claim_row=d.get("claim_row", 0),
            message=d.get("message", ""),
        )


@dataclass
class ValidationResult:
    """Result of wiki page validation."""
    passed: bool
    errors: list[ValidationError] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "passed": self.passed,
            "errors": [e.to_dict() for e in self.errors],
        }

    @classmethod
    def from_dict(cls, d: dict) -> ValidationResult:
        return cls(
            passed=d.get("passed", False),
            errors=[ValidationError.from_dict(e) for e in d.get("errors", [])],
        )


@dataclass
class JudgeVerdict:
    """A single claim verdict from the judge."""
    claim_id: str
    verdict: str  # supported, not_supported, too_broad, partial
    reason: str = ""

    def to_dict(self) -> dict:
        return {
            "claim_id": self.claim_id,
            "verdict": self.verdict,
            "reason": self.reason,
        }

    @classmethod
    def from_dict(cls, d: dict) -> JudgeVerdict:
        return cls(
            claim_id=d.get("claim_id", ""),
            verdict=d.get("verdict", "unknown"),
            reason=d.get("reason", ""),
        )


@dataclass
class JudgeResult:
    """Result of claim judging."""
    passed: bool
    verdicts: list[JudgeVerdict] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "passed": self.passed,
            "verdicts": [v.to_dict() for v in self.verdicts],
        }

    @classmethod
    def from_dict(cls, d: dict) -> JudgeResult:
        return cls(
            passed=d.get("passed", False),
            verdicts=[JudgeVerdict.from_dict(v)
                      for v in d.get("verdicts", [])],
        )


# Allowed next_action values
NEXT_ACTIONS = {
    "retry",              # Attempt synthesis again with same or different model
    "inspect_manually",   # Requires human review of draft
    "suppress_candidate",  # Do not attempt this candidate again
    "needs_more_evidence",  # Candidate lacks sufficient source claims
}


@dataclass
class FailureArtifact:
    """Structured failure artifact for debugging and retry."""
    candidate_page: str
    attempted_at: str
    draft_path: str
    worktree_path: str
    validation_result: ValidationResult | None = None
    judge_result: JudgeResult | None = None
    repair_attempted: bool = False
    repair_result: str = ""  # success, partial, failed
    repair_errors_remaining: int = 0
    worktree_preserved: bool = False
    next_action: str = "retry"

    # Internal state
    slug: str = ""
    page_slug: str = ""

    @classmethod
    def create(
        cls,
        slug: str,
        candidate_page: str,
        draft_path: Path | str,
        worktree_path: Path | str = "",
    ) -> FailureArtifact:
        """Create a new failure artifact."""
        now = datetime.now(timezone.utc).isoformat()
        page_slug = Path(candidate_page).stem

        return cls(
            candidate_page=candidate_page,
            attempted_at=now,
            draft_path=str(draft_path),
            worktree_path=str(worktree_path),
            slug=slug,
            page_slug=page_slug,
        )

    def set_validation_result(
        self,
        passed: bool,
        errors: list[dict] | None = None,
    ) -> None:
        """Set validation result from check output."""
        validation_errors = []
        if errors:
            for e in errors:
                if isinstance(e, dict):
                    validation_errors.append(ValidationError.from_dict(e))
                elif isinstance(e, ValidationError):
                    validation_errors.append(e)
        self.validation_result = ValidationResult(
            passed=passed, errors=validation_errors)

    def set_judge_result(
        self,
        passed: bool,
        verdicts: list[dict] | None = None,
    ) -> None:
        """Set judge result from judge output."""
        judge_verdicts = []
        if verdicts:
            for v in verdicts:
                if isinstance(v, dict):
                    judge_verdicts.append(JudgeVerdict.from_dict(v))
                elif isinstance(v, JudgeVerdict):
                    judge_verdicts.append(v)
        self.judge_result = JudgeResult(passed=passed, verdicts=judge_verdicts)

    def set_repair_result(
        self,
        attempted: bool,
        result: str = "",
        errors_remaining: int = 0,
    ) -> None:
        """Record repair attempt result."""
        self.repair_attempted = attempted
        self.repair_result = result
        self.repair_errors_remaining = errors_remaining

    def to_dict(self) -> dict:
        """Serialize to dictionary for JSON."""
        return {
            "candidate_page": self.candidate_page,
            "attempted_at": self.attempted_at,
            "draft_path": self.draft_path,
            "worktree_path": self.worktree_path,
            "validation_result": self.validation_result.to_dict() if self.validation_result else None,
            "judge_result": self.judge_result.to_dict() if self.judge_result else None,
            "repair_attempted": self.repair_attempted,
            "repair_result": self.repair_result,
            "repair_errors_remaining": self.repair_errors_remaining,
            "worktree_preserved": self.worktree_preserved,
            "next_action": self.next_action,
        }

    @classmethod
    def from_dict(cls, d: dict, slug: str = "", page_slug: str = "") -> FailureArtifact:
        """Reconstruct from dictionary."""
        artifact = cls(
            candidate_page=d.get("candidate_page", ""),
            attempted_at=d.get("attempted_at", ""),
            draft_path=d.get("draft_path", ""),
            worktree_path=d.get("worktree_path", ""),
            repair_attempted=d.get("repair_attempted", False),
            repair_result=d.get("repair_result", ""),
            repair_errors_remaining=d.get("repair_errors_remaining", 0),
            worktree_preserved=d.get("worktree_preserved", False),
            next_action=d.get("next_action", "retry"),
            slug=slug,
            page_slug=page_slug or Path(d.get("candidate_page", "")).stem,
        )
        if d.get("validation_result"):
            artifact.validation_result = ValidationResult.from_dict(
                d["validation_result"])
        if d.get("judge_result"):
            artifact.judge_result = JudgeResult.from_dict(d["judge_result"])
        return artifact


# ============================================================================
# File Operations
# ============================================================================


def get_failures_dir(slug: str) -> Path:
    """Get the failures directory for a slug."""
    return Path(f".wiki-extraction-state/{slug}/failures")


def get_failure_path(slug: str, page_slug: str) -> Path:
    """Get the path to a specific failure artifact."""
    return get_failures_dir(slug) / f"{page_slug}.json"


def save_failure(artifact: FailureArtifact) -> Path:
    """Save a failure artifact to disk."""
    failures_dir = get_failures_dir(artifact.slug)
    failures_dir.mkdir(parents=True, exist_ok=True)

    failure_path = failures_dir / f"{artifact.page_slug}.json"
    failure_path.write_text(json.dumps(artifact.to_dict(), indent=2) + "\n")
    return failure_path


def load_failure(slug: str, page_slug: str) -> FailureArtifact | None:
    """Load a failure artifact from disk."""
    failure_path = get_failure_path(slug, page_slug)
    if not failure_path.exists():
        return None

    try:
        data = json.loads(failure_path.read_text())
        return FailureArtifact.from_dict(data, slug=slug, page_slug=page_slug)
    except json.JSONDecodeError:
        return None


def list_failures(slug: str) -> list[FailureArtifact]:
    """List all failure artifacts for a slug."""
    failures_dir = get_failures_dir(slug)
    if not failures_dir.exists():
        return []

    artifacts = []
    for path in failures_dir.glob("*.json"):
        page_slug = path.stem
        artifact = load_failure(slug, page_slug)
        if artifact:
            artifacts.append(artifact)

    # Sort by attempted_at (newest first)
    artifacts.sort(key=lambda a: a.attempted_at, reverse=True)
    return artifacts


def delete_failure(slug: str, page_slug: str) -> bool:
    """Delete a failure artifact."""
    failure_path = get_failure_path(slug, page_slug)
    if failure_path.exists():
        failure_path.unlink()
        return True
    return False


def clean_failures(slug: str, older_than_days: int = 30) -> int:
    """Delete failure artifacts older than specified days.

    Returns the number of failures deleted.
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=older_than_days)
    failures = list_failures(slug)
    deleted = 0

    for artifact in failures:
        try:
            attempted = datetime.fromisoformat(
                artifact.attempted_at.replace("Z", "+00:00"))
            if attempted < cutoff:
                if delete_failure(slug, artifact.page_slug):
                    deleted += 1
        except (ValueError, TypeError):
            # Skip artifacts with invalid timestamps
            continue

    return deleted


# ============================================================================
# Worktree Management
# ============================================================================


def get_worktree_path(slug: str, candidate_page: str) -> Path:
    """Get the standard worktree path for a candidate.

    Convention: .wiki-worktrees/<slug>-<page-type>-<page-slug>/

    This keeps worktrees organized by source slug, page type, and candidate name,
    preventing collisions when two candidates share the same slug under different
    directories (e.g., ../concepts/state.md vs ../references/state.md).
    """
    page_path = Path(candidate_page)
    page_slug = page_path.stem

    # Extract page type from path (concepts, references, entities, procedures)
    parts = page_path.parts
    page_type = "unknown"
    for part in parts:
        if part in ("concepts", "entities", "procedures", "references"):
            page_type = part
            break

    return Path(f".wiki-worktrees/{slug}-{page_type}-{page_slug}")


def preserve_worktree(
    temp_worktree: Path,
    slug: str,
    candidate_page: str,
) -> Path:
    """Copy a temp worktree to the standard location for preservation.

    Returns the path to the preserved worktree.
    """
    dest = get_worktree_path(slug, candidate_page)

    # Remove existing if present
    if dest.exists():
        shutil.rmtree(dest)

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(temp_worktree, dest)
    return dest


def cleanup_worktree(slug: str, candidate_page: str) -> bool:
    """Remove a preserved worktree."""
    worktree_path = get_worktree_path(slug, candidate_page)
    if worktree_path.exists():
        shutil.rmtree(worktree_path)
        return True
    return False


# ============================================================================
# CLI
# ============================================================================


def cmd_list(args: argparse.Namespace) -> int:
    """List failed pages for a slug."""
    failures = list_failures(args.slug)

    if not failures:
        print(f"No failures recorded for {args.slug}")
        return 0

    print(f"# Failures for {args.slug}: {len(failures)}")
    print()

    for artifact in failures:
        status_parts = []
        if artifact.validation_result and not artifact.validation_result.passed:
            status_parts.append(
                f"validation: {len(artifact.validation_result.errors)} errors")
        if artifact.judge_result and not artifact.judge_result.passed:
            failed_verdicts = sum(
                1 for v in artifact.judge_result.verdicts if v.verdict == "not_supported")
            status_parts.append(f"judge: {failed_verdicts} not_supported")
        status = ", ".join(status_parts) or "unknown"

        print(f"- **{artifact.page_slug}**")
        print(f"  - Candidate: {artifact.candidate_page}")
        print(f"  - Attempted: {artifact.attempted_at}")
        print(f"  - Status: {status}")
        print(f"  - Next action: {artifact.next_action}")
        if artifact.worktree_preserved:
            print(f"  - Worktree: {artifact.worktree_path}")
        print()

    return 0


def cmd_clean(args: argparse.Namespace) -> int:
    """Clean old failure artifacts."""
    if args.dry_run:
        failures = list_failures(args.slug)
        cutoff = datetime.now(timezone.utc) - timedelta(days=args.older_than)
        would_delete = 0
        for artifact in failures:
            try:
                attempted = datetime.fromisoformat(
                    artifact.attempted_at.replace("Z", "+00:00"))
                if attempted < cutoff:
                    would_delete += 1
                    print(
                        f"Would delete: {artifact.page_slug} ({artifact.attempted_at})")
            except (ValueError, TypeError):
                continue
        print(f"\nWould delete {would_delete} failure artifacts")
        return 0

    deleted = clean_failures(args.slug, args.older_than)
    print(
        f"Deleted {deleted} failure artifacts older than {args.older_than} days")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Manage Phase 2 failure artifacts."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # List command
    list_parser = subparsers.add_parser("list", help="List failed pages")
    list_parser.add_argument("slug", help="Source slug")

    # Clean command
    clean_parser = subparsers.add_parser(
        "clean", help="Clean old failure artifacts")
    clean_parser.add_argument("slug", help="Source slug")
    clean_parser.add_argument(
        "--older-than", type=int, default=30,
        help="Delete artifacts older than this many days (default: 30)"
    )
    clean_parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be deleted without deleting"
    )

    args = parser.parse_args()

    if args.command == "list":
        return cmd_list(args)
    elif args.command == "clean":
        return cmd_clean(args)

    return 1


if __name__ == "__main__":
    sys.exit(main())
