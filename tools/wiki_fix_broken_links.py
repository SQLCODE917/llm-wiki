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
        updated = fix_page_links(page, original, source_path)
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


def fix_page_links(page: Path, text: str, source_path: Path | None = None) -> str:
    def replace(match: re.Match[str]) -> str:
        label = match.group(1).strip()
        target = match.group(2).strip()
        clean = target.split("#", 1)[0]
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", clean):
            return match.group(0)
        if (page.parent / clean).resolve().exists():
            return match.group(0)
        return f"{label} (not created yet)"

    updated = move_uncreated_related_pages(LINK_RE.sub(replace, text))
    if source_path is not None:
        updated = normalize_frontmatter_source_refs(page, updated, source_path)
    return updated


def normalize_frontmatter_source_refs(page: Path, text: str, source_path: Path) -> str:
    source_rel = (Path("../sources") / source_path.name).as_posix()
    slug = source_path.stem
    updated = re.sub(
        rf"(?m)^sources:\s*\[\s*['\"]?{re.escape(slug)}['\"]?\s*\]\s*$",
        f"sources:\n  - {source_rel}",
        text,
        count=1,
    )
    updated = re.sub(
        rf"(?m)^(\s*-\s*)['\"]?{re.escape(slug)}['\"]?\s*$",
        rf"\1{source_rel}",
        updated,
        count=1,
    )
    return updated


def move_uncreated_related_pages(text: str) -> str:
    lines = text.splitlines()
    related = section_bounds(lines, "## Related pages")
    if related is None:
        return text

    start, end = related
    body = lines[start + 1:end]
    uncreated: list[str] = []
    kept: list[str] = []
    for line in body:
        if "not created yet" in line.lower():
            uncreated.append(line)
        else:
            kept.append(line)

    if not uncreated:
        return text

    # Keep Related pages as a real-link section. Empty sections are invalid, so
    # use an explicit placeholder when every row/bullet was a future candidate.
    if not any(line.strip() for line in kept):
        kept = ["", "None."]

    updated = lines[:start + 1] + kept + lines[end:]
    candidate = section_bounds(updated, "## Candidate pages")
    if candidate is None:
        insert_at = len(updated)
        updated.extend(["", "## Candidate pages", ""])
        candidate = (len(updated) - 2, len(updated))
    cand_start, cand_end = candidate

    candidate_body = updated[cand_start + 1:cand_end]
    if candidate_body and candidate_body[-1].strip():
        candidate_body.append("")
    for line in uncreated:
        if line not in candidate_body:
            candidate_body.append(line)
    updated = updated[:cand_start + 1] + candidate_body + updated[cand_end:]
    return "\n".join(updated) + ("\n" if text.endswith("\n") else "")


def section_bounds(lines: list[str], heading: str) -> tuple[int, int] | None:
    start = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index
            break
    if start is None:
        return None
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return start, end


if __name__ == "__main__":
    sys.exit(main())
