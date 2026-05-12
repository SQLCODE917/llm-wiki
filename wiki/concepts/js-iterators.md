---
title: JavaScript Iterators
type: concept
tags: [javascript, iteration, functional-programming]
status: draft
last_updated: 2026-05-12
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L3931-L3931
  - js-allonge:normalized:L4005-L4005
  - js-allonge:normalized:L4027-L4027
---

# JavaScript Iterators

## Summary

JavaScript iterators are objects that provide a sequence of values, typically used to traverse collections. They enable lazy evaluation and composition of operations without immediately computing all results.

## Source-backed details

| Claim | Evidence |
| --- | --- |
| An iterator is a function that can be repeatedly called to retrieve elements from a collection, returning a done flag when exhausted. | [js-allonge:claim_js-allonge_c010_774eb80c] |
| Iterator operations such as mapping and filtering can be composed to build complex transformations while maintaining memory efficiency. | [js-allonge:claim_js-allonge_c010_87dbec9f] |
| Iterator-based operations are stateful, meaning that transformations like take() modify the underlying iterator's state rather than creating independent copies. | [js-allonge:claim_js-allonge_c010_e2809678] |

## Why it matters

Iterators allow for efficient processing of large datasets by evaluating values on-demand. They support functional programming patterns like mapping and filtering, and enable stateful transformations that maintain context across iterations.

## Related pages

- [JavaScript Arrays](../concepts/js-arrays.md)
- [JavaScript Functions](../concepts/js-functions.md)
- [JavaScript Functional Programming](../concepts/js-functional-programming.md)
- [JavaScript Control Flow](../concepts/js-control-flow.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
