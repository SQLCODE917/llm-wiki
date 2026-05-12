#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path

# Import from refactored packages
from wiki_llm.backends import get_backend, ModelConfig
from wiki_llm.responses import parse_model_output, write_parsed_files
from wiki_page_schema import WikiPageSchema, parse_llm_response, parse_llm_response_structured, ParseResult, render_page, validate_schema
from wiki_phase1_benchmark import find_normalized_source, git_changed_files, init_git, parse_candidate, run_codex
from wiki_phase2_benchmark import (
    EvidenceBankResult,
    RelatedCandidate,
    build_evidence_bank,
    candidate_title,
    changed_status_path,
    existing_created_paths,
    is_runner_artifact,
    related_candidate_rows,
    render_prompt,
    render_repair_prompt,
    run_validation,
    range_page_args,
    source_relative_to_repo,
)
from wiki_fill_evidence import expand_evidence_ids, fill_evidence_in_page
from wiki_failure_classifier import (
    FailureCategory,
    FailureSeverity,
    ValidationFailure,
    parse_validation_output,
    group_failures_by_page,
    summarize_failures,
    DETERMINISTIC_CATEGORIES,
)
from wiki_failure_artifacts import (
    FailureArtifact,
    save_failure,
    preserve_worktree,
    get_worktree_path,
)
from wiki_context_packer import check_evidence_contract_violations
from wiki_deterministic_repair import repair_page as repair_page_schema
from wiki_check_synthesis import check_synthesis_structured
from wiki_deep_extract import Claim, extract_source_locator_map, get_heading_for_line


# ---------------------------------------------------------------------------
# Claim Selection / Clustering (v3 design: Task 3)
# ---------------------------------------------------------------------------

@dataclass
class ClaimSelectionReport:
    """Report of claim selection for audit trail."""
    total_claims: int
    selected_claims: int
    headings_total: int
    headings_covered: int
    selection_log: list[dict] = field(default_factory=list)

    def to_json(self) -> dict:
        return asdict(self)


def score_claim(claim: Claim) -> float:
    """
    Score a claim for specificity.
    Higher scores = more concrete/useful.

    Note: Coverage, novelty, and spread are handled via constraints
    in the selection loop, not as score components.
    """
    score = 0.0
    text = claim.claim.lower()
    evidence = claim.evidence.lower() if claim.evidence else ""

    # Contains numbers (concrete)
    if re.search(r'\d+', text):
        score += 0.15

    # Contains code (concrete)
    if re.search(r'`[^`]+`', claim.claim):
        score += 0.15

    # Technical terms
    if any(term in text for term in ['function', 'returns', 'parameter', 'argument', 'closure', 'scope']):
        score += 0.10

    # Substantial evidence
    if len(evidence) > 50:
        score += 0.10

    # Evidence contains code
    if re.search(r'`[^`]+`', evidence):
        score += 0.10

    return min(score, 1.0)


def is_redundant(claim: Claim, selected: list[Claim], threshold: float = 0.8) -> bool:
    """
    Check if claim is too similar to already-selected claims.
    Uses simple word overlap as novelty heuristic.
    """
    claim_words = set(claim.claim.lower().split())
    for existing in selected:
        existing_words = set(existing.claim.lower().split())
        if claim_words and existing_words:
            overlap = len(claim_words & existing_words) / \
                len(claim_words | existing_words)
            if overlap > threshold:
                return True
    return False


def get_nearest_heading(locator: str, locator_map: list[tuple[int, int, str]]) -> str:
    """
    Find the nearest source heading for a locator.

    Uses locator_map from extract_source_locator_map().
    """
    match = re.match(r'normalized:L(\d+)', locator)
    if not match:
        return "unknown"

    line = int(match.group(1))
    heading = get_heading_for_line(line, locator_map)
    return heading if heading else "unknown"


def select_representative_claims(
    claims: list[Claim],
    locator_map: list[tuple[int, int, str]],
    max_claims: int = 25,
    min_section_coverage: float = 0.6,
) -> tuple[list[Claim], ClaimSelectionReport]:
    """
    Select representative claims for synthesis.

    Two-pass algorithm:
    - Pass 1: Select for heading coverage until min_section_coverage is met.
    - Pass 2: Fill remaining slots by score, regardless of heading.

    Integration point: wiki_phase2_single.py, NOT wiki_deep_extract.py.
    Extraction remains responsible for extraction.
    Selection is a synthesis concern.

    Returns selected claims AND a report for audit.
    """
    # Score each claim for specificity
    scored = [(score_claim(c), c) for c in claims]
    scored.sort(reverse=True, key=lambda x: x[0])

    # Get source headings for coverage tracking
    headings = {c.locator: get_nearest_heading(
        c.locator, locator_map) for c in claims}
    total_headings = len(set(headings.values()) - {"unknown"})
    if total_headings == 0:
        total_headings = 1  # Avoid division by zero

    selected: list[Claim] = []
    covered_headings: set[str] = set()
    selection_log: list[dict] = []

    # Pass 1: Select for heading coverage
    for score, claim in scored:
        if len(selected) >= max_claims:
            break

        heading = headings.get(claim.locator, "unknown")
        coverage_ratio = len(covered_headings) / total_headings

        # In pass 1, only accept claims that add heading coverage
        is_new_heading = heading not in covered_headings and heading != "unknown"

        if is_new_heading:
            selected.append(claim)
            covered_headings.add(heading)
            selection_log.append({
                "claim": claim.claim[:50],
                "score": round(score, 3),
                "heading": heading,
                "pass": 1,
                "reason": "new_heading",
            })
        elif coverage_ratio < min_section_coverage:
            # Add even if not new heading, to fill coverage gap
            selected.append(claim)
            if heading != "unknown":
                covered_headings.add(heading)
            selection_log.append({
                "claim": claim.claim[:50],
                "score": round(score, 3),
                "heading": heading,
                "pass": 1,
                "reason": "coverage_gap",
            })

    # Pass 2: Fill remaining slots by score (regardless of heading)
    already_selected = set(id(c) for c in selected)
    for score, claim in scored:
        if len(selected) >= max_claims:
            break
        if id(claim) in already_selected:
            continue

        # Novelty check: skip if too similar to already-selected claim
        if is_redundant(claim, selected):
            continue

        heading = headings.get(claim.locator, "unknown")
        selected.append(claim)
        selection_log.append({
            "claim": claim.claim[:50],
            "score": round(score, 3),
            "heading": heading,
            "pass": 2,
            "reason": "fill_by_score",
        })

    report = ClaimSelectionReport(
        total_claims=len(claims),
        selected_claims=len(selected),
        headings_total=total_headings,
        headings_covered=len(covered_headings),
        selection_log=selection_log,
    )

    return selected, report


def cluster_by_heading(
    topic: str,
    claims: list[Claim],
    locator_map: list[tuple[int, int, str]],
    threshold: int = 50,
) -> dict[str, list[Claim]]:
    """
    Split large topics into subtopics based on source headings.

    Uses source headings as primary clustering signal, NOT locator windows.
    """
    if len(claims) < threshold:
        return {topic: claims}

    # Group by nearest source heading
    heading_groups: dict[str, list[Claim]] = defaultdict(list)
    for claim in claims:
        heading = get_nearest_heading(claim.locator, locator_map)
        heading_groups[heading].append(claim)

    # Dedupe similar claims within each heading group
    deduped_groups: dict[str, list[Claim]] = {}
    for heading, group_claims in heading_groups.items():
        deduped = dedupe_similar_claims(group_claims)
        if deduped:
            subtopic_name = f"{topic} - {heading}" if heading != "unknown" else topic
            deduped_groups[subtopic_name] = deduped

    return deduped_groups


def dedupe_similar_claims(claims: list[Claim], threshold: float = 0.9) -> list[Claim]:
    """Remove near-duplicate claims within a group."""
    if not claims:
        return []

    deduped = [claims[0]]
    for claim in claims[1:]:
        if not is_redundant(claim, deduped, threshold=threshold):
            deduped.append(claim)
    return deduped


def save_selection_report(
    slug: str,
    topic: str,
    report: ClaimSelectionReport,
    base_dir: Path | None = None,
) -> Path:
    """Persist selection report for audit trail."""
    if base_dir is None:
        base_dir = Path(".tmp/synthesis")

    # Sanitize topic for filename
    safe_topic = re.sub(r'[^\w\-]', '_', topic.lower())[:50]
    report_dir = base_dir / slug / safe_topic
    report_dir.mkdir(parents=True, exist_ok=True)

    report_path = report_dir / "claim_selection.json"
    report_path.write_text(json.dumps(report.to_json(), indent=2))
    return report_path


def load_locator_map(slug: str, normalized_source: Path) -> list[tuple[int, int, str]]:
    """Load or compute the source locator map for claim selection."""
    source_lines = normalized_source.read_text(errors="ignore").splitlines()
    return extract_source_locator_map(source_lines)


# ---------------------------------------------------------------------------
# Original code continues below
# ---------------------------------------------------------------------------

