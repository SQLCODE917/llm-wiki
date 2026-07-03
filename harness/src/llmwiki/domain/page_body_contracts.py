"""PageBodyContract defaults, resolution, and validation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class PageBodySchema(Protocol):
    @property
    def page_body_contracts(self) -> tuple[PageBodyContract, ...]: ...

    @property
    def page_body_contract_by_page_kind(self) -> tuple[tuple[str, str], ...]: ...


@dataclass(frozen=True)
class PageBodyContract:
    contract_id: str
    match_page_kinds: tuple[str, ...]
    required_sections: tuple[str, ...] = ()
    required_markdown_shape: str = "prose"
    min_claim_bullets: int = 0
    max_claim_bullets: int = 0
    coverage_policy: str = ""
    max_words: int = 0
    max_source_word_ratio: float = 0.0
    max_copied_ngram_ratio: float = 1.0
    required_link_policy: str = "none"
    required_citation_policy: str = "none"
    required_uncertainty_policy: str = "none"


@dataclass(frozen=True)
class ResolvedPageBodyContract:
    contract_id: str
    required_sections: tuple[str, ...] = ()
    required_markdown_shape: str = "prose"
    min_claim_bullets: int = 0
    max_claim_bullets: int = 0
    coverage_policy: str = ""
    max_words: int = 0
    max_source_word_ratio: float = 0.0
    max_copied_ngram_ratio: float = 1.0
    required_link_page_ids: tuple[str, ...] = ()
    required_source_citations: tuple[str, ...] = ()
    required_uncertainty_terms: tuple[str, ...] = ()


@dataclass(frozen=True)
class PageBodyFinding:
    finding_type: str
    detail: str


@dataclass(frozen=True)
class SourcePlanContractSelection:
    contract_id: str
    match_page_kinds: tuple[str, ...] = ()
    page_ids: tuple[str, ...] = ()
    max_words_override: int = 0
    max_source_word_ratio_override: float = 0.0
    max_copied_ngram_ratio_override: float = 0.0


def default_page_body_contracts() -> tuple[PageBodyContract, ...]:
    return (
        PageBodyContract(
            contract_id="source-summary",
            match_page_kinds=("source",),
            required_sections=("Source record", "Key supported claims"),
            required_markdown_shape="claim-bullets",
            min_claim_bullets=3,
            max_claim_bullets=5,
            coverage_policy="main-supported-claims-and-explicit-limits",
            max_words=220,
            max_source_word_ratio=0.65,
            max_copied_ngram_ratio=0.50,
            required_link_policy="none",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
        PageBodyContract(
            contract_id="entity-page",
            match_page_kinds=("entity",),
            required_markdown_shape="prose",
            max_words=320,
            max_copied_ngram_ratio=0.80,
            required_link_policy="planned-related-pages",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
        PageBodyContract(
            contract_id="concept-page",
            match_page_kinds=("concept",),
            required_markdown_shape="prose",
            max_words=320,
            max_copied_ngram_ratio=0.80,
            required_link_policy="planned-related-pages",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
        PageBodyContract(
            contract_id="procedure-page",
            match_page_kinds=("procedure",),
            required_sections=("Goal", "Procedure Steps", "Source Trail"),
            required_markdown_shape="ordered-steps",
            max_words=650,
            max_copied_ngram_ratio=0.80,
            required_link_policy="planned-related-pages",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
        PageBodyContract(
            contract_id="synthesized-prose",
            match_page_kinds=("concept", "procedure", "recipe", "source"),
            required_markdown_shape="synthesized-prose",
            max_words=900,
            max_copied_ngram_ratio=0.50,
            required_link_policy="planned-related-pages",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
        PageBodyContract(
            contract_id="synthesis-page",
            match_page_kinds=("synthesis",),
            required_markdown_shape="prose",
            max_words=500,
            max_copied_ngram_ratio=0.80,
            required_link_policy="planned-related-pages",
            required_citation_policy="all-raw-sources",
            required_uncertainty_policy="preserve-source-uncertainty",
        ),
    )


def default_page_body_contract_by_page_kind() -> tuple[tuple[str, str], ...]:
    return (
        ("source", "source-summary"),
        ("entity", "entity-page"),
        ("concept", "concept-page"),
        ("procedure", "procedure-page"),
        ("synthesis", "synthesis-page"),
    )


def default_resolved_page_body_contract() -> ResolvedPageBodyContract:
    return ResolvedPageBodyContract(contract_id="default")


def contract_for_page_kind(schema: PageBodySchema, page_kind: str) -> PageBodyContract:
    contract_id = dict(schema.page_body_contract_by_page_kind).get(page_kind)
    contracts = {contract.contract_id: contract for contract in schema.page_body_contracts}
    if contract_id and contract_id in contracts:
        return contracts[contract_id]
    for contract in schema.page_body_contracts:
        if page_kind in contract.match_page_kinds:
            return contract
    return PageBodyContract(contract_id=f"{page_kind}-page", match_page_kinds=(page_kind,))


def contract_by_id(schema: PageBodySchema, contract_id: str) -> PageBodyContract:
    for contract in schema.page_body_contracts:
        if contract.contract_id == contract_id:
            return contract
    raise ValueError(f"No PageBodyContract with contract_id {contract_id!r}.")


def resolve_page_body_contract(
    contract: PageBodyContract,
    *,
    required_link_page_ids: tuple[str, ...] = (),
    required_source_citations: tuple[str, ...] = (),
    required_uncertainty_terms: tuple[str, ...] = (),
    selection: SourcePlanContractSelection | None = None,
) -> ResolvedPageBodyContract:
    max_words = selection.max_words_override if selection and selection.max_words_override else 0
    max_source_word_ratio = (
        selection.max_source_word_ratio_override
        if selection and selection.max_source_word_ratio_override
        else 0.0
    )
    max_copied_ngram_ratio = (
        selection.max_copied_ngram_ratio_override
        if selection and selection.max_copied_ngram_ratio_override
        else 0.0
    )
    return ResolvedPageBodyContract(
        contract_id=contract.contract_id,
        required_sections=contract.required_sections,
        required_markdown_shape=contract.required_markdown_shape,
        min_claim_bullets=contract.min_claim_bullets,
        max_claim_bullets=contract.max_claim_bullets,
        coverage_policy=contract.coverage_policy,
        max_words=max_words or contract.max_words,
        max_source_word_ratio=max_source_word_ratio or contract.max_source_word_ratio,
        max_copied_ngram_ratio=max_copied_ngram_ratio or contract.max_copied_ngram_ratio,
        required_link_page_ids=(
            required_link_page_ids
            if contract.required_link_policy == "planned-related-pages"
            else ()
        ),
        required_source_citations=required_source_citations,
        required_uncertainty_terms=required_uncertainty_terms,
    )


def validate_page_body(
    page_body: str,
    contract: ResolvedPageBodyContract,
    source_text: str = "",
) -> tuple[PageBodyFinding, ...]:
    from llmwiki.domain.page_body_validation import validate_page_body as _validate

    return _validate(page_body, contract, source_text)


def render_source_summary_draft(draft: object) -> str:
    from llmwiki.domain.page_body_validation import render_source_summary_draft as _render

    return _render(draft)  # type: ignore[arg-type]


def validate_source_summary_draft(
    draft: object,
    plan: object,
    source_text: str = "",
) -> tuple[PageBodyFinding, ...]:
    from llmwiki.domain.page_body_validation import validate_source_summary_draft as _validate

    return _validate(draft, plan, source_text)  # type: ignore[arg-type]


def render_page_body_findings(
    findings: tuple[PageBodyFinding, ...],
    contract: ResolvedPageBodyContract,
) -> str:
    from llmwiki.domain.page_body_validation import render_page_body_findings as _render

    return _render(findings, contract)


def uncertainty_terms_in_text(text: str) -> tuple[str, ...]:
    from llmwiki.domain.page_body_validation import uncertainty_terms_in_text as _terms

    return _terms(text)
