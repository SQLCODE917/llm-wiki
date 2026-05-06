---
title: Functional Programming
type: concept
tags: [programming, javascript, paradigm]
status: draft
last_updated: 2026-05-06
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2094-L2095
  - js-allonge:normalized:L2113-L2114
  - js-allonge:normalized:L2154-L2155
---

# Functional Programming

## Summary

Functional programming is a programming paradigm that emphasizes the use of pure functions and immutable data. It treats functions as first-class citizens, allowing them to be passed as arguments, returned from other functions, and assigned to variables. This approach promotes code clarity, modularity, and easier reasoning about program behavior.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Higher-order functions are those that either accept functions as arguments, return functions, or both, enabling powerful functional patterns. | "Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a "higher-order" function." | `normalized:L2094-L2095` | [Source](../sources/js-allonge.md) |
| Combinators are a specific type of higher-order function that build results solely through function application and previously defined combinators, often used for function composition. | "A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments." | `normalized:L2113-L2114` | [Source](../sources/js-allonge.md) |
| Function decorators modify existing functions by taking one function and returning another, often used to add functionality without altering the original. | "A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function." | `normalized:L2154-L2155` | [Source](../sources/js-allonge.md) |

## Why it matters

Functional programming techniques lead to more predictable and maintainable code. By avoiding side effects and favoring immutability, developers can reduce bugs and make code easier to test and debug. Concepts like higher-order functions, composition, and combinators enable powerful abstractions that simplify complex operations.

## Related pages

- [Functions](../concepts/functions.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
