"""Single ingest compiler contract tests."""

from __future__ import annotations

import inspect

import pytest
from forge.context import ContextManager, NoCompact

from llmwiki.cli import _build_parser
from llmwiki.config import WikiPaths
from llmwiki.domain.ingest_compiler import (
    CompilerStage,
    IngestCompilation,
    IngestCompilerInput,
    build_ingest_artifact_set,
)
from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.evidence_pack import EvidencePack
from llmwiki.domain.ledger.human_article import (
    ArticleBlock,
    ArticleClaim,
    ArticleFinding,
    ArticleRelatedLink,
    ArticleSection,
    HumanArticle,
)
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.runtime.ingest_compiler import IngestCompiler
from llmwiki.runtime.ledger_pipeline import build_source_ledger
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-07-04"


class CoherentArticleWriter:
    def write_article(
        self, pack: EvidencePack, findings: tuple[ArticleFinding, ...] = ()
    ) -> HumanArticle:
        sentence = f"{pack.title} has source-backed evidence."
        claim = ArticleClaim("claim-1", sentence, (pack.items[0].support_ref,))
        block = ArticleBlock("block-1", "paragraph", sentence)
        section = ArticleSection("section-1", "Overview", (block,), ("claim-1",))
        return HumanArticle(pack.page_id, pack.title, (section,), (claim,))


class BadRelatedLinkWriter:
    def write_article(
        self, pack: EvidencePack, findings: tuple[ArticleFinding, ...] = ()
    ) -> HumanArticle:
        sentence = f"{pack.title} has source-backed evidence."
        claim = ArticleClaim("claim-1", sentence, (pack.items[0].support_ref,))
        block = ArticleBlock("block-1", "paragraph", sentence)
        section = ArticleSection("section-1", "Overview", (block,), ("claim-1",))
        link = ArticleRelatedLink(
            page_id="missing-preview",
            label="Missing Preview",
            relation="related",
            preview_text="",
            shared_support_refs=(pack.items[0].support_ref,),
        )
        return HumanArticle(pack.page_id, pack.title, (section,), (claim,), (link,))


class FakeCompiler:
    def __init__(self) -> None:
        self.inputs: list[IngestCompilerInput] = []

    def compile(self, compiler_input: IngestCompilerInput) -> IngestCompilation:
        self.inputs.append(compiler_input)
        page = WikiPage.from_metadata(
            PageMetadata(
                page_id="moon",
                page_kind="source",
                page_family="source-manifest",
                summary="Moon compiler page.",
                sources=("raw/moon.md",),
                updated=TODAY,
            ),
            "# Moon\n\nCompiler-owned page.\n",
        )
        stage = CompilerStage("source-map", (), ("fake-source-map",), "completed", 0, 0)
        artifact_set = build_ingest_artifact_set(
            source_id="moon",
            source_locator="moon.md",
            source_hash="abc123",
            run_id="fake-run",
            stages=(stage,),
            artifacts=(),
            findings=(),
            accepted_page_ids=("moon",),
            rejected_page_ids=(),
        )
        return IngestCompilation(
            source_locator="moon.md",
            source_page_id="moon",
            source_hash="abc123",
            accepted_pages=(page,),
            artifact_files={"ingest-artifact-set.json": canonical_json(artifact_set, indent=2)},
            artifact_set=artifact_set,
            report="fake compiler report",
        )


def test_compiler_stage_order_and_artifact_manifest(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "shade.md").write_text(_shade_source(), encoding="utf-8")

    compilation = IngestCompiler(
        store=store,
        today=TODAY,
        run_id="compiler-test",
        article_writer=CoherentArticleWriter(),
    ).compile(IngestCompilerInput("shade.md"))

    assert tuple(stage.stage_name for stage in compilation.artifact_set.stages) == (
        "source-map",
        "source-structure",
        "source-profile",
        "evidence-records",
        "page-plan",
        "evidence-packs",
        "human-articles",
        "article-lint",
        "diagnostics",
        "repair",
        "staged-publish",
    )
    assert "ingest-artifact-set.json" in compilation.artifact_files
    assert "diagnostic-question-set.json" in compilation.artifact_files
    assert "diagnostic-answer-set.json" in compilation.artifact_files
    assert "diagnostic-finding-set.json" in compilation.artifact_files
    assert "diagnostics-report.md" in compilation.artifact_files
    assert "repair-task-set.json" in compilation.artifact_files
    assert "repair-run.json" in compilation.artifact_files
    assert "human-article-initial.json" in compilation.artifact_files
    assert "article-lint-runs-initial.json" in compilation.artifact_files
    assert "normalized-source-map.json" in compilation.artifact_files
    assert "source-structure-integrity.json" in compilation.artifact_files
    assert "source-record-plan.json" in compilation.artifact_files
    assert "candidate-admission-report.json" in compilation.artifact_files
    assert "article-viability-report.json" in compilation.artifact_files
    assert "claim-ledger.json" not in compilation.artifact_files
    assert "page-synthesis-plan.json" not in compilation.artifact_files
    assert set(compilation.artifact_set.accepted_page_ids) >= {"shade", "shade-shade"}


