---
title: JavaScript Iterables
type: concept
tags: [javascript, iteration, symbol, generator]
status: draft
last_updated: 2026-05-12
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4791-L4791
  - js-allonge:normalized:L4817-L4817
  - js-allonge:normalized:L4835-L4835
  - js-allonge:normalized:L4855-L4857
  - js-allonge:normalized:L4865-L4865
  - js-allonge:normalized:L4873-L4875
  - js-allonge:normalized:L5021-L5021
  - js-allonge:normalized:L5053-L5056
  - js-allonge:normalized:L5077-L5086
  - js-allonge:normalized:L5141-L5146
  - js-allonge:normalized:L5179-L5181
  - js-allonge:normalized:L5269-L5269
  - js-allonge:normalized:L5285-L5285
  - js-allonge:normalized:L5513-L5513
  - js-allonge:normalized:L5523-L5523
  - js-allonge:normalized:L5551-L5551
---

# JavaScript Iterables

## Summary

In JavaScript, iterables are objects that define how they can be traversed, typically through the Symbol.iterator method. This enables the use of constructs like for...of loops and the spread operator (...) with custom data structures.

## Source-backed details

| Claim | Evidence |
| --- | --- |
| An iterable in JavaScript is an object that implements the Symbol.iterator method, which returns an iterator object capable of producing a sequence of values. | [js-allonge:claim_js-allonge_c013_d7bbeac9] |
| JavaScript's for...of loop and the spread operator can work with any iterable, including custom objects, making it possible to iterate over non-array collections such as linked lists. | [js-allonge:claim_js-allonge_c013_63fe4b9a], [js-allonge:claim_js-allonge_c013_5d7c6406] |
| Iterables can represent both finite and infinite sequences, though infinite iterables must be consumed lazily to avoid infinite loops, and they maintain ordered collection semantics where elements... | [js-allonge:claim_js-allonge_c013_d4d8a119], [js-allonge:claim_js-allonge_c013_ae6b933d], [js-allonge:claim_js-allonge_c013_8eaa4607] |
| Generators provide a convenient syntax for writing iterators, allowing developers to define functions that can yield values one at a time, maintaining internal state implicitly. | [js-allonge:claim_js-allonge_c013_099222bb], [js-allonge:claim_js-allonge_c013_ac196e01] |
| Iterator objects manage their internal state and are consumed by repeatedly calling their next() method until they signal completion, enabling flexible traversal patterns. | [js-allonge:claim_js-allonge_c013_dfe240f7] |
| Generators are particularly useful for complex recursive enumerations, such as traversing nested data structures, where managing state explicitly would be cumbersome. | [js-allonge:claim_js-allonge_c013_d95a93de] |
| State machines can be implemented using iterables, exemplified by generating the Fibonacci sequence, where each step depends on the previous values. | [js-allonge:claim_js-allonge_c013_d0c87c7e] |
| JavaScript generators allow defining iterables directly using the function* syntax, enabling concise creation of objects that can be used in for...of loops and with the spread operator. | [js-allonge:claim_js-allonge_c014_291768ca], [js-allonge:claim_js-allonge_c014_fc07afbd] |
| Lazy evaluation is a beneficial strategy in algorithms, where computations are deferred until results are actually needed, reducing unnecessary work and memory usage. | [js-allonge:claim_js-allonge_c014_d42ed7d2] |
| Operations on iterables like map and filter can be implemented to return smaller iterable objects that reference the original, leading to reduced memory consumption for large datasets. | [js-allonge:claim_js-allonge_c014_55a2e7e5] |
| Infinite collections can be created as iterables, provided they are designed to be lazy, ensuring that only necessary elements are computed on demand. | [js-allonge:claim_js-allonge_c014_2feb3774] |

## Why it matters

Understanding iterables allows developers to create custom data structures that integrate seamlessly with JavaScript's iteration protocols. It supports efficient, memory-conscious operations and enables powerful patterns like lazy evaluation and recursive enumeration.

## Related pages

- [JavaScript Arrays](../concepts/js-arrays.md)
- [JavaScript Control Flow](../concepts/js-control-flow.md)
- [JavaScript Data Structures](../concepts/js-data-structures.md)
- [JavaScript Data Types](../concepts/js-data-types.md)
- [JavaScript Functions](../concepts/js-functions.md)

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
