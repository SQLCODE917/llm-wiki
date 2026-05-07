---
title: Data Types
type: concept
tags: [javascript, data-types, primitives, objects]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L170-L172
  - js-allonge:normalized:L4270-L4270
  - js-allonge:normalized:L4271-L4271
  - js-allonge:normalized:L4616-L4618
  - js-allonge:normalized:L4620-L4621
  - js-allonge:normalized:L631-L633
  - js-allonge:normalized:L659-L660
---

# Data Types

## Summary

JavaScript data types define how values are stored and manipulated. Primitive types include strings, numbers, and booleans, while objects and arrays are reference types. Understanding these distinctions is key to effective programming in JavaScript.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript is designed with first-class functions and lexical scoping, making it suitable for functional programming paradigms. | "It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope." | `normalized:L170-L172` | [Source](../sources/js-allonge.md) |
| Numeric literals in JavaScript are internally represented as double-precision floating-point values regardless of their format. | "Internally, both 042 and 34 have the same representation, as double-precision floating point numbers." | `normalized:L659-L660` | [Source](../sources/js-allonge.md) |
| Each evaluation of an array literal results in a unique array instance, even when the contents appear identical. | "Every time you evaluate an expression to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value." | `normalized:L631-L633` | [Source](../sources/js-allonge.md) |
| Object literals in JavaScript create distinct entities each time they are evaluated, similar to arrays. | "{ year: 2012, month: 6, day: 14 }" | `normalized:L4270-L4270` | [Source](../sources/js-allonge.md) |
| Comparing two separate object literals with the strict equality operator returns false due to differing identities. | "{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 }" | `normalized:L4271-L4271` | [Source](../sources/js-allonge.md) |
| The const keyword prevents rebinding of variables but allows mutation of their contents. | "Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction." | `normalized:L4620-L4621` | [Source](../sources/js-allonge.md) |
| JavaScript allows modification of values through reassignment and assignment operations on container elements. | "JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects." | `normalized:L4616-L4618` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
