---
title: "Source: js-allonge"
type: source
source_id: js-allonge
source_type: pdf
raw_path: ../../raw/imported/js-allonge/
normalized_path: ../../raw/normalized/js-allonge/
status: draft
last_updated: 2026-05-11
tags: []
sources:
  - ../../raw/imported/js-allonge/original.pdf
---

# Source: js-allonge

## Summary

**JavaScript Allongé, the "Six" Edition** Programming from Functions to Classes in ECMAScript 2015 This book is for sale at http://leanpub.com/javascriptallongesix This version was published on 2017-11-03

Extracted 445 claims from 19 chunks, organized into 10 viable topics.

### Extraction Metadata

- Claim count: 445
- Topic count: 10
- Generation: summary (llm), tables (deterministic)

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| ECMAScript 2015 allows collecting variable arguments into a parameter using rest | "We can also write:   **function** foo (first, ...rest) { _// ..._   }" | `normalized:L165-L167` |
| Variable argument handling in JavaScript before ES6 required manual slicing of a | "Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into " | `normalized:L147-L150` |
| Using let in loops avoids issues with closures capturing the final loop variable | "let introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; for (let i = 0; i < 3; i++) { introd" | `normalized:L3663-L3663` |
| Functions can be used to implement list printing functionality. | "print = (list) => list( () => "", (aPair) => ` ${ aPair(pairFirst) } ${ print(aPair(pairRest)) } ` )" | `normalized:L4277-L4277` |
| Parameters in a function definition allow values to be passed into the function. | "function greet(name) { console.log(`Hello, ${name}!`); }" | `normalized:L100-L100` |
| A function can have default parameter values assigned when no argument is provid | "function greet(name = 'World') { return `Hello, ${name}!`; }" | `normalized:L100-L100` |
| ECMAScript 2015 introduced block-structured variables allowing local scoping in  | "With ECMASCript 2015, we can write:   **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }  " | `normalized:L157-L158` |
| ECMAScript 2015 adds features that make programming techniques easier to explain | "ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things " | `normalized:L183-L183` |
| Before ES6, JavaScript required workarounds like IIFEs to achieve block scoping. | "Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a tr" | `normalized:L137-L140` |
| JavaScript supports iteration through iterables and generators introduced in ES6 | "Iteration and Iterables . . . . . . . . . . . . .\|. . . . . . . . . . . . . . . . . . . . . . . .\|" | `normalized:L79-L79` |

### Extracted Topics

| Topic | Claims | Sections | Status | Notes |
|---|---|---|---|---|
| Functions | 206 | 72 | synthesized |  |
| Iterators | 76 | 28 | synthesized |  |
| Data Types | 44 | 21 | synthesized |  |
| Arrays | 27 | 14 | synthesized |  |
| Control Flow | 26 | 15 | synthesized |  |
| Objects | 21 | 10 | synthesized |  |
| Functional Programming | 20 | 14 | synthesized |  |
| ES6 Features | 14 | 10 | synthesized |  |
| Recursion | 6 | 4 | synthesized |  |
| Strings | 3 | 2 | synthesized |  |
| Closures | 2 | 2 | deferred | Too few claims (2 < 3) |

## Major concepts

| Concept | Page | Status | Claims Used | Claims Available | Section Coverage |
|---|---|---|---|---|---|
| Arrays | `../concepts/arrays.md` | not_started | - | 27 | - |
| Control Flow | `../concepts/control-flow.md` | not_started | - | 26 | - |
| Data Types | `../concepts/data-types.md` | not_started | - | 44 | - |
| ES6 Features | `../concepts/es6-features.md` | not_started | - | 14 | - |
| Functional Programming | `../concepts/functional-programming.md` | not_started | - | 20 | - |
| Functions | `../concepts/functions.md` | not_started | - | 206 | - |
| Iterators | `../concepts/iterators.md` | not_started | - | 76 | - |
| Objects | `../concepts/objects.md` | not_started | - | 21 | - |
| Recursion | `../concepts/recursion.md` | not_started | - | 6 | - |
| Strings | `../concepts/strings.md` | not_started | - | 3 | - |

### Candidate Concepts

| Candidate | Canonical Slug | Priority | Claims | Sections | Sources | Status |
|---|---|---|---|---|---|---|
| Arrays | arrays | must create | 27 | 14 | 1 | discovered |
| Control Flow | control-flow | must create | 26 | 15 | 1 | discovered |
| Data Types | data-types | must create | 44 | 21 | 1 | discovered |
| ES6 Features | es6-features | must create | 14 | 10 | 1 | discovered |
| Functional Programming | functional-programming | must create | 20 | 14 | 1 | discovered |
| Functions | functions | must create | 206 | 72 | 1 | discovered |
| Iterators | iterators | must create | 76 | 28 | 1 | discovered |
| Objects | objects | must create | 21 | 10 | 1 | discovered |
| Recursion | recursion | should create | 6 | 4 | 1 | discovered |
| Strings | strings | could create | 3 | 2 | 1 | discovered |

### Source Locator Map

| Lines | Topic | Source Heading |
|---|---|---|
| 3-24 | - | Reg "raganwald" Braithwaite |
| 25-56 | - | **Contents** |
| 57-90 | Arrays, Iterators | CONTENTS |
| 91-106 | Arrays, Closures | **A Pull of the Lever: Prefaces** |
| 107-116 | Functions | **About JavaScript Allongé** |
| 117-172 | Control Flow, ES6 Features | **why the "six" edition?** |
| 173-194 | ES6 Features, Functional Programming | **that's nice. is that the only reason?** |
| 195-228 | Functional Programming, Functions | **What JavaScript Allongé is. And isn't.** |
| 229-244 | - | **how this book is organized** |
| 245-280 | - | **Foreword to the "Six" edition** |
| 281-282 | - | **Forewords to the First Edition** |
| 283-296 | - | **michael fogus** |
| 297-320 | - | **matthew knox** |
| 321-336 | - | **About The Sample PDF** |
| 337-352 | - | **Prelude: Values and Expressions over Coffee** |
| 353-358 | Data Types | **values are expressions** |
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
| Arrays | [../concepts/arrays.md](../concepts/arrays.md) | Deep extraction | must create | 27 claims covering array, arrays, javascript | created |
| Control Flow | [../concepts/control-flow.md](../concepts/control-flow.md) | Deep extraction | must create | 26 claims covering argument, before, javascript | created |
| Data Types | `../concepts/data-types.md` | Deep extraction | must create | 44 claims covering expressions, javascript, uses | not created yet |
| ES6 Features | [../concepts/es6-features.md](../concepts/es6-features.md) | Deep extraction | must create | 14 claims covering adds, allows, ecmascript | created |
| Functional Programming | [../concepts/functional-programming.md](../concepts/functional-programming.md) | Deep extraction | must create | 20 claims covering combinator, functional, higher | created |
| Functions | [../concepts/functions.md](../concepts/functions.md) | Deep extraction | must create | 206 claims covering book, functions, javascript | created |
| Iterators | [../concepts/iterators.md](../concepts/iterators.md) | Deep extraction | must create | 76 claims covering function, generators, iterator | created |
| Objects | [../concepts/objects.md](../concepts/objects.md) | Deep extraction | must create | 21 claims covering javascript, objects | created |
| Recursion | [../concepts/recursion.md](../concepts/recursion.md) | Deep extraction | should create | 6 claims covering function, functions, linear | created |
| Strings | [../concepts/strings.md](../concepts/strings.md) | Deep extraction | could create | 3 claims covering literal, quasi | created |
