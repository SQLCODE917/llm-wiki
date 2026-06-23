---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Ingest confidence report from 2026-06-22.
updated: 2026-06-22
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-22-223001
Source: raw/Sword World RPG - Complete Edition.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 10

## Artifact Reuse

- page-plan: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/page-plan.json` (fingerprint matches; fingerprint 3cd7db7a3811ef0e)
- evidence-registry: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/evidence-registry.json` (fingerprint matches; fingerprint 3cd7db7a3811ef0e)
- evidence-locators: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/evidence-locators.json` (fingerprint matches; fingerprint 3cd7db7a3811ef0e)
- technical-atoms: reuse `/home/serdm/gits/llm-wiki/harness/cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/technical-atoms.json` (fingerprint matches; fingerprint 3cd7db7a3811ef0e)

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

### technical-atoms
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none
Technical atoms: 552
- exception: 53
- formula: 293
- procedure: 20
- requirement: 31
- table-row: 142
- worked-example: 13

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
- Findings: validation-finding-f44789d089e82348
Claim candidates discovered: 784
Selected for model judgment: 1
Skipped by deterministic findings: 0
Skipped by cap: 783
Verdicts recorded: 1
Sample strategy: stratified
Sampled candidates: 1/784
Page coverage: 1/69
Source-bucket coverage: 1/18
Candidate kinds:
- prose-line: 0/2
- source-summary: 1/230
- technical-atom: 0/552
Risk tags:
- limitation: 0/68
- mechanism: 1/110
- negative-evidence: 0/58
- procedure: 1/35
- quantitative: 1/403
- requirement: 1/80
- unclassified: 0/221

## Findings

- INFO claim-support sword-world-rpg-complete-edition-13-2-7-animals-part-2: supported: The evidence excerpts fully support the claim. Excerpt evidence-672d9da4f629f13f directly states that anyone hit by a giant ant soldier will have their wound burned by the acid and must make a life force resistance roll, with failure resulting in damage from a strike power 10 strike roll plus bonus damage 4. Excerpt evidence-e4d3a73136741536 confirms that giant ant soldiers are soldier ants raised on a special diet to protect the giant ant queen. Excerpt evidence-5e38c4a31c149e9d provides the attack points and special abilities, including the toxicity score, strike power 10, and bonus damage 4. Excerpt evidence-86e81f7cfb125b2b confirms that the soldier's fangs secrete a highly toxic acid. fingerprint=claim-support-summary-sword-world-rpg-complete-edition-13-2-7-animals-part-2-3

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
