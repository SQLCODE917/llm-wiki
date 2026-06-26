---
page_id: javascriptallonge-how-to-run-the-examples
page_kind: source
summary: How to run the examples from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.289-290
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This section explains how to run the examples from JavaScript Allongé, which were tested using transpilers like Google Traceur Compiler and Babel to convert ECMAScript 2015 code into ECMAScript-5 code.

## Key supported claims

- The examples in JavaScript Allongé were tested using transpilers like Google Traceur Compiler and Babel (raw/javascriptallonge.pdf p.289-290).
- Both Traceur and Babel are transpilers that parse ECMAScript 2015 code and emit valid ECMAScript-5 code (raw/javascriptallonge.pdf p.289-290).
- To see the result of expressions, you may need to use the console in your web browser, for example, using console.log() (raw/javascriptallonge.pdf p.289-290).

## Technical details

### `technical-atom-cf768d2fea2898c0` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
const before = (decoration) => (method) => function () { decoration.apply( this, arguments); return method.apply( this, arguments) };
```

### `technical-atom-195e22314139bbf7` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
var before = function (decoration) {
```

### `technical-atom-7d789ddd06018887` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
return function (method) {
```

### `technical-atom-9537152fa244317c` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
return function () {
```

### `technical-atom-59b3349290ca71c6` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```
decoration.apply( this, arguments); return method.apply( this, arguments);
```

### `technical-atom-f95d7f03510abd40` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```
}; };
```

### `technical-atom-755c2332ffe34c02` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```
};
```

### `technical-atom-42a29e75c38d9103` code

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
const before = (decoration) => (method) => function (...args) { decoration.apply( this, args); return method.apply( this, args) };
```

## Related technical details

### From [[javascriptallonge-thanks]]: `technical-atom-9f35f622bb8fc470` exception

Relation: nearby source page; matched terms `all`, `explains`, `how`, `using`

Citation: (raw/javascriptallonge.pdf p.291-292)

Richard Feynman’s QED[105] was another inspiration: A book that explains Quantum Electrodynamics and the “Sum of the Histories” methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening–such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane–are all wrong.

### From [[javascriptallonge-interactive-generators]]: `technical-atom-f2826d58755cc716` code

Relation: nearby source page; matched terms `code`, `like`, `need`

Citation: (raw/javascriptallonge.pdf p.273-283)

```javascript
Our statelessNaughtsAndCrosses function pushes the work of tracking the game’s state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our “API” will work like this: When we want a new game, we’ll call a function that will return a game function, We’ll call the game function repeatedly, passing our moves, and get the opponent’s moves from it.
```

### From [[javascriptallonge-a-pull-of-the-lever-prefaces]]: `technical-atom-3710a2880f9758fc` requirement

Relation: nearby source page; matched terms `method`, `result`, `use`

Citation: (raw/javascriptallonge.pdf p.6)

“The important thing is that neither method of preparation should use so much water as to result in a sickly, pale ghost of Espresso.
