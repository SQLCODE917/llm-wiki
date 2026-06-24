---
page_id: javascriptallonge-how-to-run-the-examples
page_kind: source
summary: How to run the examples from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.289-290
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains how to run the examples from JavaScript Allongé, focusing on the use of transpilers like Traceur and Babel to handle ECMAScript 2015 code in environments that do not yet support it.

## Key supported claims

- All examples were tested using Google Traceur Compiler or Babel, which are transpilers that parse ECMAScript 2015 code and emit valid ECMAScript-5 code (raw/javascriptallonge.pdf p.289-290).
- Both tools offer online areas to type ECMAScript code and see the ECMAScript-5 equivalent, and you can run the code as well (raw/javascriptallonge.pdf p.289-290).
- You may have to use the console in your web browser to see the result of your expressions, as the code must be written with console.log for output (raw/javascriptallonge.pdf p.289-290).

## Technical details

### `technical-atom-da7dcd6f0c74f94e` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
const before = (decoration) => (method) => function () { decoration.apply( this , arguments); return method.apply( this , arguments) };
```

### `technical-atom-bfdd92b0ff7b2470` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
"use strict" var before = function (decoration) { return function (method) { return function () { decoration.apply( this , arguments); return method.apply( this , arguments); }; }; };
```

### `technical-atom-e2cbc913e09ebbfa` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```
100 101 http://babeljs.io/
```

### `technical-atom-ad281399ada1cea7` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
const before = (decoration) => (method) => function (...args) { decoration.apply( this , args); return method.apply( this , args) }; And it would be 'transpiled' into: var before = function (decoration) { return function (method) { return function () { for ( let _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( this , args); return method.apply( this , args); }; }; };
```

### `technical-atom-d55e747fda1e4f57` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
(() => 2 + 2)()
```

### `technical-atom-457ddf6a4dba93cb` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
console.log( (() => 2 + 2)() )
```

### `technical-atom-d86ccc4d0beb1097` procedure

Citation: (raw/javascriptallonge.pdf p.289-290)

Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics.

### `technical-atom-1a832844dd3ca479` worked-example

Citation: (raw/javascriptallonge.pdf p.289-290)

For example, this ECMAScript 2015 code:

## Related technical details

### From [[javascriptallonge-richard-feynman]]: `technical-atom-ef5f2f7fff6b3605` exception

Relation: nearby source page; matched terms `all`, `explains`, `how`, `using`

Citation: (raw/javascriptallonge.pdf p.292)

Richard Feynman's QED 105 wasanother inspiration: A book that explains Quantum Electrodynamics and the 'Sum of the Histories' methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening-such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane-are all wrong.

### From [[javascriptallonge-a-pull-of-the-lever-prefaces]]: `technical-atom-e8a303faa22d26b5` requirement

Relation: nearby source page; matched terms `method`, `result`, `use`

Citation: (raw/javascriptallonge.pdf p.6)

'The important thing is that neither method of preparation should use so much water as to result in a sickly, pale ghost of Espresso.
