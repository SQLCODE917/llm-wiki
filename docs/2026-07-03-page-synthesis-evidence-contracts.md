# TDD: Page Synthesis Evidence Contracts

## Summary

Add a synthesis layer between the source claim ledger and generated wiki pages.

The claim ledger remains the evidence authority. The projection pipeline builds a
`PageSynthesisPlan`, creates a structured `PageDraft`, validates every factual
sentence against the selected evidence, and renders final markdown only from an
accepted draft.

This follows the STORM and GraphRAG pattern of evidence selection, outline, and
article generation. This wiki adds stricter sentence-level contracts because the
generated markdown is durable project state.

## Problem

High-value generated pages can be too extractive. They often preserve source
fragments instead of creating readable wiki prose. When the source extraction is
noisy, that noise can flow into topic pages, procedure pages, recipe pages, and
collection pages.

The current projection code can check citations and source support after a page
exists. It does not have a first-class contract for the draft itself. That makes
it hard to reject weak prose before publication.

## Goals

- Generate high-value pages from a compact, explicit evidence set.
- Keep source-close lookup pages source-close.
- Validate synthesized prose before it becomes markdown.
- Make each generated factual sentence traceable to selected ledger or atom
  support.
- Reject failed synthesis instead of publishing extractive fallback pages.
- Record enough artifacts to audit accepted and rejected page drafts.

## Non-Goals

- Replace raw extraction.
- Replace the claim ledger.
- Force strict synthesis onto source manifests or section reference pages.
- Add migration support for old wiki output.
- Add a stable external artifact format.

## Glossary

- `PageSynthesisPlan`: the selected evidence, outline, related links, and page
  identity for one generated page.
- `PageDraft`: structured model output made of markdown blocks and draft claims.
- `DraftClaim`: one factual sentence plus the selected evidence references that
  support it.
- `DraftEvidenceRef`: a reference to selected support in a synthesis plan.
- `PageDraftValidator`: pure validation for support, coverage, copied phrases,
  placeholders, and malformed topic identities.
- `PageDraftRenderer`: the only component that converts an accepted draft into
  final markdown and projection coverage.

## Design

### Page Families

Use synthesis for high-value generated page families:

- `procedure-guide`
- `recipe-pattern`
- `topic-concept`
- `broad-topic`
- `collection-page`

Do not use synthesis for:

- `source-manifest`, which stays navigation-first.
- `section-reference`, which stays source-close for lookup evidence.

### Data Flow

1. Source extraction produces a claim ledger and atom contexts.
2. The existing planners choose topic, procedure, recipe, and collection page
   targets.
3. The projection layer builds a `PageSynthesisPlan` for each target.
4. A draft producer creates a structured `PageDraft`.
5. `PageDraftValidator` accepts or rejects the draft.
6. `PageDraftRenderer` renders markdown and projection coverage for accepted
   drafts.
7. Rejected pages are not published. Findings are recorded in projection
   artifacts and source review output.

### Evidence Contract

Each `PageSynthesisPlan` contains the complete selected support set. A
`DraftClaim` may reference only that selected support set.

Valid support references are:

- `ledger:<ledger_entry_id>`
- `atom:<technical_atom_id>`
- `anchor:<stable_atom_anchor>`

Each factual sentence in a rendered prose block must match exactly one
`DraftClaim.sentence`. The validator rejects factual sentences that do not have
matching draft claims.

### Validation Rules

Reject a draft when:

- A factual prose sentence has no matching `DraftClaim`.
- A `DraftClaim` uses a support reference outside the plan.
- A prose sentence copies source wording beyond the existing n-gram threshold.
- Text contains placeholders or truncation markers.
- The topic identity is weak, malformed, or produced from a broken stem.

### Rendering

`PageDraftRenderer` owns:

- final markdown structure;
- citations;
- source trail sections;
- related links;
- projection coverage entries.

Other synthesis components do not assemble final markdown.

### Artifacts

Extend projection artifacts with:

- `page-synthesis-plan.json`
- `page-draft.json`
- `page-synthesis-findings.json`

Extend projection coverage so generated prose ranges point to draft claims and
their ledger or atom support.

### Failure Policy

Failed synthesis rejects the page. The projection pipeline must not publish an
extractive fallback page for that target.

## Interfaces

```python
@dataclass(frozen=True)
class PageSynthesisPlan:
    page_id: PageId
    page_kind: PageKind
    page_family: PageFamily
    title: str
    outline: tuple[PageOutlineSection, ...]
    selected_evidence: tuple[DraftEvidenceCard, ...]
    related_links: tuple[RelatedLink, ...]
```

```python
@dataclass(frozen=True)
class PageDraft:
    page_id: PageId
    title: str
    blocks: tuple[DraftBlock, ...]
    claims: tuple[DraftClaim, ...]
```

```python
@dataclass(frozen=True)
class DraftClaim:
    claim_id: str
    sentence: str
    support_refs: tuple[DraftEvidenceRef, ...]
```

```python
@dataclass(frozen=True)
class DraftValidationResult:
    accepted: bool
    findings: tuple[PageSynthesisFinding, ...]
```

## Implementation Plan

1. Add the synthesis TDD and vocabulary entries.
2. Add synthesis domain objects and artifact serializers.
3. Build `PageSynthesisPlan` objects from existing topic, procedure, recipe,
   and collection planners.
4. Add a bounded structured draft producer that can be backed by Forge/Ollama
   and by fakes in tests.
5. Add `PageDraftValidator`.
6. Add `PageDraftRenderer`.
7. Replace high-value page renderers in staged projection with accepted
   synthesized pages.
8. Record rejected targets in synthesis findings.
9. Add tests for plan selection, validation, rendering, failure policy, and
   source-specific regression cases.
10. Update `SCHEMA.md` ingest step 5.

## Test Plan

- Unit test `PageSynthesisPlan` selection for procedure, topic, recipe, and
  collection pages.
- Unit test `PageDraftValidator` for unknown support refs, unmapped factual
  sentences, copied source phrases, placeholder text, and malformed topic
  labels.
- Unit test `PageDraftRenderer` for citations, source trails, related links, and
  projection coverage ranges.
- Unit test the failure policy: an invalid draft rejects the page and publishes
  no extractive fallback markdown.
- Integration test a Sword World character creation procedure with a fake draft
  producer.
- Integration test a JavaScript Allonge recipe page with a fake draft producer.
- Regression test that malformed labels such as `Alway` and `Bonuse` do not
  become published synthesized topic pages.

## Rollout

This is a breaking projection change. Existing `wiki/` output is disposable
generated data and can be regenerated.

Run:

```bash
uv run pytest --cov=llmwiki
uv run ruff check
uv run mypy harness/src/llmwiki
uv run llmwiki ingest raw/javascriptallonge.pdf
uv run llmwiki ingest "raw/Sword World RPG - Complete Edition.pdf"
```

## Alignment With docs/llm-wiki.md

The raw layer stays immutable. The wiki layer remains the generated,
interlinked knowledge base. The schema continues to define conventions for
model-written pages. Index and log remain harness-owned. The change improves the
ingest operation by making generated wiki pages more synthesized, auditable, and
walkable while preserving source-backed citations.
