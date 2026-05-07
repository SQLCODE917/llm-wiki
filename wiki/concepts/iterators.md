---
title: Iterators
type: concept
tags: [javascript, iteration, stateful]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L5591-L5591
  - js-allonge:normalized:L5609-L5611
  - js-allonge:normalized:L5612-L5612
  - js-allonge:normalized:L5806-L5806
  - js-allonge:normalized:L5809-L5809
  - js-allonge:normalized:L7400-L7401
  - js-allonge:normalized:L7403-L7404
---

# Iterators

## Summary

An iterator is a mechanism for sequentially accessing elements of a collection without exposing the underlying structure. It provides a way to traverse data structures by returning one element at a time, often through a function that maintains internal state.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| An iterator function can be created to access elements of a data structure one at a time, maintaining internal state to track progress. | "The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array." | `normalized:L5591-L5591` | [Source](../sources/js-allonge.md) |
| An iterator function can be created to access elements of a data structure one at a time, maintaining internal state to track progress. | "Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the..." | `normalized:L5609-L5611` | [Source](../sources/js-allonge.md) |
| Iterators are stateful objects that carry their own internal state, which can be modified during traversal, affecting subsequent iterations. | "Please note that unlike most of the other functions discussed in this book, iterators are stateful." | `normalized:L5806-L5806` | [Source](../sources/js-allonge.md) |
| Iterators are stateful objects that carry their own internal state, which can be modified during traversal, affecting subsequent iterations. | "So as you traverse the new decorator, you're changing the state of the original!" | `normalized:L5809-L5809` | [Source](../sources/js-allonge.md) |
| Iterators provide a flexible way to process data structures such as linked lists or trees, allowing for recursive enumeration and lazy evaluation. | "We can write a different iterator for a different data structure. Here's one for linked lists:" | `normalized:L5612-L5612` | [Source](../sources/js-allonge.md) |
| Iterators provide a flexible way to process data structures such as linked lists or trees, allowing for recursive enumeration and lazy evaluation. | "One of those cases is when we have to recursively enumerate something. For example, iterating over a tree." | `normalized:L7400-L7401` | [Source](../sources/js-allonge.md) |
| Iterators provide a flexible way to process data structures such as linked lists or trees, allowing for recursive enumeration and lazy evaluation. | "Given an array that might contain arrays, let's say we want to generate all the "leaf" elements, i.e. elements that are not, themselves, iterable." | `normalized:L7403-L7404` | [Source](../sources/js-allonge.md) |

## Why it matters

Iterators enable efficient traversal of data structures, support lazy evaluation, and facilitate working with potentially infinite sequences. They form the foundation for constructs like the 'for...of' loop and allow for custom iteration logic tailored to specific data types.

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
