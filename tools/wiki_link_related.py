#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from wiki_common import parse_frontmatter


CREATED = "created"
NOT_CREATED = "not created yet"


def main() -> int:
    parser = argparse.ArgumentParser(description="Replace source-page candidate rows with links for pages that exist.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("--check", action="store_true", help="do not write; fail if updates would be made")
    args = parser.parse_args()

    path = Path("wiki/sources") / f"{args.slug}.md"
    if not path.exists():
        print(f"FAIL: missing {path}")
        return 1

    original = path.read_text()
    updated = link_existing_candidates(path, original)
    if args.check:
        if updated != original:
            print(f"FAIL: {path} has existing related-page candidates that should be links")
            return 1
        print(f"PASS: {path} related-page candidates are current")
        return 0

    if updated != original:
        path.write_text(updated)
        print(f"updated {path}")
    else:
        print(f"no related-page updates needed for {path}")
    return 0


def link_existing_candidates(source_path: Path, text: str) -> str:
    lines = text.splitlines()
    in_related = False
    updated: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped == "## Related pages":
            in_related = True
            updated.append(line)
            continue
        if in_related and stripped.startswith("## "):
            in_related = False

        if in_related:
            normalized = normalize_related_row(source_path, line)
            if normalized is not None:
                updated.append(normalized)
                continue
        updated.append(line)

    return "\n".join(updated) + ("\n" if text.endswith("\n") else "")


def normalize_related_row(source_path: Path, line: str) -> str | None:
    cells = split_table_row(line)
    if cells is None or len(cells) not in {3, 5, 6}:
        return None
    title_cell = cells[0]
    path_cell = cells[1]
    status_cell = cells[-1]
    if title_cell.lower() in {"candidate page", "page"}:
        return None
    if set("".join(cells)) <= {"-", ":", " "}:
        return None

    target = code_path(path_cell) or markdown_target(path_cell)
    if not target:
        return None

    title = clean_cell_title(title_cell)
    target_path = (source_path.parent / target).resolve()
    extras = cells[2:-1]
    if page_belongs_to_source(target_path, source_path.stem):
        return format_related_row(title, f"[{target}]({target})", extras, CREATED)
    return format_related_row(title, f"`{target}`", extras, NOT_CREATED)


def page_belongs_to_source(page_path: Path, source_slug: str) -> bool:
    if not page_path.exists():
        return False
    try:
        sources = parse_frontmatter(page_path).data.get("sources")
    except Exception:
        return False
    if not isinstance(sources, list):
        return False
    return f"../sources/{source_slug}.md" in {str(source) for source in sources}


def format_related_row(title: str, path_cell: str, extras: list[str], status: str) -> str:
    cells = [title, path_cell, *extras, status]
    return "| " + " | ".join(cells) + " |"


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def code_path(cell: str) -> str | None:
    stripped = cell.strip()
    if stripped.startswith("`") and stripped.endswith("`") and stripped.count("`") == 2:
        value = stripped[1:-1].strip()
        if value.endswith(".md"):
            return value
    return None


def markdown_target(cell: str) -> str | None:
    targets = []
    for marker in "](":
        if marker not in cell:
            return None
    start = 0
    while True:
        marker = cell.find("](", start)
        if marker == -1:
            break
        close = cell.find(")", marker + 2)
        if close == -1:
            break
        target = cell[marker + 2 : close].strip()
        if target.endswith(".md"):
            targets.append(target)
        start = close + 1
    return targets[-1] if targets else None


def clean_cell_title(cell: str) -> str:
    text = cell.strip().replace("`", "")
    while "](" in text:
        marker = text.find("](")
        close = text.find(")", marker + 2)
        open_bracket = text.rfind("[", 0, marker)
        if open_bracket == -1 or close == -1:
            break
        label = text[open_bracket + 1 : marker]
        text = text[:open_bracket] + label + text[close + 1 :]
    return text.strip(" []") or "Untitled"


if __name__ == "__main__":
    sys.exit(main())
