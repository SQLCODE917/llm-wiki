"""Link graph over page bodies and deterministic lint checks.

These are the code-owned half of the lint operation (SCHEMA.md, "lint"):
broken links, orphan pages, and index drift are facts about the files, so
they are computed here rather than asked of the model.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from pathlib import Path

from llmwiki.domain.objects import LintFinding, LintRun
from llmwiki.domain.pages import PageError, parse_page, slugify

_LINK_RE = re.compile(r"\[\[([a-z0-9-]+)(?:\|[^\]]+)?\]\]")


def extract_links(text: str) -> set[str]:
    return set(_LINK_RE.findall(text))


def compute_findings(
    pages: Mapping[str, str],
    index_page_ids: set[str],
    exempt_from_orphans: frozenset[str] = frozenset(),
) -> LintRun:
    """Pure lint pass over page texts and the set of page_ids listed in index.md.

    *exempt_from_orphans* names page_ids that are orphans by construction
    (e.g. the harness-maintained health report) and shouldn't be reported.
    """
    page_ids = set(pages)
    outbound = {
        page_id: set() if page_id in exempt_from_orphans else extract_links(text)
        for page_id, text in pages.items()
    }

    broken = {
        page_id: tuple(sorted(targets - page_ids))
        for page_id, targets in outbound.items()
        if targets - page_ids
    }
    linked_to = set().union(*outbound.values()) if outbound else set()
    source_hubs = _source_hub_page_ids(pages)
    orphan_candidates = page_ids - linked_to - exempt_from_orphans - source_hubs
    orphans = tuple(sorted(orphan_candidates)) if len(page_ids) > 1 else ()
    lint_findings: list[LintFinding] = []
    for page_id, links in sorted(broken.items()):
        lint_findings.extend(
            LintFinding("broken link", page_id=page_id, cross_reference=link) for link in links
        )
    lint_findings.extend(LintFinding("orphan page", page_id=page_id) for page_id in orphans)
    lint_findings.extend(
        LintFinding("missing from index", page_id=page_id)
        for page_id in sorted(page_ids - index_page_ids)
    )
    lint_findings.extend(
        LintFinding("stale index entry", page_id=page_id)
        for page_id in sorted(index_page_ids - page_ids)
    )
    return LintRun(lint_findings=tuple(lint_findings), page_ids=tuple(sorted(page_ids)))


def _source_hub_page_ids(pages: Mapping[str, str]) -> frozenset[str]:
    hubs: set[str] = set()
    for page_id, text in pages.items():
        try:
            page = parse_page(text)
        except PageError:
            continue
        if page.page_kind != "source":
            continue
        source_locators = page.sources
        if page.page_metadata.source_id:
            source_locators = (*source_locators, page.page_metadata.source_id)
        if any(_source_locator_stem(locator) == page_id for locator in source_locators):
            hubs.add(page_id)
    return frozenset(hubs)


def _source_locator_stem(locator: str) -> str:
    raw_locator = locator.strip().removeprefix("raw/").split(" p.", maxsplit=1)[0].strip()
    return slugify(Path(raw_locator).stem)
