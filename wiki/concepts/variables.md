---
title: Variables
type: concept
tags: [javascript, scope, declaration]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4931-L4931
  - js-allonge:normalized:L4940-L4940
  - js-allonge:normalized:L4941-L4942
  - js-allonge:normalized:L5092-L5092
---

# Variables

## Summary

Variables in JavaScript are used to store data values. The behavior of variable declarations differs based on the keyword used, such as var, let, or const, particularly concerning scope and hoisting.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| The var keyword creates variables that are function-scoped rather than block-scoped, meaning they are accessible throughout the entire function regardless of where they are declared. | "var is not block scoped, it's function scoped, just like function declarations:" | `normalized:L4931-L4931` | [Source](../sources/js-allonge.md) |
| Multiple declarations of the same variable name within the same function do not result in an error, and inner declarations do not override outer ones due to the hoisting behavior of var. | "Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration." | `normalized:L4940-L4940` | [Source](../sources/js-allonge.md) |
| Multiple declarations of the same variable name within the same function do not result in an error, and inner declarations do not override outer ones due to the hoisting behavior of var. | "All var declarations behave as if they were hoisted to the top of the function, a little like function declarations." | `normalized:L4941-L4942` | [Source](../sources/js-allonge.md) |
| Using let instead of var can prevent certain errors related to variable re-declaration and scope, as let provides block-level scoping. | "The error wouldn't exist at all if we'd used let in the first place" | `normalized:L5092-L5092` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding how variables work-especially their scoping rules and hoisting behavior-is crucial for writing predictable JavaScript code. Misunderstanding these concepts can lead to unexpected behavior and bugs, especially when using var in nested scopes.

## Related pages

- [Data Types](../concepts/data-types.md)
- [Functional Programming](../concepts/functional-programming.md)
- [Iterators](../concepts/iterators.md)
- [Objects](../concepts/objects.md)
- [Recursion](../concepts/recursion.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