def quarantine_failed_page(
    worktree: Path,
    candidate_path: str,
    slug: str,
    validation_log: Path | None = None,
    log_paths: list[Path] | None = None,
    judge_report_paths: list[Path] | None = None,
    evidence_bank: str | None = None,
    validation_errors: list[dict] | None = None,
    judge_verdicts: list[dict] | None = None,
    validation_passed: bool = False,
    judge_passed: bool = False,
    repair_attempted: bool = False,
    repair_result: str = "",
    preserve_worktree_flag: bool = False,
) -> Path | None:
    """Copy failed page and all synthesis artifacts for post-mortem analysis.

    P4: Failed pages are quarantined instead of discarded, preserving
    the synthesis attempt for debugging and potential manual rescue.

    Artifacts preserved:
    - The rendered page itself
    - Validation log
    - All prompts and responses (from .tmp/model-runs/)
    - Judge reports
    - Evidence bank used
    - Structured failure artifact (JSON)

    Returns the quarantine path if successful, None otherwise.
    """
    # Resolve the page path relative to worktree
    rel_path = source_relative_to_repo(candidate_path)
    page_path = worktree / rel_path
    page_stem = Path(candidate_path).stem

    # Create quarantine directory in repo's .tmp (not worktree)
    # This survives both worktree cleanup and uningest
    quarantine_dir = Path(".tmp") / "synthesis-failures" / slug / page_stem
    quarantine_dir.mkdir(parents=True, exist_ok=True)

    # Copy the failed page if it exists
    quarantine_path = None
    if page_path.exists():
        quarantine_path = quarantine_dir / page_path.name
        shutil.copy2(page_path, quarantine_path)

    # Copy validation log if available
    if validation_log and validation_log.exists():
        log_dest = quarantine_dir / "validation.log"
        shutil.copy2(validation_log, log_dest)

    # Copy all model run logs (prompts, outputs, metadata)
    model_runs_dir = worktree / ".tmp" / "model-runs"
    if model_runs_dir.exists():
        for item in model_runs_dir.iterdir():
            if item.is_file():
                shutil.copy2(item, quarantine_dir / item.name)

    # Copy additional log paths that may be outside .tmp/model-runs/
    if log_paths:
        for log_path in log_paths:
            if log_path.exists() and log_path.is_file():
                dest = quarantine_dir / log_path.name
                if not dest.exists():  # Avoid overwriting
                    shutil.copy2(log_path, dest)

    # Copy judge reports
    if judge_report_paths:
        for report_path in judge_report_paths:
            if report_path.exists() and report_path.is_file():
                shutil.copy2(report_path, quarantine_dir / report_path.name)

    # Copy phase2-validation.log from worktree root
    phase2_val_log = worktree / "phase2-validation.log"
    if phase2_val_log.exists():
        shutil.copy2(phase2_val_log, quarantine_dir / "phase2-validation.log")

    # Save the evidence bank
    if evidence_bank:
        (quarantine_dir / "evidence-bank.md").write_text(evidence_bank)

    # Create structured failure artifact
    preserved_worktree_path = ""
    if preserve_worktree_flag:
        preserved_worktree_path = str(
            preserve_worktree(worktree, slug, candidate_path))

    failure = FailureArtifact.create(
        slug=slug,
        candidate_page=candidate_path,
        draft_path=str(quarantine_path) if quarantine_path else "",
        worktree_path=preserved_worktree_path,
    )
    failure.set_validation_result(
        passed=validation_passed, errors=validation_errors)
    failure.set_judge_result(passed=judge_passed, verdicts=judge_verdicts)
    failure.set_repair_result(
        attempted=repair_attempted,
        result=repair_result,
        errors_remaining=len(validation_errors or []
                             ) if not validation_passed else 0,
    )
    failure.worktree_preserved = bool(preserved_worktree_path)

    # Determine next action
    if judge_verdicts and any(v.get("verdict") == "not_supported" for v in judge_verdicts):
        failure.next_action = "needs_more_evidence"
    elif validation_errors and all(e.get("type") in ("missing_section", "bad_locator") for e in validation_errors):
        failure.next_action = "retry"
    else:
        failure.next_action = "retry"

    # Save the structured failure artifact
    save_failure(failure)

    # Write a summary file with metadata
    summary = [
        f"# Synthesis Failure: {page_stem}",
        f"",
        f"- Slug: {slug}",
        f"- Candidate: {candidate_path}",
        f"- Worktree: {worktree}",
        f"- Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Failure artifact: .wiki-extraction-state/{slug}/failures/{page_stem}.json",
        f"",
        f"## Files Preserved",
        f"",
    ]
    for item in sorted(quarantine_dir.iterdir()):
        summary.append(f"- {item.name}")
    (quarantine_dir / "FAILURE_SUMMARY.md").write_text("\n".join(summary) + "\n")

    return quarantine_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run one atomic Phase 2 synthesis task in a temp worktree.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument(
        "candidate_path", help="one Related pages candidate path, e.g. ../procedures/example.md")
    parser.add_argument("--candidate", default="local-4090",
                        help="local Codex candidate profile or profile:model")
    parser.add_argument("--normalized-source",
                        help="explicit normalized markdown path")
    parser.add_argument(
        "--prompt-template",
        default="auto",
        help="prompt template path, or 'auto' to choose by selected page type",
    )
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument(
        "--backend", help="Model backend: bedrock, codex, openai, anthropic. Default from WIKI_MODEL_BACKEND or codex")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--repair-attempts", type=int, default=1,
                        help="repair attempts after deterministic validation failures")
    parser.add_argument(
        "--judge-candidate", help="local Codex candidate for claim judging; defaults to --candidate")
    parser.add_argument("--judge-timeout", type=int, default=600)
    parser.add_argument("--judge-repair-attempts", type=int, default=1)
    parser.add_argument("--judge-batch", action="store_true",
                        help="judge all claim rows in one local-model call")
    parser.add_argument("--skip-judge", action="store_true",
                        help="only run deterministic validation")
    parser.add_argument("--strict-judge", action="store_true",
                        help="fail on too_broad verdicts (default: soft-pass accepts too_broad)")
    parser.add_argument(
        "--extraction-state",
        help="path to extraction state JSON (uses full evidence from claims instead of re-extracting)",
    )
    parser.add_argument("--json-output", action="store_true", default=True,
                        help="use JSON schema output format (default for backends)")
    parser.add_argument("--markdown-output", action="store_true",
                        help="use markdown output format (legacy, for codex CLI)")
    parser.add_argument(
        "--report", help="write a Markdown run report to this path")
    parser.add_argument("--keep", action="store_true",
                        help="keep temp worktree after the run")
    args = parser.parse_args()

    repo_root = Path.cwd()
    normalized_source = Path(
        args.normalized_source) if args.normalized_source else find_normalized_source(args.slug)
    if not normalized_source.exists():
        print(
            f"FAIL: normalized source does not exist: {normalized_source}", file=sys.stderr)
        return 2

    candidate_path = source_relative_candidate(args.candidate_path)

    candidate = parse_candidate(args.candidate)

    # Load extraction state claims if provided
    extraction_claims = None
    if args.extraction_state:
        extraction_state_path = Path(args.extraction_state)
        if extraction_state_path.exists():
            import json
            state_data = json.loads(extraction_state_path.read_text())
            extraction_claims = state_data.get("claims", [])
        else:
            print(
                f"WARN: extraction state not found: {extraction_state_path}", file=sys.stderr)

    # Use backend name in temp directory when not using codex
    backend_name = args.backend or os.environ.get(
        "WIKI_MODEL_BACKEND") or "codex"

    # JSON output is default for backends, markdown for codex CLI
    use_json = not args.markdown_output and backend_name != "codex"

    if backend_name != "codex":
        dir_label = backend_name
    else:
        dir_label = candidate.safe_label

    # Re-resolve prompt template with correct json setting
    prompt_template = resolve_prompt_template(
        candidate_path, args.prompt_template, json_output=use_json)
    if not prompt_template.exists():
        print(
            f"FAIL: prompt template does not exist: {prompt_template}", file=sys.stderr)
        return 2

    worktree = Path(tempfile.mkdtemp(
        prefix=f"llm-wiki-phase2-single-{args.slug}-{dir_label}.", dir="/tmp"))
    try:
        copy_repo_contents(repo_root, worktree)
        init_git(worktree)
        result = run_single_candidate(
            worktree=worktree,
            slug=args.slug,
            normalized_source=normalized_source,
            prompt_template=prompt_template,
            candidate_path=candidate_path,
            candidate=candidate,
            codex_bin=args.codex_bin,
            backend_name=args.backend,
            timeout=args.timeout,
            repair_attempts=args.repair_attempts,
            judge_candidate=args.judge_candidate or args.candidate,
            judge_timeout=args.judge_timeout,
            judge_repair_attempts=args.judge_repair_attempts,
            judge_batch=args.judge_batch,
            skip_judge=args.skip_judge,
            soft_pass=not args.strict_judge,
            extraction_claims=extraction_claims,
            json_output=use_json,
        )
        print_result(result)
        if args.report:
            write_report(Path(args.report), args.slug, candidate_path, result)

        # P4: Quarantine failed pages before cleanup
        success = result["validation_returncode"] == 0 and result["judge_returncode"] == 0
        if not success:
            validation_log = worktree / "validation.log"

            # Parse validation errors from log if available
            validation_errors = []
            if validation_log.exists():
                log_content = validation_log.read_text()
                for line in log_content.splitlines():
                    if "FAIL:" in line or "ERROR:" in line:
                        validation_errors.append({
                            "type": "validation_error",
                            "message": line.strip(),
                        })

            # Extract judge verdicts from report if available
            judge_verdicts = []
            for report_path in result.get("judge_report_paths", []):
                if report_path.exists():
                    try:
                        report_content = report_path.read_text()
                        # Try to parse JSON verdicts
                        import json as _json
                        if report_content.strip().startswith("{"):
                            report_data = _json.loads(report_content)
                            if "verdicts" in report_data:
                                judge_verdicts.extend(report_data["verdicts"])
                    except (ValueError, _json.JSONDecodeError):
                        pass

            quarantine_path = quarantine_failed_page(
                worktree, candidate_path, args.slug, validation_log,
                log_paths=result.get("log_paths", []),
                judge_report_paths=result.get("judge_report_paths", []),
                evidence_bank=result.get("evidence_bank"),
                validation_errors=validation_errors,
                judge_verdicts=judge_verdicts,
                validation_passed=(result["validation_returncode"] == 0),
                judge_passed=(result["judge_returncode"] == 0),
                repair_attempted=args.repair_attempts > 0,
                preserve_worktree_flag=args.keep,
            )
            if quarantine_path:
                print(
                    f"  Quarantined failed page to: .tmp/synthesis-failures/{args.slug}/{Path(candidate_path).stem}/")
                print(
                    f"  Failure artifact: .wiki-extraction-state/{args.slug}/failures/{Path(candidate_path).stem}.json")

        return 0 if success else 1
    finally:
        if not args.keep:
            shutil.rmtree(worktree, ignore_errors=True)


