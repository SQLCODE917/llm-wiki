---
title: "Source: js-allonge"
type: source
source_id: js-allonge
source_type: pdf
raw_path: ../../raw/imported/js-allonge/
normalized_path: ../../raw/normalized/js-allonge/
status: draft
last_updated: 2026-05-08
tags: []
sources:
  - ../../raw/imported/js-allonge/original.pdf
---

# Source: js-allonge

## Summary

**JavaScript Allongé, the "Six" Edition** Programming from Functions to Classes in ECMAScript 2015 This book is for sale at http://leanpub.com/javascriptallongesix This version was published on 2017-11-03

Extracted 372 claims from 25 chunks, organized into 13 viable topics.

### Extraction Metadata

- Claim count: 372
- Topic count: 13
- Generation: summary (llm), tables (deterministic)

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| ECMAScript 2015 introduced block-structured variables, allowing variables to be  | "Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a tr" | `normalized:L131-L141` |
| ECMAScript 2015 introduced rest parameters which allow collecting a variable num | "With ECMASCript 2015, we can write: for (let i = 0; i < array.length; ++i) { // ... } And i is scope" | `normalized:L155-L168` |
| Prior to ECMAScript 2015, JavaScript did not support collecting a variable numbe | "Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into " | `normalized:L147-L150` |
| ECMAScript 2015 (ES6) introduced new programming techniques that align with the  | "ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things " | `normalized:L183-L185` |
| ES6 features are presented in small, easily digestible pieces to help readers un | "_JavaScript Allongé_ introduces new aspects of programming with functions in each chapter, explainin" | `normalized:L231-L233` |
| ES6 has three major groups of features: improved syntax, new standard library fu | "ECMAScript 6 has three major groups of features: - Better syntax for features that already exist (e." | `normalized:L253-L266` |
| The tap function can be used as a debugging aid by executing a function for side | "tap('espresso')((it) => { console.log(`Our drink is '${ it }'`) });" | `normalized:L1965-L1965` |
| Functions created inside loops using var can access the loop variable after the  | "introductions[i] = (soAndSo) => `Hello, ${ soAndSo }, my name is ${ names[i] }`" | `normalized:L3645-L3645` |
| The let keyword provides block scoping, preventing common issues with closures i | "**let** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **let** i = 0; i < 3; " | `normalized:L3663-L3663` |
| Prior to ECMAScript 2015, JavaScript did not include block-structured variables, | "Prior to ECMAScript 2015, JavaScript did not include block-structured variables. Over time, programm" | `normalized:L121-L141` |

### Extracted Topics

| Topic | Claims | Sections | Status | Notes |
|---|---|---|---|---|
| Functions | 148 | 74 | synthesized |  |
| Iterators | 36 | 16 | synthesized |  |
| Data Types | 35 | 25 | synthesized |  |
| ES6 Features | 28 | 14 | synthesized |  |
| Arrays | 27 | 14 | synthesized |  |
| Control Flow | 19 | 14 | synthesized |  |
| Objects | 19 | 9 | synthesized |  |
| Functional Programming | 15 | 12 | synthesized |  |
| Iterables | 12 | 3 | synthesized |  |
| Closures | 11 | 8 | synthesized |  |
| Generators | 10 | 5 | synthesized |  |
| Recursion | 9 | 6 | synthesized |  |
| Strings | 3 | 2 | synthesized |  |

## Major concepts

| Concept | Page | Status | Claims Used | Claims Available | Section Coverage |
|---|---|---|---|---|---|
| Arrays | `../concepts/arrays.md` | not_started | - | 27 | - |
| Closures | `../concepts/closures.md` | not_started | - | 11 | - |
| Control Flow | `../concepts/control-flow.md` | not_started | - | 19 | - |
| Data Types | `../concepts/data-types.md` | not_started | - | 35 | - |
| ES6 Features | `../concepts/es6-features.md` | not_started | - | 28 | - |
| Functional Programming | `../concepts/functional-programming.md` | not_started | - | 15 | - |
| Functions | `../concepts/functions.md` | not_started | - | 148 | - |
| Generators | `../concepts/generators.md` | not_started | - | 10 | - |
| Iterables | `../concepts/iterables.md` | not_started | - | 12 | - |
| Iterators | `../concepts/iterators.md` | not_started | - | 36 | - |
| Objects | `../concepts/objects.md` | not_started | - | 19 | - |
| Recursion | `../concepts/recursion.md` | not_started | - | 9 | - |
| Strings | `../concepts/strings.md` | not_started | - | 3 | - |

