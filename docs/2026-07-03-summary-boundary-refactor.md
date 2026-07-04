# Summary Boundary Refactor

## Context & Problem

`DraftEvidenceCard` stores a `summary` today.
The page draft path renders that `summary` as factual prose.
This lets lossy route text become wiki knowledge.

Glossary:

- `EvidenceItem`: a non-lossy source support item for page draft work.
- `NavigationSummary`: lossy text for navigation only.
- `PageEvidenceSet`: the evidence items selected for one page.
- `PageDraft`: structured page prose and claim records.

## Goals

- Use full source text or atom payloads as page draft input.
- Keep summaries for navigation, routing, logs, and previews.
- Reject drafts that reuse navigation text as factual prose.
- Render technical atom payloads in reader-facing pages.
- Keep section reference pages source-close.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not replace PDF extraction.
- This design does not replace the claim ledger.
- This design does not add migration support for old artifacts.
- This design does not make section reference pages abstractive.

Forbidden approaches:

- Do not render a lossy summary as factual page prose.
- Do not publish a fallback page when synthesis fails.
- Do not use subject, predicate, and object summaries as draft sentences.
- Do not hide technical atom payloads behind atom identifiers.

## Requirements

- `PageSynthesisPlan` contains a `PageEvidenceSet`.
- `PageEvidenceSet` contains only non-lossy evidence items.
- Each evidence item contains full source text or full atom payload text.
- Each draft claim references evidence from the selected page evidence set.
- The validator rejects support references outside the page evidence set.
- The validator rejects prose that equals a navigation summary.
- The renderer cites the support references on each accepted draft claim.
- The renderer displays atom payload text for atom evidence.
- A Forge/Ollama draft producer can be installed explicitly for page synthesis.

## Invariants

- Raw sources stay immutable.
- The claim ledger remains the evidence authority.
- Section reference pages stay source-close.
- Index and log files stay harness-owned.
- Generated wiki data remains disposable.

## Proposed Architecture

```text
RawSource -> ClaimLedger -> EvidenceBlock -> PageEvidenceSet
                                  |
TechnicalAtom --------------------+
                                  v
                           PageSynthesisPlan
                                  v
                              PageDraft
                                  v
                           RenderedWikiPage
                                  v
                         NavigationSummary
```

`RawSource` stores immutable source documents.
`ClaimLedger` stores extracted claim and atom authority.
`EvidenceBlock` stores coherent source text for selected claims.
`PageEvidenceSet` selects non-lossy support for one page.
`PageSynthesisPlan` combines page identity, outline, and evidence.
`PageDraft` stores model prose and claim support refs.
`RenderedWikiPage` stores accepted markdown and coverage.
`NavigationSummary` stores lossy preview text for navigation.

## Key Interactions

Draft page:

```text
planner -> evidence blocks: select full source text
planner -> atoms: select payload text
planner -> page plan: attach evidence set
draft producer -> page plan: write draft claims
validator -> page plan: verify support refs
renderer -> page draft: render accepted markdown
```

Build navigation:

```text
renderer -> wiki page: produce accepted body
navigation builder -> wiki page: derive summary
source manifest -> navigation summary: render preview
related links -> related preview: render relation
```

Reject bad summary prose:

```text
draft producer -> page draft: emits navigation text
validator -> page plan: compare navigation summaries
validator -> findings: record blocking finding
projection -> staged pages: omit rejected page
```

## Data Model

`EvidenceSupportRef` identifies selected support.
The support kind is `ledger`, `atom`, `anchor`, or `evidence-block`.

`PageEvidenceItem` stores one selected support item.
It stores support ref, citation, section label, source range ids, source text,
ledger entry ids, and technical atom id.

`PageEvidenceSet` stores all evidence items for one page.

`NavigationSummary` stores a target page id, summary text, summary kind, and
page body hash.

`RelatedLinkPreview` stores target page id, relation text, preview text, and
shared support refs.

## APIs / Interfaces

`PageSynthesisPlan.selected_evidence` is replaced by
`PageSynthesisPlan.evidence_set`.

`PageEvidenceItem` is the only item type that a draft claim can cite.

`NavigationSummary` text is not valid support for a draft claim.

## Behavior & Domain Rules

The planner builds evidence items from evidence blocks.
Example: a Shade evidence item contains the full sentence about disintegration.

The planner builds atom evidence items from atom payloads.
Example: an atom item contains `Distance=20 meters`.

The validator rejects clipped draft prose.
Example: `The shade is also very fragile and will easily.` is blocking.

The validator rejects navigation text as factual prose.
Example: an index preview cannot satisfy a draft claim.

The renderer renders atom payloads.
Example: a topic page shows `Distance=20 meters`, not only an atom id.

## Acceptance Criteria

- No page synthesis plan JSON contains selected evidence `summary` fields.
- The Shade topic plan contains full Shade source text.
- The Shade topic page contains no clipped summary fragment.
- A draft with a Shade clipped fragment is rejected.
- A draft with navigation summary prose is rejected.
- Related links include readable previews.
- Atom evidence renders payload text.
- `uv run llmwiki ingest --write-human-articles <source>` uses the
  Forge/Ollama article writer instead of the rejection-only writer.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

Artifact compatibility does not apply.
The repository treats generated artifacts as disposable.

Validation findings remain blocking for rejected synthesized pages.
Rejected pages must appear in synthesis findings.

## Reference Implementations

- Evidence blocks: `harness/src/llmwiki/domain/ledger/evidence_blocks.py`
- Page synthesis: `harness/src/llmwiki/domain/ledger/page_synthesis.py`
- Source manifest navigation: `harness/src/llmwiki/domain/ledger/source_manifest_navigation.py`

## Alternatives Considered

- Keep summaries and add grammar checks: rejected because summaries stay on the prose path.
- Render exact ledger text as fallback: rejected because failed synthesis must not publish fallback pages.
- Keep old artifact fields: rejected because generated state has no compatibility contract.

## Halt Conditions

- Stop if implementation requires raw source mutation.
- Stop if implementation requires migration support for old wiki data.
- Stop if section reference pages must become abstractive pages.
