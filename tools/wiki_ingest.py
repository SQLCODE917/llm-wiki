#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from wiki_phase1_benchmark import find_normalized_source
from wiki_phase2_benchmark import RelatedCandidate, related_candidate_rows
from wiki_common import parse_frontmatter, section


DEFAULTS_PATH = Path("tools/wiki_model_defaults.json")


@dataclass(frozen=True)
class IngestConfig:
    source: Path | None
    slug: str
    candidate_phase1: str
    candidate_phase2: str
    candidate_judge: str
    max_phase2_pages: int
    normalized_source: Path | None
    dry_run: bool
    skip_phase0: bool
    skip_phase1: bool
    skip_phase2: bool
    skip_phase3: bool
    overwrite_normalized: bool
    reuse_imported: bool
    timeout: int
    judge_timeout: int


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the local-model LLM-Wiki ingest pipeline from raw/inbox through Phase 3.")
    parser.add_argument("source", nargs="?", help="source file under raw/inbox; omit to resume an already imported slug")
    parser.add_argument("--slug", help="source slug; defaults to a slugified source filename")
    parser.add_argument("--candidate", help="candidate profile/model for all model phases")
    parser.add_argument("--phase1-candidate")
    parser.add_argument("--phase2-candidate")
    parser.add_argument("--judge-candidate")
    parser.add_argument("--normalized-source")
    parser.add_argument("--max-phase2-pages", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--judge-timeout", type=int, default=900)
    parser.add_argument("--reuse-imported", action="store_true")
    parser.add_argument("--overwrite-normalized", action="store_true")
    parser.add_argument("--skip-phase0", action="store_true")
    parser.add_argument("--skip-phase1", action="store_true")
    parser.add_argument("--skip-phase2", action="store_true")
    parser.add_argument("--skip-phase3", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    defaults = load_defaults()
    phases = defaults.get("phases") if isinstance(defaults.get("phases"), dict) else {}
    source = Path(args.source) if args.source else None
    slug = args.slug or slug_from_source(source)
    if not slug:
        print("FAIL: pass --slug when resuming without a source file", file=sys.stderr)
        return 2

    fallback_candidate = str(defaults.get("default_candidate") or "local-4090")
    config = IngestConfig(
        source=source,
        slug=slug,
        candidate_phase1=args.phase1_candidate or args.candidate or str(phases.get("phase1") or fallback_candidate),
        candidate_phase2=args.phase2_candidate or args.candidate or str(phases.get("phase2") or fallback_candidate),
        candidate_judge=args.judge_candidate or args.candidate or str(phases.get("claim_judge") or fallback_candidate),
        max_phase2_pages=args.max_phase2_pages,
        normalized_source=Path(args.normalized_source) if args.normalized_source else None,
        dry_run=args.dry_run,
        skip_phase0=args.skip_phase0,
        skip_phase1=args.skip_phase1,
        skip_phase2=args.skip_phase2,
        skip_phase3=args.skip_phase3,
        overwrite_normalized=args.overwrite_normalized,
        reuse_imported=args.reuse_imported,
        timeout=args.timeout,
        judge_timeout=args.judge_timeout,
    )

    return run_ingest(config)


def run_ingest(config: IngestConfig) -> int:
    if config.source and not config.skip_phase0:
        phase0 = ["python3", "tools/wiki_phase0_import.py", config.source.as_posix(), config.slug]
        if config.reuse_imported:
            phase0.append("--reuse-imported")
        if config.overwrite_normalized:
            phase0.append("--overwrite-normalized")
        if run_or_print(phase0, config.dry_run) != 0:
            return 1

    normalized_source = config.normalized_source or normalized_source_for_ingest(config)

    if not config.skip_phase1:
        phase1 = [
            "python3",
            "tools/wiki_phase1_benchmark.py",
            config.slug,
            "--candidate",
            config.candidate_phase1,
            "--normalized-source",
            normalized_source.as_posix(),
            "--timeout",
            str(config.timeout),
            "--repair-attempts",
            "1",
            "--keep",
        ]
        output, returncode = run_capture_or_print(phase1, config.dry_run)
        if returncode != 0:
            return returncode
        if not config.dry_run:
            worktree = parse_worktree(output)
            if worktree is None:
                print("FAIL: Phase 1 passed but no worktree was reported", file=sys.stderr)
                return 1
            adopt_phase1_source(config.slug, worktree)

    if not config.skip_phase2:
        for candidate in next_phase2_candidates(config.slug, config.max_phase2_pages):
            current_total = created_page_count(config.slug) + 1
            report = Path(tempfile.gettempdir()) / f"wiki-ingest-{config.slug}-{Path(candidate.path).stem}.md"
            command = [
                "python3",
                "tools/wiki_phase2_single.py",
                config.slug,
                candidate.path,
                "--candidate",
                config.candidate_phase2,
                "--judge-candidate",
                config.candidate_judge,
                "--normalized-source",
                normalized_source.as_posix(),
                "--timeout",
                str(config.timeout),
                "--judge-timeout",
                str(config.judge_timeout),
                "--repair-attempts",
                "1",
                "--judge-repair-attempts",
                "1",
                "--judge-batch",
                "--report",
                report.as_posix(),
                "--keep",
            ]
            if run_or_print(command, config.dry_run) != 0:
                return 1
            if config.dry_run:
                continue
            worktree = parse_worktree(report.read_text())
            if worktree is None:
                print(f"FAIL: Phase 2 passed but report did not include a worktree: {report}", file=sys.stderr)
                return 1
            adopt = [
                "python3",
                "tools/wiki_adopt_phase2.py",
                config.slug,
                worktree.as_posix(),
                "--min-pages",
                str(current_total),
                "--max-pages",
                str(current_total),
                "--normalized-source",
                normalized_source.as_posix(),
                "--skip-judge",
                "phase2-single already passed deterministic validation and local claim judging",
            ]
            if run_or_print(adopt, config.dry_run) != 0:
                return 1

    if not config.skip_phase3:
        if run_or_print(["python3", "tools/wiki_phase3_finalize.py", config.slug], config.dry_run) != 0:
            return 1
    return 0


def run_or_print(command: list[str], dry_run: bool) -> int:
    if dry_run:
        print("$ " + " ".join(command))
        return 0
    completed = subprocess.run(command, text=True)
    return completed.returncode


def run_capture_or_print(command: list[str], dry_run: bool) -> tuple[str, int]:
    if dry_run:
        print("$ " + " ".join(command))
        return "", 0
    completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(completed.stdout, end="")
    return completed.stdout, completed.returncode


def adopt_phase1_source(slug: str, worktree: Path) -> None:
    source = worktree / "wiki/sources" / f"{slug}.md"
    target = Path("wiki/sources") / f"{slug}.md"
    if not source.exists():
        raise SystemExit(f"FAIL: missing Phase 1 source page {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    print(f"copied {target.as_posix()}")


def next_phase2_candidates(slug: str, limit: int) -> list[RelatedCandidate]:
    source_page = Path("wiki/sources") / f"{slug}.md"
    fm = parse_frontmatter(source_page)
    related = section(fm.body, "## Related pages")
    return related_candidate_rows(related)[:limit]


def created_page_count(slug: str) -> int:
    source_page = Path("wiki/sources") / f"{slug}.md"
    if not source_page.exists():
        return 0
    related = section(parse_frontmatter(source_page).body, "## Related pages")
    return len(re.findall(r"\[[^\]]+\]\([^)]+\.md\).*?\|\s*created\s*\|", related))


def parse_worktree(text: str) -> Path | None:
    match = re.search(r"(?:worktree:|Worktree:)\s*`?([^`\n]+)`?", text)
    return Path(match.group(1).strip()) if match else None


def load_defaults() -> dict[str, object]:
    if not DEFAULTS_PATH.exists():
        return {}
    try:
        parsed = json.loads(DEFAULTS_PATH.read_text())
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def normalized_source_for_ingest(config: IngestConfig) -> Path:
    try:
        return find_normalized_source(config.slug)
    except SystemExit:
        if config.dry_run and config.source:
            return Path("raw/normalized") / config.slug / "source.md"
        raise


def slug_from_source(source: Path | None) -> str:
    if source is None:
        return ""
    stem = source.stem.lower()
    stem = re.sub(r"[^a-z0-9]+", "-", stem).strip("-")
    return stem or "source"


if __name__ == "__main__":
    sys.exit(main())
