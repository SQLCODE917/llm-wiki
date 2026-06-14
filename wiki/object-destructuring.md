---
category: concept
summary: JavaScript object destructuring syntax and examples, including compact method syntax. sources: raw/javascriptallonge.pdf p.126-140
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

## Object Destructuring

JavaScript allows extracting properties from objects using destructuring syntax. Key examples:

- **Basic Destructuring**: `{ name: { first: given, last: surname }, occupation: { title: title } } = user` extracts nested properties.

- **Compact Method Syntax**: `{ encode(plaintext) { ... }, decode(cyphertext) { ... } }` binds named functions to object keys concisely.

- **Literal Syntax**: `{ year: 2012, month: 6, day: 14 }` creates objects with key-value pairs. Access via `date['day']` or `date.day`.

- **Examples**: The `SecretDecoderRing` object demonstrates functions bound to keys using both traditional and compact syntax.

Cite: (raw/javascriptallonge.pdf p.126-140)
