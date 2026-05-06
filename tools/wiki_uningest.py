#!/usr/bin/env python3
"""Un-ingest a source: remove all wiki pages and raw files created during ingest.

This is a deterministic reset function for testing ingest workflows.
It traces wiki pages back to normalized sources and removes everything.

Usage:
    python3 tools/wiki_uningest.py <slug> --dry-run    # Preview
    python3 tools/wiki_uningest.py <slug>               # Execute
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


def find_synthesized_pages(source_page: Path) -> list[Path]:
    """Find all synthesized pages linked from a source page's Related pages section."""
    if not source_page.exists():
        return []

    content = source_page.read_text()
    synthesized = []

    # Look for markdown links in Related pages table
    # Pattern: [../concepts/example.md](../concepts/example.md)
    link_pattern = re.compile(
        r'\[([^\]]+)\]\((\.\./(?:concepts|entities|procedures|references)/[^)]+\.md)\)')

    for match in link_pattern.finditer(content):
        rel_path = match.group(2)
        # Convert relative path from source page to absolute
        abs_path = (source_page.parent / rel_path).resolve()
        if abs_path.exists():
            synthesized.append(abs_path)

    return synthesized


def find_analysis_pages(slug: str, analyses_dir: Path) -> list[Path]:
    """Find analysis pages that cite this source."""
    if not analyses_dir.exists():
        return []

    analysis_pages = []
    source_ref = f"../sources/{slug}.md"

    for page in analyses_dir.glob("*.md"):
        content = page.read_text()
        if source_ref in content or f"sources/{slug}.md" in content:
            analysis_pages.append(page)

    return analysis_pages


def uningest(slug: str, *, dry_run: bool = False, keep_imported: bool = False) -> dict:
    """Remove all artifacts from a previous ingest.

    Args:
        slug: The source slug to un-ingest
        dry_run: If True, only report what would be removed
        keep_imported: If True, preserve raw/imported/<slug>/

    Returns:
        Dict with lists of removed paths
    """
    wiki_root = Path("wiki")
    raw_root = Path("raw")
    tmp_root = Path(".tmp")

    result = {
        "source_page": None,
        "synthesized_pages": [],
        "analysis_pages": [],
        "normalized_dir": None,
        "imported_dir": None,
        "extract_state": None,
        "errors": [],
    }

    # 1. Find source page
    source_page = wiki_root / "sources" / f"{slug}.md"
    if source_page.exists():
        result["source_page"] = source_page

    # 2. Find synthesized pages linked from source
    if source_page.exists():
        result["synthesized_pages"] = find_synthesized_pages(source_page)

    # 3. Find analysis pages citing this source
    result["analysis_pages"] = find_analysis_pages(
        slug, wiki_root / "analyses")

    # 4. Find normalized source directory
    normalized_dir = raw_root / "normalized" / slug
    if normalized_dir.exists():
        result["normalized_dir"] = normalized_dir

    # 5. Find imported original directory
    imported_dir = raw_root / "imported" / slug
    if imported_dir.exists():
        result["imported_dir"] = imported_dir

    # 6. Find extraction state
    extract_state = tmp_root / "deep-extract" / slug
    if extract_state.exists():
        result["extract_state"] = extract_state

    if dry_run:
        return result

    # Execute removal
    removed_paths = []

    # Remove synthesized pages first
    for page in result["synthesized_pages"]:
        try:
            page.unlink()
            removed_paths.append(str(page))
        except Exception as e:
            result["errors"].append(f"Failed to remove {page}: {e}")

    # Remove analysis pages (with warning)
    for page in result["analysis_pages"]:
        try:
            page.unlink()
            removed_paths.append(str(page))
        except Exception as e:
            result["errors"].append(f"Failed to remove {page}: {e}")

    # Remove source page
    if result["source_page"] and result["source_page"].exists():
        try:
            result["source_page"].unlink()
            removed_paths.append(str(result["source_page"]))
        except Exception as e:
            result["errors"].append(f"Failed to remove source page: {e}")

    # Remove normalized directory
    if result["normalized_dir"] and result["normalized_dir"].exists():
        try:
            shutil.rmtree(result["normalized_dir"])
            removed_paths.append(str(result["normalized_dir"]))
        except Exception as e:
            result["errors"].append(f"Failed to remove normalized dir: {e}")

    # Remove imported directory (unless keep_imported)
    if not keep_imported and result["imported_dir"] and result["imported_dir"].exists():
        try:
            shutil.rmtree(result["imported_dir"])
            removed_paths.append(str(result["imported_dir"]))
        except Exception as e:
            result["errors"].append(f"Failed to remove imported dir: {e}")

    # Remove extraction state
    if result["extract_state"] and result["extract_state"].exists():
        try:
            shutil.rmtree(result["extract_state"])
            removed_paths.append(str(result["extract_state"]))
        except Exception as e:
            result["errors"].append(f"Failed to remove extraction state: {e}")

    result["removed_paths"] = removed_paths
    return result


def print_result(result: dict, dry_run: bool):
    """Print un-ingest results."""
    action = "Would remove" if dry_run else "Removed"

    print(f"\n{'DRY RUN: ' if dry_run else ''}Un-ingest Summary")
    print("=" * 50)

    if result["source_page"]:
        print(f"\nSource page:")
        print(f"  {action}: {result['source_page']}")
    else:
        print("\nSource page: not found")

    if result["synthesized_pages"]:
        print(f"\nSynthesized pages ({len(result['synthesized_pages'])}):")
        for page in result["synthesized_pages"]:
            print(f"  {action}: {page}")
    else:
        print("\nSynthesized pages: none found")

    if result["analysis_pages"]:
        print(
            f"\nAnalysis pages citing source ({len(result['analysis_pages'])}):")
        for page in result["analysis_pages"]:
            print(f"  {action}: {page}")

    if result["normalized_dir"]:
        print(f"\nNormalized source:")
        print(f"  {action}: {result['normalized_dir']}/")
    else:
        print("\nNormalized source: not found")

    if result["imported_dir"]:
        print(f"\nImported original:")
        print(f"  {action}: {result['imported_dir']}/")
    else:
        print("\nImported original: not found")

    if result["extract_state"]:
        print(f"\nExtraction state:")
        print(f"  {action}: {result['extract_state']}/")

    if result.get("errors"):
        print(f"\nErrors:")
        for error in result["errors"]:
            print(f"  ERROR: {error}")

    if not dry_run and result.get("removed_paths"):
        print(f"\nTotal items removed: {len(result['removed_paths'])}")
        print("\nRun these commands to update wiki bookkeeping:")
        print("  pnpm wiki:index")
        print("  pnpm wiki:graph")


def main():
    parser = argparse.ArgumentParser(
        description="Un-ingest a source: remove all wiki pages and raw files created during ingest."
    )
    parser.add_argument("slug", help="Source slug to un-ingest")
    parser.add_argument("--dry-run", action="store_true",
                        help="Only show what would be removed")
    parser.add_argument("--keep-imported", action="store_true",
                        help="Keep raw/imported/<slug>/")
    parser.add_argument("--update-bookkeeping", action="store_true",
                        help="Run index and graph updates after removal")
    args = parser.parse_args()

    result = uningest(args.slug, dry_run=args.dry_run,
                      keep_imported=args.keep_imported)
    print_result(result, args.dry_run)

    if not args.dry_run and args.update_bookkeeping:
        import subprocess
        print("\nUpdating wiki bookkeeping...")
        subprocess.run(["pnpm", "wiki:index"], check=False)
        subprocess.run(["pnpm", "wiki:graph"], check=False)
        print("Done.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
