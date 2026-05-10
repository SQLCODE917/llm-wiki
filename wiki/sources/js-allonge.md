---
title: "Source: js-allonge"
type: source
source_id: js-allonge
source_type: pdf
raw_path: ../../raw/imported/js-allonge/
normalized_path: ../../raw/normalized/js-allonge/
status: draft
last_updated: 2026-05-09
tags: []
sources:
  - ../../raw/imported/js-allonge/original.pdf
---

# Source: js-allonge

## Summary

**JavaScript Allongé, the "Six" Edition** Programming from Functions to Classes in ECMAScript 2015 This book is for sale at http://leanpub.com/javascriptallongesix This version was published on 2017-11-03

Extracted 454 claims from 19 chunks, organized into 10 viable topics.

### Extraction Metadata

- Claim count: 454
- Topic count: 10
- Generation: summary (llm), tables (deterministic)

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| ECMAScript 2015 introduced features that make programming with functions easier  | "ECMAScript 2015 (formerly called ECMAScript 6 or "ES6"), is ushering in a very large number of impro" | `normalized:L119-L120` |
| ECMAScript 2015 allows functions to have a variable number of arguments collecte | "With ECMASCript 2015, we can write: for (let i = 0; i < array.length; ++i) { // ... } And i is scope" | `normalized:L155-L168` |
| The length function can be expressed as a fold operation with a terminal value o | "const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);" | `normalized:L2767-L2767` |
| Destructuring can be applied to function parameters to extract nested values. | "const description = ({name: { first: given }, occupation: { title: title } }) => ` ${ given } is a $" | `normalized:L3255-L3255` |
| A for loop with let creates a new binding for each iteration, preventing closure | "for ( let i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, ${ soAndSo }, my name is ${ n" | `normalized:L3663-L3663` |
| An iterator is a function that returns objects with done and value properties. | "We can write a different iterator for a different data structure. Here's one for linked lists: **con" | `normalized:L3935-L3935` |
| Default parameters allow specifying fallback values for function arguments. | "function greet(name = 'World') {   return `Hello ${name}`; }" | `normalized:L162-L164` |
| Falsy values in JavaScript include false, null, undefined, NaN, 0, and empty str | "Every other value in JavaScript is "truthy" except the aforementioned false, null, undefined, NaN, 0" | `normalized:L2205-L2205` |
| All values in JavaScript except for false, null, undefined, NaN, 0, and '' are t | "Every other value in JavaScript is "truthy" except the aforementioned false, null, undefined, NaN, 0" | `normalized:L2205-L2205` |
| ES6 introduces arrow functions which provide a shorter syntax for writing functi | "const add = (a, b) => a + b;" | `normalized:L129-L129` |

### Extracted Topics

| Topic | Claims | Sections | Status | Notes |
|---|---|---|---|---|
| Functions | 255 | 86 | synthesized |  |
| Iterators | 56 | 23 | synthesized |  |
| Data Types | 39 | 22 | synthesized |  |
| Control Flow | 24 | 12 | synthesized |  |
| Arrays | 21 | 13 | synthesized |  |
| Objects | 15 | 8 | synthesized |  |
| Recursion | 14 | 9 | synthesized |  |
| Functional Programming | 14 | 9 | synthesized |  |
| ES6 Features | 11 | 9 | synthesized |  |
| Destructuring | 3 | 1 | synthesized | Single section |
| Closures | 2 | 2 | deferred | Too few claims (2 < 3) |

## Major concepts

