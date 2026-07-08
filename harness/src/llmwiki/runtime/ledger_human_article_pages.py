"""Build generated public linked pages from evidence-pack-backed articles."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.article_write_queue import (
    ArticleWriteQueueFinding,
    ArticleWriteQueuePolicy,
    ArticleWriteQueueRun,
    build_article_write_queue_run,
    default_article_write_queue_policy,
    ordered_article_write_packs,
    queue_finding,
)
from llmwiki.domain.ledger.article_lint import lint_human_article
from llmwiki.domain.ledger.article_lint_contracts import ArticleLintRun
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
from llmwiki.domain.ledger.page_title_lint import PageTitleFinding
from llmwiki.domain.pages import PageMetadata, WikiPage

_MAX_ARTICLE_ATTEMPTS = 2


@dataclass(frozen=True)
class HumanArticleLinkedPages:
    pages: tuple[WikiPage, ...]
    collection_plans: tuple[CollectionPlan, ...]
    article_output: HumanArticleOutput
    article_lint_runs: tuple[ArticleLintRun, ...]
    article_write_queue_run: ArticleWriteQueueRun


@dataclass(frozen=True)
class HumanArticleAttempt:
    page: WikiPage | None
    record: HumanArticleRecord | None
    findings: tuple[ArticleFinding, ...]
    lint_run: ArticleLintRun | None = None


def build_human_article_linked_pages(
    *,
    evidence_pack_set: EvidencePackSet,
    source_locator: str,
    today: str,
    article_writer: ArticleWriter | None = None,
    collection_plans: tuple[CollectionPlan, ...] = (),
    title_findings_by_page_id: dict[str, tuple[PageTitleFinding, ...]] | None = None,
    queue_policy: ArticleWriteQueuePolicy | None = None,
) -> HumanArticleLinkedPages:
    writer = article_writer or RejectingArticleWriter()
    policy = queue_policy or default_article_write_queue_policy(
        evidence_pack_set.source_profile_kind
    )
    records: list[HumanArticleRecord] = []
    findings: list[ArticleFinding] = []
    lint_runs: list[ArticleLintRun] = []
    pages: list[WikiPage] = []
    queue_findings: list[ArticleWriteQueueFinding] = []
    title_findings = title_findings_by_page_id or {}
    packs_by_page_id = {pack.page_id: pack for pack in evidence_pack_set.packs}
    ordered_packs = ordered_article_write_packs(evidence_pack_set.packs, policy)

    attempted_page_ids: list[str] = []
    skipped_page_ids: list[str] = []
    exhausted_reason = "pack-list-exhausted"
    for index, pack in enumerate(ordered_packs):
        if len(records) >= policy.target_accepted_articles:
            exhausted_reason = "target-reached"
            skipped = tuple(item.page_id for item in ordered_packs[index:])
            skipped_page_ids.extend(skipped)
            queue_findings.extend(
                queue_finding(
                    "info",
                    "skipped-after-target",
                    page_id,
                    "article queue target was reached before this pack was attempted",
                )
                for page_id in skipped
            )
            break
        if len(attempted_page_ids) >= policy.max_attempted_packs:
            exhausted_reason = "attempt-budget-exhausted"
            skipped = tuple(item.page_id for item in ordered_packs[index:])
            skipped_page_ids.extend(skipped)
            queue_findings.extend(
                queue_finding(
                    "warning",
                    "attempt-budget-exceeded",
                    page_id,
                    "article write queue attempt budget was exhausted",
                )
                for page_id in skipped
            )
            break
        attempted_page_ids.append(pack.page_id)
        metadata = article_metadata(pack, source_locator, today)
        attempt = write_human_article_page(
            pack,
            metadata,
            writer,
            max_attempts=policy.max_attempts_per_pack,
            title_findings=title_findings.get(pack.page_id, ()),
        )
        if attempt.lint_run is not None:
            lint_runs.append(attempt.lint_run)
        if attempt.page is None or attempt.record is None:
            findings.extend(attempt.findings)
            queue_findings.append(_attempt_queue_finding(pack.page_id, attempt))
            continue
        pages.append(attempt.page)
        records.append(attempt.record)

    if (
        exhausted_reason == "pack-list-exhausted"
        and len(records) >= policy.target_accepted_articles
    ):
        exhausted_reason = "target-reached"

    accepted_collection_ids = {page.page_id for page in pages}
    accepted_collections = tuple(
        plan for plan in collection_plans if plan.collection_page_id in accepted_collection_ids
    )
    queue_run = build_article_write_queue_run(
        source_hash=evidence_pack_set.source_hash,
        policy=policy,
        attempted_page_ids=tuple(attempted_page_ids),
        accepted_page_ids=tuple(record.article.page_id for record in records),
        skipped_page_ids=tuple(dict.fromkeys(skipped_page_ids)),
        exhausted_reason=exhausted_reason,
        packs_by_page_id=packs_by_page_id,
        findings=tuple(queue_findings),
    )
    return HumanArticleLinkedPages(
        pages=tuple(pages),
        collection_plans=accepted_collections,
        article_output=HumanArticleOutput(tuple(records), tuple(findings)),
        article_lint_runs=tuple(lint_runs),
        article_write_queue_run=queue_run,
    )


def write_human_article_page(
    pack: EvidencePack,
    metadata: PageMetadata,
    writer: ArticleWriter,
    *,
    max_attempts: int = _MAX_ARTICLE_ATTEMPTS,
    title_findings: tuple[PageTitleFinding, ...] = (),
    initial_findings: tuple[ArticleFinding, ...] = (),
) -> HumanArticleAttempt:
    current_findings: tuple[ArticleFinding, ...] = initial_findings
    for _ in range(max_attempts):
        try:
            article = writer.write_article(pack, current_findings)
        except Exception as exc:
            message = str(exc) or exc.__class__.__name__
            return HumanArticleAttempt(
                None,
                None,
                (
                    ArticleFinding(
                        "blocking",
                        "article-writer-error",
                        pack.page_id,
                        f"Article writer failed: {message}",
                    ),
                ),
            )
        result = validate_human_article(pack, article)
        if result.accepted:
            rendered = render_human_article(pack, article)
            lint_run = lint_human_article(
                article=article,
                rendered=rendered,
                pack=pack,
                title_findings=title_findings,
            )
            if lint_run.publication_gate.decision != "accepted":
                return HumanArticleAttempt(None, None, _lint_findings(lint_run), lint_run)
            record = HumanArticleRecord(article, rendered.page_body_hash, rendered.coverage)
            page = WikiPage.from_metadata(
                with_article_coverage(metadata, pack, rendered), rendered.page_body
            )
            return HumanArticleAttempt(page, record, (), lint_run)
        current_findings = result.findings
    return HumanArticleAttempt(None, None, current_findings)


def _lint_findings(lint_run: ArticleLintRun) -> tuple[ArticleFinding, ...]:
    return tuple(
        ArticleFinding(
            finding.severity,
            finding.finding_code,
            finding.page_id,
            finding.message,
            finding.article_claim_id,
            finding.support_ref,
        )
        for finding in lint_run.findings
        if finding.severity == "blocking"
    )


def _attempt_queue_finding(
    page_id: str, attempt: HumanArticleAttempt
) -> ArticleWriteQueueFinding:
    if attempt.lint_run is not None:
        return queue_finding(
            "warning",
            "lint-blocked",
            page_id,
            "article attempt was blocked by article lint",
        )
    return queue_finding(
        "warning",
        "writer-failed",
        page_id,
        "article writer or article validation did not produce an accepted page",
    )


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
