# TDD: Human Article Renderer

## Context & Problem

Current public pages can expose extraction fragments, atom ids, and weak related
link explanations.
The wiki needs article-shaped pages that humans can read and navigate.
The harness must own markdown rendering for all generated public articles.

Glossary:

- `HumanArticle`: structured article content for one public wiki page.
- `ArticleSection`: one section in a human article.
- `ArticleClaim`: one factual sentence in a human article.
- `ArticleCitation`: one citation from an article claim to a support ref.
- `ArticleRenderer`: the component that writes markdown from a human article.
- `EvidencePack`: the selected source support for one planned page.
- `NavigationSummary`: reader-facing preview text from an accepted wiki page.

## Goals

- Generate structured human articles from evidence packs.
- Make article claims cite evidence pack support refs.
- Render markdown only from accepted human articles.
- Render related links as navigation aids.
- Improve readability by removing extraction artifact prose from public pages.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not select public pages.
- This design does not extract evidence records.
- This design does not run final lint.
- This design does not preserve model-authored raw markdown pages.

Forbidden approaches:

- Do not let the model write final markdown for generated public articles.
- Do not render atom ids without payload context.
- Do not render article claims without citations.
- Do not use extraction fragments as article paragraphs.

## Requirements

- The article writer receives one evidence pack.
- The article writer returns one human article.
- Each article claim stores one factual sentence.
- Each article claim cites at least one support ref.
- The article validator checks every support ref against the evidence pack.
- The article renderer owns frontmatter, headings, citations, source trail, and
  related links.
- The renderer writes no page when article validation fails.
- Related links include reader-facing previews and shared support refs.

## Invariants

- Public generated article markdown comes from `ArticleRenderer`.
- Source support comes from evidence packs.
- `WikiStructure` renders page paths.
- `PageMetadata` remains the page identity authority.
- Raw sources stay immutable.

## Proposed Architecture

```text
EvidencePack
     |
     v
ArticleWriter
     |
     v
HumanArticle
     |
     v
ArticleValidator
     |
     v
ArticleRenderer
     |
     v
WikiPage
```

`EvidencePack` stores selected support.
`ArticleWriter` produces structured article content.
`HumanArticle` stores sections, prose, and claims.
`ArticleValidator` checks support refs and article shape.
`ArticleRenderer` serializes accepted articles to markdown.
`WikiPage` stores rendered generated state.

## Key Interactions

Write article:

```text
article writer -> evidence pack: read support
model -> article writer: return human article
article validator -> evidence pack: verify support refs
article renderer -> wiki page: render markdown
```

Render citations:

```text
article renderer -> article claim: read citation refs
article renderer -> evidence pack: read citation labels
article renderer -> markdown: write cited sentence
```

Render related links:

```text
article renderer -> page plan: read related targets
article renderer -> navigation summary: read accepted previews
article renderer -> markdown: write related links
```

## Data Model

`HumanArticle` stores page metadata, article sections, article claims, related
links, source trail items, and article findings.

`ArticleSection` stores section id, heading, prose blocks, and article claim
ids.

`ArticleClaim` stores claim id, sentence, support refs, and claim role.

`ArticleCitation` stores claim id, support ref, citation label, and source
anchor.

## APIs / Interfaces

The article writer returns `HumanArticle`.

The article renderer accepts only validated `HumanArticle` values.

The page writer accepts only markdown from `ArticleRenderer` for generated
public articles.

## Behavior & Domain Rules

The article writer uses evidence pack support.
Example: a Shade article explains the darkness rule with a citation.

The article validator rejects uncited factual sentences.
Example: `Shade is fragile` is rejected without a support ref.

The renderer shows payload context.
Example: a spell article shows `Distance=20 meters`, not only `atom:spell-1`.

The renderer renders navigation previews.
Example: a related link says what the target page helps answer.

## Acceptance Criteria

- A unit test renders frontmatter from page metadata.
- A unit test renders citations from article claims.
- A unit test rejects an article claim with an unknown support ref.
- A unit test rejects a factual sentence without an article claim.
- A unit test renders atom payload text near technical evidence.
- A unit test renders related links with previews and shared support refs.
- A Sword World Shade fixture renders complete prose sentences.
- A JavaScript Allonge recipe fixture renders code evidence as readable support.
- A page writer test proves model-authored raw markdown is not accepted for
  generated public articles.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

The renderer records article claim coverage for lint and diagnostics.

The ingest log records article validation failures.

## Reference Implementations

- Page synthesis: `harness/src/llmwiki/domain/ledger/page_synthesis.py`
- Page body contracts: `harness/src/llmwiki/domain/page_body_contracts.py`
- Wiki pages: `harness/src/llmwiki/domain/pages.py`

## Alternatives Considered

- Let the model write markdown directly: rejected because markdown is a harness
  contract.
- Render exact evidence text as article prose: rejected because public pages
  need readable synthesis.
- Hide source trails behind citations only: rejected because readers need audit
  context.

## Halt Conditions

- Stop if a generated public article must bypass `ArticleRenderer`.
- Stop if article claims cannot map to evidence pack support refs.
