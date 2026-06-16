"""WikiStore: the only component that touches the wiki on disk.

Boundary contract (see design doc):
- `raw/` is read-only — there is no write API for it, and reads are
  confined to the directory (no traversal).
- Page writes are confined to `wiki/` and always upsert the page's
  index.md entry in the same operation, so the index can never go stale.
- log.md is append-only.

Error messages raised here are fed back to the model verbatim by forge's
tool-error channel, so they are written as corrective instructions.
"""

from __future__ import annotations

import re
from dataclasses import replace
from pathlib import Path

from llmwiki.config import SOURCE_READ_BUDGET_CHARS, WikiPaths
from llmwiki.domain.candidates import CandidateBacklog, backlog_from_json_text
from llmwiki.domain.citations import SourceInventory
from llmwiki.domain.index import (
    empty_index,
    index_page_names,
    remove_index_entry,
    upsert_index_entry,
)
from llmwiki.domain.log import format_log_entry
from llmwiki.domain.pages import WikiPage, parse_page, render_page, validate_page_name
from llmwiki.store.source_resolver import FileSourceTextResolver

_RESERVED_NAMES = frozenset({"index", "log"})
_TRUNCATION_MARKER = "\n\n[TRUNCATED: source exceeds the read budget; summarize what is shown]"


class WikiStoreError(Exception):
    """Base error; message is safe to feed back to the model."""


class PageNotFoundError(WikiStoreError):
    pass


class SourceNotFoundError(WikiStoreError):
    pass


