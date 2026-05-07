---
title: Functional Programming
type: concept
tags: [programming, paradigm, javascript]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2113-L2114
  - js-allonge:normalized:L2154-L2156
  - js-allonge:normalized:L267-L270
---

# Functional Programming

## Summary

Functional programming is a programming paradigm that emphasizes the use of pure functions and immutable data. It focuses on composing functions and treating functions as first-class citizens, enabling powerful abstractions and transformations.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Functional programming in JavaScript benefits from modern language features introduced in ECMAScript 2015, which simplify expressing functional techniques such as composition and higher-order... | "ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. It makes a number of interesting programming techniques easy to explain..." | `normalized:L267-L270` | [Source](../sources/js-allonge.md) |
| Combinators are higher-order functions that build upon other combinators and function application to create new functions, often used for function composition and abstraction. | "A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments." | `normalized:L2113-L2114` | [Source](../sources/js-allonge.md) |
| Function decorators modify existing functions to produce variations, serving as a mechanism for extending functionality while maintaining clean separation of concerns. | "A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function." | `normalized:L2154-L2156` | [Source](../sources/js-allonge.md) |

## Why it matters

Functional programming promotes code that is easier to reason about, test, and maintain due to its emphasis on immutability and pure functions. It also enables techniques like lazy evaluation and efficient recursion patterns, which are beneficial for performance and scalability.

## Related pages

- [Iterators](../concepts/iterators.md)
- [Objects](../concepts/objects.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
