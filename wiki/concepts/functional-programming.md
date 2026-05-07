---
title: Functional Programming
type: concept
tags: [programming-paradigm, functions, composition]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2094-L2095
  - js-allonge:normalized:L2112-L2114
  - js-allonge:normalized:L2129-L2131
  - js-allonge:normalized:L271-L277
---

# Functional Programming

## Summary

Functional programming is a paradigm that emphasizes the use of pure functions and immutable data. It focuses on composing functions to build complex operations and avoids changing state or mutable data.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Modern JavaScript features like classes, mixins, and iterators are built upon fundamental principles of functional programming where simple objects and functions are composed to build applications. | "Thus, the "six" edition introduces classes and mixins. It introduces the notion of implementing private properties with symbols. It introduces iterators and generators. But the common thread that..." | `normalized:L271-L277` | [Source](../sources/js-allonge.md) |
| Higher-order functions, which take other functions as arguments or return functions, are central to functional programming and are often called combinators when they follow specific mathematical... | "Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a "higher-order" function." | `normalized:L2094-L2095` | [Source](../sources/js-allonge.md) |
| Higher-order functions, which take other functions as arguments or return functions, are central to functional programming and are often called combinators when they follow specific mathematical... | "The word "combinator" has a precise technical meaning in mathematics: "A combinator is a higher-order function that uses only function application and earlier defined combinators to define a..." | `normalized:L2112-L2114` | [Source](../sources/js-allonge.md) |
| Combinators in functional programming are higher-order functions that combine other functions to produce new functions without relying on external state or variables. | "In this book, we will be using a looser definition of "combinator:" Higher-order pure functions that take only functions as arguments and return a function." | `normalized:L2129-L2131` | [Source](../sources/js-allonge.md) |

## Why it matters

Functional programming promotes code that is easier to reason about, test, and debug due to the absence of side effects. It also facilitates better composition of functionality and can lead to more maintainable and scalable software systems.

## Related pages

- [Data Types](../concepts/data-types.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
