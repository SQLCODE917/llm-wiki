---
title: JavaScript Values
type: concept
tags: [javascript, values, expressions]
status: draft
last_updated: 2026-05-12
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L355-L355
  - js-allonge:normalized:L373-L373
  - js-allonge:normalized:L397-L397
  - js-allonge:normalized:L403-L403
  - js-allonge:normalized:L407-L407
---

# JavaScript Values

## Summary

In JavaScript, values are the fundamental units of data that can be manipulated and expressed. Every value is also an expression, meaning it can be evaluated to produce itself. Values are compared using strict equality (===) and inequality (!==) operators, with identity determined by both type and content.

## Source-backed details

| Claim | Evidence |
| --- | --- |
| Every value in JavaScript is also an expression, which means it can be evaluated to yield itself, much like handing a specific item to a barista who returns exactly what was requested. | [js-allonge:claim_js-allonge_c000_c9c63d26] |
| While certain combinations of values form expressions, not all expressions qualify as values; for instance, the result of combining boiling water and ground coffee is an expression but not a... | [js-allonge:claim_js-allonge_c000_86d94a0e] |
| JavaScript employs the strict equality operator (===) to determine if two values are identical, taking into account both their type and content, and the inequality operator (!==) to check if they... | [js-allonge:claim_js-allonge_c000_1a1dea09] |
| When comparing values in JavaScript, differences in type (like a string versus a number) prevent them from being identical, even if their content appears similar, such as the string "2" and the... | [js-allonge:claim_js-allonge_c000_5e9b2b55] |
| Even when two values share the same type, they may still differ if their content varies, such as the numbers 5 and 2, which are of the same type but represent different values. | [js-allonge:claim_js-allonge_c000_41fbe069] |

## Why it matters

Understanding values is crucial for grasping how JavaScript handles data, performs comparisons, and evaluates expressions. It underpins concepts like immutability, function parameters, and object references.

## Related pages

- [JavaScript Data Types](../concepts/js-data-types.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)

## Candidate pages

- JavaScript Expressions (not created yet)
- JavaScript Equality (not created yet)
