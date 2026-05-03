#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from wiki_common import first_h1, markdown_links, parse_frontmatter, section


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate filed analysis pages.")
    parser.add_argument("page", nargs="*", help="analysis page(s); defaults to all wiki/analyses/*.md")
    args = parser.parse_args()

    pages = [Path(path) for path in args.page] if args.page else sorted(Path("wiki/analyses").glob("*.md"))
    failures: list[str] = []
    if not pages:
        print("PASS: no analysis pages")
        return 0
    for page in pages:
        failures.extend(check_analysis(page))
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        return 1
    print(f"PASS: {len(pages)} analysis page(s)")
    return 0


def check_analysis(page: Path) -> list[str]:
    failures: list[str] = []
    if not page.exists():
        return [f"missing analysis page {page}"]
    fm = parse_frontmatter(page)
    for error in fm.errors:
        failures.append(f"{page}: {error}")
    if fm.data.get("type") != "analysis":
        failures.append(f"{page}: type must be analysis")
    for key in ("title", "tags", "status", "last_updated", "sources"):
        if key not in fm.data:
            failures.append(f"{page}: missing frontmatter key {key!r}")
    if not first_h1(fm.body):
        failures.append(f"{page}: missing H1 title")

    sources = fm.data.get("sources")
    if not isinstance(sources, list) or not sources:
        failures.append(f"{page}: frontmatter sources must be a non-empty list")
        sources = []
    resolved_sources = []
    for source in sources:
        if not isinstance(source, str):
            failures.append(f"{page}: source value must be a string")
            continue
        resolved = (page.parent / source).resolve()
        if not resolved.exists():
            failures.append(f"{page}: source {source!r} does not exist")
        else:
            try:
                resolved_sources.append(resolved.relative_to(Path.cwd().resolve()))
            except ValueError:
                failures.append(f"{page}: source {source!r} is outside the repo")

    source_pages = section(fm.body, "## Source pages")
    if not source_pages:
        failures.append(f"{page}: missing ## Source pages section")
    link_targets = {
        link.resolved.relative_to(Path.cwd().resolve())
        for link in markdown_links(page)
        if link.resolved and link.resolved.exists() and is_repo_relative(link.resolved)
    }
    for source in resolved_sources:
        if source not in link_targets:
            failures.append(f"{page}: body must link to source page {source.as_posix()}")
    if "not covered in sources" not in fm.body.lower() and len(fm.body.split()) < 80:
        failures.append(f"{page}: analysis body is too thin")
    return failures


def is_repo_relative(path: Path) -> bool:
    try:
        path.relative_to(Path.cwd().resolve())
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    sys.exit(main())
