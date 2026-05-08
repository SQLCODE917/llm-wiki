---
title: Objects
type: concept
tags: [javascript, data-structures]
status: draft
last_updated: 2026-05-08
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L3159-L3159
  - js-allonge:normalized:L3205-L3205
  - js-allonge:normalized:L3209-L3209
  - js-allonge:normalized:L3227-L3227
  - js-allonge:normalized:L4539-L4539
  - js-allonge:normalized:L5903-L5917
---

# Objects

## Summary

In JavaScript, objects are fundamental data structures that serve as maps from string keys to values. They are versatile containers that can hold properties and methods, enabling complex data organization and manipulation.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript objects function as mappings between string keys and values, allowing for flexible data storage and retrieval. | "In JavaScript, an object is a map from string keys to values." | `normalized:L3159-L3159` | [Source](../sources/js-allonge.md) |
| Object properties can be accessed both via dot notation and bracket notation, offering flexibility in how data is retrieved. | "date['day'] === date.day _//=> true_" | `normalized:L3205-L3205` | [Source](../sources/js-allonge.md) |
| Objects support dynamic property names using computed property syntax, which allows for more expressive key definitions. | "{ ["p" + "i"]: 3.14159265 } _//=> {"pi":3.14159265}_" | `normalized:L3209-L3209` | [Source](../sources/js-allonge.md) |
| JavaScript objects can encapsulate behavior through methods, enabling functional programming patterns like encoding and decoding operations. | "**const** SecretDecoderRing = { encode (plaintext) { **return** plaintext .split('') .map( **char** => **char** .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) )..." | `normalized:L3227-L3227` | [Source](../sources/js-allonge.md) |
| The Object.assign() method facilitates merging properties from one or more source objects into a target object. | "**const** inventory = { apples: 12, oranges: 12 }; **const** shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment)" | `normalized:L4539-L4539` | [Source](../sources/js-allonge.md) |
| Objects can be used as lookup tables for mapping complex keys to values, such as in game state representations. | "**const** moveLookupTable = { [[ ' ' ' ' ' ' , , , ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ]]: 0, [[ 'o', 'x', ' ', ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ]]: 6, [[ 'o', 'x', 'x', ' ' ' ' ' ' , , , 'o', ' ',..." | `normalized:L5903-L5917` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
