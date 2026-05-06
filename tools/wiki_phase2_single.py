#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from wiki_model_backend import get_backend, ModelConfig, parse_model_output, write_parsed_files
from wiki_page_schema import WikiPageSchema, parse_llm_response, parse_llm_response_structured, ParseResult, render_page, validate_schema
from wiki_phase1_benchmark import find_normalized_source, git_changed_files, init_git, parse_candidate, run_codex
from wiki_phase2_benchmark import (
    EvidenceBankResult,
    RelatedCandidate,
    build_evidence_bank,
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
    ValidationFailure,
    parse_validation_output,
    group_failures_by_page,
    summarize_failures,
    DETERMINISTIC_CATEGORIES,
)
from wiki_context_packer import check_evidence_contract_violations


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
            extraction_claims=extraction_claims,
            json_output=use_json,
        )
        print_result(result)
        if args.report:
            write_report(Path(args.report), args.slug, candidate_path, result)
        return 0 if result["validation_returncode"] == 0 and result["judge_returncode"] == 0 else 1
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
) -> tuple[bool, list[ValidationFailure]]:
    """Attempt deterministic repairs based on validation failures.

    Returns:
        Tuple of (repairs_made, remaining_failures)
    """
    if not validation_log.exists():
        return False, []

    validation_output = validation_log.read_text()
    failures = parse_validation_output(validation_output)

    if not failures:
        return False, []

    # Count deterministically fixable failures
    det_failures = [
        f for f in failures if f.category in DETERMINISTIC_CATEGORIES]
    if not det_failures:
        print(
            f"  No deterministic repairs possible ({len(failures)} failures need LLM)")
        return False, failures

    print(
        f"  {len(det_failures)} deterministic, {len(failures) - len(det_failures)} need LLM")

    # Attempt repairs on the markdown file directly
    full_page_path = worktree / page_path
    if not full_page_path.exists():
        return False, failures

    page_text = full_page_path.read_text()
    repairs_made = False

    for failure in det_failures:
        if failure.category == FailureCategory.MISSING_SOURCE_LINK:
            # Add source to frontmatter
            if f"sources/{slug}.md" not in page_text:
                page_text = repair_missing_source_in_markdown(page_text, slug)
                repairs_made = True
        elif failure.category == FailureCategory.MISSING_SOURCE_SECTION:
            # Add Source pages section
            if "## Source pages" not in page_text:
                title = slug.replace("-", " ").title()
                page_text += f"\n\n## Source pages\n\n- [{title}](../sources/{slug}.md)\n"
                repairs_made = True
        elif failure.category == FailureCategory.PLACEHOLDER_TEXT:
            # Remove placeholder text
            page_text = re.sub(r"^.*Page title.*$", "",
                               page_text, flags=re.MULTILINE)
            page_text = re.sub(r"^.*Source-native group name.*$",
                               "", page_text, flags=re.MULTILINE)
            repairs_made = True
        elif failure.category == FailureCategory.BAD_SOURCE_CELL:
            # Fix source cell format in tables
            title = slug.replace("-", " ").title()
            page_text = re.sub(
                r"\|\s*\[?Source\]?\s*\|",
                f"| [{title}](../sources/{slug}.md) |",
                page_text,
            )
            repairs_made = True

    if repairs_made:
        full_page_path.write_text(page_text)
        print(f"  Applied deterministic repairs to {page_path}")

    # Return remaining failures that still need LLM
    remaining = [
        f for f in failures if f.category not in DETERMINISTIC_CATEGORIES]
    return repairs_made, remaining


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


def run_with_backend_json(
    *,
    worktree: Path,
    backend_name: str | None,
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
    for 2-column tables: | Claim | [E01] | -> | Claim | Evidence | Locator | Source |

    Otherwise falls back to fill_evidence_in_page for 3-column tables:
    | Claim | Locator | Source | -> | Claim | Evidence | Locator | Source |

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
    evidence_bank = build_evidence_bank(
        worktree, normalized_source, [selected_candidate],
        extraction_claims=extraction_claims, use_ids=True, slug=slug)
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

    # Use model backend if specified, otherwise use codex CLI
    use_backend = backend_name is not None or os.environ.get(
        "WIKI_MODEL_BACKEND") not in (None, "", "codex")

    if json_output and use_backend:
        # JSON output mode: model outputs JSON, we render markdown
        returncode, paths, page_schema = run_with_backend_json(
            worktree=worktree,
            backend_name=backend_name,
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
        )
        judge_report_paths.extend(reports)

        for attempt in range(1, judge_repair_attempts + 1):
            if judge_returncode == 0:
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
- `## Reference data` must have at least 2 data rows and include `Evidence` and `Locator` columns.
- `## Source-backed details` must have at least 3 rows with header `| Claim | Evidence | Locator | Source |`.
- If a row fails "excerpt is not found in locator range", shorten the Evidence cell to an exact substring from that locator line, or remove the row if it is optional.
- If a source line contains internal quotation marks, use a shorter exact excerpt that avoids those internal quotation marks.
- If a row fails weak generic fact language, rewrite the fact or claim cell, not the Evidence cell.
- Do not use these weak generic words in fact or claim cells: important, crucial, fundamental, essential, success.
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
- Prefer narrowing the claim to exactly what the cited evidence supports.
- If the judge suggests a narrower claim, use it unless it conflicts with the evidence.
- If the evidence is weak, replace that row with a stronger exact excerpt from the evidence bank.
- Claim cells must not use weak generic words: important, crucial, fundamental, essential, success.
- Keep all evidence cells as exact excerpts from `{normalized_source.as_posix()}`.
- Keep all locators as `normalized:L12` or `normalized:L12-L14`, and ensure the excerpt appears in that range.
- If this is a reference page, `## Reference data` must include `Evidence` and `Locator` columns for every source-derived row.
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
