---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Ingest confidence report from 2026-06-22.
updated: 2026-06-22
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-22-130124
Source: raw/Sword World RPG - Complete Edition.pdf
Confidence status: failed
Blockers: 1
Warnings: 1
Gates: 9

## Artifact Reuse

- pdf-extraction: reuse `/home/serdm/gits/llm-wiki/harness/cache/e5870dca757ef182` (source hash matches; fingerprint e5870dca757ef182)
- page-plan: rebuild `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/page-plan.json` (fingerprint is missing or invalid; fingerprint ce63a70c73916c37)
- evidence-registry: missing `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/evidence-registry.json` (artifact is missing; fingerprint ce63a70c73916c37)
- evidence-locators: missing `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/evidence-locators.json` (artifact is missing; fingerprint ce63a70c73916c37)

## Gates

### source-summary-quality
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: fail
- Findings: validation-finding-809aee6479c8af75
Selected ineligible claims: 3
False source uncertainty claims: 0
Source-framing bullets: 0
Missing unit coverage: 0

### citation-syntax
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none

### evidence-registry
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 70
Evidence records: 12557

### locator-stability
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none
Locators: 11556
Stable locators: 11556
Locator drift: 0
Invalid locators: 0

### source-range
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none

### evidence
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none

### graph
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none

### index
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none

### claim-support
- Kind: model-assisted
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: fail
- Findings: validation-finding-5b1dce2824a5d2ae
Claim candidates discovered: 329
Selected for model judgment: 1
Skipped by deterministic findings: 0
Skipped by cap: 328
Verdicts recorded: 1

## Findings

- WARNING source-summary: Selected source-summary claims include ineligible claims. Count: 3.
- BLOCKER claim-support sword-world-rpg-complete-edition-1-3-skills: not_supported: The provided evidence excerpts do not support the claim that "Skill levels 0‑10 outrank ability scores, shaping actions." The excerpts discuss skill types, racial characteristics, and basic descriptions of half-elves, but none address the ranking or relationship between skill levels and ability scores. The claim introduces a concept not present in the evidence. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-3-skills-1

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
