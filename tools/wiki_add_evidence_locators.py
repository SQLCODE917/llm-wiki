#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from wiki_check_synthesis import clean_evidence_excerpt, normalize_for_search
from wiki_common import parse_frontmatter


SYNTH_DIRS = ("wiki/concepts", "wiki/entities", "wiki/procedures", "wiki/references")


def main() -> int:
    parser = argparse.ArgumentParser(description="Add normalized-source line locators to evidence tables.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("--normalized-source", required=True, help="normalized markdown file used as evidence source")
    parser.add_argument(
        "--page",
        action="append",
        default=[],
        help="repo-relative synthesized page to update; defaults to all pages citing the source",
    )
    parser.add_argument("--refresh", action="store_true", help="recompute existing locator cells")
    parser.add_argument("--check", action="store_true", help="report pages that need changes without writing")
    args = parser.parse_args()

    source_page = Path("wiki/sources") / f"{args.slug}.md"
    normalized_source = Path(args.normalized_source)
    if not source_page.exists():
        print(f"FAIL: missing source page {source_page}", file=sys.stderr)
        return 2
    if not normalized_source.exists():
        print(f"FAIL: missing normalized source {normalized_source}", file=sys.stderr)
        return 2

    source_lines = normalized_source.read_text(errors="ignore").splitlines()
    pages = [Path(path) for path in args.page] if args.page else synthesized_pages_for_source(source_page)
    if not pages:
        print(f"no synthesized pages cite {source_page}")
        return 0

    changed_pages: list[Path] = []
    failures: list[str] = []
    for page in pages:
        if not page.exists():
            failures.append(f"{page}: missing page")
            continue
        try:
            new_text, changed = add_locators(page.read_text(), source_lines, refresh=args.refresh)
        except LocatorError as error:
            failures.append(f"{page}: {error}")
            continue
        if changed:
            changed_pages.append(page)
            if not args.check:
                page.write_text(new_text)

    for page in changed_pages:
        action = "would update" if args.check else "updated"
        print(f"{action}: {page}")
    for failure in failures:
        print(f"FAIL: {failure}", file=sys.stderr)
    return 1 if failures or (args.check and changed_pages) else 0


def synthesized_pages_for_source(source_page: Path) -> list[Path]:
    pages: list[Path] = []
    for directory in SYNTH_DIRS:
        root = Path(directory)
        if not root.exists():
            continue
        for page in sorted(root.glob("*.md")):
            fm = parse_frontmatter(page)
            sources = fm.data.get("sources")
            if not isinstance(sources, list):
                continue
            for source in sources:
                if isinstance(source, str) and (page.parent / source).resolve() == source_page.resolve():
                    pages.append(page)
                    break
    return pages


def add_locators(text: str, source_lines: list[str], *, refresh: bool = False) -> tuple[str, bool]:
    lines = text.splitlines()
    out: list[str] = []
    changed = False
    in_evidence_table = False

    for line in lines:
        cells = split_table_row(line)
        if cells is None:
            in_evidence_table = False
            out.append(line)
            continue

        normalized = [cell.strip().lower() for cell in cells]
        if normalized == ["claim", "evidence", "source"]:
            out.append("| Claim | Evidence | Locator | Source |")
            in_evidence_table = True
            changed = True
            continue
        if normalized == ["claim", "evidence", "locator", "source"]:
            out.append(line)
            in_evidence_table = True
            continue

        if not in_evidence_table:
            out.append(line)
            continue

        if is_separator_row(cells):
            if len(cells) == 3:
                out.append("|---|---|---|---|")
                changed = True
            else:
                out.append(line)
            continue

        if len(cells) == 3:
            claim, evidence, source = (cell.strip() for cell in cells)
            locator = find_locator(clean_evidence_excerpt(evidence), source_lines)
            out.append(f"| {claim} | {evidence} | `{locator}` | {source} |")
            changed = True
            continue

        if len(cells) == 4:
            claim, evidence, locator, source = (cell.strip() for cell in cells)
            if refresh or not locator:
                refreshed = f"`{find_locator(clean_evidence_excerpt(evidence), source_lines)}`"
                out.append(f"| {claim} | {evidence} | {refreshed} | {source} |")
                if refreshed != locator:
                    changed = True
                continue
            out.append(line)
            continue

        out.append(line)

    trailing_newline = "\n" if text.endswith("\n") else ""
    return "\n".join(out) + trailing_newline, changed


def find_locator(excerpt: str, source_lines: list[str]) -> str:
    excerpt_norm = normalize_for_search(excerpt)
    if not excerpt_norm:
        raise LocatorError("empty evidence excerpt")

    max_window = min(8, len(source_lines))
    for window_size in range(1, max_window + 1):
        for start_index in range(0, len(source_lines) - window_size + 1):
            end_index = start_index + window_size
            window_text = "\n".join(source_lines[start_index:end_index])
            if excerpt_norm in normalize_for_search(window_text):
                return format_locator(start_index + 1, end_index)
    raise LocatorError(f"could not locate evidence excerpt: {excerpt[:90]!r}")


def format_locator(start_line: int, end_line: int) -> str:
    if start_line == end_line:
        return f"normalized:L{start_line}"
    return f"normalized:L{start_line}-L{end_line}"


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


class LocatorError(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
