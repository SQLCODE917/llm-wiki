# Atomic Local Ingest and Audit Flow

This document is the source of truth for growing the wiki with local models that run on a single 4090-class GPU.

The goal is an auditable wiki, not fast-looking summaries. A page is acceptable only when its reusable claims are backed by exact source excerpts and locators, and when a small judge task has had a chance to flag claims that are too broad, unsupported, or unclear.

## Principles

1. Use local models for small bounded jobs.
2. Let deterministic tools handle syntax, links, evidence lookup, source locators, allowed paths, and report generation.
3. Use model judgment only where deterministic checks cannot decide meaning.
4. Treat the human curator as the final authority, but escalate to the human only after deterministic checks and local model judging have narrowed the issue.
5. Do not adopt generated pages into the main wiki until validation and judging pass.

## Atomic Work Units

The reliable unit for local synthesis is one source page or one synthesized page, not a whole source-to-wiki expansion.

### Unit A: Source Page

Input:
- one normalized source
- one target `wiki/sources/<slug>.md`

Output:
- source page only
- key claims
- natural groupings
- candidate related pages

Validation:
- `pnpm wiki:check-source <slug> --require-claim-evidence --normalized-source <normalized-source>`
- optional source grounding flags

### Unit B: Evidence Bank

Input:
- normalized source
- selected candidate page path

Output:
- exact evidence snippets
- normalized line locators

Validation:
- deterministic extraction only
- no model needed

Command:

```bash
pnpm wiki:evidence-bank <normalized-source> <candidate-path>
```

### Unit C: Single Synthesized Page

Input:
- source page
- selected candidate page
- evidence bank for that candidate

Output:
- exactly one synthesized page
- source page related row updated for that page

Validation:
- `pnpm wiki:link-related <slug>`
- `pnpm wiki:fix-links <slug>`
- `pnpm wiki:normalize-ascii <slug>`
- `pnpm wiki:normalize-tables <slug>`
- `pnpm wiki:check-synthesis <slug>`
- `pnpm wiki:grounding:check`

### Unit D: Claim Judge

Input:
- one synthesized page
- its source-backed claim rows
- exact evidence excerpts
- line-located source context
- brief summaries of sibling pages from the same source

Output:
- a judge report with page-level and claim-level verdicts

Verdicts:
- `supported`
- `too_broad`
- `not_supported`
- `unclear`

Validation:
- deterministic report parsing
- optional failure if any claim is not `supported`

Command:

```bash
pnpm wiki:judge-claims wiki/concepts/example.md --normalized-source raw/normalized/<slug>/source.md --candidate local-4090 --fail-on-issues
```

### Unit E: Repair

Input:
- failing deterministic validation output or claim judge report
- only the failing page or failing claim rows

Output:
- repaired page

Validation:
- rerun the deterministic checks
- rerun the judge on repaired rows or the repaired page

## Adoption Gate

A synthesized page is eligible for adoption only when all are true:

1. It passes deterministic synthesis validation.
2. It has exact evidence quotes and locator ranges.
3. The local judge marks each important claim as `supported`.
4. The local judge does not mark the page as `duplicate_or_overlap` or `unclear`.
5. Any remaining ambiguity has been escalated to the human curator.

## Deterministic Responsibilities

Deterministic tools should check:

- required frontmatter
- required headings
- allowed changed-file scope
- related-page path shape
- broken Markdown links
- source back-links
- exact evidence table shape
- evidence quote appears in normalized source
- evidence quote appears in cited locator range
- source-page key claims have exact evidence and normalized locators
- reference-page lookup rows have exact evidence and normalized locators
- page-type sections, such as `## Steps` and `## Reference data`
- placeholder text such as `Page title`
- obvious malformed table rows
- index and graph freshness
- grounding report

## Local Judge Responsibilities

The local judge should decide:

- whether each claim follows from its evidence
- whether a claim is too broad for its evidence
- whether a claim needs qualification
- whether the page appears useful as a reusable wiki page
- whether the page appears to overlap heavily with sibling pages
- whether the strongest local evidence is missing or the evidence is weak

The judge must not rewrite files. It only produces a report.

## Human Escalation

Escalate to the human curator when:

- the judge returns `unclear`
- multiple sources contradict each other
- the page may be useful but overlaps another page
- the model and deterministic checks disagree after one repair
- a claim seems strategically important but the source support is ambiguous

## Recommended 4090 Operating Mode

For local models such as `local-4090`, use this default loop:

1. Phase 1 source page.
2. Select one candidate page.
3. Generate evidence bank for that one page.
4. Create or repair exactly that one page with `pnpm wiki:phase2-single <slug> <candidate-path>`.
5. Run deterministic checks and normalizers.
6. Run `wiki:judge-claims` with `local-4090`.
7. Repair only flagged rows.
8. Rerun checks and judge.
9. Adopt and finalize only after the page passes.

This is slower than asking for many pages at once, but it is much more reliable and audit-friendly.
