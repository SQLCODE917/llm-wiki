---
title: "Source: js-allonge"
type: source
source_id: js-allonge
source_type: pdf
raw_path: ../../raw/imported/js-allonge/
normalized_path: ../../raw/normalized/js-allonge/
status: draft
last_updated: 2026-05-12
tags: []
sources:
  - ../../raw/imported/js-allonge/original.pdf
---

# Source: js-allonge

## Summary

**JavaScript Allongé, the "Six" Edition** Programming from Functions to Classes in ECMAScript 2015 This book is for sale at http://leanpub.com/javascriptallongesix This version was published on 2017-11-03

Extracted 453 claims from 19 chunks, organized into 16 viable topics.

### Extraction Metadata

- Claim count: 453
- Topic count: 16
- Generation: summary (llm), tables (deterministic)

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| ECMAScript 2015 introduced features that make programming with functions more ex | "ECMAScript 2015 (formerly called ECMAScript 6 or "ES6"), is ushering in a very large number of impro" | `normalized:L119-L119` |
| ECMAScript 2015 allows for collecting a variable number of arguments into a para | "We can also write:   **function** foo (first, ...rest) { _// ..._   }" | `normalized:L165-L167` |
| ECMAScript 6 introduced three major groups of features: better syntax, new funct | "ECMAScript 6 has three major groups of features:   - Better syntax for features that already exist (" | `normalized:L253-L265` |
| ECMAScript 2015 allows functions to have a variable number of arguments collecte | "We can also write:   **function** foo (first, ...rest) { _// ..._   }" | `normalized:L165-L167` |
| Prior to ECMAScript 2015, JavaScript required workarounds to collect variable ar | "Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into " | `normalized:L147-L150` |
| Destructuring can be used to simulate multiple return values from functions | "**const** description = (nameAndOccupation) => { **if** (nameAndOccupation.length < 2) { **return** " | `normalized:L2547-L2551` |
| The var keyword is function-scoped and hoisted, which can lead to unexpected beh | "var i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, ${soAndSo}, my name is ${names[i]}`" | `normalized:L3641-L3641` |
| Using let instead of var in loops ensures proper scoping of loop variables for c | "for (let i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, ${soAndSo}, my name is ${names" | `normalized:L3663-L3663` |
| Block-structured variables in ECMAScript 2015 allow for local scoping of variabl | "With ECMASCript 2015, we can write:   **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }  " | `normalized:L157-L157` |
| ECMAScript 2015 introduced block-structured variables allowing local scoping wit | "With ECMASCript 2015, we can write:   **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }  " | `normalized:L157-L157` |

## Major concepts

### Extracted Topics

| Topic | Claims | Sections | Status | Notes |
|---|---|---|---|---|
| Functions | 162 | 69 | not_started |  |
| Control Flow | 58 | 29 | not_started |  |
| Data Types | 56 | 32 | not_started |  |
| Data Structures | 34 | 14 | not_started |  |
| Arrays | 27 | 16 | not_started |  |
| Iterables | 22 | 12 | not_started |  |
| Functional Programming | 15 | 10 | not_started |  |
| Objects | 14 | 10 | not_started |  |
| Variables | 13 | 3 | not_started |  |
| Memory Management | 11 | 7 | not_started |  |
| Collections | 10 | 6 | not_started |  |
| Iterators | 10 | 7 | not_started |  |
| Values | 5 | 3 | not_started |  |
| Recursion | 5 | 4 | not_started |  |
| Algorithms | 5 | 3 | not_started |  |
| Scope | 3 | 1 | not_started | Single section |
| Pattern Matching | 2 | 2 | deferred | Too few claims (2 < 3) |
| Lazy Evaluation | 1 | 1 | deferred | Too few claims (1 < 3) |

| Concept | Page | Status | Claims Used | Claims Available | Section Coverage |
|---|---|---|---|---|---|
| Algorithms | `../concepts/js-algorithms.md` | not_started | - | 5 | - |
| Arrays | `../concepts/js-arrays.md` | not_started | - | 27 | - |
| Collections | `../concepts/js-collections.md` | not_started | - | 10 | - |
| Control Flow | `../concepts/js-control-flow.md` | not_started | - | 58 | - |
| Data Structures | `../concepts/js-data-structures.md` | not_started | - | 34 | - |
| Data Types | `../concepts/js-data-types.md` | not_started | - | 56 | - |
| Functional Programming | `../concepts/js-functional-programming.md` | not_started | - | 15 | - |
| Functions | `../concepts/js-functions.md` | not_started | - | 162 | - |
| Iterables | `../concepts/js-iterables.md` | not_started | - | 22 | - |
| Iterators | `../concepts/js-iterators.md` | not_started | - | 10 | - |
| Memory Management | `../concepts/js-memory-management.md` | not_started | - | 11 | - |
| Objects | `../concepts/js-objects.md` | not_started | - | 14 | - |
| Recursion | `../concepts/js-recursion.md` | not_started | - | 5 | - |
| Scope | `../concepts/js-scope.md` | not_started | - | 3 | - |
| Values | `../concepts/js-values.md` | not_started | - | 5 | - |
| Variables | `../concepts/js-variables.md` | not_started | - | 13 | - |

### Candidate Concepts

