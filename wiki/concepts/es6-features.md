---
title: ES6 Features
type: concept
tags: [javascript, ecmascript, es6]
status: draft
last_updated: 2026-05-08
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1199-L1200
  - js-allonge:normalized:L1395-L1395
  - js-allonge:normalized:L253-L266
  - js-allonge:normalized:L5149-L5149
  - js-allonge:normalized:L5285-L5285
  - js-allonge:normalized:L5379-L5379
---

# ES6 Features

## Summary

ECMAScript 6 (ES6), also known as ECMAScript 2015, introduced significant enhancements to JavaScript. These include syntactic improvements, new standard library functionalities, and entirely new features like generators and proxies. ES6 aimed to modernize JavaScript while maintaining backward compatibility.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| ECMAScript 6 introduced a structured set of features organized into three main categories: enhanced syntax for existing capabilities, expanded standard library functionality, and entirely new... | "ECMAScript 6 has three major groups of features: - Better syntax for features that already exist (e.g. via libraries). For example: classes and modules. - New functionality in the standard..." | `normalized:L253-L266` | [Source](../sources/js-allonge.md) |
| The const keyword in ES6 provides a way to declare variables that cannot be reassigned, offering immutability for references within their scope, although they can be shadowed. | "(diameter) => { **const** PI = 3.14159265;" | `normalized:L1199-L1200` | [Source](../sources/js-allonge.md) |
| The const keyword in ES6 provides a way to declare variables that cannot be reassigned, offering immutability for references within their scope, although they can be shadowed. | "JavaScript does not permit us to rebind a name that has been bound with const. We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a..." | `normalized:L1395-L1395` | [Source](../sources/js-allonge.md) |
| ES6 brought forth new iteration mechanisms such as generators and the Symbol.iterator protocol, enabling developers to define custom iteration behaviors for objects. | "**function** * empty () {};" | `normalized:L5149-L5149` | [Source](../sources/js-allonge.md) |
| ES6 brought forth new iteration mechanisms such as generators and the Symbol.iterator protocol, enabling developers to define custom iteration behaviors for objects. | "**const** ThreeNumbers = { *[Symbol.iterator] () { **yield** 1; **yield** 2; **yield** 3 } }" | `normalized:L5285-L5285` | [Source](../sources/js-allonge.md) |
| ES6 brought forth new iteration mechanisms such as generators and the Symbol.iterator protocol, enabling developers to define custom iteration behaviors for objects. | "**const** isIterable = (something) => !!something[Symbol.iterator]; **function** * tree (iterable) { **for** ( **const** e **of** iterable) { **if** (isIterable(e)) { **yield** * tree(e); }..." | `normalized:L5379-L5379` | [Source](../sources/js-allonge.md) |

## Why it matters

ES6 features provide developers with more powerful tools for writing clean, expressive, and maintainable code. Concepts like const, let, destructuring, and iterators improve variable scoping, data handling, and iteration patterns, making JavaScript more robust and easier to reason about.

## Related pages

- [Arrays](../concepts/arrays.md)
- [Data Types](../concepts/data-types.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
