"""Static checks for the root CHECK_PLAN contract."""

from __future__ import annotations

import inspect
from pathlib import Path

import pytest

from llmwiki.cli import _build_parser
from llmwiki.domain.schema import PAGE_FAMILIES, PAGE_KINDS, PAGE_METADATA_FIELDS
from llmwiki.runtime.ingest_compiler import IngestCompiler
from llmwiki.runtime.ingest_compiler_artifacts import _STAGE_ORDER, compiler_artifact_files
from llmwiki.runtime.session import Session

REPO_ROOT = Path(__file__).resolve().parents[2]
CHECK_PLAN_PATH = REPO_ROOT / "CHECK_PLAN.md"

REQUIRED_SECTIONS = (
    "## Source-Of-Truth Map",
    "## Page Contract Table",
    "## Compiler Artifact Table",
    "## Forbidden Patterns",
    "## Agent Workflow Catalog",
    "## Update Order",
    "## Three-Pass Validation",
)

FORBIDDEN_ACTIVE_STRINGS = (
    "build_source_ledger(",
    "_finish_ledger_ingest(",
    "_persist_page_plan(",
    "_pdf_page_plan(",
    "page-synthesis-plan.json",
    "page-draft.json",
    "claim-ledger.json",
    "chunk_file(",
)

REMOVED_INGEST_FLAGS = (
    "--write-human-articles",
    "--reintegrate",
    "--ingest-flow",
)


def test_check_plan_exists_and_has_required_sections() -> None:
    text = CHECK_PLAN_PATH.read_text(encoding="utf-8")

    for section in REQUIRED_SECTIONS:
        assert section in text


def test_guidance_docs_reference_check_plan() -> None:
    for relative_path in (
        "AGENTS.md",
        "SCHEMA.md",
        "docs/writing-tdds.md",
    ):
        text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        assert "CHECK_PLAN.md" in text


def test_domain_vocabulary_contains_check_plan_terms() -> None:
    text = (REPO_ROOT / "docs" / "domain-vocabulary.md").read_text(encoding="utf-8")

    for term in (
        "| check plan |",
        "| contract source of truth |",
        "| forbidden pattern |",
        "| agent workflow |",
        "| `CheckPlan` | `check_plan` |",
        "| `ContractSourceOfTruth` | `contract_source_of_truth` |",
        "| `ForbiddenPattern` | `forbidden_pattern` |",
        "| `AgentWorkflow` | `agent_workflow` |",
    ):
        assert term in text


def test_check_plan_lists_schema_page_contract_constants() -> None:
    text = CHECK_PLAN_PATH.read_text(encoding="utf-8")

    for page_kind in PAGE_KINDS:
        assert f"| {page_kind} |" in text
    for page_family in PAGE_FAMILIES:
        assert f"| {page_family} |" in text
    for field in PAGE_METADATA_FIELDS:
        assert f"| {field} |" in text


def test_check_plan_lists_compiler_stage_order_and_output_artifacts() -> None:
    text = CHECK_PLAN_PATH.read_text(encoding="utf-8")

    for stage_name, _inputs, outputs in _STAGE_ORDER:
        assert f"| {stage_name} |" in text
        for artifact_kind in outputs:
            assert _artifact_path(artifact_kind) in text
    assert "ingest-artifact-set.json" in text


def test_active_entrypoints_do_not_reactivate_superseded_ingest_paths() -> None:
    active_sources = {
        "Session.ingest": inspect.getsource(Session.ingest),
        "IngestCompiler.compile": inspect.getsource(IngestCompiler.compile),
        "compiler_artifact_files": inspect.getsource(compiler_artifact_files),
        "source_resolver.py": (
            REPO_ROOT / "harness" / "src" / "llmwiki" / "store" / "source_resolver.py"
        ).read_text(encoding="utf-8"),
    }

    for surface, source in active_sources.items():
        for forbidden in FORBIDDEN_ACTIVE_STRINGS:
            assert forbidden not in source, f"{surface} contains {forbidden}"


def test_compiler_stage_outputs_do_not_include_superseded_artifacts() -> None:
    output_paths = {
        _artifact_path(artifact_kind)
        for _stage_name, _inputs, outputs in _STAGE_ORDER
        for artifact_kind in outputs
    }

    assert "claim-ledger.json" not in output_paths
    assert "page-synthesis-plan.json" not in output_paths
    assert "page-draft.json" not in output_paths


def test_ingest_parser_rejects_removed_old_flow_flags() -> None:
    parser = _build_parser()

    for flag in REMOVED_INGEST_FLAGS:
        with pytest.raises(SystemExit):
            parser.parse_args(["ingest", "book.pdf", flag])


def test_session_ingest_signature_exposes_no_removed_old_flow_controls() -> None:
    signature = inspect.signature(Session.ingest)

    assert tuple(signature.parameters) == ("self", "source_locator", "reextract")


def test_schema_has_no_current_chunk_manifest_navigation_guidance() -> None:
    text = (REPO_ROOT / "SCHEMA.md").read_text(encoding="utf-8")

    for phrase in ("chunk manifest", "chunking", "Page-Map Navigation"):
        assert phrase not in text


def _artifact_path(artifact_kind: str) -> str:
    suffix = ".md" if artifact_kind == "diagnostics-report" else ".json"
    return f"{artifact_kind}{suffix}"
