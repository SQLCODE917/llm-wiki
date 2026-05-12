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

Extracted 452 claims from 19 chunks, organized into 19 viable topics.

### Extraction Metadata

- Claim count: 452
- Topic count: 19
- Generation: summary (llm), tables (deterministic)

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| ECMAScript 2015 introduced features that make programming with functions easier  | "ECMAScript 2015 (formerly called ECMAScript 6 or "ES6"), is ushering in a very large number of impro" | `normalized:L119-L119` |
| ECMAScript 2015 allows for collecting a variable number of arguments into a para | "We can also write:   **function** foo (first, ...rest) { _// ..._   }  And presto, rest collects the" | `normalized:L159-L167` |
| ECMAScript 2015 allows for variable argument handling using rest parameters inst | "Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into " | `normalized:L147-L149` |
| Block-structured variables in ECMAScript 2015 allow for local scoping of variabl | "With ECMASCript 2015, we can write:   **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }  " | `normalized:L157-L157` |
| ECMAScript 2015 introduced block-structured variables that allow for local scopi | "Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a tr" | `normalized:L137-L140` |
| ECMAScript 2015 introduced features that make programming with arrays and collec | "ECMAScript 2015 (formerly called ECMAScript 6 or "ES6"), is ushering in a very large number of impro" | `normalized:L119-L119` |
| Octal literals in JavaScript begin with a zero and are interpreted in base 8. | "If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is" | `normalized:L469-L470` |
| JavaScript's largest safe integer is 2^53 - 1, beyond which precision may be los | "The largest integer JavaScript can safely[14] handle is 9007199254740991, or 2['53'] - 1." | `normalized:L473-L473` |
| Cycle detection in sequences can be solved using the tortoise and hare algorithm | "const tortoiseAndHare = (iterable) => { const hare = iterable[Symbol.iterator](); let hareResult = (" | `normalized:L5714-L5722` |
| JavaScript Allongé is a book about programming with functions and how to compose | "JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It's written" | `normalized:L109-L110` |

## Major concepts

### Extracted Topics

| Topic | Claims | Sections | Status | Notes |
|---|---|---|---|---|
| Functions | 150 | 64 | not_started |  |
| Control Flow | 44 | 22 | not_started |  |
| Data Types | 42 | 25 | not_started |  |
| Arrays | 34 | 17 | not_started |  |
| Data Structures | 34 | 12 | not_started |  |
| Iterables | 31 | 12 | not_started |  |
| Variables | 20 | 12 | not_started |  |
| Objects | 15 | 8 | not_started |  |
| Collections | 14 | 6 | not_started |  |
| Memory Management | 13 | 8 | not_started |  |
| Functional Programming | 11 | 7 | not_started |  |
| Iterators | 10 | 8 | not_started |  |
| Operations | 6 | 3 | not_started |  |
| Algorithms | 6 | 3 | not_started |  |
| Programming Paradigms | 5 | 2 | not_started |  |
| Expressions | 4 | 3 | not_started |  |
| Recursion | 4 | 2 | not_started |  |
| Scopes | 3 | 1 | not_started | Single section |
| Generators | 3 | 2 | not_started |  |
| Performance Optimization | 2 | 2 | deferred | Too few claims (2 < 3) |
| Lazy Evaluation | 1 | 1 | deferred | Too few claims (1 < 3) |

| Concept | Page | Status | Claims Used | Claims Available | Section Coverage |
|---|---|---|---|---|---|
| Algorithms | `../concepts/js-algorithms.md` | not_started | - | 6 | - |
| Arrays | `../concepts/js-arrays.md` | not_started | - | 34 | - |
| Collections | `../concepts/js-collections.md` | not_started | - | 14 | - |
| Control Flow | `../concepts/js-control-flow.md` | not_started | - | 44 | - |
| Data Structures | `../concepts/js-data-structures.md` | not_started | - | 34 | - |
| Data Types | `../concepts/js-data-types.md` | not_started | - | 42 | - |
| Expressions | `../concepts/js-expressions.md` | not_started | - | 4 | - |
| Functional Programming | `../concepts/js-functional-programming.md` | not_started | - | 11 | - |
| Functions | `../concepts/js-functions.md` | not_started | - | 150 | - |
| Generators | `../concepts/js-generators.md` | not_started | - | 3 | - |
| Iterables | `../concepts/js-iterables.md` | not_started | - | 31 | - |
| Iterators | `../concepts/js-iterators.md` | not_started | - | 10 | - |
| Memory Management | `../concepts/js-memory-management.md` | not_started | - | 13 | - |
| Objects | `../concepts/js-objects.md` | not_started | - | 15 | - |
| Operations | `../concepts/js-operations.md` | not_started | - | 6 | - |
| Programming Paradigms | `../concepts/js-programming-paradigms.md` | not_started | - | 5 | - |
| Recursion | `../concepts/js-recursion.md` | not_started | - | 4 | - |
| Scopes | `../concepts/js-scopes.md` | not_started | - | 3 | - |
| Variables | `../concepts/js-variables.md` | not_started | - | 20 | - |

### Candidate Concepts

