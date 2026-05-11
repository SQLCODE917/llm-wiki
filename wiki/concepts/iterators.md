---
title: Iterators
type: concept
tags: [javascript, iteration, generators]
status: draft
last_updated: 2026-05-11
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4017-L4017
  - js-allonge:normalized:L4027-L4027
  - js-allonge:normalized:L4761-L4761
  - js-allonge:normalized:L4791-L4791
  - js-allonge:normalized:L5143-L5143
  - js-allonge:normalized:L5261-L5261
  - js-allonge:normalized:L5315-L5315
  - js-allonge:normalized:L5395-L5395
  - js-allonge:normalized:L5449-L5449
  - js-allonge:normalized:L5807-L5807
  - js-allonge:normalized:L6069-L6072
  - js-allonge:normalized:L6075-L6080
  - js-allonge:normalized:L6077-L6082
  - js-allonge:normalized:L6095-L6103
---

# Iterators

## Summary

Iterators are objects that provide a sequence of values through a standardized interface. They enable efficient traversal of data structures without loading all elements into memory at once.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| An iterator object simplifies the process of accessing sequential data compared to iterator functions by using a .next() method instead of repeated function calls. | "Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. Like this:" | `normalized:L4761-L4761` | [Source](../sources/js-allonge.md) |
| The Symbol.iterator property represents a special symbol used to identify the method that objects should implement to return an iterator object. | "The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object." | `normalized:L4791-L4791` | [Source](../sources/js-allonge.md) |
| Generator functions are defined using the function * syntax, distinguishing them from regular functions or arrow functions. | "1. We declare the function using the function * syntax. Not a fat arrow. Not a plain function." | `normalized:L5143-L5143` | [Source](../sources/js-allonge.md) |
| A generator function produces an iterator when invoked, rather than returning a single value directly. | "Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and..." | `normalized:L5261-L5261` | [Source](../sources/js-allonge.md) |
| The Fibonacci sequence can be implemented as an ordered collection using a generator method with the Symbol.iterator property. | "**const** Fibonacci = { *[Symbol.iterator] () { **let** a, b; **yield** a = 0; **yield** b = 1; **while** ( **true** ) { [a, b] = [b, a + b] **yield** b; } } } **for** ( **const** i **of**..." | `normalized:L5315-L5315` | [Source](../sources/js-allonge.md) |
| The mapWith function applies a transformation to each element in an iterable using a generator approach. | "**function** * mapWith (fn, iterable) { **for** ( **const** element **of** iterable) { **yield** fn(element); } }" | `normalized:L5395-L5395` | [Source](../sources/js-allonge.md) |
| LazyCollection is a mixin that allows any ordered collection to be composed with iterable operations. | "Here is LazyCollection, a mixin we can use with any ordered collection that is also an iterable:" | `normalized:L5449-L5449` | [Source](../sources/js-allonge.md) |
| The firstInIteration function efficiently retrieves the first element matching a condition from an iterator. | "**const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);" | `normalized:L4017-L4017` | [Source](../sources/js-allonge.md) |
| Iterator functions maintain internal state, which affects how they behave when passed between functions. | "Please note that unlike most of the other functions discussed in this book, iterators are _stateful_ . There are some important implications of stateful functions. One is that while functions like..." | `normalized:L4027-L4027` | [Source](../sources/js-allonge.md) |
| Generators can be used to create iterators that manage implicit state, including for recursive unfolds and state machines. | "We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that..." | `normalized:L5807-L5807` | [Source](../sources/js-allonge.md) |
| The memoize function creates a cached version of a generator that stores previously yielded values. | "**function** memoize (generator) { **const** memos = {}, iterators = {}; **return function** * (...args) { **const** key = JSON.stringify(args); **let** i = 0; **if** (memos[key] == **null** ) {..." | `normalized:L6095-L6103` | [Source](../sources/js-allonge.md) |
| The zip function combines multiple iterables into a single iterable of grouped elements. | "**function** * zip (...iterables) { **const** iterators = iterables.map(i => i[Symbol.iterator]()); **while** ( **true** ) { **const** pairs = iterators.map(j => j.next()), dones = pairs.map(p =>..." | `normalized:L6075-L6080` | [Source](../sources/js-allonge.md) |
| The zipWith function combines multiple iterables using a provided function to transform grouped elements. | "**while** ( **true** ) { **const** pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); **if** (dones.indexOf( **true** ) >= 0) **break** ;..." | `normalized:L6077-L6082` | [Source](../sources/js-allonge.md) |
| The take function extracts a specified number of elements from an iterable. | "**function** * take (numberToTake, iterable) { **const** iterator = iterable[Symbol.iterator](); **for** ( **let** i = 0; i < numberToTake; ++i) { **const** { done, value } = iterator.next();..." | `normalized:L6069-L6072` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
