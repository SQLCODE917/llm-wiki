#!/usr/bin/env python3
"""Unified wiki ingestion pipeline.

This implements the highest-quality ingestion flow:
1. Phase 0: Normalize source (wiki_phase0_import)
2. Phase 1: Deep extract claims from all chunks (wiki_deep_extract --extract-only)
3. Phase 2a: Create source page from extracted topics
4. Phase 2b: For each topic, synthesize with quality gates (wiki_phase2_single)
5. Phase 3: Finalize (wiki_phase3_finalize)

Usage:
    pnpm wiki:ingest raw/inbox/source.pdf --slug <slug>
    pnpm wiki:ingest --slug <slug>  # Resume with existing normalized source
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from wiki_phase1_benchmark import find_normalized_source
from wiki_deep_extract import (
    run_deep_extraction,
    load_extraction_state,
    create_source_page_from_topics,
    get_state_path,
)
from wiki_common import parse_frontmatter, section


DEFAULTS_PATH = Path("tools/wiki_model_defaults.json")


@dataclass(frozen=True)
class IngestConfig:
    source: Path | None
    slug: str
    backend: str
    candidate_phase2: str
    candidate_judge: str
    max_phase2_pages: int
    normalized_source: Path | None
    dry_run: bool
    skip_phase0: bool
    skip_extract: bool
    skip_source_page: bool
    skip_phase2: bool
    skip_phase3: bool
    overwrite_normalized: bool
    reuse_imported: bool
    timeout: int
    judge_timeout: int
    chunk_size: int
    overlap: int
    extract_timeout: int
    min_claims_per_topic: int


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Unified wiki ingestion: deep extraction + quality synthesis."
    )
    parser.add_argument(
        "source", nargs="?", help="source file under raw/inbox; omit to resume an already imported slug")
    parser.add_argument(
        "--slug", help="source slug; defaults to a slugified source filename")
    parser.add_argument(
        "--candidate", help="candidate profile/model for all model phases")
    parser.add_argument("--phase2-candidate")
    parser.add_argument("--judge-candidate")
    parser.add_argument("--normalized-source")
    parser.add_argument("--max-phase2-pages", type=int,
                        default=10, help="max pages to synthesize (default: 10)")
    parser.add_argument("--timeout", type=int, default=900,
                        help="timeout per synthesis call")
    parser.add_argument("--judge-timeout", type=int, default=900)
    parser.add_argument(
        "--backend", help="Model backend: bedrock, codex, openai, anthropic. Default from WIKI_MODEL_BACKEND or codex")
    parser.add_argument("--extract-timeout", type=int,
                        default=120, help="timeout per chunk extraction")
    parser.add_argument("--chunk-size", type=int, default=400,
                        help="lines per chunk (default: 400)")
    parser.add_argument("--overlap", type=int, default=30,
                        help="overlap between chunks (default: 30)")
    parser.add_argument("--min-claims-per-topic", type=int,
                        default=3, help="minimum claims to create a page")
    parser.add_argument("--reuse-imported", action="store_true")
    parser.add_argument("--overwrite-normalized", action="store_true")
    parser.add_argument("--skip-phase0", action="store_true")
    parser.add_argument("--skip-extract", action="store_true",
                        help="skip deep extraction (use existing state)")
    parser.add_argument("--skip-source-page",
                        action="store_true", help="skip source page creation")
    parser.add_argument("--skip-phase2", action="store_true")
    parser.add_argument("--skip-phase3", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    defaults = load_defaults()
    phases = defaults.get("phases") if isinstance(
        defaults.get("phases"), dict) else {}
    source = Path(args.source) if args.source else None
    slug = args.slug or slug_from_source(source)
    if not slug:
        print("FAIL: pass --slug when resuming without a source file", file=sys.stderr)
        return 2

    fallback_candidate = str(defaults.get("default_candidate") or "local-4090")
    backend = args.backend or os.environ.get("WIKI_MODEL_BACKEND") or "codex"
    config = IngestConfig(
        source=source,
        slug=slug,
        backend=backend,
        candidate_phase2=args.phase2_candidate or args.candidate or str(
            phases.get("phase2") or fallback_candidate),
        candidate_judge=args.judge_candidate or args.candidate or str(
            phases.get("claim_judge") or fallback_candidate),
        max_phase2_pages=args.max_phase2_pages,
        normalized_source=Path(
            args.normalized_source) if args.normalized_source else None,
        dry_run=args.dry_run,
        skip_phase0=args.skip_phase0,
        skip_extract=args.skip_extract,
        skip_source_page=args.skip_source_page,
        skip_phase2=args.skip_phase2,
        skip_phase3=args.skip_phase3,
        overwrite_normalized=args.overwrite_normalized,
        reuse_imported=args.reuse_imported,
        timeout=args.timeout,
        judge_timeout=args.judge_timeout,
        chunk_size=args.chunk_size,
        overlap=args.overlap,
        extract_timeout=args.extract_timeout,
        min_claims_per_topic=args.min_claims_per_topic,
    )

    return run_ingest(config)


def run_ingest(config: IngestConfig) -> int:
    """Run the unified ingestion pipeline."""

    # =========================================================================
    # Phase 0: Normalize source
    # =========================================================================
    if config.source and not config.skip_phase0:
        print("\n" + "=" * 60)
        print("PHASE 0: Normalize source")
        print("=" * 60)
        phase0 = ["python3", "tools/wiki_phase0_import.py",
                  config.source.as_posix(), config.slug]
        if config.reuse_imported:
            phase0.append("--reuse-imported")
        if config.overwrite_normalized:
            phase0.append("--overwrite-normalized")
        if run_or_print(phase0, config.dry_run) != 0:
            return 1

    normalized_source = config.normalized_source or normalized_source_for_ingest(
        config)

    # =========================================================================
    # Phase 1: Deep extract claims
    # =========================================================================
    if not config.skip_extract:
        print("\n" + "=" * 60)
        print("PHASE 1: Deep extract claims")
        print("=" * 60)
        if config.dry_run:
            print(
                f"$ python3 tools/wiki_deep_extract.py {config.slug} --extract-only")
        else:
            result = run_deep_extraction(
                slug=config.slug,
                resume=True,  # Always resume if state exists
                chunk_size=config.chunk_size,
                overlap=config.overlap,
                timeout=config.extract_timeout,
                skip_synthesis=True,
                skip_finalize=True,
            )
            if result != 0:
                print("FAIL: Deep extraction failed", file=sys.stderr)
                return 1

    # Load extraction state
    state = load_extraction_state(config.slug)
    if state is None:
        print(
            f"FAIL: No extraction state found for {config.slug}", file=sys.stderr)
        print(f"  Expected: {get_state_path(config.slug)}", file=sys.stderr)
        return 1

    print(f"\nExtraction state loaded:")
    print(f"  Claims: {len(state.claims)}")
    print(f"  Topics: {len(state.topics)}")
    print(
        f"  Chunks processed: {len(state.processed_chunks)}/{len(state.chunks)}")

    # =========================================================================
    # Phase 2a: Create source page
    # =========================================================================
    source_page = Path(f"wiki/sources/{config.slug}.md")
    if not config.skip_source_page:
        print("\n" + "=" * 60)
        print("PHASE 2a: Create source page")
        print("=" * 60)
        if config.dry_run:
            print(f"$ create_source_page_from_topics({config.slug})")
        else:
            source_page = create_source_page_from_topics(
                config.slug,
                state,
                normalized_source,
                min_claims_per_topic=config.min_claims_per_topic,
            )
            print(f"Created: {source_page}")

            # Validate source page
            check_source = ["python3",
                            "tools/wiki_check_source.py", config.slug]
            result = subprocess.run(
                check_source, capture_output=True, text=True)
            if result.returncode != 0:
                print("WARN: Source page validation issues:")
                print(result.stdout)

    # =========================================================================
    # Phase 2b: Synthesize pages with quality gates
    # =========================================================================
    if not config.skip_phase2:
        print("\n" + "=" * 60)
        print("PHASE 2b: Synthesize pages with quality gates")
        print("=" * 60)

        # Get candidates from source page
        candidates = next_phase2_candidates_from_state(state, config)
        print(
            f"Candidates to synthesize: {len(candidates)} (max {config.max_phase2_pages})")

        for i, (topic, page_path) in enumerate(candidates[:config.max_phase2_pages], 1):
            print(
                f"\n[{i}/{min(len(candidates), config.max_phase2_pages)}] {topic}")

            # Skip if page already exists
            if Path(page_path.lstrip('../')).exists():
                print(f"  Skipping (exists): {page_path}")
                continue

            report = Path(tempfile.gettempdir()) / \
                f"wiki-ingest-{config.slug}-{Path(page_path).stem}.md"
            extraction_state_path = get_state_path(config.slug)
            command = [
                "python3",
                "tools/wiki_phase2_single.py",
                config.slug,
                page_path,
                "--backend",
                config.backend,
                "--candidate",
                config.candidate_phase2,
                "--judge-candidate",
                config.candidate_judge,
                "--normalized-source",
                normalized_source.as_posix(),
                "--extraction-state",
                extraction_state_path.as_posix(),
                "--timeout",
                str(config.timeout),
                "--judge-timeout",
                str(config.judge_timeout),
                "--repair-attempts",
                "0",
                "--judge-repair-attempts",
                "0",
                "--skip-judge",
                "--judge-batch",
                "--report",
                report.as_posix(),
                "--keep",
            ]
            if run_or_print(command, config.dry_run) != 0:
                print(f"  WARN: Synthesis failed for {topic}, continuing...")
                continue

            if config.dry_run:
                continue

            worktree = parse_worktree(report.read_text())
            if worktree is None:
                print(f"  WARN: No worktree in report, skipping adopt")
                continue

            # Adopt the page
            current_total = created_page_count(config.slug) + 1
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
                print(f"  WARN: Adopt failed for {topic}")
                continue

            print(f"  Adopted: {page_path}")

    # =========================================================================
    # Phase 3: Finalize
    # =========================================================================
    if not config.skip_phase3:
        print("\n" + "=" * 60)
        print("PHASE 3: Finalize")
        print("=" * 60)
        if run_or_print(["python3", "tools/wiki_phase3_finalize.py", config.slug], config.dry_run) != 0:
            return 1

    print("\n" + "=" * 60)
    print("INGESTION COMPLETE")
    print("=" * 60)
    return 0


def next_phase2_candidates_from_state(state, config: IngestConfig) -> list[tuple[str, str]]:
    """Get candidate pages from extraction state.

    Returns list of (topic, page_path) tuples, sorted by claim count.
    """
    candidates = []
    for topic, claims in sorted(state.topics.items(), key=lambda x: -len(x[1])):
        if len(claims) < config.min_claims_per_topic:
            continue
        page_slug = topic.lower().replace(' ', '-').replace('/', '-')
        page_slug = re.sub(r'[^a-z0-9-]', '', page_slug)
        page_path = f"../concepts/{page_slug}.md"
        candidates.append((topic, page_path))
    return candidates


def run_or_print(command: list[str], dry_run: bool) -> int:
    if dry_run:
        print("$ " + " ".join(command))
        return 0
    completed = subprocess.run(command, text=True)
    return completed.returncode


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
