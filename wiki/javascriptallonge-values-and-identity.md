---
page_id: javascriptallonge-values-and-identity
page_kind: source
summary: values and identity from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.21-23
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses JavaScript values, identity, and the === operator, using coffee cup metaphors to explain value types and reference types.

## Key supported claims

- JavaScript uses === to test if two values are identical, and !== to test if they are not identical (raw/javascriptallonge.pdf p.21-23).
- Values of the same type with the same content are identical, such as strings, numbers, and booleans (raw/javascriptallonge.pdf p.21-23).
- Arrays and functions are reference types; even if they look the same, they are not identical with === (raw/javascriptallonge.pdf p.21-23).

## Technical details

### `technical-atom-047883408a2c29a2` code

Citation: (raw/javascriptallonge.pdf p.21-23)

```
In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:
```

### `technical-atom-3d6dcd93a42c7f4f` code

Citation: (raw/javascriptallonge.pdf p.21-23)

```javascript
2 === 2 //=> true 'hello' !== 'goodbye' //=> true
```

### `technical-atom-e94990165303b45c` code

Citation: (raw/javascriptallonge.pdf p.21-23)

```javascript
2 === '2' //=> false true !== 'true' //=> true
```

### `technical-atom-e112b43d01b2d97c` code

Citation: (raw/javascriptallonge.pdf p.21-23)

```javascript
true === false //=> false 2 !== 5 //=> true 'two' === 'five' //=> false
```

### `technical-atom-b107898923bfbe97` code

Citation: (raw/javascriptallonge.pdf p.21-23)

```javascript
- 2 + 2 === 4 //=> true
```

### `technical-atom-6cf13d48545d00c0` code

Citation: (raw/javascriptallonge.pdf p.21-23)

```javascript
- (2 + 2 === 4) === (2 !== 5) //=> true
```

### `technical-atom-b531f58f4fd3abe3` procedure

Citation: (raw/javascriptallonge.pdf p.21-23)

And then you’re shown another cup of coffee.

### `technical-atom-bf45c9ac88cf9921` procedure

Citation: (raw/javascriptallonge.pdf p.21-23)

First, sometimes, the cups are of different kinds.

## Related technical details

### From [[javascriptallonge-a-rich-aroma-basic-numbers]]: `technical-atom-2fdee7ba3e1580d5` code

Relation: nearby source page; matched terms `arrays`, `booleans`, `numbers`, `strings`, `such`, `type`

Citation: (raw/javascriptallonge.pdf p.24-27)

```javascript
In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.— Wikipedia[12]
```

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please]]: `technical-atom-07b4f982763531cb` code

Relation: nearby source page; matched terms `arrays`, `functions`, `true`, `values`

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
Expressions consist either of representations of values (like 3.14159265, true, and undefined), operators that combine expressions (like 3 + 2), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments) { body-statements } for creating functions.
```

### From [[javascriptallonge-a-rich-aroma-basic-numbers]]: `technical-atom-1fc4f4d7cccf56ac` exception

Relation: nearby source page; matched terms `javascript`, `not`, `numbers`

Citation: (raw/javascriptallonge.pdf p.24-27)

Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

### From [[javascriptallonge-a-rich-aroma-basic-numbers]]: `technical-atom-33ed5a77d524cfa4` worked-example

Relation: nearby source page; matched terms `javascript`, `numbers`, `worked-example`

Citation: (raw/javascriptallonge.pdf p.24-27)

For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1.
