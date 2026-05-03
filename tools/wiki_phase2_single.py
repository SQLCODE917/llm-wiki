#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
import time
from pathlib import Path

from wiki_phase1_benchmark import find_normalized_source, git_changed_files, init_git, parse_candidate, run_codex
from wiki_phase2_benchmark import (
    RelatedCandidate,
    build_evidence_bank,
    existing_created_paths,
    related_candidate_rows,
    render_prompt,
    render_repair_prompt,
    run_validation,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one atomic Phase 2 synthesis task in a temp worktree.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("candidate_path", help="one Related pages candidate path, e.g. ../procedures/example.md")
    parser.add_argument("--candidate", default="local-4090", help="local Codex candidate profile or profile:model")
    parser.add_argument("--normalized-source", help="explicit normalized markdown path")
    parser.add_argument("--prompt-template", default="tools/prompts/phase2-synthesis.md")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--repair-attempts", type=int, default=1)
    parser.add_argument("--keep", action="store_true", help="keep temp worktree after the run")
    args = parser.parse_args()

    repo_root = Path.cwd()
    normalized_source = Path(args.normalized_source) if args.normalized_source else find_normalized_source(args.slug)
    if not normalized_source.exists():
        print(f"FAIL: normalized source does not exist: {normalized_source}", file=sys.stderr)
        return 2

    prompt_template = Path(args.prompt_template)
    if not prompt_template.exists():
        print(f"FAIL: prompt template does not exist: {prompt_template}", file=sys.stderr)
        return 2

    candidate = parse_candidate(args.candidate)
    worktree = Path(tempfile.mkdtemp(prefix=f"llm-wiki-phase2-single-{args.slug}-{candidate.safe_label}.", dir="/tmp"))
    try:
        copy_repo_contents(repo_root, worktree)
        init_git(worktree)
        result = run_single_candidate(
            worktree=worktree,
            slug=args.slug,
            normalized_source=normalized_source,
            prompt_template=prompt_template,
            candidate_path=source_relative_candidate(args.candidate_path),
            candidate=candidate,
            codex_bin=args.codex_bin,
            timeout=args.timeout,
            repair_attempts=args.repair_attempts,
        )
        print_result(result)
        return 0 if result["validation_returncode"] == 0 else 1
    finally:
        if not args.keep:
            shutil.rmtree(worktree, ignore_errors=True)


def copy_repo_contents(src: Path, dst: Path) -> None:
    from wiki_phase1_benchmark import copy_repo

    copy_repo(src, dst)


def run_single_candidate(
    *,
    worktree: Path,
    slug: str,
    normalized_source: Path,
    prompt_template: Path,
    candidate_path: str,
    candidate,
    codex_bin: str,
    timeout: int,
    repair_attempts: int,
) -> dict[str, object]:
    source_page = worktree / "wiki/sources" / f"{slug}.md"
    selected_candidate = find_related_candidate(source_page, candidate_path)
    existing_paths = existing_created_paths(source_page)
    if selected_candidate.path in existing_paths:
        raise SystemExit(f"candidate is already created: {selected_candidate.path}")

    selected_paths = [selected_candidate.path]
    allowed_paths = sorted(set(existing_paths + selected_paths))
    expected_total_pages = len(allowed_paths)
    evidence_bank = build_evidence_bank(worktree, normalized_source, selected_paths)
    prompt = render_prompt(
        template=(worktree / prompt_template).read_text(),
        slug=slug,
        normalized_source=normalized_source.as_posix(),
        min_pages=expected_total_pages,
        max_pages=expected_total_pages,
        existing_paths=existing_paths,
        selected_candidates=[selected_candidate],
        expected_total_pages=expected_total_pages,
        evidence_bank=evidence_bank,
    )

    start = time.monotonic()
    codex_returncodes: list[int | None] = []
    log_paths: list[Path] = []

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
    validation_returncode = run_validation(
        worktree,
        slug,
        expected_total_pages,
        expected_total_pages,
        allowed_paths,
        normalized_source,
    )

    for attempt in range(1, repair_attempts + 1):
        if validation_returncode == 0:
            break
        repair_prompt = render_repair_prompt(
            slug=slug,
            validation_output=(worktree / "phase2-validation.log").read_text(),
            min_pages=expected_total_pages,
            max_pages=expected_total_pages,
            selected_candidates=[selected_candidate],
            existing_paths=existing_paths,
            normalized_source=normalized_source,
            evidence_bank=evidence_bank,
        )
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
        validation_returncode = run_validation(
            worktree,
            slug,
            expected_total_pages,
            expected_total_pages,
            allowed_paths,
            normalized_source,
        )

    return {
        "candidate": candidate.label,
        "worktree": worktree,
        "duration_s": time.monotonic() - start,
        "codex_returncodes": codex_returncodes,
        "validation_returncode": validation_returncode,
        "changed_files": git_changed_files(worktree),
        "log_paths": log_paths,
    }


def find_related_candidate(source_page: Path, candidate_path: str) -> RelatedCandidate:
    related = source_page.read_text()
    rows = related_candidate_rows(related)
    for row in rows:
        if row.path == candidate_path:
            return row
    available = "\n".join(f"- {row.path}" for row in rows) or "- none"
    raise SystemExit(f"candidate path is not an uncreated Related pages candidate: {candidate_path}\nAvailable:\n{available}")


def source_relative_candidate(raw: str) -> str:
    if raw.startswith("wiki/"):
        rel = Path(raw).relative_to("wiki")
        return (Path("..") / rel).as_posix()
    return raw


def print_result(result: dict[str, object]) -> None:
    returncodes = result["codex_returncodes"]
    assert isinstance(returncodes, list)
    codex_status = ", ".join("timeout" if code is None else str(code) for code in returncodes)
    validation_returncode = result["validation_returncode"]
    validation_status = "pass" if validation_returncode == 0 else f"fail:{validation_returncode}"
    print(f"\n## {result['candidate']}")
    print(f"- worktree: {result['worktree']}")
    print(f"- duration_s: {float(result['duration_s']):.1f}")
    print(f"- codex_returncodes: {codex_status}")
    print(f"- validation: {validation_status}")
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
    print(f"- logs: {', '.join(str(path) for path in log_paths)}, {Path(result['worktree']) / 'phase2-validation.log'}")


if __name__ == "__main__":
    sys.exit(main())