def copy_repo_contents(src: Path, dst: Path) -> None:
    from wiki_phase1_benchmark import copy_repo

    copy_repo(src, dst)


def resolve_prompt_template(candidate_path: str, raw_template: str, json_output: bool = False) -> Path:
    if raw_template != "auto":
        return Path(raw_template)
    if json_output:
        return Path("tools/prompts/phase2-synthesis-json.md")
    if source_relative_to_repo(candidate_path).startswith("wiki/references/"):
        return Path("tools/prompts/phase2-reference-synthesis.md")
    return Path("tools/prompts/phase2-synthesis.md")


def run_with_backend(
    *,
    worktree: Path,
    backend_name: str | None,
    candidate,
    prompt: str,
    timeout: int,
    prefix: str,
) -> tuple[int | None, list[Path]]:
    """Run synthesis using model backend abstraction.

    Returns:
        Tuple of (returncode, log_paths) compatible with run_codex output.
        returncode is 0 on success, 1 on failure, None on timeout.
    """
    from wiki_common import log_context_stats

    log_context_stats(prompt, label=f"{prefix} prompt")

    # Determine backend from env if not specified
    if backend_name is None:
        backend_name = os.environ.get("WIKI_MODEL_BACKEND", "codex")

    backend = get_backend(backend_name)
    config = ModelConfig(
        worktree=worktree,
        prefix=prefix,
        timeout=timeout,
        save_debug_files=True,
        system_prompt_style="synthesis",  # Use slim synthesis-focused prompt
        codex_profile=candidate.profile,
        codex_model=candidate.model,
    )

    response = backend.run(prompt, config)
    log_paths = list(response.log_paths)

    # Save response output for debugging
    output_path = worktree / f"{prefix}-output.md"
    output_path.write_text(response.output)
    log_paths.append(output_path)

    if not response.success:
        print(f"  Model error: {response.error}")
        return 1, log_paths

    # Parse and write files from response
    files = parse_model_output(response.output)
    if not files:
        print(f"  No files found in model output")
        # Save last-message for compatibility
        last_message_path = worktree / f"{prefix}-last-message.md"
        last_message_path.write_text(response.output)
        log_paths.append(last_message_path)
        return 1, log_paths

    print(f"  Parsed {len(files)} files from model output")
    written = write_parsed_files(files, worktree)

    # Save last-message for compatibility with existing code
    last_message_path = worktree / f"{prefix}-last-message.md"
    last_message_path.write_text(response.output)
    log_paths.append(last_message_path)

    return 0, log_paths


def attempt_deterministic_repairs(
    *,
    worktree: Path,
    slug: str,
    page_path: str,
    validation_log: Path,
    page_schema: WikiPageSchema | None,
    evidence_bank: EvidenceBankResult | None,
    normalized_source: Path | None = None,
    max_iterations: int = 3,
) -> tuple[bool, list[ValidationFailure]]:
    """Attempt deterministic repairs based on validation failures.

    This function runs repairs in a loop until:
    - No more deterministic repairs are possible
    - max_iterations is reached
    - Only LLM-requiring failures remain

    If page_schema is provided, uses schema-level repairs (more precise).
    Otherwise falls back to markdown-level repairs.

    Returns:
        Tuple of (any_repairs_made, remaining_failures)
    """
    any_repairs_made = False
    full_page_path = worktree / page_path

    for iteration in range(max_iterations):
        # Get structured failures
        failures = get_structured_failures(
            worktree, slug, validation_log, page_path, normalized_source
        )

        # Filter out runner artifacts that aren't real page issues
        failures = [
            f for f in failures
            if f.category != FailureCategory.FILE_SCOPE_VIOLATION
        ]

        if not failures:
            return any_repairs_made, []

        # Partition failures
        det_failures = [
            f for f in failures if f.category in DETERMINISTIC_CATEGORIES]
        llm_failures = [
            f for f in failures if f.category not in DETERMINISTIC_CATEGORIES]

        if not det_failures:
            if iteration == 0:
                print(
                    f"  No deterministic repairs possible ({len(llm_failures)} failures need LLM)")
            return any_repairs_made, llm_failures

        print(
            f"  Repair iteration {iteration + 1}: {len(det_failures)} deterministic, {len(llm_failures)} need LLM")

        # Attempt schema-level repairs if we have the schema
        repairs_this_iteration = False
        if page_schema is not None:
            repaired_schema, remaining = repair_page_schema(
                page_schema, det_failures, evidence_bank, slug
            )
            if repaired_schema is not page_schema:
                # Re-render the repaired schema
                markdown = render_page(repaired_schema, evidence_bank, slug)
                full_page_path.write_text(markdown)
                page_schema = repaired_schema
                repairs_this_iteration = True
                print(f"    Applied schema-level repairs")

        # Fall back to markdown-level repairs for anything not fixed
        if not repairs_this_iteration and full_page_path.exists():
            repairs_this_iteration = attempt_markdown_repairs(
                full_page_path, det_failures, slug, normalized_source
            )
            if repairs_this_iteration:
                print(f"    Applied markdown-level repairs")

        if repairs_this_iteration:
            any_repairs_made = True
        else:
            # No progress - avoid infinite loop
            return any_repairs_made, llm_failures

    # Max iterations reached
    return any_repairs_made, get_structured_failures(
        worktree, slug, validation_log, page_path, normalized_source
    )


def get_structured_failures(
    worktree: Path,
    slug: str,
    validation_log: Path,
    page_path: str,
    normalized_source: Path | None,
) -> list[ValidationFailure]:
    """Get structured failures from validation.

    Parses the validation log produced by running checks in the worktree context.
    The log is authoritative because it was generated with the correct paths.
    """
    # Parse the validation log (produced in worktree context)
    if validation_log.exists():
        return parse_validation_output(validation_log.read_text())

    return []


