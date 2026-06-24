---
page_id: javascriptallonge-richard-feynman
page_kind: source
summary: Richard Feynman from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.292-292
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Richard Feynman's QED explains Quantum Electrodynamics and the 'Sum of the Histories' methodology using the simple expedient of explaining how light reflects off a mirror.

## Key supported claims

- Richard Feynman's QED 105 was another inspiration: A book that explains Quantum Electrodynamics and the 'Sum of the Histories' methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening—such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane—are all wrong. (raw/javascriptallonge.pdf p.292-292)

## Technical details

### `technical-atom-c2221cfe16124f04` formula

Citation: (raw/javascriptallonge.pdf p.292)

105 http://www.amzn.com/0691125759?tag=raganwald001-20

### `technical-atom-ef5f2f7fff6b3605` exception

Citation: (raw/javascriptallonge.pdf p.292)

Richard Feynman's QED 105 wasanother inspiration: A book that explains Quantum Electrodynamics and the 'Sum of the Histories' methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening-such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane-are all wrong.

## Related technical details

### From [[javascriptallonge-how-to-run-the-examples]]: `technical-atom-ad281399ada1cea7` code

Relation: nearby source page; matched terms `function`, `how`, `key`, `method`

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
const before = (decoration) => (method) => function (...args) { decoration.apply( this , args); return method.apply( this , args) }; And it would be 'transpiled' into: var before = function (decoration) { return function (method) { return function () { for ( let _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( this , args); return method.apply( this , args); }; }; };
```

### From [[javascriptallonge-how-to-run-the-examples]]: `technical-atom-da7dcd6f0c74f94e` code

Relation: nearby source page; matched terms `function`, `how`, `method`

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
const before = (decoration) => (method) => function () { decoration.apply( this , arguments); return method.apply( this , arguments) };
```

### From [[javascriptallonge-how-to-run-the-examples]]: `technical-atom-bfdd92b0ff7b2470` code

Relation: nearby source page; matched terms `function`, `how`, `method`

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
"use strict" var before = function (decoration) { return function (method) { return function () { decoration.apply( this , arguments); return method.apply( this , arguments); }; }; };
```
