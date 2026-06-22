---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Ingest confidence report from 2026-06-22.
updated: 2026-06-22
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-22-160544
Source: raw/Sword World RPG - Complete Edition.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 9

## Artifact Reuse

- pdf-extraction: reuse `/home/serdm/gits/llm-wiki/harness/cache/e5870dca757ef182` (source hash matches; fingerprint e5870dca757ef182)
- page-plan: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/page-plan.json` (fingerprint matches; fingerprint fc7995e6a6e90887)
- evidence-registry: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/evidence-registry.json` (fingerprint matches; fingerprint fc7995e6a6e90887)
- evidence-locators: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/evidence-locators.json` (fingerprint matches; fingerprint fc7995e6a6e90887)

## Gates

### source-summary-quality
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none
Selected ineligible claims: 0
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
Evidence records: 7913

### locator-stability
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none
Locators: 7425
Stable locators: 7425
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
- Status: pass
- Findings: validation-finding-344a39e29774c506, validation-finding-f6bab2b8410b177c, validation-finding-ed3b00f59f592c4f, validation-finding-fd49914ee1805e5d, validation-finding-9629f91469956e22
Claim candidates discovered: 232
Selected for model judgment: 5
Skipped by deterministic findings: 0
Skipped by cap: 227
Verdicts recorded: 5
Sample strategy: stratified
Sampled candidates: 5/232
Page coverage: 5/69
Source-bucket coverage: 4/18
Candidate kinds:
- prose-line: 1/2
- source-summary: 4/230
Risk tags:
- limitation: 0/18
- mechanism: 2/22
- negative-evidence: 0/15
- procedure: 2/16
- quantitative: 3/72
- requirement: 1/29
- unclassified: 2/110

## Findings

- INFO claim-support sword-world-rpg-complete-edition-13-2-7-animals-part-2: supported: The evidence excerpts fully support the claim. Evidence-672d9da4f629f13f directly states the damage mechanics, evidence-e4d3a73136741536 confirms the special diet, and evidence-5e38c4a31c149e9d provides the relevant stats including the toxic acid and damage values. Evidence-86e81f7cfb125b2b confirms the toxic acid secretion. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-13-2-7-animals-part-2-3
- INFO claim-support sword-world-rpg-complete-edition-13-2-1-how-to-read-the-monster-catalog: supported: The evidence excerpts support the claim that the section explains how to interpret data in the monster catalog, covering formats for various monster attributes including level, rarity, agility, movement speed, number, frequency, intellect, reaction, attack points, strike points, evasion points, defense points, life points/resistance, mental points/resistance, special abilities, habitat, perception, and languages. fingerprint=claim-support-prose-sword-world-rpg-complete-edition-13-2-1-how-to-read-the-monster-catalog-3
- INFO claim-support sword-world-rpg-complete-edition-books-related-to-sword-world-rpg: supported: The evidence excerpts support that the Sword World RPG Replay Collections help understand gameplay through actual play reproductions and are based on the old rule version, which may have contradictions. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-books-related-to-sword-world-rpg-1
- INFO claim-support sword-world-rpg-complete-edition-1-3-skills: supported: The evidence excerpts support that skills describe character characteristics and have a greater impact than ability scores, with examples showing how skills determine character actions and characteristics. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-3-skills-1
- INFO claim-support sword-world-rpg-complete-edition-2-3-checks: supported: The evidence excerpts support the claim that success roll is 2D + baseline score ≥ target score, with specific examples showing how dice rolls are added to baseline scores to determine success. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-2-3-checks-3

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
