"""Inbound navigation closure for generated compiler pages."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.links import extract_links


@dataclass(frozen=True)
class ProjectionNavigationFinding:
    finding_type: str
    page_id: str
    message: str


def generated_page_navigation_findings(
    *,
    source_page_id: str,
    page_bodies: dict[str, str],
    page_families: dict[str, str],
) -> tuple[ProjectionNavigationFinding, ...]:
    page_ids = set(page_bodies)
    inbound: dict[str, set[str]] = {page_id: set() for page_id in page_ids}
    for source_id, body in page_bodies.items():
        for target_id in extract_links(body) & page_ids:
            if target_id != source_id:
                inbound[target_id].add(source_id)
    findings: list[ProjectionNavigationFinding] = []
    for page_id in sorted(page_ids):
        if _is_navigation_exempt(page_id, source_page_id, page_families.get(page_id, "")):
            continue
        if inbound[page_id]:
            continue
        findings.append(
            ProjectionNavigationFinding(
                "generated-page-has-no-inbound-route",
                page_id,
                "generated source-scoped page has no inbound route from this staged projection",
            )
        )
    return tuple(findings)


def _is_navigation_exempt(page_id: str, source_page_id: str, page_family: str) -> bool:
    return page_id == source_page_id or page_family == "source-manifest"
