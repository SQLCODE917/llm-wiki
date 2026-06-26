---
page_id: javascriptallonge-a-rich-aroma-basic-numbers
page_kind: source
summary: A Rich Aroma: Basic Numbers from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.24-27
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers literals, number representations, and basic operations in JavaScript.

## Key supported claims

- JavaScript has literals for atomic values such as integers, floating-point numbers, and strings, (raw/javascriptallonge.pdf p.24-27)
- A literal like 42 represents the number forty-two, which is 42 base 10, (raw/javascriptallonge.pdf p.24-27)
- Internally, numbers are represented as double-precision floating point numbers, (raw/javascriptallonge.pdf p.24-27)
- The largest integer JavaScript can safely handle is 9007199254740991, or 2^53 - 1, (raw/javascriptallonge.pdf p.24-27)
- Floating point numbers can lead to inexactitude, such as 0.1 + 0.1 + 0.1 not equaling 0.3, (raw/javascriptallonge.pdf p.24-27)

## Technical details

### `technical-atom-2fdee7ba3e1580d5` code

Citation: (raw/javascriptallonge.pdf p.24-27)

```javascript
In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.— Wikipedia[12]
```

### `technical-atom-1fc4f4d7cccf56ac` exception

Citation: (raw/javascriptallonge.pdf p.24-27)

Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

### `technical-atom-46c5d6c18d4ee16d` exception

Citation: (raw/javascriptallonge.pdf p.24-27)

Most programmers never encounter the limit on the magnitude of an integer.

### `technical-atom-33ed5a77d524cfa4` worked-example

Citation: (raw/javascriptallonge.pdf p.24-27)

For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1.

### `technical-atom-b5baf419a49989ef` worked-example

Citation: (raw/javascriptallonge.pdf p.24-27)

We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers.

### `technical-atom-9cd748928c271ecf` worked-example

Citation: (raw/javascriptallonge.pdf p.24-27)

One of the most oft-repeated examples is this:

### `technical-atom-cc122154c131d5bc` worked-example

Citation: (raw/javascriptallonge.pdf p.24-27)

For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982.

### `technical-atom-53506ac332f632f7` worked-example

Citation: (raw/javascriptallonge.pdf p.24-27)

For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.

## Related technical details

### From [[javascriptallonge-values-and-identity]]: `technical-atom-047883408a2c29a2` code

Relation: nearby source page; matched terms `identity`, `javascript`, `not`, `values`

Citation: (raw/javascriptallonge.pdf p.21-23)

```
In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:
```

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-6f035a06fb85b432` code

Relation: nearby source page; matched terms `can`, `function`, `not`, `same`, `you`

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.
```

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please]]: `technical-atom-07b4f982763531cb` code

Relation: nearby source page; matched terms `function`, `like`, `representations`, `values`

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
Expressions consist either of representations of values (like 3.14159265, true, and undefined), operators that combine expressions (like 3 + 2), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments) { body-statements } for creating functions.
```

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please]]: `technical-atom-059258f79c64cecb` code

Relation: nearby source page; matched terms `can`, `expression`, `function`, `like`

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
This loose definition is recursive, so we can intuit (or use our experience with other languages) that since a function can contain a return statement with an expression, we can write a function that returns a function, or an array that contains another array expression. Or a function that returns an array, an array of functions, a function that returns an array of functions, and so forth:
```
