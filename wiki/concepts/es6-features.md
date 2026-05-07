---
title: ES6 Features
type: concept
tags: [javascript, ecmascript, es6, syntax, programming]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L267-L270
  - js-allonge:normalized:L382-L389
  - js-allonge:normalized:L4817-L4820
  - js-allonge:normalized:L4866-L4874
  - js-allonge:normalized:L4884-L4892
  - js-allonge:normalized:L5017-L5018
  - js-allonge:normalized:L6877-L6879
  - js-allonge:normalized:L6881-L6882
  - js-allonge:normalized:L7792-L7793
  - js-allonge:normalized:L7801-L7805
  - js-allonge:normalized:L8953-L8964
---

# ES6 Features

## Summary

ECMAScript 6 (ES6), also known as ES2015, introduced significant enhancements to JavaScript, including new syntax, improved variable scoping, and powerful new features like generators and modules.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| ECMAScript 6 brought substantial improvements beyond simple syntactic sugar, enabling easier implementation of advanced programming techniques. | "ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. It makes a number of interesting programming techniques easy to explain..." | `normalized:L267-L270` | [Source](../sources/js-allonge.md) |
| ES6 introduced new variable declarations 'let' and 'const', which provide block-scoped alternatives to the traditional 'var' keyword, helping prevent common scoping issues. | "let age = 52; age = 53; age //=> 53" | `normalized:L4817-L4820` | [Source](../sources/js-allonge.md) |
| ES6 introduced new variable declarations 'let' and 'const', which provide block-scoped alternatives to the traditional 'var' keyword, helping prevent common scoping issues. | "(() => { let age = 49; if (true) { const age = 50; } age = 51; return age; })() //=> 51" | `normalized:L4866-L4874` | [Source](../sources/js-allonge.md) |
| ES6 introduced new variable declarations 'let' and 'const', which provide block-scoped alternatives to the traditional 'var' keyword, helping prevent common scoping issues. | "(() => { const age = 49; if (true) { let age = 50; } age = 52; return age; })() //=> ERROR: age is read-only" | `normalized:L4884-L4892` | [Source](../sources/js-allonge.md) |
| ES6 introduced new variable declarations 'let' and 'const', which provide block-scoped alternatives to the traditional 'var' keyword, helping prevent common scoping issues. | "const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var" | `normalized:L5017-L5018` | [Source](../sources/js-allonge.md) |
| ES6 expanded JavaScript's capabilities through new syntax, standard library additions, and entirely novel features such as generators, proxies, and symbols. | "ECMAScript 6 has three major groups of features: • Better syntax for features that already exist (e.g. via libraries). For example: classes and modules. • New functionality in the standard..." | `normalized:L382-L389` | [Source](../sources/js-allonge.md) |
| ES6 expanded JavaScript's capabilities through new syntax, standard library additions, and entirely novel features such as generators, proxies, and symbols. | "JavaScript provides a symbol. Symbols are unique constants that are guaranteed not to conflict with existing strings." | `normalized:L6877-L6879` | [Source](../sources/js-allonge.md) |
| ES6 expanded JavaScript's capabilities through new syntax, standard library additions, and entirely novel features such as generators, proxies, and symbols. | "The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object." | `normalized:L6881-L6882` | [Source](../sources/js-allonge.md) |
| ES6 expanded JavaScript's capabilities through new syntax, standard library additions, and entirely novel features such as generators, proxies, and symbols. | "const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } }" | `normalized:L7801-L7805` | [Source](../sources/js-allonge.md) |
| ES6 expanded JavaScript's capabilities through new syntax, standard library additions, and entirely novel features such as generators, proxies, and symbols. | "This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:" | `normalized:L7792-L7793` | [Source](../sources/js-allonge.md) |
| ES6 expanded JavaScript's capabilities through new syntax, standard library additions, and entirely novel features such as generators, proxies, and symbols. | "return ({ *[Symbol.iterator] () { let [x, y] = position; while (x >= 0 && y >=0 && x < size && y < size) { const direction = board[y][x]; yield direction; [x, y] = MOVE[direction]([x, y]); } } });" | `normalized:L8953-L8964` | [Source](../sources/js-allonge.md) |

## Related pages

- [Functional Programming](../concepts/functional-programming.md)
- [Iterators](../concepts/iterators.md)
- [Objects](../concepts/objects.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
