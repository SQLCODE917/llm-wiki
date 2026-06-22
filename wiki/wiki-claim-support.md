---
page_id: wiki-claim-support
page_kind: synthesis
summary: Claim support audit report from 2026-06-22.
updated: 2026-06-22
---

# Claim Support Audit

## Audit Scope

Run id: 2026-06-22-104715
Claim candidates discovered: 663
Audited candidates: 22
Selected for model judgment: 5
Skipped by deterministic findings: 17
Skipped by cap: 641
Max claims: 5

## Deterministic Findings

- BLOCKER javascriptallonge-reg-raganwald-braithwaite claim-support-summary-javascriptallonge-reg-raganwald-braithwaite-1: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-reg-raganwald-braithwaite claim-support-summary-javascriptallonge-reg-raganwald-braithwaite-2: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-reference-types claim-support-summary-javascriptallonge-reference-types-1: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-reference-types claim-support-summary-javascriptallonge-reference-types-2: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-reference-types claim-support-summary-javascriptallonge-reference-types-3: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-prelude-values-and-expressions-over-coffee claim-support-summary-javascriptallonge-prelude-values-and-expressions-over-coffee-1: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-prelude-values-and-expressions-over-coffee claim-support-summary-javascriptallonge-prelude-values-and-expressions-over-coffee-2: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-prelude-values-and-expressions-over-coffee claim-support-summary-javascriptallonge-prelude-values-and-expressions-over-coffee-3: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-value-types claim-support-summary-javascriptallonge-value-types-1: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-value-types claim-support-summary-javascriptallonge-value-types-2: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-value-types claim-support-summary-javascriptallonge-value-types-3: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-values-and-identity claim-support-summary-javascriptallonge-values-and-identity-1: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-values-and-identity claim-support-summary-javascriptallonge-values-and-identity-1: copied-evidence: Copied evidence text mismatches EvidenceRecord excerpts.
- BLOCKER javascriptallonge-values-and-identity claim-support-summary-javascriptallonge-values-and-identity-2: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-values-and-identity claim-support-summary-javascriptallonge-values-and-identity-3: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-values-and-identity claim-support-summary-javascriptallonge-values-and-identity-4: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-values-and-identity claim-support-summary-javascriptallonge-values-and-identity-5: source-range: Citation locator is outside the planned source range for this page.
- BLOCKER javascriptallonge-a-balanced-statement-about-combinators claim-support-summary-javascriptallonge-a-balanced-statement-about-combinators-3: missing-evidence: No EvidenceRecord matched.

## Verdict Totals

- supported: 3
- too_broad: 0
- not_supported: 1
- unclear: 1

## Model Verdicts

### Verdict 1: INFO - supported on claim-support-summary-javascriptallonge-a-balanced-statement-about-combinators-1

- Rationale: The evidence excerpt directly supports the claim by showing that combinators name verbs and adverbs like doubleOf, addOne, and compose, while avoiding keywords and noun names.
- Recommended action: No action needed; the evidence fully supports the claim.

### Verdict 2: INFO - supported on claim-support-summary-javascriptallonge-a-balanced-statement-about-combinators-2

- Rationale: The evidence excerpt supports the claim by stating that combinators are useful when you want to emphasize what you're doing and how it fits together.
- Recommended action: No action needed; the evidence fully supports the claim.

### Verdict 3: BLOCKER - not_supported on claim-support-summary-javascriptallonge-a-few-utilities-1

- Rationale: The evidence excerpt does not provide sufficient information to support the claim that the section introduces fundamental list manipulation utilities such as copy, first, rest, reverse, mapWith, at, and set functions. The excerpt only shows a partial code example without explicitly naming or describing these functions.
- Recommended action: The evidence needs to be expanded to explicitly mention and describe the listed utilities.

### Verdict 4: WARNING - unclear on claim-support-summary-javascriptallonge-a-history-lesson-1

- Rationale: The evidence excerpt only states "53 Another history lesson" and does not provide specific information to support or refute the claim about JavaScript not being able to gather parameters in 'Ye Olde Days.'
- Recommended action: Additional evidence is needed to clarify the historical context of JavaScript's parameter gathering capabilities.

### Verdict 5: INFO - supported on claim-support-summary-javascriptallonge-a-history-lesson-2

- Rationale: The evidence excerpt directly supports the claim by defining a right-variadic function as one that has fixed arguments with the rest gathered into the rightmost argument.
- Recommended action: No action needed; the evidence fully supports the claim.

## Model Report

Per-candidate verdict rationale and recommended action are recorded above. The free-form finish note is omitted so structured tool-call verdicts remain authoritative.

## Caveat

This is a bounded claim-support audit over selected generated claims, not proof that every wiki claim is supported.
