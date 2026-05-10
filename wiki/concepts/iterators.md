---
title: Iterators
type: concept
tags: [javascript, iteration, stateful, generator]
status: draft
last_updated: 2026-05-09
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4027-L4027
  - js-allonge:normalized:L4761-L4761
  - js-allonge:normalized:L5261-L5261
---

# Iterators

## Summary

An iterator is an object that provides a sequence of values, typically through a .next() method. Iterators are fundamental to JavaScript's iteration protocol and enable efficient traversal of data structures, especially when dealing with potentially large or infinite sequences.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| An iterator is an object that provides a sequence of values through a .next() method, allowing controlled access to elements one at a time. | "Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. Like this:" | `normalized:L4761-L4761` | [Source](../sources/js-allonge.md) |
| Iterators in JavaScript are often implemented using generator functions, which provide a concise way to define stateful iteration logic. | "Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and..." | `normalized:L5261-L5261` | [Source](../sources/js-allonge.md) |
| Iterators maintain internal state, and operations on them can modify the underlying state, meaning that multiple references to an iterator may share the same mutable state. | "Please note that unlike most of the other functions discussed in this book, iterators are _stateful_ . There are some important implications of stateful functions. One is that while functions like..." | `normalized:L4027-L4027` | [Source](../sources/js-allonge.md) |

## Why it matters

Iterators allow for lazy evaluation, enabling efficient processing of large datasets without loading everything into memory at once. They form the basis for JavaScript's for...of loop and the spread operator, making code more readable and expressive when working with ordered collections.

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
