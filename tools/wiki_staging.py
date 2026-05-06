#!/usr/bin/env python3
"""Staging path support for Phase 2 synthesis.

Invalid pages never touch wiki/ - they stay in staging until validated.

Directory structure:
    .tmp/phase2/
    ├── pages/
    │   └── <slug>.json          # Schema WIP
    ├── rendered/
    │   └── <slug>.md            # Rendered WIP  
    ├── failed/
    │   └── <slug>-attempt-N.md  # Failed attempts
    └── stats/
        └── <slug>.json          # Context/token stats
"""
from __future__ import annotations

import json
import shutil
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path


@dataclass
class StagingPaths:
    """Paths for a single page in staging."""
    slug: str
    base: Path = field(default_factory=lambda: Path(".tmp/phase2"))

    @property
    def pages_dir(self) -> Path:
        return self.base / "pages"

    @property
    def rendered_dir(self) -> Path:
        return self.base / "rendered"

    @property
    def failed_dir(self) -> Path:
        return self.base / "failed"

    @property
    def stats_dir(self) -> Path:
        return self.base / "stats"

    @property
    def schema_path(self) -> Path:
        return self.pages_dir / f"{self.slug}.json"

    @property
    def rendered_path(self) -> Path:
        return self.rendered_dir / f"{self.slug}.md"

    @property
    def stats_path(self) -> Path:
        return self.stats_dir / f"{self.slug}.json"

    def failed_attempt_path(self, attempt: int) -> Path:
        return self.failed_dir / f"{self.slug}-attempt-{attempt}.md"

    def ensure_dirs(self) -> None:
        """Create staging directories if they don't exist."""
        for d in [self.pages_dir, self.rendered_dir, self.failed_dir, self.stats_dir]:
            d.mkdir(parents=True, exist_ok=True)


@dataclass
class ContextStats:
    """Statistics about context packing."""
    target_tokens: int = 0
    actual_tokens: int = 0
    evidence_tokens: int = 0
    excerpt_tokens: int = 0
    validator_tokens: int = 0
    neighbor_tokens: int = 0
    related_wiki_tokens: int = 0
    repair_tokens: int = 0
    dropped_sections: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class StagingResult:
    """Result of a staging operation."""
    success: bool
    schema_path: Path | None = None
    rendered_path: Path | None = None
    failed_path: Path | None = None
    stats: ContextStats | None = None
    message: str = ""


def stage_schema(
    staging: StagingPaths,
    schema: dict,
    stats: ContextStats | None = None,
) -> StagingResult:
    """Stage a page schema (JSON) for validation."""
    staging.ensure_dirs()

    try:
        staging.schema_path.write_text(json.dumps(schema, indent=2))

        if stats:
            staging.stats_path.write_text(
                json.dumps(stats.to_dict(), indent=2))

        return StagingResult(
            success=True,
            schema_path=staging.schema_path,
            stats=stats,
            message=f"Staged schema to {staging.schema_path}",
        )
    except Exception as e:
        return StagingResult(
            success=False,
            message=f"Failed to stage schema: {e}",
        )


def stage_rendered(
    staging: StagingPaths,
    markdown: str,
) -> StagingResult:
    """Stage rendered markdown for validation."""
    staging.ensure_dirs()

    try:
        staging.rendered_path.write_text(markdown)
        return StagingResult(
            success=True,
            rendered_path=staging.rendered_path,
            message=f"Staged rendered page to {staging.rendered_path}",
        )
    except Exception as e:
        return StagingResult(
            success=False,
            message=f"Failed to stage rendered page: {e}",
        )


def stage_failed_attempt(
    staging: StagingPaths,
    markdown: str,
    attempt: int,
) -> StagingResult:
    """Archive a failed attempt."""
    staging.ensure_dirs()

    path = staging.failed_attempt_path(attempt)
    try:
        path.write_text(markdown)
        return StagingResult(
            success=True,
            failed_path=path,
            message=f"Archived failed attempt to {path}",
        )
    except Exception as e:
        return StagingResult(
            success=False,
            message=f"Failed to archive attempt: {e}",
        )


def accept_page(
    staging: StagingPaths,
    target_path: Path,
    cleanup: bool = True,
) -> StagingResult:
    """Move validated page from staging to wiki.

    Only call this after validation passes.
    """
    if not staging.rendered_path.exists():
        return StagingResult(
            success=False,
            message=f"No rendered page at {staging.rendered_path}",
        )

    try:
        # Ensure target directory exists
        target_path.parent.mkdir(parents=True, exist_ok=True)

        # Copy (not move) so we keep staging for debugging
        shutil.copy2(staging.rendered_path, target_path)

        if cleanup:
            # Clean up staging files for this slug
            cleanup_staging(staging)

        return StagingResult(
            success=True,
            rendered_path=target_path,
            message=f"Accepted page to {target_path}",
        )
    except Exception as e:
        return StagingResult(
            success=False,
            message=f"Failed to accept page: {e}",
        )