def attempt_markdown_repairs(
    page_path: Path,
    failures: list[ValidationFailure],
    slug: str,
    normalized_source: Path | None = None,
) -> bool:
    """Apply markdown-level repairs for deterministic failures.

    Returns True if any repairs were made.
    """
    if not page_path.exists():
        return False

    page_text = page_path.read_text()
    original_text = page_text
    repairs_made = False

    for failure in failures:
        if failure.category == FailureCategory.MISSING_SOURCE_LINK:
            if f"sources/{slug}.md" not in page_text:
                page_text = repair_missing_source_in_markdown(page_text, slug)
                repairs_made = True

        elif failure.category == FailureCategory.MISSING_SOURCE_SECTION:
            if "## Source pages" not in page_text and "## Sources" not in page_text:
                title = slug.replace("-", " ").title()
                page_text += f"\n\n## Source pages\n\n- [{title}](../sources/{slug}.md)\n"
                repairs_made = True

        elif failure.category == FailureCategory.MISSING_SOURCES_SECTION:
            if "## Source pages" not in page_text and "## Sources" not in page_text:
                title = slug.replace("-", " ").title()
                page_text += f"\n\n## Source pages\n\n- [{title}](../sources/{slug}.md)\n"
                repairs_made = True

        elif failure.category == FailureCategory.MISSING_SOURCE_BACKLINK:
            if f"../sources/{slug}.md" not in page_text:
                title = slug.replace("-", " ").title()
                # Add to Source pages section if it exists
                if "## Source pages" in page_text:
                    page_text = re.sub(
                        r"(## Source pages\s*\n)",
                        rf"\1\n- [{title}](../sources/{slug}.md)\n",
                        page_text,
                    )
                else:
                    page_text += f"\n\n## Source pages\n\n- [{title}](../sources/{slug}.md)\n"
                repairs_made = True

        elif failure.category == FailureCategory.PLACEHOLDER_TEXT:
            # Remove placeholder text patterns
            old_text = page_text
            page_text = re.sub(r"^.*Page title.*$", "",
                               page_text, flags=re.MULTILINE)
            page_text = re.sub(r"^.*Source-native group name.*$",
                               "", page_text, flags=re.MULTILINE)
            page_text = re.sub(r"^.*concrete evidence basis.*$",
                               "", page_text, flags=re.MULTILINE)
            if page_text != old_text:
                repairs_made = True

        elif failure.category == FailureCategory.BAD_SOURCE_CELL:
            title = slug.replace("-", " ").title()
            old_text = page_text
            page_text = re.sub(
                r"\|\s*\[?Source\]?\s*\|",
                f"| [{title}](../sources/{slug}.md) |",
                page_text,
            )
            if page_text != old_text:
                repairs_made = True

        elif failure.category == FailureCategory.WRONG_SOURCE_LINK:
            # Fix incorrect source links in tables
            title = slug.replace("-", " ").title()
            old_text = page_text
            # Replace generic "Source" links with proper source link
            page_text = re.sub(
                r"\[Source\]\([^)]+\.md\)",
                f"[{title}](../sources/{slug}.md)",
                page_text,
            )
            if page_text != old_text:
                repairs_made = True

        elif failure.category == FailureCategory.NON_ASCII_CHARS:
            # Normalize common non-ASCII characters
            old_text = page_text
            replacements = {
                "\u00a0": " ",   # non-breaking space
                "\u2010": "-",   # hyphen
                "\u2011": "-",   # non-breaking hyphen
                "\u2012": "-",   # figure dash
                "\u2013": "-",   # en dash
                "\u2014": "-",   # em dash
                "\u2015": "-",   # horizontal bar
                "\u2018": "'",   # left single quote
                "\u2019": "'",   # right single quote
                "\u201c": '"',   # left double quote
                "\u201d": '"',   # right double quote
                "\u2026": "...",  # ellipsis
            }
            for old, new in replacements.items():
                page_text = page_text.replace(old, new)
            if page_text != old_text:
                repairs_made = True

        elif failure.category == FailureCategory.STRAY_FRONTMATTER:
            # Remove stray frontmatter lines from body
            old_text = page_text
            # Only remove outside of YAML frontmatter block
            in_frontmatter = False
            lines = page_text.splitlines()
            new_lines = []
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    in_frontmatter = not in_frontmatter
                    new_lines.append(line)
                elif not in_frontmatter and re.match(
                    r"^(?:title|type|tags|status|last_updated|sources):\s*",
                    line.strip()
                ):
                    # Skip stray frontmatter line
                    continue
                else:
                    new_lines.append(line)
            page_text = "\n".join(new_lines)
            if page_text != old_text:
                repairs_made = True

        elif failure.category == FailureCategory.CANDIDATE_PAGE_EXISTS:
            # Convert candidate code format to link format
            old_text = page_text
            # Pattern: `../concepts/page.md` -> [../concepts/page.md](../concepts/page.md)
            page_text = re.sub(
                r'`(\.\./(?:concepts|entities|procedures|references)/[^`]+\.md)`',
                r'[\1](\1)',
                page_text,
            )
            if page_text != old_text:
                repairs_made = True

        elif failure.category == FailureCategory.EVIDENCE_NOT_IN_LOCATOR:
            # Evidence text doesn't match the locator - search nearby lines
            if normalized_source and normalized_source.exists() and failure.row:
                old_text = page_text
                page_text = repair_evidence_locator(
                    page_text, failure.row, normalized_source
                )
                if page_text != old_text:
                    repairs_made = True

        elif failure.category in (
            FailureCategory.REFERENCE_TO_UNCREATED,
            FailureCategory.BROKEN_LINK,
        ):
            # Move uncreated page references from Related pages to Candidate pages
            old_text = page_text
            page_text = repair_related_to_candidates_markdown(
                page_text, page_path)
            if page_text != old_text:
                repairs_made = True

    if repairs_made and page_text != original_text:
        page_path.write_text(page_text)
        return True

    return False


def repair_evidence_locator(
    page_text: str,
    row: int,
    normalized_source: Path,
) -> str:
    """Find correct locator for evidence row by searching normalized source.

    When evidence text doesn't match the cited locator, search nearby lines
    (and then the full document) to find where the text actually appears.
    """
    source_lines = normalized_source.read_text().splitlines()

    # Parse the evidence table
    table_match = re.search(
        r'\|\s*Claim\s*\|\s*Evidence\s*\|\s*Locator\s*\|\s*Source\s*\|'
        r'(.*?)(?=\n\n|\n##|\Z)',
        page_text,
        re.DOTALL | re.IGNORECASE
    )
    if not table_match:
        return page_text

    table_text = table_match.group(0)
    table_lines = [l for l in table_text.splitlines()
                   if l.strip().startswith('|')]

    # Skip header and separator (first 2 lines)
    data_rows = [l for l in table_lines[2:] if '---' not in l]

    if row < 1 or row > len(data_rows):
        return page_text

    row_text = data_rows[row - 1]

    # Parse the row: | Claim | Evidence | Locator | Source |
    cells = [c.strip() for c in row_text.split('|')]
    if len(cells) < 5:
        return page_text

    # 0=empty, 1=claim, 2=evidence, 3=locator, 4=source
    evidence_cell = cells[2]
    locator_cell = cells[3]

    # Extract evidence text (remove quotes)
    evidence_text = re.sub(r'^["\']|["\']$', '', evidence_cell.strip())
    if not evidence_text or evidence_text == "N/A":
        return page_text

    # Parse current locator to get starting point
    loc_match = re.search(r'L(\d+)(?:-L(\d+))?', locator_cell)
    original_line = 1
    if loc_match:
        original_line = int(loc_match.group(1))

    # Normalize for search
    def normalize(s: str) -> str:
        return re.sub(r'\s+', ' ', s.lower().strip())

    evidence_norm = normalize(evidence_text)

    # Search strategy: start from original locator line, expand outward
    # This prefers tighter ranges around the original locator
    max_distance = 20  # Max lines to search from original

    def find_evidence_range(start_idx: int) -> tuple[int, int] | None:
        """Try to find evidence starting from start_idx, return (start, end) 1-indexed or None."""
        for end_offset in range(1, 6):  # Try 1-5 lines
            if start_idx + end_offset > len(source_lines):
                break
            chunk = ' '.join(source_lines[start_idx:start_idx + end_offset])
            if evidence_norm in normalize(chunk):
                return (start_idx + 1, start_idx + end_offset)
        return None

    # Search outward from original line (prefer closer matches)
    for distance in range(max_distance + 1):
        # Try original line + distance
        for offset in ([0] if distance == 0 else [distance, -distance]):
            idx = original_line - 1 + offset  # 0-indexed
            if 0 <= idx < len(source_lines):
                result = find_evidence_range(idx)
                if result:
                    new_start, new_end = result
                    if new_start == new_end:
                        new_locator = f"`normalized:L{new_start}`"
                    else:
                        new_locator = f"`normalized:L{new_start}-L{new_end}`"

                    # Replace the locator in the row
                    old_locator_pattern = re.escape(locator_cell)
                    new_row = re.sub(old_locator_pattern,
                                     new_locator.strip('`'), row_text)
                    page_text = page_text.replace(row_text, new_row)
                    return page_text

    return page_text


def repair_missing_source_in_markdown(text: str, slug: str) -> str:
    """Add source page to frontmatter sources list."""
    source_path = f"../sources/{slug}.md"

    # Try to add to existing sources list
    sources_match = re.search(r"(sources:\s*\n(?:\s+-[^\n]+\n)*)", text)
    if sources_match:
        # Append to list
        old_block = sources_match.group(1)
        new_block = old_block.rstrip() + f"\n  - {source_path}\n"
        return text.replace(old_block, new_block)

    # Try to add sources: key after frontmatter opening
    if "sources:" not in text:
        text = re.sub(
            r"(---\n(?:.*\n)*?)(---)",
            rf"\1sources:\n  - {source_path}\n\2",
            text,
            count=1,
        )

    return text


