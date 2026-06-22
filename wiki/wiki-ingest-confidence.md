---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Ingest confidence report from 2026-06-22.
updated: 2026-06-22
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-22-145613
Source: raw/Sword World RPG - Complete Edition.pdf
Confidence status: passed with warnings
Blockers: 0
Warnings: 1
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
- Findings: validation-finding-a51dc29d9c93f520, validation-finding-a3060a3abbcd436e, validation-finding-6a64aef4e04eeea5, validation-finding-da5534f1b1766944, validation-finding-eb4031974105639d
Claim candidates discovered: 232
Selected for model judgment: 5
Skipped by deterministic findings: 0
Skipped by cap: 227
Verdicts recorded: 5

## Findings

- WARNING source-summary: Selected source-summary claims include ineligible claims. Count: 3.
- INFO claim-support sword-world-rpg-complete-edition-1-3-skills: supported: The evidence excerpts support the claim that skills describe character characteristics with greater impact than ability scores. Specifically, evidence-3fe8f57a611b44c8 states "Skills have a greater impact on a character's actions than ability scores," and evidence-2d1f90851068b610 mentions that skills are used alongside ability scores to describe character characteristics. The excerpts collectively support the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-3-skills-1
- INFO claim-support sword-world-rpg-complete-edition-1-3-skills: supported: The evidence excerpts support the claim that adventurer skills are for player characters with eight available: fighter, thief, priest, sorcerer, shaman, sage, ranger, and bard. Evidence-fea1fd9e868304f2 explicitly lists these eight skills, and evidence-ebc4f774c747baf8 confirms that adventurer skills are acquired by player characters. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-3-skills-2
- INFO claim-support sword-world-rpg-complete-edition-1-3-skills: supported: The evidence excerpts support the claim that instead of saying 'someone who has the fighter skill', they are simply called 'fighters'. Evidence-d0fe589931c98bd3 directly states "So instead of _someone who has the fighter skill_, they are simply called _fighters_." This supports the claim directly. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-3-skills-3
- INFO claim-support sword-world-rpg-complete-edition-1-4-character-creation-part-1: supported: The evidence excerpts support the claim that players choose a race, such as human, dwarf, grassrunner, elf, or half-elf, each with unique traits and limitations. Evidence-dfb33dc7a693080e lists these five races, and evidence-3b533389208d4240 states that each race has their own characteristics and limitations. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-4-character-creation-part-1-1
- INFO claim-support sword-world-rpg-complete-edition-1-4-character-creation-part-1: supported: The evidence excerpts support the claim that each race has specific ability score averages, with humans having the most average scores. Evidence-00911a2a54112302 explicitly states that "Humans have the most average ability scores and can do almost anything without a hitch," and evidence-e6b671c58262e675 refers to a table showing average ability scores by race. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-4-character-creation-part-1-2

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
