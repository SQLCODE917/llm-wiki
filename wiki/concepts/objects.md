---
title: Objects
type: concept
tags: [javascript, data-structures]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4258-L4258
  - js-allonge:normalized:L4267-L4270
  - js-allonge:normalized:L4274-L4276
  - js-allonge:normalized:L4286-L4288
  - js-allonge:normalized:L4299-L4300
  - js-allonge:normalized:L4302-L4305
  - js-allonge:normalized:L4306-L4311
  - js-allonge:normalized:L4313-L4331
  - js-allonge:normalized:L4360-L4377
  - js-allonge:normalized:L4570-L4576
  - js-allonge:normalized:L6470-L6473
  - js-allonge:normalized:L6484-L6484
  - js-allonge:normalized:L6741-L6743
  - js-allonge:normalized:L6809-L6843
  - js-allonge:normalized:L8767-L8787
  - js-allonge:normalized:L9339-L9388
---

# Objects

## Summary

In JavaScript, objects are collections of key-value pairs used to store and organize data. They serve as fundamental data structures that can hold various types of values, including functions, and support dynamic property access and manipulation.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript objects are mappings from string keys to values, allowing for flexible data storage. | "In JavaScript, an object is a map from string keys to values." | `normalized:L4258-L4258` | [Source](../sources/js-allonge.md) |
| Objects in JavaScript can be created using literal syntax and accessed using bracket notation or dot notation. | "JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day: { year: 2012, month: 6, day: 14 }" | `normalized:L4267-L4270` | [Source](../sources/js-allonge.md) |
| Objects in JavaScript can be created using literal syntax and accessed using bracket notation or dot notation. | "Objects use [] to access the values by name, using a string: { year: 2012, month: 6, day: 14 }['day']" | `normalized:L4274-L4276` | [Source](../sources/js-allonge.md) |
| Objects in JavaScript can be created using literal syntax and accessed using bracket notation or dot notation. | "date['day'] === date.day //=> true" | `normalized:L4299-L4300` | [Source](../sources/js-allonge.md) |
| JavaScript objects support arbitrary key names, including those with spaces or special characters, which require quote delimiters. | "Names needn't be alphanumeric strings. For anything else, enclose the label in quotes: { 'first name': 'reginald', 'last name': 'lewis' }['first name']" | `normalized:L4286-L4288` | [Source](../sources/js-allonge.md) |
| JavaScript objects support arbitrary key names, including those with spaces or special characters, which require quote delimiters. | "{ ["p" + "i"]: 3.14159265 } //=> {"pi":3.14159265}" | `normalized:L4302-L4305` | [Source](../sources/js-allonge.md) |
| Functions can be stored as values within objects, enabling methods and encapsulation of behavior. | "All containers can contain any value, including functions or other containers, like a fat arrow function: const Mathematics = { abs: (a) => a < 0 ? -a : a };" | `normalized:L4306-L4311` | [Source](../sources/js-allonge.md) |
| Functions can be stored as values within objects, enabling methods and encapsulation of behavior. | "Or proper functions: const SecretDecoderRing = { encode: function (plaintext) { return plaintext .split('') .map( char => char.charCodeAt() ) .map( code => code + 1 ) .map( code =>..." | `normalized:L4313-L4331` | [Source](../sources/js-allonge.md) |
| Functions can be stored as values within objects, enabling methods and encapsulation of behavior. | "const SecretDecoderRing = { encode (plaintext) { return plaintext .split('') .map( char => char.charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); },..." | `normalized:L4360-L4377` | [Source](../sources/js-allonge.md) |
| Object properties can be dynamically assigned and modified after creation, supporting flexible data structures. | "name.middleName = 'Austin' name //=> { firstName: 'Leonard', lastName: 'Braithwaite', middleName: 'Austin' }" | `normalized:L4570-L4576` | [Source](../sources/js-allonge.md) |
| JavaScript provides utility methods like Object.assign for combining or copying object properties. | "Object.assign(inventory, shipment)" | `normalized:L6484-L6484` | [Source](../sources/js-allonge.md) |
| JavaScript provides utility methods like Object.assign for combining or copying object properties. | "Object.assign({}, { apples: 12, oranges: 12 })" | `normalized:L6470-L6473` | [Source](../sources/js-allonge.md) |
| Objects can define iterators to enable iteration over their contents using standard JavaScript protocols. | "The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript..." | `normalized:L6741-L6743` | [Source](../sources/js-allonge.md) |
| Objects can define iterators to enable iteration over their contents using standard JavaScript protocols. | "const Stack2 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[this.index] = undefined; if..." | `normalized:L6809-L6843` | [Source](../sources/js-allonge.md) |
| Objects can be used to implement complex data structures such as pairs and collections through composition and method definitions. | "const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false, [Symbol.iterator]: function () { let currentPair = this; return { next: () => { if (currentPair.isEmpty()) {..." | `normalized:L8767-L8787` | [Source](../sources/js-allonge.md) |
| Objects can utilize arrays as keys, allowing for advanced mapping strategies based on complex data structures. | "const moveLookupTable = { [[ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]]: 0, [[ 'o', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]]: 6, [[ 'o', 'x', 'x', ' ', ' ', ' ', 'o', ' ', ' ' ]]: 3, [[ 'o',..." | `normalized:L9339-L9388` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
