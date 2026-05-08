---
title: ES6 Features
type: concept
tags: []
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
---

# ES6 Features

ECMAScript 2015 introduced several key features that improved JavaScript's handling of scope and function parameters, including block-scoped variables and rest syntax for collecting arguments.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| ECMAScript 2015 introduced block-structured variables allowing local scoping in loops. | "**for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }" | normalized:L157-L158 | [Source](../sources/js-allonge.md) |
| ECMAScript 2015 allows functions to collect a variable number of arguments into a parameter using rest syntax. | "**function** foo (first, ...rest) { _// ..._ }" | normalized:L165-L167 | [Source](../sources/js-allonge.md) |
| The let keyword provides block scoping which avoids issues with closures in loops where variables would otherwise retain their final value after the loop completes. | "**let** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **let** i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, **${** soAndSo **}** , my name is **${** names[i]..." | normalized:L3663-L3663 | [Source](../sources/js-allonge.md) |
| Block-scoped variables declared with let provide cleaner syntax compared to immediately-invoked function expressions (IIFEs) for avoiding closure issues. | "The error wouldn't exist at all if we'd used let in the first place **let** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **let** i = 0; i < 3; i++) { introductions[i] =..." | normalized:L3661-L3663 | [Source](../sources/js-allonge.md) |

## Why it matters

These ES6 features address common pitfalls in JavaScript programming, particularly around variable scoping and function argument handling. The introduction of `let` and block scoping resolves issues with closures in loops, making code more predictable and easier to reason about. Additionally, rest syntax simplifies working with variable-length argument lists, leading to more flexible and readable function definitions.

## Source pages

- [Source](../sources/js-allonge.md)
```