#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import first_h1, markdown_links, one_line, parse_frontmatter, section


SYNTH_DIRS = {"concepts", "entities", "procedures", "references"}
WEAK_CLAIM_PATTERNS = [
    r"\bimportant\b",
    r"\bcrucial\b",
    r"\bfundamental\b",
    r"\bessential\b",
    r"\bsuccess\b",
]


@dataclass(frozen=True)
class EvidenceRow:
    claim: str
    evidence: str
    source: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a curator review packet for a Phase 2 worktree.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("worktree", help="Phase 2 benchmark worktree to review")
    parser.add_argument("--min-pages", type=int, default=5)
    parser.add_argument("--max-pages", type=int, default=15)
    parser.add_argument("--normalized-source", help="normalized source markdown for evidence excerpt checks")
    parser.add_argument("--output", help="write packet to this path instead of stdout")
    args = parser.parse_args()

    worktree = Path(args.worktree).resolve()
    if not worktree.exists():
        print(f"FAIL: missing worktree {worktree}", file=sys.stderr)
        return 1

    packet, status = render_review_packet(
        slug=args.slug,
        worktree=worktree,
        min_pages=args.min_pages,
        max_pages=args.max_pages,
        normalized_source=args.normalized_source,
    )

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(packet)
        print(f"wrote {output}")
    else:
        print(packet)
    return status


def render_review_packet(
    *,
    slug: str,
    worktree: Path,
    min_pages: int,
    max_pages: int,
    normalized_source: str | None,
) -> tuple[str, int]:
    source_page = worktree / "wiki/sources" / f"{slug}.md"
    if not source_page.exists():
        return f"# Curator Review Packet: {slug}\n\nFAIL: missing `{source_page}`\n", 1

    validation_output, validation_status = run_validation(worktree, slug, min_pages, max_pages, normalized_source)
    source_fm = parse_frontmatter(source_page)
    source_title = str(source_fm.data.get("title") or slug)
    linked_pages = linked_synthesized_pages(source_page)
    proposed_files = [Path("wiki/sources") / f"{slug}.md", *linked_pages]

    lines: list[str] = [
        f"# Curator Review Packet: {source_title}",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Source slug: `{slug}`",
        f"Worktree: `{worktree}`",
        "",
        "## Decision",
        "",
        "Choose one:",
        "",
        f"- Adopt: `pnpm wiki:adopt-phase2 {slug} {worktree} --min-pages {min_pages} --max-pages {max_pages}{normalized_arg(normalized_source)}`",
        f"- Adopt then finalize: `pnpm wiki:phase3 {slug}`",
        "- Revise: run another targeted Phase 2 repair or benchmark prompt.",
        "- Defer: keep source candidates uncreated for now.",
        "- Contradiction: append a `contradiction` entry to `wiki/log.md` and wait for human resolution.",
        "",
        "## Validation",
        "",
        f"Status: {'PASS' if validation_status == 0 else 'FAIL'}",
        "",
        "```text",
        validation_output.strip() or "No validation output.",
        "```",
        "",
        "## Proposed Files",
        "",
    ]

    for rel in proposed_files:
        marker = "new" if not (Path.cwd() / rel).exists() else "updates existing"
        lines.append(f"- `{rel.as_posix()}` — {marker}")
    lines.extend(["", "## Source Related Pages", ""])
    lines.extend(related_page_rows(source_page))
    lines.extend(["", "## Page Review", ""])

    all_rows: list[EvidenceRow] = []
    for rel in linked_pages:
        page = worktree / rel
        rows = evidence_rows(page)
        all_rows.extend(rows)
        lines.extend(render_page_section(rel, page, rows))

    lines.extend(render_review_checks(linked_pages, all_rows))
    lines.extend(["", "## Curator Checklist", ""])
    lines.extend(
        [
            "- Do the selected pages match the source's strongest reusable concepts?",
            "- Does every claim follow from its evidence, rather than merely sharing words with it?",
            "- Are any claims too broad and in need of qualification?",
            "- Does the source contradict an existing page or another source?",
            "- Should the adopted pages remain `draft`, or should any be marked `reviewed` after human reading?",
        ]
    )
    lines.append("")
    return "\n".join(lines), validation_status


