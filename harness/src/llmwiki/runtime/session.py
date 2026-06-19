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
from llmwiki.domain.chatwindow import QAPair
from llmwiki.domain.contradictions import (
    ContradictionAuditReport,
    ContradictionFinding,
    ContradictionSelection,
)
from llmwiki.domain.evidence import EvidenceLintReport, EvidencePolicy
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
from llmwiki.domain.links import LintFindings, compute_findings
from llmwiki.domain.pages import PageMetadata, WikiPage, parse_page, slugify
from llmwiki.domain.salience import SalienceReport, compute_salience, reconcile_key_lists
from llmwiki.domain.semantic_lint import (
    SemanticFinding,
    SemanticLintReport,
    SemanticLintSelection,
)
from llmwiki.domain.system_pages import (
    CONTRADICTIONS_PAGE,
    GROUNDING_PAGE,
    HEALTH_PAGE,
    ORPHAN_EXEMPT_PAGES,
    SEMANTIC_LINT_PAGE,
)
from llmwiki.pdf import PdfError
from llmwiki.pdf.pipeline import (
    ExtractionResult,
    chunk_file,
    read_source_text,
    save_manifest,
)
from llmwiki.runtime.transcript import TranscriptWriter
from llmwiki.store import WikiStore
from llmwiki.workflows import (
    build_chat_file_workflow,
    build_chat_workflow,
    build_contradiction_workflow,
    build_grounding_workflow,
    build_ingest_workflow,
    build_lint_workflow,
    build_query_workflow,
    build_semantic_lint_workflow,
)
from llmwiki.workflows.pdf_ingest import build_integrate_workflow, build_map_workflow

_MAX_ITERATIONS = {
    "ingest": 24,
    "query": 12,
    "lint": 24,
    "contradictions": 18,
    "grounding": 18,
    "semantic-lint": 18,
    "pdf-chunk": 24,
    "pdf-integrate": 20,
    "chat": 12,
    "chat-file": 14,
}

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
    "chat": ("Reply with exactly one tool call. Use respond to deliver your answer to the user."),
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

    link_findings: LintFindings
    evidence_report: EvidenceLintReport

    def render(self) -> str:
        return (
            "Link/index/orphan findings:\n"
            f"{self.link_findings.render()}\n\n"
            "Citation evidence findings:\n"
            f"{self.evidence_report.render()}"
        )


