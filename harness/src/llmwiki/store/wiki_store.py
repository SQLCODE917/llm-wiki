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

import hashlib
import re
from dataclasses import replace
from pathlib import Path

from llmwiki.config import SOURCE_READ_BUDGET_CHARS, WikiPaths
from llmwiki.domain.candidates import CandidateBacklog, backlog_from_json_text
from llmwiki.domain.citations import SourceInventory
from llmwiki.domain.evidence_locator_index import (
    EvidenceLocatorIndex,
)
from llmwiki.domain.evidence_locator_index_io import (
    evidence_locator_index_from_json,
)
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.evidence_registry_io import registry_from_json
from llmwiki.domain.index import (
    empty_index,
    index_page_ids,
    remove_index_entry,
    upsert_index_entry,
)
from llmwiki.domain.ingest_route_history import IngestRoutePlanRecord
from llmwiki.domain.log import format_log_entry
from llmwiki.domain.objects import RawSource
from llmwiki.domain.pages import (
    LOCAL_FLAT_STRUCTURE,
    PageMetadata,
    WikiPage,
    WikiStructure,
    parse_page,
    render_page,
    validate_page_id,
)
from llmwiki.domain.source_summary import (
    SourceSummaryDraftArtifact,
    source_summary_draft_from_json,
)
from llmwiki.store.source_resolver import FileSourceTextResolver

_RESERVED_PAGE_IDS = frozenset({"index", "log"})
_TRUNCATION_MARKER = "\n\n[TRUNCATED: source exceeds the read budget; summarize what is shown]"


class WikiStoreError(Exception):
    """Base error; message is safe to feed back to the model."""


class PageNotFoundError(WikiStoreError):
    pass


class SourceNotFoundError(WikiStoreError):
    pass