def repair_related_to_candidates_markdown(page_text: str, page_path: Path) -> str:
    """Move uncreated page references from Related pages to Candidate pages in markdown.

    This handles two cases:
    1. "Page name (not created yet)" text references
    2. Markdown links to non-existent files

    Moves these to a Candidate pages section as plain text bullet points.
    """
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")
    not_created_pattern = re.compile(
        r"([^-\n]+?)\s*\(not created yet\)", re.IGNORECASE)

    # Find Related pages section
    related_match = re.search(
        r"(## Related pages\s*\n)(.*?)(?=\n## |\Z)",
        page_text,
        re.DOTALL | re.IGNORECASE
    )

    if not related_match:
        return page_text

    related_header = related_match.group(1)
    related_content = related_match.group(2)

    uncreated_pages: list[str] = []
    valid_lines: list[str] = []

    for line in related_content.splitlines():
        line_modified = line

        # Check for broken links (links to files that don't exist)
        for match in link_pattern.finditer(line):
            link_text, link_path = match.groups()
            # Resolve relative to the page's location
            target_path = (page_path.parent / link_path).resolve()

            if not target_path.exists():
                uncreated_pages.append(link_text.strip())
                # Remove the link from the line
                line_modified = line_modified.replace(
                    match.group(0), "").strip()

        # Check for "not created yet" patterns
        for match in not_created_pattern.finditer(line_modified):
            page_name = match.group(1).strip()
            # Clean up bullet point or list marker
            page_name = re.sub(r"^[-*]\s*", "", page_name).strip()
            if page_name:
                uncreated_pages.append(page_name)
            # Remove the pattern from the line
            line_modified = line_modified.replace(match.group(0), "").strip()

        # Keep line if it still has content
        line_modified = line_modified.strip()
        if line_modified and not re.match(r"^[-*•]\s*$", line_modified):
            valid_lines.append(line_modified)

    if not uncreated_pages:
        return page_text

    # Deduplicate uncreated pages
    seen = set()
    unique_uncreated = []
    for p in uncreated_pages:
        p_clean = p.strip()
        if p_clean and p_clean.lower() not in seen:
            seen.add(p_clean.lower())
            unique_uncreated.append(p_clean)

    # Build new Related pages content
    new_related_content = "\n".join(valid_lines) if valid_lines else "None."
    new_related_section = related_header + new_related_content

    # Replace Related pages section
    page_text = page_text[:related_match.start()] + \
        new_related_section + page_text[related_match.end():]

    # Build Candidate pages content
    candidate_bullets = "\n".join(f"- {p}" for p in unique_uncreated)

    # Check if Candidate pages section exists
    candidate_match = re.search(
        r"(## Candidate pages\s*\n)(.*?)(?=\n## |\Z)",
        page_text,
        re.DOTALL | re.IGNORECASE
    )

    if candidate_match:
        # Append to existing section
        old_content = candidate_match.group(2).strip()
        if old_content and old_content.lower() != "none.":
            new_content = old_content + "\n" + candidate_bullets
        else:
            new_content = candidate_bullets
        new_candidate = candidate_match.group(1) + new_content
        page_text = page_text[:candidate_match.start(
        )] + new_candidate + page_text[candidate_match.end():]
    else:
        # Insert new Candidate pages section after Related pages
        # Find updated Related pages section position
        related_match_new = re.search(
            r"(## Related pages\s*\n.*?)(?=\n## |\Z)",
            page_text,
            re.DOTALL | re.IGNORECASE
        )
        if related_match_new:
            insert_pos = related_match_new.end()
            new_candidate = f"\n\n## Candidate pages\n\n{candidate_bullets}\n"
            page_text = page_text[:insert_pos] + \
                new_candidate + page_text[insert_pos:]

    return page_text


def run_with_backend_json(
    *,
    worktree: Path,
    backend_name: str | None,
    candidate,
    prompt: str,
    timeout: int,
    prefix: str,
    evidence_bank: EvidenceBankResult,
    slug: str,
    expected_path: str,
) -> tuple[int | None, list[Path], WikiPageSchema | None]:
    """Run synthesis with JSON output mode.

    Model outputs JSON, we parse and render to markdown deterministically.

    Validation is split into phases:
    - Schema validation (pre-render): catches model errors
    - Render validation (post-render): catches renderer bugs

    Returns:
        Tuple of (returncode, log_paths, parsed_schema)
    """
    from wiki_common import log_context_stats
    from wiki_failure_classifier import FailureSeverity

    log_context_stats(prompt, label=f"{prefix} prompt")

    # Determine backend from env if not specified
    if backend_name is None:
        backend_name = os.environ.get("WIKI_MODEL_BACKEND", "codex")

    backend = get_backend(backend_name)
    config = ModelConfig(
        worktree=worktree,
        prefix=prefix,
        timeout=timeout,
        save_debug_files=True,
        system_prompt_style="synthesis-json",  # JSON output system prompt
        codex_profile=candidate.profile,
        codex_model=candidate.model,
    )

    response = backend.run(prompt, config)
    log_paths = list(response.log_paths)

    # Save raw response for debugging
    output_path = worktree / f"{prefix}-output.json"
    output_path.write_text(response.output)
    log_paths.append(output_path)

    if not response.success:
        print(f"  Model error: {response.error}")
        return 1, log_paths, None

    # Parse JSON and render markdown with structured validation
    result = parse_llm_response_structured(
        response.output, evidence_bank, slug)

    # Log schema validation issues (model errors)
    schema_errors = [
        f for f in result.schema_failures if f.severity == FailureSeverity.ERROR]
    schema_warnings = [
        f for f in result.schema_failures if f.severity == FailureSeverity.WARNING]

    if schema_errors:
        print(f"  Schema errors: {len(schema_errors)} (model issue)")
        for err in schema_errors:
            print(f"    - {err.field or err.category.value}: {err.message}")
        return 1, log_paths, result.schema

    if schema_warnings:
        print(f"  Schema warnings: {len(schema_warnings)}")
        for warn in schema_warnings:
            print(f"    - {warn.field or warn.category.value}: {warn.message}")

    if not result.markdown:
        print("  Failed to render markdown from JSON")
        return 1, log_paths, result.schema

    # Log render validation issues (renderer bugs - should never happen)
    if result.has_renderer_bugs:
        print(
            f"  RENDERER BUGS: {len(result.render_failures)} (code issue, not model)")
        for bug in result.render_failures:
            print(f"    - {bug.fix_hint or bug.message}")

    # Write the rendered markdown
    repo_path = source_relative_to_repo(expected_path)
    full_path = worktree / repo_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(result.markdown)
    print(f"  Rendered {repo_path} from JSON schema")

    return 0, log_paths, result.schema


def fix_synthesized_evidence(
    worktree: Path,
    page_path: str,
    normalized_source: Path,
    evidence_bank: EvidenceBankResult | None = None,
    slug: str = "",
) -> int:
    """Fill evidence cells deterministically from locators or evidence IDs.

    If evidence_bank is provided (with ID mapping), uses expand_evidence_ids
    to normalize model output to canonical 2-column stable-ID tables.

    Otherwise falls back to fill_evidence_in_page for legacy locator-based tables.

    Returns number of evidence cells filled.
    """
    full_page_path = worktree / page_path
    if not full_page_path.exists():
        return 0

    page_text = full_page_path.read_text()

    # Try evidence ID expansion first if we have a bank
    if evidence_bank and isinstance(evidence_bank, EvidenceBankResult) and evidence_bank.items:
        filled_text, changes = expand_evidence_ids(
            page_text, evidence_bank, slug)
        if changes:
            full_page_path.write_text(filled_text)
            print(
                f"Expanded {len(changes)} evidence ID(s) in {page_path}", file=sys.stderr)
            return len(changes)

    # Fall back to locator-based filling
    source_lines = normalized_source.read_text().splitlines()
    filled_text, changes = fill_evidence_in_page(page_text, source_lines)

    if changes:
        full_page_path.write_text(filled_text)
        print(
            f"Filled {len(changes)} evidence cell(s) in {page_path}", file=sys.stderr)

    return len(changes)


