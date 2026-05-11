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
    page_slug_for_topic,
)
from wiki_common import parse_frontmatter, section
from wiki_manifest import Manifest, PhaseStatus, load_or_create_manifest


DEFAULTS_PATH = Path("tools/wiki_model_defaults.json")


@dataclass(frozen=True)
class IngestConfig:
    source: Path | None
    slug: str
    backend: str
    candidate_phase2: str
    candidate_judge: str
    normalized_source: Path | None
    dry_run: bool
    skip_phase0: bool
    skip_extract: bool
    skip_source_page: bool
    skip_phase2: bool
    skip_phase3: bool
    strict_judge: bool
    overwrite_normalized: bool
    reuse_imported: bool
    pdf_extractor: str
    timeout: int
    judge_timeout: int
    phase2_repair_attempts: int
    chunk_size: int
    overlap: int
    extract_timeout: int
    min_claims_per_topic: int
    use_structured_chunking: bool
    target_tokens: int


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
    parser.add_argument("--timeout", type=int, default=900,
                        help="timeout per synthesis call")
    parser.add_argument("--judge-timeout", type=int, default=900)
    parser.add_argument("--phase2-repair-attempts", type=int, default=1,
                        help="repair attempts after Phase 2 deterministic validation failures")
    parser.add_argument(
        "--backend", help="Model backend: bedrock, codex, openai, anthropic. Default from WIKI_MODEL_BACKEND or codex")
    parser.add_argument("--extract-timeout", type=int,
                        default=120, help="timeout per chunk extraction")
    parser.add_argument("--chunk-size", type=int, default=400,
                        help="lines per chunk for line-based chunking (default: 400)")
    parser.add_argument("--overlap", type=int, default=30,
                        help="overlap between chunks for line-based chunking (default: 30)")
    parser.add_argument("--min-claims-per-topic", type=int,
                        default=3, help="minimum claims to create a page")
    parser.add_argument("--structured", action="store_true",
                        help="Use token-aware structural chunking instead of line-based (recommended)")
    parser.add_argument("--target-tokens", type=int, default=3500,
                        help="Target source tokens per chunk for structured chunking (default: 3500)")
    parser.add_argument("--reuse-imported", action="store_true")
    parser.add_argument("--overwrite-normalized", action="store_true")
    parser.add_argument(
        "--pdf-extractor",
        choices=["auto", "marker", "pymupdf", "pymupdf4llm", "pdfplumber"],
        default="pymupdf4llm",
        help="PDF extraction backend for Phase 0 (default: pymupdf4llm)",
    )
    parser.add_argument("--skip-phase0", action="store_true")
    parser.add_argument("--skip-extract", action="store_true",
                        help="skip deep extraction (use existing state)")
    parser.add_argument("--skip-source-page",
                        action="store_true", help="skip source page creation")
    parser.add_argument("--skip-phase2", action="store_true")
    parser.add_argument("--skip-phase3", action="store_true")
    parser.add_argument("--strict-judge", action="store_true",
                        help="fail on too_broad verdicts (default: soft-pass accepts too_broad)")
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
        normalized_source=Path(
            args.normalized_source) if args.normalized_source else None,
        dry_run=args.dry_run,
        skip_phase0=args.skip_phase0,
        skip_extract=args.skip_extract,
        skip_source_page=args.skip_source_page,
        skip_phase2=args.skip_phase2,
        skip_phase3=args.skip_phase3,
        strict_judge=args.strict_judge,
        overwrite_normalized=args.overwrite_normalized,
        reuse_imported=args.reuse_imported,
        pdf_extractor=args.pdf_extractor,
        timeout=args.timeout,
        judge_timeout=args.judge_timeout,
        phase2_repair_attempts=args.phase2_repair_attempts,
        chunk_size=args.chunk_size,
        overlap=args.overlap,
        extract_timeout=args.extract_timeout,
        min_claims_per_topic=args.min_claims_per_topic,
        use_structured_chunking=args.structured,
        target_tokens=args.target_tokens,
    )

    return run_ingest(config)


