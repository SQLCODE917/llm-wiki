---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Ingest confidence report from 2026-06-22.
updated: 2026-06-22
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-22-163328
Source: raw/Sword World RPG - Complete Edition.pdf
Confidence status: failed
Blockers: 2
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
- Status: fail
- Findings: validation-finding-dbd72aaca95b2924, validation-finding-cb87c20d81d3c1b0, validation-finding-271116261c1a96d5, validation-finding-b5d7380ff936f7ce, validation-finding-7c0c33cd6ef28e52, validation-finding-7b6550622166c264, validation-finding-33d95d6e57f1acaf, validation-finding-5b00af296591cd7e, validation-finding-b1fab951b7445195, validation-finding-2ed96a0ba890e964, validation-finding-93ef872a0f1b005b, validation-finding-8e166ec9a2cb316a, validation-finding-b52613316705cbca, validation-finding-825945587f215fc8, validation-finding-6df0a247a105acd3, validation-finding-fece6684926879ec, validation-finding-5e9d39dfacb173a3, validation-finding-59596d81b50cc639, validation-finding-6a267b1235f46a37, validation-finding-c77ab3fa6a3b22fb, validation-finding-54df3f9430d8dfa1, validation-finding-27fdd77988e48401, validation-finding-0e6b321b56d9b7d4, validation-finding-58e17681f48e01a7, validation-finding-d0ffc61bb9064c60
Claim candidates discovered: 232
Selected for model judgment: 25
Skipped by deterministic findings: 0
Skipped by cap: 207
Verdicts recorded: 25
Sample strategy: stratified
Sampled candidates: 25/232
Page coverage: 24/69
Source-bucket coverage: 18/18
Candidate kinds:
- prose-line: 1/2
- source-summary: 24/230
Risk tags:
- limitation: 1/18
- mechanism: 6/22
- negative-evidence: 2/15
- procedure: 7/16
- quantitative: 17/72
- requirement: 5/29
- unclassified: 3/110

## Findings

