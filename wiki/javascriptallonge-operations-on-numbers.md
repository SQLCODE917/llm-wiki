---
page_id: javascriptallonge-operations-on-numbers
page_kind: source
summary: operations on numbers from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.26-27
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé covers operations on numbers, including arithmetic operators, precedence, and additional operators like modulus and bitwise operations.

## Key supported claims

- JavaScript uses arithmetic operators like +, -, *, and / to create expressions (raw/javascriptallonge.pdf p.26-27).
- Operators have precedence, so 2 * 5 + 1 is evaluated as (2 * 5) + 1 (raw/javascriptallonge.pdf p.26-27).
- JavaScript supports additional operators such as modulus % and unary negation - (raw/javascriptallonge.pdf p.26-27).

## Technical details

### `technical-atom-86535bd19717c695` code

Citation: (raw/javascriptallonge.pdf p.26-27)

```javascript
2 * 5 + 1 //=> 11 1 + 5 * 2 //=> 11
```

### `technical-atom-d0aad52ee8c53e7f` worked-example

Citation: (raw/javascriptallonge.pdf p.26-27)

We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 .

## Related technical details

### From [[javascriptallonge-as-little-as-possible-about-functions-but-no-less]]: `technical-atom-dbe44efe552e814c` requirement

Relation: nearby source page; matched terms `function`, `has`, `javascript`

Citation: (raw/javascriptallonge.pdf p.30-31)

But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

### From [[javascriptallonge-floating]]: `technical-atom-02b0bf8004b983cd` requirement

Relation: nearby source page; matched terms `arithmetic`, `have`, `more`, `numbers`

Citation: (raw/javascriptallonge.pdf p.25-26)

But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 .

### From [[javascriptallonge-floating]]: `technical-atom-d907c07935ec06a5` worked-example

Relation: nearby source page; matched terms `javascript`, `numbers`, `these`

Citation: (raw/javascriptallonge.pdf p.25-26)

We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers.
