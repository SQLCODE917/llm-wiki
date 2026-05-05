---
title: Variables
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Variables

In JavaScript, variables declared with `var` are function-scoped rather than block-scoped, meaning they are accessible throughout the entire function in which they are declared, unlike `let` and `const` which are block-scoped. Additionally, `var` declarations are hoisted to the top of their function scope, behaving as if they were declared at the beginning of the function regardless of where they appear in the code.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Var declarations are function-scoped, not block-scoped, similar to function declarations | "First, var is not block scoped, it's function scoped, just like function declarations:" | `normalized:L4931` | [Source](../sources/js-allonge.md) |
| Var declarations behave as if they were hoisted to the top of the function | "All var declarations behave as if they were hoisted to the top of the function, a little like function declarations." | `normalized:L4941` | [Source](../sources/js-allonge.md) |
| Using var in loops can lead to closures capturing the loop variable, causing unexpected behavior | "The error wouldn't exist at all if we'd used let in the first place" | `normalized:L5092` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding that `var` is function-scoped and hoisted helps prevent common bugs in JavaScript, especially when working with loops and closures. Because `var` doesn't respect block boundaries, using it in loops can cause closures to capture the same variable reference, leading to unexpected results where all callbacks refer to the final value of the loop variable instead of the value at the time the callback was created.

## Source pages

- [Source](../sources/js-allonge.md)