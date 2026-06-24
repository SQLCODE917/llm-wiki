---
page_id: javascriptallonge-a-warm-cup-basic-strings-and-quasi-literals
page_kind: source
summary: A Warm Cup: Basic Strings and Quasi-Literals from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.202-203
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on basic strings and quasi-literals in JavaScript Allongé.

## Key supported claims

- Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. (raw/javascriptallonge.pdf p.202-203)
- There are operators that can be used on strings. (raw/javascriptallonge.pdf p.202-203)
- String manipulation is extremely common in programming. (raw/javascriptallonge.pdf p.202-203)
- For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line'. (raw/javascriptallonge.pdf p.202-203)

## Technical details

### `technical-atom-1682a5d04ab0b8ac` code

Citation: (raw/javascriptallonge.pdf p.202-203)

```javascript
'fu' + 'bar' //=> 'fubar'
```

### `technical-atom-a0d1e0ac69fe7f62` worked-example

Citation: (raw/javascriptallonge.pdf p.202-203)

For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line' .

## Related technical details

### From [[javascriptallonge-quasi-literals]]: `technical-atom-0397927ede51fe53` procedure

Relation: nearby source page; matched terms `literals`, `quasi`, `string`

Citation: (raw/javascriptallonge.pdf p.203-204)

The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

### From [[javascriptallonge-why]]: `technical-atom-adca9ea1d55f4eb3` worked-example

Relation: nearby source page; matched terms `example`, `worked-example`, `writing`

Citation: (raw/javascriptallonge.pdf p.201)

For example, you could start by writing:

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-f9a05369dedddd46` requirement

Relation: nearby source page; matched terms `basic`, `method`, `special`

Citation: (raw/javascriptallonge.pdf p.211-215)

The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-13e57f96247ba73c` worked-example

Relation: nearby source page; matched terms `basic`, `example`, `worked-example`

Citation: (raw/javascriptallonge.pdf p.211-215)

For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.
