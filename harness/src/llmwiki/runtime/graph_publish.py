"""Harness-owned wiki graph publication."""

from __future__ import annotations

from llmwiki.domain.graph import GraphStatus, build_wiki_graph, graph_status
from llmwiki.store import WikiStore


def refresh_wiki_graph(store: WikiStore, *, today: str) -> GraphStatus:
    graph = build_wiki_graph(store.page_texts(), generated_date=today)
    store.write_graph_json(graph.to_json_text())
    return graph_status(graph, store.read_graph_json())
