---
title: JavaScript Scope
type: concept
tags: [javascript, scope, lexical, block-scoped]
status: draft
last_updated: 2026-05-12
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1843-L1843
  - js-allonge:normalized:L1845-L1845
  - js-allonge:normalized:L1847-L1847
---

# JavaScript Scope

## Summary

Scope in JavaScript defines the accessibility and visibility of variables and functions within different parts of the code. It determines where variables can be referenced and how they interact with each other in nested contexts.

## Source-backed details

| Claim | Evidence |
| --- | --- |
| Blocks in JavaScript create their own lexical scope, allowing const declarations within them to be scoped locally to that block. | [js-allonge:claim_js-allonge_c005_e3d14cc5] |
| Scopes in JavaScript are organized in a hierarchical manner, where inner scopes can access variables from outer scopes, enabling closure behavior through free variable references. | [js-allonge:claim_js-allonge_c005_0a2b6262] |
| Variables declared in an outer scope can be overridden or shadowed by variables with the same name declared in an inner scope. | [js-allonge:claim_js-allonge_c005_cb5e23e6] |

## Why it matters

Understanding scope is crucial for managing variable access, preventing naming conflicts, and writing predictable code. It enables features like closures and helps control the lifetime and visibility of variables.

## Related pages

- [JavaScript Variables](../concepts/js-variables.md)
- [JavaScript Functions](../concepts/js-functions.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)

## Candidate pages

- JavaScript Closures (not created yet)