def run_validation(
    worktree: Path,
    slug: str,
    min_pages: int,
    max_pages: int,
    normalized_source: str | None,
) -> tuple[str, int]:
    commands = [[
        "python3",
        "tools/wiki_check_synthesis.py",
        slug,
        "--min-pages",
        str(min_pages),
        "--max-pages",
        str(max_pages),
    ]]
    if normalized_source:
        commands[0].extend(["--normalized-source", normalized_source])
    commands.append(["pnpm", "wiki:grounding:check"])

    output: list[str] = []
    status = 0
    for command in commands:
        completed = subprocess.run(
            command,
            cwd=worktree,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        output.append("$ " + " ".join(command))
        output.append(completed.stdout)
        if completed.returncode != 0 and status == 0:
            status = completed.returncode
    return "\n".join(output), status


def linked_synthesized_pages(source_page: Path) -> list[Path]:
    heading_line = line_number_of_heading(source_page.read_text(), "## Related pages")
    pages: list[Path] = []
    for link in markdown_links(source_page):
        if link.line <= heading_line or not link.resolved or not link.resolved.exists():
            continue
        try:
            rel = link.resolved.relative_to(source_page.parents[2].resolve())
        except ValueError:
            continue
        if len(rel.parts) >= 3 and rel.parts[0] == "wiki" and rel.parts[1] in SYNTH_DIRS:
            pages.append(rel)
    return sorted(set(pages))


def related_page_rows(source_page: Path) -> list[str]:
    related = section(parse_frontmatter(source_page).body, "## Related pages")
    rows = [line for line in related.splitlines() if line.strip().startswith("|")]
    return rows or ["None."]


def render_page_section(rel: Path, page: Path, rows: list[EvidenceRow]) -> list[str]:
    fm = parse_frontmatter(page)
    title = str(fm.data.get("title") or rel.stem.replace("-", " ").title())
    page_type = str(fm.data.get("type") or "unknown")
    status = str(fm.data.get("status") or "unknown")
    body = fm.body
    summary = one_line(first_paragraph_after_h1(body) or section(body, "## Summary") or "No summary found.")
    issues = page_review_notes(page, rows)

    lines = [
        f"### {title}",
        "",
        f"- Path: `{rel.as_posix()}`",
        f"- Type: `{page_type}`",
        f"- Status: `{status}`",
        f"- Summary: {summary}",
        f"- Evidence rows: {len(rows)}",
        "",
    ]
    if issues:
        lines.append("Review notes:")
        lines.extend(f"- {issue}" for issue in issues)
        lines.append("")

    lines.extend(["Evidence:", "", "| Claim | Evidence | Source |", "|---|---|---|"])
    if rows:
        for row in rows:
            lines.append(f"| {escape_cell(row.claim)} | {escape_cell(row.evidence)} | {escape_cell(row.source)} |")
    else:
        lines.append("| MISSING | MISSING | MISSING |")
    lines.append("")
    return lines


def evidence_rows(page: Path) -> list[EvidenceRow]:
    fm = parse_frontmatter(page)
    details = section(fm.body, "## Source-backed details")
    rows: list[EvidenceRow] = []
    header_seen = False
    for line in details.splitlines():
        cells = split_table_row(line)
        if cells is None:
            continue
        normalized = [cell.strip().lower() for cell in cells]
        if normalized == ["claim", "evidence", "source"]:
            header_seen = True
            continue
        if not header_seen or is_separator_row(cells) or len(cells) != 3:
            continue
        rows.append(EvidenceRow(cells[0], cells[1], cells[2]))
    return rows


def render_review_checks(linked_pages: list[Path], rows: list[EvidenceRow]) -> list[str]:
    counts = Counter()
    for row in rows:
        if any(re.search(pattern, row.claim, flags=re.IGNORECASE) for pattern in WEAK_CLAIM_PATTERNS):
            counts["generic_claim_language"] += 1
        if len(word_tokens(strip_markdown(row.claim))) < 6:
            counts["short_claims"] += 1

    lines = ["## Review Signals", ""]
    lines.append(f"- Proposed synthesized pages: {len(linked_pages)}")
    lines.append(f"- Evidence rows: {len(rows)}")
    lines.append(f"- Short claims for human review: {counts['short_claims']}")
    lines.append(f"- Generic claim-language hits: {counts['generic_claim_language']}")
    lines.append("")
    return lines


def page_review_notes(page: Path, rows: list[EvidenceRow]) -> list[str]:
    notes: list[str] = []
    if not rows:
        notes.append("Missing evidence rows.")
    for index, row in enumerate(rows, start=1):
        if any(re.search(pattern, row.claim, flags=re.IGNORECASE) for pattern in WEAK_CLAIM_PATTERNS):
            notes.append(f"Evidence row {index} uses generic claim language.")
        if len(word_tokens(strip_markdown(row.claim))) < 6:
            notes.append(f"Evidence row {index} claim is short; check whether it is useful synthesis.")
    if page.exists() and (Path.cwd() / page.relative_to(page.parents[2])).exists():
        notes.append("This page already exists in the real repo; review the update as an integration, not only a new page.")
    return notes


def first_paragraph_after_h1(body: str) -> str:
    seen_h1 = False
    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            seen_h1 = True
            continue
        if not seen_h1:
            continue
        if not stripped:
            if lines:
                break
            continue
        if stripped.startswith("## "):
            break
        lines.append(stripped)
    return " ".join(lines)


def line_number_of_heading(text: str, heading: str) -> int:
    for i, line in enumerate(text.splitlines(), start=1):
        if line.strip() == heading:
            return i
    return 0


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


def escape_cell(text: str) -> str:
    return text.replace("|", "/").replace("\n", " ").strip()


def strip_markdown(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text).replace("`", "").replace("*", "")


def word_tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9']+", text)


def normalized_arg(normalized_source: str | None) -> str:
    return f" --normalized-source {normalized_source}" if normalized_source else ""


if __name__ == "__main__":
    sys.exit(main())
