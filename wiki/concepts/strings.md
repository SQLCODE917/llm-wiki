---
title: Strings
type: concept
tags: [javascript, syntax, literals]
status: draft
last_updated: 2026-05-11
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4621-L4621
  - js-allonge:normalized:L4641-L4641
  - js-allonge:normalized:L4649-L4649
---

# Strings

## Summary

Strings in JavaScript are sequences of characters used to represent text. They can be created using literal syntax or quasi-literals, which allow for interpolation of expressions within the string.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Quasi-literals in JavaScript enable embedding expressions within string templates using the ${} syntax, allowing dynamic value insertion. | "Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this "unquoting," the more contemporary term is "interpolation." An unquoted..." | `normalized:L4621-L4621` | [Source](../sources/js-allonge.md) |
| Quasi-literals offer better readability compared to traditional string concatenation and are less prone to errors. | "However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid..." | `normalized:L4641-L4641` | [Source](../sources/js-allonge.md) |
| Expressions within quasi-literals are evaluated at runtime, ensuring that the interpolated values reflect the current state of variables. | "Like any other expression, quasi-literals are evaluated _late_ , when that line or lines of code is evaluated." | `normalized:L4649-L4649` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding string literals and quasi-literals is essential for writing readable and maintainable JavaScript code. Quasi-literals provide a powerful way to construct strings dynamically while maintaining clarity.

## Related pages

- [Arrays](../concepts/arrays.md)
- [Control Flow](../concepts/control-flow.md)
- [ES6 Features](../concepts/es6-features.md)
- [Functional Programming](../concepts/functional-programming.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)
- [Objects](../concepts/objects.md)
- [Recursion](../concepts/recursion.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