| Candidate | Canonical Slug | Priority | Claims | Sections | Sources | Status |
|---|---|---|---|---|---|---|
| Algorithms | js-algorithms | should create | 5 | 3 | 1 | discovered |
| Arrays | js-arrays | must create | 27 | 16 | 1 | discovered |
| Collections | js-collections | must create | 10 | 6 | 1 | discovered |
| Control Flow | js-control-flow | must create | 58 | 29 | 1 | discovered |
| Data Structures | js-data-structures | must create | 34 | 14 | 1 | discovered |
| Data Types | js-data-types | must create | 56 | 32 | 1 | discovered |
| Functional Programming | js-functional-programming | must create | 15 | 10 | 1 | discovered |
| Functions | js-functions | must create | 162 | 69 | 1 | discovered |
| Iterables | js-iterables | must create | 22 | 12 | 1 | discovered |
| Iterators | js-iterators | must create | 10 | 7 | 1 | discovered |
| Memory Management | js-memory-management | must create | 11 | 7 | 1 | discovered |
| Objects | js-objects | must create | 14 | 10 | 1 | discovered |
| Recursion | js-recursion | should create | 5 | 4 | 1 | discovered |
| Scope | js-scope | could create | 3 | 1 | 1 | discovered |
| Values | js-values | should create | 5 | 3 | 1 | discovered |
| Variables | js-variables | must create | 13 | 3 | 1 | discovered |

### Source Locator Map

| Lines | Topic | Source Heading |
|---|---|---|
| 3-24 | - | Reg "raganwald" Braithwaite |
| 25-56 | - | **Contents** |
| 57-90 | - | CONTENTS |
| 91-106 | Arrays, Control Flow | **A Pull of the Lever: Prefaces** |
| 107-116 | Arrays, Control Flow | **About JavaScript Allongé** |
| 117-172 | Arrays, Control Flow | **why the "six" edition?** |
| 173-194 | Functions, Objects | **that's nice. is that the only reason?** |
| 195-228 | Functions, Objects | **What JavaScript Allongé is. And isn't.** |
| 229-244 | Functions | **how this book is organized** |
| 245-280 | Functions | **Foreword to the "Six" edition** |
| 281-282 | - | **Forewords to the First Edition** |
| 283-296 | - | **michael fogus** |
| 297-320 | - | **matthew knox** |
| 321-336 | - | **About The Sample PDF** |
| 337-352 | - | **Prelude: Values and Expressions over Coffee** |
| 353-358 | Values | **values are expressions** |
| 359-364 | - | 42 |
| 365-394 | Data Types, Values | 42 |
| 395-416 | Control Flow, Data Types | **values and identity** |
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
| Algorithms | [../concepts/js-algorithms.md](../concepts/js-algorithms.md) | Deep extraction | should create | 5 claims covering cycle, detection, hare | created |
| Arrays | [../concepts/js-arrays.md](../concepts/js-arrays.md) | Deep extraction | must create | 27 claims covering allows, array, arrays | created |
| Collections | [../concepts/js-collections.md](../concepts/js-collections.md) | Deep extraction | must create | 10 claims covering collections, eager, lazy | created |
| Control Flow | [../concepts/js-control-flow.md](../concepts/js-control-flow.md) | Deep extraction | must create | 58 claims covering allows, ecmascript, introduced | created |
| Data Structures | [../concepts/js-data-structures.md](../concepts/js-data-structures.md) | Deep extraction | must create | 34 claims covering cells, cons, linked | created |
| Data Types | [../concepts/js-data-types.md](../concepts/js-data-types.md) | Deep extraction | must create | 56 claims covering javascript, numbers, strings | created |
| Functional Programming | [../concepts/js-functional-programming.md](../concepts/js-functional-programming.md) | Deep extraction | must create | 15 claims covering allow, composed, folding | created |
| Functions | [../concepts/js-functions.md](../concepts/js-functions.md) | Deep extraction | must create | 162 claims covering book, functions, javascript | created |
| Iterables | [../concepts/js-iterables.md](../concepts/js-iterables.md) | Deep extraction | must create | 22 claims covering iterable, javascript, object | created |
| Iterators | [../concepts/js-iterators.md](../concepts/js-iterators.md) | Deep extraction | must create | 10 claims covering allow, collections, eager | created |
| Memory Management | [../concepts/js-memory-management.md](../concepts/js-memory-management.md) | Deep extraction | must create | 11 claims covering copy, copying, creating | created |
| Objects | [../concepts/js-objects.md](../concepts/js-objects.md) | Deep extraction | must create | 14 claims covering edition, javascript, object | created |
| Recursion | [../concepts/js-recursion.md](../concepts/js-recursion.md) | Deep extraction | should create | 5 claims covering functions, linear, recursion | created |
| Scope | [../concepts/js-scope.md](../concepts/js-scope.md) | Deep extraction | could create | 3 claims covering blocks, create, nested | created |
| Values | [../concepts/js-values.md](../concepts/js-values.md) | Deep extraction | should create | 5 claims covering expressions, javascript, uses | created |
| Variables | [../concepts/js-variables.md](../concepts/js-variables.md) | Deep extraction | must create | 13 claims covering bindings, const, declarations | created |