| Concept | Page | Status | Claims Used | Claims Available | Section Coverage |
|---|---|---|---|---|---|
| Arrays | [../concepts/arrays.md](../concepts/arrays.md) | draft | - | 21 | 13/216 headings |
| Control Flow | [../concepts/control-flow.md](../concepts/control-flow.md) | draft | - | 24 | 12/216 headings |
| Data Types | [../concepts/data-types.md](../concepts/data-types.md) | draft | - | 39 | 22/216 headings |
| Destructuring | `../concepts/destructuring.md` | not_started | - | 3 | - |
| ES6 Features | `../concepts/es6-features.md` | not_started | - | 11 | - |
| Functional Programming | [../concepts/functional-programming.md](../concepts/functional-programming.md) | draft | - | 14 | 9/216 headings |
| Functions | [../concepts/functions.md](../concepts/functions.md) | draft | - | 255 | 86/216 headings |
| Iterators | [../concepts/iterators.md](../concepts/iterators.md) | draft | - | 56 | 23/216 headings |
| Objects | `../concepts/objects.md` | not_started | - | 15 | - |
| Recursion | [../concepts/recursion.md](../concepts/recursion.md) | draft | - | 14 | 9/216 headings |

### Candidate Concepts

| Candidate | Canonical Slug | Priority | Claims | Sections | Sources | Status |
|---|---|---|---|---|---|---|
| Destructuring | destructuring | could create | 3 | 1 | 1 | discovered |
| ES6 Features | es6-features | must create | 11 | 9 | 1 | discovered |
| Objects | objects | must create | 15 | 8 | 1 | discovered |

### Source Locator Map

| Lines | Topic | Source Heading |
|---|---|---|
| 3-24 | - | Reg "raganwald" Braithwaite |
| 25-56 | - | **Contents** |
| 57-90 | Functions | CONTENTS |
| 91-106 | Control Flow, Data Types | **A Pull of the Lever: Prefaces** |
| 107-116 | Arrays, Closures | **About JavaScript Allongé** |
| 117-172 | Arrays, Control Flow | **why the "six" edition?** |
| 173-194 | Functions | **that's nice. is that the only reason?** |
| 195-228 | Functions | **What JavaScript Allongé is. And isn't.** |
| 229-244 | Functions | **how this book is organized** |
| 245-280 | - | **Foreword to the "Six" edition** |
| 281-282 | - | **Forewords to the First Edition** |
| 283-296 | Functions | **michael fogus** |
| 297-320 | Functions | **matthew knox** |
| 321-336 | - | **About The Sample PDF** |
| 337-352 | - | **Prelude: Values and Expressions over Coffee** |
| 353-358 | - | **values are expressions** |
| 359-364 | - | 42 |
| 365-394 | Data Types | 42 |
| 395-416 | Data Types | **values and identity** |
| 417-432 | Data Types | **value types** |

## Entities

None identified.

## Procedures

None identified.

## References

None identified.

## Open questions

- Additional topics may emerge from deeper analysis

## Related pages

| Candidate page | Intended path | Group | Priority | Evidence basis | Status |
|---|---|---|---|---|---|
| Arrays | [../concepts/arrays.md](../concepts/arrays.md) | Deep extraction | must create | 21 claims covering array, arrays, elements | created |
| Control Flow | [../concepts/control-flow.md](../concepts/control-flow.md) | Deep extraction | must create | 24 claims covering every, javascript, logical | created |
| Data Types | [../concepts/data-types.md](../concepts/data-types.md) | Deep extraction | must create | 39 claims covering expressions, javascript, numbers | created |
| Destructuring | [../concepts/destructuring.md](../concepts/destructuring.md) | Deep extraction | could create | 3 claims covering applied, destructuring, object | created |
| ES6 Features | [../concepts/es6-features.md](../concepts/es6-features.md) | Deep extraction | must create | 11 claims covering declared, default, destructuring | created |
| Functional Programming | [../concepts/functional-programming.md](../concepts/functional-programming.md) | Deep extraction | must create | 14 claims covering functional, functions, linked | created |
| Functions | [../concepts/functions.md](../concepts/functions.md) | Deep extraction | must create | 255 claims covering book, functions, javascript | created |
| Iterators | [../concepts/iterators.md](../concepts/iterators.md) | Deep extraction | must create | 56 claims covering composed, evaluation, function | created |
| Objects | `../concepts/objects.md` | Deep extraction | must create | 15 claims covering javascript, literals, object | not created yet |
| Recursion | [../concepts/recursion.md](../concepts/recursion.md) | Deep extraction | must create | 14 claims covering linear, recursion, self | created |