class WikiStore:
    def __init__(self, paths: WikiPaths, structure: WikiStructure = LOCAL_FLAT_STRUCTURE) -> None:
        self._paths = paths
        self._structure = structure

    @property
    def structure(self) -> WikiStructure:
        return self._structure

    # -- schema layer -----------------------------------------------------

    def read_schema(self) -> str:
        return self._paths.schema_path.read_text(encoding="utf-8")

    # -- raw layer (read-only) ---------------------------------------------

    def raw_source_path(self, source_locator: str) -> Path:
        """Resolve a RawSource locator (read-only; confined to raw/)."""
        path = (self._paths.raw_dir / source_locator).resolve()
        if not path.is_relative_to(self._paths.raw_dir.resolve()):
            raise SourceNotFoundError(
                f"{source_locator!r} is outside raw/. "
                "Pass a source_locator relative to raw/, e.g. 'article.md'."
            )
        if not path.is_file():
            available = ", ".join(self.list_sources()) or "none"
            raise SourceNotFoundError(
                f"No RawSource at raw/{source_locator}. Available: {available}."
            )
        return path

    def raw_source(self, source_locator: str) -> RawSource:
        self.raw_source_path(source_locator)
        return RawSource.from_locator(source_locator)

    def read_source(self, source_locator: str) -> str:
        text = self.raw_source_path(source_locator).read_text(encoding="utf-8")
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
            p.stem
            for p in self._paths.wiki_dir.rglob("*.md")
            if p.stem not in _RESERVED_PAGE_IDS and not _is_hidden_path(p, self._paths.wiki_dir)
        )

    def read_page(self, page_id: str) -> str:
        validate_page_id(page_id)
        path = self.page_path_for_page_id(page_id)
        if page_id in _RESERVED_PAGE_IDS or not path.is_file():
            raise PageNotFoundError(
                f"No WikiPage with page_id {page_id!r}. Use search_wiki to find existing pages."
            )
        return path.read_text(encoding="utf-8")

    def read_wiki_page(self, page_id: str) -> WikiPage:
        return parse_page(self.read_page(page_id))

    def page_texts(self) -> dict[str, str]:
        return {page_id: self.read_page(page_id) for page_id in self.list_pages()}

    def write_page(self, page: WikiPage) -> None:
        if page.page_id in _RESERVED_PAGE_IDS:
            raise WikiStoreError(f"{page.page_id!r} is reserved; choose another page_id.")
        page_path = self.page_path(page)
        self._ensure_wiki_path(page_path)
        page_path.parent.mkdir(parents=True, exist_ok=True)
        index_text = upsert_index_entry(self.read_index(), page.page_metadata)
        page_path.write_text(render_page(page), encoding="utf-8")
        self._paths.index_path.write_text(index_text, encoding="utf-8")

    def page_path_for_page_id(self, page_id: str) -> Path:
        candidates = self._page_paths_for_page_id(page_id)
        if len(candidates) == 1:
            return candidates[0]
        if len(candidates) > 1:
            rendered = ", ".join(str(path.relative_to(self._paths.wiki_dir)) for path in candidates)
            raise WikiStoreError(f"Multiple WikiPages with page_id {page_id!r}: {rendered}.")
        metadata = PageMetadata(page_id=page_id, page_kind="source", summary="placeholder")
        page = WikiPage.from_metadata(metadata, "")
        return self._paths.wiki_dir / page.page_path(self._structure)

    def page_path(self, page: WikiPage) -> Path:
        return self._paths.wiki_dir / page.page_path(self._structure)

    def rendered_page_path(self, page: WikiPage) -> str:
        return str(page.page_path(self._structure))

    def _ensure_wiki_path(self, path: Path) -> None:
        if not path.resolve().is_relative_to(self._paths.wiki_dir.resolve()):
            raise WikiStoreError(f"Rendered PagePath {path} is outside wiki/.")

    def _page_paths_for_page_id(self, page_id: str) -> list[Path]:
        validate_page_id(page_id)
        return sorted(
            path
            for path in self._paths.wiki_dir.rglob(f"{page_id}.md")
            if path.stem == page_id and not _is_hidden_path(path, self._paths.wiki_dir)
        )

    def rename_page(
        self,
        old_name: str,
        new_name: str,
        *,
        summary: str | None = None,
        today: str = "",
    ) -> None:
        old_page = self.read_wiki_page(old_name)
        if old_name == new_name:
            raise WikiStoreError("Old and new page names are the same.")
        if new_name in self.list_pages():
            raise WikiStoreError(
                f"Page {new_name!r} already exists. Use merge_page to combine pages."
            )
        metadata = replace(
            old_page.page_metadata,
            page_id=new_name,
            summary=summary or old_page.summary,
            updated=today or old_page.updated,
        )
        renamed = WikiPage.from_metadata(metadata, old_page.page_body)
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
        old_page = self.read_wiki_page(old_name)
        target_page = self.read_wiki_page(target_name)
        sources = tuple(dict.fromkeys((*target_page.sources, *old_page.sources)))
        metadata = replace(
            target_page.page_metadata,
            summary=summary or target_page.summary,
            sources=sources,
            updated=today or target_page.updated,
        )
        merged = WikiPage.from_metadata(metadata, target_page.page_body)
        self.write_page(merged)
        self._rewrite_links(old_name, target_name)
        self._delete_page_file_and_index(old_name)

    def delete_page(self, name: str) -> None:
        self._delete_page_file_and_index(name)

    def replace_page_link(
        self,
        page_name: str,
        old_target: str,
        new_target: str,
        *,
        alias: str | None = None,
        today: str = "",
    ) -> None:
        if alias is not None and ("]" in alias or "\n" in alias):
            raise WikiStoreError("Link aliases cannot contain ']' or newlines.")
        page = self.read_wiki_page(page_name)
        self.read_page(new_target)
        pattern = re.compile(rf"\[\[{re.escape(old_target)}(?P<alias>\|[^\]]+)?\]\]")
        body = pattern.sub(
            lambda match: f"[[{new_target}{match['alias'] or (f'|{alias}' if alias else '')}]]",
            page.page_body,
        )
        if body == page.page_body:
            raise WikiStoreError(f"Page {page_name!r} does not link to {old_target!r}.")
        metadata = replace(page.page_metadata, updated=today or page.updated)
        self.write_page(WikiPage.from_metadata(metadata, body))

    def _rewrite_links(self, old_name: str, new_name: str) -> None:
        pattern = re.compile(rf"\[\[{re.escape(old_name)}(?P<alias>\|[^\]]+)?\]\]")
        for page_name in self.list_pages():
            path = self.page_path_for_page_id(page_name)
            text = path.read_text(encoding="utf-8")
            rewritten = pattern.sub(lambda match: f"[[{new_name}{match['alias'] or ''}]]", text)
            if rewritten != text:
                path.write_text(rewritten, encoding="utf-8")

    def _delete_page_file_and_index(self, name: str) -> None:
        if name in _RESERVED_PAGE_IDS:
            raise WikiStoreError(f"{name!r} is reserved and cannot be deleted.")
        path = self.page_path_for_page_id(name)
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

    # -- harness-owned global ingest planning artifacts ---------------------

    def page_plan_artifact_dir(self, source_locator: str) -> Path:
        digest = hashlib.sha256(source_locator.encode("utf-8")).hexdigest()[:12]
        stem = re.sub(r"[^a-z0-9]+", "-", Path(source_locator).stem.lower()).strip("-")
        return self._paths.cache_dir / "page-plans" / f"{stem or 'source'}-{digest}"

    def write_page_plan_artifacts(
        self, source_locator: str, page_plan_json: str, observation_report: str
    ) -> tuple[Path, Path]:
        artifact_dir = self.page_plan_artifact_dir(source_locator)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        plan_path = artifact_dir / "page-plan.json"
        report_path = artifact_dir / "observation-report.md"
        plan_path.write_text(page_plan_json, encoding="utf-8")
        report_path.write_text(observation_report, encoding="utf-8")
        return plan_path, report_path

    def write_evidence_registry_artifact(
        self, source_locator: str, evidence_registry_json: str
    ) -> Path:
        artifact_dir = self.page_plan_artifact_dir(source_locator)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        registry_path = artifact_dir / "evidence-registry.json"
        registry_path.write_text(evidence_registry_json, encoding="utf-8")
        return registry_path

    def read_evidence_registry_artifact(self, source_locator: str) -> EvidenceRegistry | None:
        registry_path = self.page_plan_artifact_dir(source_locator) / "evidence-registry.json"
        if not registry_path.is_file():
            return None
        return registry_from_json(registry_path.read_text(encoding="utf-8"))

    def write_evidence_locator_index_artifact(
        self, source_locator: str, evidence_locator_index_json: str
    ) -> Path:
        artifact_dir = self.page_plan_artifact_dir(source_locator)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        locator_path = artifact_dir / "evidence-locators.json"
        locator_path.write_text(evidence_locator_index_json, encoding="utf-8")
        return locator_path

    def read_evidence_locator_index_artifact(
        self, source_locator: str
    ) -> EvidenceLocatorIndex | None:
        locator_path = self.page_plan_artifact_dir(source_locator) / "evidence-locators.json"
        if not locator_path.is_file():
            return None
        return evidence_locator_index_from_json(locator_path.read_text(encoding="utf-8"))

    def write_source_summary_draft_artifact(
        self,
        source_locator: str,
        planned_write_id: str,
        draft_json: str,
    ) -> Path:
        artifact_dir = self.page_plan_artifact_dir(source_locator) / "accepted-source-summaries"
        artifact_dir.mkdir(parents=True, exist_ok=True)
        draft_path = artifact_dir / f"{planned_write_id}.json"
        draft_path.write_text(draft_json, encoding="utf-8")
        return draft_path

    def read_source_summary_draft_artifacts(
        self, source_locator: str | None = None
    ) -> tuple[SourceSummaryDraftArtifact, ...]:
        source_locators = (source_locator,) if source_locator else self.list_sources()
        artifacts: list[SourceSummaryDraftArtifact] = []
        for locator in source_locators:
            artifact_dir = self.page_plan_artifact_dir(locator) / "accepted-source-summaries"
            if not artifact_dir.is_dir():
                continue
            for draft_path in sorted(artifact_dir.glob("*.json")):
                write_id = draft_path.stem
                artifacts.append(
                    SourceSummaryDraftArtifact(
                        source_locator=locator,
                        write_id=write_id,
                        page_id_hint=write_id.removeprefix("write-"),
                        draft=source_summary_draft_from_json(
                            draft_path.read_text(encoding="utf-8")
                        ),
                    )
                )
        return tuple(artifacts)

    # -- harness-owned ingest route plan history ----------------------------

    def append_ingest_route_plan_record(self, record: IngestRoutePlanRecord) -> None:
        self._paths.route_plan_history_path.parent.mkdir(parents=True, exist_ok=True)
        with self._paths.route_plan_history_path.open("a", encoding="utf-8") as fh:
            fh.write(record.to_json_line() + "\n")

    # -- navigation files ----------------------------------------------------

    def read_index(self) -> str:
        return self._paths.index_path.read_text(encoding="utf-8")

    def index_page_ids(self) -> set[str]:
        return index_page_ids(self.read_index())

    def append_log(self, date_iso: str, op: str, subject: str, detail: str) -> None:
        entry = format_log_entry(date_iso, op, subject, detail)
        with self._paths.log_path.open("a", encoding="utf-8") as fh:
            fh.write(entry)


def _is_hidden_path(path: Path, root: Path) -> bool:
    return any(part.startswith(".") for part in path.relative_to(root).parts)
