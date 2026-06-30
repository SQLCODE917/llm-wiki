"""Operation orchestrator: arranges workflow, runner, transcript, and log.

Side effects are coordinated here; content decisions belong to the model
and bookkeeping formats to the domain layer. The LLM client and context
manager are injected, so tests drive the real WorkflowRunner with a fake
client and no network.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from forge.context import ContextManager
from forge.core.messages import Message, MessageMeta, MessageRole, MessageType
from forge.core.runner import WorkflowRunner

from llmwiki.config import StrictEvidenceMode
from llmwiki.domain.chat_grounding import (
    ChatEvidenceScope,
    ChatTaskMode,
    plan_chat_grounding,
    render_grounded_user_message,
)
from llmwiki.domain.chatwindow import QAPair
from llmwiki.domain.claim_support import (
    ClaimSupportAuditReport,
    ClaimSupportCandidate,
    ClaimSupportSelection,
    ClaimSupportVerdict,
)
from llmwiki.domain.contradictions import (
    ContradictionAuditReport,
    ContradictionFinding,
    ContradictionSelection,
)
from llmwiki.domain.evidence import EvidenceLintReport, EvidencePolicy
from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.evidence_registry import (
    SourceText,
    build_evidence_registry,
    source_text_from_text,
)
from llmwiki.domain.evidence_registry_io import registry_to_json
from llmwiki.domain.grounding import GroundingAuditReport, GroundingSelection, GroundingVerdict
from llmwiki.domain.ingest_profiles import (
    IngestProfile,
    prevents_singular_plural_siblings,
    required_new_page_prefix,
)
from llmwiki.domain.ingest_route_history import IngestRoutePlanRecord
from llmwiki.domain.ingest_route_plan import (
    IngestRouteContext,
    IngestRoutePlanScope,
    IngestRoutePlanState,
)
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.current_artifacts import build_current_ledger_artifacts
from llmwiki.domain.links import compute_findings, extract_links
from llmwiki.domain.objects import (
    IngestRun,
    LintRun,
    PagePlan,
    PlannedPageWrite,
    RawSource,
    SourceBundle,
    SourcePlan,
)
from llmwiki.domain.pages import PageMetadata, WikiPage, parse_page, slugify
from llmwiki.domain.planning import (
    build_markdown_page_plan,
    build_page_plan,
    observation_report,
    page_plan_from_json,
    page_plan_to_json,
)
from llmwiki.domain.planning_analysis import build_extracted_unit
from llmwiki.domain.salience import SalienceReport, compute_salience, reconcile_key_lists
from llmwiki.domain.search import render_hits, search_pages
from llmwiki.domain.semantic_lint import (
    SemanticFinding,
    SemanticLintReport,
    SemanticLintSelection,
)
from llmwiki.domain.source_page_groups import source_page_group_label
from llmwiki.domain.system_pages import (
    CLAIM_SUPPORT_PAGE,
    CONTRADICTIONS_PAGE,
    GROUNDING_PAGE,
    HEALTH_PAGE,
    ORPHAN_EXEMPT_PAGES,
    SEMANTIC_LINT_PAGE,
)
from llmwiki.domain.task_evidence import build_task_evidence_pack
from llmwiki.domain.technical_atom_builder import build_technical_atom_catalog
from llmwiki.domain.technical_atom_io import technical_atom_catalog_to_json
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog
from llmwiki.domain.topic_navigation import reconcile_topic_links
from llmwiki.pdf import PdfError
from llmwiki.pdf.document import DocumentModel
from llmwiki.pdf.manifest import ChunkRecord, Manifest
from llmwiki.pdf.pipeline import (
    ExtractionResult,
    chunk_file,
    read_document_model,
    read_source_text,
    save_manifest,
)
from llmwiki.runtime.cross_source_pipeline import build_cross_source_pages
from llmwiki.runtime.ledger_pipeline import build_source_ledger
from llmwiki.runtime.ledger_segmentation import ChunkText
from llmwiki.runtime.source_summary_replay import replay_source_summary_work_unit
from llmwiki.runtime.transcript import TranscriptWriter
from llmwiki.store import WikiStore
from llmwiki.workflows import (
    build_chat_file_workflow,
    build_chat_workflow,
    build_claim_support_workflow,
    build_contradiction_workflow,
    build_grounding_workflow,
    build_lint_workflow,
    build_query_workflow,
    build_semantic_lint_workflow,
)

_MAX_ITERATIONS = {
    "ingest": 24,
    "query": 12,
    "lint": 24,
    "contradictions": 18,
    "grounding": 18,
    "claim-support": 18,
    "semantic-lint": 18,
    "pdf-chunk": 24,
    "pdf-integrate": 32,
    "chat": 24,
    "chat-file": 14,
}
_MAX_TOOL_ERRORS = {
    "chat": 10,
}
_CLAIM_SUPPORT_BATCH_SIZE = 5

# (pdf_path, source_rel, reextract) -> ExtractionResult; injectable for tests.
ExtractFn = Callable[[Path, str, bool], ExtractionResult]

# Bare text usually means the model finished its work and wants to report.
# Name the terminal tool in the retry nudge so the model can exit the loop
# (forge ADR-013: small models need the structured way out spelled out).
_RETRY_NUDGES = {
    "ingest": (
        "Reply with exactly one tool call. Call plan_pages before write_page. "
        "If the wiki now fully reflects the source, call finish_ingest with "
        "your report; otherwise call the next tool you need."
    ),
    "query": ("Reply with exactly one tool call. Use respond to deliver your answer to the user."),
    "lint": (
        "Reply with exactly one tool call. If the review is complete, call "
        "finish_lint with the health report; otherwise call the next tool you need."
    ),
    "contradictions": (
        "Reply with exactly one tool call. If the audit is complete, call "
        "finish_contradictions with the audit report; otherwise call the next tool you need."
    ),
    "grounding": (
        "Reply with exactly one tool call. If the audit is complete, call "
        "finish_grounding with the audit report; otherwise call record_grounding_verdict."
    ),
    "claim-support": (
        "Reply with exactly one tool call. If the audit is complete, call "
        "finish_claim_support with the audit report; otherwise call "
        "record_claim_support_verdict."
    ),
    "semantic-lint": (
        "Reply with exactly one tool call. If the audit is complete, call "
        "finish_semantic_lint with the audit report; otherwise call "
        "record_semantic_finding or read_page."
    ),
    "pdf-chunk": (
        "Reply with exactly one tool call. Call plan_pages before write_page. "
        "If the wiki now reflects this chunk, call finish_chunk with your "
        "notes; otherwise call the next tool you need."
    ),
    "pdf-integrate": (
        "Reply with exactly one tool call. Call plan_pages before write_page. "
        "If the hub page and cross-links are in place, call finish_ingest "
        "with your report; otherwise call the next tool you need."
    ),
    "chat": (
        "Reply with exactly one tool call. If submit_procedure_execution is "
        "available, call submit_procedure_execution next with one step_result "
        "for every required step; use unresolved outputs instead of searching "
        "forever. Otherwise use respond to deliver your answer to the user."
    ),
    "chat-file": (
        "Reply with exactly one tool call. If the durable synthesis is filed "
        "or cannot be supported, call finish_chat_file; otherwise call the "
        "next tool you need."
    ),
}


@dataclass(frozen=True)
class OperationResult:
    op: str
    subject: str
    output: str
    transcript_path: Path | None


@dataclass(frozen=True)
class LintSnapshot:
    """Deterministic lint state at one point in the operation."""

    lint_run: LintRun
    evidence_report: EvidenceLintReport

    def render(self) -> str:
        return (
            "Link/index/orphan findings:\n"
            f"{self.lint_run.render()}\n\n"
            "Citation evidence findings:\n"
            f"{self.evidence_report.render()}"
        )


@dataclass(frozen=True)
class LintDelta:
    """Deterministic before/after change summary for a lint operation."""

    before: LintSnapshot
    after: LintSnapshot

    def render(self) -> str:
        before_orphans = set(self.before.lint_run.orphan_pages)
        after_orphans = set(self.after.lint_run.orphan_pages)
        before_broken = _broken_link_edges(self.before.lint_run)
        after_broken = _broken_link_edges(self.after.lint_run)
        before_evidence = set(self.before.evidence_report.findings)
        after_evidence = set(self.after.evidence_report.findings)
        return "\n\n".join(
            [
                _render_name_delta(
                    "Resolved orphan pages",
                    sorted(before_orphans - after_orphans),
                ),
                _render_name_delta("New orphan pages", sorted(after_orphans - before_orphans)),
                _render_name_delta("Remaining orphan pages", sorted(after_orphans)),
                _render_count_delta("Broken link findings", len(before_broken), len(after_broken)),
                _render_count_delta(
                    "Pages missing from index.md",
                    len(self.before.lint_run.missing_from_index),
                    len(self.after.lint_run.missing_from_index),
                ),
                _render_count_delta(
                    "Stale index entries",
                    len(self.before.lint_run.stale_index_entries),
                    len(self.after.lint_run.stale_index_entries),
                ),
                _render_count_delta(
                    "Citation evidence findings",
                    len(before_evidence),
                    len(after_evidence),
                ),
            ]
        )


@dataclass(frozen=True)
class Session:
    """One operation run: explicit dependencies, one public method per op."""

    store: WikiStore
    client: Any  # forge LLMClient protocol
    context_manager: ContextManager
    today: str
    runs_dir: Path | None = None
    run_id: str = ""  # unique per run (e.g. timestamp); falls back to date
    extract_pdf: ExtractFn | None = None  # required for PDF ingest; CLI wires it
    on_chunk_note: Callable[[str], None] | None = None  # per-chunk supervision
    strict_evidence: StrictEvidenceMode = "off"
    ingest_profiles: tuple[IngestProfile, ...] = ()

    def _evidence_policy(self) -> EvidencePolicy:
        return EvidencePolicy(mode=self.strict_evidence)

    async def ingest(
        self, source_locator: str, reextract: bool = False, reintegrate: bool = False
    ) -> OperationResult:
        ingest_run = self._ingest_run(source_locator)
        source_locator = _single_source_locator(ingest_run)
        if source_locator.lower().endswith(".pdf"):
            return await self._ingest_pdf(source_locator, reextract, reintegrate, ingest_run)
        if reintegrate:
            raise PdfError("--reintegrate applies to chunked (PDF) sources only.")
        page_plan = self._markdown_page_plan(ingest_run, source_locator)
        self._persist_page_plan(source_locator, page_plan)
        source_text = source_text_from_text(source_locator, self.store.read_source(source_locator))
        return self._finish_ledger_ingest(
            source_locator=source_locator,
            page_plan=page_plan,
            chunks=_chunks_from_page_plan(page_plan),
            document_model=None,
            source_text=source_text,
            ingest_run=ingest_run,
        )

    async def _ingest_pdf(
        self,
        source_locator: str,
        reextract: bool,
        reintegrate: bool = False,
        ingest_run: IngestRun | None = None,
    ) -> OperationResult:
        if ingest_run is None:
            ingest_run = self._ingest_run(source_locator)
        source_locator = _single_source_locator(ingest_run)
        if self.extract_pdf is None:
            raise RuntimeError("Session has no PDF extractor wired (extract_pdf).")
        result = self.extract_pdf(
            self.store.raw_source_path(source_locator), source_locator, reextract
        )
        page_plan = self._pdf_page_plan(
            ingest_run,
            source_locator,
            result,
            reuse_persisted=not reextract,
        )
        cached_plan_is_current = (
            not reextract
            and self._cached_pdf_page_plan(source_locator, result.manifest, result.cache_dir)
            is not None
        )
        self._persist_page_plan(
            source_locator,
            page_plan,
            reuse_technical_catalog=reintegrate,
            skip_existing_artifacts=cached_plan_is_current,
        )
        save_manifest(
            ExtractionResult(manifest=result.manifest.mark_integrated(), cache_dir=result.cache_dir)
        )
        source_text = source_text_from_text(
            source_locator, read_source_text(result.cache_dir), "pdf-cache"
        )
        return self._finish_ledger_ingest(
            source_locator=source_locator,
            page_plan=page_plan,
            chunks=_chunks_from_page_plan(page_plan),
            document_model=read_document_model(result.cache_dir),
            source_text=source_text,
            ingest_run=ingest_run,
        )

    def _finish_ledger_ingest(
        self,
        *,
        source_locator: str,
        page_plan: PagePlan,
        chunks: tuple[ChunkText, ...],
        document_model: DocumentModel | None,
        source_text: SourceText,
        ingest_run: IngestRun,
    ) -> OperationResult:
        registry = build_evidence_registry(page_plan, (source_text,))
        registry_hash = short_digest(registry_to_json(registry), 32)
        ledger = build_source_ledger(
            source_locator=source_locator,
            source_hash=source_text.source_hash,
            evidence_registry_hash=registry_hash,
            chunks=chunks,
            document_model=document_model,
            source_claims=page_plan.source_claims,
            today=self.today,
            schema=ingest_run.schema,
        )
        self.store.write_ledger_artifacts(source_locator, ledger.artifact_files)
        written = "none (authoritative write blocked; see blocked-write-diagnostic.json)"
        if ledger.wiki_page is not None:
            self.store.write_page(ledger.wiki_page)
            written = f"[[{ledger.page_id}]]"
        for topic_page in ledger.topic_pages:
            self.store.write_page(topic_page)
        if ledger.wiki_page is not None:
            keep_page_ids = {
                ledger.wiki_page.page_id,
                *(page.page_id for page in ledger.topic_pages),
            }
            self.store.delete_source_pages_not_in(source_locator, keep_page_ids)
        if self.on_chunk_note is not None:
            self.on_chunk_note(ledger.summary)
        report = (
            f"Claim-ledger ingest of raw/{source_locator} ({len(chunks)} source unit(s)).\n"
            f"{ledger.summary}\n"
            f"Source page: {written}; linked pages: {len(ledger.topic_pages)}. "
            f"Ledger artifacts: {self.store.page_plan_artifact_dir(source_locator)}/ledger."
        )
        self.store.append_log(self.today, "ingest", source_locator, report)
        return OperationResult("ingest", source_locator, report, None)

    async def synthesize(self) -> OperationResult:
        """Build canonical concept pages from stored topic indexes and ledgers."""
        topic_jsons = tuple(self.store.list_topic_index_artifacts())
        claim_ledger_jsons = tuple(self.store.list_claim_ledger_artifacts())
        if len(topic_jsons) < 2:
            report = (
                "Cross-source synthesis needs at least two ingested sources with topic indexes; "
                f"found {len(topic_jsons)}."
            )
            self.store.append_log(self.today, "synthesize", "cross-source", report)
            return OperationResult("synthesize", "cross-source", report, None)
        result = build_cross_source_pages(topic_jsons, claim_ledger_jsons, today=self.today)
        for page in result.pages:
            self.store.write_page(page)
        self.store.delete_cross_source_pages_not_in({page.page_id for page in result.pages})
        self.store.append_log(self.today, "synthesize", "cross-source", result.summary)
        return OperationResult("synthesize", "cross-source", result.summary, None)

    def _ingest_run(self, source_locator: str) -> IngestRun:
        raw_source = self.store.raw_source(source_locator)
        return IngestRun(
            source_bundle=SourceBundle.one(raw_source),
            source_plans=(
                SourcePlan(
                    raw_source=raw_source,
                    source_classification=raw_source.source_format,
                    ingest_disposition="plan-pages",
                ),
            ),
        )

    def _markdown_page_plan(self, ingest_run: IngestRun, source_locator: str) -> PagePlan:
        raw_source = _single_raw_source(ingest_run)
        return build_markdown_page_plan(
            plan_id=self._page_plan_id(source_locator, "source"),
            source_bundle=ingest_run.source_bundle,
            raw_source=raw_source,
            source_text=self.store.read_source(source_locator),
            existing_pages=self.store.page_texts(),
            wiki_structure=ingest_run.wiki_structure,
            today=self.today,
            schema=ingest_run.schema,
            source_plan=_source_plan_for(ingest_run, raw_source),
            new_page_prefix=required_new_page_prefix(self.ingest_profiles, source_locator),
        )

    def _pdf_page_plan(
        self,
        ingest_run: IngestRun,
        source_locator: str,
        result: ExtractionResult,
        *,
        reuse_persisted: bool = True,
    ) -> PagePlan:
        if reuse_persisted and _manifest_has_progress(result.manifest):
            cached_plan = self._cached_pdf_page_plan(
                source_locator, result.manifest, result.cache_dir
            )
            if cached_plan is not None:
                return cached_plan
        raw_source = _single_raw_source(ingest_run)
        units = tuple(
            build_extracted_unit(
                unit_id=f"unit-{record.chunk_id:04d}",
                raw_source=raw_source,
                locator=f"p.{record.start_page}-{record.end_page}",
                heading_path=record.heading,
                text=chunk_file(result.cache_dir, record.chunk_id).read_text(encoding="utf-8"),
            )
            for record in result.manifest.chunks
        )
        return build_page_plan(
            plan_id=self._page_plan_id(source_locator, "pdf"),
            source_bundle=ingest_run.source_bundle,
            raw_source=raw_source,
            extracted_units=units,
            existing_pages=self.store.page_texts(),
            wiki_structure=ingest_run.wiki_structure,
            today=self.today,
            schema=ingest_run.schema,
            source_plan=_source_plan_for(ingest_run, raw_source),
            new_page_prefix=self._pdf_page_prefix(source_locator),
        )

    def _cached_pdf_page_plan(
        self, source_locator: str, manifest: Manifest, cache_dir: Path
    ) -> PagePlan | None:
        cached = self.store.read_page_plan_artifact(source_locator)
        if cached is None:
            return None
        try:
            plan = page_plan_from_json(cached)
        except Exception:
            return None
        if not _pdf_page_plan_matches_manifest(plan, source_locator, manifest):
            return None
        if not _pdf_page_plan_matches_cache_text(plan, manifest, cache_dir):
            return None
        return plan

    def _persist_page_plan(
        self,
        source_locator: str,
        page_plan: PagePlan,
        *,
        reuse_technical_catalog: bool = False,
        skip_existing_artifacts: bool = False,
    ) -> str:
        report = observation_report(page_plan)
        has_page_plan_artifact = self.store.read_page_plan_artifact(source_locator) is not None
        if skip_existing_artifacts and has_page_plan_artifact:
            return report
        if reuse_technical_catalog and has_page_plan_artifact:
            return report
        self.store.write_page_plan_artifacts(source_locator, page_plan_to_json(page_plan), report)
        source_texts = tuple(
            source_text
            for raw_source in page_plan.source_bundle.raw_sources
            if (source_text := self.store.source_resolver().source_text(raw_source.source_locator))
            is not None
        )
        registry = build_evidence_registry(page_plan, source_texts)
        self.store.write_evidence_registry_artifact(source_locator, registry_to_json(registry))
        existing_catalog = self.store.read_technical_atom_catalog_artifact(source_locator)
        catalog: TechnicalAtomCatalog | None
        if not _has_matching_technical_catalog(
            existing_catalog,
            page_plan.plan_id,
            reuse_technical_catalog,
        ):
            catalog = build_technical_atom_catalog(
                source_locator=source_locator,
                page_plan=page_plan,
                evidence_registry=registry,
                artifact_fingerprint=page_plan.plan_id,
            )
            self.store.write_technical_atom_catalog_artifact(
                source_locator,
                technical_atom_catalog_to_json(catalog),
            )
        else:
            catalog = existing_catalog
        if catalog is not None:
            ledger_artifacts = build_current_ledger_artifacts(
                source_locator=source_locator,
                page_plan=page_plan,
                evidence_registry=registry,
                technical_atom_catalog=catalog,
            )
            self.store.write_claim_ledger_artifacts(source_locator, ledger_artifacts.artifact_files)
        return report

    def _recover_pending_pdf_chunks(
        self, manifest: Manifest, source_locator: str, page_plan: PagePlan
    ) -> Manifest:
        existing_pages = set(self.store.list_pages())
        hub = slugify(Path(source_locator).stem)
        planned_writes_by_page = {
            write.page_metadata.page_id: write for write in page_plan.planned_writes
        }
        for record in manifest.pending:
            targets = _page_plan_targets_for_chunk(page_plan, record.chunk_id, hub)
            if targets and all(
                target in existing_pages
                and self._pending_pdf_page_is_recoverable(planned_writes_by_page.get(target))
                for target in targets
            ):
                manifest = manifest.mark_done(
                    record.chunk_id,
                    "Recovered existing wiki page(s): " + ", ".join(targets),
                    pages_written=targets,
                    route_plan_pages=len(targets),
                )
        return manifest

    def _replay_completed_pdf_source_summary_pages(
        self, source_locator: str, page_plan: PagePlan, manifest: Manifest
    ) -> tuple[str, ...]:
        replayed_page_ids: list[str] = []
        for work_records in _pending_pdf_work_units(page_plan, manifest.chunks):
            replay = replay_source_summary_work_unit(
                self.store,
                self.today,
                source_locator,
                page_plan,
                work_records,
            )
            if replay is None:
                continue
            replayed_page_ids.extend(replay.page_ids)
            if self.on_chunk_note is not None:
                self.on_chunk_note(f"[{_work_unit_name(work_records)}] {replay.notes}")
        return tuple(dict.fromkeys(replayed_page_ids))

    @staticmethod
    def _pending_pdf_page_is_recoverable(planned_write: PlannedPageWrite | None) -> bool:
        return planned_write is None or planned_write.source_summary_plan is None

    def _verify_pdf_hub(
        self,
        hub_page_id: str,
        required_link_targets: tuple[str, ...],
        *,
        min_required_links: int,
    ) -> None:
        try:
            hub_text = self.store.read_page(hub_page_id)
        except Exception as exc:
            raise PdfError(
                f"PDF integration finished without writing hub page {hub_page_id!r}."
            ) from exc
        linked_targets = extract_links(hub_text) & frozenset(required_link_targets)
        if len(linked_targets) < min_required_links:
            raise PdfError(
                f"PDF integration hub {hub_page_id!r} links {len(linked_targets)} "
                f"chunk page(s), expected at least {min_required_links}."
            )

    def _page_plan_id(self, source_locator: str, scope: str) -> str:
        return f"{self.run_id or self.today}-{scope}-{slugify(Path(source_locator).stem)}"

    def _record_ingest_route_plan(
        self,
        state: IngestRoutePlanState,
        *,
        page_writes: tuple[str, ...] = (),
    ) -> None:
        if state.active_plan is None:
            return
        self.store.append_ingest_route_plan_record(
            IngestRoutePlanRecord.from_plan(
                state.active_plan,
                date=self.today,
                run_id=self.run_id,
                page_writes=page_writes,
            )
        )

    def _ingest_route_plan_state(
        self,
        source_locator: str,
        scope: IngestRoutePlanScope,
        *,
        chunk_id: int | None = None,
        page_plan: PagePlan | None = None,
    ) -> IngestRoutePlanState:
        return IngestRoutePlanState(
            IngestRouteContext(
                source_locator=source_locator,
                scope=scope,
                profile_ids=tuple(profile.id for profile in self.ingest_profiles),
                chunk_id=chunk_id,
                page_plan=page_plan,
                existing_pages=frozenset(self.store.list_pages()),
                new_page_prefix=(
                    self._pdf_page_prefix(source_locator)
                    if scope in {"pdf-chunk", "pdf-integrate"}
                    else required_new_page_prefix(self.ingest_profiles, source_locator)
                ),
                prevent_singular_plural_siblings=prevents_singular_plural_siblings(
                    self.ingest_profiles
                ),
            )
        )

    def _pdf_page_prefix(self, source_locator: str) -> str:
        return required_new_page_prefix(self.ingest_profiles, source_locator) or slugify(
            Path(source_locator).stem
        )

    def _page_sources_by_id(self) -> dict[str, tuple[str, ...]]:
        sources: dict[str, tuple[str, ...]] = {}
        for page_id in self.store.list_pages():
            try:
                sources[page_id] = self.store.read_wiki_page(page_id).page_metadata.sources
            except Exception:
                sources[page_id] = ()
        return sources

    def _reconcile_hub_key_lists(
        self, hub: str, salience: SalienceReport, source_locator: str
    ) -> None:
        """Harness-owned bookkeeping: the hub's key-lists mirror the salience
        report by construction (same contract as index.md entries)."""
        if hub not in self.store.list_pages():
            return  # no hub page; lint's findings will surface it
        page = parse_page(self.store.read_page(hub))
        body = reconcile_key_lists(page.page_body, salience)
        body = reconcile_topic_links(
            body,
            self.store.read_topic_index_artifact(source_locator),
            frozenset(self.store.list_pages()) - {hub},
        )
        if body != page.page_body:
            metadata = replace(page.page_metadata, updated=self.today)
            self.store.write_page(WikiPage.from_metadata(metadata, body))

    async def query(self, question: str) -> OperationResult:
        workflow = build_query_workflow(self.store, self.today, self._evidence_policy())
        answer, transcript = await self._run(workflow, question, "query")
        self.store.append_log(self.today, "query", question, answer)
        return OperationResult("query", question, answer, transcript)

    async def chat_turn(
        self, question: str, window: Sequence[QAPair], grounded: bool, tag: str
    ) -> tuple[str, Path | None]:
        """One read-only conversation turn, seeded with windowed Q/A pairs.

        The seed carries question/answer text only — prior tool calls and
        page contents are never replayed; evidence is re-fetched on demand.
        The current question chooses the evidence mode: catalog questions get
        the index, conversational refinements get the prior Q/A window, and
        fresh content lookups get deterministic search hints before the model
        reads wiki pages.
        """
        grounding_plan = plan_chat_grounding(question, grounded=grounded, has_window=bool(window))
        search_results = ""
        evidence_scope: ChatEvidenceScope | None = None
        task_evidence_pack_text = ""
        task_evidence_pack = None
        if grounding_plan.include_search_results:
            pages = self.store.page_texts()
            search_hits = search_pages(pages, question)
            search_results = render_hits(search_hits)
            evidence_scope = ChatEvidenceScope.from_search_hits(pages, search_hits)
            task_evidence_pack = build_task_evidence_pack(
                pages,
                search_hits,
                task_mode=grounding_plan.task_mode,
            )
            if task_evidence_pack is not None:
                task_evidence_pack_text = task_evidence_pack.render()
        workflow = build_chat_workflow(
            self.store,
            allow_index_response=grounding_plan.allow_index_response,
            require_wiki_read=grounding_plan.require_wiki_read,
            evidence_scope=evidence_scope,
            task_evidence_pack=task_evidence_pack,
            require_procedure_execution=task_evidence_pack is not None
            and grounding_plan.task_mode is ChatTaskMode.EXECUTE_PROCEDURE,
        )
        rendered = workflow.build_system_prompt(schema=self.store.read_schema())
        seed = [Message(MessageRole.SYSTEM, rendered, MessageMeta(MessageType.SYSTEM_PROMPT))]
        for pair in window:
            seed.append(
                Message(MessageRole.USER, pair.question, MessageMeta(MessageType.USER_INPUT))
            )
            seed.append(
                Message(MessageRole.ASSISTANT, pair.answer, MessageMeta(MessageType.TEXT_RESPONSE))
            )
        message = question
        if grounding_plan.include_index or grounding_plan.include_search_results:
            message = render_grounded_user_message(
                question,
                grounding_plan,
                index_text=self.store.read_index() if grounding_plan.include_index else "",
                search_results=search_results,
                task_evidence_pack=task_evidence_pack_text,
            )
        seed.append(Message(MessageRole.USER, message, MessageMeta(MessageType.USER_INPUT)))
        return await self._run(workflow, message, "chat", tag=tag, initial_messages=seed)

    async def file_chat_synthesis(
        self,
        page_id: str,
        question: str,
        answer: str,
        scope: str = "",
        tag: str = "chat-file",
    ) -> OperationResult:
        workflow = build_chat_file_workflow(self.store, self.today)
        slug = slugify(page_id)
        message = (
            f"File a durable synthesis WikiPage with PageId '{slug}' from the latest chat turn. "
            "Use page_kind='synthesis'. Chat text is context only; re-read current "
            "wiki pages before writing and cite wiki/raw evidence.\n\n"
            f"Requested scope: {scope or '(none provided)'}\n\n"
            f"Latest chat question:\n{question}\n\n"
            f"Latest chat answer:\n{answer}"
        )
        report, transcript = await self._run(workflow, message, "chat-file", tag=tag)
        self.store.append_log(self.today, "chat-file", slug, report)
        return OperationResult("chat-file", slug, report, transcript)

    async def lint(self) -> OperationResult:
        if not self.store.list_pages():
            report = "Wiki is empty — nothing to lint."
            self.store.append_log(self.today, "lint", "empty wiki", report)
            return OperationResult("lint", "wiki health", report, None)
        evidence_policy = self._evidence_policy()
        before = self._lint_snapshot(evidence_policy)
        workflow = build_lint_workflow(self.store, self.today, evidence_policy)
        salience_block = compute_salience(self.store.page_texts()).render()
        message = (
            "Run a lint pass. Deterministic findings from the harness:\n\n"
            f"{before.lint_run.render()}\n\n"
            "Citation evidence findings:\n\n"
            f"{before.evidence_report.render()}\n\n"
            f"{salience_block}\n"
            "The salience report names the most load-bearing pages — protect "
            "their content. Review the affected pages (and spot-check "
            "others), then call finish_lint with the health report."
        )
        model_report, transcript = await self._run(workflow, message, "lint")
        after = self._lint_snapshot(evidence_policy)
        verified_report = self._verified_lint_report(model_report, before, after)
        self._file_lint_report(verified_report)
        self.store.append_log(self.today, "lint", "wiki health", verified_report)
        return OperationResult("lint", "wiki health", verified_report, transcript)

    async def contradictions(self, selection: ContradictionSelection) -> OperationResult:
        findings: list[ContradictionFinding] = []
        if not selection.candidates:
            report = self._contradiction_report(selection, (), "No candidate pairs to audit.")
            self._file_contradiction_report(report)
            self.store.append_log(self.today, "contradiction", "contradiction audit", report)
            return OperationResult("contradictions", "contradiction audit", report, None)
        workflow = build_contradiction_workflow(self.store, findings)
        message = (
            "Run a contradiction audit over these bounded candidate pairs. "
            "Inspect pairs in order. Read the pages for the current pair before "
            "recording a finding, then either continue to the next pair or finish. "
            "Do not spend the whole tool budget trying to exhaust the wiki. Record "
            "only claims that cannot both be true as written.\n\n"
            f"Candidate pairs discovered: {selection.candidate_count}\n"
            f"Audited pairs: {selection.audited_count}\n"
            f"Skipped by cap: {selection.skipped_count}\n\n"
            f"{selection.render_for_prompt()}"
        )
        model_report, transcript = await self._run(workflow, message, "contradictions")
        report = self._contradiction_report(selection, tuple(findings), model_report)
        self._file_contradiction_report(report)
        self.store.append_log(self.today, "contradiction", "contradiction audit", report)
        return OperationResult("contradictions", "contradiction audit", report, transcript)

    async def grounding(self, selection: GroundingSelection) -> OperationResult:
        verdicts: list[GroundingVerdict] = []
        if not selection.candidates:
            report = self._grounding_report(selection, (), "No claim candidates to audit.")
            self._file_grounding_report(report)
            self.store.append_log(self.today, "grounding", "grounding audit", report)
            return OperationResult("grounding", "grounding audit", report, None)
        workflow = build_grounding_workflow(self.store, verdicts, selection.candidates)
        message = (
            "Run a grounding audit over these bounded claim candidates. "
            "Do not judge claims with deterministic citation failures; those are "
            "already reported by the harness. For each selected claim, decide "
            "whether the evidence supports the claim as written.\n\n"
            f"Claim candidates discovered: {selection.candidate_count}\n"
            f"Audited claims: {selection.audited_count}\n"
            f"Skipped by cap: {selection.skipped_count}\n\n"
            f"{selection.render_for_prompt()}"
        )
        model_report, transcript = await self._run(workflow, message, "grounding")
        report = self._grounding_report(selection, tuple(verdicts), model_report)
        self._file_grounding_report(report)
        self.store.append_log(self.today, "grounding", "grounding audit", report)
        return OperationResult("grounding", "grounding audit", report, transcript)

    async def claim_support_audit(
        self, selection: ClaimSupportSelection
    ) -> tuple[ClaimSupportAuditReport, Path | None]:
        verdicts: list[ClaimSupportVerdict] = []
        if not selection.candidates:
            return (
                self._claim_support_audit_report(
                    selection, (), "No claim-support candidates to audit."
                ),
                None,
            )
        model_reports: list[str] = []
        transcript: Path | None = None
        batches = _claim_support_batches(selection.candidates)
        for batch_index, candidates in enumerate(batches, 1):
            batch_selection = _claim_support_batch_selection(selection, candidates)
            workflow = build_claim_support_workflow(self.store, verdicts, candidates, ())
            message = _claim_support_audit_message(
                batch_selection=batch_selection,
                total_selected=selection.selected_count,
                batch_index=batch_index,
                batch_count=len(batches),
            )
            model_report, batch_transcript = await self._run(workflow, message, "claim-support")
            model_reports.append(model_report)
            transcript = transcript or batch_transcript
        return self._claim_support_audit_report(
            selection, tuple(verdicts), "\n\n".join(model_reports)
        ), transcript

    async def claim_support(self, selection: ClaimSupportSelection) -> OperationResult:
        audit, transcript = await self.claim_support_audit(selection)
        report = audit.render()
        self._file_claim_support_report(report)
        self.store.append_log(self.today, "claim-support", "claim support audit", report)
        return OperationResult("claim-support", "claim support audit", report, transcript)

    async def semantic_lint(self, selection: SemanticLintSelection) -> OperationResult:
        findings: list[SemanticFinding] = []
        if not selection.candidates:
            report = self._semantic_lint_report(
                selection, (), "No semantic lint candidates to audit."
            )
            self._file_semantic_lint_report(report)
            self.store.append_log(self.today, "semantic-lint", "semantic audit", report)
            return OperationResult("semantic-lint", "semantic audit", report, None)
        workflow = build_semantic_lint_workflow(self.store, findings)
        message = (
            "Run a bounded semantic lint audit over these candidate items. "
            "Read relevant pages before recording findings. Record only stale "
            "claims, possible supersessions, or data gaps that deserve curator "
            "review; do not edit pages.\n\n"
            f"Candidate items discovered: {selection.candidate_count}\n"
            f"Audited items: {selection.audited_count}\n"
            f"Skipped by cap: {selection.skipped_count}\n\n"
            f"{selection.render_for_prompt()}"
        )
        model_report, transcript = await self._run(workflow, message, "semantic-lint")
        report = self._semantic_lint_report(selection, tuple(findings), model_report)
        self._file_semantic_lint_report(report)
        self.store.append_log(self.today, "semantic-lint", "semantic audit", report)
        return OperationResult("semantic-lint", "semantic audit", report, transcript)

    def _lint_snapshot(self, evidence_policy: EvidencePolicy) -> LintSnapshot:
        page_texts = self.store.page_texts()
        inventory = self.store.source_inventory() if evidence_policy.enabled else None
        return LintSnapshot(
            lint_run=compute_findings(
                page_texts,
                self.store.index_page_ids(),
                exempt_from_orphans=ORPHAN_EXEMPT_PAGES,
            ),
            evidence_report=evidence_policy.lint_pages(
                page_texts,
                inventory,
                self.store.source_resolver() if evidence_policy.enabled else None,
                locator_index=self._latest_evidence_locator_index()
                if evidence_policy.enabled
                else None,
            ),
        )

    def _latest_evidence_locator_index(self) -> EvidenceLocatorIndex | None:
        indexes = []
        for source_locator in self.store.list_sources():
            try:
                index = self.store.read_evidence_locator_index_artifact(source_locator)
            except Exception:
                continue
            if index is not None:
                indexes.append(index)
        if not indexes:
            return None
        return indexes[-1]

    def _verified_lint_report(
        self, model_report: str, before: LintSnapshot, after: LintSnapshot
    ) -> str:
        return (
            "## Model report\n\n"
            f"{model_report.strip() or 'No model report.'}\n\n"
            "## Deterministic verification\n\n"
            "### Delta\n\n"
            f"{LintDelta(before, after).render()}\n\n"
            "### Before model pass\n\n"
            f"{before.render()}\n\n"
            "### After model pass\n\n"
            f"{after.render()}"
        )

    async def _run(
        self,
        workflow: Any,
        message: str,
        op: str,
        tag: str = "",
        initial_messages: list[Message] | None = None,
    ) -> tuple[str, Path | None]:
        writer = (
            TranscriptWriter(self.runs_dir / f"{self.run_id or self.today}-{tag or op}.jsonl")
            if self.runs_dir is not None
            else None
        )
        runner = WorkflowRunner(
            client=self.client,
            context_manager=self.context_manager,
            max_iterations=_MAX_ITERATIONS[op],
            max_tool_errors=_MAX_TOOL_ERRORS.get(op, 2),
            on_message=writer.on_message if writer else None,
            retry_nudge=_RETRY_NUDGES[op],
        )
        try:
            result = await runner.run(
                workflow,
                message,
                prompt_vars={"schema": self.store.read_schema()},
                initial_messages=initial_messages,
            )
        finally:
            if writer:
                writer.close()
        return str(result), writer.path if writer else None

    def _file_lint_report(self, report: str) -> None:
        self.store.write_page(
            WikiPage(
                page_metadata=PageMetadata(
                    page_id=HEALTH_PAGE,
                    page_kind="synthesis",
                    summary=f"Wiki health report from the latest lint pass ({self.today}).",
                    updated=self.today,
                ),
                page_body=report,
            )
        )

    def _contradiction_report(
        self,
        selection: ContradictionSelection,
        findings: tuple[ContradictionFinding, ...],
        model_report: str,
    ) -> str:
        return ContradictionAuditReport(
            selection=selection,
            findings=findings,
            model_report=model_report,
        ).render()

    def _file_contradiction_report(self, report: str) -> None:
        self.store.write_page(
            WikiPage(
                page_metadata=PageMetadata(
                    page_id=CONTRADICTIONS_PAGE,
                    page_kind="synthesis",
                    summary=f"Contradiction audit report from {self.today}.",
                    updated=self.today,
                ),
                page_body=report,
            )
        )

    def _grounding_report(
        self,
        selection: GroundingSelection,
        verdicts: tuple[GroundingVerdict, ...],
        model_report: str,
    ) -> str:
        return GroundingAuditReport(
            selection=selection,
            verdicts=verdicts,
            model_report=model_report,
        ).render()

    def _file_grounding_report(self, report: str) -> None:
        self.store.write_page(
            WikiPage(
                page_metadata=PageMetadata(
                    page_id=GROUNDING_PAGE,
                    page_kind="synthesis",
                    summary=f"Grounding audit report from {self.today}.",
                    updated=self.today,
                ),
                page_body=report,
            )
        )

    def _claim_support_audit_report(
        self,
        selection: ClaimSupportSelection,
        verdicts: tuple[ClaimSupportVerdict, ...],
        model_report: str,
    ) -> ClaimSupportAuditReport:
        return ClaimSupportAuditReport(
            run_id=self.run_id or self.today,
            selection=selection,
            verdicts=verdicts,
            model_report=model_report,
        )

    def _file_claim_support_report(self, report: str) -> None:
        self.store.write_page(
            WikiPage(
                page_metadata=PageMetadata(
                    page_id=CLAIM_SUPPORT_PAGE,
                    page_kind="synthesis",
                    summary=f"Claim support audit report from {self.today}.",
                    updated=self.today,
                ),
                page_body=report,
            )
        )

    def _semantic_lint_report(
        self,
        selection: SemanticLintSelection,
        findings: tuple[SemanticFinding, ...],
        model_report: str,
    ) -> str:
        return SemanticLintReport(
            selection=selection,
            findings=findings,
            model_report=model_report,
        ).render()

    def _file_semantic_lint_report(self, report: str) -> None:
        self.store.write_page(
            WikiPage(
                page_metadata=PageMetadata(
                    page_id=SEMANTIC_LINT_PAGE,
                    page_kind="synthesis",
                    summary=f"Semantic lint report from {self.today}.",
                    updated=self.today,
                ),
                page_body=report,
            )
        )


def _broken_link_edges(findings: LintRun) -> set[tuple[str, str]]:
    return {(page, target) for page, targets in findings.broken_links.items() for target in targets}


def _single_source_locator(ingest_run: IngestRun) -> str:
    return _single_raw_source(ingest_run).source_locator


def _expected_page_plan_writes(page_plan: PagePlan) -> tuple[str, ...]:
    return tuple(
        write.page_metadata.page_id
        for write in page_plan.planned_writes
        if write.action in {"create-new", "enrich-existing"}
    )


def _single_raw_source(ingest_run: IngestRun) -> RawSource:
    return ingest_run.source_bundle.raw_sources[0]


def _chunks_from_page_plan(page_plan: PagePlan) -> tuple[ChunkText, ...]:
    return tuple(
        ChunkText(unit.unit_id, unit.locator, unit.heading_path, unit.text)
        for unit in page_plan.extracted_units
    )


def _page_plan_sources_match_source(page_plan: PagePlan, source_locator: str) -> bool:
    source_locators = tuple(source.source_locator for source in page_plan.source_bundle.raw_sources)
    return source_locators == (source_locator,)


def _manifest_has_progress(manifest: Manifest) -> bool:
    return any(record.status == "done" for record in manifest.chunks) or manifest.integrated


def _has_matching_technical_catalog(
    catalog: TechnicalAtomCatalog | None, page_plan_id: str, reuse_enabled: bool
) -> bool:
    return reuse_enabled and catalog is not None and catalog.artifact_fingerprint == page_plan_id


def _pdf_page_plan_matches_manifest(
    page_plan: PagePlan, source_locator: str, manifest: Manifest
) -> bool:
    if not page_plan.plan_id.endswith(f"-pdf-{slugify(Path(source_locator).stem)}"):
        return False
    if not _page_plan_sources_match_source(page_plan, source_locator):
        return False
    return _page_plan_unit_map(page_plan) == _manifest_unit_map(manifest)


def _pdf_page_plan_matches_cache_text(
    page_plan: PagePlan, manifest: Manifest, cache_dir: Path
) -> bool:
    units_by_id = {unit.unit_id: unit for unit in page_plan.extracted_units}
    for record in manifest.chunks:
        unit = units_by_id.get(f"unit-{record.chunk_id:04d}")
        if unit is None:
            return False
        chunk_path = chunk_file(cache_dir, record.chunk_id)
        if not chunk_path.is_file():
            return False
        if unit.text != chunk_path.read_text(encoding="utf-8"):
            return False
    return True


def _page_plan_unit_map(page_plan: PagePlan) -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (unit.unit_id, unit.locator, unit.heading_path) for unit in page_plan.extracted_units
    )


def _manifest_unit_map(manifest: Manifest) -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (f"unit-{record.chunk_id:04d}", f"p.{record.start_page}-{record.end_page}", record.heading)
        for record in manifest.chunks
    )


def _source_plan_for(ingest_run: IngestRun, raw_source: RawSource) -> SourcePlan | None:
    for source_plan in ingest_run.source_plans:
        if source_plan.raw_source == raw_source:
            return source_plan
    return None


def _page_plan_targets_for_chunk(
    page_plan: PagePlan, chunk_id: int, hub_page_id: str
) -> tuple[str, ...]:
    unit_id = f"unit-{chunk_id:04d}"
    return tuple(
        write.page_metadata.page_id
        for write in page_plan.planned_writes
        if write.action != "defer"
        and write.page_metadata.page_id != hub_page_id
        and unit_id in write.extracted_units
    )


def _pending_pdf_work_units(
    page_plan: PagePlan,
    pending_records: tuple[ChunkRecord, ...],
) -> tuple[tuple[ChunkRecord, ...], ...]:
    if not page_plan.source_page_groups:
        return tuple((record,) for record in pending_records)
    records_by_unit = {f"unit-{record.chunk_id:04d}": record for record in pending_records}
    groups_by_first_chunk: dict[int, tuple[ChunkRecord, ...]] = {}
    covered: set[int] = set()
    for group in page_plan.source_page_groups:
        records = tuple(
            records_by_unit[unit_id]
            for unit_id in group.extracted_units
            if unit_id in records_by_unit
        )
        if records:
            groups_by_first_chunk[records[0].chunk_id] = records
    work_units: list[tuple[ChunkRecord, ...]] = []
    for record in pending_records:
        if record.chunk_id in covered:
            continue
        records = groups_by_first_chunk.get(record.chunk_id, (record,))
        work_units.append(records)
        covered.update(item.chunk_id for item in records)
    return tuple(work_units)


def _work_unit_targets(
    page_plan: PagePlan, records: tuple[ChunkRecord, ...], hub_page_id: str
) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            page_id
            for record in records
            for page_id in _page_plan_targets_for_chunk(page_plan, record.chunk_id, hub_page_id)
        )
    )


def _work_unit_write_ids(
    page_plan: PagePlan, records: tuple[ChunkRecord, ...], hub_page_id: str
) -> tuple[str, ...]:
    unit_ids = {f"unit-{record.chunk_id:04d}" for record in records}
    return tuple(
        write.write_id
        for write in page_plan.planned_writes
        if write.action != "defer"
        and write.page_metadata.page_id != hub_page_id
        and unit_ids.intersection(write.extracted_units)
    )


def _work_unit_chunk_text(cache_dir: Path, records: tuple[ChunkRecord, ...]) -> str:
    chunks: list[str] = []
    for record in records:
        text = chunk_file(cache_dir, record.chunk_id).read_text(encoding="utf-8")
        chunks.append(
            f"## {record.heading} (pages {record.start_page}-{record.end_page})\n\n{text}"
        )
    return "\n\n".join(chunks)


def _work_unit_name(records: tuple[ChunkRecord, ...]) -> str:
    if len(records) == 1:
        return f"chunk {records[0].chunk_id}"
    return f"chunk group {records[0].chunk_id}-{records[-1].chunk_id}"


def _claim_support_batches(
    candidates: Sequence[ClaimSupportCandidate],
) -> tuple[tuple[ClaimSupportCandidate, ...], ...]:
    return tuple(
        tuple(candidates[start : start + _CLAIM_SUPPORT_BATCH_SIZE])
        for start in range(0, len(candidates), _CLAIM_SUPPORT_BATCH_SIZE)
    )


def _claim_support_batch_selection(
    selection: ClaimSupportSelection,
    candidates: tuple[ClaimSupportCandidate, ...],
) -> ClaimSupportSelection:
    return replace(
        selection,
        candidates=candidates,
        blocked_candidates=(),
        deterministic_findings=(),
        candidate_count=len(candidates),
        max_claims=len(candidates),
        sample_coverage=None,
    )


def _claim_support_audit_message(
    *,
    batch_selection: ClaimSupportSelection,
    total_selected: int,
    batch_index: int,
    batch_count: int,
) -> str:
    return (
        "Run a claim-support audit over this bounded candidate batch. "
        "For every candidate in this batch, decide whether the EvidenceRecord "
        "excerpts support the generated wiki claim as written. Record exactly "
        "one record_claim_support_verdict tool call for each candidate before "
        "calling finish_claim_support. The finish_claim_support report should "
        "give qualitative uncertainty and curator next steps only; do not "
        "restate verdict counts or skipped-candidate counts.\n\n"
        f"Batch: {batch_index}/{batch_count}\n"
        f"Selected for model judgment in full sample: {total_selected}\n"
        f"Selected for model judgment in this batch: {batch_selection.selected_count}\n\n"
        f"{batch_selection.render_for_prompt()}"
    )


def _work_unit_section_label(records: tuple[ChunkRecord, ...]) -> str:
    if len(records) == 1:
        record = records[0]
        return f"{record.heading} (pages {record.start_page}-{record.end_page})"
    return (
        f"{records[0].heading} through {records[-1].heading} "
        f"(pages {records[0].start_page}-{records[-1].end_page})"
    )


def _work_unit_citation_guidance(source_locator: str, records: tuple[ChunkRecord, ...]) -> str:
    if len(records) == 1:
        record = records[0]
        return (
            f"Cite this material as (raw/{source_locator} p.{record.start_page}-{record.end_page})."
        )
    citations = ", ".join(
        f"(raw/{source_locator} p.{record.start_page}-{record.end_page})" for record in records
    )
    return f"Cite grouped claims with their matching page locator: {citations}."


def _targetless_work_unit_notes(records: tuple[ChunkRecord, ...]) -> str:
    return (
        "No page write was planned for this PDF chunk because deterministic "
        "analysis found no claim-bearing source-page material."
    )


def _targetless_work_unit_gap_summary(records: tuple[ChunkRecord, ...]) -> str:
    label = _work_unit_section_label(records)
    return f"{label}: no claim-bearing source-page material."


def _required_hub_page_map(
    page_plan: PagePlan, manifest: Manifest, hub_page_id: str
) -> tuple[tuple[str, ...], tuple[tuple[str, str], ...]]:
    if page_plan.source_page_groups:
        group_link_targets: list[str] = []
        group_page_map_entries: list[tuple[str, str]] = []
        seen_group_targets: set[str] = set()
        for group in page_plan.source_page_groups:
            if group.page_id == hub_page_id or group.page_id in seen_group_targets:
                continue
            group_link_targets.append(group.page_id)
            group_page_map_entries.append((group.page_id, source_page_group_label(group)))
            seen_group_targets.add(group.page_id)
        return tuple(group_link_targets), tuple(group_page_map_entries)
    link_targets: list[str] = []
    page_map_entries: list[tuple[str, str]] = []
    seen_targets: set[str] = set()
    for chunk in manifest.chunks:
        for page in chunk.pages_written:
            if page != hub_page_id and page not in seen_targets:
                link_targets.append(page)
                page_map_entries.append((page, chunk.heading))
                seen_targets.add(page)
    return tuple(link_targets), tuple(page_map_entries)


def _render_count_delta(label: str, before: int, after: int) -> str:
    return f"{label}: {before} -> {after}"


def _render_name_delta(label: str, names: list[str]) -> str:
    if not names:
        return f"{label}: None."
    return label + ":\n" + "\n".join(f"- {name}" for name in names)
