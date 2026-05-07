---
title: Closures
type: concept
tags: [javascript, functional programming, scope]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1275-L1275
  - js-allonge:normalized:L1307-L1307
  - js-allonge:normalized:L1356-L1356
  - js-allonge:normalized:L1697-L1700
  - js-allonge:normalized:L1743-L1754
  - js-allonge:normalized:L9438-L9462
---

# Closures

## Summary

A closure occurs when a function 'remembers' and has access to variables from its outer lexical scope, even after the outer function has finished executing. This mechanism enables functions to maintain private state and create encapsulated behavior.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| A closure is formed when a function contains one or more free variables, allowing it to retain access to variables from its enclosing scope even after the outer function has returned. | "Functions containing one or more free variables are called closures." | `normalized:L1275-L1275` | [Source](../sources/js-allonge.md) |
| When a function is executed, its environment includes bindings from both its local scope and the scopes of its outer functions, and variables with the same name in inner scopes can shadow those in... | "The environment for ((y) => x)(2) is actually {y: 2, '..': {x: 1, ...}}" | `normalized:L1307-L1307` | [Source](../sources/js-allonge.md) |
| When a function is executed, its environment includes bindings from both its local scope and the scopes of its outer functions, and variables with the same name in inner scopes can shadow those in... | "When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor." | `normalized:L1356-L1356` | [Source](../sources/js-allonge.md) |
| Closures enable the creation of functions that maintain private state, such as constants like PI, which can be accessed by inner functions without being exposed globally. | "const PI = 3.14159265; return (diameter) => diameter * PI" | `normalized:L1697-L1700` | [Source](../sources/js-allonge.md) |
| Closures enable the creation of functions that maintain private state, such as constants like PI, which can be accessed by inner functions without being exposed globally. | "((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265)" | `normalized:L1743-L1754` | [Source](../sources/js-allonge.md) |
| The behavior of closures allows for the preservation of variable state across multiple invocations of a function, as demonstrated by a game state management function that retains its internal... | "const statefulNaughtsAndCrosses = () => { const state = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]; return (x = false) => { if (x) { if (state[x] === ' ') { state[x] = 'x'; } else throw..." | `normalized:L9438-L9462` | [Source](../sources/js-allonge.md) |

## Why it matters

Closures are fundamental to functional programming patterns in JavaScript, enabling the creation of private variables, modules, and higher-order functions. They allow developers to encapsulate data and behavior together, leading to more modular and maintainable code.

## Related pages

- [Functional Programming](../concepts/functional-programming.md)
- [Iterators](../concepts/iterators.md)
- [Objects](../concepts/objects.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
