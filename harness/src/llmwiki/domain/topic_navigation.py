"""Dense hub navigation from persisted source topic indexes."""

from __future__ import annotations

import json
import re

_KEY_TOPICS_RE = re.compile(r"^\s*\**\s*key topics\b", re.IGNORECASE)


def topic_index_prompt_block(topic_index_json: str | None, existing_pages: frozenset[str]) -> str:
    links = _topic_links(topic_index_json, existing_pages)
    if not links:
        return ""
    rendered = ", ".join(f"[[{page_id}]] ({count})" for page_id, count in links[:16])
    return f"Source topic index: {rendered}"


def reconcile_topic_links(
    body: str,
    topic_index_json: str | None,
    existing_pages: frozenset[str],
    *,
    limit: int = 16,
) -> str:
    links = _topic_links(topic_index_json, existing_pages)[:limit]
    lines = [line for line in body.splitlines() if not _KEY_TOPICS_RE.match(line)]
    while lines and not lines[-1].strip():
        lines.pop()
    if links:
        rendered = ", ".join(f"[[{page_id}]]" for page_id, _count in links)
        lines.extend(["", f"**Key topics:** {rendered}"])
    return "\n".join(lines)


def _topic_links(
    topic_index_json: str | None, existing_pages: frozenset[str]
) -> tuple[tuple[str, int], ...]:
    if not topic_index_json:
        return ()
    try:
        payload = json.loads(topic_index_json)
    except json.JSONDecodeError:
        return ()
    links: list[tuple[str, int]] = []
    seen: set[str] = set()
    for topic in payload.get("topics", ()):
        if not isinstance(topic, dict):
            continue
        key = str(topic.get("topic_key", ""))
        if key not in existing_pages or key in seen:
            continue
        seen.add(key)
        count = int(topic.get("entry_count", 0)) + int(topic.get("atom_count", 0))
        links.append((key, count))
    return tuple(sorted(links, key=lambda item: (-item[1], item[0])))
