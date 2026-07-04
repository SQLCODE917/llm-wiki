# TDD: Citation Readability Lint

## Context & Problem

Current lint can check links and citation shape after pages exist.
It does not fully block unreadable public prose before publication.
Generated articles need a deterministic gate for authority and coherence.

Glossary:

- `ArticleLintRun`: one lint run for generated public articles.
- `ArticleLintFinding`: one article lint issue.
- `ReadabilityFinding`: one coherence or prose quality issue.
- `CitationFinding`: one article citation issue.
- `PublicationGate`: the decision that allows or blocks page publication.
- `HumanArticle`: structured article content for one public wiki page.
- `EvidencePack`: the selected source support for one planned page.
- `RenderedMarkdown`: the markdown that would become one public wiki page.

## Goals

- Block unsupported factual prose before publication.
- Block clipped or malformed sentences before publication.
- Block unreadable technical evidence before publication.
- Block weak titles and over-budget pages before publication.
- Measure article authority and coherence in lint artifacts.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not extract evidence records.
- This design does not select source profiles.
- This design does not replace diagnostic questions.
- This design does not repair failed articles.

Forbidden approaches:

- Do not publish pages with blocking article lint findings.
- Do not trust model self-report as lint success.
- Do not treat source-backed fragments as readable prose.
- Do not let citation count alone prove article authority.

## Requirements

- The article linter reads rendered markdown, human article data, and evidence
  packs.
- The article linter verifies every article claim citation.
- The article linter verifies each factual sentence maps to one article claim.
- The article linter checks copied phrase limits.
- The article linter checks clipped fragment patterns.
- The article linter checks title findings from the page plan.
- The article linter checks related link previews.
- The publication gate blocks pages with blocking findings.
- The lint artifact records authority and coherence metrics.

## Invariants

- Public pages publish only after a publication gate accepts them.
- Evidence packs remain the article support authority.
- Raw sources stay immutable.
- Generated wiki data remains disposable.
- Deterministic lint recomputes findings after model repair.

## Proposed Architecture

```text
HumanArticle
     |
     +--> RenderedMarkdown
     |
     +--> EvidencePack
     |
     v
ArticleLinter
     |
     v
ArticleLintRun
     |
     v
PublicationGate
```

`HumanArticle` stores article claims and sections.
`RenderedMarkdown` stores the markdown that would be published.
`EvidencePack` stores selected support.
`ArticleLinter` computes findings.
`ArticleLintRun` stores findings and metrics.
`PublicationGate` accepts or rejects the article.

## Key Interactions

Lint article:

```text
article linter -> human article: read claims
article linter -> rendered markdown: read sentences
article linter -> evidence pack: verify support
article linter -> lint run: write findings
```

Block publication:

```text
publication gate -> lint run: read blocking findings
publication gate -> staged page: reject page
publication gate -> findings artifact: record reason
```

Check repair:

```text
repair loop -> article renderer: render repaired article
article linter -> repaired article: recompute findings
publication gate -> lint run: accept or reject
```

## Data Model

`ArticleLintRun` stores page id, source id, findings, authority metrics,
coherence metrics, and publication decision.

`ArticleLintFinding` stores finding id, page id, severity, finding code, source
anchor, article claim id, and message.

`ReadabilityFinding` is an article lint finding with a readability code.

`CitationFinding` is an article lint finding with a citation code.

`PublicationGate` stores page id, decision, blocking finding ids, and timestamp.

## APIs / Interfaces

The staged publisher accepts only pages with an accepted publication gate.

The lint reporter writes article lint runs to ingest artifacts.

The repair loop reads blocking article lint findings.

## Behavior & Domain Rules

The linter blocks unsupported claims.
Example: a sentence without an article claim creates a blocking citation finding.

The linter blocks clipped fragments.
Example: `If a shade itself comes into will -o-wisp's body or enters the area.`
creates a blocking readability finding.

The linter blocks unreadable evidence.
Example: a technical evidence section with only atom ids creates a blocking
readability finding.

The linter records metrics.
Example: authority coverage equals cited factual sentences divided by factual
sentences.

## Acceptance Criteria

- A unit test blocks a sentence without an article claim.
- A unit test blocks a claim with an unknown support ref.
- A unit test blocks the three known Shade clipped fragments.
- A unit test blocks a technical section that contains only atom ids.
- A unit test blocks a page with a title finding from the page plan.
- A unit test records authority coverage for a rendered page.
- A unit test records clipped sentence count for a rendered page.
- A staged publication test omits pages with blocking findings.
- A repair test proves lint recomputes findings after a draft change.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

Lint artifacts are part of ingest diagnostics.
They are not public wiki content unless a later report page cites them.

The ingest log records accepted count, rejected count, and top blocking codes.

## Reference Implementations

- Staged flow: `harness/src/llmwiki/domain/ledger/staged_flow.py`
- Citation parser: `harness/src/llmwiki/domain/citations.py`
- Claim support audit: `harness/src/llmwiki/domain/claim_support.py`

## Alternatives Considered

- Ask the model to judge readability: rejected because lint must be
  recomputable.
- Publish then lint: rejected because bad public pages become generated state.
- Use citation count as authority score: rejected because citations must map to
  evidence support.

## Halt Conditions

- Stop if the staged publisher must publish pages with blocking findings.
- Stop if lint cannot recompute without a model call.
