#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from wiki_common import (
    iter_content_pages,
    markdown_links,
    one_line,
    page_node_id,
    parse_frontmatter,
    section,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate wiki/_graph.json from wiki markdown files.")
    parser.add_argument("--check", action="store_true", help="do not write; fail if graph is stale")
    args = parser.parse_args()

    graph_path = Path("wiki/_graph.json")
    existing = _read_existing(graph_path)
    graph = build_graph(existing)
    rendered = json.dumps(graph, indent=2, sort_keys=False) + "\n"

    if args.check:
        current = graph_path.read_text() if graph_path.exists() else ""
        if current != rendered:
            print("FAIL: wiki/_graph.json is stale; run pnpm wiki:graph")
            return 1
        print("PASS: wiki/_graph.json is current")
        return 0

    graph_path.write_text(rendered)
    print(f"wrote {graph_path}")
    return 0


def build_graph(existing: dict[str, object]) -> dict[str, object]:
    meta = existing.get("_meta") if isinstance(existing.get("_meta"), dict) else {}
    version = meta.get("version", "0.1.0") if isinstance(meta, dict) else "0.1.0"

    node_ids_by_path = {path.resolve(): page_node_id(path) for path in iter_content_pages()}
    nodes: dict[str, object] = {}

    for path in iter_content_pages():
        fm = parse_frontmatter(path)
        rel = path.as_posix()
        node_id = page_node_id(path)
        depends_on = []
        for link in markdown_links(path):
            if link.resolved and link.resolved in node_ids_by_path:
                depends_on.append(node_ids_by_path[link.resolved])

        summary = section(fm.body, "## Summary")
        description = one_line(summary or _first_paragraph(fm.body) or str(fm.data.get("title", path.stem)))
        sources = fm.data.get("sources", [])
        if not isinstance(sources, list):
            sources = []

        nodes[node_id] = {
            "type": str(fm.data.get("type", "unknown")),
            "path": rel,
            "description": description,
            "sources": sorted(str(source) for source in sources),
            "depends_on": sorted(set(depends_on)),
        }

    return {
        "_meta": {
            "domain": "llm-wiki",
            "version": str(version),
            "updated": date.today().isoformat(),
            "generated_by": "tools/wiki_graph.py",
        },
        "nodes": nodes,
    }


def _read_existing(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def _first_paragraph(body: str) -> str:
    lines = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "---":
            if lines:
                break
            continue
        if stripped.startswith("- ") or stripped.startswith("|"):
            continue
        lines.append(stripped)
    return " ".join(lines)


if __name__ == "__main__":
    sys.exit(main())
