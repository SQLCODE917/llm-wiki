#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

from wiki_common import parse_frontmatter, section


SYNTH_DIRS = {"concepts", "entities", "procedures", "references"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Adopt a passing Phase 2 benchmark worktree into this repo.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("worktree", help="Phase 2 benchmark worktree to adopt from")
    parser.add_argument("--min-pages", type=int, default=5)
    parser.add_argument("--max-pages", type=int, default=15)
    parser.add_argument("--normalized-source", help="normalized source markdown for evidence excerpt checks")
    parser.add_argument("--judge-candidate", default="local-4090", help="local Codex candidate for claim judging")
    parser.add_argument("--judge-timeout", type=int, default=600)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument(
        "--human-override-judge",
        help="explicit curator reason for adopting without a passing local claim judge",
    )
    parser.add_argument(
        "--skip-judge",
        help="machine-readable reason for skipping judge validation, usually because an upstream Phase 2 single run already passed it",
    )
    parser.add_argument("--dry-run", action="store_true", help="show files that would be copied without writing")
    args = parser.parse_args()

    worktree = Path(args.worktree).resolve()
    if not worktree.exists():
        print(f"FAIL: missing worktree {worktree}")
        return 1

    source = worktree / "wiki/sources" / f"{args.slug}.md"
    if not source.exists():
        print(f"FAIL: missing source page in worktree: {source}")
        return 1

    validation = validate_worktree(worktree, args.slug, args.min_pages, args.max_pages, args.normalized_source)
    if validation != 0:
        return validation

    files = [Path("wiki/sources") / f"{args.slug}.md"]
    synthesized_pages = linked_synthesized_pages(source)
    files.extend(synthesized_pages)
    files = sorted(set(files))

    if args.human_override_judge:
        print(f"Judge override accepted: {args.human_override_judge}")
    elif args.skip_judge:
        print(f"Judge validation skipped: {args.skip_judge}")
    else:
        if not args.normalized_source:
            print("FAIL: --normalized-source is required unless --human-override-judge is provided")
            return 1
        judge_status = validate_judges(
            worktree=worktree,
            pages=synthesized_pages,
            normalized_source=args.normalized_source,
            candidate=args.judge_candidate,
            codex_bin=args.codex_bin,
            timeout=args.judge_timeout,
        )
        if judge_status != 0:
            return judge_status

    if args.dry_run:
        print("Files that would be adopted:")
        for path in files:
            print(f"- {path.as_posix()}")
        return 0

    for rel in files:
        src = worktree / rel
        dst = Path.cwd() / rel
        if not src.exists():
            print(f"FAIL: expected file missing from worktree: {src}")
            return 1
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"copied {rel.as_posix()}")

    print("Adopted Phase 2 files. Run `pnpm wiki:phase3 <slug>` to update navigation, graph, log, and lint report.")
    return 0


def validate_worktree(
    worktree: Path,
    slug: str,
    min_pages: int,
    max_pages: int,
    normalized_source: str | None,
) -> int:
    command = [
        "python3",
        "tools/wiki_check_synthesis.py",
        slug,
        "--min-pages",
        str(min_pages),
        "--max-pages",
        str(max_pages),
    ]
    if normalized_source:
        command.extend(["--normalized-source", normalized_source])

    completed = subprocess.run(
        command,
        cwd=worktree,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    print(completed.stdout, end="")
    return completed.returncode


def validate_judges(
    *,
    worktree: Path,
    pages: list[Path],
    normalized_source: str,
    candidate: str,
    codex_bin: str,
    timeout: int,
) -> int:
    if not pages:
        print("FAIL: no synthesized pages found for judge validation")
        return 1

    status = 0
    report_dir = worktree / "phase2-judge-reports"
    report_dir.mkdir(exist_ok=True)
    for page in pages:
        output = report_dir / f"{page.stem}.md"
        command = [
            "python3",
            "tools/wiki_judge_claims.py",
            page.as_posix(),
            "--normalized-source",
            normalized_source,
            "--candidate",
            candidate,
            "--codex-bin",
            codex_bin,
            "--timeout",
            str(timeout),
            "--output",
            output.as_posix(),
            "--fail-on-issues",
        ]
        completed = subprocess.run(
            command,
            cwd=worktree,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print(completed.stdout, end="")
        if completed.returncode != 0:
            print(f"FAIL: judge did not pass for {page.as_posix()} (report: {output.as_posix()})")
            status = completed.returncode if status == 0 else status
    return status


def linked_synthesized_pages(source_page: Path) -> list[Path]:
    fm = parse_frontmatter(source_page)
    related = section(fm.body, "## Related pages")
    pages: list[Path] = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", related):
        resolved = (source_page.parent / target).resolve()
        try:
            rel = resolved.relative_to(source_page.parents[2].resolve())
        except ValueError:
            continue
        if len(rel.parts) >= 3 and rel.parts[0] == "wiki" and rel.parts[1] in SYNTH_DIRS:
            pages.append(rel)
    return pages


if __name__ == "__main__":
    sys.exit(main())
