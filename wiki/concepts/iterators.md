---
title: Iterators
type: concept
tags: [javascript, iteration, functions]
status: draft
last_updated: 2026-05-08
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L3973-L3973
  - js-allonge:normalized:L3981-L3981
  - js-allonge:normalized:L3999-L3999
  - js-allonge:normalized:L4791-L4791
  - js-allonge:normalized:L4801-L4801
  - js-allonge:normalized:L4817-L4817
  - js-allonge:normalized:L4835-L4835
  - js-allonge:normalized:L5143-L5143
  - js-allonge:normalized:L5269-L5269
---

# Iterators

## Summary

An iterator in JavaScript is an object that provides a sequence of values, typically through a next() method or generator function. Iterators enable lazy evaluation and allow for efficient processing of potentially infinite sequences without loading all elements into memory at once.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| An iterator can be implemented either as a function that returns an object with a next method or as a generator function, allowing for lazy evaluation of sequences. | "1. We declare the function using the function * syntax. Not a fat arrow. Not a plain function." | `normalized:L5143-L5143` | [Source](../sources/js-allonge.md) |
| An iterator can be implemented either as a function that returns an object with a next method or as a generator function, allowing for lazy evaluation of sequences. | "**const** ThreeNumbers = { [Symbol.iterator]: **function** * () { **yield** 1; **yield** 2; **yield** 3 } } **for** ( **const** i **of** ThreeNumbers) { console.log(i); } _//=>_ 1 2 3..." | `normalized:L5269-L5269` | [Source](../sources/js-allonge.md) |
| An iterator can be implemented either as a function that returns an object with a next method or as a generator function, allowing for lazy evaluation of sequences. | "**const** ThreeNumbers = { [Symbol.iterator]: **function** * () { **yield** 1; **yield** 2; **yield** 3 } } **for** ( **const** i **of** ThreeNumbers) { console.log(i); } _//=>_ 1 2 3..." | `normalized:L5269-L5269` | [Source](../sources/js-allonge.md) |
| Iterator functions can be composed to create new iterators, such as mapping or filtering operations, which transform existing iterators into different sequences. | "This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take, an easy function that returns..." | `normalized:L3981-L3981` | [Source](../sources/js-allonge.md) |
| Iterator functions can be composed to create new iterators, such as mapping or filtering operations, which transform existing iterators into different sequences. | "**const** mapIteratorWith = (fn, iterator) => () => { **const** {done, value} = iterator(); **return** ({done, value: done ? **undefined** : fn(value)}); } **const** squares = mapIteratorWith((x)..." | `normalized:L3973-L3973` | [Source](../sources/js-allonge.md) |
| Iterator functions can be composed to create new iterators, such as mapping or filtering operations, which transform existing iterators into different sequences. | "**const** filterIteratorWith = (fn, iterator) => () => { **do** { **const** {done, value} = iterator(); } **while** (!done && !fn(value)); **return** {done, value}; }" | `normalized:L3999-L3999` | [Source](../sources/js-allonge.md) |
| Objects can implement the Symbol.iterator method to make them iterable, enabling their use with for...of loops and the spread operator. | "The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object." | `normalized:L4791-L4791` | [Source](../sources/js-allonge.md) |
| Objects can implement the Symbol.iterator method to make them iterable, enabling their use with for...of loops and the spread operator. | "**const** Stack3 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this**..." | `normalized:L4801-L4801` | [Source](../sources/js-allonge.md) |
| Objects can implement the Symbol.iterator method to make them iterable, enabling their use with for...of loops and the spread operator. | "The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object." | `normalized:L4791-L4791` | [Source](../sources/js-allonge.md) |
| Objects can implement the Symbol.iterator method to make them iterable, enabling their use with for...of loops and the spread operator. | "Indeed we do. Behold the for...of loop:" | `normalized:L4817-L4817` | [Source](../sources/js-allonge.md) |
| Objects can implement the Symbol.iterator method to make them iterable, enabling their use with for...of loops and the spread operator. | "As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator (...) can spread the elements of an array in an..." | `normalized:L4835-L4835` | [Source](../sources/js-allonge.md) |

## Why it matters

Iterators provide a standardized way to traverse collections and define custom iteration behavior. They support constructs like for...of loops and the spread operator, making code more expressive and enabling functional programming patterns such as mapping and filtering over sequences.

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
