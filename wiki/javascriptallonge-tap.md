---
page_id: javascriptallonge-tap
page_kind: source
summary: Tap from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.84-85
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

The tap combinator is a basic function that takes a value and returns a function. It is used for side-effects while preserving the value.

## Key supported claims

- The tap combinator is a basic function that takes a value and returns a function, used for side-effects while preserving the value (raw/javascriptallonge.pdf p.84-85).
- Tap can be used as a debugging aid, executing a function for side-effects while keeping the value around (raw/javascriptallonge.pdf p.84-85).
- Tap can be implemented to work both curried and uncurried, supporting different usage patterns (raw/javascriptallonge.pdf p.84-85).

## Technical details

### `technical-atom-246c88f3c9f74eab` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
const K = (x) => (y) => x;
```

### `technical-atom-fede72e9d642662d` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
const tap = (value) => (fn) => ( typeof (fn) === 'function' && fn(value), value)
```

### `technical-atom-1fb07c1da09c6445` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
tap('espresso')((it) => { console.log(`Our drink is ' ${ it } '`) }); //=> Our drink is 'espresso' 'espresso'
```

### `technical-atom-ae39c1b87e12dec4` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
tap('espresso')(); //=> 'espresso'
```

### `technical-atom-114027cf81d5daae` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
.tap('espresso', (it) => console.log(`Our drink is ' ${ it } '`)); //=> Our drink is 'espresso'_ 'espresso'
```

### `technical-atom-e82edd8fc9d318e3` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
const tap = (value, fn) => { const curried = (fn) => ( typeof (fn) === 'function' && fn(value), value); return fn === undefined ? curried: curried(fn); }
```

### `technical-atom-92db73aed55a8d05` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
tap('espresso', (it) => { console.log(`Our drink is ' ${ it } '`) }); //=> Our drink is 'espresso' 'espresso' And if we wish it to do nothing at all, We can write either tap('espresso')() or tap('espresso', null)
```

### `technical-atom-2c8eaeb0663fecee` requirement

Citation: (raw/javascriptallonge.pdf p.84-85)

It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects.

## Related technical details

### From [[javascriptallonge-partial-application]]: `technical-atom-a4e2222067936b67` procedure

Relation: nearby source page; matched terms `can`, `more`, `than`

Citation: (raw/javascriptallonge.pdf p.80-81)

We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

### From [[javascriptallonge-maybe]]: `technical-atom-937bc370ec3a1ac2` code

Relation: nearby source page; matched terms `function`, `value`

Citation: (raw/javascriptallonge.pdf p.86-87)

```javascript
Model.prototype.setSomething = maybe( function (value) { this .something = value; });
```

### From [[javascriptallonge-unary]]: `technical-atom-2fb846e09e5cacfd` procedure

Relation: nearby source page; matched terms `function`, `takes`

Citation: (raw/javascriptallonge.pdf p.82-83)

“Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.
