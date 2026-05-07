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
  - js-allonge:normalized:L1307-L1308
  - js-allonge:normalized:L1356-L1356
  - js-allonge:normalized:L1703-L1704
  - js-allonge:normalized:L1756-L1758
---

# Closures

## Summary

A closure occurs when a function 'remembers' the variables from its outer (enclosing) scope even after the outer function has finished executing. This mechanism enables functions to maintain access to variables from their creation context, forming a persistent link between the function and its lexical environment.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| A closure is formed when a function contains free variables, allowing it to access variables from its enclosing scope even after the outer function has returned. | "Functions containing one or more free variables are called closures." | `normalized:L1275-L1275` | [Source](../sources/js-allonge.md) |
| When a function is executed, its environment includes references to its parent scope, and variable shadowing can occur if a local variable shares the same name as one in an outer scope. | "The environment for ((y) => x)(2) is actually {y: 2, '..': {x: 1, ...}}. '..' means something like "parent" or "enclosure" or "super-environment."" | `normalized:L1307-L1308` | [Source](../sources/js-allonge.md) |
| When a function is executed, its environment includes references to its parent scope, and variable shadowing can occur if a local variable shares the same name as one in an outer scope. | "When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor." | `normalized:L1356-L1356` | [Source](../sources/js-allonge.md) |
| The lexical scoping rules apply consistently to variable bindings, whether they result from function parameters or constant declarations, ensuring predictable access to variables within nested scopes. | "Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope." | `normalized:L1703-L1704` | [Source](../sources/js-allonge.md) |
| The lexical scoping rules apply consistently to variable bindings, whether they result from function parameters or constant declarations, ensuring predictable access to variables within nested scopes. | "We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding." | `normalized:L1756-L1758` | [Source](../sources/js-allonge.md) |

## Why it matters

Closures are fundamental to functional programming patterns in JavaScript, enabling the creation of private variables, function factories, and maintaining state without global variables. They provide a way to encapsulate data and behavior together, enhancing code modularity and preventing namespace pollution.

## Related pages

- [Functions](../concepts/functions.md)
- [Functional Programming](../concepts/functional-programming.md)

## Candidate pages

- Scope

## Source pages

- [Js Allonge](../sources/js-allonge.md)