def run_single_candidate(
    *,
    worktree: Path,
    slug: str,
    normalized_source: Path,
    prompt_template: Path,
    candidate_path: str,
    candidate,
    codex_bin: str,
    backend_name: str | None,
    timeout: int,
    repair_attempts: int,
    judge_candidate: str,
    judge_timeout: int,
    judge_repair_attempts: int,
    judge_batch: bool,
    skip_judge: bool,
    soft_pass: bool = True,
    extraction_claims: list[dict] | None = None,
    json_output: bool = False,
) -> dict[str, object]:
    source_page = worktree / "wiki/sources" / f"{slug}.md"
    selected_candidate = find_related_candidate(source_page, candidate_path)
    existing_paths = existing_created_paths(source_page)
    if selected_candidate.path in existing_paths:
        raise SystemExit(
            f"candidate is already created: {selected_candidate.path}")

    selected_paths = [selected_candidate.path]
    allowed_paths = sorted(set(existing_paths + selected_paths))
    expected_total_pages = len(allowed_paths)

    # ---------------------------------------------------------------------------
    # Claim Selection (v3 design: Task 3)
    # For topics with many claims, select representative subset before synthesis.
    # ---------------------------------------------------------------------------
    selected_extraction_claims = extraction_claims
    selection_report: ClaimSelectionReport | None = None

    if extraction_claims:
        # Get topic name from candidate path (e.g., ../concepts/functions.md -> "Functions")
        topic_name = candidate_title(selected_candidate) or ""

        # Filter claims by topic
        topic_claims_dicts = [
            c for c in extraction_claims
            if c.get("topic", "").lower() == topic_name.lower()
        ]

        # Apply claim selection if we have many claims
        if len(topic_claims_dicts) > 25:
            print(
                f"  Claim selection: {len(topic_claims_dicts)} claims for topic '{topic_name}'")

            # Load locator map
            locator_map = load_locator_map(slug, normalized_source)

            # Convert dicts to Claim objects
            topic_claims = [Claim.from_dict(c) for c in topic_claims_dicts]

            # Select representative claims
            selected_claims, selection_report = select_representative_claims(
                topic_claims,
                locator_map,
                max_claims=25,
                min_section_coverage=0.6,
            )

            print(f"  Selected {len(selected_claims)}/{len(topic_claims)} claims "
                  f"({selection_report.headings_covered}/{selection_report.headings_total} headings)")

            # Save selection report
            report_path = save_selection_report(
                slug, topic_name, selection_report)
            print(f"  Selection report: {report_path}")

            # Convert back to dicts for evidence_bank
            selected_dicts = [c.to_dict() for c in selected_claims]

            # Replace topic claims in extraction_claims with selected subset
            other_claims = [
                c for c in extraction_claims
                if c.get("topic", "").lower() != topic_name.lower()
            ]
            selected_extraction_claims = other_claims + selected_dicts

    evidence_bank = build_evidence_bank(
        worktree, normalized_source, [selected_candidate],
        extraction_claims=selected_extraction_claims, use_ids=True, slug=slug)
    selected_repo_path = source_relative_to_repo(selected_candidate.path)
    prompt = render_prompt(
        template=(worktree / prompt_template).read_text(),
        slug=slug,
        normalized_source=normalized_source.as_posix(),
        min_pages=expected_total_pages,
        max_pages=expected_total_pages,
        existing_paths=existing_paths,
        selected_candidates=[selected_candidate],
        expected_total_pages=expected_total_pages,
        evidence_bank=evidence_bank.prompt_text if isinstance(
            evidence_bank, EvidenceBankResult) else evidence_bank,
        range_page_args=range_page_args(selected_paths),
    )

    start = time.monotonic()
    codex_returncodes: list[int | None] = []
    log_paths: list[Path] = []
    judge_report_paths: list[Path] = []
    page_schema: WikiPageSchema | None = None

    # Use the backend abstraction for cloud/API backends. Keep codex on the
    # Codex CLI path because it may edit files directly rather than returning
    # fenced file blocks for parse_model_output().
    effective_backend = backend_name or os.environ.get("WIKI_MODEL_BACKEND")
    use_backend = effective_backend not in (None, "", "codex")

    if json_output and use_backend:
        # JSON output mode: model outputs JSON, we render markdown
        returncode, paths, page_schema = run_with_backend_json(
            worktree=worktree,
            backend_name=backend_name,
            candidate=candidate,
            prompt=prompt,
            timeout=timeout,
            prefix="codex-initial",
            evidence_bank=evidence_bank if isinstance(
                evidence_bank, EvidenceBankResult) else EvidenceBankResult("", {}, {}),
            slug=slug,
            expected_path=selected_candidate.path,
        )
    elif use_backend:
        returncode, paths = run_with_backend(
            worktree=worktree,
            backend_name=backend_name,
            candidate=candidate,
            prompt=prompt,
            timeout=timeout,
            prefix="codex-initial",
        )
    else:
        returncode, paths = run_codex(
            worktree=worktree,
            candidate=candidate,
            codex_bin=codex_bin,
            prompt=prompt,
            timeout=timeout,
            prefix="codex-initial",
        )
    codex_returncodes.append(returncode)
    log_paths.extend(paths)

    # Check for evidence contract violations (model wrote forbidden fields)
    contract_violations: list[ValidationFailure] = []
    if not json_output:
        # For markdown output, check the written page for contract violations
        full_page_path = worktree / selected_repo_path
        if full_page_path.exists():
            page_text = full_page_path.read_text()
            contract_violations = check_evidence_contract_violations(
                page_text, selected_repo_path)
            if contract_violations:
                print(f"  Contract violations: {len(contract_violations)}")
                for v in contract_violations:
                    print(f"    - {v.message}")
                # Don't fail immediately - let evidence expansion try to fix it

    # Skip evidence expansion for JSON output mode (already rendered in markdown)
    if not json_output:
        fix_synthesized_evidence(
            worktree, selected_repo_path, worktree / normalized_source,
            evidence_bank=evidence_bank if isinstance(
                evidence_bank, EvidenceBankResult) else None,
            slug=slug,
        )

    validation_returncode = run_validation(
        worktree,
        slug,
        expected_total_pages,
        expected_total_pages,
        allowed_paths,
        normalized_source,
        range_paths=selected_paths,
    )

    # Try deterministic repairs before LLM repair loop
    if validation_returncode != 0:
        repairs_made, remaining_failures = attempt_deterministic_repairs(
            worktree=worktree,
            slug=slug,
            page_path=selected_repo_path,
            validation_log=worktree / "phase2-validation.log",
            page_schema=page_schema,
            evidence_bank=evidence_bank if isinstance(
                evidence_bank, EvidenceBankResult) else None,
            normalized_source=worktree / normalized_source,
        )
        if repairs_made:
            # Re-validate after deterministic repairs
            validation_returncode = run_validation(
                worktree,
                slug,
                expected_total_pages,
                expected_total_pages,
                allowed_paths,
                normalized_source,
                range_paths=selected_paths,
            )

    for attempt in range(1, repair_attempts + 1):
        if validation_returncode == 0:
            break
        validation_output = (worktree / "phase2-validation.log").read_text()
        hints = claim_repair_hints(
            worktree, selected_repo_path, normalized_source)
        if is_reference_candidate(selected_candidate.path):
            repair_prompt = render_reference_repair_prompt(
                slug=slug,
                selected_candidate=selected_candidate,
                selected_repo_path=selected_repo_path,
                existing_paths=existing_paths,
                expected_total_pages=expected_total_pages,
                normalized_source=normalized_source,
                evidence_bank=evidence_bank,
                validation_output=validation_output,
                claim_hints=hints,
            )
        else:
            repair_prompt = render_repair_prompt(
                slug=slug,
                validation_output=validation_output,
                min_pages=expected_total_pages,
                max_pages=expected_total_pages,
                selected_candidates=[selected_candidate],
                existing_paths=existing_paths,
                normalized_source=normalized_source,
                evidence_bank=evidence_bank,
            )
            repair_prompt = append_claim_repair_hints(repair_prompt, hints)

        # Use JSON mode for repairs too if initial was JSON
        if json_output and use_backend:
            returncode, paths, _ = run_with_backend_json(
                worktree=worktree,
                backend_name=backend_name,
                candidate=candidate,
                prompt=repair_prompt,
                timeout=timeout,
                prefix=f"codex-repair-{attempt}",
                evidence_bank=evidence_bank if isinstance(
                    evidence_bank, EvidenceBankResult) else EvidenceBankResult("", {}, {}),
                slug=slug,
                expected_path=selected_candidate.path,
            )
        elif use_backend:
            returncode, paths = run_with_backend(
                worktree=worktree,
                backend_name=backend_name,
                candidate=candidate,
                prompt=repair_prompt,
                timeout=timeout,
                prefix=f"codex-repair-{attempt}",
            )
        else:
            returncode, paths = run_codex(
                worktree=worktree,
                candidate=candidate,
                codex_bin=codex_bin,
                prompt=repair_prompt,
                timeout=timeout,
                prefix=f"codex-repair-{attempt}",
            )
        codex_returncodes.append(returncode)
        log_paths.extend(paths)

        # Skip evidence expansion for JSON output mode (already rendered in markdown)
        if not json_output:
            fix_synthesized_evidence(
                worktree, selected_repo_path, worktree / normalized_source,
                evidence_bank=evidence_bank if isinstance(
                    evidence_bank, EvidenceBankResult) else None,
                slug=slug,
            )

        validation_returncode = run_validation(
            worktree,
            slug,
            expected_total_pages,
            expected_total_pages,
            allowed_paths,
            normalized_source,
            range_paths=selected_paths,
        )

    judge_returncode = 0
    if validation_returncode == 0 and not skip_judge:
        judge_returncode, judge_report, reports = run_judge_with_optional_row_fallback(
            worktree=worktree,
            page=selected_repo_path,
            normalized_source=normalized_source,
            backend_name=backend_name,
            judge_candidate=judge_candidate,
            codex_bin=codex_bin,
            timeout=judge_timeout,
            batch=judge_batch,
            prefix="phase2-judge",
            soft_pass=soft_pass,
        )
        judge_report_paths.extend(reports)

        # Patch 3: Sticky initial synthesis - skip repair if only "too_broad" verdicts
        # "too_broad" from vocabulary differences is often a false positive
        # Only repair if there are genuine "not_supported" verdicts
        should_repair = should_run_judge_repair(
            judge_report) if judge_returncode != 0 else False

        for attempt in range(1, judge_repair_attempts + 1):
            if judge_returncode == 0 or not should_repair:
                break
            repair_prompt = render_judge_repair_prompt(
                slug=slug,
                selected_candidate=selected_candidate,
                selected_repo_path=selected_repo_path,
                existing_paths=existing_paths,
                expected_total_pages=expected_total_pages,
                normalized_source=normalized_source,
                evidence_bank=evidence_bank,
                judge_report=judge_report.read_text(
                    errors="ignore") if judge_report.exists() else "missing judge report",
                judge_candidate=judge_candidate,
            )
            repair_prompt = append_claim_repair_hints(
                repair_prompt,
                claim_repair_hints(
                    worktree, selected_repo_path, normalized_source),
            )

            # Use JSON mode for judge-repairs too if initial was JSON
            if json_output and use_backend:
                returncode, paths, _ = run_with_backend_json(
                    worktree=worktree,
                    backend_name=backend_name,
                    candidate=candidate,
                    prompt=repair_prompt,
                    timeout=timeout,
                    prefix=f"codex-judge-repair-{attempt}",
                    evidence_bank=evidence_bank if isinstance(
                        evidence_bank, EvidenceBankResult) else EvidenceBankResult("", {}, {}),
                    slug=slug,
                    expected_path=selected_candidate.path,
                )
            elif use_backend:
                returncode, paths = run_with_backend(
                    worktree=worktree,
                    backend_name=backend_name,
                    candidate=candidate,
                    prompt=repair_prompt,
                    timeout=timeout,
                    prefix=f"codex-judge-repair-{attempt}",
                )
            else:
                returncode, paths = run_codex(
                    worktree=worktree,
                    candidate=candidate,
                    codex_bin=codex_bin,
                    prompt=repair_prompt,
                    timeout=timeout,
                    prefix=f"codex-judge-repair-{attempt}",
                )
            codex_returncodes.append(returncode)
            log_paths.extend(paths)

            # Skip evidence expansion for JSON output mode (already rendered in markdown)
            if not json_output:
                fix_synthesized_evidence(
                    worktree, selected_repo_path, worktree / normalized_source,
                    evidence_bank=evidence_bank if isinstance(
                        evidence_bank, EvidenceBankResult) else None,
                    slug=slug,
                )

            validation_returncode = run_validation(
                worktree,
                slug,
                expected_total_pages,
                expected_total_pages,
                allowed_paths,
                normalized_source,
                range_paths=selected_paths,
            )
            if validation_returncode != 0:
                judge_returncode = 1
                break
            judge_returncode, judge_report, reports = run_judge_with_optional_row_fallback(
                worktree=worktree,
                page=selected_repo_path,
                normalized_source=normalized_source,
                backend_name=backend_name,
                judge_candidate=judge_candidate,
                codex_bin=codex_bin,
                timeout=judge_timeout,
                batch=judge_batch,
                prefix=f"phase2-judge-repair-{attempt}",
                soft_pass=soft_pass,
            )
            judge_report_paths.extend(reports)
    elif validation_returncode != 0:
        judge_returncode = 1

    # Use backend name as label when not using codex
    result_label = backend_name if backend_name and backend_name != "codex" else candidate.label

    return {
        "candidate": result_label,
        "worktree": worktree,
        "duration_s": time.monotonic() - start,
        "codex_returncodes": codex_returncodes,
        "validation_returncode": validation_returncode,
        "judge_returncode": judge_returncode,
        "changed_files": phase2_changed_files(worktree),
        "log_paths": log_paths,
        "judge_report_paths": judge_report_paths,
        "evidence_bank": evidence_bank.prompt_text if isinstance(evidence_bank, EvidenceBankResult) else evidence_bank,
    }


