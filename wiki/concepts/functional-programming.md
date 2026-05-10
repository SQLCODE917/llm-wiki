---
title: Functional Programming
type: concept
tags: [programming-paradigm, javascript, data-structures]
status: draft
last_updated: 2026-05-09
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L159-L159
  - js-allonge:normalized:L3071-L3071
  - js-allonge:normalized:L3283-L3283
  - js-allonge:normalized:L3299-L3299
  - js-allonge:normalized:L3329-L3329
  - js-allonge:normalized:L3341-L3341
  - js-allonge:normalized:L3419-L3419
  - js-allonge:normalized:L3463-L3463
  - js-allonge:normalized:L3899-L3899
  - js-allonge:normalized:L4057-L4057
  - js-allonge:normalized:L4059-L4059
  - js-allonge:normalized:L4909-L4909
  - js-allonge:normalized:L5937-L5940
---

# Functional Programming

## Summary

Functional programming is a programming paradigm that emphasizes the use of pure functions and immutable data structures. It avoids changing state and mutable data, favoring declarative and composable code patterns.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Linked lists can be implemented using recursive data structures where each node points to the next, enabling efficient construction and manipulation without direct array indexing. | "**const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));" | `normalized:L3071-L3071` | [Source](../sources/js-allonge.md) |
| Linked lists can be implemented using recursive data structures where each node points to the next, enabling efficient construction and manipulation without direct array indexing. | "In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } }." | `normalized:L3283-L3283` | [Source](../sources/js-allonge.md) |
| Operations on linked lists such as length calculation and reversal can be elegantly expressed using recursion and immutable updates, which helps maintain data integrity and simplifies reasoning... | "**const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);" | `normalized:L3299-L3299` | [Source](../sources/js-allonge.md) |
| Operations on linked lists such as length calculation and reversal can be elegantly expressed using recursion and immutable updates, which helps maintain data integrity and simplifies reasoning... | "**const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });" | `normalized:L3329-L3329` | [Source](../sources/js-allonge.md) |
| Operations on linked lists such as length calculation and reversal can be elegantly expressed using recursion and immutable updates, which helps maintain data integrity and simplifies reasoning... | "**const** mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });" | `normalized:L3341-L3341` | [Source](../sources/js-allonge.md) |
| Functional programming principles advocate for minimizing mutation during data processing, favoring immutable data structures and pure functions to reduce bugs and improve code reliability. | "One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript..." | `normalized:L3419-L3419` | [Source](../sources/js-allonge.md) |
| Functional programming principles advocate for minimizing mutation during data processing, favoring immutable data structures and pure functions to reduce bugs and improve code reliability. | "So back to avoiding mutation. In general, it's easier to reason about data that doesn't change. We don't have to remember to use copying operations when we pass it as a value to a function, or..." | `normalized:L3463-L3463` | [Source](../sources/js-allonge.md) |
| The theoretical foundation of computation shows that complex operations can be modeled using simple constructs like functions, demonstrating that higher-level abstractions like arrays or objects... | "They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a..." | `normalized:L4059-L4059` | [Source](../sources/js-allonge.md) |
| The theoretical foundation of computation shows that complex operations can be modeled using simple constructs like functions, demonstrating that higher-level abstractions like arrays or objects... | "A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations...." | `normalized:L4057-L4057` | [Source](../sources/js-allonge.md) |
| While iterative approaches like loops are common, functional programming often favors higher-order functions such as folds for expressing algorithms, providing a more declarative way to process... | "Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is..." | `normalized:L3899-L3899` | [Source](../sources/js-allonge.md) |
| Collections in functional programming are made iterable through standard protocols, allowing for consistent traversal and interaction with various data structures using iterators. | "This illustrates the general pattern of working with ordered collections: We make them _iterables_ , meaning that they have a [Symbol.iterator] method, that returns an _iterator_ . An iterator is..." | `normalized:L4909-L4909` | [Source](../sources/js-allonge.md) |
| Stateless implementations of algorithms, such as a game board evaluator, demonstrate how functional techniques can manage complex logic without relying on mutable internal states. | "statelessNaughtsAndCrosses([ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]) _//=> 3_" | `normalized:L5937-L5940` | [Source](../sources/js-allonge.md) |
| In functional contexts, variables are typically scoped to their enclosing blocks, supporting clean and predictable variable access patterns. | "And i is scoped to the for loop. We can also write:" | `normalized:L159-L159` | [Source](../sources/js-allonge.md) |

## Why it matters

Functional programming promotes code that is easier to reason about, test, and debug due to the absence of side effects and mutable state. It encourages writing programs as transformations of data, leading to more predictable behavior and reduced complexity.

## Related pages

- [Arrays](../concepts/arrays.md)
- [Control Flow](../concepts/control-flow.md)
- [Data Types](../concepts/data-types.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)
- [Recursion](../concepts/recursion.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
