---
title: Variables in JavaScript
type: concept
tags: [javascript, scope, declaration]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4931-L4931
  - js-allonge:normalized:L4941-L4942
  - js-allonge:normalized:L5092-L5092
---

# Variables in JavaScript

## Summary

Variables in JavaScript are containers for storing data values. The behavior of variables differs based on how they are declared, particularly with respect to scoping and hoisting.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| The var keyword creates variables that are function-scoped rather than block-scoped, meaning they are accessible throughout the entire function regardless of where they are declared. | "First, var is not block scoped, it's function scoped, just like function declarations:" | `normalized:L4931-L4931` | [Source](../sources/js-allonge.md) |
| All variable declarations made with var are effectively moved to the top of their containing function during the compilation phase, a behavior known as hoisting. | "All var declarations behave as if they were hoisted to the top of the function, a little like function declarations." | `normalized:L4941-L4942` | [Source](../sources/js-allonge.md) |
| Using let instead of var can prevent certain types of errors related to variable scope, particularly in scenarios involving loops and conditional blocks where var might cause unexpected behavior. | "The error wouldn't exist at all if we'd used let in the first place" | `normalized:L5092-L5092` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding variable scoping and hoisting is crucial for writing predictable JavaScript code. Misunderstanding these concepts can lead to unexpected behavior and bugs, especially when using 'var' declarations.

## Related pages

- [Closures](../concepts/closures.md)
- [Data Types](../concepts/data-types.md)
- [Functions](../concepts/functions.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
