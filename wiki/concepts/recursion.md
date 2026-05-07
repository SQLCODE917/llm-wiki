---
title: Recursion
type: concept
tags: [programming, functional programming, javascript]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L3366-L3367
  - js-allonge:normalized:L3731-L3732
  - js-allonge:normalized:L3752-L3753
  - js-allonge:normalized:L3920-L3921
---

# Recursion

## Summary

Recursion is a programming technique where a function calls itself to solve a problem. It is particularly useful for processing data structures like lists, where the solution can be broken down into smaller subproblems. A key optimization in languages with tail-call support is that tail-recursive calls can be optimized to avoid additional stack frames, improving performance and preventing stack overflow.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| A list can be defined inductively as either being empty or consisting of an element concatenated with another list, which forms the basis for recursive processing. | "One of the simplest, and longest-standing in computer science, is to say that a list is: 1. Empty, or; 2. Consists of an element concatenated with a list" | `normalized:L3366-L3367` | [Source](../sources/js-allonge.md) |
| When a function's final action is to call another function and return its result, it is said to perform a tail-call, which can be optimized by the JavaScript engine to eliminate unnecessary stack... | "A "tail-call" occurs when a function's last act is to invoke another function, and then return whatever the other function returns." | `normalized:L3731-L3732` | [Source](../sources/js-allonge.md) |
| When a function's final action is to call another function and return its result, it is said to perform a tail-call, which can be optimized by the JavaScript engine to eliminate unnecessary stack... | "If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space." | `normalized:L3752-L3753` | [Source](../sources/js-allonge.md) |
| Tail-call optimization allows programmers to write recursive functions that process large arrays efficiently without exhausting memory or causing stack overflow errors. | "We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls." | `normalized:L3920-L3921` | [Source](../sources/js-allonge.md) |

## Why it matters

Recursion provides a natural way to express algorithms that operate on recursively defined data structures such as lists. Understanding recursion and its optimization through tail calls is crucial for writing efficient functional programs in JavaScript, especially when dealing with large datasets.

## Related pages

- [Functional Programming](../concepts/functional-programming.md)
- [Iterators](../concepts/iterators.md)
- [Arrays](../concepts/arrays.md)
- [Objects](../concepts/objects.md)
- [ES6 Features](../concepts/es6-features.md)
- [Data Types](../concepts/data-types.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
