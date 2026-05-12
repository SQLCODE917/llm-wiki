---
title: JavaScript Data Types
type: concept
tags: [javascript, data types, values, expressions]
status: draft
last_updated: 2026-05-12
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L355-L355
  - js-allonge:normalized:L373-L373
  - js-allonge:normalized:L425-L425
  - js-allonge:normalized:L449-L450
  - js-allonge:normalized:L569-L569
  - js-allonge:normalized:L695-L695
  - js-allonge:normalized:L931-L931
  - js-allonge:normalized:L933-L933
  - js-allonge:normalized:L945-L945
---

# JavaScript Data Types

## Summary

JavaScript data types categorize values into primitive types (like strings, numbers, booleans) and reference types (like arrays and functions). Primitive types are immutable and compared by value, while reference types are mutable and compared by identity. Understanding these distinctions is crucial for predictable behavior in JavaScript programs.

## Source-backed details

| Claim | Evidence |
| --- | --- |
| In JavaScript, primitive values such as strings, numbers, and booleans are immutable and compared by their content rather than by identity, whereas arrays and functions are reference types that... | [js-allonge:claim_js-allonge_c001_edb2befa], [js-allonge:claim_js-allonge_c001_8e8ef6c7], [js-allonge:claim_js-allonge_c001_9306381e] |
| JavaScript implements call-by-sharing semantics where values are passed to functions by reference, but the reference itself behaves like a copy, ensuring that modifications to parameters inside a... | [js-allonge:claim_js-allonge_c002_00b76aeb], [js-allonge:claim_js-allonge_c002_e9162af7], [js-allonge:claim_js-allonge_c002_4093dabe] |
| JavaScript distinguishes between expressions and values, where all values are expressions, but not all expressions are values; expressions can combine values with operators to form new constructs,... | [js-allonge:claim_js-allonge_c000_2dd1b93f], [js-allonge:claim_js-allonge_c000_eda33c89], [js-allonge:claim_js-allonge_c001_a486ff67] |

## Why it matters

Knowing how JavaScript handles data types helps developers avoid common pitfalls related to equality checks, mutability, and function passing. It underpins core concepts like call-by-sharing and enables understanding of how values are manipulated within the language.

## Related pages

- [JavaScript Control Flow](../concepts/js-control-flow.md)
- [JavaScript Functions](../concepts/js-functions.md)

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
