---
page_id: javascriptallonge-iteration
page_kind: concept
summary: Iteration: 2 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iteration@1d712d47992d3deafb6a64908bd35e8e
---

# Iteration

What [[javascriptallonge]] covers about iteration:

## Statements

### Iteration and Iterables

- 186

Served by the Pot: Collections **const** stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) _//=> 6_

We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method: **const** collectionSum = (collection) => { **const** iterator = collection.iterator(); **let** eachIteration, sum = 0; **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 6_

If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

This is a good thing.

## **iterator objects**

Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators.

In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-00250))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Iteration and Iterables: 186  Served by the Pot: Collections **const** stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) _//=> 6_  We could save a ... [truncated] (2 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Iteration and Iterables: 186  Served by the Pot: Collections **const** stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) _//=> 6_  We could save a ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
