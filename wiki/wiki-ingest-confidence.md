---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Ingest confidence report from 2026-06-22.
updated: 2026-06-22
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-22-153701
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
- Findings: validation-finding-f9abc9e272133c02, validation-finding-969c5bdef055f6bb, validation-finding-3c3c2f7adc428b54, validation-finding-e8d5a3c2d46b8ec3, validation-finding-4c613d201d9219c1
Claim candidates discovered: 232
Selected for model judgment: 5
Skipped by deterministic findings: 0
Skipped by cap: 227
Verdicts recorded: 5

## Findings

- INFO claim-support sword-world-rpg-complete-edition-1-3-skills: supported: The evidence excerpts support the claim that skills describe character characteristics with greater impact than ability scores. Specifically, evidence-3fe8f57a611b44c8 states "Skills have a greater impact on a character's actions than ability scores," which directly supports the claim. Additionally, evidence-2d1f90851068b610 mentions that skills are used alongside ability scores to describe character characteristics, reinforcing the importance of skills. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-3-skills-1
- INFO claim-support sword-world-rpg-complete-edition-1-3-skills: supported: The evidence excerpts support the claim that adventurer skills are for player characters with eight available skills. Evidence-fea1fd9e868304f2 explicitly lists the eight skills: fighter, thief, priest, sorcerer, shaman, sage, ranger, and bard. Additionally, evidence-ebc4f774c747baf8 confirms that adventurer skills are acquired by player characters, which aligns with the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-3-skills-2
- INFO claim-support sword-world-rpg-complete-edition-1-3-skills: supported: The evidence excerpts support the claim that instead of saying 'someone who has the fighter skill', they are simply called 'fighters'. Evidence-d0fe589931c98bd3 directly states "So instead of _someone who has the fighter skill_ , they are simply called _fighters_." This provides clear support for the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-3-skills-3
- INFO claim-support sword-world-rpg-complete-edition-1-4-character-creation-part-1: supported: The evidence excerpts support the claim that players choose a race, such as human, dwarf, grassrunner, elf, or half-elf, each with unique traits and limitations. Evidence-dfb33dc7a693080e lists the five types of races to choose from: human, dwarf, grassrunner, elf, and half-elf. Furthermore, evidence-3b533389208d4240 explicitly states that each race has their own characteristics and limitations. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-4-character-creation-part-1-1
- INFO claim-support sword-world-rpg-complete-edition-1-4-character-creation-part-1: supported: The evidence excerpts support the claim that each race has specific ability score averages, with humans having the most average scores. Evidence-00911a2a54112302 states that "Humans have the most average ability scores and can do almost anything without a hitch." Additionally, evidence-e6b671c58262e675 refers to a table showing average ability scores by race, which supports the idea that each race has specific averages. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-4-character-creation-part-1-2

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
