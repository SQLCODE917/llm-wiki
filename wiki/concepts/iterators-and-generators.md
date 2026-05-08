---
title: Iterators And Generators
type: concept
tags: []
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
---

# Iterators And Generators

Iterators and generators are fundamental concepts in JavaScript that enable efficient traversal and manipulation of data sequences. Iterators provide a standardized way to access elements one at a time, while generators offer a concise syntax for creating iterators with built-in state management. Together, they support lazy evaluation, infinite sequences, and clean implementations of iterative algorithms.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| An iterator is a function that returns objects with done and value properties, enabling traversal of data structures one element at a time. | "Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the..." | normalized:L3931-L3932 | [Source](../sources/js-allonge.md) |
| An iterable object has a Symbol.iterator method that returns an iterator object with a next method for traversal. | "**const** Stack3 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this**..." | normalized:L4801-L4801 | [Source](../sources/js-allonge.md) |
| Any iterable can be spread into an array literal using the spread operator, which creates an array from the elements of the iterable. | "- ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_" | normalized:L4839-L4839 | [Source](../sources/js-allonge.md) |
| The rest function returns an iterable that iterates over all but the first element of an iterable, similar to array destructuring. | "**const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next();..." | normalized:L4965-L4965 | [Source](../sources/js-allonge.md) |
| When a generator function is invoked, it returns an iterator object that can be called with .next() to execute the generator step by step. | "When we invoke the function, we get an iterator object back. Let's start with the degenerate example, the empty iterator:[91] **function** * empty () {};" | normalized:L5147-L5149 | [Source](../sources/js-allonge.md) |
| Generators can be used to implement infinite sequences by using a while loop with yield statements. | "**const** Numbers = { *[Symbol.iterator] () { **let** i = 0; **while** ( **true** ) { **yield** i++; } } }; **for** ( **const** i **of** Numbers) { console.log(i); } _//=>_ 0 1 2 3 4 5 6 7" | normalized:L5295-L5295 | [Source](../sources/js-allonge.md) |
| Generator functions can be used to rewrite traditional iterable operations like map, filter, and until in a more concise way. | "**function** * mapWith (fn, iterable) { **for** ( **const** element **of** iterable) { **yield** fn(element); } }" | normalized:L5395-L5395 | [Source](../sources/js-allonge.md) |
| Generator functions can be used to create lazy iterables that produce values on-demand rather than computing all values upfront. | "append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results." | normalized:L5365-L5365 | [Source](../sources/js-allonge.md) |
| Generators simplify code for recursive iterations or state patterns without needing to wrap values in objects with .done and .value properties. | "A generator is a function that is defined with function * and uses yield (or yield *) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us..." | normalized:L5421-L5423 | [Source](../sources/js-allonge.md) |
| Lazy collection operations like map and filter on iterables produce small iterable objects that refer back to the original iteration rather than creating temporary arrays. | "Whereas the .map and .filter methods on Pair work with iterators. They produce small iterable objects that refer back to the original iteration. This reduces the memory footprint. When working with..." | normalized:L5523-L5523 | [Source](../sources/js-allonge.md) |
| Infinite collections can be implemented using lazy evaluation since they cannot be fully computed at once. | "You recall we briefly touched on the idea of infinite collections? Let's make iterable numbers. They _have_ to be lazy, otherwise we couldn't write things like:" | normalized:L5551-L5551 | [Source](../sources/js-allonge.md) |
| Generator functions can be used to create iterators that embody their state in control flow rather than explicit data. | normalized:L6048-L6048 | [Source](../sources/js-allonge.md) |

## Why it matters

These concepts are essential for writing efficient and expressive JavaScript code. They allow developers to work with large datasets without loading everything into memory at once, support elegant solutions for recursive problems, and provide a clean syntax for implementing complex iteration logic. By leveraging lazy evaluation and generator functions, programmers can build more performant applications that handle infinite sequences and on-demand computations gracefully.

## Source pages

- [Source](../sources/js-allonge.md)
```