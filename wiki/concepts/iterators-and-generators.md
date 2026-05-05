---
title: Iterators And Generators
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Iterators And Generators

Iterators are objects or functions that enable sequential access to elements in a data structure, allowing for lazy evaluation and efficient handling of both finite and infinite collections. Generators provide a convenient syntax for writing iterators using a generation-style programming approach.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Iterators are functions that return elements from a data structure one at a time until completion | "The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array." | `normalized:L5609` | [Source](../sources/js-allonge.md) |
| Lazy evaluation can be implemented with iterators to avoid computing values until they are needed | "This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test." | `normalized:L5798` | [Source](../sources/js-allonge.md) |
| An iterator can also be implemented as an object with a next() method | "Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method." | `normalized:L6806` | [Source](../sources/js-allonge.md) |
| Iterables can represent infinite collections | "Iterables needn't represent finite collections: const Numbers = { [Symbol.iterator] () { let n = 0; return { next: () => ({done: false, value: n++}) } } }" | `normalized:L7034` | [Source](../sources/js-allonge.md) |
| Collection operations like mapWith preserve the ordered collection semantics of their input | "mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation." | `normalized:L7189` | [Source](../sources/js-allonge.md) |
| The iterator protocol separates the concern of how to iterate over a collection from what to do with its elements | "Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection." | `normalized:L7330` | [Source](../sources/js-allonge.md) |
| JavaScript generators allow writing iterators in a generation-style programming approach | "We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator." | `normalized:L7576` | [Source](../sources/js-allonge.md) |
| An object can be made iterable by implementing a [Symbol.iterator] method that returns an iterator | "This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator], it's a generator instead of an iterator." | `normalized:L7808` | [Source](../sources/js-allonge.md) |
| The yield* syntax can be used to yield all elements from another iterable | "yield* is handy when writing generator functions that operate on or create iterables." | `normalized:L8122` | [Source](../sources/js-allonge.md) |
| The yield* operator can be used to yield all elements of an iterable in order | "yield * yields all of the elements of an iterable, in order." | `normalized:L8100` | [Source](../sources/js-allonge.md) |
| Lazy evaluation means computations are deferred until the result is actually needed | "Laziness is the characteristic of not doing any work until you know you need the result of the work." | `normalized:L8501` | [Source](../sources/js-allonge.md) |
| Infinite collections can be implemented using lazy evaluation and iterators | "You recall we briefly touched on the idea of infinite collections? Let's make iterable numbers. They have to be lazy, otherwise we couldn't write things like:" | `normalized:L8624` | [Source](../sources/js-allonge.md) |

## Why it matters

Iterators and generators provide powerful mechanisms for working with sequences of data in JavaScript. They enable lazy evaluation which improves performance by avoiding unnecessary computations, support both finite and infinite collections, and offer a clean separation between iteration logic and data processing. Generators specifically simplify the implementation of iterators by providing a more intuitive syntax that resembles synchronous code while maintaining the benefits of asynchronous-like behavior.

## Source pages

- [Source](../sources/js-allonge.md)