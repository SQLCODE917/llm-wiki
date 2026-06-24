---
page_id: javascriptallonge-floating
page_kind: source
summary: floating from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.25-26
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses floating-point representation in JavaScript, including how numbers are represented internally as floating point, and the implications for handling monetary amounts.

## Key supported claims

- But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers (raw/javascriptallonge.pdf p.25-26).
- We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers (raw/javascriptallonge.pdf p.25-26).
- It's tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, 'Nooooooooooooooooooooo.' A computer's internal representation for a floating point number is binary, while our literal number was in base ten (raw/javascriptallonge.pdf p.25-26).
- Professional programmers almost never use floating point numbers to represent monetary amounts (raw/javascriptallonge.pdf p.25-26).

## Technical details

### `technical-atom-d2490142f4314380` code

Citation: (raw/javascriptallonge.pdf p.25-26)

```javascript
1.0 //=> 1 1.0 + 1.0 //=> 2 1.0 + 1.0 + 1.0 //=> 3
```

### `technical-atom-0ee51eb9d87f4b1b` code

Citation: (raw/javascriptallonge.pdf p.25-26)

```javascript
0.1 //=> 0.1 0.1 + 0.1 //=> 0.2 0.1 + 0.1 + 0.1 //=> 0.30000000000000004
```

### `technical-atom-02b0bf8004b983cd` requirement

Citation: (raw/javascriptallonge.pdf p.25-26)

But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 .

### `technical-atom-fbe1e6b64af346dc` exception

Citation: (raw/javascriptallonge.pdf p.25-26)

Most programmers never encounter the limit on the magnitude of an integer.

### `technical-atom-d907c07935ec06a5` worked-example

Citation: (raw/javascriptallonge.pdf p.25-26)

We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers.

### `technical-atom-12967e399641f4b8` worked-example

Citation: (raw/javascriptallonge.pdf p.25-26)

For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 .

### `technical-atom-54ca14d0839771d1` worked-example

Citation: (raw/javascriptallonge.pdf p.25-26)

For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript's calculation is less than a pixel, there is no observable error.

### `technical-atom-ae43ed904573c8b5` worked-example

Citation: (raw/javascriptallonge.pdf p.25-26)

For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 .

## Related technical details

### From [[javascriptallonge-values-and-identity]]: `technical-atom-ce645dd09a6b9040` worked-example

Relation: nearby source page; matched terms `but`, `example`, `have`, `identity`, `javascript`, `not`

Citation: (raw/javascriptallonge.pdf p.21)

This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

### From [[javascriptallonge-operations-on-numbers]]: `technical-atom-d0aad52ee8c53e7f` worked-example

Relation: nearby source page; matched terms `can`, `example`, `like`, `numbers`, `worked-example`, `write`

Citation: (raw/javascriptallonge.pdf p.26-27)

We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 .

### From [[javascriptallonge-values-and-identity]]: `technical-atom-29882a09023a1a70` worked-example

Relation: nearby source page; matched terms `example`, `identity`, `not`, `number`, `worked-example`

Citation: (raw/javascriptallonge.pdf p.21)

For example, the string "2" is not the same thing as the number 2 .

### From [[javascriptallonge-values-and-identity]]: `technical-atom-62ac41d9e7c334de` code

Relation: nearby source page; matched terms `identity`, `javascript`, `not`, `they`

Citation: (raw/javascriptallonge.pdf p.21)

```
In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:
```
