#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from wiki_common import first_h1, markdown_links, parse_frontmatter, section
from wiki_evidence_ranges import locator_within_ranges, parse_locator_range, source_ranges_for_page


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
    failures.extend(check_analysis_locators(page, fm.body, resolved_sources))
    if "not covered in sources" not in fm.body.lower() and len(fm.body.split()) < 80:
        failures.append(f"{page}: analysis body is too thin")
    return failures


def check_analysis_locators(page: Path, body: str, resolved_sources: list[Path]) -> list[str]:
    failures: list[str] = []
    source_contexts = source_contexts_for_analysis(resolved_sources)
    locator_matches = list(re.finditer(r"(?:(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*):)?normalized:L\d+(?:-L?\d+)?", body))

    for link in markdown_links(page):
        if re.search(r"#L\d+\b", link.target):
            failures.append(
                f"{page}:{link.line}: use normalized locator text instead of wiki line anchor in link {link.target!r}"
            )

    if not locator_matches:
        return failures
    if not source_contexts:
        failures.append(f"{page}: uses normalized locators but has no resolvable source-page context")
        return failures

    for match in locator_matches:
        raw_locator = match.group(0)
        parsed = parse_locator_range(raw_locator)
        if parsed is None:
            failures.append(f"{page}: locator {raw_locator!r} is not parseable")
            continue
        source_slug = match.group("slug")
        contexts = [context for context in source_contexts if source_slug in {None, context.slug}]
        if source_slug is None and len(source_contexts) > 1:
            failures.append(f"{page}: locator {raw_locator!r} is ambiguous; prefix with a source slug")
            continue
        if not contexts:
            failures.append(f"{page}: locator {raw_locator!r} does not match an analysis source page")
            continue
        for context in contexts:
            start, end = parsed
            if end > len(context.lines):
                failures.append(
                    f"{page}: locator {raw_locator!r} is outside normalized source for {context.source_page.as_posix()}"
                )
                continue
            line_text = line_containing_offset(body, match.start())
            failures.extend(check_locator_against_linked_ranges(page, raw_locator, start, end, line_text, context))
    return failures


class SourceContext:
    def __init__(self, *, slug: str, source_page: Path, normalized_source: Path, lines: list[str]) -> None:
        self.slug = slug
        self.source_page = source_page
        self.normalized_source = normalized_source
        self.lines = lines


def source_contexts_for_analysis(resolved_sources: list[Path]) -> list[SourceContext]:
    contexts: list[SourceContext] = []
    for source in resolved_sources:
        fm = parse_frontmatter(source)
        if fm.data.get("type") != "source":
            continue
        slug = str(fm.data.get("source_id") or source.stem)
        normalized = normalized_markdown_from_source_page(source)
        if normalized is None:
            continue
        contexts.append(
            SourceContext(
                slug=slug,
                source_page=source,
                normalized_source=normalized,
                lines=normalized.read_text(errors="ignore").splitlines(),
            )
        )
    return contexts


def normalized_markdown_from_source_page(source_page: Path) -> Path | None:
    fm = parse_frontmatter(source_page)
    normalized_path = fm.data.get("normalized_path")
    if not isinstance(normalized_path, str):
        return None
    root = (source_page.parent / normalized_path).resolve()
    if root.is_file():
        return root
    if root.is_dir():
        matches = sorted(path for path in root.rglob("*.md") if path.is_file())
        if len(matches) == 1:
            return matches[0]
    return None


def line_containing_offset(text: str, offset: int) -> str:
    start = text.rfind("\n", 0, offset) + 1
    end = text.find("\n", offset)
    if end == -1:
        end = len(text)
    return text[start:end]


def check_locator_against_linked_ranges(
    page: Path,
    raw_locator: str,
    start: int,
    end: int,
    line_text: str,
    context: SourceContext,
) -> list[str]:
    failures: list[str] = []
    linked_range_pages = []
    cwd = Path.cwd().resolve()
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)", line_text):
        linked = (page.parent / match.group(1)).resolve()
        if not linked.exists():
            continue
        try:
            rel = linked.relative_to(cwd)
        except ValueError:
            continue
        if len(rel.parts) >= 3 and rel.parts[0] == "wiki" and rel.parts[1] in {"concepts", "entities", "procedures", "references"}:
            linked_range_pages.append(rel)
    for linked in linked_range_pages:
        fm = parse_frontmatter(linked)
        range_result = source_ranges_for_page(
            page=linked,
            frontmatter=fm.data,
            source_slug=context.slug,
            source_lines=context.lines,
            related_title=str(fm.data.get("title") or linked.stem),
        )
        ranges = range_result.ranges
        if ranges and locator_within_ranges(start, end, ranges):
            return []
    if linked_range_pages:
        failures.append(
            f"{page}: locator {raw_locator!r} appears beside linked wiki pages but is outside their declared or derived source ranges"
        )
    return failures


def is_repo_relative(path: Path) -> bool:
    try:
        path.relative_to(Path.cwd().resolve())
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    sys.exit(main())
