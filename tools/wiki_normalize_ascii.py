#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from wiki_common import parse_frontmatter


SYNTH_DIRS = ("wiki/concepts", "wiki/entities",
              "wiki/procedures", "wiki/references")
# Only replace typography issues and mojibake (encoding errors).
# Preserve legitimate accented characters (é, ñ, etc.) that appear in sources.
REPLACEMENTS = {
    # Typography normalization
    "\u00a0": " ",   # non-breaking space
    "\u2010": "-",   # hyphen
    "\u2011": "-",   # non-breaking hyphen
    "\u2012": "-",   # figure dash
    "\u2013": "-",   # en dash
    "\u2014": "-",   # em dash
    "\u2015": "-",   # horizontal bar
    "\u2018": "'",   # left single quote
    "\u2019": "'",   # right single quote
    "\u201c": '"',   # left double quote
    "\u201d": '"',   # right double quote
    "\u2026": "...",  # ellipsis
    # Mojibake patterns (UTF-8 misinterpreted as Latin-1)
    "Ã©": "é",  # preserve accent
    "Ã¨": "è",
    "Ã ": "à",
    "Ã¢": "â",
    "Ã´": "ô",
    "Ã§": "ç",
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normalize common Unicode punctuation to ASCII in synthesized pages for one source."
    )
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("--check", action="store_true",
                        help="do not write; fail if normalization would change files")
    args = parser.parse_args()

    source_path = Path("wiki/sources") / f"{args.slug}.md"
    if not source_path.exists():
        print(f"FAIL: missing {source_path}")
        return 1

    changed: list[Path] = []
    for page in sourced_synthesized_pages(source_path):
        original = page.read_text()
        updated = normalize_ascii(original)
        if updated == original:
            continue
        changed.append(page)
        if not args.check:
            page.write_text(updated)

    if changed and args.check:
        for page in changed:
            print(
                f"FAIL: {page} has common Unicode punctuation that can be normalized")
        return 1
    if changed:
        for page in changed:
            print(f"updated {page}")
    else:
        print(f"no ASCII normalization needed for {args.slug}")
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


def normalize_ascii(text: str) -> str:
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    return text


if __name__ == "__main__":
    sys.exit(main())
