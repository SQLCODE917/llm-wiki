---
title: Objects
type: concept
tags: []
status: draft
last_updated: 2026-05-06
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4258-L4258
  - js-allonge:normalized:L4267-L4270
  - js-allonge:normalized:L4299-L4300
---

# Objects

## Summary

In JavaScript, objects are fundamental data structures that map string keys to values. They support various ways of creation, including literal syntax, and provide mechanisms for accessing and manipulating their properties.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| An object in JavaScript is fundamentally a mapping from string keys to values. | "In JavaScript, an object is a map from string keys to values." | `normalized:L4258-L4258` | [Source](../sources/js-allonge.md) |
| JavaScript allows for concise object creation using literal syntax, where key-value pairs are defined directly within curly braces. | "JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day: { year: 2012, month: 6, day: 14 }" | `normalized:L4267-L4270` | [Source](../sources/js-allonge.md) |
| Properties of an object can be accessed either using dot notation or bracket notation, which accepts string keys. | "date['day'] === date.day //=> true" | `normalized:L4299-L4300` | [Source](../sources/js-allonge.md) |

## Why it matters

Objects are central to JavaScript's data modeling capabilities, enabling developers to create complex data structures and encapsulate behavior through methods. Understanding how to define, access, and manipulate objects is crucial for effective JavaScript programming.

## Related pages

- [Functional Programming](../concepts/functional-programming.md)
- [Functions](../concepts/functions.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
