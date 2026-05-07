---
title: Recursion
type: concept
tags: [computer science, functional programming, algorithms]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L3366-L3367
  - js-allonge:normalized:L3617-L3620
  - js-allonge:normalized:L3731-L3732
  - js-allonge:normalized:L3752-L3753
  - js-allonge:normalized:L3920-L3923
  - js-allonge:normalized:L4067-L4070
  - js-allonge:normalized:L7403-L7404
---

# Recursion

## Summary

Recursion is a programming technique where a function calls itself to solve a problem. It is particularly useful for processing data structures like lists and trees, and can be optimized in languages that support tail-call elimination.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| A fundamental recursive definition describes a list as either empty or composed of an element concatenated with another list, mirroring how such structures are built. | "One of the simplest, and longest-standing in computer science, is to say that a list is: 1. Empty, or; 2. Consists of an element concatenated with a list ." | `normalized:L3366-L3367` | [Source](../sources/js-allonge.md) |
| Linear recursion aligns with the construction of linear data structures and serves as a foundational approach for algorithm design, making it inherently comprehensible. | "Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable." | `normalized:L3617-L3620` | [Source](../sources/js-allonge.md) |
| Tail-call optimization allows a function to efficiently reuse stack space when its final action is to invoke another function, returning the result directly. | "A "tail-call" occurs when a function's last act is to invoke another function, and then return whatever the other function returns." | `normalized:L3731-L3732` | [Source](../sources/js-allonge.md) |
| Tail-call optimization allows a function to efficiently reuse stack space when its final action is to invoke another function, returning the result directly. | "If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space." | `normalized:L3752-L3753` | [Source](../sources/js-allonge.md) |
| When a recursive function performs a tail call, JavaScript can eliminate the overhead of additional function calls, enhancing both memory usage and performance. | "If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space." | `normalized:L3752-L3753` | [Source](../sources/js-allonge.md) |
| Transforming a recursive function to make tail calls is a common and valuable technique for managing large datasets without excessive memory consumption. | "Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a..." | `normalized:L3920-L3923` | [Source](../sources/js-allonge.md) |
| Recursive approaches are essential for traversing complex data structures like nested arrays, enabling operations such as flattening or collecting specific elements. | "For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the "leaf" elements, i.e. elements that are not, themselves, iterable." | `normalized:L7403-L7404` | [Source](../sources/js-allonge.md) |
| Each recursive invocation in a function like mapWith creates a new array, demonstrating how recursion can lead to significant memory usage if not optimized. | "Every time we call mapWith, we're calling [...prepend, fn(first)]. To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next..." | `normalized:L4067-L4070` | [Source](../sources/js-allonge.md) |

## Why it matters

Recursion provides a natural way to express algorithms that operate on recursively defined data structures. It also enables optimizations like tail-call elimination, which can improve performance and prevent stack overflow errors in certain cases.

## Related pages

- [Data Types](../concepts/data-types.md)
- [Functional Programming](../concepts/functional-programming.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)
- [Objects](../concepts/objects.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