### Candidate Concepts

| Candidate | Canonical Slug | Priority | Claims | Sections | Sources | Status |
|---|---|---|---|---|---|---|
| Arrays | arrays | must create | 27 | 14 | 1 | discovered |
| Closures | closures | must create | 11 | 8 | 1 | discovered |
| Control Flow | control-flow | must create | 19 | 14 | 1 | discovered |
| Data Types | data-types | must create | 35 | 25 | 1 | discovered |
| ES6 Features | es6-features | must create | 28 | 14 | 1 | discovered |
| Functional Programming | functional-programming | must create | 15 | 12 | 1 | discovered |
| Functions | functions | must create | 148 | 74 | 1 | discovered |
| Generators | generators | must create | 10 | 5 | 1 | discovered |
| Iterables | iterables | must create | 12 | 3 | 1 | discovered |
| Iterators | iterators | must create | 36 | 16 | 1 | discovered |
| Objects | objects | must create | 19 | 9 | 1 | discovered |
| Recursion | recursion | must create | 9 | 6 | 1 | discovered |
| Strings | strings | could create | 3 | 2 | 1 | discovered |

### Source Locator Map

| Lines | Topic | Source Heading |
|---|---|---|
| 3-24 | - | Reg "raganwald" Braithwaite |
| 25-56 | - | **Contents** |
| 57-90 | - | CONTENTS |
| 91-106 | - | **A Pull of the Lever: Prefaces** |
| 107-116 | Functions | **About JavaScript Allongé** |
| 117-172 | ES6 Features | **why the "six" edition?** |
| 173-194 | ES6 Features | **that's nice. is that the only reason?** |
| 195-228 | Functions | **What JavaScript Allongé is. And isn't.** |
| 229-244 | ES6 Features | **how this book is organized** |
| 245-280 | ES6 Features | **Foreword to the "Six" edition** |
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
| Arrays | `../concepts/arrays.md` | Deep extraction | must create | 27 claims covering array, arrays, created | not created yet |
| Closures | `../concepts/closures.md` | Deep extraction | must create | 11 claims covering closure, free, function | not created yet |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 19 claims covering blocks, logical, operator | not created yet |
| Data Types | `../concepts/data-types.md` | Deep extraction | must create | 35 claims covering concatenation, expressions, javascript | not created yet |
| ES6 Features | `../concepts/es6-features.md` | Deep extraction | must create | 28 claims covering ecmascript, introduced, prior | not created yet |
| Functional Programming | `../concepts/functional-programming.md` | Deep extraction | must create | 15 claims covering applies, combines, folding | not created yet |
| Functions | `../concepts/functions.md` | Deep extraction | must create | 148 claims covering book, functions, javascript | not created yet |
| Generators | `../concepts/generators.md` | Deep extraction | must create | 10 claims covering functions, generator, generators | not created yet |
| Iterables | `../concepts/iterables.md` | Deep extraction | must create | 12 claims covering generators, iterable, made | not created yet |
| Iterators | `../concepts/iterators.md` | Deep extraction | must create | 36 claims covering composed, functions, generate | not created yet |
| Objects | `../concepts/objects.md` | Deep extraction | must create | 19 claims covering created, javascript, objects | not created yet |
| Recursion | `../concepts/recursion.md` | Deep extraction | must create | 9 claims covering flattening, functions, linear | not created yet |
| Strings | `../concepts/strings.md` | Deep extraction | could create | 3 claims covering literal, literals, quasi | not created yet |