@dataclass(frozen=True)
class LintDelta:
    """Deterministic before/after change summary for a lint operation."""

    before: LintSnapshot
    after: LintSnapshot

    def render(self) -> str:
        before_orphans = set(self.before.link_findings.orphan_pages)
        after_orphans = set(self.after.link_findings.orphan_pages)
        before_broken = _broken_link_edges(self.before.link_findings)
        after_broken = _broken_link_edges(self.after.link_findings)
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
                    len(self.before.link_findings.missing_from_index),
                    len(self.after.link_findings.missing_from_index),
                ),
                _render_count_delta(
                    "Stale index entries",
                    len(self.before.link_findings.stale_index_entries),
                    len(self.after.link_findings.stale_index_entries),
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
        self, source_path: str, reextract: bool = False, reintegrate: bool = False
    ) -> OperationResult:
        if source_path.lower().endswith(".pdf"):
            return await self._ingest_pdf(source_path, reextract, reintegrate)
        if reintegrate:
            raise PdfError("--reintegrate applies to chunked (PDF) sources only.")
        ingest_route_plan_state = self._ingest_route_plan_state(source_path, "source")
        write_log: list[str] = []
        workflow = build_ingest_workflow(
            self.store,
            self.today,
            self._evidence_policy(),
            profiles=self.ingest_profiles,
            source_path=source_path,
            new_page_prefix=required_new_page_prefix(self.ingest_profiles, source_path),
            write_log=write_log,
            ingest_route_plan_state=ingest_route_plan_state,
        )
        message = (
            f"Ingest the source 'raw/{source_path}' into the wiki. "
            f"Pass path='{source_path}' to read_source."
        )
        report, transcript = await self._run(workflow, message, "ingest")
        self._record_ingest_route_plan(
            ingest_route_plan_state,
            page_writes=tuple(dict.fromkeys(write_log)),
        )
        self.store.append_log(self.today, "ingest", source_path, report)
        return OperationResult("ingest", source_path, report, transcript)

    async def _ingest_pdf(
        self, source_path: str, reextract: bool, reintegrate: bool = False
    ) -> OperationResult:
        if self.extract_pdf is None:
            raise RuntimeError("Session has no PDF extractor wired (extract_pdf).")
        result = self.extract_pdf(self.store.source_path(source_path), source_path, reextract)
        manifest, total = result.manifest, len(result.manifest.chunks)
        if reintegrate and manifest.pending:
            raise PdfError(
                f"--reintegrate requires a completed ingest; raw/{source_path} "
                f"has {len(manifest.pending)} pending chunk(s) — run a plain "
                "ingest to finish them first."
            )

        for record in manifest.pending:
            text = chunk_file(result.cache_dir, record.chunk_id).read_text(encoding="utf-8")
            ingest_route_plan_state = self._ingest_route_plan_state(
                source_path,
                "pdf-chunk",
                chunk_id=record.chunk_id,
            )
            message = (
                f"Ingest chunk {record.chunk_id} of {total} from 'raw/{source_path}'.\n"
                f"Section: {record.heading} (pages {record.start_page}-{record.end_page}).\n"
                f"Cite this material as (raw/{source_path} "
                f"p.{record.start_page}-{record.end_page}).\n\n<chunk>\n{text}\n</chunk>"
            )
            write_log: list[str] = []
            notes, _ = await self._run(
                build_map_workflow(
                    self.store,
                    self.today,
                    write_log=write_log,
                    evidence_policy=self._evidence_policy(),
                    profiles=self.ingest_profiles,
                    source_path=source_path,
                    new_page_prefix=required_new_page_prefix(self.ingest_profiles, source_path),
                    chunk_id=record.chunk_id,
                    ingest_route_plan_state=ingest_route_plan_state,
                ),
                message,
                "pdf-chunk",
                tag=f"pdf-chunk-{record.chunk_id:04d}",
            )
            route_summary = ingest_route_plan_state.summary()
            manifest = manifest.mark_done(
                record.chunk_id,
                notes,
                pages_written=tuple(dict.fromkeys(write_log)),
                route_plan_pages=route_summary.planned_page_count,
                route_plan_gaps=route_summary.route_gap_count,
                route_gap_summaries=route_summary.route_gap_summaries,
            )
            save_manifest(ExtractionResult(manifest=manifest, cache_dir=result.cache_dir))
            if self.on_chunk_note is not None:
                self.on_chunk_note(f"[chunk {record.chunk_id}/{total}] {notes}")

        hub = slugify(Path(source_path).stem)
        salience = compute_salience(
            self.store.page_texts(),
            manifest.write_counts(),
            source_text=read_source_text(result.cache_dir),
            scope_source=source_path,
            exclude_inbound_from=frozenset({hub}),
        )
        salience_block = salience.render()
        message = (
            f"All {total} chunks of 'raw/{source_path}' are ingested. Ensure the hub "
            f"source page '{hub}' exists and links the pages written during "
            f"chunking.\n\n{salience_block}\n\n"
            f"Machine-recorded chunk page map:\n\n<page-map>\n{manifest.page_map()}\n</page-map>"
        )
        link_targets: list[str] = []
        seen_targets: set[str] = set()
        for chunk in manifest.chunks:
            for page in chunk.pages_written:
                if page != hub and page not in seen_targets:
                    link_targets.append(page)
                    seen_targets.add(page)
        required_link_targets = tuple(link_targets)
        ingest_route_plan_state = self._ingest_route_plan_state(source_path, "pdf-integrate")
        report, transcript = await self._run(
            build_integrate_workflow(
                self.store,
                self.today,
                self._evidence_policy(),
                profiles=self.ingest_profiles,
                source_path=source_path,
                new_page_prefix=required_new_page_prefix(self.ingest_profiles, source_path),
                required_link_targets=required_link_targets,
                min_required_links=min(12, len(required_link_targets)),
                ingest_route_plan_state=ingest_route_plan_state,
            ),
            message,
            "pdf-integrate",
            tag="pdf-integrate",
        )
        self._reconcile_hub_key_lists(hub, salience)
        save_manifest(
            ExtractionResult(manifest=manifest.mark_integrated(), cache_dir=result.cache_dir)
        )
        self.store.append_log(self.today, "ingest", source_path, report)
        return OperationResult("ingest", source_path, report, transcript)

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
        source_path: str,
        scope: IngestRoutePlanScope,
        *,
        chunk_id: int | None = None,
    ) -> IngestRoutePlanState:
        return IngestRoutePlanState(
            IngestRouteContext(
                source_path=source_path,
                scope=scope,
                profile_ids=tuple(profile.id for profile in self.ingest_profiles),
                chunk_id=chunk_id,
                existing_pages=frozenset(self.store.list_pages()),
                new_page_prefix=required_new_page_prefix(self.ingest_profiles, source_path),
                prevent_singular_plural_siblings=prevents_singular_plural_siblings(
                    self.ingest_profiles
                ),
            )
        )

    def _reconcile_hub_key_lists(self, hub: str, salience: SalienceReport) -> None:
        """Harness-owned bookkeeping: the hub's key-lists mirror the salience
        report by construction (same contract as index.md entries)."""
        if hub not in self.store.list_pages():
            return  # no hub page; lint's findings will surface it
        page = parse_page(self.store.read_page(hub))
        body = reconcile_key_lists(page.page_body, salience)
        if body != page.page_body:
            metadata = replace(page.page_metadata, updated=self.today)
            self.store.write_page(WikiPage.from_metadata(metadata, body))

    async def query(self, question: str) -> OperationResult:
        workflow = build_query_workflow(self.store, self.today, self._evidence_policy())
        # Factual lookups don't benefit from Qwen3's thinking preamble.
        answer, transcript = await self._run(workflow, question + " /no_think", "query")
        self.store.append_log(self.today, "query", question, answer)
        return OperationResult("query", question, answer, transcript)

    async def chat_turn(
        self, question: str, window: Sequence[QAPair], grounded: bool, tag: str
    ) -> tuple[str, Path | None]:
        """One read-only conversation turn, seeded with windowed Q/A pairs.

        The seed carries question/answer text only — prior tool calls and
        page contents are never replayed; evidence is re-fetched on demand.
        *grounded* (a conversation's first turn) provisions the wiki index
        with the question, so the opening answer starts from the catalog
        and drills into pages — grounding by provisioning, not enforcement.
        """
        workflow = build_chat_workflow(self.store)
        rendered = workflow.build_system_prompt(schema=self.store.read_schema())
        seed = [Message(MessageRole.SYSTEM, rendered, MessageMeta(MessageType.SYSTEM_PROMPT))]
        for pair in window:
            seed.append(
                Message(MessageRole.USER, pair.question, MessageMeta(MessageType.USER_INPUT))
            )
            seed.append(
                Message(MessageRole.ASSISTANT, pair.answer, MessageMeta(MessageType.TEXT_RESPONSE))
            )
        message = question + " /no_think"
        if grounded:
            message = (
                "The wiki's index — the catalog of every page:\n\n"
                f"{self.store.read_index()}\n\n"
                f"Question: {message}"
            )
        seed.append(Message(MessageRole.USER, message, MessageMeta(MessageType.USER_INPUT)))
        return await self._run(workflow, message, "chat", tag=tag, initial_messages=seed)

    async def file_chat_synthesis(
        self,
        page_name: str,
        question: str,
        answer: str,
        scope: str = "",
        tag: str = "chat-file",
    ) -> OperationResult:
        workflow = build_chat_file_workflow(self.store, self.today)
        slug = slugify(page_name)
        message = (
            f"File a durable synthesis page named '{slug}' from the latest chat turn. "
            "Use category='synthesis'. Chat text is context only; re-read current "
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
            f"{before.link_findings.render()}\n\n"
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
            link_findings=compute_findings(
                page_texts,
                self.store.index_names(),
                exempt_from_orphans=ORPHAN_EXEMPT_PAGES,
            ),
            evidence_report=evidence_policy.lint_pages(
                page_texts,
                inventory,
                self.store.source_resolver() if evidence_policy.enabled else None,
            ),
        )

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


def _broken_link_edges(findings: LintFindings) -> set[tuple[str, str]]:
    return {(page, target) for page, targets in findings.broken_links.items() for target in targets}


def _render_count_delta(label: str, before: int, after: int) -> str:
    return f"{label}: {before} -> {after}"


def _render_name_delta(label: str, names: list[str]) -> str:
    if not names:
        return f"{label}: None."
    return label + ":\n" + "\n".join(f"- {name}" for name in names)
