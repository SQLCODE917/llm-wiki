---
title: Objects
type: concept
tags: [javascript, data-structures, literals]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L4258-L4258
  - js-allonge:normalized:L4267-L4270
  - js-allonge:normalized:L4274-L4276
  - js-allonge:normalized:L4302-L4305
  - js-allonge:normalized:L4306-L4311
  - js-allonge:normalized:L4570-L4576
  - js-allonge:normalized:L6484-L6484
  - js-allonge:normalized:L9337-L9388
---

# Objects

## Summary

In JavaScript, objects are collections of key-value pairs used to store and organize data. They support various ways of defining properties, accessing values, and can contain nested structures including functions.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| An object in JavaScript is fundamentally a mapping from string keys to values, enabling flexible data organization. | "In JavaScript, an object is a map from string keys to values." | `normalized:L4258-L4258` | [Source](../sources/js-allonge.md) |
| JavaScript provides a concise literal syntax for creating objects, allowing direct assignment of key-value pairs without explicit constructor calls. | "JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day: { year: 2012, month: 6, day: 14 }" | `normalized:L4267-L4270` | [Source](../sources/js-allonge.md) |
| Properties within objects can be accessed using bracket notation, which supports both alphanumeric and non-alphanumeric key names when quoted. | "Objects use [] to access the values by name, using a string: { year: 2012, month: 6, day: 14 }['day']" | `normalized:L4274-L4276` | [Source](../sources/js-allonge.md) |
| Object properties can hold any type of value, including functions, making them suitable for defining methods and encapsulating behavior. | "All containers can contain any value, including functions or other containers, like a fat arrow function: const Mathematics = { abs: (a) => a < 0 ? -a : a };" | `normalized:L4306-L4311` | [Source](../sources/js-allonge.md) |
| Objects support dynamic property assignment and modification, allowing runtime changes to their structure. | "name.middleName = 'Austin' name //=> { firstName: 'Leonard', lastName: 'Braithwaite', middleName: 'Austin' }" | `normalized:L4570-L4576` | [Source](../sources/js-allonge.md) |
| The Object.assign method facilitates copying properties from one object to another, useful for merging configurations or extending functionality. | "Object.assign(inventory, shipment)" | `normalized:L6484-L6484` | [Source](../sources/js-allonge.md) |
| JavaScript objects can utilize computed property names via bracket expressions, enabling keys derived from expressions or variables. | "{ ["p" + "i"]: 3.14159265 } //=> {"pi":3.14159265}" | `normalized:L4302-L4305` | [Source](../sources/js-allonge.md) |
| Objects can serve as maps where keys are not limited to strings but can be any expression, provided they are converted to strings. | "We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we..." | `normalized:L9337-L9388` | [Source](../sources/js-allonge.md) |

## Why it matters

Objects are fundamental to JavaScript's data modeling capabilities. They allow developers to represent complex real-world entities and relationships, encapsulate behavior through methods, and provide flexible storage mechanisms for dynamic applications.

## Related pages

- [Iterators](../concepts/iterators.md)

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
