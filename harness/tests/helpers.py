"""Test data builders for domain objects."""

from llmwiki.domain.pages import PageMetadata, WikiPage


def wiki_page(
    *,
    name: str,
    category: str,
    summary: str,
    body: str,
    sources: tuple[str, ...] = (),
    updated: str = "",
) -> WikiPage:
    """Build a WikiPage while tests still describe scenarios in user-facing terms."""
    return WikiPage(
        page_metadata=PageMetadata(
            page_id=name,
            page_kind=category,
            summary=summary,
            sources=sources,
            updated=updated,
        ),
        page_body=body,
    )
