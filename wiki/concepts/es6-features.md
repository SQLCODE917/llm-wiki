---
title: ES6 Features
type: concept
tags: [javascript, ecmascript, syntax, functions, variables]
status: draft
last_updated: 2026-05-11
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L165-L167
  - js-allonge:normalized:L183-L183
  - js-allonge:normalized:L2969-L2969
  - js-allonge:normalized:L3519-L3521
  - js-allonge:normalized:L3527-L3527
  - js-allonge:normalized:L3547-L3547
  - js-allonge:normalized:L3585-L3585
---

# ES6 Features

## Summary

ES6, also known as ECMAScript 2015, introduced significant enhancements to JavaScript, including new syntax, variable scoping, functional programming tools, and iterator protocols that improve code expressiveness and maintainability.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| ES6 enhances JavaScript by introducing syntactic sugar and simplifying common programming patterns, making advanced techniques more accessible. | "ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. It makes a number of interesting programming techniques easy to explain..." | `normalized:L183-L183` | [Source](../sources/js-allonge.md) |
| The introduction of let and const variables provides better scoping control compared to var, preventing issues related to hoisting and block scope. | "**let** age = 52; age = 53; age _//=> 53_" | `normalized:L3519-L3521` | [Source](../sources/js-allonge.md) |
| The introduction of let and const variables provides better scoping control compared to var, preventing issues related to hoisting and block scope. | "(() => { **let** age = 49; **if** ( **true** ) { **let** age = 50; } **return** age; })() _//=> 49_" | `normalized:L3527-L3527` | [Source](../sources/js-allonge.md) |
| The introduction of let and const variables provides better scoping control compared to var, preventing issues related to hoisting and block scope. | "(() => { **let** age = 49; **if** ( **true** ) { age = 50; } **return** age; })() _//=> 50_" | `normalized:L3547-L3547` | [Source](../sources/js-allonge.md) |
| The introduction of let and const variables provides better scoping control compared to var, preventing issues related to hoisting and block scope. | "(() => { **var** age = 49; **if** ( **true** ) { **var** age = 50; } **return** age; })() _//=> 50_" | `normalized:L3585-L3585` | [Source](../sources/js-allonge.md) |
| ES6 supports default parameters, rest parameters, and arrow functions which facilitate functional programming paradigms such as recursion and higher-order functions. | "**function** foo (first, ...rest) { _// ..._ }" | `normalized:L165-L167` | [Source](../sources/js-allonge.md) |
| ES6 supports default parameters, rest parameters, and arrow functions which facilitate functional programming paradigms such as recursion and higher-order functions. | "**const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_" | `normalized:L2969-L2969` | [Source](../sources/js-allonge.md) |

## Related pages

- [Arrays](../concepts/arrays.md)
- [Control Flow](../concepts/control-flow.md)
- [Functional Programming](../concepts/functional-programming.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)
- [Objects](../concepts/objects.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
