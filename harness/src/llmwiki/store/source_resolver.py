"""Filesystem-backed source text lookup for strict evidence checks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


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
        for manifest_path in sorted(self._cache_dir.glob("*/manifest.json")):
            try:
                data: dict[str, Any] = json.loads(manifest_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if data.get("source") != source_rel:
                continue
            chunks_dir = manifest_path.parent / "chunks"
            chunk_texts = [
                path.read_text(encoding="utf-8")
                for path in sorted(chunks_dir.glob("*.md"))
                if path.is_file()
            ]
            return tuple("\n\n".join(chunk_texts).splitlines()) if chunk_texts else None
        return None
