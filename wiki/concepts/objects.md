---
title: Objects
type: concept
tags: [javascript, data-structures, programming-concepts]
status: draft
last_updated: 2026-05-11
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L3159-L3159
  - js-allonge:normalized:L3205-L3205
  - js-allonge:normalized:L3209-L3209
  - js-allonge:normalized:L4535-L4535
  - js-allonge:normalized:L4539-L4539
  - js-allonge:normalized:L4559-L4559
---

# Objects

## Summary

In JavaScript, objects are fundamental data structures that map string keys to values. They serve as the primary mechanism for organizing and storing data, supporting both simple key-value pairs and complex nested structures. Objects can be manipulated through property assignment, copying, and various methods for combining or transforming their contents.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript objects function as mappings from string keys to values, enabling flexible data organization. | "In JavaScript, an object is a map from string keys to values." | `normalized:L3159-L3159` | [Source](../sources/js-allonge.md) |
| Objects in JavaScript support both dot notation and bracket notation for accessing properties, allowing for dynamic key handling. | "date['day'] === date.day _//=> true_" | `normalized:L3205-L3205` | [Source](../sources/js-allonge.md) |
| Objects in JavaScript support both dot notation and bracket notation for accessing properties, allowing for dynamic key handling. | "{ ["p" + "i"]: 3.14159265 } _//=> {"pi":3.14159265}_" | `normalized:L3209-L3209` | [Source](../sources/js-allonge.md) |
| JavaScript provides mechanisms for copying and combining objects, such as Object.assign, which facilitates operations like cloning and merging. | "Object.assign({}, { apples: 12, oranges: 12 }) _//=> { apples: 12, oranges: 12 }_" | `normalized:L4535-L4535` | [Source](../sources/js-allonge.md) |
| JavaScript provides mechanisms for copying and combining objects, such as Object.assign, which facilitates operations like cloning and merging. | "**const** inventory = { apples: 12, oranges: 12 }; **const** shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment)" | `normalized:L4539-L4539` | [Source](../sources/js-allonge.md) |
| JavaScript provides mechanisms for copying and combining objects, such as Object.assign, which facilitates operations like cloning and merging. | "Assigning properties from one object to another (also called "cloning" or "shallow copying") is a basic building block that we will later use to implement more advanced paradigms like mixins." | `normalized:L4559-L4559` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
