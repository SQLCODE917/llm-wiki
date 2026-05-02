#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from wiki_common import (
    code_paths,
    h2_headings,
    markdown_links,
    parse_frontmatter,
    section,
)


SYNTH_TYPES = {"concept", "entity", "procedure", "reference"}
REQUIRED_KEYS = ["title", "type", "tags", "status", "last_updated", "sources"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Phase 2 synthesized pages for one source.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("--min-pages", type=int, default=3)
    parser.add_argument("--max-pages", type=int, default=15)
    args = parser.parse_args()

    failures = check_synthesis(args.slug, args.min_pages, args.max_pages)
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        return 1
    print(f"PASS: synthesis for {args.slug}")
    return 0


def check_synthesis(slug: str, min_pages: int, max_pages: int) -> list[str]:
    source_path = Path("wiki/sources") / f"{slug}.md"
    failures: list[str] = []
    if not source_path.exists():
        return [f"missing source page {source_path}"]

    created_pages = linked_synthesized_pages(source_path)
    if len(created_pages) < min_pages:
        failures.append(f"{source_path}: only {len(created_pages)} synthesized page links; expected at least {min_pages}")
    if len(created_pages) > max_pages:
        failures.append(f"{source_path}: {len(created_pages)} synthesized page links; expected at most {max_pages}")

    for page in created_pages:
        failures.extend(check_synthesized_page(page, source_path))

    related = section(parse_frontmatter(source_path).body, "## Related pages")
    for code_path in code_paths(related):
        candidate = (source_path.parent / code_path).resolve()
        if candidate.exists():
            failures.append(
                f"{source_path}: existing page {code_path!r} is still listed as a candidate instead of a Markdown link"
            )
    return failures


def linked_synthesized_pages(source_path: Path) -> list[Path]:
    heading_line = line_number_of_heading(source_path.read_text(), "## Related pages")
    pages: list[Path] = []
    for link in markdown_links(source_path):
        if link.line <= heading_line or not link.resolved or not link.resolved.exists():
            continue
        try:
            rel = link.resolved.relative_to(Path.cwd().resolve())
        except ValueError:
            continue
        if len(rel.parts) >= 3 and rel.parts[0] == "wiki" and rel.parts[1] in {"concepts", "entities", "procedures", "references"}:
            pages.append(rel)
    return sorted(set(pages))


def check_synthesized_page(page: Path, source_path: Path) -> list[str]:
    failures: list[str] = []
    fm = parse_frontmatter(page)
    for error in fm.errors:
        failures.append(f"{page}: {error}")
    for key in REQUIRED_KEYS:
        if key not in fm.data:
            failures.append(f"{page}: missing frontmatter key {key!r}")

    page_type = fm.data.get("type")
    if page_type not in SYNTH_TYPES:
        failures.append(f"{page}: type must be one of {sorted(SYNTH_TYPES)}")

    if not re.search(r"^# .+", fm.body, re.MULTILINE):
        failures.append(f"{page}: missing H1 title")

    source_rel = relative_link(page, source_path)
    sources = fm.data.get("sources")
    if not isinstance(sources, list) or source_rel not in sources:
        failures.append(f"{page}: frontmatter sources must include {source_rel}")

    body_links = [link.resolved for link in markdown_links(page) if link.resolved]
    if source_path.resolve() not in body_links:
        failures.append(f"{page}: body must link back to {source_rel}")

    body_headings = h2_headings(fm.body)
    if "## Source pages" not in body_headings and "## Sources" not in body_headings:
        failures.append(f"{page}: missing source page section")
    return failures


def relative_link(page: Path, target: Path) -> str:
    return Path("../" * (len(page.parent.relative_to("wiki").parts)) + target.relative_to("wiki").as_posix()).as_posix()


def line_number_of_heading(text: str, heading: str) -> int:
    for i, line in enumerate(text.splitlines(), start=1):
        if line.strip() == heading:
            return i
    return 0


if __name__ == "__main__":
    sys.exit(main())
