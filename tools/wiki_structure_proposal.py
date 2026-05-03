#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import CONTENT_DIRS, iter_content_pages, parse_frontmatter, section


@dataclass(frozen=True)
class RelatedPage:
    source_slug: str
    title: str
    path: str
    status: str
    group: str
    priority: str
    evidence_basis: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Draft a directory-structure proposal from source-native groupings.")
    parser.add_argument("slug", nargs="*", help="source slug(s) to include; defaults to all source pages")
    parser.add_argument(
        "--min-sources-for-restructure",
        type=int,
        default=2,
        help="recommend waiting until this many non-trivial sources are present",
    )
    parser.add_argument("--append-log", action="store_true", help="append the proposal to wiki/log.md")
    args = parser.parse_args()

    source_pages = selected_source_pages(args.slug)
    if not source_pages:
        print("FAIL: no source pages found", file=sys.stderr)
        return 1

    proposal = render_proposal(source_pages, min_sources_for_restructure=args.min_sources_for_restructure)
    if args.append_log:
        log = Path("wiki/log.md")
        with log.open("a") as f:
            if log.exists() and log.stat().st_size:
                f.write("\n")
            f.write(proposal)
            f.write("\n")
        print(f"appended directory-structure proposal to {log}")
    else:
        print(proposal)
    return 0


def selected_source_pages(slugs: list[str]) -> list[Path]:
    if slugs:
        return [Path("wiki/sources") / f"{slug}.md" for slug in slugs if (Path("wiki/sources") / f"{slug}.md").exists()]
    return sorted(Path("wiki/sources").glob("*.md"))


def render_proposal(source_pages: list[Path], *, min_sources_for_restructure: int) -> str:
    related_pages = [related for source in source_pages for related in related_rows(source)]
    source_slugs = [path.stem for path in source_pages]
    created_count = sum(1 for related in related_pages if related.status == "created")
    candidate_count = sum(1 for related in related_pages if related.status == "not created yet")
    by_group: dict[str, list[RelatedPage]] = defaultdict(list)
    for related in related_pages:
        by_group[related.group].append(related)

    type_counts = Counter(page_type(path) for path in iter_content_pages() if path.parts[1] != "sources")
    recommendation = recommendation_text(source_pages, by_group, min_sources_for_restructure)

    lines: list[str] = [
        f"## [{date.today().isoformat()}] proposal | directory structure",
        "",
        f"- Sources reviewed: {', '.join(source_slugs)}",
        f"- Current physical structure: type-based directories under `wiki/`.",
        f"- Related pages observed: {len(related_pages)} total ({created_count} created, {candidate_count} candidates).",
        f"- Current synthesized page type counts: {format_counts(type_counts)}",
        f"- Recommendation: {recommendation}",
        "",
        "Natural groupings observed:",
    ]

    if by_group:
        for group, rows in sorted(by_group.items(), key=lambda item: (-len(item[1]), item[0])):
            sources = sorted({row.source_slug for row in rows})
            statuses = Counter(row.status for row in rows)
            priorities = Counter(row.priority for row in rows if row.priority != "unspecified")
            lines.append(
                f"- {group}: {len(rows)} pages from {', '.join(sources)} "
                f"({format_counts(statuses)}; priorities: {format_counts(priorities)})"
            )
            sample_titles = ", ".join(row.title for row in rows[:5])
            if sample_titles:
                lines.append(f"  Pages: {sample_titles}")
    else:
        lines.append("- None recorded yet.")

    lines.extend(
        [
            "",
            "Directory proposal:",
            "- Keep `wiki/sources/`, `wiki/concepts/`, `wiki/entities/`, `wiki/procedures/`, `wiki/references/`, and `wiki/analyses/` unless the curator approves a logged restructure.",
            "- Use source-native groups for page selection, index organization, tags, and future restructure evidence.",
            "- Reconsider physical directories after more ingests show stable, non-overlapping groups that cannot be represented cleanly by page type.",
            "",
            "Curator decision needed:",
            "- approve current type-based structure",
            "- defer until more ingests",
            "- request a concrete rename/move plan",
            "",
            "---",
        ]
    )
    return "\n".join(lines)


def recommendation_text(
    source_pages: list[Path],
    by_group: dict[str, list[RelatedPage]],
    min_sources_for_restructure: int,
) -> str:
    if len(source_pages) < min_sources_for_restructure:
        return (
            "defer physical directory changes; one source can reveal natural groups, "
            "but it is weak evidence for a durable repo-wide directory structure"
        )
    if not by_group:
        return "keep type-based directories until source-native groups are recorded"
    repeated_groups = [group for group, rows in by_group.items() if len({row.source_slug for row in rows}) > 1]
    if repeated_groups:
        return "review repeated source-native groups before deciding whether a domain structure is warranted"
    return "keep type-based directories; observed groups have not repeated across sources yet"


def related_rows(source_page: Path) -> list[RelatedPage]:
    related = section(parse_frontmatter(source_page).body, "## Related pages")
    rows: list[RelatedPage] = []
    for line in related.splitlines():
        cells = split_table_row(line)
        if cells is None or is_separator_row(cells) or cells[0].strip().lower() in {"candidate page", "page"}:
            continue
        if len(cells) not in {3, 5, 6}:
            continue
        title = clean_markdown(cells[0])
        target = code_path(cells[1]) or markdown_target(cells[1]) or clean_markdown(cells[1])
        status = cells[-1].strip().lower()
        group = "unclassified"
        priority = "unspecified"
        evidence_basis = ""
        if len(cells) == 5:
            priority = cells[2].strip().lower()
            evidence_basis = cells[3].strip()
        elif len(cells) == 6:
            group = clean_markdown(cells[2]) or "unclassified"
            priority = cells[3].strip().lower()
            evidence_basis = cells[4].strip()
        rows.append(
            RelatedPage(
                source_slug=source_page.stem,
                title=title,
                path=target,
                status=status,
                group=group,
                priority=priority,
                evidence_basis=evidence_basis,
            )
        )
    return rows


def page_type(path: Path) -> str:
    fm = parse_frontmatter(path)
    value = fm.data.get("type")
    if isinstance(value, str) and value:
        return value
    if len(path.parts) > 1 and path.parts[1] in CONTENT_DIRS:
        return path.parts[1].rstrip("s")
    return "unknown"


def format_counts(counts: Counter[str]) -> str:
    if not counts:
        return "none"
    return ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


def code_path(cell: str) -> str | None:
    match = re.fullmatch(r"`([^`]+\.md)`", cell.strip())
    return match.group(1) if match else None


def markdown_target(cell: str) -> str | None:
    match = re.search(r"\[[^\]]+\]\(([^)]+\.md)\)", cell)
    return match.group(1) if match else None


def clean_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.replace("`", "").strip()


if __name__ == "__main__":
    sys.exit(main())