class WikiStore:
    def __init__(self, paths: WikiPaths) -> None:
        self._paths = paths

    # -- schema layer -----------------------------------------------------

    def read_schema(self) -> str:
        return self._paths.schema_path.read_text(encoding="utf-8")

    # -- raw layer (read-only) ---------------------------------------------

    def source_path(self, rel_path: str) -> Path:
        """Resolve a raw-source path (read-only; confined to raw/)."""
        path = (self._paths.raw_dir / rel_path).resolve()
        if not path.is_relative_to(self._paths.raw_dir.resolve()):
            raise SourceNotFoundError(
                f"{rel_path!r} is outside raw/. Pass a path relative to raw/, e.g. 'article.md'."
            )
        if not path.is_file():
            available = ", ".join(self.list_sources()) or "none"
            raise SourceNotFoundError(f"No source at raw/{rel_path}. Available: {available}.")
        return path

    def read_source(self, rel_path: str) -> str:
        text = self.source_path(rel_path).read_text(encoding="utf-8")
        if len(text) > SOURCE_READ_BUDGET_CHARS:
            return text[:SOURCE_READ_BUDGET_CHARS] + _TRUNCATION_MARKER
        return text

    def list_sources(self) -> list[str]:
        raw = self._paths.raw_dir
        return sorted(
            str(p.relative_to(raw))
            for p in raw.rglob("*")
            if p.is_file() and not p.name.startswith(".")
        )

    def source_inventory(self) -> SourceInventory:
        """Return raw-source existence facts for deterministic citation checks."""

        return SourceInventory.from_raw_relative_paths(self.list_sources())

    def source_resolver(self) -> FileSourceTextResolver:
        """Return line-addressable raw/cached source text for evidence checks."""

        return FileSourceTextResolver(self._paths.raw_dir, self._paths.cache_dir)

    # -- wiki layer ---------------------------------------------------------

    def list_pages(self) -> list[str]:
        return sorted(
            p.stem for p in self._paths.wiki_dir.glob("*.md") if p.stem not in _RESERVED_NAMES
        )

    def read_page(self, name: str) -> str:
        validate_page_name(name)
        path = self._paths.wiki_dir / f"{name}.md"
        if name in _RESERVED_NAMES or not path.is_file():
            raise PageNotFoundError(
                f"No page named {name!r}. Use search_wiki to find existing pages."
            )
        return path.read_text(encoding="utf-8")

    def page_texts(self) -> dict[str, str]:
        return {name: self.read_page(name) for name in self.list_pages()}

    def write_page(self, page: WikiPage) -> None:
        if page.name in _RESERVED_NAMES:
            raise WikiStoreError(
                f"{page.name!r} is reserved (maintained by the harness); choose another name."
            )
        page_path = self._paths.wiki_dir / f"{page.name}.md"
        index_text = upsert_index_entry(self.read_index(), page.name, page.category, page.summary)
        page_path.write_text(render_page(page), encoding="utf-8")
        self._paths.index_path.write_text(index_text, encoding="utf-8")

    def rename_page(
        self,
        old_name: str,
        new_name: str,
        *,
        summary: str | None = None,
        today: str = "",
    ) -> None:
        old_page = parse_page(old_name, self.read_page(old_name))
        if old_name == new_name:
            raise WikiStoreError("Old and new page names are the same.")
        if new_name in self.list_pages():
            raise WikiStoreError(
                f"Page {new_name!r} already exists. Use merge_page to combine pages."
            )
        renamed = replace(
            old_page,
            name=new_name,
            summary=summary or old_page.summary,
            updated=today or old_page.updated,
        )
        self.write_page(renamed)
        self._rewrite_links(old_name, new_name)
        self._delete_page_file_and_index(old_name)

    def merge_page(
        self,
        old_name: str,
        target_name: str,
        *,
        summary: str | None = None,
        today: str = "",
    ) -> None:
        old_page = parse_page(old_name, self.read_page(old_name))
        target_page = parse_page(target_name, self.read_page(target_name))
        sources = tuple(dict.fromkeys((*target_page.sources, *old_page.sources)))
        merged = replace(
            target_page,
            summary=summary or target_page.summary,
            sources=sources,
            updated=today or target_page.updated,
        )
        self.write_page(merged)
        self._rewrite_links(old_name, target_name)
        self._delete_page_file_and_index(old_name)

    def _rewrite_links(self, old_name: str, new_name: str) -> None:
        pattern = re.compile(rf"\[\[{re.escape(old_name)}(?P<alias>\|[^\]]+)?\]\]")
        for page_name in self.list_pages():
            path = self._paths.wiki_dir / f"{page_name}.md"
            text = path.read_text(encoding="utf-8")
            rewritten = pattern.sub(lambda match: f"[[{new_name}{match['alias'] or ''}]]", text)
            if rewritten != text:
                path.write_text(rewritten, encoding="utf-8")

    def _delete_page_file_and_index(self, name: str) -> None:
        if name in _RESERVED_NAMES:
            raise WikiStoreError(f"{name!r} is reserved and cannot be deleted.")
        path = self._paths.wiki_dir / f"{name}.md"
        if path.is_file():
            path.unlink()
        index_text = remove_index_entry(self.read_index(), name)
        self._paths.index_path.write_text(index_text, encoding="utf-8")

    def ensure_navigation_files(self) -> None:
        """Create missing harness-owned navigation files for maintenance runs."""
        if not self._paths.index_path.exists():
            self._paths.index_path.write_text(empty_index(), encoding="utf-8")
        if not self._paths.log_path.exists():
            self._paths.log_path.write_text("# Log\n", encoding="utf-8")

    # -- harness-owned candidate backlog ------------------------------------

    def read_candidate_backlog(self) -> CandidateBacklog:
        if not self._paths.candidates_path.exists():
            return CandidateBacklog()
        return backlog_from_json_text(self._paths.candidates_path.read_text(encoding="utf-8"))

    def write_candidate_backlog(self, backlog: CandidateBacklog) -> None:
        self._paths.candidates_path.write_text(backlog.to_json_text(), encoding="utf-8")

    def read_graph_json(self) -> str | None:
        if not self._paths.graph_path.exists():
            return None
        return self._paths.graph_path.read_text(encoding="utf-8")

    def write_graph_json(self, text: str) -> None:
        self._paths.graph_path.write_text(text, encoding="utf-8")

    # -- navigation files ----------------------------------------------------

    def read_index(self) -> str:
        return self._paths.index_path.read_text(encoding="utf-8")

    def index_names(self) -> set[str]:
        return index_page_names(self.read_index())

    def append_log(self, date_iso: str, op: str, subject: str, detail: str) -> None:
        entry = format_log_entry(date_iso, op, subject, detail)
        with self._paths.log_path.open("a", encoding="utf-8") as fh:
            fh.write(entry)
