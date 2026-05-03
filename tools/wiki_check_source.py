#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from wiki_common import (
    SOURCE_HEADINGS,
    bullet_count,
    code_paths,
    content_tokens,
    h2_headings,
    markdown_links,
    parse_frontmatter,
    section,
)


REQUIRED_SOURCE_KEYS = [
    "title",
    "type",
    "source_id",
    "source_type",
    "raw_path",
    "normalized_path",
    "status",
    "last_updated",
    "tags",
    "sources",
]

FORBIDDEN_PATTERNS = [
    r"DE \(Dark Age\)",
    r"created as part of ingestion",
    r"created during ingestion",
    r"self-referential",
    r"AoE2 community forums",
    r"Tournament strategies",
]

METADATA_CLAIM_PATTERNS = [
    r"\bguide\b",
    r"\bauthor\b",
    r"\bdocument\b",
    r"\bcoached?\b",
    r"\bTwitch\b",
    r"\bGoogle Docs\b",
    r"\bpublished\b",
]

WEAK_CLAIM_PATTERNS = [
    r"\bfundamental\b",
    r"\bimportant\b",
    r"\bcrucial\b",
    r"\bessential\b",
    r"\bsuccess\b",
]

RELATED_PRIORITIES = {"must create", "should create", "could create", "defer"}
RELATED_STATUSES = {"not created yet", "created"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate one wiki source page.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("--min-claims", type=int, default=8)
    parser.add_argument("--max-claims", type=int)
    parser.add_argument("--min-claim-words", type=int, default=0)
    parser.add_argument("--min-related-candidates", type=int, default=0)
    parser.add_argument("--max-related-candidates", type=int, default=24)
    parser.add_argument("--require-natural-groups", action="store_true")
    parser.add_argument("--min-natural-groups", type=int, default=0)
    parser.add_argument("--reject-weak-claims", action="store_true")
    parser.add_argument("--normalized-source", help="normalized source markdown for optional claim grounding checks")
    parser.add_argument(
        "--max-unsupported-claim-tokens",
        type=int,
        default=0,
        help="fail claims with more than this many non-stopword tokens absent from --normalized-source; 0 disables",
    )
    parser.add_argument("--allow-metadata-claims", action="store_true")
    args = parser.parse_args()

    path = Path("wiki/sources") / f"{args.slug}.md"
    failures: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        print(f"FAIL: missing {path}")
        return 1

    text = path.read_text()
    fm = parse_frontmatter(path)
    failures.extend(f"{path}: {error}" for error in fm.errors)

    for key in REQUIRED_SOURCE_KEYS:
        if key not in fm.data:
            failures.append(f"{path}: missing frontmatter key {key!r}")

    if fm.data.get("type") != "source":
        failures.append(f"{path}: type must be source")
    if fm.data.get("source_id") != args.slug:
        failures.append(f"{path}: source_id must be {args.slug!r}")

    source_type = fm.data.get("source_type")
    if source_type not in {"pdf", "markdown", "web", "other"}:
        failures.append(f"{path}: invalid source_type {source_type!r}")

    expected_raw_path = f"../../raw/imported/{args.slug}/"
    expected_normalized_path = f"../../raw/normalized/{args.slug}/"
    if fm.data.get("raw_path") != expected_raw_path:
        failures.append(f"{path}: raw_path must be {expected_raw_path}")
    if fm.data.get("normalized_path") != expected_normalized_path:
        failures.append(f"{path}: normalized_path must be {expected_normalized_path}")

    sources = fm.data.get("sources")
    if not isinstance(sources, list):
        failures.append(f"{path}: sources must be a YAML list")
        sources = []
    if source_type == "pdf":
        expected_pdf = f"../../raw/imported/{args.slug}/original.pdf"
        if expected_pdf not in sources:
            failures.append(f"{path}: pdf source must include {expected_pdf}")

    if not re.search(r"^# .+", fm.body, re.MULTILINE):
        failures.append(f"{path}: missing H1 title")

    headings = h2_headings(fm.body)
    if headings != SOURCE_HEADINGS:
        failures.append(f"{path}: source headings must exactly match required order")

    key_claims = section(fm.body, "## Key claims")
    claims = [
        line
        for line in key_claims.splitlines()
        if re.match(r"^\s*(?:[-*]\s+|\d+[.]\s+)", line)
    ]
    claim_count = len(claims)
    if claim_count < args.min_claims:
        failures.append(f"{path}: only {claim_count} key claims; expected at least {args.min_claims}")
    if args.max_claims is not None and claim_count > args.max_claims:
        failures.append(f"{path}: {claim_count} key claims; expected at most {args.max_claims}")

    if not args.allow_metadata_claims:
        for i, claim in enumerate(claims, start=1):
            if any(re.search(pattern, claim, flags=re.IGNORECASE) for pattern in METADATA_CLAIM_PATTERNS):
                failures.append(f"{path}: key claim {i} appears to be document metadata, not reusable content")

    if args.min_claim_words:
        for i, claim in enumerate(claims, start=1):
            word_count = len(re.findall(r"[A-Za-z0-9']+", _strip_list_marker(claim)))
            if word_count < args.min_claim_words:
                failures.append(
                    f"{path}: key claim {i} has {word_count} words; expected at least {args.min_claim_words}"
                )

    if args.reject_weak_claims:
        for i, claim in enumerate(claims, start=1):
            if any(re.search(pattern, claim, flags=re.IGNORECASE) for pattern in WEAK_CLAIM_PATTERNS):
                failures.append(f"{path}: key claim {i} uses weak generic claim language")

    major_concepts = section(fm.body, "## Major concepts")
    natural_groups, group_failures = validate_natural_group_rows(path, major_concepts)
    failures.extend(group_failures)
    if args.require_natural_groups and len(natural_groups) < args.min_natural_groups:
        failures.append(
            f"{path}: only {len(natural_groups)} natural groups; expected at least {args.min_natural_groups}"
        )

    if args.normalized_source and args.max_unsupported_claim_tokens:
        source_path = Path(args.normalized_source)
        if not source_path.exists():
            failures.append(f"{path}: normalized source does not exist: {source_path}")
        else:
            source_tokens = set(content_tokens(source_path.read_text()))
            for i, claim in enumerate(claims, start=1):
                unsupported = sorted(set(content_tokens(_strip_list_marker(claim))) - source_tokens)
                if len(unsupported) > args.max_unsupported_claim_tokens:
                    sample = ", ".join(unsupported[:8])
                    failures.append(
                        f"{path}: key claim {i} has {len(unsupported)} tokens not found in normalized source: {sample}"
                    )

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            failures.append(f"{path}: forbidden pattern matched: {pattern}")

    related = section(fm.body, "## Related pages")
    failures.extend(validate_related_rows(path, related, natural_groups if natural_groups else None))
    related_markdown_links = [
        link for link in markdown_links(path) if link.line > _line_number_of_heading(text, "## Related pages")
    ]
    for link in related_markdown_links:
        if link.resolved and not link.resolved.exists():
            failures.append(f"{path}:{link.line}: broken Related pages Markdown link {link.target!r}")

    related_code_paths = code_paths(related)
    related_count = len(related_code_paths) + len(related_markdown_links)
    if args.min_related_candidates and related_count < args.min_related_candidates:
        failures.append(
            f"{path}: Related pages has {related_count} related entries; "
            f"expected at least {args.min_related_candidates}"
        )
    if related_code_paths and len(related_code_paths) > args.max_related_candidates:
        failures.append(
            f"{path}: Related pages has {len(related_code_paths)} candidate paths; "
            f"expected at most {args.max_related_candidates}"
        )

    if not related_markdown_links and not related_code_paths:
        warnings.append(f"{path}: Related pages has neither Markdown links nor candidate code paths")

    for link in markdown_links(path):
        if link.resolved and not link.resolved.exists():
            failures.append(f"{path}:{link.line}: broken Markdown link {link.target!r}")

    for warning in warnings:
        print(f"WARN: {warning}")
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        return 1

    print(f"PASS: {path} ({claim_count} key claims)")
    return 0


def _line_number_of_heading(text: str, heading: str) -> int:
    for i, line in enumerate(text.splitlines(), start=1):
        if line.strip() == heading:
            return i
    return 0


def _strip_list_marker(line: str) -> str:
    return re.sub(r"^\s*(?:[-*]\s+|\d+[.]\s+)", "", line).strip()


def validate_natural_group_rows(path: Path, major_concepts: str) -> tuple[set[str], list[str]]:
    failures: list[str] = []
    groups: set[str] = set()
    header_seen = False
    for row_number, line in enumerate(major_concepts.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = split_table_row(stripped)
        if cells is None:
            continue
        normalized = [cell.strip().lower() for cell in cells]
        if normalized == ["group", "scope", "evidence basis", "candidate page types"]:
            header_seen = True
            continue
        if not header_seen or is_separator_row(cells):
            continue
        if len(cells) != 4:
            failures.append(f"{path}: natural group row {row_number} must have four cells")
            continue
        group, scope, evidence_basis, page_types = (cell.strip() for cell in cells)
        if not group:
            failures.append(f"{path}: natural group row {row_number} has an empty group")
            continue
        if len(re.findall(r"[A-Za-z0-9']+", scope)) < 3:
            failures.append(f"{path}: natural group row {row_number} scope is too thin")
        if len(re.findall(r"[A-Za-z0-9']+", evidence_basis)) < 3:
            failures.append(f"{path}: natural group row {row_number} evidence basis is too thin")
        page_type_values = {value.strip().lower() for value in page_types.split(",") if value.strip()}
        invalid_page_types = sorted(page_type_values - {"concept", "entity", "procedure", "reference"})
        if invalid_page_types:
            failures.append(
                f"{path}: natural group row {row_number} has invalid candidate page types: {', '.join(invalid_page_types)}"
            )
        groups.add(normalize_group_name(group))
    return groups, failures


def validate_related_rows(path: Path, related: str, natural_groups: set[str] | None = None) -> list[str]:
    failures: list[str] = []
    for row_number, line in enumerate(related.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = split_table_row(stripped)
        if cells is None:
            failures.append(f"{path}: Related pages row {row_number} is not a valid Markdown table row")
            continue
        if is_separator_row(cells) or cells[0].lower() in {"candidate page", "page"}:
            continue
        if cells[0].strip().lower() == "page title":
            failures.append(f"{path}: Related pages row {row_number} uses placeholder title 'Page title'")
        if len(cells) not in {3, 5, 6}:
            failures.append(f"{path}: Related pages row {row_number} must have three, five, or six cells")
            continue
        group = None
        priority_cell = None
        evidence_basis = None
        if len(cells) == 5:
            priority_cell = cells[2].strip().lower()
            evidence_basis = cells[3].strip()
        elif len(cells) == 6:
            group = cells[2].strip()
            priority_cell = cells[3].strip().lower()
            evidence_basis = cells[4].strip()
            if not group:
                failures.append(f"{path}: Related pages row {row_number} group must not be empty")
            elif natural_groups is not None and normalize_group_name(group) not in natural_groups:
                failures.append(
                    f"{path}: Related pages row {row_number} group {group!r} is not listed in Major concepts natural groups"
                )

        if priority_cell is not None:
            if priority_cell not in RELATED_PRIORITIES:
                failures.append(
                    f"{path}: Related pages row {row_number} priority must be one of {sorted(RELATED_PRIORITIES)}"
                )
            if evidence_basis is not None and len(re.findall(r"[A-Za-z0-9']+", evidence_basis)) < 3:
                failures.append(f"{path}: Related pages row {row_number} evidence basis is too thin")
        status = cells[-1].strip().lower()
        if status not in RELATED_STATUSES:
            failures.append(f"{path}: Related pages row {row_number} status must be created or not created yet")
        path_cell = cells[1].strip()
        if status == "not created yet" and not re.fullmatch(r"`[^`]+\.md`", path_cell):
            failures.append(f"{path}: Related pages row {row_number} uncreated path must be code-formatted")
        if status == "created" and not re.fullmatch(r"\[[^\]]+\]\([^)]+\.md\)", path_cell):
            failures.append(f"{path}: Related pages row {row_number} created path must be a Markdown link")
    return failures


def normalize_group_name(group: str) -> str:
    return " ".join(group.strip().lower().split())


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)




if __name__ == "__main__":
    sys.exit(main())
