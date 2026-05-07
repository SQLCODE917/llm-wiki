---
title: Recursion
type: concept
tags: [computer-science, functional-programming, javascript]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L3366-L3367
  - js-allonge:normalized:L3731-L3732
  - js-allonge:normalized:L3775-L3778
  - js-allonge:normalized:L4067-L4070
  - js-allonge:normalized:L4087-L4090
---

# Recursion

## Summary

Recursion is a programming technique where a function calls itself to solve a problem. It is foundational in computer science and functional programming, often used to process data structures like lists. Recursion can be optimized through tail-call elimination, which allows the JavaScript engine to reuse stack frames and avoid unnecessary overhead.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| A list can be defined recursively as either empty or consisting of an element concatenated with another list. | "One of the simplest, and longest-standing in computer science, is to say that a list is: 1. Empty, or; 2. Consists of an element concatenated with a list" | `normalized:L3366-L3367` | [Source](../sources/js-allonge.md) |
| A tail-call occurs when a function's final action is to invoke another function and return its result, enabling potential performance optimizations. | "A "tail-call" occurs when a function's last act is to invoke another function, and then return whatever the other function returns. ... JavaScript optimizes away the function call overhead and..." | `normalized:L3731-L3732` | [Source](../sources/js-allonge.md) |
| Converting a recursive operation into a tail-recursive form involves shifting computational work into the arguments of recursive calls. | "The obvious solution is push the 1 + work into the call to length. Here's our first cut: const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded :..." | `normalized:L3775-L3778` | [Source](../sources/js-allonge.md) |
| The recursive approach using destructuring creates numerous temporary arrays, leading to inefficient memory usage due to repeated copying of elements. | "Key Point: Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up..." | `normalized:L4087-L4090` | [Source](../sources/js-allonge.md) |
| Each invocation of a recursive mapping function constructs a new array by appending elements, resulting in significant overhead during execution. | "Every time we call mapWith, we're calling [...prepend, fn(first)]. To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next..." | `normalized:L4067-L4070` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
