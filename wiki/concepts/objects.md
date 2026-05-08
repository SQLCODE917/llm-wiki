---
title: Objects
type: concept
tags: []
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
---

# Objects

In JavaScript, objects serve as fundamental data structures that map string keys to values, functioning as collections where each key-value pair represents a property of the object. They can be instantiated through literal syntax, which allows for direct specification of key-value pairs, and possess unique identities even when their contents are identical. Properties within objects can be accessed using either bracket or dot notation, depending on whether the key is a valid identifier. Additionally, objects can store functions as values, enabling method definitions, and support operations like copying properties between objects using utilities such as `Object.assign`.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript objects are maps from string keys to values. | "In JavaScript, an object is a map from string keys to values." | normalized:L3159-L3159 | [Source](../sources/js-allonge.md) |
| JavaScript objects can be created using literal syntax with key-value pairs. | "## **literal object syntax** JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day: - { year: 2012, month: 6, day: 14 }" | normalized:L3167-L3171 | [Source](../sources/js-allonge.md) |
| Objects created with literal syntax have different identities even if they have the same content. | "Two objects created with separate evaluations have differing identities, just like arrays: - { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_" | normalized:L3173-L3175 | [Source](../sources/js-allonge.md) |
| Object properties can be accessed using bracket notation with strings. | "Objects use [] to access the values by name, using a string: - { year: 2012, month: 6, day: 14 }['day'] _//=> 14_" | normalized:L3177-L3179 | [Source](../sources/js-allonge.md) |
| Object properties can be accessed using dot notation when the key is a valid identifier. | "date['day'] === date.day _//=> true_" | normalized:L3205-L3205 | [Source](../sources/js-allonge.md) |
| Object keys can be computed expressions enclosed in brackets. | "Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ]: { ["p" + "i"]: 3.14159265 } _//=> {"pi":3.14159265}_" | normalized:L3207-L3209 | [Source](../sources/js-allonge.md) |
| Objects can contain functions as values. | "All containers can contain any value, including functions or other containers, like a fat arrow function: **const** Mathematics = { abs: (a) => a < 0 ? -a : a }; Mathematics.abs(-5) _//=> 5_" | normalized:L3211-L3213 | [Source](../sources/js-allonge.md) |
| Object.assign can be used to copy properties from one object to another, effectively extending an object with properties from another. | "**const** inventory = { apples: 12, oranges: 12 }; **const** shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment)" | normalized:L4539-L4539 | [Source](../sources/js-allonge.md) |
| Object.assign can be used to copy all properties from one object to another by extending an empty object. | "Object.assign({}, { apples: 12, oranges: 12 }) _//=> { apples: 12, oranges: 12 }_" | normalized:L4535-L4535 | [Source](../sources/js-allonge.md) |
| The author has authored libraries for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. | "When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg "Raganwald" Braithwaite has authored libraries[221] for JavaScript, CoffeeScript,..." | normalized:L6477-L6477 | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding JavaScript objects is crucial because they form the backbone of data organization and behavior in the language. Their ability to hold both data and functions makes them essential for creating reusable and modular code. The distinction between identity and content helps developers understand how equality works with objects, while various access methods provide flexibility in working with dynamic property names. Tools like `Object.assign` enable powerful patterns for object composition and extension, which are foundational in functional programming approaches within JavaScript.

## Source pages

- [Source](../sources/js-allonge.md)
```