- INFO claim-support sword-world-rpg-complete-edition-13-2-7-animals-part-2: supported: The evidence excerpts fully support the claim. Evidence-672d9da4f629f13f directly states the acid burn effect and resistance roll, evidence-e4d3a73136741536 confirms the special diet, and evidence-5e38c4a31c149e9d provides the strike power and bonus damage details. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-13-2-7-animals-part-2-3
- INFO claim-support sword-world-rpg-complete-edition-13-2-1-how-to-read-the-monster-catalog: supported: The evidence excerpts support the claim that the section explains how to interpret data in the monster catalog, covering formats for monster level, rarity, agility, movement speed, number, frequency, intellect, reaction, attack points, strike points, evasion points, defense points, life points/resistance, mental points/resistance, special abilities, habitat, perception, and languages. fingerprint=claim-support-prose-sword-world-rpg-complete-edition-13-2-1-how-to-read-the-monster-catalog-3
- INFO claim-support sword-world-rpg-complete-edition-books-related-to-sword-world-rpg: supported: The evidence excerpts support the claim that the Sword World RPG Replay Collections help understand gameplay through actual play reproductions and are based on the old rule version, which may have contradictions. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-books-related-to-sword-world-rpg-1
- INFO claim-support sword-world-rpg-complete-edition-1-3-skills: supported: The evidence excerpts support the claim that skills describe character characteristics with greater impact than ability scores, as evidenced by the direct statement in evidence-3fe8f57a611b44c8 and the explanation in evidence-2d1f90851068b610. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-3-skills-1
- INFO claim-support sword-world-rpg-complete-edition-2-3-checks: supported: The evidence excerpts support the claim that a success roll is made by rolling 2D and adding the baseline score to the roll, as evidenced by evidence-32fb0d7a079d8381, evidence-3c700659884fee45, and evidence-3bec44d626fe3216. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-2-3-checks-3
- INFO claim-support sword-world-rpg-complete-edition-3-4-movement-and-actions: supported: The evidence excerpts confirm that for monsters, movement speed is set separately from agility, and they can move up to movement speed x 3 meters. This directly supports the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-3-4-movement-and-actions-4
- INFO claim-support sword-world-rpg-complete-edition-4-5-attacks-from-characters-against-monsters: supported: The evidence confirms that damage calculation involves determining base damage, adding bonus damage, and subtracting the monster's defense points, which aligns with the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-4-5-attacks-from-characters-against-monsters-2
- INFO claim-support sword-world-rpg-complete-edition-5-1-1-types-of-magic: supported: The evidence confirms that spells are divided into levels from 1-10, and higher levels require higher rune master skills, directly supporting the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-5-1-1-types-of-magic-4
- INFO claim-support sword-world-rpg-complete-edition-6-2-thief-skill: supported: The evidence explicitly states that the thief skill is taught at the thieves' guild, which directly supports the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-6-2-thief-skill-1
- INFO claim-support sword-world-rpg-complete-edition-7-2-merchant-skill: supported: The evidence confirms that the merchant skill allows adventurers to sell items in shops or on the street and includes abilities such as Value Check and Negotiation, supporting the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-7-2-merchant-skill-2
- INFO claim-support sword-world-rpg-complete-edition-8-1-experience-points: supported: The evidence excerpts confirm that the experience points required to increase each skill are shown in Table 8-1: Experience Points by Skill. The excerpts also provide specific examples and references to the table, supporting the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-8-1-experience-points-3
- INFO claim-support sword-world-rpg-complete-edition-9-2-should-you-use-a-target-score-check-or-a-difficulty-check: supported: The evidence excerpts support the claim that target scores are used for actions with clear success or failure. The excerpts explicitly mention target scores in the context of success rolls and actions with clear outcomes. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-9-2-should-you-use-a-target-score-check-or-a-difficulty-check-1
- INFO claim-support sword-world-rpg-complete-edition-10-3-surprise-attacks: supported: The evidence excerpts confirm that the game master rolls 2D and adds it to the monster level, and adventurers roll ranger skill + intelligence bonus. This matches the claim exactly. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-10-3-surprise-attacks-2
- INFO claim-support sword-world-rpg-complete-edition-11-2-dark-magic-part-1: supported: The evidence excerpts support the claim that in a narrow sense, only Phalaris priests are dark priests, and it is unknown if other wicked gods' followers exist. The excerpts confirm this by stating that believers in wicked gods other than Phalaris are rarely seen. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-11-2-dark-magic-part-1-2
- INFO claim-support sword-world-rpg-complete-edition-12-2-rules-for-poison-illness-and-infection-part-1: supported: The evidence excerpts support the claim that poisons disrupt spirit power and require detoxification. The excerpts explicitly state that poisons force an imbalance in spirit power and can be cleared using specific antidotes or magic. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-12-2-rules-for-poison-illness-and-infection-part-1-2
- INFO claim-support sword-world-rpg-complete-edition-13-1-types-of-monsters: supported: The evidence excerpts confirm that there are 12 types of monsters in Alecrast, as stated in the claim. The excerpts explicitly list these 12 types and reference Laverna's Natural History, supporting the claim that Alecrast has 12 monster types per Laverna's Natural History. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-13-1-types-of-monsters-1
- INFO claim-support sword-world-rpg-complete-edition-14-1-treasure-and-rewards-in-sword-world: supported: The evidence excerpt directly states that to determine the value (upper limit) of the treasure that can be obtained in terms of silver coins, multiply the adventurer levels of all the player characters, then multiply the total by 500. This matches the claim exactly. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-14-1-treasure-and-rewards-in-sword-world-4
- BLOCKER claim-support sword-world-rpg-complete-edition-16-1-combat-in-which-monsters-roll-dice: not_supported: The evidence excerpts describe the process for determining success rolls with monster's attack points or evasion points as difficulty, but they do not explicitly state that the target score is calculated as monster's attack points - 7, added to 2D roll. The claim is more specific than what is supported by the evidence. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-16-1-combat-in-which-monsters-roll-dice-4
- BLOCKER claim-support sword-world-rpg-complete-edition-17-2-lost-spells: not_supported: The evidence excerpts indicate that not all ancient magic spells are taught in the sorcerers' guild, and that some spells are lost with the fall of the ancient kingdom. However, they do not explicitly state that lost spells are not taught in the guild, which is the claim. The evidence is insufficient to support the claim as stated. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-17-2-lost-spells-1
- INFO claim-support sword-world-rpg-complete-edition-18-3-rules-for-destroying-structures: supported: The evidence excerpts confirm that damage calculation involves subtracting defense points from determined damage, and that if the damage exceeds the destruction points, the structure will be destroyed. This supports the claim that damage calculation subtracts defense points from damage, determining if structure is destroyed. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-18-3-rules-for-destroying-structures-4
- INFO claim-support sword-world-rpg-complete-edition-charts: supported: The evidence excerpts directly support the claim that Sage skill abilities such as Monster Check and Languages are not possible to retry. The table in evidence-e4a7784613fd4157 explicitly lists "Monster Check" and "Languages" under the "Retrying a success roll on the same target" column with "Not Possible" as the value, which aligns with the claim. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-charts-3
- INFO claim-support sword-world-rpg-complete-edition-1-4-character-creation-part-1: supported: The evidence excerpts support the claim that each race has specific ability score averages, with humans having the most average scores. Evidence-e6b671c58262e675 mentions that average ability scores are shown in a table, and evidence-00911a2a54112302 explicitly states that humans have the most average ability scores. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-1-4-character-creation-part-1-2
- INFO claim-support sword-world-rpg-complete-edition-2-7-resistance-rolls: supported: The evidence excerpts support the claim that life force resistance rolls avoid physical dangers like poison, using adventurer level + life force bonus as baseline score. Evidence-05c75303826af816 defines life force resistance rolls using adventurer level + life force bonus, and evidence-a75e40c5c08462ce states that these rolls are made to avoid physical dangers such as poison. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-2-7-resistance-rolls-1
- INFO claim-support sword-world-rpg-complete-edition-3-4-movement-and-actions: supported: The evidence excerpts support the claim that standing still allows use of magic and projectiles, with movement limited to 3 meters. Evidence-f85506a771dcba3b states that standing still allows use of magic and projectiles, and evidence-7dfb1885ffd85488 indicates that the distance you can go with full movement is character's agility x 3 meters. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-3-4-movement-and-actions-5
- INFO claim-support sword-world-rpg-complete-edition-4-9-unconscious-and-death-checks: supported: The evidence excerpts support the claim that if a character's life force becomes 0 or negative, they fall unconscious and are in danger of dying. Evidence-28be6a3a296f8ac9 states that a character falls unconscious if their life force becomes 0 or negative, and evidence-37f2747884ef9cb4 indicates that if left unconscious, they may die. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-4-9-unconscious-and-death-checks-1

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
