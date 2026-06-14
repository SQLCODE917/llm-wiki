"""index.md as data: parse and upsert entries. Format defined in SCHEMA.md.

Entry format: `- [[page-name]] — one-line summary`, grouped under one
`## <Category>` heading per page category. All transformations are pure
text-to-text so the file stays human-readable and diff-friendly.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

CATEGORY_HEADINGS = {
    "source": "## Sources",
    "entity": "## Entities",
    "concept": "## Concepts",
    "synthesis": "## Syntheses",
}

_ENTRY_RE = re.compile(r"^- \[\[(?P<name>[a-z0-9-]+)\]\] — (?P<summary>.*)$")


@dataclass(frozen=True)
class IndexEntry:
    name: str
    category: str
    summary: str


def _entry_line(name: str, summary: str) -> str:
    return f"- [[{name}]] — {summary}"


def parse_index(text: str) -> list[IndexEntry]:
    """Extract all entries with the category they appear under."""
    heading_to_category = {h: c for c, h in CATEGORY_HEADINGS.items()}
    entries: list[IndexEntry] = []
    category: str | None = None
    for line in text.splitlines():
        if line.strip() in heading_to_category:
            category = heading_to_category[line.strip()]
            continue
        match = _ENTRY_RE.match(line.strip())
        if match and category is not None:
            entries.append(
                IndexEntry(name=match["name"], category=category, summary=match["summary"])
            )
    return entries


def index_page_names(text: str) -> set[str]:
    return {entry.name for entry in parse_index(text)}


def upsert_index_entry(text: str, name: str, category: str, summary: str) -> str:
    """Insert or replace the entry for *name*, keeping its category block sorted.

    A page that changed category is removed from its old block first, so a
    page appears in exactly one place.
    """
    heading = CATEGORY_HEADINGS[category]
    lines = [
        line
        for line in text.splitlines()
        if not (_ENTRY_RE.match(line.strip()) and _ENTRY_RE.match(line.strip())["name"] == name)  # type: ignore[index]
    ]
    if heading not in [line.strip() for line in lines]:
        raise ValueError(f"index.md is missing the {heading!r} heading; restore it from SCHEMA.md")

    result: list[str] = []
    inserted = False
    in_block = False
    for line in lines:
        stripped = line.strip()
        if stripped == heading:
            in_block = True
            result.append(line)
            continue
        if in_block and not inserted:
            existing = _ENTRY_RE.match(stripped)
            block_ended = stripped.startswith("## ")
            if existing and existing["name"] > name:
                result.append(_entry_line(name, summary))
                inserted = True
            elif block_ended:
                # Insert before the next heading, after any trailing blanks.
                while result and result[-1].strip() == "":
                    result.pop()
                result.extend([_entry_line(name, summary), ""])
                inserted = True
                in_block = False
        result.append(line)
    if not inserted:
        while result and result[-1].strip() == "":
            result.pop()
        result.append(_entry_line(name, summary))
    return "\n".join(result) + "\n"
