"""Shared fixtures: a temporary three-layer wiki tree and its store."""

from pathlib import Path

import pytest

from llmwiki.config import WikiPaths
from llmwiki.store import WikiStore

INDEX_SKELETON = """# Index

## Sources

## Entities

## Concepts

## Syntheses
"""


@pytest.fixture
def paths(tmp_path: Path) -> WikiPaths:
    (tmp_path / "raw").mkdir()
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "index.md").write_text(INDEX_SKELETON, encoding="utf-8")
    (wiki / "log.md").write_text("# Log\n", encoding="utf-8")
    (tmp_path / "SCHEMA.md").write_text("# Schema\n\nTest conventions.\n", encoding="utf-8")
    return WikiPaths(root=tmp_path)


@pytest.fixture
def store(paths: WikiPaths) -> WikiStore:
    return WikiStore(paths)