def cleanup_staging(staging: StagingPaths) -> None:
    """Remove staging files for a slug after acceptance."""
    for path in [staging.schema_path, staging.rendered_path, staging.stats_path]:
        if path.exists():
            path.unlink()


def get_staging_stats(staging: StagingPaths) -> ContextStats | None:
    """Load context stats from staging."""
    if not staging.stats_path.exists():
        return None

    try:
        data = json.loads(staging.stats_path.read_text())
        return ContextStats(**data)
    except Exception:
        return None


def list_staged_pages(base: Path | None = None) -> list[str]:
    """List all page slugs currently in staging."""
    if base is None:
        base = Path(".tmp/phase2")

    pages_dir = base / "pages"
    if not pages_dir.exists():
        return []

    return sorted(p.stem for p in pages_dir.glob("*.json"))


def list_failed_attempts(staging: StagingPaths) -> list[Path]:
    """List all failed attempt files for a slug."""
    if not staging.failed_dir.exists():
        return []

    return sorted(staging.failed_dir.glob(f"{staging.slug}-attempt-*.md"))


@dataclass
class QuarantinedPage:
    """A page that failed validation after all repair attempts."""
    slug: str
    page_path: str
    reason: str
    failure_count: int
    failure_categories: list[str]
    last_attempt: str
    attempts: int

    def to_dict(self) -> dict:
        return asdict(self)


def quarantine_page(
    staging: StagingPaths,
    page_path: str,
    failures: list,  # list[ValidationFailure]
    attempts: int,
    quarantine_report_path: Path | None = None,
) -> QuarantinedPage:
    """Quarantine a page that can't be fixed.

    Records the page in the quarantine report for human review.
    """
    from wiki_failure_classifier import FailureCategory

    # Determine primary reason
    categories = [f.category for f in failures if hasattr(f, 'category')]

    if any(c == FailureCategory.TOO_FEW_CLAIMS for c in categories):
        reason = "insufficient_evidence"
    elif any(c == FailureCategory.LOCATOR_OUT_OF_RANGE for c in categories):
        reason = "evidence_outside_source_range"
    elif any(c == FailureCategory.UNSUPPORTED_CLAIM for c in categories):
        reason = "claims_not_grounded"
    elif any(c in [FailureCategory.CLAIM_COPIES_EVIDENCE, FailureCategory.WEAK_CLAIM_TEXT] for c in categories):
        reason = "semantic_quality"
    else:
        reason = "validation_failures"

    quarantined = QuarantinedPage(
        slug=staging.slug,
        page_path=page_path,
        reason=reason,
        failure_count=len(failures),
        failure_categories=[str(c.value) if hasattr(
            c, 'value') else str(c) for c in categories],
        last_attempt=datetime.now().isoformat(),
        attempts=attempts,
    )

    # Append to quarantine report
    if quarantine_report_path is None:
        quarantine_report_path = Path("wiki/_quarantine-report.md")

    append_to_quarantine_report(quarantine_report_path, quarantined, failures)

    return quarantined


def append_to_quarantine_report(
    report_path: Path,
    quarantined: QuarantinedPage,
    failures: list,
) -> None:
    """Append a quarantined page to the report."""
    if not report_path.exists():
        # Create header
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            "# Quarantined Pages\n\nPages that failed validation after all repair attempts.\n\n---\n\n")

    lines = [
        f"## {quarantined.page_path}",
        "",
        f"- **Slug**: {quarantined.slug}",
        f"- **Reason**: {quarantined.reason}",
        f"- **Attempts**: {quarantined.attempts}",
        f"- **Failures**: {quarantined.failure_count}",
        f"- **Timestamp**: {quarantined.last_attempt}",
        "",
        "### Failure details",
        "",
    ]

    for f in failures:
        msg = f.message if hasattr(f, 'message') else str(f)
        cat = f.category.value if hasattr(f, 'category') and hasattr(
            f.category, 'value') else "unknown"
        lines.append(f"- [{cat}] {msg}")

    lines.extend(["", "---", ""])

    with open(report_path, "a") as fp:
        fp.write("\n".join(lines))


def main() -> int:
    """CLI for staging operations."""
    import argparse

    parser = argparse.ArgumentParser(description="Staging path utilities")
    parser.add_argument("--list", action="store_true",
                        help="List staged pages")
    parser.add_argument("--cleanup", metavar="SLUG",
                        help="Cleanup staging for slug")
    parser.add_argument("--stats", metavar="SLUG", help="Show stats for slug")
    args = parser.parse_args()

    if args.list:
        for slug in list_staged_pages():
            print(slug)
        return 0

    if args.cleanup:
        staging = StagingPaths(slug=args.cleanup)
        cleanup_staging(staging)
        print(f"Cleaned up staging for {args.cleanup}")
        return 0

    if args.stats:
        staging = StagingPaths(slug=args.stats)
        stats = get_staging_stats(staging)
        if stats:
            print(json.dumps(stats.to_dict(), indent=2))
        else:
            print(f"No stats for {args.stats}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
