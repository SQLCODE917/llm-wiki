---
title: Objects
type: concept
tags: [javascript, data-structures, dictionaries]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4255-L4258
  - js-allonge:normalized:L4268-L4270
  - js-allonge:normalized:L4274-L4276
  - js-allonge:normalized:L4299-L4300
  - js-allonge:normalized:L4391-L4401
  - js-allonge:normalized:L4407-L4408
  - js-allonge:normalized:L4428-L4429
---

# Objects

## Summary

In JavaScript, objects serve as the primary mechanism for organizing and storing data. They function as dictionaries mapping string keys to values, allowing for flexible data structures that can hold both primitive values and references to other objects. Objects support dynamic property addition and retrieval, making them central to JavaScript's data manipulation capabilities.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript uses objects as dictionaries to map string keys to values, providing a flexible way to store and organize data. | "JavaScript has dictionaries, and it calls them "objects." The word "object" is loaded in programming circles, due to the widespread use of the term "object-oriented programming" that was coined by..." | `normalized:L4255-L4258` | [Source](../sources/js-allonge.md) |
| Objects in JavaScript allow for dynamic access to properties using bracket notation or dot notation, enabling versatile data retrieval. | "{ year: 2012, month: 6, day: 14 }" | `normalized:L4268-L4270` | [Source](../sources/js-allonge.md) |
| Objects in JavaScript allow for dynamic access to properties using bracket notation or dot notation, enabling versatile data retrieval. | "{ year: 2012, month: 6, day: 14 }['day']" | `normalized:L4274-L4276` | [Source](../sources/js-allonge.md) |
| Objects in JavaScript allow for dynamic access to properties using bracket notation or dot notation, enabling versatile data retrieval. | "date['day'] === date.day" | `normalized:L4299-L4300` | [Source](../sources/js-allonge.md) |
| JavaScript objects support nested structures and can contain complex data including arrays and other objects, facilitating rich data modeling. | "const user = { name: { first: "Reginald", last: "Braithwaite" }, occupation: { title: "Author", responsibilities: [ "JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto" ] } };" | `normalized:L4391-L4401` | [Source](../sources/js-allonge.md) |
| JavaScript objects support nested structures and can contain complex data including arrays and other objects, facilitating rich data modeling. | "const {name: { first: given, last: surname}, occupation: { title: title } } = user;" | `normalized:L4407-L4408` | [Source](../sources/js-allonge.md) |
| JavaScript objects support nested structures and can contain complex data including arrays and other objects, facilitating rich data modeling. | "const description = ({name: { first }, occupation: { title } }) => `${first} is a ${title}`;" | `normalized:L4428-L4429` | [Source](../sources/js-allonge.md) |

## Why it matters

Objects are fundamental to JavaScript's design and are essential for structuring data and implementing behavior. Understanding how to create, access, and manipulate objects is crucial for writing effective JavaScript code. Their flexibility allows developers to model real-world entities and relationships, while features like destructuring and methods enable powerful patterns for data handling.

## Related pages

- [Data Types](../concepts/data-types.md)
- [Functional Programming](../concepts/functional-programming.md)
- [Functions](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
