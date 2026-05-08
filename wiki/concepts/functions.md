---
title: Functions
type: concept
tags: [javascript, programming, functions]
status: draft
last_updated: 2026-05-08
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1229-L1229
  - js-allonge:normalized:L1415-L1421
  - js-allonge:normalized:L159-L168
  - js-allonge:normalized:L891-L891
  - js-allonge:normalized:L899-L899
---

# Functions

## Summary

Functions are fundamental building blocks in JavaScript, serving as first-class entities that can be assigned to variables, passed as arguments, and returned from other functions. They enable modular, reusable code and support various programming paradigms including functional programming.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Functions in JavaScript are treated as first-class citizens, meaning they can be assigned to variables, passed as arguments to other functions, and returned from functions, enabling flexible and... | "Amazing how such an important idea-naming functions-can be explained _en passant_ in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as "first..." | `normalized:L1229-L1229` | [Source](../sources/js-allonge.md) |
| JavaScript supports modern syntax features like arrow functions and rest parameters, which provide more concise ways to define and work with functions compared to traditional function expressions. | "And i is scoped to the for loop. We can also write: iv A Pull of the Lever: Prefaces **function** foo (first, ...rest) { _// ..._ }" | `normalized:L159-L168` | [Source](../sources/js-allonge.md) |
| JavaScript supports modern syntax features like arrow functions and rest parameters, which provide more concise ways to define and work with functions compared to traditional function expressions. | "Here's our repeat function written using a "fat arrow" (str) => str + str And here's (almost) the exact same function written using the function keyword: **function** (str) { **return** str + str }" | `normalized:L1415-L1421` | [Source](../sources/js-allonge.md) |
| Functions in JavaScript create their own environments when invoked, maintaining a mapping between variable names and their values, which allows for lexical scoping and closure behavior. | "Every time a function is invoked ("invoked" means "applied to zero or more arguments"), a new _environment_ is created. An environment is a (possibly empty) dictionary that maps variables to..." | `normalized:L891-L891` | [Source](../sources/js-allonge.md) |
| Functions in JavaScript create their own environments when invoked, maintaining a mapping between variable names and their values, which allows for lexical scoping and closure behavior. | "How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So..." | `normalized:L899-L899` | [Source](../sources/js-allonge.md) |

## Why it matters

Functions are central to JavaScript programming, allowing developers to compose complex behaviors from smaller, manageable pieces. They facilitate concepts like closures, higher-order functions, and functional programming patterns, which enhance code expressiveness and maintainability.

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
