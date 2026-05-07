---
title: Iterators
type: concept
tags: [javascript, iteration, stateful]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L5582-L5591
  - js-allonge:normalized:L5806-L5806
  - js-allonge:normalized:L5810-L5811
  - js-allonge:normalized:L6806-L6807
  - js-allonge:normalized:L6881-L6882
  - js-allonge:normalized:L7759-L7765
---

# Iterators

## Summary

An iterator in JavaScript is a stateful object that produces a sequence of values on demand. It typically provides a function that, when called repeatedly, returns the next value in the sequence along with a flag indicating whether the sequence is complete.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| An iterator is a function that, when invoked, returns an object containing a value and a done flag, enabling sequential access to elements. | "const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ? undefined : array[i++] } } }" | `normalized:L5582-L5591` | [Source](../sources/js-allonge.md) |
| Iterators are inherently stateful, meaning their internal state changes as values are consumed, and once passed to a function, the original owner should not assume control over the iterator's state. | "Please note that unlike most of the other functions discussed in this book, iterators are stateful." | `normalized:L5806-L5806` | [Source](../sources/js-allonge.md) |
| Iterators are inherently stateful, meaning their internal state changes as values are consumed, and once passed to a function, the original owner should not assume control over the iterator's state. | "Once you pass an iterator to a function, you can expect that you no longer "own" that iterator, and that its state either has changed or will change." | `normalized:L5810-L5811` | [Source](../sources/js-allonge.md) |
| Iterators can be implemented using generator functions or by manually creating functions that maintain state, and they support the iterable protocol through the Symbol.iterator method. | "const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } }" | `normalized:L7759-L7765` | [Source](../sources/js-allonge.md) |
| Iterators can be implemented using generator functions or by manually creating functions that maintain state, and they support the iterable protocol through the Symbol.iterator method. | "The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object." | `normalized:L6881-L6882` | [Source](../sources/js-allonge.md) |
| Iterators can be implemented using generator functions or by manually creating functions that maintain state, and they support the iterable protocol through the Symbol.iterator method. | "Instead of having a function that you call to get the next element, you have an object with a .next() method." | `normalized:L6806-L6807` | [Source](../sources/js-allonge.md) |

## Why it matters

Iterators enable efficient handling of sequences, especially large or infinite ones, by allowing lazy evaluation. They form the foundation for iterable protocols and constructs like for...of loops, making code more expressive and memory-efficient.

## Source pages

- [JS Allongé](../sources/js-allonge.md)
