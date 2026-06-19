"""Graph repair tools exposed to lint workflows."""

from __future__ import annotations

from dataclasses import replace

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.links import compute_findings
from llmwiki.domain.pages import WikiPage, parse_page
from llmwiki.domain.system_pages import ORPHAN_EXEMPT_PAGES
from llmwiki.store import WikiStore, WikiStoreError


class LinkOrphanParams(BaseModel):
    from_page: str = Field(
        description="Existing page that should link to the orphan, e.g. "
        "'javascriptallonge-closures-and-scope'."
    )
    orphan_page: str = Field(description="Existing orphan page to link to, e.g. 'closure'.")


def link_orphan_tool(store: WikiStore, today: str) -> ToolDef:
    """Deterministically add one inbound wiki link to repair an orphan page."""

    def _link_orphan(**kwargs: object) -> str:
        params = LinkOrphanParams(**kwargs)  # type: ignore[arg-type]
        if params.from_page == params.orphan_page:
            raise WikiStoreError("from_page and orphan_page must be different pages.")
        source = parse_page(store.read_page(params.from_page))
        store.read_page(params.orphan_page)  # verifies the target exists before writing.
        link = f"[[{params.orphan_page}]]"
        if link in source.page_body:
            return f"wiki/{params.from_page}.md already links to {link}; no change needed."
        findings = compute_findings(
            store.page_texts(),
            store.index_page_ids(),
            exempt_from_orphans=ORPHAN_EXEMPT_PAGES,
        )
        if params.orphan_page not in findings.orphan_pages:
            raise WikiStoreError(
                f"Page '{params.orphan_page}' is not currently an orphan. "
                "Use link_orphan only for pages listed in the deterministic orphan findings."
            )
        body = source.page_body.rstrip() + f"\n\nRelated: {link}.\n"
        metadata = replace(source.page_metadata, updated=today)
        store.write_page(WikiPage.from_metadata(metadata, body))
        return (
            f"Added {link} to wiki/{params.from_page}.md. "
            f"This creates an inbound link to {params.orphan_page}."
        )

    return ToolDef(
        spec=ToolSpec(
            name="link_orphan",
            description="Fix one orphan page by adding a deterministic inbound "
            "[[orphan-page]] link from a related existing page. Prefer this "
            "over rewriting either page when the finding is only orphan status.",
            parameters=LinkOrphanParams,
        ),
        callable=_link_orphan,
    )
