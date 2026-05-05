---
title: ES6 Features
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# ES6 Features

ECMAScript 2015 (ES6) introduced significant improvements that made JavaScript more expressive and easier to write small, powerful components. These enhancements included new syntax, standard library functionality, and entirely new features that transformed how developers approach JavaScript programming.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| ECMAScript 2015 introduced significant improvements that make JavaScript more expressive and easier to write small, powerful components | "ECMAScript 2015 (formerly called ECMAScript 6 or "ES6"), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs." | normalized:L184 | [Source](../sources/js-allonge.md) |
| ES6 added features like destructuring, block-structured variables, iterables, generators, and the class keyword that make JavaScript programming more expressive | "Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive." | normalized:L186 | [Source](../sources/js-allonge.md) |
| ECMAScript 6 was developed as a successor to ECMAScript 3, replacing the abandoned ECMAScript 4 plan with two upgrades | "After internal conflict, a settlement was reached in July 2008 and a new plan was made - to abandon ECMAScript 4 and to replace it with two upgrades:" | normalized:L375 | [Source](../sources/js-allonge.md) |
| ECMAScript 6 introduced three major groups of features: better syntax for existing features, new functionality in the standard library, and completely new features | "ECMAScript 6 has three major groups of features: • Better syntax for features that already exist (e.g. via libraries). For example: classes and modules. • New functionality in the standard library. For example: - New methods for strings and arrays - Promises (for asynchronous programming) - Maps and sets • Completely new features. For example: Generators, proxies and WeakMaps." | normalized:L382 | [Source](../sources/js-allonge.md) |
| Multiple name-value pairs can be bound using const statements by separating them with commas or placing each on a separate line for readability | "We can bind more than one name-value pair by separating them with commas. For readability, most people put one binding per line:" | normalized:L1555 | [Source](../sources/js-allonge.md) |
| Constants declared with const can be rebound within block scopes but not within function scopes | "Names bound with const shadow enclosing bindings just like parameters." | normalized:L1775 | [Source](../sources/js-allonge.md) |
| Left-variadic functions can be implemented using a decorator that gathers arguments from the left side of the parameter list | "const leftVariadic = (fn) => {if (fn.length < 1) {return fn;}else {return function (...args) {const gathered = args.slice(0, args.length - fn.length + 1),spread = args.slice(args.length - fn.length + 1);return fn.apply(this, [gathered].concat(spread));}}}; " | normalized:L2809 | [Source](../sources/js-allonge.md) |
| Default parameters in JavaScript provide a clean way to supply initial values for recursive functions | "const length = ([first, ...rest], numberToBeAdded = 0) => first === undefined ? numberToBeAdded : length(rest, 1 + numberToBeAdded)" | normalized:L4016 | [Source](../sources/js-allonge.md) |
| Variables declared with var are function-scoped, not block-scoped like let and const | "var is not block scoped, it's function scoped, just like function declarations:" | normalized:L4931 | [Source](../sources/js-allonge.md) |
| Let and const were introduced to solve problems with var's functional scoping | "const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var" | normalized:L5017 | [Source](../sources/js-allonge.md) |
| Generator functions use the function* syntax and can use yield and yield* to generate values | "A generator is a function that is defined with function * and uses yield (or yield *) to generate values." | normalized:L8187 | [Source](../sources/js-allonge.md) |
| ES6 generators enable the creation of custom iterators with implicit state management | "We used generators to build iterators that maintain implicit state." | normalized:L9179 | [Source](../sources/js-allonge.md) |

## Why it matters

ES6 features significantly modernized JavaScript by introducing more expressive syntax and powerful constructs that improved code clarity and maintainability. The addition of let and const solved longstanding scoping issues with var, while new features like destructuring, generators, and default parameters provided developers with cleaner ways to handle common programming patterns. These improvements laid the foundation for modern JavaScript development practices and helped bridge the gap between JavaScript and other programming languages.

## Source pages

- [Source](../sources/js-allonge.md)