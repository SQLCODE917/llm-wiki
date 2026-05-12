---
title: JavaScript Data Types
type: concept
tags: [javascript, data types, primitives, reference types]
status: draft
last_updated: 2026-05-12
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L397-L397
  - js-allonge:normalized:L405-L405
  - js-allonge:normalized:L425-L425
  - js-allonge:normalized:L451-L451
  - js-allonge:normalized:L931-L931
  - js-allonge:normalized:L933-L933
  - js-allonge:normalized:L943-L943
---

# JavaScript Data Types

## Summary

JavaScript data types are categorized into primitive and reference types. Primitive types include strings, numbers, booleans, null, undefined, and symbols, while reference types include objects, arrays, and functions. Understanding these distinctions is crucial for managing memory, equality checks, and value copying in JavaScript programs.

## Source-backed details

| Claim | Evidence |
| --- | --- |
| JavaScript distinguishes between primitive and reference types, where primitives are immutable and copied when assigned, while references are shared through pointers. | [js-allonge:claim_js-allonge_c002_d51582f6], [js-allonge:claim_js-allonge_c002_fd5ac43e], [js-allonge:claim_js-allonge_c002_2afb0230] |
| Primitive values such as strings, numbers, and booleans are identical if they have the same content, whereas reference types like arrays and functions are unique instances even if they appear... | [js-allonge:claim_js-allonge_c001_16a66e98], [js-allonge:claim_js-allonge_c001_c56d9628] |
| JavaScript evaluates expressions differently based on whether they produce primitive or reference values, with primitives being compared by value and references by identity. | [js-allonge:claim_js-allonge_c000_9ac26230], [js-allonge:claim_js-allonge_c000_176a1ef4] |

## Why it matters

Knowing the difference between primitive and reference types helps developers avoid common pitfalls such as unexpected mutations, incorrect equality comparisons, and issues with passing values to functions. It also informs decisions about how to properly manage state and data flow in applications.

## Related pages

- [JavaScript Control Flow](../concepts/js-control-flow.md)
- [JavaScript Functions](../concepts/js-functions.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
