#!/usr/bin/env python3
"""Fix fabricated evidence in wiki pages by replacing with actual source text.

The model often hallucinates evidence text even when given correct locators.
This tool deterministically replaces evidence cells with the actual text from
the cited source lines.

Usage:
    python3 tools/wiki_fix_evidence.py wiki/concepts/functions.md --normalized-source raw/normalized/js-allonge/source.md
    python3 tools/wiki_fix_evidence.py wiki/concepts/functions.md --slug js-allonge
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fix fabricated evidence by replacing with actual source text")
    parser.add_argument("page", help="wiki page to fix")
    parser.add_argument("--normalized-source", help="path to normalized source markdown")
    parser.add_argument("--slug", help="source slug (auto-finds normalized source)")
    parser.add_argument("--dry-run", action="store_true", help="show changes without writing")
    parser.add_argument("--force", action="store_true", 
                        help="always replace evidence, even if it seems to match")
    parser.add_argument("--max-evidence-chars", type=int, default=300,
                        help="max chars for evidence excerpt")
    args = parser.parse_args()

    page_path = Path(args.page)
    if not page_path.exists():
        print(f"FAIL: page not found: {page_path}", file=sys.stderr)
        return 1

    # Find normalized source
    if args.normalized_source:
        source_path = Path(args.normalized_source)
    elif args.slug:
        source_path = Path(f"raw/normalized/{args.slug}/source.md")
    else:
        # Try to extract slug from page sources frontmatter
        source_path = find_source_from_page(page_path)
        if source_path is None:
            print("FAIL: could not determine normalized source; use --slug or --normalized-source", file=sys.stderr)
            return 1

    if not source_path.exists():
        print(f"FAIL: normalized source not found: {source_path}", file=sys.stderr)
        return 1

    # Load source lines
    source_text = source_path.read_text(errors="ignore")
    source_lines = source_text.splitlines()

    # Fix evidence in page
    page_text = page_path.read_text()
    fixed_text, changes = fix_evidence_in_page(
        page_text, source_lines, args.max_evidence_chars, force=args.force
    )

    if not changes:
        print(f"No evidence fixes needed in {page_path}")
        return 0

    print(f"Fixed {len(changes)} evidence cells in {page_path}:")
    for change in changes:
        print(f"  - Row {change['row']}: {change['locator']}")
        if args.dry_run:
            print(f"    OLD: {change['old'][:80]}...")
            print(f"    NEW: {change['new'][:80]}...")

    if not args.dry_run:
        page_path.write_text(fixed_text)
        print(f"Wrote {page_path}")

    return 0


def find_source_from_page(page_path: Path) -> Path | None:
    """Extract source slug from page frontmatter or source links."""
    text = page_path.read_text()
    
    # Try to find source slug from sources frontmatter
    match = re.search(r"sources:\s*\n\s*-\s*\.\.\/sources\/([^/\n]+)\.md", text)
    if match:
        slug = match.group(1)
        return Path(f"raw/normalized/{slug}/source.md")
    
    # Try to find from source_ranges frontmatter
    match = re.search(r"source_ranges:\s*\n\s*-\s*([^:]+):normalized:", text)
    if match:
        slug = match.group(1)
        return Path(f"raw/normalized/{slug}/source.md")
    
    return None


def fix_evidence_in_page(
    page_text: str, source_lines: list[str], max_chars: int, force: bool = False
) -> tuple[str, list[dict]]:
    """Fix evidence cells in a page by replacing with actual source text.
    
    Args:
        page_text: The wiki page content
        source_lines: Lines from the normalized source
        max_chars: Maximum characters for evidence excerpts
        force: If True, always replace evidence regardless of similarity
    
    Returns:
        Tuple of (fixed_text, list of changes made)
    """
    lines = page_text.splitlines()
    changes: list[dict] = []
    fixed_lines: list[str] = []
    
    in_table = False
    header_cols: list[str] = []
    evidence_col_idx = -1
    locator_col_idx = -1
    row_num = 0
    
    for line in lines:
        stripped = line.strip()
        
        # Detect table start (header row)
        if stripped.startswith("|") and stripped.endswith("|") and not in_table:
            cols = parse_table_row(stripped)
            if cols:
                # Check if this looks like an evidence table header
                cols_lower = [c.lower() for c in cols]
                if "evidence" in cols_lower and "locator" in cols_lower:
                    in_table = True
                    header_cols = cols
                    evidence_col_idx = cols_lower.index("evidence")
                    locator_col_idx = cols_lower.index("locator")
                    row_num = 0
                    fixed_lines.append(line)
                    continue
        
        # Skip separator row
        if in_table and is_separator_row(stripped):
            fixed_lines.append(line)
            continue
        
        # Process data rows
        if in_table and stripped.startswith("|") and stripped.endswith("|"):
            cols = parse_table_row(stripped)
            if cols and len(cols) >= max(evidence_col_idx, locator_col_idx) + 1:
                row_num += 1
                evidence = cols[evidence_col_idx]
                locator = cols[locator_col_idx]
                
                # Extract line number(s) from locator
                parsed = parse_locator(locator)
                if parsed is not None:
                    start_line, end_line = parsed
                    if 1 <= start_line <= len(source_lines):
                        actual_text = get_evidence_excerpt(source_lines, start_line, end_line, max_chars)
                        
                        # Decide whether to replace
                        evidence_clean = evidence.strip('"\'').strip()
                        actual_clean = actual_text.strip()
                        
                        should_replace = force or not texts_match(evidence_clean, actual_clean)
                        
                        if should_replace and actual_clean:
                            old_evidence = evidence
                            new_evidence = f'"{actual_text}"'
                            cols[evidence_col_idx] = new_evidence
                            line = format_table_row(cols)
                            changes.append({
                                "row": row_num,
                                "locator": locator,
                                "old": old_evidence,
                            "new": new_evidence,
                        })
        
        # End of table detection
        if in_table and not stripped.startswith("|"):
            in_table = False
            header_cols = []
            evidence_col_idx = -1
            locator_col_idx = -1
        
        fixed_lines.append(line)
    
    return "\n".join(fixed_lines), changes


def parse_table_row(line: str) -> list[str] | None:
    """Parse a markdown table row into cells."""
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    # Remove leading/trailing pipes and split
    inner = stripped[1:-1]
    return [cell.strip() for cell in inner.split("|")]


def is_separator_row(line: str) -> bool:
    """Check if a line is a table separator row (e.g., | --- | --- |)."""
    if not line.startswith("|") or not line.endswith("|"):
        return False
    inner = line[1:-1]
    cells = inner.split("|")
    return all(cell.strip() and set(cell.strip()) <= {"-", ":", " "} for cell in cells)


def format_table_row(cols: list[str]) -> str:
    """Format cells back into a markdown table row."""
    return "| " + " | ".join(cols) + " |"


def parse_locator(locator: str) -> tuple[int, int | None] | None:
    """Extract line number(s) from a locator.
    
    Returns:
        Tuple of (start_line, end_line) where end_line may be None for single-line locators.
        Or None if parsing fails.
    """
    # Remove backticks
    locator = locator.strip("`")
    
    # Match range pattern like normalized:L123-L456 or normalized:L123-456
    match = re.search(r"normalized:L(\d+)[-–]L?(\d+)", locator)
    if match:
        return int(match.group(1)), int(match.group(2))
    
    # Match single line pattern like normalized:L123
    match = re.search(r"normalized:L(\d+)", locator)
    if match:
        return int(match.group(1)), None
    
    # Also try slug:normalized:L123-L456
    match = re.search(r":normalized:L(\d+)[-–]L?(\d+)", locator)
    if match:
        return int(match.group(1)), int(match.group(2))
    
    match = re.search(r":normalized:L(\d+)", locator)
    if match:
        return int(match.group(1)), None
    
    return None


def get_evidence_excerpt(source_lines: list[str], start_line: int, end_line: int | None, max_chars: int) -> str:
    """Get an evidence excerpt from the source lines.
    
    Gets text from start_line to end_line (or just start_line if end_line is None).
    Does NOT extend beyond the specified range, as the locator defines exactly
    which lines the evidence should come from.
    """
    if start_line < 1 or start_line > len(source_lines):
        return ""
    
    # Determine the range of lines to use
    start_idx = start_line - 1
    end_idx = (end_line - 1) if end_line else start_idx
    
    # Ensure end is within bounds
    end_idx = min(end_idx, len(source_lines) - 1)
    
    # Get all lines in the range
    excerpt_lines = [source_lines[i].strip() for i in range(start_idx, end_idx + 1)]
    excerpt = " ".join(line for line in excerpt_lines if line)
    
    # Truncate if too long
    if len(excerpt) > max_chars:
        truncated = excerpt[:max_chars]
        last_space = truncated.rfind(" ")
        if last_space > max_chars // 2:
            truncated = truncated[:last_space]
        excerpt = truncated
    
    # Escape pipe characters for table cells
    excerpt = excerpt.replace("|", "/")
    
    return excerpt


def texts_match(evidence: str, source_text: str, threshold: float = 0.9) -> bool:
    """Check if evidence exactly matches (or is contained in) the source text.
    
    Returns True ONLY if the evidence text is found IN the source text.
    This is strict because validation checks that evidence appears in the cited lines.
    
    If the evidence is LONGER than the source (model fabricated extra text), we return
    False so the evidence gets replaced with the actual source text.
    
    Args:
        evidence: The evidence text from the wiki page's evidence cell
        source_text: The actual text from the normalized source at the cited line(s)
    """
    # Normalize for comparison
    ev = evidence.lower().replace('"', '').replace("'", "").strip()
    src = source_text.lower().replace('"', '').replace("'", "").strip()
    
    # Direct match
    if ev == src:
        return True
    
    # Evidence must be found IN the source text (not the other way around!)
    # If evidence is longer than source, validation will fail, so we must replace
    if ev in src:
        return True
    
    return False


if __name__ == "__main__":
    sys.exit(main())
