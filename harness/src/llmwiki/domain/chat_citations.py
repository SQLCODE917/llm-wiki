"""Citation policy for grounded wiki chat answers."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.links import extract_links

_ANY_WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
_PAGE_ID_RE = re.compile(r"[a-z0-9-]+(?:\|[^\]]+)?")


@dataclass(frozen=True)
class ChatResponseCitationDecision:
    allowed: bool
    message: str = ""


@dataclass(frozen=True)
class ChatResponseCitationPolicy:
    """Citation contract for a chat answer grounded in read wiki pages."""

    read_page_ids: frozenset[str]

    def response_decision(self, message: str) -> ChatResponseCitationDecision:
        if not self.read_page_ids:
            return ChatResponseCitationDecision(allowed=True)
        malformed_links = _malformed_wikilinks(message)
        if malformed_links:
            examples = ", ".join(f"[[{link}]]" for link in sorted(malformed_links)[:3])
            return ChatResponseCitationDecision(
                allowed=False,
                message=(
                    "Use [[page-id]] links only for actual wiki page IDs read for "
                    "this answer. Do not wrap table titles or labels in wiki links; "
                    f"write them as plain text instead. Invalid link(s): {examples}."
                ),
            )
        page_links = extract_links(message)
        unread_links = page_links - self.read_page_ids
        if unread_links:
            examples = ", ".join(f"[[{link}]]" for link in sorted(unread_links)[:3])
            return ChatResponseCitationDecision(
                allowed=False,
                message=(
                    "Only cite wiki pages read for this answer. Remove unread "
                    f"wiki link(s) or cite a read page instead: {examples}."
                ),
            )
        cited_read_pages = page_links & self.read_page_ids
        if cited_read_pages:
            return ChatResponseCitationDecision(allowed=True)
        suggestions = ", ".join(f"[[{page_id}]]" for page_id in sorted(self.read_page_ids)[:3])
        return ChatResponseCitationDecision(
            allowed=False,
            message=(
                "Cite at least one wiki page read for this answer with a [[page-id]] "
                f"link, such as {suggestions}. Raw source citations alone are not "
                "enough because the chat answer must identify the wiki evidence page."
            ),
        )


def _malformed_wikilinks(message: str) -> frozenset[str]:
    return frozenset(
        link for link in _ANY_WIKILINK_RE.findall(message) if _PAGE_ID_RE.fullmatch(link) is None
    )
