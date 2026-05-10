---
title: Data Types
type: concept
tags: [javascript, data-types, values, expressions]
status: draft
last_updated: 2026-05-09
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2177-L2177
  - js-allonge:normalized:L2203-L2205
  - js-allonge:normalized:L3363-L3363
  - js-allonge:normalized:L397-L397
  - js-allonge:normalized:L425-L425
  - js-allonge:normalized:L449-L450
  - js-allonge:normalized:L569-L569
  - js-allonge:normalized:L663-L663
---

# Data Types

## Summary

Data types in JavaScript define how values behave and what operations can be performed on them. JavaScript distinguishes between primitive types (like strings, numbers, booleans) and reference types (like arrays and objects). Primitive values are immutable, while reference types can be mutated. Understanding these distinctions is key to working effectively with JavaScript's data model.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| When JavaScript evaluates expressions that produce strings, numbers, or booleans, those values are identical to any other value of the same type with the same content, indicating they are... | "Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with..." | `normalized:L425-L425` | [Source](../sources/js-allonge.md) |
| JavaScript treats strings, numbers, and booleans as primitive types, meaning they are immutable and compared by value rather than identity. | "Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with..." | `normalized:L425-L425` | [Source](../sources/js-allonge.md) |
| Functions in JavaScript are reference types, similar to arrays, where each evaluation of a function expression creates a unique function instance. | "Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it...." | `normalized:L569-L569` | [Source](../sources/js-allonge.md) |
| Arrays in JavaScript are reference types, and each time an array expression is evaluated, it produces a new, distinct array instance regardless of its appearance. | "How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other..." | `normalized:L449-L450` | [Source](../sources/js-allonge.md) |
| JavaScript allows mutation of certain data types, specifically arrays and objects, where changes to a value affect all references to that value. | "In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value..." | `normalized:L3363-L3363` | [Source](../sources/js-allonge.md) |
| In JavaScript, the concept of truthiness determines how values are interpreted in conditional contexts, with all values being either truthy or falsy. | "In JavaScript, there is a notion of "truthiness." Every value is either "truthy" or "falsy." Obviously, false is falsy. So are null and undefined, values that semantically represent "no value."..." | `normalized:L2203-L2205` | [Source](../sources/js-allonge.md) |
| The undefined value in JavaScript represents the absence of a value and is itself a distinct value type. | "In JavaScript, the absence of a value is written undefined, and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type:" | `normalized:L663-L663` | [Source](../sources/js-allonge.md) |
| Boolean values in JavaScript are represented by the literals true and false, forming a fundamental part of the language's logical operations. | "JavaScript does have "boolean" values, they're written true and false:" | `normalized:L2177-L2177` | [Source](../sources/js-allonge.md) |
| JavaScript's equality operator === compares values based on both type and content, distinguishing between different types such as strings and numbers. | "In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:" | `normalized:L397-L397` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
