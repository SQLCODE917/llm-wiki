#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from wiki_common import parse_frontmatter


SYNTH_DIRS = ("wiki/concepts", "wiki/entities", "wiki/procedures", "wiki/references")


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize obvious malformed Markdown table rows for one source.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("--check", action="store_true", help="do not write; fail if updates would be made")
    args = parser.parse_args()

    source_page = Path("wiki/sources") / f"{args.slug}.md"
    if not source_page.exists():
        print(f"FAIL: missing {source_page}", file=sys.stderr)
        return 1

    pages = [source_page, *synthesized_pages_for_source(source_page)]
    changed: list[Path] = []
    for page in pages:
        original = page.read_text()
        updated = normalize_tables(original)
        if updated == original:
            continue
        changed.append(page)
        if not args.check:
            page.write_text(updated)

    for page in changed:
        action = "would update" if args.check else "updated"
        print(f"{action}: {page}")
    if changed and args.check:
        return 1
    if not changed:
        print(f"no table normalization needed for {args.slug}")
    return 0


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


def normalize_tables(text: str) -> str:
    out: list[str] = []
    in_table = False
    for line in text.splitlines():
        stripped = line.strip()
        candidate = stripped
        if in_table and candidate.startswith(("+", "-")) and "|" in candidate and not candidate.startswith("|"):
            candidate = candidate[1:].strip()
        if in_table and "|" in candidate and not candidate.startswith("|"):
            candidate = f"| {candidate.strip()}"
            if not candidate.endswith("|"):
                candidate += " |"
        if candidate.startswith("|") and "|" in candidate[1:] and not candidate.endswith("|"):
            candidate = candidate.rstrip() + " |"

        if candidate.startswith("|") and "|" in candidate[1:]:
            out.append(candidate)
            in_table = True
            continue

        out.append(line)
        if not stripped or stripped.startswith("#") or "|" not in stripped:
            in_table = False

    trailing_newline = "\n" if text.endswith("\n") else ""
    return "\n".join(out) + trailing_newline


if __name__ == "__main__":
    sys.exit(main())
