"""Quality checks for evidence-pack-backed human article prose."""

from __future__ import annotations

import re
from collections import Counter

from llmwiki.domain.ledger.evidence_pack import EvidencePack
from llmwiki.domain.ledger.human_article import ArticleBlock, ArticleFinding, HumanArticle
from llmwiki.domain.ledger.page_synthesis_text import ngrams, words
from llmwiki.domain.prose_flow import structural_incompleteness_reason

_COPIED_NGRAM_SIZE = 8
_MAX_COPIED_NGRAM_RATIO = 0.50
_MODAL_ADVERB_TERMINAL = re.compile(
    r"\b(?:will|would|can|could|may|might|must|should|shall)\s+"
    r"(?:easily|also|only|then|again|therefore)[.!?]?$",
    re.IGNORECASE,
)
_DETERMINER_MODAL_JAM = re.compile(
    r"\b(?:a|an|the)\s+(?:will|can|may|must|should|shall)\s+\w+",
    re.IGNORECASE,
)
_CONJUNCTION_MODAL_JAM = re.compile(
    r"\b(?:destroys?|enters?|creates?|takes?)\s+(?:a|an|the)\s+"
    r"(?:will|can|may|must|should|shall)\b",
    re.IGNORECASE,
)
_CLIPPED_WILL_O_WISP = re.compile(
    r"\bcomes?\s+into\s+will\s*-\s*o\s*-\s*wisp",
    re.IGNORECASE,
)


def clipped_fragment_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleFinding, ...]:
    item_by_ref = {item.support_ref.code: item for item in pack.items}
    findings: list[ArticleFinding] = []
    for claim in article.claims:
        if _is_structurally_clipped(claim.sentence):
            findings.append(
                _finding(
                    pack,
                    "clipped-evidence-fragment",
                    "article claim appears to be a clipped source fragment",
                    claim.claim_id,
                )
            )
            continue
        claim_words = words(claim.sentence)
        if len(claim_words) < 5:
            continue
        for support_ref in claim.support_refs:
            item = item_by_ref.get(support_ref.code)
            if item is None:
                continue
            source_words = words(f"{item.source_text}\n{item.payload_text}")
            if _looks_like_clipped_fragment(claim_words, source_words):
                findings.append(
                    _finding(
                        pack,
                        "clipped-evidence-fragment",
                        "article claim appears to be a clipped source fragment",
                        claim.claim_id,
                        support_ref.code,
                    )
                )
                break
    return tuple(findings)


def copied_phrase_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleFinding, ...]:
    source_text = " ".join(f"{item.source_text} {item.payload_text}" for item in pack.items)
    source_ngrams = set(ngrams(words(source_text), _COPIED_NGRAM_SIZE))
    if not source_ngrams:
        return ()
    article_text = " ".join(
        text for block in _blocks(article) for text in _article_block_texts(block)
    )
    article_ngrams = ngrams(words(article_text), _COPIED_NGRAM_SIZE)
    if not article_ngrams:
        return ()
    copied = sum(
        count for ngram, count in Counter(article_ngrams).items() if ngram in source_ngrams
    )
    ratio = copied / len(article_ngrams)
    if ratio <= _MAX_COPIED_NGRAM_RATIO:
        return ()
    return (
        _finding(
            pack,
            "copied-source-phrases",
            f"copied 8-gram ratio {ratio:.2f} exceeds {_MAX_COPIED_NGRAM_RATIO:.2f}",
        ),
    )


def _blocks(article: HumanArticle) -> tuple[ArticleBlock, ...]:
    return tuple(block for section in article.sections for block in section.blocks)


def _article_block_texts(block: ArticleBlock) -> tuple[str, ...]:
    if block.block_kind == "table":
        return tuple(cell for row in block.table_rows for cell in row)
    if block.items:
        return block.items
    if block.text:
        return (block.text,)
    return ()


def _looks_like_clipped_fragment(
    claim_words: tuple[str, ...], source_words: tuple[str, ...]
) -> bool:
    if len(source_words) <= len(claim_words) + 2:
        return False
    if claim_words == source_words[: len(claim_words)]:
        return True
    return _is_ordered_subsequence(claim_words, source_words) and (
        len(source_words) - len(claim_words) >= 3
    )


def _is_structurally_clipped(text: str) -> bool:
    cleaned = " ".join(text.split()).strip()
    return (
        structural_incompleteness_reason(cleaned) is not None
        or _MODAL_ADVERB_TERMINAL.search(cleaned) is not None
        or _CONJUNCTION_MODAL_JAM.search(cleaned) is not None
        or _DETERMINER_MODAL_JAM.search(cleaned) is not None
        or _CLIPPED_WILL_O_WISP.search(cleaned) is not None
    )


def _is_ordered_subsequence(needle: tuple[str, ...], haystack: tuple[str, ...]) -> bool:
    index = 0
    for word in haystack:
        if word == needle[index]:
            index += 1
            if index == len(needle):
                return True
    return False


def _finding(
    pack: EvidencePack,
    finding_type: str,
    message: str,
    claim_id: str = "",
    support_ref: str = "",
) -> ArticleFinding:
    return ArticleFinding(
        "blocking", finding_type, pack.page_id, message, claim_id, support_ref
    )
