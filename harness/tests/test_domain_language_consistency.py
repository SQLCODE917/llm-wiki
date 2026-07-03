"""Static checks for the domain-language consistency TDD."""

from __future__ import annotations

import re
from dataclasses import fields
from pathlib import Path

from llmwiki.domain.links import compute_findings
from llmwiki.domain.objects import LintRun, SourcePlan
from llmwiki.domain.pages import PageMetadata, WikiPage, render_page
from llmwiki.domain.schema import PAGE_FAMILIES, PAGE_KINDS, PAGE_METADATA_FIELDS
from llmwiki.workflows.tools import ReadPageParams, ReadSourceParams, WritePageParams

REPO_ROOT = Path(__file__).resolve().parents[2]
CORE_FILES = (
    "SCHEMA.md",
    "docs/domain-vocabulary.md",
    "harness/src/llmwiki/domain/pages.py",
    "harness/src/llmwiki/domain/index.py",
    "harness/src/llmwiki/domain/objects.py",
    "harness/src/llmwiki/domain/links.py",
    "harness/src/llmwiki/domain/ingest_profiles.py",
    "harness/src/llmwiki/domain/ingest_route_plan.py",
    "harness/src/llmwiki/domain/ingest_route_history.py",
    "harness/src/llmwiki/store/wiki_store.py",
    "harness/src/llmwiki/workflows/tools.py",
    "harness/src/llmwiki/workflows/definitions.py",
    "harness/src/llmwiki/workflows/chat_file_tools.py",
    "harness/src/llmwiki/workflows/fixed_page_tools.py",
    "harness/src/llmwiki/workflows/ingest_route_tools.py",
    "harness/src/llmwiki/workflows/pdf_ingest.py",
    "harness/src/llmwiki/workflows/prompts.py",
    "harness/src/llmwiki/runtime/session.py",
)

FORBIDDEN_CORE_PATTERNS = (
    r"\bPAGE_CATEGORIES\b",
    r"\bvalidate_page_name\b",
    r"\bvalidate_category\b",
    r"\bindex_page_names\b",
    r"\bindex_names\b",
    r"\btarget_page_metadata\b",
    r"\btarget_page_paths\b",
    r"\bexpected_wiki_pages\b",
    r"\brel_path\b",
    r"\bsource_path\b",
    r"\bparams\.path\b",
    r"\bparams\.name\b",
    r"\bparams\.category\b",
    r"\bparams\.content\b",
    r"category: ",
    r"category='",
    r"parameter=content>",
)


def test_core_boundaries_do_not_use_legacy_domain_terms() -> None:
    for relative_path in CORE_FILES:
        text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        for pattern in FORBIDDEN_CORE_PATTERNS:
            assert not re.search(pattern, text), f"{relative_path} contains {pattern}"


def test_model_facing_tool_params_use_domain_code_names() -> None:
    assert set(ReadSourceParams.model_fields) == {"source_locator"}
    assert set(ReadPageParams.model_fields) == {"page_id"}
    assert set(WritePageParams.model_fields) == {
        "page_id",
        "page_kind",
        "summary",
        "page_body",
        "source_record_text",
        "claim_bullets",
        "sources",
    }


def test_domain_vocabulary_contains_domain_term_code_name_table() -> None:
    text = (REPO_ROOT / "docs/domain-vocabulary.md").read_text(encoding="utf-8")

    assert "| DomainTerm | CodeName |" in text
    for row in (
        "| `PageId` | `page_id` |",
        "| `PageKind` | `page_kind` |",
        "| `PageBody` | `page_body` |",
        "| `SourceLocator` | `source_locator` |",
        "| `LintFinding` | `lint_finding` |",
    ):
        assert row in text


def test_domain_frontmatter_uses_page_metadata_field_names() -> None:
    metadata = PageMetadata(
        page_id="closure",
        page_kind="concept",
        page_family="topic-concept",
        summary="A closure.",
    )
    page = WikiPage.from_metadata(metadata, "Body.")
    rendered = render_page(page)

    assert "page_id: closure" in rendered
    assert "page_kind: concept" in rendered
    assert "page_family: topic-concept" in rendered
    assert "summary: A closure." in rendered
    assert "category:" not in rendered
    assert "name:" not in rendered


def test_schema_module_is_the_page_kind_and_metadata_field_source() -> None:
    assert PAGE_KINDS == ("source", "entity", "concept", "procedure", "recipe", "synthesis")
    assert PAGE_FAMILIES == (
        "source-manifest",
        "source-summary",
        "section-reference",
        "topic-concept",
        "procedure-guide",
        "recipe-pattern",
        "collection-page",
        "broad-topic",
        "entity-profile",
        "cross-source-synthesis",
    )
    assert PAGE_METADATA_FIELDS == (
        "PageId",
        "PageKind",
        "PageFamily",
        "Summary",
        "Sources",
        "Updated",
    )


def test_source_plan_references_planned_page_writes_without_target_duplicates() -> None:
    source_plan_fields = {field.name for field in fields(SourcePlan)}
    assert "planned_page_write_ids" in source_plan_fields
    assert "target_page_metadata" not in source_plan_fields
    assert "target_page_paths" not in source_plan_fields
    assert "expected_wiki_pages" not in source_plan_fields


def test_compute_findings_returns_lint_run() -> None:
    lint_run = compute_findings({"alpha": "See [[ghost]]."}, index_page_ids={"alpha"})

    assert isinstance(lint_run, LintRun)
    assert lint_run.lint_findings[0].page_id == "alpha"
