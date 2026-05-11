---
title: Functions
type: concept
tags: [javascript, programming, functions]
status: draft
last_updated: 2026-05-11
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1029-L1029
  - js-allonge:normalized:L109-L110
  - js-allonge:normalized:L113-L113
  - js-allonge:normalized:L573-L574
  - js-allonge:normalized:L575-L577
  - js-allonge:normalized:L863-L863
  - js-allonge:normalized:L997-L997
  - js-allonge:normalized:L999-L999
---

# Functions

## Summary

Functions are central to programming with functions, serving as first-class citizens in JavaScript that enable powerful abstractions like closures and lexical scoping. They allow for expressive code composition and are foundational to concepts such as pure functions and function application.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript Allongé is fundamentally a book about programming with functions, utilizing JavaScript due to its widespread adoption and support for first-class functions with lexical scope. | "JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of..." | `normalized:L109-L110` | [Source](../sources/js-allonge.md) |
| The book offers practical guidance on employing functions to develop software that is more straightforward, cleaner, and less convoluted compared to object-centric or code-centric methodologies. | "It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms..." | `normalized:L113-L113` | [Source](../sources/js-allonge.md) |
| A pure function is defined as one that contains no free variables, making it predictable and easier to understand regardless of where it is used. | "- Functions containing no free variables are called _pure functions_ ." | `normalized:L997-L997` | [Source](../sources/js-allonge.md) |
| A closure is characterized by containing one or more free variables, allowing it to retain access to variables from its outer scope even after the outer function has finished executing. | "- Functions containing one or more free variables are called _closures_ ." | `normalized:L999-L999` | [Source](../sources/js-allonge.md) |
| When a function is applied to arguments, its execution environment includes a reference to its parent environment, which enables variable lookup in enclosing scopes. | "The environment for ((y) => x)(2) is _actually_ {y: 2, '..': {x: 1, ...}}. '..' means something like "parent" or "enclosure" or "super-environment." It's (x) => ...'s environment, because the..." | `normalized:L1029-L1029` | [Source](../sources/js-allonge.md) |
| Applying a function in JavaScript involves supplying it with zero or more arguments, producing a value similar to how arithmetic operations yield results. | "Here's how we apply a function to some values in JavaScript: Let's say that _fn_expr_ is an expression that when evaluated, produces a function. Let's call the arguments _args_ . Here's how to..." | `normalized:L575-L577` | [Source](../sources/js-allonge.md) |
| The process of applying functions in JavaScript mirrors how mathematical functions operate, where the act of applying a function to arguments results in a computed value. | "Let's put functions to work. The way we use functions is to _apply_ them to zero or more values called _arguments_ . Just as 2 + 2 produces a value (in this case 4), applying a function to zero or..." | `normalized:L573-L574` | [Source](../sources/js-allonge.md) |
| JavaScript follows a call-by-value evaluation strategy, meaning expressions passed to functions are evaluated prior to function invocation, and the resulting values are used in the function's... | "Like most contemporary programming languages, JavaScript uses the "call by value" evaluation strategy[23] . That means that when you write some code that appears to apply a function to an..." | `normalized:L863-L863` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
