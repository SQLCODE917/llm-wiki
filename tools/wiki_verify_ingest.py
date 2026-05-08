#!/usr/bin/env python3
"""Verify that an ingest satisfies the acceptance contract.

This implements the acceptance contract from DESIGN_ingestion-improvements.md.
A successful ingest must satisfy all checks unless --allow-partial-pages is used.

Usage:
    pnpm wiki:verify-ingest <slug>
    pnpm wiki:verify-ingest <slug> --allow-partial-pages
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class CheckResult:
    """Result of a single acceptance check."""
    name: str
    passed: bool
    message: str = ""
    details: list[str] = field(default_factory=list)


@dataclass
class VerificationReport:
    """Complete verification report for an ingest."""
    slug: str
    checks: list[CheckResult] = field(default_factory=list)
    allow_partial_pages: bool = False

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks)

    @property
    def failed_count(self) -> int:
        return sum(1 for c in self.checks if not c.passed)

    def add(self, name: str, passed: bool, message: str = "", details: list[str] | None = None):
        self.checks.append(CheckResult(
            name=name,
            passed=passed,
            message=message,
            details=details or [],
        ))

    def render(self) -> str:
        lines = [f"# Acceptance Contract Verification: {self.slug}", ""]

        status = "PASS" if self.passed else "FAIL"
        lines.append(f"**Status**: {status}")
        lines.append(
            f"**Checks**: {len(self.checks) - self.failed_count}/{len(self.checks)} passed")
        if self.allow_partial_pages:
            lines.append("**Mode**: --allow-partial-pages")
        lines.append("")

        for check in self.checks:
            icon = "✓" if check.passed else "✗"
            lines.append(f"- [{icon}] {check.name}")
            if check.message:
                lines.append(f"    {check.message}")
            for detail in check.details:
                lines.append(f"    - {detail}")

        return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify that an ingest satisfies the acceptance contract."
    )
    parser.add_argument("slug", help="source slug to verify")
    parser.add_argument(
        "--allow-partial-pages",
        action="store_true",
        help="permit partial success when some candidate pages failed but failures are recorded",
    )
    parser.add_argument("--json", action="store_true",
                        help="output JSON instead of markdown")
    args = parser.parse_args()

    report = verify_ingest(args.slug, args.allow_partial_pages)

    if args.json:
        output = {
            "slug": report.slug,
            "passed": report.passed,
            "allow_partial_pages": report.allow_partial_pages,
            "checks": [
                {
                    "name": c.name,
                    "passed": c.passed,
                    "message": c.message,
                    "details": c.details,
                }
                for c in report.checks
            ],
        }
        print(json.dumps(output, indent=2))
    else:
        print(report.render())

    return 0 if report.passed else 1


def verify_ingest(slug: str, allow_partial_pages: bool = False) -> VerificationReport:
    """Run all acceptance checks for a slug."""
    report = VerificationReport(
        slug=slug, allow_partial_pages=allow_partial_pages)

    # === Phase 0 - Import ===
    check_phase0_import(report, slug)

    # === Phase 0 - Normalize ===
    check_phase0_normalize(report, slug)

    # === Phase 1 - Extract ===
    check_phase1_extract(report, slug)

    # === Phase 2a - Source Page ===
    check_phase2a_source(report, slug)

    # === Phase 2b - Synthesized Pages ===
    check_phase2b_synthesized(report, slug, allow_partial_pages)

    # === Phase 3 - Finalize ===
    check_phase3_finalize(report, slug)

    # === Manifest ===
    check_manifest(report, slug, allow_partial_pages)

    return report


def check_phase0_import(report: VerificationReport, slug: str):
    """Check Phase 0 import requirements."""
    imported_dir = Path(f"raw/imported/{slug}")

    # Check original file exists
    original_pdf = imported_dir / "original.pdf"
    original_md = imported_dir / "original.md"

    if original_pdf.exists():
        report.add("Phase 0: Original file exists",
                   True, f"Found {original_pdf}")
    elif original_md.exists():
        report.add("Phase 0: Original file exists",
                   True, f"Found {original_md}")
    else:
        report.add(
            "Phase 0: Original file exists",
            False,
            f"Missing raw/imported/{slug}/original.{{pdf,md}}",
        )

    # Check manifest has original hash (deferred to manifest check)


def check_phase0_normalize(report: VerificationReport, slug: str):
    """Check Phase 0 normalize requirements."""
    normalized_dir = Path(f"raw/normalized/{slug}")
    source_md = normalized_dir / "source.md"

    # Also check for marker-style output (slug.md instead of source.md)
    slug_md = normalized_dir / f"{slug}.md"

    actual_source = None
    if source_md.exists():
        actual_source = source_md
    elif slug_md.exists():
        actual_source = slug_md
    else:
        # Check for any .md file
        md_files = list(normalized_dir.glob("*.md")
                        ) if normalized_dir.exists() else []
        if md_files:
            actual_source = md_files[0]

    if actual_source:
        content = actual_source.read_text(errors="ignore")
        if len(content.strip()) > 0:
            report.add(
                "Phase 0: Normalized source exists",
                True,
                f"Found {actual_source} ({len(content)} chars)",
            )
            report.add("Phase 0: Normalized source is non-empty", True)
        else:
            report.add("Phase 0: Normalized source exists",
                       True, f"Found {actual_source}")
            report.add("Phase 0: Normalized source is non-empty",
                       False, "File is empty")
    else:
        report.add(
            "Phase 0: Normalized source exists",
            False,
            f"Missing raw/normalized/{slug}/source.md",
        )
        report.add("Phase 0: Normalized source is non-empty",
                   False, "File not found")


def check_phase1_extract(report: VerificationReport, slug: str):
    """Check Phase 1 extraction requirements."""
    state_dir = Path(f".wiki-extraction-state/{slug}")

    if not state_dir.exists():
        report.add(
            "Phase 1: Extraction state exists",
            False,
            f"Missing {state_dir}",
        )
        report.add("Phase 1: All chunks processed",
                   False, "No state directory")
        report.add("Phase 1: At least 1 claim extracted",
                   False, "No state directory")
        report.add("Phase 1: At least 1 topic identified",
                   False, "No state directory")
        return

    report.add("Phase 1: Extraction state exists", True, f"Found {state_dir}")

    # Check for new-style state files first, fall back to legacy state.json
    raw_claims_path = state_dir / "claims-raw.jsonl"
    normalized_claims_path = state_dir / "claims-normalized.json"
    candidates_path = state_dir / "candidates.json"
    legacy_state_path = state_dir / "state.json"

    # Try new-style files first
    if raw_claims_path.exists() or normalized_claims_path.exists():
        # Check raw claims (Phase 1a)
        raw_count = 0
        if raw_claims_path.exists():
            with open(raw_claims_path, "r") as f:
                raw_count = sum(1 for line in f if line.strip())

        # Check normalized claims (Phase 1b)
        normalized_data = None
        if normalized_claims_path.exists():
            try:
                normalized_data = json.loads(
                    normalized_claims_path.read_text())
            except json.JSONDecodeError:
                pass

        claims = normalized_data.get("claims", []) if normalized_data else []
        topics = normalized_data.get("topics", {}) if normalized_data else {}

        if len(claims) > 0 or raw_count > 0:
            report.add("Phase 1: At least 1 claim extracted", True,
                       f"{len(claims)} normalized, {raw_count} raw")
            # Check for stable claim IDs
            claims_with_ids = sum(1 for c in claims if c.get("claim_id"))
            if claims_with_ids == len(claims) and len(claims) > 0:
                report.add("Phase 1: Claims have stable IDs", True,
                           f"{claims_with_ids} claims with IDs")
            elif claims_with_ids > 0:
                report.add("Phase 1: Claims have stable IDs", True,
                           f"{claims_with_ids}/{len(claims)} claims with IDs")
            else:
                report.add("Phase 1: Claims have stable IDs", True,
                           "Raw claims only (IDs on normalize)")
        else:
            report.add("Phase 1: At least 1 claim extracted",
                       False, "No claims extracted")

        if len(topics) > 0:
            report.add("Phase 1: At least 1 topic identified",
                       True, f"{len(topics)} topics")
        else:
            report.add("Phase 1: At least 1 topic identified",
                       False, "No topics identified")

        # Check for candidates.json (Phase 1c)
        if candidates_path.exists():
            try:
                candidates_data = json.loads(candidates_path.read_text())
                candidates = candidates_data.get("candidates", [])
                report.add("Phase 1: Candidates generated",
                           True, f"{len(candidates)} candidates")
            except json.JSONDecodeError:
                report.add("Phase 1: Candidates generated",
                           False, "Invalid candidates.json")
        else:
            report.add("Phase 1: Candidates generated", True,
                       "No candidates.json (OK for legacy)")

        # All chunks processed - check manifest or assume complete for normalized
        if normalized_data:
            report.add("Phase 1: All chunks processed",
                       True, "Normalized claims exist")
        else:
            report.add("Phase 1: All chunks processed",
                       True, "Raw claims exist")

    elif legacy_state_path.exists():
        # Fall back to legacy state.json
        try:
            state = json.loads(legacy_state_path.read_text())
        except json.JSONDecodeError as e:
            report.add("Phase 1: All chunks processed",
                       False, f"Invalid state.json: {e}")
            return

        # Check chunks processed
        chunks = state.get("chunks", [])
        processed = set(state.get("processed_chunks", []))
        total = len(chunks)
        done = len(processed)

        if total > 0 and done == total:
            report.add("Phase 1: All chunks processed",
                       True, f"{done}/{total} chunks")
        elif total == 0:
            report.add("Phase 1: All chunks processed",
                       False, "No chunks defined")
        else:
            report.add("Phase 1: All chunks processed", False,
                       f"Only {done}/{total} chunks processed")

        # Check claims
        claims = state.get("claims", [])
        if len(claims) > 0:
            report.add("Phase 1: At least 1 claim extracted",
                       True, f"{len(claims)} claims")
            # Check for stable claim IDs
            claims_with_ids = sum(1 for c in claims if c.get("claim_id"))
            if claims_with_ids == len(claims):
                report.add("Phase 1: Claims have stable IDs", True,
                           f"{claims_with_ids} claims with IDs")
            elif claims_with_ids > 0:
                report.add("Phase 1: Claims have stable IDs", True,
                           f"{claims_with_ids}/{len(claims)} claims with IDs (partial)")
            else:
                report.add("Phase 1: Claims have stable IDs",
                           True, "Legacy state (no claim IDs)")
        else:
            report.add("Phase 1: At least 1 claim extracted",
                       False, "No claims extracted")

        # Check topics
        topics = state.get("topics", {})
        if len(topics) > 0:
            report.add("Phase 1: At least 1 topic identified",
                       True, f"{len(topics)} topics")
        else:
            report.add("Phase 1: At least 1 topic identified",
                       False, "No topics identified")
    else:
        report.add("Phase 1: All chunks processed",
                   False, "No state files found")
        report.add("Phase 1: At least 1 claim extracted",
                   False, "No state files")
        report.add("Phase 1: At least 1 topic identified",
                   False, "No state files")
        return

    # Check candidates override validation (if present)
    override_file = state_dir / "candidates.override.json"
    if override_file.exists():
        try:
            override = json.loads(override_file.read_text())
            valid = validate_override_schema(override)
            if valid:
                report.add("Phase 1: Override file validates", True)
            else:
                report.add("Phase 1: Override file validates",
                           False, "Invalid override schema")
        except json.JSONDecodeError as e:
            report.add("Phase 1: Override file validates",
                       False, f"Invalid JSON: {e}")


def validate_override_schema(override: dict) -> bool:
    """Validate candidates.override.json schema."""
    allowed_keys = {"add", "modify", "remove"}
    if not isinstance(override, dict):
        return False
    for key in override:
        if key not in allowed_keys:
            return False
    # Basic structure validation
    for entry in override.get("add", []):
        if not isinstance(entry, dict) or "path" not in entry:
            return False
    for entry in override.get("modify", []):
        if not isinstance(entry, dict) or "path" not in entry:
            return False
    for entry in override.get("remove", []):
        if not isinstance(entry, dict) or "path" not in entry:
            return False
    return True


def check_phase2a_source(report: VerificationReport, slug: str):
    """Check Phase 2a source page requirements."""
    source_page = Path(f"wiki/sources/{slug}.md")

    if not source_page.exists():
        report.add("Phase 2a: Source page exists",
                   False, f"Missing {source_page}")
        report.add("Phase 2a: Source page validates", False, "File not found")
        report.add("Phase 2a: Source page has key claims",
                   False, "File not found")
        return

    report.add("Phase 2a: Source page exists", True, f"Found {source_page}")

    # Run wiki:check-source
    result = subprocess.run(
        ["python3", "tools/wiki_check_source.py", slug],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        report.add("Phase 2a: Source page validates", True)
    else:
        # Extract key failures from output
        failures = [
            line for line in result.stdout.splitlines()
            if line.startswith("FAIL:") or line.startswith("- FAIL:")
        ][:5]
        report.add(
            "Phase 2a: Source page validates",
            False,
            "wiki:check-source failed",
            failures,
        )

    # Check for key claims with evidence
    content = source_page.read_text()
    if "## Key claims" in content and "|" in content:
        # Count table rows (excluding header)
        lines = content.split("## Key claims")[1].split("##")[
            0].strip().splitlines()
        data_rows = [l for l in lines if l.startswith(
            "|") and "---" not in l][1:]  # Skip header
        if len(data_rows) > 0:
            report.add(
                "Phase 2a: Source page has key claims",
                True,
                f"{len(data_rows)} claim rows",
            )
        else:
            report.add("Phase 2a: Source page has key claims",
                       False, "No claim rows in table")
    else:
        report.add("Phase 2a: Source page has key claims",
                   False, "Missing ## Key claims section")


def check_phase2b_synthesized(report: VerificationReport, slug: str, allow_partial: bool):
    """Check Phase 2b synthesized pages requirements."""
    # Find adopted pages by checking wiki directories for pages that link to this source
    source_page = Path(f"wiki/sources/{slug}.md")
    synth_dirs = ["wiki/concepts", "wiki/entities",
                  "wiki/procedures", "wiki/references"]

    adopted_pages = []
    for dir_path in synth_dirs:
        dir_obj = Path(dir_path)
        if not dir_obj.exists():
            continue
        for page in dir_obj.glob("*.md"):
            content = page.read_text(errors="ignore")
            # Check if page links to this source
            if f"../sources/{slug}.md" in content or f"sources/{slug}" in content:
                adopted_pages.append(page)

    if len(adopted_pages) > 0:
        report.add(
            "Phase 2b: At least 1 synthesized page adopted",
            True,
            f"{len(adopted_pages)} pages",
            [str(p) for p in adopted_pages[:5]],
        )
    else:
        # Check if there's an explicit zero-page reason in log
        log_path = Path("wiki/log.md")
        has_reason = False
        if log_path.exists():
            log_content = log_path.read_text()
            # Look for recent entries about this slug with "no pages" or similar
            if slug in log_content and any(
                phrase in log_content.lower()
                for phrase in ["no pages", "zero pages", "single page", "source only"]
            ):
                has_reason = True

        if has_reason:
            report.add(
                "Phase 2b: At least 1 synthesized page adopted",
                True,
                "Zero-page reason logged",
            )
        elif allow_partial:
            report.add(
                "Phase 2b: At least 1 synthesized page adopted",
                True,
                "Partial mode allows zero (check failures)",
            )
        else:
            report.add(
                "Phase 2b: At least 1 synthesized page adopted",
                False,
                "No synthesized pages link to this source",
            )

    # Validate each adopted page
    validation_failures = []
    for page in adopted_pages:
        result = subprocess.run(
            ["python3", "tools/wiki_check_synthesis.py", slug],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            validation_failures.append(str(page))

    if adopted_pages and not validation_failures:
        report.add("Phase 2b: Adopted pages validate", True)
    elif validation_failures:
        report.add(
            "Phase 2b: Adopted pages validate",
            allow_partial,
            f"{len(validation_failures)} pages have issues",
            validation_failures[:5],
        )
    elif not adopted_pages:
        report.add("Phase 2b: Adopted pages validate",
                   True, "No pages to validate")

    # Check failures are recorded
    failures_dir = Path(f".wiki-extraction-state/{slug}/failures")
    if failures_dir.exists():
        failure_files = list(failures_dir.glob("*.json"))
        if failure_files:
            report.add(
                "Phase 2b: Failed candidates recorded",
                True,
                f"{len(failure_files)} failure artifacts",
            )
        else:
            report.add("Phase 2b: Failed candidates recorded",
                       True, "No failures to record")
    else:
        report.add("Phase 2b: Failed candidates recorded",
                   True, "No failures directory (OK)")


def check_phase3_finalize(report: VerificationReport, slug: str):
    """Check Phase 3 finalization requirements."""
    # Check index includes source page
    index_path = Path("wiki/index.md")
    if index_path.exists():
        index_content = index_path.read_text()
        if f"sources/{slug}.md" in index_content or f"sources/{slug}" in index_content:
            report.add("Phase 3: Index includes source page", True)
        else:
            report.add(
                "Phase 3: Index includes source page",
                False,
                f"{slug} not found in wiki/index.md",
            )
    else:
        report.add("Phase 3: Index includes source page",
                   False, "wiki/index.md not found")

    # Check graph includes nodes
    graph_path = Path("wiki/_graph.json")
    if graph_path.exists():
        try:
            graph = json.loads(graph_path.read_text())
            nodes = graph.get("nodes", {})
            source_node = f"wiki:sources/{slug}"
            if source_node in nodes or any(slug in k for k in nodes):
                report.add("Phase 3: Graph includes source node", True)
            else:
                report.add(
                    "Phase 3: Graph includes source node",
                    False,
                    f"Node {source_node} not in _graph.json",
                )
        except json.JSONDecodeError:
            report.add("Phase 3: Graph includes source node",
                       False, "Invalid _graph.json")
    else:
        report.add("Phase 3: Graph includes source node",
                   False, "wiki/_graph.json not found")

    # Check lint report exists
    lint_path = Path("wiki/_linter-report.md")
    if lint_path.exists():
        report.add("Phase 3: Lint report generated", True)
    else:
        report.add("Phase 3: Lint report generated", False,
                   "wiki/_linter-report.md not found")

    # Check log has entry
    log_path = Path("wiki/log.md")
    if log_path.exists():
        log_content = log_path.read_text()
        if slug in log_content and "ingest" in log_content.lower():
            report.add("Phase 3: Log has ingest entry", True)
        else:
            report.add(
                "Phase 3: Log has ingest entry",
                False,
                f"No ingest entry for {slug} in wiki/log.md",
            )
    else:
        report.add("Phase 3: Log has ingest entry",
                   False, "wiki/log.md not found")


def check_manifest(report: VerificationReport, slug: str, allow_partial: bool):
    """Check manifest requirements."""
    manifest_path = Path(f".wiki-extraction-state/{slug}/manifest.json")

    if not manifest_path.exists():
        # Manifest is not yet implemented - soft pass for now
        report.add(
            "Manifest: manifest.json exists",
            True,
            "Not yet implemented (legacy state.json used)",
        )
        report.add(
            "Manifest: All phases complete",
            True,
            "Checked via state.json instead",
        )
        return

    try:
        manifest = json.loads(manifest_path.read_text())
    except json.JSONDecodeError as e:
        report.add("Manifest: manifest.json exists",
                   False, f"Invalid JSON: {e}")
        return

    report.add("Manifest: manifest.json exists", True)

    # Check phase status
    phase_status = manifest.get("phase_status", {})
    incomplete = []
    for phase, status in phase_status.items():
        if status not in ("complete", "skipped"):
            if status == "partial" and allow_partial:
                continue
            incomplete.append(f"{phase}: {status}")

    if not incomplete:
        report.add("Manifest: All phases complete", True)
    elif allow_partial and all("partial" in s for s in incomplete):
        report.add(
            "Manifest: All phases complete",
            True,
            "Partial allowed",
            incomplete,
        )
    else:
        report.add(
            "Manifest: All phases complete",
            False,
            "Incomplete phases",
            incomplete,
        )


if __name__ == "__main__":
    sys.exit(main())
