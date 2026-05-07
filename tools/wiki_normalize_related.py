#!/usr/bin/env python3
"""Normalize Related pages and Candidate pages sections.

This post-processor ensures clean wiki graph hygiene:
- Related pages: Only Markdown links to existing pages
- Candidate pages: Plain text names for uncreated concepts

Usage:
    python3 tools/wiki_normalize_related.py <slug>
    python3 tools/wiki_normalize_related.py <slug> --page wiki/concepts/example.md
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


def normalize_related_sections(content: str, wiki_root: Path, page_path: Path) -> tuple[str, bool]:
    """Normalize Related pages and Candidate pages sections.

    Moves "(not created yet)" entries from Related pages to Candidate pages.
    Returns (new_content, changed).
    """
    lines = content.splitlines(keepends=True)

    related_start = None
    related_end = None
    candidate_start = None
    candidate_end = None
    source_pages_start = None

    # Find section boundaries
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("## Related pages"):
            related_start = i
        elif stripped.startswith("## Candidate pages"):
            candidate_start = i
        elif stripped.startswith("## Source pages"):
            source_pages_start = i
        elif stripped.startswith("## ") and related_start is not None and related_end is None:
            related_end = i
        elif stripped.startswith("## ") and candidate_start is not None and candidate_end is None:
            candidate_end = i

    if related_start is None:
        return content, False

    # Find end of related section if not set
    if related_end is None:
        related_end = len(lines)
        for i in range(related_start + 1, len(lines)):
            if lines[i].strip().startswith("## "):
                related_end = i
                break

    # Extract Related pages section content
    related_lines = lines[related_start + 1:related_end]

    # Separate valid links from uncreated page mentions
    valid_links = []
    uncreated_pages = []

    for line in related_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("|"):
            # Skip empty lines and table formatting
            continue

        # Check for "(not created yet)" pattern
        not_created_match = re.search(
            r'^-?\s*(.+?)\s*\(not created(?:\s+yet)?\)', stripped, re.IGNORECASE)
        if not_created_match:
            page_name = not_created_match.group(1).strip()
            # Remove any link formatting
            link_match = re.match(r'\[([^\]]+)\]', page_name)
            if link_match:
                page_name = link_match.group(1)
            uncreated_pages.append(page_name)
            continue

        # Check for Markdown links
        link_match = re.search(r'\[([^\]]+)\]\(([^)]+\.md)\)', stripped)
        if link_match:
            link_text, link_target = link_match.groups()
            # Resolve relative path from page location
            target_path = (page_path.parent / link_target).resolve()
            if target_path.exists():
                valid_links.append(stripped)
            else:
                # Broken link - move to candidates
                uncreated_pages.append(link_text)
            continue

        # Plain text that looks like a page reference
        if stripped.startswith("-"):
            page_name = stripped[1:].strip()
            if page_name and not page_name.startswith("["):
                uncreated_pages.append(page_name)
            continue

        # Keep anything else (like valid links)
        valid_links.append(stripped)

    if not uncreated_pages:
        return content, False

    # Build new Related pages section
    new_related = ["## Related pages\n", "\n"]
    for link in valid_links:
        if not link.startswith("-"):
            new_related.append(f"- {link}\n")
        else:
            new_related.append(f"{link}\n")
    if not valid_links:
        new_related.append("None.\n")
    new_related.append("\n")

    # Build Candidate pages section
    new_candidate = ["## Candidate pages\n", "\n"]
    for page_name in sorted(set(uncreated_pages)):
        new_candidate.append(f"- {page_name}\n")
    new_candidate.append("\n")

    # Reconstruct content
    new_lines = lines[:related_start]
    new_lines.extend(new_related)

    # Add Candidate pages before Source pages if it exists, otherwise before next section
    if candidate_start is not None:
        # Replace existing Candidate pages section
        if candidate_end is None:
            candidate_end = len(lines)
        remaining_start = candidate_end
    elif source_pages_start is not None:
        # Insert before Source pages
        remaining_start = source_pages_start
    else:
        # Insert before end
        remaining_start = related_end

    new_lines.extend(new_candidate)

    # Add remaining content
    # Skip old related section end if we're inserting candidate pages there
    if candidate_start is None:
        new_lines.extend(lines[remaining_start:])
    else:
        new_lines.extend(lines[remaining_start:])

    new_content = "".join(new_lines)
    return new_content, new_content != content


def normalize_page(page: Path, wiki_root: Path) -> bool:
    """Normalize a single page's Related/Candidate sections. Returns True if changed."""
    if not page.exists():
        return False

    content = page.read_text()
    new_content, changed = normalize_related_sections(content, wiki_root, page)

    if changed:
        page.write_text(new_content)
        print(f"updated {page}")
        return True
    return False


def normalize_slug(slug: str, wiki_root: Path) -> int:
    """Normalize all synthesized pages for a source slug. Returns count of changed files."""
    changed = 0

    # Find all synthesized pages that might reference this source
    for subdir in ["concepts", "entities", "procedures", "references"]:
        subdir_path = wiki_root / subdir
        if not subdir_path.exists():
            continue
        for page in subdir_path.glob("*.md"):
            if normalize_page(page, wiki_root):
                changed += 1

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normalize Related pages and Candidate pages sections.")
    parser.add_argument("slug", help="Source slug to normalize pages for")
    parser.add_argument("--page", type=Path,
                        help="Normalize a specific page only")
    parser.add_argument("--wiki-root", type=Path, default=Path("wiki"),
                        help="Wiki root directory")
    args = parser.parse_args()

    wiki_root = args.wiki_root

    if args.page:
        changed = normalize_page(args.page, wiki_root)
        if not changed:
            print(f"no related-page normalization needed for {args.page}")
        return 0

    changed = normalize_slug(args.slug, wiki_root)
    if changed == 0:
        print(f"no related-page normalization needed for {args.slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
