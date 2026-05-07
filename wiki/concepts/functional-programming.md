---
title: Functional Programming
type: concept
tags: [programming, javascript, combinators]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2113-L2114
  - js-allonge:normalized:L2129-L2131
  - js-allonge:normalized:L2134-L2135
  - js-allonge:normalized:L2195-L2195
  - js-allonge:normalized:L262-L266
---

# Functional Programming

## Summary

Functional programming is a paradigm that emphasizes the use of pure functions, immutability, and higher-order functions to build software. It focuses on describing what should be computed rather than how to compute it, often through composition and recursion.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| The JavaScript language is particularly suited for functional programming paradigms, making it an ideal choice for exploring concepts like decorators and combinators. | "Thus, the focus on things like writing decorators. As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and..." | `normalized:L262-L266` | [Source](../sources/js-allonge.md) |
| Combinators are higher-order functions that build new functions from existing ones, often defined using only function application and previously defined combinators. | "A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments." | `normalized:L2113-L2114` | [Source](../sources/js-allonge.md) |
| Combinators are higher-order functions that build new functions from existing ones, often defined using only function application and previously defined combinators. | "In this book, we will be using a looser definition of "combinator:" Higher-order pure functions that take only functions as arguments and return a function." | `normalized:L2129-L2131` | [Source](../sources/js-allonge.md) |
| Function composition is a core concept where chaining multiple functions together allows for building complex operations from simpler ones, exemplified by the compose function. | "const compose = (a, b) => (c) => a(b(c))" | `normalized:L2134-L2135` | [Source](../sources/js-allonge.md) |
| Function composition is a core concept where chaining multiple functions together allows for building complex operations from simpler ones, exemplified by the compose function. | "Whenever you are chaining two or more functions together, you're composing them." | `normalized:L2195-L2195` | [Source](../sources/js-allonge.md) |

## Why it matters

Functional programming promotes code that is easier to reason about, test, and maintain due to its emphasis on immutability and pure functions. It also enables powerful abstractions like function composition and lazy evaluation, which can lead to more efficient and expressive code.

## Related pages

- [Iterators](../concepts/iterators.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
