---
title: ES6 Features
type: concept
tags: [javascript, es6, ecmascript]
status: draft
last_updated: 2026-05-09
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2969-L2969
  - js-allonge:normalized:L2985-L2985
  - js-allonge:normalized:L3527-L3527
  - js-allonge:normalized:L3585-L3585
  - js-allonge:normalized:L4835-L4835
---

# ES6 Features

## Summary

ECMAScript 2015 (ES6) introduced significant enhancements to JavaScript, including new variable declarations, default parameters, destructuring assignment, and generator functions. These features improve code clarity, reduce boilerplate, and enable more expressive programming patterns.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Default parameter values can be specified in function definitions to provide fallbacks when arguments are omitted. | "**const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_" | `normalized:L2969-L2969` | [Source](../sources/js-allonge.md) |
| Array destructuring allows extracting values from arrays using a pattern matching syntax, with optional default values for missing elements. | "**const** [first, second = "two"] = ["one"];" | `normalized:L2985-L2985` | [Source](../sources/js-allonge.md) |
| Block-scoped variables declared with 'let' maintain their scope within the enclosing block and do not interfere with outer scopes. | "(() => { **let** age = 49; **if** ( **true** ) { **let** age = 50; } **return** age; })() _//=> 49_" | `normalized:L3527-L3527` | [Source](../sources/js-allonge.md) |
| Variables declared with 'var' are function-scoped rather than block-scoped, causing redeclarations to overwrite previous values in the same scope. | "(() => { **var** age = 49; **if** ( **true** ) { **var** age = 50; } **return** age; })() _//=> 50_" | `normalized:L3585-L3585` | [Source](../sources/js-allonge.md) |
| The spread operator enables the expansion of iterable elements into array literals or function arguments, enhancing flexibility in handling collections. | "As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator (...) can spread the elements of an array in an..." | `normalized:L4835-L4835` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
