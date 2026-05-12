#!/usr/bin/env python3
"""Normalize evidence cells deterministically from locators or evidence IDs.

This replaces the need for LLMs to write evidence text. The LLM outputs
a 2-column table (Claim | [stable-id]), and this script keeps that canonical
2-column shape while normalizing any prompt-local or hybrid table output.

Usage:
    python3 tools/wiki_fill_evidence.py wiki/concepts/example.md --source raw/normalized/slug/source.md
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

# Import from refactored packages
from wiki_io.evidence import canonicalize_for_evidence_match, EvidenceResolver

if TYPE_CHECKING:
    from wiki_phase2_benchmark import EvidenceBankResult


@dataclass
class EvidenceExpansion:
    """Record of an evidence expansion."""
    row: int
    evidence_id: str | None
    locator: str
    evidence: str


def make_table_safe(text: str, max_len: int = 200) -> str:
    """Make text safe for markdown table cells.

    - Collapses all whitespace (including newlines) to single spaces
    - Escapes pipe characters
    - Truncates long text with ellipsis
    """
    # Collapse all whitespace to single spaces
    safe = " ".join(text.split())
    # Escape pipe characters
    safe = safe.replace("|", "\\|")
    # Truncate if too long
    if len(safe) > max_len:
        safe = safe[:max_len - 3].rsplit(" ", 1)[0] + "..."
    return safe


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fill evidence cells from locators (deterministic)")
    parser.add_argument("page", help="wiki page to process")
    parser.add_argument("--source", required=True,
                        help="normalized source markdown")
    parser.add_argument("--dry-run", action="store_true",
                        help="show changes without writing")
    parser.add_argument("--max-evidence-chars", type=int, default=200,
                        help="max chars for evidence excerpt")
    args = parser.parse_args()

    page_path = Path(args.page)
    source_path = Path(args.source)

    if not page_path.exists():
        print(f"FAIL: page not found: {page_path}", file=sys.stderr)
        return 1

    if not source_path.exists():
        print(f"FAIL: source not found: {source_path}", file=sys.stderr)
        return 1

    source_lines = source_path.read_text(errors="ignore").splitlines()
    page_text = page_path.read_text()

    result, changes = fill_evidence_in_page(
        page_text, source_lines, args.max_evidence_chars)

    if not changes:
        print(f"No evidence fills needed in {page_path}")
        return 0

    print(f"Filled {len(changes)} evidence cell(s) in {page_path}")
    for change in changes:
        if args.dry_run:
            print(f"  Row {change['row']}: {change['locator']}")
            print(f"    Evidence: {change['evidence'][:60]}...")

    if not args.dry_run:
        page_path.write_text(result)

    return 0


def expand_evidence_ids(
    page_text: str,
    evidence_bank: "EvidenceBankResult",
    slug: str,
) -> tuple[str, list[dict]]:
    """Normalize evidence-ID tables to the canonical 2-column wiki format.

    Input: | Claim | [source:claim_id] |
    Output: | Claim | Evidence |

    Args:
        page_text: Page content with evidence ID citations
        evidence_bank: EvidenceBankResult with ID -> evidence mapping.
        slug: Source slug.

    Returns:
        Tuple of (transformed_text, list of expansions)
    """
    lines = page_text.splitlines()
    result_lines: list[str] = []
    expansions: list[dict] = []

    in_table = False
    table_type = None  # "2col_id", "reference_id"
    evidence_index = -1
    row_num = 0

    for line in lines:
        stripped = line.strip()

        # Detect table start
        if stripped.startswith("|") and stripped.endswith("|") and not in_table:
            cols = parse_table_row(stripped)
            if cols:
                cols_lower = [c.lower() for c in cols]

                # Check for canonical 2-column ID format: | Claim | Evidence |
                if len(cols) == 2 and "claim" in cols_lower and "evidence" in cols_lower:
                    in_table = True
                    table_type = "2col_id"
                    evidence_index = cols_lower.index("evidence")
                    row_num = 0
                    result_lines.append("| Claim | Evidence |")
                    continue

                # Legacy/hybrid model output:
                # | Claim | Evidence | Locator | Source |
                # where Evidence is still an ID. Strip renderer-owned columns.
                if len(cols) == 4 and cols_lower == ["claim", "evidence", "locator", "source"]:
                    in_table = True
                    table_type = "4col_id"
                    evidence_index = 1
                    row_num = 0
                    result_lines.append("| Claim | Evidence |")
                    continue

                # Check for ID-based reference data:
                # | Item | Supported fact | Evidence |
                if len(cols) >= 3 and "evidence" in cols_lower and "locator" not in cols_lower:
                    in_table = True
                    table_type = "reference_id"
                    evidence_index = cols_lower.index("evidence")
                    row_num = 0
                    result_lines.append(format_table_row(cols))
                    continue

        # Transform separator row
        if in_table and is_separator_row(stripped):
            if table_type == "reference_id":
                result_lines.append(line)
            else:
                result_lines.append("| --- | --- |")
            continue

        # Process data rows with evidence IDs
        if in_table and stripped.startswith("|") and stripped.endswith("|"):
            cols = parse_table_row(stripped)

            if cols and table_type in {"2col_id", "4col_id"} and len(cols) >= 2:
                row_num += 1
                claim = cols[0]
                evidence_cell = cols[evidence_index].strip()

                ids = evidence_ids_from_cell(evidence_cell)
                had_ids = bool(ids)
                if not ids:
                    matched_id = evidence_id_for_excerpt(
                        evidence_cell, evidence_bank, slug)
                    ids = [matched_id] if matched_id else []
                canonical_ids = []
                for evidence_id in ids:
                    item = resolved_evidence_tuple(
                        evidence_id, evidence_bank, slug)
                    if item:
                        item_id, locator, evidence = item
                        canonical_ids.append(item_id)
                        expansions.append({
                            "row": row_num,
                            "id": item_id,
                            "locator": locator,
                            "evidence": evidence,
                        })
                if canonical_ids:
                    new_cols = [
                        make_table_safe(claim),
                        ", ".join(f"[{eid}]" for eid in canonical_ids),
                    ]
                    result_lines.append(format_table_row(new_cols))
                    continue

                if not had_ids:
                    # The model wrote an excerpt that is not backed by a known
                    # claim ID. Drop it so validation does not adopt an
                    # unresolvable evidence row.
                    continue

                # If an explicit ID was invalid, keep the row so validation
                # reports the bad ID clearly.
                result_lines.append(line)
                continue

            if cols and table_type == "reference_id" and len(cols) >= 3 and evidence_index < len(cols):
                row_num += 1
                evidence_cell = cols[evidence_index].strip()

                ids = evidence_ids_from_cell(evidence_cell)
                had_ids = bool(ids)
                if not ids:
                    matched_id = evidence_id_for_excerpt(
                        evidence_cell, evidence_bank, slug)
                    ids = [matched_id] if matched_id else []
                canonical_ids = []
                for evidence_id in ids:
                    item = resolved_evidence_tuple(
                        evidence_id, evidence_bank, slug)
                    if item:
                        item_id, locator, evidence = item
                        canonical_ids.append(item_id)
                        expansions.append({
                            "row": row_num,
                            "id": item_id,
                            "locator": locator,
                            "evidence": evidence,
                        })
                if canonical_ids:
                    new_cols = (
                        [make_table_safe(cell)
                         for cell in cols[:evidence_index]]
                        + [", ".join(f"[{eid}]" for eid in canonical_ids)]
                        + [make_table_safe(cell)
                           for cell in cols[evidence_index + 1:]]
                    )
                    result_lines.append(format_table_row(new_cols))
                    continue

                if not had_ids:
                    continue

                result_lines.append(line)
                continue

        # End of table detection
        if in_table and stripped and not stripped.startswith("|"):
            in_table = False
            table_type = None

        result_lines.append(line)

    return "\n".join(result_lines), expansions


def evidence_ids_from_cell(cell: str) -> list[str]:
    ids = re.findall(r"\[([A-Za-z0-9_:-]+)\]", cell)
    if ids:
        return ids
    stripped = cell.strip().strip("`")
    if re.fullmatch(r"[A-Za-z0-9_:-]+", stripped):
        return [stripped]
    return []


def resolved_evidence_tuple(
    evidence_id: str,
    evidence_bank: "EvidenceBankResult",
    slug: str,
) -> tuple[str, str, str] | None:
    item = evidence_bank.items.get(
        evidence_id) or evidence_bank.items.get(evidence_id.upper())
    if item:
        return item.id, item.locator, item.exact_text
    resolver = EvidenceResolver.for_slug(slug) if slug else None
    resolved = resolver.resolve(evidence_id) if resolver else None
    if resolved:
        return resolved.evidence_id, resolved.locator, resolved.evidence
    return None


def evidence_id_for_excerpt(cell: str, evidence_bank: "EvidenceBankResult", slug: str = "") -> str | None:
    needle = evidence_match_key(cell)
    if not needle:
        return None
    best_id: str | None = None
    best_len = 0
    for evidence_id, item in evidence_bank.items.items():
        candidates = [
            item.exact_text,
            item.display_text,
        ]
        for candidate in candidates:
            haystack = evidence_match_key(candidate)
            if not haystack:
                continue
            if needle == haystack or needle in haystack or haystack in needle:
                score = min(len(needle), len(haystack))
                if score > best_len:
                    best_id = evidence_id
                    best_len = score
    if best_id is not None or not slug:
        return best_id

    resolver = EvidenceResolver.for_slug(slug)
    if resolver is None:
        return None
    for item in resolver._items.values():
        haystack = evidence_match_key(item.evidence)
        if not haystack:
            continue
        if needle == haystack or needle in haystack or haystack in needle:
            score = min(len(needle), len(haystack))
            if score > best_len:
                best_id = item.evidence_id
                best_len = score
    return best_id


def evidence_match_key(text: str) -> str:
    key = canonicalize_for_evidence_match(
        strip_outer_quotes(text).replace("**", "").replace("*", ""))
    key = key.replace('"', "").replace("'", "")
    key = key.replace("•", "")
    return " ".join(key.split())


def strip_outer_quotes(text: str) -> str:
    stripped = text.strip()
    if (stripped.startswith('"') and stripped.endswith('"')) or (
        stripped.startswith("'") and stripped.endswith("'")
    ):
        return stripped[1:-1].strip()
    return stripped


def fill_evidence_in_page(
    page_text: str,
    source_lines: list[str],
    max_chars: int = 200,
) -> tuple[str, list[dict]]:
    """Fill evidence cells from locators in a wiki page.

    Handles multiple table formats:
    1. 3-column: | Claim | Locator | Source | -> expands to 4-column with Evidence
    2. 4-column reference: | Item | Fact | Locator | Source | -> expands to 5-column with Evidence
    3. 4-column with placeholder: | Claim | {{FILL}} | Locator | Source | -> fills placeholder

    Returns:
        Tuple of (transformed_text, list of changes)
    """
    lines = page_text.splitlines()
    changes: list[dict] = []
    result_lines: list[str] = []

    in_table = False
    table_type = None  # "3col_claim", "4col_reference", "4col_placeholder"
    header_transformed = False
    separator_transformed = False
    row_num = 0

    for line in lines:
        stripped = line.strip()

        # Detect table start
        if stripped.startswith("|") and stripped.endswith("|") and not in_table:
            cols = parse_table_row(stripped)
            if cols:
                cols_lower = [c.lower() for c in cols]

                # Check for 3-column claim format: Claim | Locator | Source
                if len(cols) == 3 and "claim" in cols_lower and "locator" in cols_lower:
                    in_table = True
                    table_type = "3col_claim"
                    header_transformed = False
                    separator_transformed = False
                    row_num = 0
                    # Transform header to 4-column
                    locator_idx = cols_lower.index("locator")
                    new_cols = cols[:locator_idx] + \
                        ["Evidence"] + cols[locator_idx:]
                    result_lines.append(format_table_row(new_cols))
                    header_transformed = True
                    continue

                # Check for 4-column reference data format: Item | Fact | Locator | Source
                if len(cols) == 4 and "item" in cols_lower and "locator" in cols_lower and "evidence" not in cols_lower:
                    in_table = True
                    table_type = "4col_reference"
                    header_transformed = False
                    separator_transformed = False
                    row_num = 0
                    # Transform header to 5-column
                    locator_idx = cols_lower.index("locator")
                    new_cols = cols[:locator_idx] + \
                        ["Evidence"] + cols[locator_idx:]
                    result_lines.append(format_table_row(new_cols))
                    header_transformed = True
                    continue

                # Check for 4-column with placeholder evidence
                if len(cols) == 4 and "claim" in cols_lower and "evidence" in cols_lower:
                    in_table = True
                    table_type = "4col_placeholder"
                    row_num = 0

        # Transform separator row for 3-col -> 4-col or 4-col -> 5-col
        if in_table and table_type in ("3col_claim", "4col_reference") and not separator_transformed and is_separator_row(stripped):
            cols = parse_table_row(stripped)
            if cols:
                expected_cols = 3 if table_type == "3col_claim" else 4
                if len(cols) == expected_cols:
                    # Insert separator for Evidence column
                    insert_idx = 1 if table_type == "3col_claim" else 2
                    new_cols = cols[:insert_idx] + ["---"] + cols[insert_idx:]
                    result_lines.append(format_table_row(new_cols))
                    separator_transformed = True
                    continue

        # Process data rows
        if in_table and stripped.startswith("|") and stripped.endswith("|"):
            cols = parse_table_row(stripped)

            if cols and table_type == "3col_claim" and len(cols) == 3:
                # 3-column: Claim | Locator | Source -> Claim | Evidence | Locator | Source
                row_num += 1
                claim = cols[0]
                locator = cols[1]
                source = cols[2]

                evidence = get_evidence_for_locator(
                    locator, source_lines, max_chars)
                if evidence:
                    new_cols = [make_table_safe(
                        claim), f'"{make_table_safe(evidence)}"', locator, source]
                    result_lines.append(format_table_row(new_cols))
                    changes.append({
                        "row": row_num,
                        "locator": locator,
                        "evidence": evidence,
                    })
                    continue

            elif cols and table_type == "4col_reference" and len(cols) == 4:
                # 4-column: Item | Fact | Locator | Source -> Item | Fact | Evidence | Locator | Source
                row_num += 1
                item = cols[0]
                fact = cols[1]
                locator = cols[2]
                source = cols[3]

                evidence = get_evidence_for_locator(
                    locator, source_lines, max_chars)
                if evidence:
                    new_cols = [make_table_safe(item), make_table_safe(
                        fact), f'"{make_table_safe(evidence)}"', locator, source]
                    result_lines.append(format_table_row(new_cols))
                    changes.append({
                        "row": row_num,
                        "locator": locator,
                        "evidence": evidence,
                    })
                    continue

            elif cols and table_type == "4col_placeholder" and len(cols) == 4:
                # 4-column with placeholder: check if evidence needs filling
                row_num += 1
                evidence_cell = cols[1].strip()
                locator = cols[2]

                # Check for placeholder markers
                if is_placeholder(evidence_cell):
                    evidence = get_evidence_for_locator(
                        locator, source_lines, max_chars)
                    if evidence:
                        cols[1] = f'"{make_table_safe(evidence)}"'
                        result_lines.append(format_table_row(cols))
                        changes.append({
                            "row": row_num,
                            "locator": locator,
                            "evidence": evidence,
                        })
                        continue

        # End of table detection
        if in_table and stripped and not stripped.startswith("|"):
            in_table = False
            table_type = None

        result_lines.append(line)

    return "\n".join(result_lines), changes


def is_placeholder(text: str) -> bool:
    """Check if evidence cell is a placeholder."""
    text = text.strip().lower()
    placeholders = [
        "{{fill}}",
        "{{evidence}}",
        "[fill]",
        "[evidence]",
        "fill",
        "evidence",
        "...",
        "—",
        "-",
        "",
    ]
    return text in placeholders or text.startswith("{{") or text.startswith("[fill")


def get_evidence_for_locator(locator: str, source_lines: list[str], max_chars: int) -> str | None:
    """Extract evidence text from source at the given locator."""
    # Parse locator: normalized:L123 or normalized:L123-L456
    match = re.search(r'L(\d+)(?:-L?(\d+))?', locator)
    if not match:
        return None

    start_line = int(match.group(1))
    end_line = int(match.group(2)) if match.group(2) else start_line

    if start_line < 1 or start_line > len(source_lines):
        return None

    # Clamp end_line
    end_line = min(end_line, len(source_lines))

    # Extract lines (1-indexed)
    extracted = []
    for i in range(start_line - 1, end_line):
        if i < len(source_lines):
            extracted.append(source_lines[i])

    text = " ".join(extracted).strip()

    # Truncate if needed
    if len(text) > max_chars:
        text = text[:max_chars].rsplit(" ", 1)[0] + "..."

    return text if text else None


def parse_table_row(line: str) -> list[str] | None:
    """Parse a markdown table row into cells."""
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    inner = stripped[1:-1]
    return [cell.strip() for cell in inner.split("|")]


def is_separator_row(line: str) -> bool:
    """Check if a line is a table separator row."""
    if not line.startswith("|") or not line.endswith("|"):
        return False
    inner = line[1:-1]
    cells = inner.split("|")
    return all(cell.strip() and set(cell.strip()) <= {"-", ":", " "} for cell in cells)


def format_table_row(cols: list[str]) -> str:
    """Format cells into a markdown table row."""
    return "| " + " | ".join(cols) + " |"


if __name__ == "__main__":
    sys.exit(main())
