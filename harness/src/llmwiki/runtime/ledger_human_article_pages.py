"""Build generated public linked pages from evidence-pack-backed articles."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.collection_pages import CollectionPlan
from llmwiki.domain.ledger.coverage import RenderedPage
from llmwiki.domain.ledger.evidence_pack import EvidencePack, EvidencePackSet
from llmwiki.domain.ledger.human_article import (
    ArticleFinding,
    ArticleWriter,
    HumanArticleOutput,
    HumanArticleRecord,
    RejectingArticleWriter,
)
from llmwiki.domain.ledger.human_article_rendering import render_human_article
from llmwiki.domain.ledger.human_article_validation import validate_human_article
from llmwiki.domain.pages import PageMetadata, WikiPage

_MAX_ARTICLE_ATTEMPTS = 2


@dataclass(frozen=True)
class HumanArticleLinkedPages:
    pages: tuple[WikiPage, ...]
    collection_plans: tuple[CollectionPlan, ...]
    article_output: HumanArticleOutput


@dataclass(frozen=True)
class HumanArticleAttempt:
    page: WikiPage | None
    record: HumanArticleRecord | None
    findings: tuple[ArticleFinding, ...]


def build_human_article_linked_pages(
    *,
    evidence_pack_set: EvidencePackSet,
    source_locator: str,
    today: str,
    article_writer: ArticleWriter | None = None,
    collection_plans: tuple[CollectionPlan, ...] = (),
) -> HumanArticleLinkedPages:
    writer = article_writer or RejectingArticleWriter()
    records: list[HumanArticleRecord] = []
    findings: list[ArticleFinding] = []
    pages: list[WikiPage] = []

    for pack in evidence_pack_set.packs:
        metadata = article_metadata(pack, source_locator, today)
        attempt = write_human_article_page(pack, metadata, writer)
        if attempt.page is None or attempt.record is None:
            findings.extend(attempt.findings)
            continue
        pages.append(attempt.page)
        records.append(attempt.record)

    accepted_collection_ids = {page.page_id for page in pages}
    accepted_collections = tuple(
        plan for plan in collection_plans if plan.collection_page_id in accepted_collection_ids
    )
    return HumanArticleLinkedPages(
        pages=tuple(pages),
        collection_plans=accepted_collections,
        article_output=HumanArticleOutput(tuple(records), tuple(findings)),
    )


def write_human_article_page(
    pack: EvidencePack,
    metadata: PageMetadata,
    writer: ArticleWriter,
    *,
    max_attempts: int = _MAX_ARTICLE_ATTEMPTS,
) -> HumanArticleAttempt:
    current_findings: tuple[ArticleFinding, ...] = ()
    for _ in range(max_attempts):
        article = writer.write_article(pack, current_findings)
        result = validate_human_article(pack, article)
        if result.accepted:
            rendered = render_human_article(pack, article)
            record = HumanArticleRecord(article, rendered.page_body_hash, rendered.coverage)
            page = WikiPage.from_metadata(
                with_article_coverage(metadata, pack, rendered), rendered.page_body
            )
            return HumanArticleAttempt(page, record, ())
        current_findings = result.findings
    return HumanArticleAttempt(None, None, current_findings)


def article_metadata(pack: EvidencePack, source_locator: str, today: str) -> PageMetadata:
    return PageMetadata(
        page_id=pack.page_id,
        page_kind=pack.page_kind,
        page_family=pack.page_family,
        summary=f"{pack.title}: human article from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=pack.source_id,
        category_path=_category_path(pack),
        source_id=source_locator,
    )


def with_article_coverage(
    metadata: PageMetadata, pack: EvidencePack, rendered: RenderedPage
) -> PageMetadata:
    return PageMetadata(
        page_id=metadata.page_id,
        page_kind=metadata.page_kind,
        summary=_navigation_summary_from_accepted_page(pack, rendered),
        page_family=metadata.page_family,
        sources=metadata.sources,
        updated=metadata.updated,
        domain=metadata.domain,
        category_path=metadata.category_path,
        project_id=metadata.project_id,
        source_id=metadata.source_id,
        tags=metadata.tags,
        aliases=metadata.aliases,
        projection_coverage_pointer=f"human-article-{pack.page_id}@{rendered.page_body_hash}",
    )


def _category_path(pack: EvidencePack) -> str:
    return {
        "procedure-guide": f"procedures/{pack.source_id}",
        "recipe-pattern": f"recipes/{pack.source_id}",
        "collection-page": f"sources/{pack.source_id}/collections",
        "topic-concept": f"concepts/{pack.source_id}",
        "broad-topic": f"concepts/{pack.source_id}",
    }.get(pack.page_family, f"pages/{pack.source_id}")


def _navigation_summary_from_accepted_page(pack: EvidencePack, rendered: RenderedPage) -> str:
    for line in rendered.page_body.splitlines():
        cleaned = _navigation_preview_line(line)
        if cleaned and cleaned != pack.title:
            return _trim_preview(f"{pack.title}: {cleaned}")
    return f"{pack.title}: accepted human article from source evidence."


_MARKDOWN_LINK_RE = re.compile(r"\[\[([^\]]+)]]")
_CITATION_RE = re.compile(r"\s+_\([^_]*\)_")


def _navigation_preview_line(line: str) -> str:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return ""
    if stripped.startswith("- Source ") or stripped.startswith("## Source Trail"):
        return ""
    stripped = re.sub(r"^\d+\.\s+", "", stripped)
    stripped = stripped.removeprefix("- ").strip()
    stripped = _CITATION_RE.sub("", stripped)
    stripped = _MARKDOWN_LINK_RE.sub(r"\1", stripped)
    return " ".join(stripped.split()).strip()


def _trim_preview(text: str, max_chars: int = 180) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0].rstrip(" ,;:") + "..."
