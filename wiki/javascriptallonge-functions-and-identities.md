---
page_id: javascriptallonge-functions-and-identities
page_kind: source
summary: functions and identities from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.31-31
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

A section on functions and identities in JavaScript Allongé, discussing how functions are reference types and how evaluating expressions produces new, non-identical functions.

## Key supported claims

- Functions are reference types in JavaScript (raw/javascriptallonge.pdf p.31-31).
- Each evaluation of a function expression produces a new function (raw/javascriptallonge.pdf p.31-31).
- Parentheses are used to appease the JavaScript parser when defining functions (raw/javascriptallonge.pdf p.31-31).

## Technical details

### `technical-atom-b45c93b762c2d46e` code

Citation: (raw/javascriptallonge.pdf p.31)

```javascript
(() => 0) === (() => 0) //=> false
```

## Related technical details

### From [[javascriptallonge-functions-that-return-values-and-evaluate-expressions]]: `technical-atom-053e216a0ba143de` code

Relation: nearby source page; matched terms `expressions`, `functions`, `javascript`

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => 1)() //=> 1 (() => "Hello, JavaScript")() //=> "Hello, JavaScript" (() => Infinity )() //=> Infinity
```

### From [[javascriptallonge-functions-that-return-values-and-evaluate-expressions]]: `technical-atom-b5a28ac67439659d` code

Relation: nearby source page; matched terms `expressions`, `functions`, `javascript`

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity
```

### From [[javascriptallonge-as-little-as-possible-about-functions-but-no-less]]: `technical-atom-dbe44efe552e814c` requirement

Relation: nearby source page; matched terms `function`, `functions`, `javascript`

Citation: (raw/javascriptallonge.pdf p.30-31)

But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

### From [[javascriptallonge-functions-that-return-values-and-evaluate-expressions]]: `technical-atom-3ac7bed3402992a5` worked-example

Relation: nearby source page; matched terms `expression`, `expressions`, `functions`

Citation: (raw/javascriptallonge.pdf p.32-33)

For example, (() => 0)() is an expression.
