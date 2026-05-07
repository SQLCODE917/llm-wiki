---
title: Iterators
type: concept
tags: [javascript, programming, collections, iteration]
status: draft
last_updated: 2024-07-15
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L5609-L5610
  - js-allonge:normalized:L5657-L5657
  - js-allonge:normalized:L5657-L5658
  - js-allonge:normalized:L5806-L5807
  - js-allonge:normalized:L6963-L6964
  - js-allonge:normalized:L7017-L7020
  - js-allonge:normalized:L7052-L7055
  - js-allonge:normalized:L7294-L7300
  - js-allonge:normalized:L7349-L7349
---

# Iterators

## Summary

Iterators are functions that produce a sequence of values, either by traversing existing data structures or generating new values on demand. They maintain internal state to track their position during iteration.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| An iterator function accepts an array and produces a function capable of sequentially returning its elements. | "The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array." | `normalized:L5609-L5610` | [Source](../sources/js-allonge.md) |
| Iterators can be implemented as functions that either access pre-existing data or dynamically generate new data during traversal. | "Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go." | `normalized:L5657-L5658` | [Source](../sources/js-allonge.md) |
| Iterator implementations may generate data dynamically rather than simply accessing stored values. | "But they could just as easily manufacture the data as they go." | `normalized:L5657-L5657` | [Source](../sources/js-allonge.md) |
| Unlike most other functions in the book, iterators are stateful, requiring careful handling to avoid unintended side effects. | "Please note that unlike most of the other functions discussed in this book, iterators are stateful. There are some important implications of stateful functions." | `normalized:L5806-L5807` | [Source](../sources/js-allonge.md) |
| Custom collections can be extended with methods by assigning functions to their properties, enabling flexible behavior. | "We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ]. And if we assign a function to a..." | `normalized:L7294-L7300` | [Source](../sources/js-allonge.md) |
| Iterators must manage their own internal state to determine what value to return upon each invocation. | "Iterators have to arrange its own state such that when you call them, they compute and return the next item." | `normalized:L7349-L7349` | [Source](../sources/js-allonge.md) |
| The for...of construct operates directly with iterable objects, which are defined by having a Symbol.iterator method that returns an iterator. | "The for...of loop works directly with any object that is iterable, meaning it works with any object that has a Symbol.iterator method that returns an object iterator." | `normalized:L6963-L6964` | [Source](../sources/js-allonge.md) |
| The spread operator allows elements from any iterable to be included in array literals or passed as function arguments. | "Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal: ['some squares', ...someSquares]" | `normalized:L7017-L7020` | [Source](../sources/js-allonge.md) |
| Attempting to spread an infinite iterable into an array will result in an infinite loop and failure. | "['all the numbers', ...Numbers] //=> infinite loop! firstAndSecondElement(...Numbers) //=> infinite loop!" | `normalized:L7052-L7055` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
