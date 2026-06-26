---
page_id: javascriptallonge-as-little-as-possible-about-functions-but-no-less
page_kind: source
summary: As Little As Possible About Functions, But No Less from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.30-38
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter introduces basic functions in JavaScript, covering their representation as values, identity (as reference types), application, and how to return values and expressions from functions.

## Key supported claims

- Functions in JavaScript are values representing computations (raw/javascriptallonge.pdf p.30-38).
- Functions are reference types, not value types (raw/javascriptallonge.pdf p.30-38).
- Functions are applied to arguments to produce a value (raw/javascriptallonge.pdf p.30-38).
- Functions can return values or evaluate expressions (raw/javascriptallonge.pdf p.30-38).
- Functions can return other functions (raw/javascriptallonge.pdf p.30-38).

## Technical details

### `technical-atom-d7bf8573ef18d9c4` code

Citation: (raw/javascriptallonge.pdf p.30-38)

```javascript
> 16 The simplest possible function is () => {}, we’ll see that later.
```

### `technical-atom-692965100fdc06e7` code

Citation: (raw/javascriptallonge.pdf p.30-38)

```javascript
(() => 0) === (() => 0)
```

### `technical-atom-7d3a4a47ef531ed5` code

Citation: (raw/javascriptallonge.pdf p.30-38)

```javascript
(() => 0)() //=> 0
```

### `technical-atom-768edade4f61bb08` code

Citation: (raw/javascriptallonge.pdf p.30-38)

```javascript
(() => 1)() //=> 1 (() => "Hello, JavaScript")() //=> "Hello, JavaScript" (() => Infinity)() //=> Infinity
```

### `technical-atom-f10d0ee0f9a27539` code

Citation: (raw/javascriptallonge.pdf p.30-38)

```javascript
(() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity
```

### `technical-atom-5d5fc95fbaf36e10` code

Citation: (raw/javascriptallonge.pdf p.30-38)

```javascript
(() => (() => 0)())() //=> 0
```

### `technical-atom-80aebdeb09a79181` code

Citation: (raw/javascriptallonge.pdf p.30-38)

```javascript
(() => (1 + 1, 2 + 2))() //=> 4
```

### `technical-atom-9a9fb89fab463626` code

Citation: (raw/javascriptallonge.pdf p.30-38)

```javascript
() => (1 + 1, 2 + 2)
```

## Related technical details

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-6f035a06fb85b432` code

Relation: nearby source page; matched terms `about`, `arguments`, `but`, `can`, `function`, `functions`

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.
```

### From [[javascriptallonge-a-rich-aroma-basic-numbers]]: `technical-atom-2fdee7ba3e1580d5` code

Relation: nearby source page; matched terms `basic`, `function`, `representing`, `types`, `value`, `values`

Citation: (raw/javascriptallonge.pdf p.24-27)

```javascript
In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.— Wikipedia[12]
```

### From [[javascriptallonge-values-and-identity]]: `technical-atom-047883408a2c29a2` code

Relation: nearby source page; matched terms `identity`, `javascript`, `not`, `they`, `values`, `whether`

Citation: (raw/javascriptallonge.pdf p.21-23)

```
In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:
```

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please]]: `technical-atom-07b4f982763531cb` code

Relation: nearby source page; matched terms `arguments`, `expressions`, `function`, `functions`, `values`

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
Expressions consist either of representations of values (like 3.14159265, true, and undefined), operators that combine expressions (like 3 + 2), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments) { body-statements } for creating functions.
```
