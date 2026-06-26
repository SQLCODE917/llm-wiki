---
page_id: javascriptallonge-left-variadic-functions
page_kind: source
summary: Left-Variadic Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.89-93
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on left-variadic functions in JavaScript Allongé, covering variadic functions, left-variadic functions, and destructuring.

## Key supported claims

- Left-variadic functions gather parameters from the left, not the right, in JavaScript (raw/javascriptallonge.pdf p.89-93).
- JavaScript variadic functions can be unary, binary, ternary, and so forth, but not variary; they must be variadic (raw/javascriptallonge.pdf p.89-93).
- The `leftVariadic` decorator turns functions into left-variadic functions, gathering parameters from the left (raw/javascriptallonge.pdf p.89-93).
- A `leftGather` utility function is used for left-gathering arrays, similar to how `leftVariadic` works for functions (raw/javascriptallonge.pdf p.89-93).
- The `leftVariadic` decorator was created to enable left-variadic functions, which JavaScript does not support natively (raw/javascriptallonge.pdf p.89-93).

## Technical details

### `technical-atom-b60e84f35acc69cb` code

Citation: (raw/javascriptallonge.pdf p.89-93)

```javascript
const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5]
```

### `technical-atom-0c23903402221b14` code

Citation: (raw/javascriptallonge.pdf p.89-93)

```javascript
function team(coach, captain, ...players) { console.log(` ${ captain } (captain)`); for ( let player of players) { console.log(player); } console.log(`squad coached by ${ coach } `); } team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen', 'Martín Montoya', 'Gerard Piqué') //=> Xavi Hernández (captain) Marc-André ter Stegen Martín Montoya Gerard Piqué squad coached by Luis Enrique
```

### `technical-atom-fc50dc9050a3b75b` code

Citation: (raw/javascriptallonge.pdf p.89-93)

```javascript
function team2(...players, captain, coach) { console.log(` ${ captain } (captain)`); for ( let player of players) { console.log(player); } console.log(`squad coached by ${ coach } `); } //=> Unexpected token
```

### `technical-atom-e62e08b696689236` code

Citation: (raw/javascriptallonge.pdf p.89-93)

```
var __slice = Array.prototype.slice;
```

### `technical-atom-a1826ad5eefcc067` code

Citation: (raw/javascriptallonge.pdf p.89-93)

```javascript
function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1): []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]): []); return fn.apply( this, args); } }; var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') //=> ["why",["hello","there","little","droid"]]
```

### `technical-atom-7bf49c7ff08aeb0d` code

Citation: (raw/javascriptallonge.pdf p.89-93)

```javascript
var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] });
```

### `technical-atom-51c8c4479fd9dc31` code

Citation: (raw/javascriptallonge.pdf p.89-93)

```javascript
const firstAndButFirst = (first, ...butFirst) => [first, butFirst];
```

### `technical-atom-8221fcef2200cbba` code

Citation: (raw/javascriptallonge.pdf p.89-93)

```javascript
const butLastAndLast = (...butLast, last) => [butLast, last];
```

## Related technical details

### From [[javascriptallonge-picking-the-bean-choice-and-truthiness]]: `technical-atom-bd8a5462e95eea45` code

Relation: nearby source page; matched terms `but`, `does`, `javascript`, `not`

Citation: (raw/javascriptallonge.pdf p.94-99)

```
But that’s not what happens. || and && have short-cut semantics . In this case, if n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). Likewise, if n === 1, JavaScript evaluates n !== 1 && even(n - 2) as false without ever evaluating even(n - 2).
```

### From [[javascriptallonge-self-similarity]]: `technical-atom-940ab647a8cf16dd` code

Relation: nearby source page; matched terms `arrays`, `but`, `does`, `not`, `our`

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
> 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0, but we are doing backflips to keep this within a very small and contrived playground.
```

### From [[javascriptallonge-picking-the-bean-choice-and-truthiness]]: `technical-atom-f1849007585d2d23` code

Relation: nearby source page; matched terms `does`, `javascript`, `not`

Citation: (raw/javascriptallonge.pdf p.94-99)

```
If n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). This is very important! Imagine that JavaScript evaluated both sides of the || operator before determining its value. n === 0 would be true. What about (n !== 1 && even(n - 2))? Well, it would evaluate even(n - 2), or even(-2)
```

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-b4bbdc6766be3fad` code

Relation: nearby source page; matched terms `but`, `can`, `first`, `function`, `javascript`, `return`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
There are three places it returns. The first two don’t return anything, they don’t matter. But the third is fn.apply(this, args). This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. It isn’t going to do any more work, so it can throw its existing stack frame away.
```
