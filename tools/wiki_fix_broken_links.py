#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from wiki_common import parse_frontmatter


LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+\.md)\)")
SYNTH_DIRS = ("wiki/concepts", "wiki/entities", "wiki/procedures", "wiki/references")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert broken Markdown links in synthesized pages for one source into plain text."
    )
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("--check", action="store_true", help="do not write; fail if cleanup would change files")
    args = parser.parse_args()

    source_path = Path("wiki/sources") / f"{args.slug}.md"
    if not source_path.exists():
        print(f"FAIL: missing {source_path}")
        return 1

    changed: list[Path] = []
    for page in sourced_synthesized_pages(source_path):
        original = page.read_text()
        updated = fix_page_links(page, original)
        if updated == original:
            continue
        changed.append(page)
        if not args.check:
            page.write_text(updated)

    if changed and args.check:
        for page in changed:
            print(f"FAIL: {page} has broken Markdown links that can be made plain text")
        return 1
    if changed:
        for page in changed:
            print(f"updated {page}")
    else:
        print(f"no broken synthesized-page links found for {args.slug}")
    return 0


def sourced_synthesized_pages(source_path: Path) -> list[Path]:
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
                if isinstance(source, str) and (page.parent / source).resolve() == source_path.resolve():
                    pages.append(page)
                    break
    return pages


def fix_page_links(page: Path, text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        label = match.group(1).strip()
        target = match.group(2).strip()
        clean = target.split("#", 1)[0]
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", clean):
            return match.group(0)
        if (page.parent / clean).resolve().exists():
            return match.group(0)
        return f"{label} (not created yet)"

    return LINK_RE.sub(replace, text)


if __name__ == "__main__":
    sys.exit(main())
