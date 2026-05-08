---
title: Control Flow
type: concept
tags: []
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
---

# Control Flow

Control flow in JavaScript refers to the order in which statements are executed and how program execution can be altered through various constructs. Key aspects include the evolution of variable scoping mechanisms, the behavior of logical operators as control structures, and techniques for managing loop variable bindings to avoid common pitfalls.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Prior to ES6, JavaScript did not support block-structured variables, requiring workarounds like IIFEs. | "**var** i; **for** (i = 0; i < array.length; ++i) { ( **function** (i) { _// ..._ })(i) } To create the same scoping with an Immediately Invoked Function Expression, or "IIFE."" | normalized:L137-L141 | [Source](../sources/js-allonge.md) |
| The logical operators && and || are control-flow operators that use short-circuit evaluation instead of returning boolean values. | normalized:L2261-L2265 | [Source](../sources/js-allonge.md) |
| The logical operators || and && do not always return true or false, and they have short-cut semantics. | normalized:L2285-L2285 | [Source](../sources/js-allonge.md) |
| The || operator returns the value of the left-hand expression if it is truthy, otherwise it evaluates and returns the right-hand expression. | normalized:L2267-L2271 | [Source](../sources/js-allonge.md) |
| Using var in loops can lead to unexpected behavior due to functional scoping, where variables persist in the surrounding environment beyond the loop. | "**var** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **var** i = 0; i < 3; i++) { introductions[i] = "Hello, my name is " + names[i] } introductions _//=> [ 'Hello, my name..." | normalized:L3641-L3649 | [Source](../sources/js-allonge.md) |
| JavaScript's for loop with var creates a single binding for the loop variable, which persists outside the loop body, unlike let which creates a new binding per iteration. | "**var** sum = 0; **for** ( **var** i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050" | normalized:L3629-L3629 | [Source](../sources/js-allonge.md) |
| Lazy evaluation can be achieved by composing functions that process data incrementally rather than processing all elements upfront, avoiding unnecessary computation. | "This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:" | normalized:L4019-L4019 | [Source](../sources/js-allonge.md) |
| The author maintains a blog called Raganwald where he writes about programming. | "He writes about programming on "Raganwald[222] ," as well as general-purpose ruminations on "Braythwayt Dot Com[223] "." | normalized:L6479-L6479 | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding control flow is essential for writing predictable and efficient JavaScript code. The evolution from var to let and const has significantly impacted how developers manage scope and avoid common bugs. Logical operators serving as control structures provide powerful yet subtle ways to express conditional logic, while proper loop variable handling prevents scoping issues that can lead to hard-to-debug problems. These concepts form the foundation for more advanced programming patterns and contribute to writing cleaner, more maintainable code.

## Source pages

- [Source](../sources/js-allonge.md)
```