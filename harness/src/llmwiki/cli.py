"""llmwiki CLI: ingest, query, lint.

Thin entry point — parses arguments, boots the backend, delegates to a
Session, prints the result. All wiki logic lives in domain/store/workflows.
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

from forge.context import ContextManager, NoCompact

from llmwiki.config import (
    VALID_STRICT_EVIDENCE_MODES,
    ConfigError,
    StrictEvidenceMode,
    WikiPaths,
    load_backend_config,
    resolve_strict_evidence_mode,
)
from llmwiki.domain.candidates import (
    reject_candidate,
    signals_from_broken_links,
    update_candidate_backlog,
)
from llmwiki.domain.claim_support import DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS
from llmwiki.domain.claim_support_selection import select_claim_support_candidates
from llmwiki.domain.contradictions import DEFAULT_MAX_PAIRS, select_contradiction_candidates
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.graph import build_wiki_graph, graph_status
from llmwiki.domain.grounding import DEFAULT_MAX_CLAIMS, select_grounding_claims
from llmwiki.domain.index import index_page_ids
from llmwiki.domain.ingest_confidence import IngestConfidenceGate, ValidationFinding
from llmwiki.domain.ingest_profiles import (
    IngestProfile,
    load_ingest_profiles,
    profile_summary,
    render_profiles,
    select_ingest_profiles,
)
from llmwiki.domain.ingest_route_history import ingest_route_plan_records_from_jsonl
from llmwiki.domain.links import compute_findings
from llmwiki.domain.maintenance import RoutePlanStatus, build_curator_status, recent_log_entries
from llmwiki.domain.pages import PageMetadata, WikiPage, parse_page
from llmwiki.domain.salience import compute_salience
from llmwiki.domain.semantic_lint import DEFAULT_MAX_ITEMS, select_semantic_lint_candidates
from llmwiki.domain.system_pages import (
    CLAIM_SUPPORT_PAGE,
    CURATOR_STATUS_PAGE,
    INGEST_CONFIDENCE_PAGE,
    ORPHAN_EXEMPT_PAGES,
    SEMANTIC_LINT_PAGE,
)
from llmwiki.pdf import PdfError
from llmwiki.runtime.backend import start_backend
from llmwiki.runtime.chat_repl import ChatRepl
from llmwiki.runtime.ingest_confidence import (
    claim_support_gate_from_audit,
    file_ingest_confidence_report,
    render_ingest_confidence_report,
    skipped_claim_support_gate,
)
from llmwiki.runtime.ingest_confidence_artifacts import prepare_ingest_confidence_artifacts
from llmwiki.runtime.ingest_confidence_gates import (
    DeterministicConfidence,
    deterministic_confidence,
)
from llmwiki.runtime.session import ExtractFn, OperationResult, Session
from llmwiki.store import WikiStore
from llmwiki.store.chat_store import ChatStore

if TYPE_CHECKING:
    from llmwiki.pdf.pipeline import ExtractionResult
    from llmwiki.pdf.recognizer import TextRecognizer


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="llmwiki",
        description="LLM-maintained local wiki (Ollama via forge).",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Project root containing raw/, wiki/, SCHEMA.md (default: cwd).",
    )
    parser.add_argument(
        "--runtime",
        help="Runtime profile: ollama-default or local-4090 "
        "(default: LLMWIKI_RUNTIME or ollama-default).",
    )
    sub = parser.add_subparsers(dest="op", required=True)

    ingest = sub.add_parser("ingest", help="Integrate one raw source into the wiki.")
    _add_strict_evidence_arg(ingest)
    ingest.add_argument("source", help="Source path relative to raw/, e.g. article.md")
    ingest.add_argument(
        "--profile",
        action="append",
        default=[],
        help="Ingest profile id from profiles/ingest/*.toml. Repeat to compose profiles.",
    )
    ingest.add_argument(
        "--reextract",
        action="store_true",
        help="PDF only: discard the cached extraction/manifest and start over "
        "(default resumes a partial ingest).",
    )
    ingest.add_argument(
        "--reintegrate",
        action="store_true",
        help="PDF only: rerun just the integrate pass of a completed ingest "
        "(rebuilds the hub with current salience).",
    )

    query = sub.add_parser("query", help="Answer a question from the wiki.")
    _add_strict_evidence_arg(query)
    query.add_argument("question", help="The question to answer.")

    lint = sub.add_parser("lint", help="Health-check the wiki.")
    _add_strict_evidence_arg(lint)

    curator_status = sub.add_parser(
        "curator-status",
        help="Print deterministic wiki maintenance status without starting a model.",
    )
    _add_strict_evidence_arg(curator_status)

    maintenance = sub.add_parser(
        "maintenance",
        help="File deterministic curator status and append a maintenance log entry.",
    )
    _add_strict_evidence_arg(maintenance)

    candidates = sub.add_parser(
        "candidates",
        help="List or update the harness-owned candidate page backlog.",
    )
    candidate_sub = candidates.add_subparsers(dest="candidate_op")
    candidate_sub.add_parser("list", help="List active candidate pages.")
    reject = candidate_sub.add_parser("reject", help="Reject a candidate page slug.")
    reject.add_argument("slug", help="Candidate slug to reject.")
    reject.add_argument(
        "--reason",
        required=True,
        help="Why this candidate should not be promoted.",
    )

    contradictions = sub.add_parser(
        "contradictions",
        help="Audit bounded candidate page pairs for semantic contradictions.",
    )
    contradictions.add_argument(
        "--max-pairs",
        type=int,
        default=DEFAULT_MAX_PAIRS,
        help=f"Maximum candidate pairs to audit (default: {DEFAULT_MAX_PAIRS}).",
    )

    grounding = sub.add_parser(
        "grounding",
        help="Audit bounded wiki claims for support by cited evidence.",
    )
    grounding.add_argument(
        "--max-claims",
        type=int,
        default=DEFAULT_MAX_CLAIMS,
        help=f"Maximum claim candidates to judge (default: {DEFAULT_MAX_CLAIMS}).",
    )

    claim_support = sub.add_parser(
        "claim-support",
        help="Audit generated wiki claims against EvidenceRecord support.",
    )
    claim_support.add_argument(
        "--max-claims",
        type=int,
        default=DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS,
        help="Maximum claim-support candidates to judge "
        f"(default: {DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS}).",
    )
    claim_support.add_argument(
        "--source",
        default="",
        help="Limit candidates to one raw source, e.g. raw/book.pdf.",
    )

    ingest_confidence = sub.add_parser(
        "ingest-confidence",
        help="File a post-ingest confidence report for one raw source.",
    )
    ingest_confidence.add_argument("source", help="Source path relative to raw/, e.g. article.md")
    ingest_confidence.add_argument(
        "--fresh",
        action="store_true",
        help="Rebuild generated ingest artifacts before running confidence gates.",
    )
    ingest_confidence.add_argument(
        "--max-claims",
        type=int,
        default=DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS,
        help="Maximum claim-support candidates to judge "
        f"(default: {DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS}).",
    )
    ingest_confidence.add_argument(
        "--profile",
        action="append",
        default=[],
        help="Ingest profile id from profiles/ingest/*.toml. Repeat to compose profiles.",
    )

    semantic_lint = sub.add_parser(
        "semantic-lint",
        help="Audit bounded semantic leads for stale claims and data gaps.",
    )
    semantic_lint.add_argument(
        "--max-items",
        type=int,
        default=DEFAULT_MAX_ITEMS,
        help=f"Maximum semantic lint items to audit (default: {DEFAULT_MAX_ITEMS}).",
    )

    graph = sub.add_parser("graph", help="Write or check the deterministic wiki graph export.")
    graph.add_argument(
        "--check",
        action="store_true",
        help="Fail if wiki/wiki-graph.json is missing, invalid, or stale.",
    )

    pages = sub.add_parser(
        "pages",
        help="Deterministic page maintenance operations.",
    )
    page_sub = pages.add_subparsers(dest="page_op", required=True)
    rename = page_sub.add_parser("rename", help="Rename a page and rewrite inbound links.")
    rename.add_argument("old", help="Existing page slug.")
    rename.add_argument("new", help="New page slug.")
    rename.add_argument("--summary", help="Replacement index summary for the renamed page.")
    merge = page_sub.add_parser("merge", help="Merge an old page into an existing target page.")
    merge.add_argument("old", help="Existing page slug to remove.")
    merge.add_argument("target", help="Existing page slug to keep.")
    merge.add_argument("--summary", help="Replacement index summary for the target page.")
    delete = page_sub.add_parser("delete", help="Delete page(s) and remove index entries.")
    delete.add_argument("page", nargs="+", help="Existing page slug to delete.")
    relink = page_sub.add_parser(
        "relink",
        help="Replace one page's broken link target with an existing page target.",
    )
    relink.add_argument("page", help="Existing page containing the link.")
    relink.add_argument("old_target", help="Broken link target to replace.")
    relink.add_argument("new_target", help="Existing page target to link instead.")
    relink.add_argument("--alias", help="Alias label to use when the old link had none.")

    sub.add_parser(
        "profiles",
        help="List configured ingest profiles without starting a model.",
    )

    chat = sub.add_parser("chat", help="Converse with the wiki (model stays loaded).")
    _add_strict_evidence_arg(chat)
    chat.add_argument(
        "--resume",
        nargs="?",
        const="latest",
        default=None,
        metavar="SESSION_ID",
        help="Continue a conversation (default: the most recent one).",
    )
    return parser


def _add_strict_evidence_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--strict-evidence",
        choices=VALID_STRICT_EVIDENCE_MODES,
        help="Citation evidence validation: off, warn, or fail "
        "(default: LLMWIKI_STRICT_EVIDENCE or off).",
    )


def _pdf_extractor(paths: WikiPaths) -> ExtractFn:
    def extract(pdf_path: Path, source_rel: str, reextract: bool) -> ExtractionResult:
        from llmwiki.pdf.pipeline import ensure_extracted

        return ensure_extracted(
            pdf_path,
            source_rel,
            cache_root=paths.cache_dir,
            recognizer=_default_text_recognizer(),
            reextract=reextract,
        )

    return extract


def _default_text_recognizer() -> TextRecognizer:
    try:
        import Foundation  # noqa: F401
        import Vision  # noqa: F401
    except ImportError:
        from llmwiki.pdf.recognizer import NullRecognizer

        return NullRecognizer()
    from llmwiki.pdf.vision import AppleVisionRecognizer

    return AppleVisionRecognizer()


async def _run(args: argparse.Namespace) -> OperationResult:
    paths = WikiPaths(root=args.root.resolve())
    strict_evidence = resolve_strict_evidence_mode(getattr(args, "strict_evidence", None))

    now = datetime.now()
    if args.op == "profiles":
        return _run_profiles(paths)
    if args.op in {"curator-status", "maintenance"}:
        paths.validate_status()
        return _run_curator_operation(args.op, paths, strict_evidence, now.date().isoformat())
    if args.op == "candidates":
        paths.validate_status()
        return _run_candidates(args, paths, now.date().isoformat())
    if args.op == "graph":
        paths.validate_status()
        return _run_graph(args, paths, now.date().isoformat())
    if args.op == "pages":
        paths.validate_status()
        return _run_pages(args, paths, now.date().isoformat())

    if args.op == "contradictions":
        return await _run_contradictions(args, paths, now)
    if args.op == "grounding":
        return await _run_grounding(args, paths, now)
    if args.op == "claim-support":
        return await _run_claim_support(args, paths, now)
    if args.op == "ingest-confidence":
        return await _run_ingest_confidence(args, paths, now)
    if args.op == "semantic-lint":
        return await _run_semantic_lint(args, paths, now)

    paths.validate()
    ingest_profiles: tuple[IngestProfile, ...] = ()
    if args.op == "ingest":
        ingest_profiles = _select_profiles(paths, args.profile)
    backend_config = load_backend_config(args.runtime)
    backend = await start_backend(backend_config)
    try:
        print(f"[runtime: {backend.summary}]", file=sys.stderr)
        print(f"[strict-evidence: {strict_evidence}]", file=sys.stderr)
        if args.op == "ingest":
            print(f"[ingest-profiles: {profile_summary(ingest_profiles)}]", file=sys.stderr)
        store = WikiStore(paths)
        store.ensure_navigation_files()
        session = Session(
            store=store,
            client=backend.client,
            context_manager=backend.context_manager,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
            extract_pdf=_pdf_extractor(paths),
            on_chunk_note=lambda note: print(note, flush=True),
            strict_evidence=strict_evidence,
            ingest_profiles=ingest_profiles,
        )
        if args.op == "ingest":
            return await session.ingest(
                args.source, reextract=args.reextract, reintegrate=args.reintegrate
            )
        if args.op == "query":
            return await session.query(args.question)
        if args.op == "chat":
            return await _run_chat(session, paths, args.resume)
        return await session.lint()
    finally:
        await backend.aclose()


def _select_profiles(paths: WikiPaths, requested: list[str]) -> tuple[IngestProfile, ...]:
    available = load_ingest_profiles(paths.ingest_profiles_dir)
    return select_ingest_profiles(available, requested)


def _run_profiles(paths: WikiPaths) -> OperationResult:
    profiles = load_ingest_profiles(paths.ingest_profiles_dir)
    return OperationResult("profiles", "ingest profiles", render_profiles(profiles), None)


async def _run_contradictions(
    args: argparse.Namespace, paths: WikiPaths, now: datetime
) -> OperationResult:
    if args.max_pairs < 1:
        raise ConfigError("--max-pairs must be at least 1.")
    paths.validate()
    store = WikiStore(paths)
    selection = select_contradiction_candidates(store.page_texts(), max_pairs=args.max_pairs)
    if not selection.candidates:
        session = Session(
            store=store,
            client=None,
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
            today=now.date().isoformat(),
        )
        return await session.contradictions(selection)

    backend_config = load_backend_config(args.runtime)
    backend = await start_backend(backend_config)
    try:
        print(f"[runtime: {backend.summary}]", file=sys.stderr)
        session = Session(
            store=store,
            client=backend.client,
            context_manager=backend.context_manager,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
        )
        return await session.contradictions(selection)
    finally:
        await backend.aclose()


async def _run_grounding(
    args: argparse.Namespace, paths: WikiPaths, now: datetime
) -> OperationResult:
    if args.max_claims < 1:
        raise ConfigError("--max-claims must be at least 1.")
    paths.validate()
    store = WikiStore(paths)
    selection = select_grounding_claims(
        store.page_texts(),
        store.source_inventory(),
        store.source_resolver(),
        max_claims=args.max_claims,
    )
    if not selection.candidates:
        session = Session(
            store=store,
            client=None,
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
            today=now.date().isoformat(),
        )
        return await session.grounding(selection)

    backend_config = load_backend_config(args.runtime)
    backend = await start_backend(backend_config)
    try:
        print(f"[runtime: {backend.summary}]", file=sys.stderr)
        session = Session(
            store=store,
            client=backend.client,
            context_manager=backend.context_manager,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
        )
        return await session.grounding(selection)
    finally:
        await backend.aclose()


async def _run_claim_support(
    args: argparse.Namespace, paths: WikiPaths, now: datetime
) -> OperationResult:
    if args.max_claims < 1:
        raise ConfigError("--max-claims must be at least 1.")
    paths.validate()
    store = WikiStore(paths)
    source_locator = args.source.removeprefix("raw/") if args.source else None
    selection = select_claim_support_candidates(
        store.page_texts(),
        store.source_inventory(),
        _evidence_registries(store, source_locator),
        store.read_source_summary_draft_artifacts(source_locator),
        max_claims=args.max_claims,
        source=args.source,
    )
    if not selection.candidates:
        session = Session(
            store=store,
            client=None,
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
            today=now.date().isoformat(),
        )
        return await session.claim_support(selection)

    backend_config = load_backend_config(args.runtime)
    backend = await start_backend(backend_config)
    try:
        print(f"[runtime: {backend.summary}]", file=sys.stderr)
        session = Session(
            store=store,
            client=backend.client,
            context_manager=backend.context_manager,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
        )
        return await session.claim_support(selection)
    finally:
        await backend.aclose()


async def _run_ingest_confidence(
    args: argparse.Namespace, paths: WikiPaths, now: datetime
) -> OperationResult:
    if args.max_claims < 1:
        raise ConfigError("--max-claims must be at least 1.")
    paths.validate()
    source_locator = args.source.removeprefix("raw/")
    profiles = _select_profiles(paths, args.profile)
    today = now.date().isoformat()
    run_id = now.strftime("%Y-%m-%d-%H%M%S")
    store = WikiStore(paths)
    store.ensure_navigation_files()
    prepared = prepare_ingest_confidence_artifacts(
        store=store,
        cache_dir=paths.cache_dir,
        source_locator=source_locator,
        today=today,
        profiles=profiles,
        fresh=args.fresh,
        extract_pdf=_pdf_extractor(paths),
    )
    deterministic = deterministic_confidence(
        store=store,
        source_locator=source_locator,
        today=today,
        prepared=prepared,
        max_claims=args.max_claims,
    )
    claim_gate, claim_findings, transcript = await _confidence_claim_support_gate(
        args, paths, store, now, source_locator, deterministic
    )
    report = render_ingest_confidence_report(
        run_id=run_id,
        source_locator=source_locator,
        prepared=prepared,
        deterministic=deterministic,
        claim_support_gate=claim_gate,
        claim_support_findings=claim_findings,
    )
    file_ingest_confidence_report(store, report, today)
    rendered = report.render()
    store.append_log(today, "ingest-confidence", source_locator, rendered)
    return OperationResult("ingest-confidence", source_locator, rendered, transcript)


async def _confidence_claim_support_gate(
    args: argparse.Namespace,
    paths: WikiPaths,
    store: WikiStore,
    now: datetime,
    source_locator: str,
    deterministic: DeterministicConfidence,
) -> tuple[IngestConfidenceGate, tuple[ValidationFinding, ...], Path | None]:
    if deterministic.has_blockers:
        gate, findings = skipped_claim_support_gate(
            source_locator, "Skipped because deterministic blockers exist."
        )
        return gate, findings, None
    selection = deterministic.claim_support_selection
    if selection is None:
        gate, findings = skipped_claim_support_gate(
            source_locator, "Skipped because no EvidenceRegistry is available."
        )
        return gate, findings, None
    if not selection.candidates:
        reason = "Skipped because no claim-support candidates with evidence excerpts were selected."
        gate, findings = skipped_claim_support_gate(source_locator, reason)
        return gate, findings, None
    backend_config = load_backend_config(args.runtime)
    backend = await start_backend(backend_config)
    try:
        print(f"[runtime: {backend.summary}]", file=sys.stderr)
        session = Session(
            store=store,
            client=backend.client,
            context_manager=backend.context_manager,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
        )
        audit, transcript = await session.claim_support_audit(selection)
        gate, findings = claim_support_gate_from_audit(source_locator, audit)
        return gate, findings, transcript
    finally:
        await backend.aclose()


async def _run_semantic_lint(
    args: argparse.Namespace, paths: WikiPaths, now: datetime
) -> OperationResult:
    if args.max_items < 1:
        raise ConfigError("--max-items must be at least 1.")
    paths.validate()
    store = WikiStore(paths)
    selection = select_semantic_lint_candidates(
        store.page_texts(),
        store.read_candidate_backlog(),
        max_items=args.max_items,
    )
    if not selection.candidates:
        session = Session(
            store=store,
            client=None,
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
            today=now.date().isoformat(),
        )
        return await session.semantic_lint(selection)

    backend_config = load_backend_config(args.runtime)
    backend = await start_backend(backend_config)
    try:
        print(f"[runtime: {backend.summary}]", file=sys.stderr)
        session = Session(
            store=store,
            client=backend.client,
            context_manager=backend.context_manager,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
        )
        return await session.semantic_lint(selection)
    finally:
        await backend.aclose()


def _run_curator_operation(
    op: str, paths: WikiPaths, strict_evidence: StrictEvidenceMode, today: str
) -> OperationResult:
    store = WikiStore(paths)
    if op == "maintenance":
        report = _curator_report(store, paths, strict_evidence, update_candidates=True, today=today)
        store.ensure_navigation_files()
        store.write_page(
            WikiPage(
                page_metadata=PageMetadata(
                    page_id=CURATOR_STATUS_PAGE,
                    page_kind="synthesis",
                    summary=f"Deterministic curator status from {today}.",
                    updated=today,
                ),
                page_body=report,
            )
        )
        store.append_log(today, "maintenance", "curator status", report)
    else:
        report = _curator_report(store, paths, strict_evidence)
    return OperationResult(op, "curator status", report, None)


def _curator_report(
    store: WikiStore,
    paths: WikiPaths,
    strict_evidence: StrictEvidenceMode,
    *,
    update_candidates: bool = False,
    today: str = "",
) -> str:
    page_texts = store.page_texts()
    index_exists = paths.index_path.is_file()
    log_exists = paths.log_path.is_file()
    index_text = paths.index_path.read_text(encoding="utf-8") if index_exists else ""
    log_text = paths.log_path.read_text(encoding="utf-8") if log_exists else ""
    lint_run = compute_findings(
        page_texts,
        index_page_ids(index_text),
        exempt_from_orphans=ORPHAN_EXEMPT_PAGES,
    )
    candidate_backlog = store.read_candidate_backlog()
    if update_candidates:
        candidate_backlog = update_candidate_backlog(
            candidate_backlog,
            signals_from_broken_links(lint_run.broken_links),
            existing_pages=set(page_texts),
            today=today,
        )
        store.write_candidate_backlog(candidate_backlog)
    evidence_policy = EvidencePolicy(mode=strict_evidence)
    inventory = store.source_inventory() if evidence_policy.enabled else None
    registry = _latest_evidence_registry(store) if evidence_policy.enabled else None
    locator_index = _latest_evidence_locator_index(store) if evidence_policy.enabled else None
    status = build_curator_status(
        page_texts=page_texts,
        index_page_ids=index_page_ids(index_text),
        raw_source_count=len(store.list_sources()),
        index_exists=index_exists,
        log_exists=log_exists,
        recent_log_entries=recent_log_entries(log_text),
        evidence_report=evidence_policy.lint_pages(
            page_texts,
            inventory,
            store.source_resolver() if evidence_policy.enabled else None,
            registry=registry,
            locator_index=locator_index,
        ),
        salience_report=compute_salience(page_texts),
        candidate_backlog=candidate_backlog,
        strict_evidence=strict_evidence,
        claim_support_summary=_claim_support_summary(store),
        semantic_lint_summary=_semantic_lint_summary(store),
        route_plan_status=_route_plan_status(paths),
        graph_status=graph_status(
            build_wiki_graph(page_texts, generated_date=today or "status-check"),
            store.read_graph_json(),
        ),
        lint_run=lint_run,
        ingest_confidence_summary=_ingest_confidence_summary(store),
    )
    return status.render()


def _route_plan_status(paths: WikiPaths) -> RoutePlanStatus:
    total_planned_pages = 0
    total_route_gaps = 0
    recent_route_gaps: list[str] = []
    if paths.route_plan_history_path.exists():
        records = ingest_route_plan_records_from_jsonl(
            paths.route_plan_history_path.read_text(encoding="utf-8")
        )
        for record in records:
            total_planned_pages += record.planned_page_count
            total_route_gaps += record.route_gap_count
            for summary in record.route_gap_summaries:
                recent_route_gaps.append(f"raw/{record.source_locator}: {summary}")
    for manifest_path in sorted(paths.cache_dir.glob("*/manifest.json")):
        from llmwiki.pdf.manifest import from_json as manifest_from_json

        manifest = manifest_from_json(manifest_path.read_text(encoding="utf-8"))
        for chunk in manifest.chunks:
            total_planned_pages += chunk.route_plan_pages
            total_route_gaps += chunk.route_plan_gaps
            for summary in chunk.route_gap_summaries:
                recent_route_gaps.append(f"raw/{manifest.source} chunk {chunk.chunk_id}: {summary}")
    return RoutePlanStatus(
        total_planned_pages=total_planned_pages,
        total_route_gaps=total_route_gaps,
        recent_route_gaps=tuple(recent_route_gaps[-5:]),
    )


def _latest_evidence_registry(store: WikiStore) -> EvidenceRegistry | None:
    registries = []
    for source_locator in store.list_sources():
        registry = store.read_evidence_registry_artifact(source_locator)
        if registry is not None:
            registries.append(registry)
    if not registries:
        return None
    return registries[-1]


def _latest_evidence_locator_index(store: WikiStore) -> EvidenceLocatorIndex | None:
    indexes = []
    for source_locator in store.list_sources():
        try:
            index = store.read_evidence_locator_index_artifact(source_locator)
        except Exception:
            continue
        if index is not None:
            indexes.append(index)
    if not indexes:
        return None
    return indexes[-1]


def _evidence_registries(
    store: WikiStore, source_locator: str | None = None
) -> tuple[EvidenceRegistry, ...]:
    locators = (source_locator,) if source_locator else store.list_sources()
    registries: list[EvidenceRegistry] = []
    for locator in locators:
        registry = store.read_evidence_registry_artifact(locator)
        if registry is not None:
            registries.append(registry)
    return tuple(registries)


def _claim_support_summary(store: WikiStore) -> str:
    return _system_report_summary(store, CLAIM_SUPPORT_PAGE)


def _semantic_lint_summary(store: WikiStore) -> str:
    return _system_report_summary(store, SEMANTIC_LINT_PAGE)


def _ingest_confidence_summary(store: WikiStore) -> str:
    return _system_report_summary(store, INGEST_CONFIDENCE_PAGE)


def _system_report_summary(store: WikiStore, page_id: str) -> str:
    if page_id not in store.list_pages():
        return ""
    text = parse_page(store.read_page(page_id)).page_body
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.startswith("---") and not line.startswith("#")
    ]
    return "\n".join(lines[:5])


def _run_graph(args: argparse.Namespace, paths: WikiPaths, today: str) -> OperationResult:
    store = WikiStore(paths)
    graph = build_wiki_graph(store.page_texts(), generated_date=today)
    status = graph_status(graph, store.read_graph_json())
    if args.check:
        if not status.is_current:
            raise ConfigError(status.render())
        return OperationResult("graph", "wiki graph", status.render(), None)
    store.write_graph_json(graph.to_json_text())
    store.ensure_navigation_files()
    status = graph_status(graph, store.read_graph_json())
    report = status.render()
    store.append_log(today, "graph", "wiki graph", report)
    return OperationResult("graph", "wiki graph", report, None)


def _run_pages(args: argparse.Namespace, paths: WikiPaths, today: str) -> OperationResult:
    store = WikiStore(paths)
    store.ensure_navigation_files()
    if args.page_op == "rename":
        store.rename_page(args.old, args.new, summary=args.summary, today=today)
        detail = f"Renamed [[{args.old}]] to [[{args.new}]] and rewrote inbound links."
        store.append_log(today, "pages", args.new, detail)
        return OperationResult("pages", args.new, detail, None)
    if args.page_op == "merge":
        store.merge_page(args.old, args.target, summary=args.summary, today=today)
        detail = f"Merged [[{args.old}]] into [[{args.target}]] and rewrote inbound links."
        store.append_log(today, "pages", args.target, detail)
        return OperationResult("pages", args.target, detail, None)
    if args.page_op == "delete":
        for page in args.page:
            store.delete_page(page)
        pages = ", ".join(f"[[{page}]]" for page in args.page)
        detail = f"Deleted {pages} and removed their index entries."
        subject = ", ".join(args.page)
        store.append_log(today, "pages", subject, detail)
        return OperationResult("pages", subject, detail, None)
    if args.page_op == "relink":
        store.replace_page_link(
            args.page,
            args.old_target,
            args.new_target,
            alias=args.alias,
            today=today,
        )
        detail = f"Replaced [[{args.old_target}]] with [[{args.new_target}]] in [[{args.page}]]."
        store.append_log(today, "pages", args.page, detail)
        return OperationResult("pages", args.page, detail, None)
    raise ConfigError(f"Unknown pages operation {args.page_op!r}.")


def _run_candidates(args: argparse.Namespace, paths: WikiPaths, today: str) -> OperationResult:
    store = WikiStore(paths)
    backlog = store.read_candidate_backlog()
    op = args.candidate_op or "list"
    if op == "reject":
        slug = str(args.slug)
        backlog = reject_candidate(backlog, slug, args.reason, today)
        store.write_candidate_backlog(backlog)
        store.ensure_navigation_files()
        detail = f"Rejected candidate `{slug}`: {args.reason}"
        store.append_log(today, "candidates", slug, detail)
        return OperationResult("candidates", slug, detail, None)
    return OperationResult("candidates", "candidate backlog", backlog.render(), None)


async def _run_chat(session: Session, paths: WikiPaths, resume: str | None) -> OperationResult:
    """The thin input loop; all REPL logic lives in ChatRepl (testable)."""
    chat_store = ChatStore(paths.root / "harness" / "chat.db")
    repl = ChatRepl(session=session, chat_store=chat_store)
    try:
        repl.start(resume)
        while True:
            try:
                line = await asyncio.to_thread(input, "llmwiki> ")
            except EOFError:  # Ctrl-D
                break
            if not await repl.handle(line):
                break
    except KeyboardInterrupt:  # Ctrl-C: same graceful path as /exit
        pass
    finally:
        repl.finish()
        chat_store.close()
    summary = (
        f"chat ended: {repl.turns} turns across {len(repl.conversations_touched)} conversation(s)"
    )
    return OperationResult("chat", "conversation", summary, None)


def main() -> None:
    args = _build_parser().parse_args()
    try:
        result = asyncio.run(_run(args))
    except (ConfigError, PdfError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    print(result.output)
    if result.transcript_path is not None:
        print(f"\n[transcript: {result.transcript_path}]", file=sys.stderr)


if __name__ == "__main__":
    main()
