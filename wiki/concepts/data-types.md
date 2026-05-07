---
title: Data Types
type: concept
tags: [javascript, types, primitives, arrays, objects]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4271-L4271
  - js-allonge:normalized:L4616-L4618
  - js-allonge:normalized:L4620-L4621
  - js-allonge:normalized:L599-L600
  - js-allonge:normalized:L631-L633
  - js-allonge:normalized:L659-L660
---

# Data Types

## Summary

JavaScript data types define how values are stored and manipulated. Primitive types like strings, numbers, and booleans are immutable and compared by value. Arrays and objects are mutable and compared by reference. JavaScript also supports copy-on-write strategies for efficient memory management.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Strings, numbers, and booleans in JavaScript are categorized as primitive or value types. | "Strings, numbers, and booleans are examples of what JavaScript calls "value" or "primitive" types." | `normalized:L599-L600` | [Source](../sources/js-allonge.md) |
| Integer literals with leading zeros in JavaScript are interpreted as octal values internally represented as double-precision floating-point numbers. | "Internally, both 042 and 34 have the same representation, as double-precision floating point numbers." | `normalized:L659-L660` | [Source](../sources/js-allonge.md) |
| Each evaluation of an array creation expression results in a unique, distinct array value regardless of apparent similarity. | "Every time you evaluate an expression to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value." | `normalized:L631-L633` | [Source](../sources/js-allonge.md) |
| Object literals created separately do not share identity, even when containing identical key-value pairs. | "{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 }" | `normalized:L4271-L4271` | [Source](../sources/js-allonge.md) |
| JavaScript allows modification of existing bindings and elements within containers such as arrays and objects through reassignment. | "JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects." | `normalized:L4616-L4618` | [Source](../sources/js-allonge.md) |
| Declaring a variable with const prevents rebinding but does not prevent mutation of the underlying value. | "Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name." | `normalized:L4620-L4621` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
