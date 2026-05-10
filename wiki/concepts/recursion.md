---
title: Recursion
type: concept
tags: [programming, functions, data-structures]
status: draft
last_updated: 2026-05-09
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2299-L2310
  - js-allonge:normalized:L2589-L2593
  - js-allonge:normalized:L2631-L2637
---

# Recursion

## Summary

Recursion is a programming technique where a function calls itself to solve a problem. It is particularly useful for processing self-similar data structures like lists and trees, and can be optimized in languages that support tail-call elimination.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| A recursive function can be designed such that it avoids infinite loops by using conditional logic that stops the recursion when a base case is met, like checking if a number equals zero. | "**const** even = (n) => n === 0 \|\| (n !== 1 && even(n - 2)) even(42) _//=> true_ If n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). This is very important! Imagine that..." | `normalized:L2299-L2310` | [Source](../sources/js-allonge.md) |
| Recursive definitions are common in computer science, such as defining a list as either empty or composed of an element concatenated with another list. | "But we can also define a list by describing a rule for building lists. One of the simplest, and longeststanding in computer science, is to say that a list is: 1. Empty, or; 2. Consists of an..." | `normalized:L2589-L2593` | [Source](../sources/js-allonge.md) |
| Recursive algorithms often mirror the structure of the data they process, such as calculating the length of a list by recursively processing its elements until reaching the empty list. | "**const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest); Let's try it! length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_ Our..." | `normalized:L2631-L2637` | [Source](../sources/js-allonge.md) |

## Why it matters

Recursion allows for elegant and intuitive solutions to problems involving self-similar structures. It aligns well with mathematical definitions and can simplify code when dealing with recursive data types. Furthermore, in JavaScript, tail-recursive functions can be optimized to avoid excessive memory usage.

## Related pages

- [Arrays](../concepts/arrays.md)
- [Control Flow](../concepts/control-flow.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
