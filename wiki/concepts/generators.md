---
title: Generators
type: concept
tags: [javascript, functions, iteration]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L7801-L7807
  - js-allonge:normalized:L7929-L7932
  - js-allonge:normalized:L8075-L8075
---

# Generators

## Summary

Generators are a special type of function in JavaScript that can be paused and resumed during execution, allowing for the creation of iterators with a clean and readable syntax.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| A generator function is defined using the function* syntax and can contain yield expressions to pause execution and return values. | "const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } }" | `normalized:L7801-L7807` | [Source](../sources/js-allonge.md) |
| Generators allow developers to write iterative algorithms in a more natural and state-managed way compared to manually implementing iterators. | "We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly..." | `normalized:L7929-L7932` | [Source](../sources/js-allonge.md) |
| Generator functions can delegate to other iterables using the yield* syntax, enabling composition of different iteration behaviors. | "yield * iterable;" | `normalized:L8075-L8075` | [Source](../sources/js-allonge.md) |

## Why it matters

Generators provide an elegant way to handle iteration and asynchronous operations in JavaScript. They simplify the creation of custom iterators and enable more readable code when dealing with complex state management.

## Related pages

- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)
- [Closures](../concepts/closures.md)
- [Functional Programming](../concepts/functional-programming.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
