#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from wiki_common import iter_content_pages, one_line, parse_frontmatter, section


SECTION_ORDER = [
    ("source", "Sources"),
    ("entity", "Entities"),
    ("concept", "Concepts"),
    ("procedure", "Procedures"),
    ("reference", "References"),
    ("analysis", "Analyses"),
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate wiki/index.md from wiki content pages.")
    parser.add_argument("--check", action="store_true", help="do not write; fail if index is stale")
    args = parser.parse_args()

    index_path = Path("wiki/index.md")
    rendered = render_index()

    if args.check:
        current = index_path.read_text() if index_path.exists() else ""
        if current != rendered:
            print("FAIL: wiki/index.md is stale; run pnpm wiki:index")
            return 1
        print("PASS: wiki/index.md is current")
        return 0

    index_path.write_text(rendered)
    print(f"wrote {index_path}")
    return 0


def render_index() -> str:
    entries_by_type: dict[str, list[tuple[str, str, str]]] = {page_type: [] for page_type, _ in SECTION_ORDER}

    for path in iter_content_pages():
        fm = parse_frontmatter(path)
        page_type = str(fm.data.get("type", ""))
        if page_type not in entries_by_type:
            continue
        title = str(fm.data.get("title") or _title_from_path(path))
        link = path.relative_to("wiki").as_posix()
        description = _description(path, fm.body)
        entries_by_type[page_type].append((title.lower(), f"- [{title}]({link}) — {description}", link))

    lines = ["# Index", ""]
    for page_type, heading in SECTION_ORDER:
        lines.extend([f"## {heading}", ""])
        entries = sorted(entries_by_type[page_type])
        if entries:
            lines.extend(entry for _, entry, _ in entries)
        else:
            lines.append("None.")
        lines.append("")

    lines.extend(["## Code", ""])
    code_entries = code_index_entries()
    if code_entries:
        lines.extend(code_entries)
    else:
        lines.append("None.")
    lines.append("")

    return "\n".join(lines)


def _description(path: Path, body: str) -> str:
    summary = section(body, "## Summary")
    if summary:
        return one_line(_strip_markdown_links(summary))

    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("|"):
            continue
        if stripped.startswith("- ") or stripped.startswith("```"):
            continue
        return one_line(_strip_markdown_links(stripped))
    return f"{path.stem.replace('-', ' ')} page."


def _strip_markdown_links(text: str) -> str:
    return text.replace("[", "").replace("]", "")


def _title_from_path(path: Path) -> str:
    return path.stem.replace("-", " ").title()


def code_index_entries() -> list[str]:
    roots = [
        (Path("packages/concepts/src"), "TypeScript implementation"),
        (Path("packages/concepts/tests"), "TypeScript test"),
    ]
    entries: list[tuple[str, str]] = []
    for root, description in roots:
        if not root.exists():
            continue
        for path in sorted(root.glob("*.ts")):
            link = "../" + path.as_posix()
            entries.append((path.as_posix(), f"- [{path.name}]({link}) — {description}."))
    return [entry for _, entry in sorted(entries)]


if __name__ == "__main__":
    sys.exit(main())
