"""Deterministic wiki graph export."""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal

from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.system_pages import SYSTEM_PAGES

GRAPH_SCHEMA_VERSION = 1
GRAPH_GENERATOR = "llmwiki.graph.v1"
GraphArtifactStatus = Literal["missing", "current", "stale", "invalid"]


@dataclass(frozen=True)
class GraphNode:
    name: str
    category: str
    summary: str
    sources: tuple[str, ...]
    outbound_links: tuple[str, ...]


@dataclass(frozen=True)
class GraphEdge:
    source: str
    target: str
    resolved: bool


@dataclass(frozen=True)
class WikiGraph:
    nodes: tuple[GraphNode, ...]
    edges: tuple[GraphEdge, ...]
    generated_date: str

    def to_json_text(self) -> str:
        return json.dumps(self.to_payload(), indent=2, sort_keys=True) + "\n"

    def to_payload(self) -> dict[str, object]:
        return {
            "metadata": {
                "schema_version": GRAPH_SCHEMA_VERSION,
                "generator": GRAPH_GENERATOR,
                "generated_date": self.generated_date,
                "system_pages": "excluded",
            },
            "nodes": [
                {
                    "name": node.name,
                    "category": node.category,
                    "summary": node.summary,
                    "sources": list(node.sources),
                    "outbound_links": list(node.outbound_links),
                }
                for node in self.nodes
            ],
            "edges": [
                {"source": edge.source, "target": edge.target, "resolved": edge.resolved}
                for edge in self.edges
            ],
        }


@dataclass(frozen=True)
class GraphStatus:
    status: GraphArtifactStatus
    node_count: int
    edge_count: int
    unresolved_edge_count: int
    message: str

    @property
    def is_current(self) -> bool:
        return self.status == "current"

    def render(self) -> str:
        return (
            f"Graph export: {self.status}\n"
            f"Nodes: {self.node_count}\n"
            f"Edges: {self.edge_count}\n"
            f"Unresolved edges: {self.unresolved_edge_count}\n"
            f"{self.message}"
        )


def build_wiki_graph(page_texts: Mapping[str, str], *, generated_date: str) -> WikiGraph:
    page_names = {name for name in page_texts if name not in SYSTEM_PAGES}
    nodes: list[GraphNode] = []
    edges: list[GraphEdge] = []
    for name in sorted(page_names):
        text = page_texts[name]
        links = tuple(sorted(extract_links(text)))
        try:
            page = parse_page(text)
            category = page.category
            summary = page.summary
            sources = page.sources
        except PageError:
            category = "invalid"
            summary = "Invalid page frontmatter."
            sources = ()
        nodes.append(
            GraphNode(
                name=name,
                category=category,
                summary=summary,
                sources=tuple(sorted(sources)),
                outbound_links=links,
            )
        )
        for target in links:
            edges.append(GraphEdge(source=name, target=target, resolved=target in page_names))
    return WikiGraph(
        nodes=tuple(nodes),
        edges=tuple(sorted(edges, key=lambda edge: (edge.source, edge.target))),
        generated_date=generated_date,
    )


def graph_status(current_graph: WikiGraph, existing_json: str | None) -> GraphStatus:
    unresolved = sum(1 for edge in current_graph.edges if not edge.resolved)
    if existing_json is None:
        return GraphStatus(
            "missing",
            len(current_graph.nodes),
            len(current_graph.edges),
            unresolved,
            "wiki/wiki-graph.json is missing.",
        )
    try:
        existing = json.loads(existing_json)
    except json.JSONDecodeError:
        return GraphStatus(
            "invalid",
            len(current_graph.nodes),
            len(current_graph.edges),
            unresolved,
            "wiki/wiki-graph.json is not valid JSON.",
        )
    if _comparable(existing) == _comparable(current_graph.to_payload()):
        return GraphStatus(
            "current",
            len(current_graph.nodes),
            len(current_graph.edges),
            unresolved,
            "wiki/wiki-graph.json matches the current wiki graph.",
        )
    return GraphStatus(
        "stale",
        len(current_graph.nodes),
        len(current_graph.edges),
        unresolved,
        "wiki/wiki-graph.json differs from the current wiki graph.",
    )


def _comparable(payload: object) -> object:
    if not isinstance(payload, dict):
        return payload
    copied = dict(payload)
    metadata = copied.get("metadata")
    if isinstance(metadata, dict):
        metadata = dict(metadata)
        metadata.pop("generated_date", None)
        copied["metadata"] = metadata
    return copied
