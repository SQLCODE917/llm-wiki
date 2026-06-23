---
page_id: javascriptallonge-overcoming-limitations
page_kind: source
summary: overcoming limitations from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.91-92
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on overcoming limitations in JavaScript, including left-variadic functions and the leftVariadic decorator.

## Key supported claims

- Left-variadic functions have one or more fixed arguments, with the rest gathered into the leftmost argument, which JavaScript does not support directly (raw/javascriptallonge.pdf p.91-92).
- The leftVariadic function is a decorator that turns functions into left-variadic ones, gathering parameters from the left instead of the right (raw/javascriptallonge.pdf p.91-92).
- A left-variadic function cannot be written directly in JavaScript; a decorator is needed to achieve this behavior (raw/javascriptallonge.pdf p.91-92).

## Technical details

### `technical-atom-32b73cea66ff6f87` code

Citation: (raw/javascriptallonge.pdf p.91-92)

```javascript
const butLastAndLast = (...butLast, last) => [butLast, last];
```

### `technical-atom-43d819f29893dfbe` code

Citation: (raw/javascriptallonge.pdf p.91-92)

```javascript
const leftVariadic = (fn) => { if (fn.length < 1) { return fn; } else { return function (...args) { const gathered = args.slice(0, args.length - fn.length + 1), spread = args.slice(args.length - fn.length + 1); return fn.apply( this , [gathered].concat(spread)
```

### `technical-atom-efe78fb5e8dc355c` code

Citation: (raw/javascriptallonge.pdf p.91-92)

```javascript
); } } }; const butLastAndLast = leftVariadic((butLast, last) => [butLast, last]); butLastAndLast('why', 'hello', 'there', 'little', 'droid') //=> [["why","hello","there","little"],"droid"]
```

### `technical-atom-da5e8aae05dc73cc` procedure

Citation: (raw/javascriptallonge.pdf p.91-92)

But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function?

### `technical-atom-0cc478268532bafb` procedure

Citation: (raw/javascriptallonge.pdf p.91-92)

Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right.
