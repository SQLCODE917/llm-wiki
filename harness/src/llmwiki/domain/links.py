"""Link graph over page bodies and deterministic lint checks.

These are the code-owned half of the lint operation (SCHEMA.md, "lint"):
broken links, orphan pages, and index drift are facts about the files, so
they are computed here rather than asked of the model.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass, field

_LINK_RE = re.compile(r"\[\[([a-z0-9-]+)\]\]")


def extract_links(text: str) -> set[str]:
    return set(_LINK_RE.findall(text))


@dataclass(frozen=True)
class LintFindings:
    """Deterministic wiki-health facts, ready to hand to the model."""

    broken_links: dict[str, tuple[str, ...]] = field(default_factory=dict)
    orphan_pages: tuple[str, ...] = ()
    missing_from_index: tuple[str, ...] = ()
    stale_index_entries: tuple[str, ...] = ()

    @property
    def is_clean(self) -> bool:
        return not (
            self.broken_links
            or self.orphan_pages
            or self.missing_from_index
            or self.stale_index_entries
        )

    def render(self) -> str:
        if self.is_clean:
            return "No deterministic issues found (links, orphans, and index are consistent)."
        sections: list[str] = []
        if self.broken_links:
            lines = [
                f"- {page} links to missing page(s): {', '.join(targets)}"
                for page, targets in sorted(self.broken_links.items())
            ]
            sections.append("Broken [[links]] (target page does not exist):\n" + "\n".join(lines))
        if self.orphan_pages:
            sections.append(
                "Orphan pages (no inbound links from any other page):\n"
                + "\n".join(f"- {name}" for name in self.orphan_pages)
            )
        if self.missing_from_index:
            sections.append(
                "Pages missing from index.md:\n"
                + "\n".join(f"- {name}" for name in self.missing_from_index)
            )
        if self.stale_index_entries:
            sections.append(
                "index.md entries whose page does not exist:\n"
                + "\n".join(f"- {name}" for name in self.stale_index_entries)
            )
        return "\n\n".join(sections)


def compute_findings(
    pages: Mapping[str, str],
    index_names: set[str],
    exempt_from_orphans: frozenset[str] = frozenset(),
) -> LintFindings:
    """Pure lint pass over page texts and the set of names listed in index.md.

    *exempt_from_orphans* names pages that are orphans by construction
    (e.g. the harness-maintained health report) and shouldn't be reported.
    """
    page_names = set(pages)
    outbound = {name: extract_links(text) for name, text in pages.items()}

    broken = {
        name: tuple(sorted(targets - page_names))
        for name, targets in outbound.items()
        if targets - page_names
    }
    linked_to = set().union(*outbound.values()) if outbound else set()
    orphan_candidates = page_names - linked_to - exempt_from_orphans
    orphans = tuple(sorted(orphan_candidates)) if len(page_names) > 1 else ()
    return LintFindings(
        broken_links=broken,
        orphan_pages=orphans,
        missing_from_index=tuple(sorted(page_names - index_names)),
        stale_index_entries=tuple(sorted(index_names - page_names)),
    )