| Candidate | Canonical Slug | Priority | Claims | Sections | Sources | Status |
|---|---|---|---|---|---|---|
| Algorithms | js-algorithms | should create | 6 | 3 | 1 | discovered |
| Arrays | js-arrays | must create | 34 | 17 | 1 | discovered |
| Collections | js-collections | must create | 14 | 6 | 1 | discovered |
| Control Flow | js-control-flow | must create | 44 | 22 | 1 | discovered |
| Data Structures | js-data-structures | must create | 34 | 12 | 1 | discovered |
| Data Types | js-data-types | must create | 42 | 25 | 1 | discovered |
| Expressions | js-expressions | could create | 4 | 3 | 1 | discovered |
| Functional Programming | js-functional-programming | must create | 11 | 7 | 1 | discovered |
| Functions | js-functions | must create | 150 | 64 | 1 | discovered |
| Generators | js-generators | could create | 3 | 2 | 1 | discovered |
| Iterables | js-iterables | must create | 31 | 12 | 1 | discovered |
| Iterators | js-iterators | must create | 10 | 8 | 1 | discovered |
| Memory Management | js-memory-management | must create | 13 | 8 | 1 | discovered |
| Objects | js-objects | must create | 15 | 8 | 1 | discovered |
| Operations | js-operations | should create | 6 | 3 | 1 | discovered |
| Programming Paradigms | js-programming-paradigms | should create | 5 | 2 | 1 | discovered |
| Recursion | js-recursion | could create | 4 | 2 | 1 | discovered |
| Scopes | js-scopes | could create | 3 | 1 | 1 | discovered |
| Variables | js-variables | must create | 20 | 12 | 1 | discovered |

### Source Locator Map

| Lines | Topic | Source Heading |
|---|---|---|
| 3-24 | - | Reg "raganwald" Braithwaite |
| 25-56 | - | **Contents** |
| 57-90 | Arrays | CONTENTS |
| 91-106 | Arrays, Control Flow | **A Pull of the Lever: Prefaces** |
| 107-116 | Arrays, Control Flow | **About JavaScript Allongé** |
| 117-172 | Arrays, Control Flow | **why the "six" edition?** |
| 173-194 | Functions | **that's nice. is that the only reason?** |
| 195-228 | Functions | **What JavaScript Allongé is. And isn't.** |
| 229-244 | - | **how this book is organized** |
| 245-280 | - | **Foreword to the "Six" edition** |
| 281-282 | - | **Forewords to the First Edition** |
| 283-296 | - | **michael fogus** |
| 297-320 | - | **matthew knox** |
| 321-336 | - | **About The Sample PDF** |
| 337-352 | - | **Prelude: Values and Expressions over Coffee** |
| 353-358 | Data Types | **values are expressions** |
| 359-364 | - | 42 |
| 365-394 | Data Types, Expressions | 42 |
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
| Algorithms | [../concepts/js-algorithms.md](../concepts/js-algorithms.md) | Deep extraction | should create | 6 claims covering hare, teleporting, tortoise | created |
| Arrays | [../concepts/js-arrays.md](../concepts/js-arrays.md) | Deep extraction | must create | 34 claims covering covers, discusses, ecmascript | created |
| Collections | [../concepts/js-collections.md](../concepts/js-collections.md) | Deep extraction | must create | 14 claims covering collections, eager, infinite | created |
| Control Flow | [../concepts/js-control-flow.md](../concepts/js-control-flow.md) | Deep extraction | must create | 44 claims covering allows, comma, ecmascript | created |
| Data Structures | [../concepts/js-data-structures.md](../concepts/js-data-structures.md) | Deep extraction | must create | 34 claims covering cells, cons, linked | created |
| Data Types | [../concepts/js-data-types.md](../concepts/js-data-types.md) | Deep extraction | must create | 42 claims covering expressions, javascript, uses | created |
| Expressions | [../concepts/js-expressions.md](../concepts/js-expressions.md) | Deep extraction | could create | 4 claims covering array, concatenation, expression | created |
| Functional Programming | [../concepts/js-functional-programming.md](../concepts/js-functional-programming.md) | Deep extraction | must create | 11 claims covering combinatory, folding, logic | created |
| Functions | [../concepts/js-functions.md](../concepts/js-functions.md) | Deep extraction | must create | 150 claims covering book, functions, javascript | created |
| Generators | [../concepts/js-generators.md](../concepts/js-generators.md) | Deep extraction | could create | 3 claims covering functions, generator, generators | created |
| Iterables | [../concepts/js-iterables.md](../concepts/js-iterables.md) | Deep extraction | must create | 31 claims covering iterables, iterator, javascript | created |
| Iterators | [../concepts/js-iterators.md](../concepts/js-iterators.md) | Deep extraction | must create | 10 claims covering allow, composed, evaluation | created |
| Memory Management | [../concepts/js-memory-management.md](../concepts/js-memory-management.md) | Deep extraction | must create | 13 claims covering call, converting, recursive | created |
| Objects | [../concepts/js-objects.md](../concepts/js-objects.md) | Deep extraction | must create | 15 claims covering explains, javascript, teaches | created |
| Operations | [../concepts/js-operations.md](../concepts/js-operations.md) | Deep extraction | should create | 6 claims covering floating, javascript, literals | created |
| Programming Paradigms | [../concepts/js-programming-paradigms.md](../concepts/js-programming-paradigms.md) | Deep extraction | should create | 5 claims covering functional, functions, programming | created |
| Recursion | [../concepts/js-recursion.md](../concepts/js-recursion.md) | Deep extraction | could create | 4 claims covering function, functions, linear | created |
| Scopes | [../concepts/js-scopes.md](../concepts/js-scopes.md) | Deep extraction | could create | 3 claims covering blocks, create, nested | created |
| Variables | `../concepts/js-variables.md` | Deep extraction | must create | 20 claims covering arguments, bound, function | not created yet |