def phase2_changed_files(worktree: Path) -> list[str]:
    out: list[str] = []
    for changed in git_changed_files(worktree):
        path = changed_status_path(changed)
        if path and is_runner_artifact(path):
            continue
        out.append(changed)
    return out


def run_judge(
    *,
    worktree: Path,
    page: str,
    normalized_source: Path,
    backend_name: str | None,
    judge_candidate: str | None,
    codex_bin: str,
    timeout: int,
    batch: bool,
    prefix: str,
    soft_pass: bool = True,  # Default: accept too_broad, only fail on not_supported
) -> tuple[int, Path]:
    output = worktree / f"{prefix}-{Path(page).stem}.md"
    command = [
        "python3",
        "tools/wiki_judge_claims.py",
        page,
        "--normalized-source",
        normalized_source.as_posix(),
        "--timeout",
        str(timeout),
        "--output",
        output.as_posix(),
        "--fail-on-issues",
    ]
    if soft_pass:
        command.append("--soft-pass")
    # Use backend if specified, otherwise fall back to codex with candidate
    if backend_name:
        command.extend(["--backend", backend_name])
    if judge_candidate:
        command.extend(["--candidate", judge_candidate])
    if codex_bin != "codex":
        command.extend(["--codex-bin", codex_bin])
    if batch:
        command.append("--batch")
    completed = subprocess.run(
        command,
        cwd=worktree,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    (worktree / f"{prefix}.log").write_text("$ " +
                                            " ".join(command) + "\n" + completed.stdout)
    return completed.returncode, output


def run_judge_with_optional_row_fallback(
    *,
    worktree: Path,
    page: str,
    normalized_source: Path,
    backend_name: str | None,
    judge_candidate: str | None,
    codex_bin: str,
    timeout: int,
    batch: bool,
    prefix: str,
    soft_pass: bool = True,
) -> tuple[int, Path, list[Path]]:
    returncode, report = run_judge(
        worktree=worktree,
        page=page,
        normalized_source=normalized_source,
        backend_name=backend_name,
        judge_candidate=judge_candidate,
        codex_bin=codex_bin,
        timeout=timeout,
        batch=batch,
        prefix=prefix,
        soft_pass=soft_pass,
    )
    reports = [report]
    if not batch or returncode == 0 or not should_retry_batch_judge_rowwise(report):
        return returncode, report, reports

    rowwise_returncode, rowwise_report = run_judge(
        worktree=worktree,
        page=page,
        normalized_source=normalized_source,
        backend_name=backend_name,
        judge_candidate=judge_candidate,
        codex_bin=codex_bin,
        timeout=timeout,
        batch=False,
        prefix=f"{prefix}-rowwise",
        soft_pass=soft_pass,
    )
    reports.append(rowwise_report)
    return rowwise_returncode, rowwise_report, reports


def should_retry_batch_judge_rowwise(report: Path) -> bool:
    if not report.exists():
        return False
    text = report.read_text(errors="ignore").lower()
    batch_format_errors = [
        "local judge did not return a json object",
        "local judge json was not an object",
        "local judge json missing claim_results list",
        "local judge returned invalid page_verdict",
        "local judge returned invalid claim verdict",
    ]
    return any(error in text for error in batch_format_errors)


def should_run_judge_repair(report: Path) -> bool:
    """Patch 3: Sticky initial synthesis.

    Only run judge repair if there are genuine "not_supported" verdicts.
    Skip repair if only "too_broad" verdicts - these are often false positives
    from vocabulary differences between synthesized claims and evidence.

    Returns True if repair should run, False if initial synthesis should be kept.
    """
    if not report.exists():
        return True  # Can't tell, default to repair

    text = report.read_text(errors="ignore").lower()

    # Check for genuinely unsupported claims
    has_not_supported = "not_supported" in text or "not supported" in text

    # Check for format errors that need retry
    has_format_error = any(error in text for error in [
        "local judge did not return",
        "could not be parsed",
        "missing claim_results",
    ])

    # Only repair if there are genuine content issues
    if has_not_supported or has_format_error:
        return True

    # too_broad alone is not enough to trigger repair
    # It's often a false positive from semantic judge seeing vocabulary differences
    return False


def claim_repair_hints(worktree: Path, page: str, normalized_source: Path) -> str:
    command = [
        "python3",
        "tools/wiki_claim_repair_hints.py",
        page,
        "--normalized-source",
        normalized_source.as_posix(),
        "--allow-missing",
    ]
    completed = subprocess.run(
        command,
        cwd=worktree,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return completed.stdout.strip()


def append_claim_repair_hints(prompt: str, hints: str) -> str:
    if not hints:
        return prompt
    return prompt + "\n\nAdditional deterministic claim-repair hints:\n\n```text\n" + hints + "\n```\n"


def is_reference_candidate(candidate_path: str) -> bool:
    return source_relative_to_repo(candidate_path).startswith("wiki/references/")


def render_reference_repair_prompt(
    *,
    slug: str,
    selected_candidate: RelatedCandidate,
    selected_repo_path: str,
    existing_paths: list[str],
    expected_total_pages: int,
    normalized_source: Path,
    evidence_bank: str,
    validation_output: str,
    claim_hints: str,
) -> str:
    allowed_paths = sorted(set(existing_paths + [selected_candidate.path]))
    return f"""Read `AGENTS.md` fully before acting.

Repair exactly one Phase 2 reference page. This is a narrow edit task, not a rewrite of the whole wiki.

Allowed writes:
- `wiki/sources/{slug}.md`
- `{selected_repo_path}`

Forbidden writes:
- `raw/imported/**`
- `raw/normalized/**`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_graph.json`
- `wiki/_linter-report.md`
- `wiki/_claim-judge-report.md`
- `wiki/_grounding-report.md`
- `wiki/analyses/**`
- `wiki/concepts/**`
- `wiki/entities/**`
- `wiki/procedures/**`
- `packages/**`
- `tools/**`
- any synthesized page other than `{selected_repo_path}`
- backup files such as `*.bak`, `*.orig`, `*.tmp`, or `*~`

Selected page:
- `{selected_candidate.path}` - group: {selected_candidate.group or "unclassified"}; priority: {selected_candidate.priority}

Existing synthesized pages for this source that must remain linked:
{render_existing(existing_paths)}

Validation failed with:

```text
{validation_output.strip()}
```

Deterministic claim hints:

```text
{claim_hints.strip() or "No claim-hint output."}
```

Evidence bank:
{evidence_bank}

Mechanical repair rules:
- Edit `{selected_repo_path}` first. Touch `wiki/sources/{slug}.md` only if its Related pages row is incorrect.
- Keep `{selected_repo_path}` as `type: reference`.
- `## Reference data` must have at least 2 data rows with an `Evidence` column containing evidence IDs only.
- `## Source-backed details` must have at least 3 rows with header `| Claim | Evidence |`.
- In both tables, Evidence cells must contain stable evidence IDs copied from the evidence bank.
- Do not write source quote text, locators, or source links in reference or source-backed tables; deterministic post-processing expands evidence IDs.
- If a Source-backed details row fails evidence support, replace its Evidence cell with a stronger ID from the evidence bank, or remove the row if it is optional.
- If a row fails weak generic fact language, rewrite the fact or claim cell, not the Evidence cell.
- Do not use these weak generic words in fact or claim cells: important, crucial, fundamental, essential, success.
- CONSERVATIVE CLAIMS: Each claim/fact must be fully entailed by the cited evidence. Do NOT add details, qualifications, or explanations not present in the evidence.
- Do not copy the Evidence sentence into the fact or claim cell.
- Do not put YAML/frontmatter keys such as `tags:`, `sources:`, `status:`, or `last_updated:` in the Markdown body.
- It is acceptable to remove failed optional rows as long as the page still has the minimum required rows.
- Do not add new pages.
- Do not create backup files.
- Do not create scratch files such as `.fixed` files or `temp_file.md`.
- Do not update index, graph, log, reports, raw files, code, or tools.

After editing, run exactly:

```bash
python3 tools/wiki_link_related.py {slug}
python3 tools/wiki_fix_broken_links.py {slug}
python3 tools/wiki_normalize_ascii.py {slug}
python3 tools/wiki_normalize_tables.py {slug}
python3 tools/wiki_check_synthesis.py {slug} --min-pages {expected_total_pages} --max-pages {expected_total_pages}{allowed_page_args(allowed_paths)} --require-allowed-pages --normalized-source {normalized_source.as_posix()}{range_page_args([selected_candidate.path])}
pnpm wiki:grounding:check
```

If validation still fails, make another narrow edit to `{selected_repo_path}` and rerun the same commands.
"""


def render_judge_repair_prompt(
    *,
    slug: str,
    selected_candidate: RelatedCandidate,
    selected_repo_path: str,
    existing_paths: list[str],
    expected_total_pages: int,
    normalized_source: Path,
    evidence_bank: str,
    judge_report: str,
    judge_candidate: str,
) -> str:
    allowed_paths = sorted(set(existing_paths + [selected_candidate.path]))
    return f"""Read `AGENTS.md` fully before acting.

Repair only the local-judge failures for one Phase 2 synthesized page.

CRITICAL: Make minimal targeted edits only. DO NOT rewrite the page from scratch.
- Keep the existing `## Source-backed details` and `## Source pages` sections.
- Fix only the specific rows mentioned in the judge report.
- Preserve all existing structure and content that passes validation.

Allowed writes:
- `wiki/sources/{slug}.md`
- `{selected_repo_path}`

Forbidden writes:
- `raw/imported/**`
- `raw/normalized/**`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_graph.json`
- `wiki/_linter-report.md`
- `wiki/_claim-judge-report.md`
- `wiki/_grounding-report.md`
- `wiki/analyses/**`
- `packages/**`
- `tools/**`
- any synthesized page other than `{selected_repo_path}`
- backup files such as `*.bak`, `*.orig`, `*.tmp`, or `*~`

Selected page:
- `{selected_candidate.path}` - group: {selected_candidate.group or "unclassified"}; priority: {selected_candidate.priority}

Existing synthesized pages for this source that must remain linked:
{render_existing(existing_paths)}

Evidence bank:
{evidence_bank}

The local claim judge failed with this report:

```md
{judge_report.strip()}
```

Repair rules:
- Fix rows listed under `## Deterministic Flags`, even if the model verdict table marks the row as supported.
- Fix only rows marked `too_broad`, `not_supported`, `unclear`, or `not judged`.
- SYNTHESIS means expressing the SAME MEANING as the evidence using DIFFERENT WORDS. Example:
  - Evidence: "Linear recursion is a basic building block of algorithms."
  - BAD claim (copies evidence): "Linear recursion is a basic building block of algorithms."
  - BAD claim (adds facts): "Linear recursion is a pattern where functions repeatedly apply themselves."
  - GOOD claim (synthesizes): "Linear recursion serves as a core component for constructing algorithms."
- Prefer narrowing the claim to exactly what the cited evidence supports, but use your own phrasing.
- If the judge suggests a narrower claim, use it unless it conflicts with the evidence.
- If the evidence is weak, replace that row's Evidence cell with a stronger evidence ID from the evidence bank.
- Claim cells must not use weak generic words: important, crucial, fundamental, essential, success.
- In `## Source-backed details`, keep Evidence cells as stable evidence IDs copied from the evidence bank.
- Do not write source quote text, locators, or source links in source-backed tables; deterministic post-processing expands evidence IDs.
- If this is a reference page, `## Reference data` Evidence cells must also use evidence IDs only.
- Do not add new pages.
- Do not create backup files.
- Do not remove existing linked pages for this source.

After editing, run exactly:

```bash
python3 tools/wiki_link_related.py {slug}
python3 tools/wiki_fix_broken_links.py {slug}
python3 tools/wiki_normalize_ascii.py {slug}
python3 tools/wiki_normalize_tables.py {slug}
python3 tools/wiki_check_synthesis.py {slug} --min-pages {expected_total_pages} --max-pages {expected_total_pages}{allowed_page_args(allowed_paths)} --require-allowed-pages --normalized-source {normalized_source.as_posix()}{range_page_args([selected_candidate.path])}
pnpm wiki:grounding:check
python3 tools/wiki_judge_claims.py {selected_repo_path} --normalized-source {normalized_source.as_posix()} --candidate {judge_candidate} --fail-on-issues
```

If validation or judging still fails, repair only `{selected_repo_path}` and `wiki/sources/{slug}.md`, then rerun the same commands.
"""


def render_existing(paths: list[str]) -> str:
    if not paths:
        return "- None."
    return "\n".join(f"- `{path}`" for path in paths)


def allowed_page_args(paths: list[str]) -> str:
    return "".join(f" --allowed-page {source_relative_to_repo(path)}" for path in paths)


def find_related_candidate(source_page: Path, candidate_path: str) -> RelatedCandidate:
    related = source_page.read_text()
    rows = related_candidate_rows(related)
    for row in rows:
        if row.path == candidate_path:
            return row
    available = "\n".join(f"- {row.path}" for row in rows) or "- none"
    raise SystemExit(
        f"candidate path is not an uncreated Related pages candidate: {candidate_path}\nAvailable:\n{available}")


def source_relative_candidate(raw: str) -> str:
    if raw.startswith("wiki/"):
        rel = Path(raw).relative_to("wiki")
        return (Path("..") / rel).as_posix()
    return raw


def print_result(result: dict[str, object]) -> None:
    returncodes = result["codex_returncodes"]
    assert isinstance(returncodes, list)
    codex_status = ", ".join(
        "timeout" if code is None else str(code) for code in returncodes)
    validation_returncode = result["validation_returncode"]
    validation_status = "pass" if validation_returncode == 0 else f"fail:{validation_returncode}"
    judge_returncode = result["judge_returncode"]
    judge_status = "pass" if judge_returncode == 0 else f"fail:{judge_returncode}"
    print(f"\n## {result['candidate']}")
    print(f"- worktree: {result['worktree']}")
    print(f"- duration_s: {float(result['duration_s']):.1f}")
    print(f"- codex_returncodes: {codex_status}")
    print(f"- validation: {validation_status}")
    print(f"- judge: {judge_status}")
    print("- changed_files:")
    changed_files = result["changed_files"]
    assert isinstance(changed_files, list)
    if changed_files:
        for changed in changed_files:
            print(f"  - {changed}")
    else:
        print("  - None")
    log_paths = result["log_paths"]
    assert isinstance(log_paths, list)
    print(
        f"- logs: {', '.join(str(path) for path in log_paths)}, {Path(result['worktree']) / 'phase2-validation.log'}")
    judge_report_paths = result["judge_report_paths"]
    assert isinstance(judge_report_paths, list)
    if judge_report_paths:
        print(
            f"- judge_reports: {', '.join(str(path) for path in judge_report_paths)}")


def write_report(path: Path, slug: str, candidate_path: str, result: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    returncodes = result["codex_returncodes"]
    changed_files = result["changed_files"]
    log_paths = result["log_paths"]
    judge_report_paths = result["judge_report_paths"]
    assert isinstance(returncodes, list)
    assert isinstance(changed_files, list)
    assert isinstance(log_paths, list)
    assert isinstance(judge_report_paths, list)
    lines = [
        "# Phase 2 Single Run Report",
        "",
        f"- Source slug: `{slug}`",
        f"- Candidate path: `{candidate_path}`",
        f"- Candidate model: `{result['candidate']}`",
        f"- Worktree: `{result['worktree']}`",
        f"- Duration: {float(result['duration_s']):.1f}s",
        f"- Codex return codes: {', '.join('timeout' if code is None else str(code) for code in returncodes)}",
        f"- Validation: {'pass' if result['validation_returncode'] == 0 else 'fail'}",
        f"- Judge: {'pass' if result['judge_returncode'] == 0 else 'fail'}",
        "",
        "## Changed Files",
        "",
    ]
    lines.extend(f"- `{changed}`" for changed in changed_files)
    if not changed_files:
        lines.append("- None.")
    lines.extend(["", "## Logs", ""])
    lines.extend(f"- `{log}`" for log in log_paths)
    lines.append(f"- `{Path(result['worktree']) / 'phase2-validation.log'}`")
    if judge_report_paths:
        lines.extend(["", "## Judge Reports", ""])
        lines.extend(
            f"- `{judge_report}`" for judge_report in judge_report_paths)
    path.write_text("\n".join(lines) + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    sys.exit(main())
