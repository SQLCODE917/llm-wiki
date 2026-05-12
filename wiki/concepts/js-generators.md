---
title: JavaScript Generators
type: concept
tags: [javascript, functions, iteration, control-flow]
status: draft
last_updated: 2026-05-12
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L5077-L5079
  - js-allonge:normalized:L5141-L5146
  - js-allonge:normalized:L5147-L5147
---

# JavaScript Generators

## Summary

JavaScript generators are a special type of function that can be paused and resumed during execution, allowing for the creation of iterators in a more declarative way. They use the `function*` syntax and the `yield` keyword to produce values one at a time.

## Source-backed details

| Claim | Evidence |
| --- | --- |
| A generator is a specific kind of iterator created using a special function declaration syntax that includes an asterisk, which allows for yielding values one at a time rather than returning them... | [js-allonge:claim_js-allonge_c013_099222bb] |
| When a generator function is invoked, it returns an iterator object that can be used to control the execution of the function step-by-step through the yielded values. | [js-allonge:claim_js-allonge_c013_513de41b] |
| Generators are particularly useful for modeling iterables as state machines, such as generating sequences like the Fibonacci series, where each value depends on the previous ones. | [js-allonge:claim_js-allonge_c013_e316f362] |

## Why it matters

Generators provide a powerful mechanism for creating iterable objects and managing asynchronous operations. They enable lazy evaluation and help in writing clean, readable code for complex iteration patterns, such as infinite sequences or state machines.

## Related pages

- [JavaScript Functions](../concepts/js-functions.md)
- [JavaScript Iterators](../concepts/js-iterators.md)
- [JavaScript Iterables](../concepts/js-iterables.md)
- [JavaScript Control Flow](../concepts/js-control-flow.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