def run_ingest(config: IngestConfig) -> int:
    """Run the unified ingestion pipeline."""

    # =========================================================================
    # Initialize manifest
    # =========================================================================
    source_kind = "pdf" if config.source and config.source.suffix.lower(
    ) == ".pdf" else "markdown"
    manifest = load_or_create_manifest(
        config.slug,
        source_file=config.source,
        source_kind=source_kind,
        command=f"pnpm wiki:ingest {config.source or ''} --slug {config.slug}",
        extractor="pymupdf4llm",
        structured=config.use_structured_chunking,
        target_tokens=config.target_tokens,
        model_backend=config.backend,
        candidate=config.candidate_phase2,
    )
    manifest.save()
    print(f"Manifest: {manifest._state_dir / 'manifest.json'}")

    # =========================================================================
    # Phase 0: Normalize source
    # =========================================================================
    if config.source and not config.skip_phase0:
        print("\n" + "=" * 60)
        print("PHASE 0: Normalize source")
        print("=" * 60)
        manifest.set_phase_status("phase0_import", PhaseStatus.RUNNING)
        manifest.save()

        phase0 = ["python3", "tools/wiki_phase0_import.py",
                  config.source.as_posix(), config.slug]
        phase0.extend(["--pdf-extractor", config.pdf_extractor])
        if config.reuse_imported:
            phase0.append("--reuse-imported")
        if config.overwrite_normalized:
            phase0.append("--overwrite-normalized")
        if run_or_print(phase0, config.dry_run) != 0:
            manifest.record_error("phase0_import", "Phase 0 import failed")
            manifest.save()
            return 1

        manifest.set_phase_status("phase0_import", PhaseStatus.COMPLETE)
        manifest.set_phase_status("phase0_normalize", PhaseStatus.COMPLETE)
        # Record file hashes
        imported_path = Path(
            f"raw/imported/{config.slug}/original{config.source.suffix}")
        normalized_path = Path(f"raw/normalized/{config.slug}/source.md")
        manifest.set_original_hash(imported_path)
        manifest.set_normalized_hash(normalized_path)
        manifest.save()
    elif config.skip_phase0:
        manifest.set_phase_status("phase0_import", PhaseStatus.SKIPPED)
        manifest.set_phase_status("phase0_normalize", PhaseStatus.SKIPPED)
        manifest.save()

    normalized_source = config.normalized_source or normalized_source_for_ingest(
        config)

    # =========================================================================
    # Phase 1: Deep extract claims
    # =========================================================================
    if not config.skip_extract:
        print("\n" + "=" * 60)
        print("PHASE 1: Deep extract claims")
        print("=" * 60)
        manifest.set_phase_status("phase1a_extract", PhaseStatus.RUNNING)
        manifest.save()

        if config.dry_run:
            print(
                f"$ python3 tools/wiki_deep_extract.py {config.slug} --extract-only")
        else:
            result = run_deep_extraction(
                slug=config.slug,
                resume=True,  # Always resume if state exists
                chunk_size=config.chunk_size,
                overlap=config.overlap,
                backend_name=config.backend,
                timeout=config.extract_timeout,
                skip_synthesis=True,
                skip_finalize=True,
                use_structured_chunking=config.use_structured_chunking,
                target_tokens=config.target_tokens,
            )
            if result != 0:
                manifest.record_error(
                    "phase1a_extract", "Deep extraction failed")
                manifest.save()
                print("FAIL: Deep extraction failed", file=sys.stderr)
                return 1

        manifest.set_phase_status("phase1a_extract", PhaseStatus.COMPLETE)
        manifest.set_phase_status("phase1b_dedupe", PhaseStatus.COMPLETE)
        manifest.set_phase_status("phase1c_candidates", PhaseStatus.COMPLETE)
        manifest.save()
    else:
        # Phase 1 skipped - mark as skipped
        manifest.set_phase_status("phase1a_extract", PhaseStatus.SKIPPED)
        manifest.set_phase_status("phase1b_dedupe", PhaseStatus.SKIPPED)
        manifest.set_phase_status("phase1c_candidates", PhaseStatus.SKIPPED)
        manifest.save()

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
        manifest.set_phase_status("phase2a_source", PhaseStatus.RUNNING)
        manifest.save()

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

        manifest.set_phase_status("phase2a_source", PhaseStatus.COMPLETE)
        manifest.save()
    else:
        manifest.set_phase_status("phase2a_source", PhaseStatus.SKIPPED)
        manifest.save()

    # =========================================================================
    # Phase 2b: Synthesize pages with quality gates
    # =========================================================================
    if not config.skip_phase2:
        print("\n" + "=" * 60)
        print("PHASE 2b: Synthesize pages with quality gates")
        print("=" * 60)
        manifest.set_phase_status("phase2b_synthesize", PhaseStatus.RUNNING)
        manifest.save()

        # Get candidates from source page
        candidates = next_phase2_candidates_from_state(state, config)
        print(f"Candidates to synthesize: {len(candidates)}")
        manifest.update_phase2_progress(
            total=len(candidates), pending=len(candidates))

        synthesized_count = 0
        adopted_count = 0
        failed_count = 0

        for i, (topic, page_path) in enumerate(candidates, 1):
            print(f"\n[{i}/{len(candidates)}] {topic}")

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
                str(config.phase2_repair_attempts),
                "--judge-repair-attempts",
                "1",  # Allow one repair if judge finds not_supported
                "--judge-batch",
                "--report",
                report.as_posix(),
                "--keep",
            ]
            # Default: soft-pass mode (accepts too_broad, fails on not_supported)
            # Use --strict-judge for quality-critical ingests
            if config.strict_judge:
                command.append("--strict-judge")
            if run_or_print(command, config.dry_run) != 0:
                print(f"  WARN: Synthesis failed for {topic}, continuing...")
                failed_count += 1
                manifest.update_phase2_progress(
                    synthesized=synthesized_count,
                    adopted=adopted_count,
                    failed=failed_count,
                    pending=len(candidates) - i,
                )
                manifest.save()
                continue

            synthesized_count += 1

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
                "phase2-single already ran judge with soft-pass (accepts too_broad)",
            ]
            if run_or_print(adopt, config.dry_run) != 0:
                print(f"  WARN: Adopt failed for {topic}")
                failed_count += 1
                manifest.update_phase2_progress(
                    synthesized=synthesized_count,
                    adopted=adopted_count,
                    failed=failed_count,
                    pending=len(candidates) - i,
                )
                manifest.save()
                continue

            adopted_count += 1
            manifest.update_phase2_progress(
                synthesized=synthesized_count,
                adopted=adopted_count,
                failed=failed_count,
                pending=len(candidates) - i,
            )
            manifest.save()
            print(f"  Adopted: {page_path}")

        # Update final Phase 2b status
        if adopted_count > 0:
            if failed_count > 0:
                manifest.set_phase_status(
                    "phase2b_synthesize", PhaseStatus.PARTIAL)
                manifest.set_phase_status("phase2c_adopt", PhaseStatus.PARTIAL)
                manifest.partial_success_reason = f"{failed_count} of {len(candidates)} candidates failed"
            else:
                manifest.set_phase_status(
                    "phase2b_synthesize", PhaseStatus.COMPLETE)
                manifest.set_phase_status(
                    "phase2c_adopt", PhaseStatus.COMPLETE)
        else:
            manifest.set_phase_status("phase2b_synthesize", PhaseStatus.FAILED)
            manifest.set_phase_status("phase2c_adopt", PhaseStatus.FAILED)
            manifest.record_error("phase2b_synthesize",
                                  "No pages were adopted")
        manifest.save()
    else:
        manifest.set_phase_status("phase2b_synthesize", PhaseStatus.SKIPPED)
        manifest.set_phase_status("phase2c_adopt", PhaseStatus.SKIPPED)
        manifest.save()

    # =========================================================================
    # Phase 3: Finalize
    # =========================================================================
    if not config.skip_phase3:
        print("\n" + "=" * 60)
        print("PHASE 3: Finalize")
        print("=" * 60)
        manifest.set_phase_status("phase3a_index", PhaseStatus.RUNNING)
        manifest.save()

        if run_or_print(["python3", "tools/wiki_phase3_finalize.py", config.slug], config.dry_run) != 0:
            manifest.record_error("phase3a_index", "Phase 3 finalize failed")
            manifest.save()
            return 1

        manifest.set_phase_status("phase3a_index", PhaseStatus.COMPLETE)
        manifest.set_phase_status("phase3b_graph", PhaseStatus.COMPLETE)
        manifest.set_phase_status("phase3c_lint", PhaseStatus.COMPLETE)
        manifest.set_phase_status("phase3d_log", PhaseStatus.COMPLETE)
        manifest.save()
    else:
        manifest.set_phase_status("phase3a_index", PhaseStatus.SKIPPED)
        manifest.set_phase_status("phase3b_graph", PhaseStatus.SKIPPED)
        manifest.set_phase_status("phase3c_lint", PhaseStatus.SKIPPED)
        manifest.set_phase_status("phase3d_log", PhaseStatus.SKIPPED)
        manifest.save()

    print("\n" + "=" * 60)
    print("INGESTION COMPLETE")
    print("=" * 60)
    print(f"Manifest: {manifest._state_dir / 'manifest.json'}")
    return 0


def next_phase2_candidates_from_state(state, config: IngestConfig) -> list[tuple[str, str]]:
    """Get candidate pages from extraction state.

    Returns list of (topic, page_path) tuples, sorted by claim count.
    """
    candidates = []
    for topic, claims in sorted(state.topics.items(), key=lambda x: -len(x[1])):
        if len(claims) < config.min_claims_per_topic:
            continue
        page_slug = page_slug_for_topic(topic, config.slug)
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
