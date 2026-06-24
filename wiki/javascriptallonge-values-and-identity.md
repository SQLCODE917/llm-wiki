---
page_id: javascriptallonge-values-and-identity
page_kind: source
summary: values and identity from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.21-21
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on values and identity in JavaScript Allongé.

## Key supported claims

- The === operator in JavaScript tests whether two values are identical (raw/javascriptallonge.pdf p.21-21).
- Values of different types in JavaScript are never identical (raw/javascriptallonge.pdf p.21-21).
- Values of the same type but different content in JavaScript are not identical (raw/javascriptallonge.pdf p.21-21).

## Technical details

### `technical-atom-8bcbda933bb72dcb` code

Citation: (raw/javascriptallonge.pdf p.21)

```javascript
2 === 2 //=> true 'hello' !== 'goodbye' //=> true
```

### `technical-atom-cf7c08bb5dbc2329` code

Citation: (raw/javascriptallonge.pdf p.21)

```javascript
2 === '2' //=> false true !== 'true' //=> true
```

### `technical-atom-62ad60ef6f731bb9` code

Citation: (raw/javascriptallonge.pdf p.21)

```javascript
true === false //=> false 2 !== 5 //=> true 'two' === 'five' //=> false
```

### `technical-atom-62ac41d9e7c334de` code

Citation: (raw/javascriptallonge.pdf p.21)

```
In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:
```

### `technical-atom-9a6c1c132a3d3462` procedure

Citation: (raw/javascriptallonge.pdf p.21)

And then you're shown another cup of coffee.

### `technical-atom-b5a75dfd93d8a668` procedure

Citation: (raw/javascriptallonge.pdf p.21)

First, sometimes, the cups are of different kinds.

### `technical-atom-29882a09023a1a70` worked-example

Citation: (raw/javascriptallonge.pdf p.21)

For example, the string "2" is not the same thing as the number 2 .

### `technical-atom-ce645dd09a6b9040` worked-example

Citation: (raw/javascriptallonge.pdf p.21)

This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

## Related technical details

### From [[javascriptallonge-what-javascript-allong-is-and-isn-t]]: `technical-atom-a88c178dfe08b992` worked-example

Relation: nearby source page; matched terms `allong`, `different`, `javascript`, `worked-example`

Citation: (raw/javascriptallonge.pdf p.10-11)

For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source.

### From [[javascriptallonge-what-javascript-allong-is-and-isn-t]]: `technical-atom-a43838c767b6eaed` code

Relation: nearby source page; matched terms `allong`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.10-11)

```javascript
const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } });
```

### From [[javascriptallonge-what-javascript-allong-is-and-isn-t]]: `technical-atom-b1be71a4ab47a537` code

Relation: nearby source page; matched terms `allong`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.10-11)

```javascript
const filterWith = (fn, iterable) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { if (!!fn(element)) yield element; } } });
```

### From [[javascriptallonge-what-javascript-allong-is-and-isn-t]]: `technical-atom-7e00a5ef835a9f73` requirement

Relation: nearby source page; matched terms `allong`, `javascript`, `same`

Citation: (raw/javascriptallonge.pdf p.10-11)

Should code written by a small team of specialists use the same techniques and patterns as code maintained by a continuously changing cast of inexperienced interns?
