---
title: Functional Programming
type: concept
tags: [functional programming, recursion, mapping, folding]
status: draft
last_updated: 2026-05-08
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2711-L2711
  - js-allonge:normalized:L2743-L2743
  - js-allonge:normalized:L2751-L2751
  - js-allonge:normalized:L3029-L3029
  - js-allonge:normalized:L3131-L3131
  - js-allonge:normalized:L4435-L4435
  - js-allonge:normalized:L5513-L5513
  - js-allonge:normalized:L5523-L5523
---

# Functional Programming

## Summary

Functional programming emphasizes the use of pure functions and immutable data. It encourages composing functions from common patterns rather than building them from scratch, leveraging recursion and higher-order functions for data manipulation.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Mapping represents a specific form of linear recursion where functions are used to transform elements of a data structure. | "This specific case of linear recursion is called "mapping," and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's..." | `normalized:L2711-L2711` | [Source](../sources/js-allonge.md) |
| The process of summing squares can be achieved by rewriting the mapping function to suit the desired operation. | "Let's rewrite mapWith so that we can use it to sum squares." | `normalized:L2743-L2743` | [Source](../sources/js-allonge.md) |
| The fold function generalizes the mapping function, allowing representation of mapping through folding with appropriate rebuilding logic. | "Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:" | `normalized:L2751-L2751` | [Source](../sources/js-allonge.md) |
| While recursive approaches using destructuring illustrate recursion principles, they are not optimal for performance in practice. | "Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. But it is an extremely simple illustration of how..." | `normalized:L3131-L3131` | [Source](../sources/js-allonge.md) |
| Recursion using destructuring patterns is inefficient due to the creation of numerous temporary arrays during execution. | "**Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end..." | `normalized:L3029-L3029` | [Source](../sources/js-allonge.md) |
| Both mapping and folding patterns lead to similar outcomes by enabling composition of functions from shared components. | "Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common..." | `normalized:L4435-L4435` | [Source](../sources/js-allonge.md) |
| Lazy evaluation strategies defer computation until results are actually needed, improving algorithmic efficiency. | ""Laziness" is a very pejorative word when applied to people. But it can be an excellent strategy for efficiency in algorithms. Let's be precise: _Laziness_ is the characteristic of not doing any..." | `normalized:L5513-L5513` | [Source](../sources/js-allonge.md) |
| Iterator-based operations reduce memory usage compared to traditional array-based transformations. | "Whereas the .map and .filter methods on Pair work with iterators. They produce small iterable objects that refer back to the original iteration. This reduces the memory footprint. When working..." | `normalized:L5523-L5523` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
