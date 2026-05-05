---
title: Objects
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Objects

In JavaScript, objects serve as flexible dictionaries that map string keys to values, enabling the storage of heterogeneous data through literal syntax and supporting various access patterns including bracket and dot notation.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| JavaScript objects serve as dictionaries mapping string keys to values, providing a flexible way to store heterogeneous data | "In JavaScript, an object is a map from string keys to values." | `normalized:L4258` | [Source](../sources/js-allonge.md) |
| JavaScript objects can be created using literal syntax | "JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day: { year: 2012, month: 6, day: 14 }" | `normalized:L4268` | [Source](../sources/js-allonge.md) |
| Objects in JavaScript can store any type of value including functions and other objects | "All containers can contain any value, including functions or other containers, like a fat arrow function: const Mathematics = { abs: (a) => a < 0 ? -a : a };" | `normalized:L4306` | [Source](../sources/js-allonge.md) |
| Object properties can be accessed using bracket notation with strings or dot notation for alphanumeric keys | "Objects use [] to access the values by name, using a string: { year: 2012, month: 6, day: 14 }['day']" | `normalized:L4274` | [Source](../sources/js-allonge.md) |
| JavaScript objects support compact method syntax for defining functions as object properties | "There is a "compact method syntax" for binding named function expressions to keywords: const SecretDecoderRing = { encode (plaintext) { return plaintext .split('').map( char => char.charCodeAt() ).map( code => code + 1 ).map( code => String.fromCharCode(code) ).join(''); }, decode (cyphertext) { return cyphertext .split('').map( char => char.charCodeAt() ).map( code => code - 1 ).map( code => String.fromCharCode(code) ).join(''); } }" | `normalized:L4360` | [Source](../sources/js-allonge.md) |
| You can add new properties to an object by assigning a value to a property name that doesn't exist yet | "name.middleName = 'Austin'" | `normalized:L4570` | [Source](../sources/js-allonge.md) |
| Object.assign can be used to extend one object with properties from another | "You can extend one object with another: Object.assign(inventory, shipment)" | `normalized:L6484` | [Source](../sources/js-allonge.md) |
| Object.assign can be used to copy an object by extending an empty object | "You can copy an object by extending an empty object: Object.assign({}, {apples: 12, oranges: 12})" | `normalized:L6470` | [Source](../sources/js-allonge.md) |
| Objects can encapsulate data and behavior together | "const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[this.index] = undefined; if (this.index >= 0) { this.index -= 1 } return value }, isEmpty () { return this.index < 0 }, iterator () { let iterationIndex = this.index; return () => { if (iterationIndex > this.index) { iterationIndex = this.index; } if (iterationIndex < 0) { return {done: true}; } else { return {done: false, value: this.array[iterationIndex--]} } } } });" | `normalized:L6690` | [Source](../sources/js-allonge.md) |
| Object-oriented collections can delegate implementation details to generic iterable operations | "Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith." | `normalized:L8221` | [Source](../sources/js-allonge.md) |

## Why it matters

Objects in JavaScript provide a fundamental data structure for organizing and manipulating heterogeneous data. They enable flexible key-value storage, support complex nested structures including functions and other objects, and offer multiple ways to access properties. The ability to dynamically add properties and use methods like Object.assign allows for powerful object manipulation patterns. Furthermore, objects facilitate encapsulation of both data and behavior, making them essential for implementing object-oriented programming concepts in JavaScript.

## Source pages

- [Source](../sources/js-allonge.md)