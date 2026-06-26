---
page_id: javascriptallonge-about-javascript-allong
page_kind: source
summary: About JavaScript Allongé from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.7-9
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé is a first and foremost, a book about programming with functions. It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope.

## Key supported claims

- JavaScript Allongé is a book about programming with functions, written in JavaScript for its perfect sweet spot of being widely used with proper first-class functions (raw/javascriptallonge.pdf p.7-9).
- The book begins at the beginning with values and expressions, building to types, identity, functions, closures, scopes, collections, iterators, and classes (raw/javascriptallonge.pdf p.7-9).
- It teaches how to handle complex code and simplify it without dumbing it down, making it a rich read on JavaScript's subtleties (raw/javascriptallonge.pdf p.7-9).

## Technical details

### `technical-atom-b6326ae2779c19b2` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```
for ( int i = 0; i < array.length; ++i) {
```

### `technical-atom-f865bca0189c3406` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```
var i;
```

### `technical-atom-fcef76e420062c39` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```

### `technical-atom-2c2deb7ff6b1c072` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
function foo () { var first = arguments[0], rest = [].slice.call(arguments, 1); // ... }
```

### `technical-atom-59aa4f640fbaaacb` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
for ( let i = 0; i < array.length; ++i) { // ... }
```

### `technical-atom-653ce954a299106d` code

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
function foo (first, ...rest) { // ...
```

### `technical-atom-e1907bc36d10e981` exception

Citation: (raw/javascriptallonge.pdf p.7-9)

_JavaScript Allongé_ teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down.

### `technical-atom-dec96b6e058217c0` worked-example

Citation: (raw/javascriptallonge.pdf p.7-9)

For example, JavaScript did not include block-structured variables.

## Related technical details

### From [[javascriptallonge-a-rich-aroma-basic-numbers]]: `technical-atom-2fdee7ba3e1580d5` code

Relation: nearby source page; matched terms `code`, `function`, `programming`, `rich`, `types`, `values`

Citation: (raw/javascriptallonge.pdf p.24-27)

```javascript
In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.— Wikipedia[12]
```

### From [[javascriptallonge-what-javascript-allong-is-and-isn-t]]: `technical-atom-0223e65089dcbedc` code

Relation: nearby source page; matched terms `allong`, `code`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.10-12)

```javascript
const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } });
```

### From [[javascriptallonge-what-javascript-allong-is-and-isn-t]]: `technical-atom-f16b184216c43f2a` code

Relation: nearby source page; matched terms `allong`, `code`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.10-12)

```javascript
const filterWith = (fn, iterable) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { if (!!fn(element)) yield element; } } });
```

### From [[javascriptallonge-values-and-identity]]: `technical-atom-047883408a2c29a2` code

Relation: nearby source page; matched terms `code`, `identity`, `javascript`, `values`

Citation: (raw/javascriptallonge.pdf p.21-23)

```
In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:
```
