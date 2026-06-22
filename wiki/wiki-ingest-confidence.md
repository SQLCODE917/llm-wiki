---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Ingest confidence report from 2026-06-22.
updated: 2026-06-22
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-22-122255
Source: raw/javascriptallonge.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 9

## Artifact Reuse

- pdf-extraction: reuse `/home/serdm/gits/llm-wiki/harness/cache/c98ab3e62b35ab0f` (source hash matches; fingerprint c98ab3e62b35ab0f)
- page-plan: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/javascriptallonge-5873116c6496/page-plan.json` (fingerprint matches; fingerprint 6f0e0c9957d20723)
- evidence-registry: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/javascriptallonge-5873116c6496/evidence-registry.json` (fingerprint matches; fingerprint 6f0e0c9957d20723)
- evidence-locators: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/javascriptallonge-5873116c6496/evidence-locators.json` (fingerprint matches; fingerprint 6f0e0c9957d20723)

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

### locator-stability
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none
Locators: 2916
Stable locators: 2916
Locator drift: 0
Invalid locators: 0

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
- Findings: validation-finding-e057e2bee3551e12
Claim candidates discovered: 563
Selected for model judgment: 1
Skipped by deterministic findings: 0
Skipped by cap: 562
Verdicts recorded: 1

## Findings

- INFO claim-support javascriptallonge-a-balanced-statement-about-combinators: supported: The evidence excerpts support the claim that combinators name verbs and adverbs such as doubleOf, addOne, and compose, avoiding keywords and noun names. The first excerpt explicitly states that code using combinators tends to name verbs and adverbs while avoiding keywords and noun names, which aligns directly with the claim. fingerprint=claim-support-summary-javascriptallonge-a-balanced-statement-about-combinators-1

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
