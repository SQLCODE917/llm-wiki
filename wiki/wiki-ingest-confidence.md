---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Ingest confidence report from 2026-06-22.
updated: 2026-06-22
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-22-114050
Source: raw/javascriptallonge.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 8

## Artifact Reuse

- pdf-extraction: reuse `/home/serdm/gits/llm-wiki/harness/cache/c98ab3e62b35ab0f` (source hash matches; fingerprint c98ab3e62b35ab0f)
- page-plan: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/javascriptallonge-5873116c6496/page-plan.json` (fingerprint matches; fingerprint 6f0e0c9957d20723)
- evidence-registry: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/javascriptallonge-5873116c6496/evidence-registry.json` (fingerprint matches; fingerprint 6f0e0c9957d20723)

## Gates

### source-summary-quality
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none
Selected ineligible claims: 0
False source uncertainty claims: 0
Source-framing bullets: 0
Missing unit coverage: 0

### citation-syntax
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none

### evidence-registry
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 203
Evidence records: 2928

### source-range
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none

### evidence
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none

### graph
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none

### index
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none

### claim-support
- Kind: model-assisted
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: validation-finding-433c4136cb15765d, validation-finding-ff17bbca3429bcf1, validation-finding-8635f60b47e73caa, validation-finding-1f78a9d5008d6574, validation-finding-4a210660ffd86e6f
Claim candidates discovered: 563
Selected for model judgment: 5
Skipped by deterministic findings: 0
Skipped by cap: 558
Verdicts recorded: 5

## Findings

- INFO claim-support javascriptallonge-a-balanced-statement-about-combinators: supported: The evidence excerpt directly supports the claim by stating that code using combinators tends to name verbs and adverbs (like doubleOf, addOne, and compose) while avoiding language keywords and noun names, which aligns with the claim about combinators naming verbs and adverbs. fingerprint=claim-support-summary-javascriptallonge-a-balanced-statement-about-combinators-1
- INFO claim-support javascriptallonge-a-balanced-statement-about-combinators: supported: The evidence excerpt directly supports the claim by stating that one perspective is that combinators are useful when you want to emphasize what you're doing and how it fits together, which aligns with the claim about combinators emphasizing what you're doing and how it fits together. fingerprint=claim-support-summary-javascriptallonge-a-balanced-statement-about-combinators-2
- INFO claim-support javascriptallonge-a-history-lesson: supported: The evidence excerpt directly supports the claim by defining a right-variadic function as one that has one or more fixed arguments, and the rest are gathered into the rightmost argument, which aligns with the claim. fingerprint=claim-support-summary-javascriptallonge-a-history-lesson-1
- INFO claim-support javascriptallonge-a-pull-of-the-lever-prefaces: supported: The evidence excerpt directly supports the claim by stating that Café Allongé is a drink midway between an Espresso and Americano in strength, which aligns with the claim. fingerprint=claim-support-summary-javascriptallonge-a-pull-of-the-lever-prefaces-1
- INFO claim-support javascriptallonge-a-pull-of-the-lever-prefaces: supported: The evidence excerpt directly supports the claim by stating that the first method to make Café Allongé is to add a small amount of hot water to a double or quadruple Espresso Ristretto, which aligns with the claim. fingerprint=claim-support-summary-javascriptallonge-a-pull-of-the-lever-prefaces-2

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
