---
title: Variables
type: concept
tags: [javascript, scope, declaration]
status: draft
last_updated: 2026-05-06
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4931-L4931
  - js-allonge:normalized:L4941-L4942
  - js-allonge:normalized:L5092-L5092
---

# Variables

## Summary

Variables in JavaScript are containers for storing data values. Their behavior is influenced by how they are declared, particularly with respect to scope and hoisting.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| The var keyword creates variables that are scoped to the entire function rather than to blocks, unlike modern alternatives such as let and const. | "var is not block scoped, it's function scoped, just like function declarations:" | `normalized:L4931-L4931` | [Source](../sources/js-allonge.md) |
| All variable declarations made with var are effectively moved to the beginning of their containing function during execution, a behavior known as hoisting. | "All var declarations behave as if they were hoisted to the top of the function, a little like function declarations." | `normalized:L4941-L4942` | [Source](../sources/js-allonge.md) |
| Using let instead of var can prevent certain runtime errors related to variable access before declaration, which occur because let introduces a temporal dead zone. | "The error wouldn't exist at all if we'd used let in the first place" | `normalized:L5092-L5092` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding variable scoping and hoisting is crucial for avoiding common pitfalls in JavaScript, such as unexpected behavior due to function-scoped variables or temporal dead zones when using let and const.

## Related pages

- [Functional Programming](../concepts/functional-programming.md)
- [Functions](../concepts/functions.md)
- [Objects](../concepts/objects.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