def test_blocking_article_lint_omits_only_generated_article(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "shade.md").write_text(_shade_source(), encoding="utf-8")

    compilation = IngestCompiler(
        store=store,
        today=TODAY,
        run_id="compiler-test",
        article_writer=BadRelatedLinkWriter(),
    ).compile(IngestCompilerInput("shade.md"))

    assert tuple(page.page_id for page in compilation.accepted_pages) == ("shade",)
    assert any(
        finding.stage_name == "article-lint"
        and finding.finding_code == "missing-related-link-preview"
        and finding.page_id == "shade-shade"
        for finding in compilation.artifact_set.findings
    )


def test_javascript_recipe_publishes_code_payload_context(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "javascriptallonge.md").write_text(
        _javascript_recipe_source(),
        encoding="utf-8",
    )

    compilation = IngestCompiler(
        store=store,
        today=TODAY,
        run_id="compiler-test",
        article_writer=CoherentArticleWriter(),
    ).compile(IngestCompilerInput("javascriptallonge.md"))

    recipe = next(
        page
        for page in compilation.accepted_pages
        if page.page_metadata.page_family == "recipe-pattern"
    )
    assert "## Evidence Details" in recipe.page_body
    assert "values.map" in recipe.page_body
    assert "diagnostic-question-set.json" in compilation.artifact_files
    assert "repair-run.json" in compilation.artifact_files


async def test_session_ingest_calls_injected_compiler(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "moon.md").write_text("The Moon is bright.", encoding="utf-8")
    compiler = FakeCompiler()
    session = Session(
        store=store,
        client=None,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
        today=TODAY,
        ingest_compiler=compiler,
    )

    result = await session.ingest("moon.md")

    assert compiler.inputs == [IngestCompilerInput("moon.md")]
    assert result.output.startswith("fake compiler report\nCompiler artifacts: ")
    assert store.read_page("moon").startswith("---")
    assert (store.ingest_compiler_artifact_dir("moon.md") / "ingest-artifact-set.json").is_file()


def test_session_ingest_method_is_compiler_only() -> None:
    source = inspect.getsource(Session.ingest)

    assert "build_source_ledger" not in source
    assert "_finish_ledger_ingest" not in source
    assert "_persist_page_plan" not in source
    assert "_pdf_page_plan" not in source


def test_superseded_ledger_page_plan_surfaces_are_marked_for_removal() -> None:
    marker = "Superseded PagePlan/claim-ledger ingest path"
    surfaces = (
        Session._ingest_pdf,
        Session._finish_ledger_ingest,
        Session._pdf_page_plan,
        Session._cached_pdf_page_plan,
        Session._persist_page_plan,
        build_source_ledger,
    )

    for surface in surfaces:
        doc = inspect.getdoc(surface) or ""
        assert marker in doc
        assert "Do not call this from production ingest" in doc
        assert "scheduled for removal" in doc


def test_cli_ingest_removed_old_flow_flags() -> None:
    parser = _build_parser()

    with pytest.raises(SystemExit):
        parser.parse_args(["ingest", "book.pdf", "--write-human-articles"])
    with pytest.raises(SystemExit):
        parser.parse_args(["ingest", "book.pdf", "--reintegrate"])


def _shade_source() -> str:
    return """# Shade

Shade is a dark spirit.
A shade can create darkness around a target.
"""


def _javascript_recipe_source() -> str:
    return """# Map Transform

JavaScript examples can transform each value.

```js
const doubled = values.map(value => value * 2);
```

Map takes a function and returns a new array.
"""
