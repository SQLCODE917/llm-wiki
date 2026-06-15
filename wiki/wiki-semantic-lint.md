---
category: synthesis
summary: Semantic lint report from 2026-06-15.
updated: 2026-06-15
---

# Semantic Lint

## Audit Scope

Candidate items discovered: 74
Audited items: 2
Skipped by cap: 72
Max items: 2

## Findings

### Finding 1: stale_claim

- Pages: [[partial-application]]
- Rationale: The page [[partial-application]] contains a stale claim about the implementation of partial application. It mentions `callFirst(fn, larg)` as an example of partial application, but the implementation details in [[javascriptallonge-recipes-with-basic-functions]] show that `callFirst` is part of a broader set of partial application techniques (callFirst, callLast, callLeft, callRight) without explicitly defining `callFirst` as a standalone function. The example in [[partial-application]] is not directly supported by the source material.
- Evidence consulted: [[javascriptallonge-recipes-with-basic-functions]], [[partial-application]]
- Recommended action: Review the implementation examples in [[partial-application]] to ensure they align with the source material in [[javascriptallonge-recipes-with-basic-functions]]. The example for `callFirst` should be either removed or verified against the actual source code.

### Finding 2: stale_claim

- Pages: [[unary-functions]]
- Rationale: The page [[unary-functions]] contains a stale claim about the `unary` decorator. It includes an example implementation that is not directly supported by the source material in [[javascriptallonge-recipes-with-basic-functions]]. The example shows `const unary = (fn) => fn.length === 1 ? fn : something => fn.call(this, something);` which is not consistent with the explanation provided in the source material.
- Evidence consulted: [[javascriptallonge-recipes-with-basic-functions]], [[unary-functions]]
- Recommended action: Verify the implementation of the `unary` decorator in [[unary-functions]] against the source material. Ensure that the example code aligns with the explanation and implementation in [[javascriptallonge-recipes-with-basic-functions]].

## Model Report

Audited 2 items for semantic linting. Found 2 stale claims in the pages [[partial-application]] and [[unary-functions]] that need review to ensure alignment with the source material in [[javascriptallonge-recipes-with-basic-functions]]. No edits were made; findings are reported for curator review.

## Uncertainty

This is a bounded semantic lint pass over selected leads, not proof that the wiki has no stale claims or data gaps.
