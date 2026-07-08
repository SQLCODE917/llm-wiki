"""Filesystem-backed source text lookup for strict evidence checks."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from llmwiki.domain.evidence_registry import SourceText, source_text_from_text
from llmwiki.domain.source_map import normalized_source_map_from_json, source_map_text


class FileSourceTextResolver:
    def __init__(self, raw_dir: Path, cache_dir: Path) -> None:
        self._raw_dir = raw_dir
        self._cache_dir = cache_dir
        self._cache: dict[str, tuple[str, ...] | None] = {}

    def source_lines(self, source_path: str) -> tuple[str, ...] | None:
        if source_path in self._cache:
            return self._cache[source_path]
        rel = source_path.removeprefix("raw/")
        lines = self._load_raw_text(rel)
        if lines is None and rel.lower().endswith(".pdf"):
            lines = self._load_cached_pdf_text(rel)
        self._cache[source_path] = lines
        return lines

    def source_text(self, source_locator: str) -> SourceText | None:
        if source_locator.lower().endswith(".pdf"):
            text = self._load_cached_pdf_joined_text(source_locator)
            if text is None:
                return None
            return source_text_from_text(source_locator, text, "pdf-cache")
        path = (self._raw_dir / source_locator).resolve()
        if not path.is_relative_to(self._raw_dir.resolve()) or not path.is_file():
            return None
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return None
        return SourceText(
            source_locator=source_locator,
            source_hash=_sha256(path),
            source_text_kind="markdown",
            lines=tuple(text.splitlines()),
        )

    def _load_raw_text(self, rel_path: str) -> tuple[str, ...] | None:
        path = (self._raw_dir / rel_path).resolve()
        if not path.is_relative_to(self._raw_dir.resolve()) or not path.is_file():
            return None
        if path.suffix.lower() == ".pdf":
            return None
        try:
            return tuple(path.read_text(encoding="utf-8").splitlines())
        except UnicodeDecodeError:
            return None

    def _load_cached_pdf_text(self, source_rel: str) -> tuple[str, ...] | None:
        text = self._load_cached_pdf_joined_text(source_rel)
        return tuple(text.splitlines()) if text is not None else None

    def _load_cached_pdf_joined_text(self, source_rel: str) -> str | None:
        for manifest_path in sorted(self._cache_dir.glob("*/manifest.json")):
            data: dict[str, Any] = json.loads(manifest_path.read_text(encoding="utf-8"))
            if data.get("source") != source_rel:
                continue
            source_map_path = manifest_path.parent / "normalized_source_map.json"
            if not source_map_path.is_file():
                return None
            source_map = normalized_source_map_from_json(
                source_map_path.read_text(encoding="utf-8")
            )
            return source_map_text(source_map)
        return None


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()
