---
page_id: javascriptallonge-tap
page_kind: source
summary: Tap from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.84-85
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Tap is a traditional name borrowed from various Unix shell commands. It can do more than just act as a debugging aid.

## Key supported claims

- tap is a traditional name borrowed from Unix shell commands (raw/javascriptallonge.pdf p.84-85)
- tap can do more than just act as a debugging aid (raw/javascriptallonge.pdf p.84-85)
- tap executes a function for side-effects and then returns the original value (raw/javascriptallonge.pdf p.84-85)
- tap works with both curried and uncurried function styles (raw/javascriptallonge.pdf p.84-85)
- tap is useful for working with object and instance methods (raw/javascriptallonge.pdf p.84-85)

## Technical details

### `technical-atom-2a090e7bb7640613` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
const K = (x) => (y) => x;
```

### `technical-atom-4dd35e6cf210b9bd` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
const tap = (value) => (fn) => ( typeof (fn) === 'function' && fn(value), value )
```

### `technical-atom-c8fa273077e85aaf` code

Citation: (raw/javascriptallonge.pdf p.84-85)

```javascript
const tap = (value, fn) => { const curried = (fn) => ( typeof (fn) === 'function' && fn(value), value ); return fn === undefined ? curried : curried(fn); } Now we can write: tap('espresso')((it) => { console.log(`Our drink is ' ${ it } '`) }); //=> Our drink is 'espresso' 'espresso' Or: tap('espresso', (it) => { console.log(`Our drink is ' ${ it } '`) }); //=> Our drink is 'espresso' 'espresso'
```

### `technical-atom-d826f90f6b4a4330` procedure

Citation: (raw/javascriptallonge.pdf p.84-85)

tap('espresso')((it) => { console.log(`Our drink is ' ${ it } '`) }); //=> Our drink is 'espresso' 'espresso' It's easy to turn off: tap('espresso')(); //=> 'espresso' Libraries like Underscore 49 use a version of tap that is 'uncurried:' _.tap('espresso', (it) => console.log(`Our drink is ' ${ it } '`) ); //=> Our drink is 'espresso' 'espresso'

### `technical-atom-29b21e75a59e70f6` requirement

Citation: (raw/javascriptallonge.pdf p.84-85)

It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects.
