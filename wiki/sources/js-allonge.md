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

Extracted 346 claims from 19 chunks, organized into 11 viable topics.

### Extraction Metadata

- Claim count: 346
- Topic count: 11
- Generation: summary (llm), tables (deterministic)

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| ECMAScript 2015 introduced features that make programming with functions easier  | "ECMAScript 2015 (formerly called ECMAScript 6 or "ES6"), is ushering in a very large number of impro" | `normalized:L119-L120` |
| Before ECMAScript 2015, JavaScript did not support collecting a variable number  | "Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into " | `normalized:L147-L150` |
| ECMAScript 2015 allows for cleaner syntax for block-scoped variables using 'let' | "We can also write: function foo (first, ...rest) { // ... } And presto, rest collects the rest of th" | `normalized:L159-L168` |
| ECMAScript 2015 (ES6) introduced three major groups of features: better syntax f | "ECMAScript 6 has three major groups of features: - Better syntax for features that already exist (e." | `normalized:L253-L266` |
| ECMAScript 2015 introduced block-structured variables using 'let' which allows v | "We can write: for (let i = 0; i < array.length; ++i) { // ... } And i is scoped to the for loop." | `normalized:L157-L158` |
| ECMAScript 2015 introduced rest parameters using the spread operator (...) which | "We can also write: function foo (first, ...rest) { // ... } And presto, rest collects the rest of th" | `normalized:L165-L168` |
| Prior to ECMAScript 2015, JavaScript lacked block-structured variables, so progr | "Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a tr" | `normalized:L131-L141` |
| ECMAScript 2015 brought significant improvements to JavaScript, including classe | "ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17" | `normalized:L245-L266` |
| In JavaScript, values are either truthy or falsy, with false, null, undefined, N | "Every value is either "truthy" or "falsy". Obviously, false is falsy. So are null and undefined, val" | `normalized:L2203-L2205` |
| Every value in JavaScript is either truthy or falsy, with specific values being  | "In JavaScript, there is a notion of "truthiness." Every value is either "truthy" or "falsy." Obvious" | `normalized:L2203-L2205` |

### Extracted Topics

| Topic | Claims | Sections | Status | Notes |
|---|---|---|---|---|
| Functions | 133 | 60 | synthesized |  |
| Iterators | 58 | 20 | synthesized |  |
| Data Types | 47 | 20 | synthesized |  |
| Control Flow | 33 | 14 | synthesized |  |
| Functional Programming | 17 | 13 | synthesized |  |
| Arrays | 17 | 10 | synthesized |  |
| ES6 Features | 13 | 8 | synthesized |  |
| Objects | 11 | 5 | synthesized |  |
| Closures | 7 | 4 | synthesized |  |
| Values | 5 | 3 | synthesized |  |
| Recursion | 3 | 3 | synthesized |  |
| Destructuring | 2 | 1 | deferred | Too few claims (2 < 3) |

## Major concepts

| Concept | Page | Status | Claims Used | Claims Available | Section Coverage |
|---|---|---|---|---|---|
| Arrays | `../concepts/arrays.md` | not_started | - | 17 | - |
| Closures | `../concepts/closures.md` | not_started | - | 7 | - |
| Control Flow | `../concepts/control-flow.md` | not_started | - | 33 | - |
| Data Types | `../concepts/data-types.md` | not_started | - | 47 | - |
| ES6 Features | `../concepts/es6-features.md` | not_started | - | 13 | - |
| Functional Programming | `../concepts/functional-programming.md` | not_started | - | 17 | - |
| Functions | `../concepts/functions.md` | not_started | - | 133 | - |
| Iterators | `../concepts/iterators.md` | not_started | - | 58 | - |
| Objects | `../concepts/objects.md` | not_started | - | 11 | - |
| Recursion | `../concepts/recursion.md` | not_started | - | 3 | - |
| Values | `../concepts/values.md` | not_started | - | 5 | - |

### Candidate Concepts

| Candidate | Canonical Slug | Priority | Claims | Sections | Sources | Status |
|---|---|---|---|---|---|---|
| Arrays | arrays | must create | 17 | 10 | 1 | discovered |
| Closures | closures | should create | 7 | 4 | 1 | discovered |
| Control Flow | control-flow | must create | 33 | 14 | 1 | discovered |
| Data Types | data-types | must create | 47 | 20 | 1 | discovered |
| ES6 Features | es6-features | must create | 13 | 8 | 1 | discovered |
| Functional Programming | functional-programming | must create | 17 | 13 | 1 | discovered |
| Functions | functions | must create | 133 | 60 | 1 | discovered |
| Iterators | iterators | must create | 58 | 20 | 1 | discovered |
| Objects | objects | must create | 11 | 5 | 1 | discovered |
| Recursion | recursion | could create | 3 | 3 | 1 | discovered |
| Values | values | should create | 5 | 3 | 1 | discovered |

### Source Locator Map

| Lines | Topic | Source Heading |
|---|---|---|
| 3-24 | - | Reg "raganwald" Braithwaite |
| 25-56 | - | **Contents** |
| 57-90 | - | CONTENTS |
| 91-106 | - | **A Pull of the Lever: Prefaces** |
| 107-116 | Functions | **About JavaScript Allongé** |
| 117-172 | ES6 Features, Functions | **why the "six" edition?** |
| 173-194 | Functions | **that's nice. is that the only reason?** |
| 195-228 | Functions | **What JavaScript Allongé is. And isn't.** |
| 229-244 | Functions | **how this book is organized** |
| 245-280 | ES6 Features | **Foreword to the "Six" edition** |
| 281-282 | - | **Forewords to the First Edition** |
| 283-296 | - | **michael fogus** |
| 297-320 | - | **matthew knox** |
| 321-336 | - | **About The Sample PDF** |
| 337-352 | - | **Prelude: Values and Expressions over Coffee** |
| 353-358 | Values | **values are expressions** |
| 359-364 | - | 42 |
| 365-394 | Data Types, Values | 42 |
| 395-416 | Data Types, Values | **values and identity** |
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
| Arrays | `../concepts/arrays.md` | Deep extraction | must create | 17 claims covering allows, array, destructuring | not created yet |
| Closures | `../concepts/closures.md` | Deep extraction | should create | 7 claims covering access, closure, closures | not created yet |
| Control Flow | `../concepts/control-flow.md` | Deep extraction | must create | 33 claims covering comma, javascript, operator | not created yet |
| Data Types | `../concepts/data-types.md` | Deep extraction | must create | 47 claims covering expressions, javascript, some | not created yet |
| ES6 Features | `../concepts/es6-features.md` | Deep extraction | must create | 13 claims covering brought, ecmascript, introduced | not created yet |
| Functional Programming | `../concepts/functional-programming.md` | Deep extraction | must create | 17 claims covering combinator, compose, higher | not created yet |
| Functions | `../concepts/functions.md` | Deep extraction | must create | 133 claims covering book, functions, javascript | not created yet |
| Iterators | `../concepts/iterators.md` | Deep extraction | must create | 58 claims covering filtering, function, iterator | not created yet |
| Objects | `../concepts/objects.md` | Deep extraction | must create | 11 claims covering created, javascript, object | not created yet |
| Recursion | `../concepts/recursion.md` | Deep extraction | could create | 3 claims covering functions, linear, recursion | not created yet |
| Values | `../concepts/values.md` | Deep extraction | should create | 5 claims covering expressions, javascript, operator | not created yet |
