---
page_id: javascriptallonge-partial-application
page_kind: source
summary: Partial Application from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.80-81
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on partial application in JavaScript Allongé, discussing recipes for partial application and examples using callFirst, callLast, callLeft, and callRight.

## Key supported claims

- Partial application is common in JavaScript libraries (raw/javascriptallonge.pdf p.80-81).
- You can apply arguments either leftmost or rightmost (raw/javascriptallonge.pdf p.80-81).
- Partial application uses building blocks for function composition (raw/javascriptallonge.pdf p.80-81).

## Technical details

### `technical-atom-a57295fce728475d` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const callFirst = (fn, larg) => function (...rest) { return fn.call( this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call( this, ...rest, rarg); } const greet = (me, you) => `Hello, ${ you }, my name is ${ me } `;
```

### `technical-atom-9466d549281cfb25` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const heliosSaysHello = callFirst(greet, 'Helios');
```

### `technical-atom-8749db9ee0a38511` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const sayHelloToCeline = callLast(greet, 'Celine');
```

### `technical-atom-067114683f5c7a85` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const callLeft = (fn, ...args) =>
```

### `technical-atom-855c7459bb9c0cfa` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
(...remainingArgs) => fn(...args, ...remainingArgs);
```

### `technical-atom-26c5d7f57e480c60` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
```

### `technical-atom-a4e2222067936b67` procedure

Citation: (raw/javascriptallonge.pdf p.80-81)

We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

### `technical-atom-652a1af087f00c04` worked-example

Citation: (raw/javascriptallonge.pdf p.80-81)

You’ll find examples in Lemonad[45] from Michael Fogus, Functional JavaScript[46] from Oliver Steele and the terse but handy node-ap[47] from James Halliday.

## Related technical details

### From [[javascriptallonge-building-blocks]]: `technical-atom-cc7f0e20542b4dff` code

Relation: nearby source page; matched terms `application`, `argument`, `blocks`, `building`, `function`, `partial`

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:
```

### From [[javascriptallonge-once]]: `technical-atom-c8a91a61773905e3` code

Relation: nearby source page; matched terms `apply`, `arguments`, `function`

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
const once = (fn) => { let done = false; return function () { return done ? void 0: ((done = true), fn.apply( this, arguments)) } }
```

### From [[javascriptallonge-combinators-and-function-decorators]]: `technical-atom-4ec0e2f5cfc99090` code

Relation: nearby source page; matched terms `arguments`, `can`, `either`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.
```

### From [[javascriptallonge-once]]: `technical-atom-d895d8e104807911` formula

Relation: nearby source page; matched terms `apply`, `arguments`

Citation: (raw/javascriptallonge.pdf p.88)

**void** 0 : ((done = **true** ), fn.apply( **this** , arguments)) } }
