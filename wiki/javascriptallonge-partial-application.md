---
page_id: javascriptallonge-partial-application
page_kind: source
summary: Partial Application from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.80-81
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers partial application, a fundamental concept in functional programming, and demonstrates its application with practical examples using the Underscore library and custom implementations.

## Key supported claims

- This is such a common tool that many libraries provide some form of partial application (raw/javascriptallonge.pdf p.80-81).
- As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware (raw/javascriptallonge.pdf p.80-81).
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument (raw/javascriptallonge.pdf p.80-81).
- If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments (raw/javascriptallonge.pdf p.80-81).
- In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it (raw/javascriptallonge.pdf p.80-81).

## Technical details

### `technical-atom-bdb0c986ad531c92` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
_.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9]
```

### `technical-atom-efcab5389b61119e` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const squareAll = (array) => map(array, (n) => n * n);
```

### `technical-atom-f804d3132fbf4fc5` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9]
```

### `technical-atom-68c7a1439fb776e2` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### `technical-atom-09f1b07ce4c1f3b2` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
safeSquareAll([1, null , 2, 3]) //=> [1, null, 4, 9]
```

### `technical-atom-6fce045843894525` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const callFirst = (fn, larg) => function (...rest) { return fn.call( this , larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call( this , ...rest, rarg); } const greet = (me, you) => `Hello, ${ you } , my name is ${ me } `; const heliosSaysHello = callFirst(greet, 'Helios'); heliosSaysHello('Eartha') //=> 'Hello, Eartha, my name is Helios' const sayHelloToCeline = callLast(greet, 'Celine'); sayHelloToCeline('Eartha') //=> 'Hello, Celine, my name is Eartha'
```

### `technical-atom-85ddb1703e266644` code

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const callLeft = (fn, ...args) => (...remainingArgs) => fn(...args, ...remainingArgs); const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
```

### `technical-atom-c1e5e9bc1d645cbb` exception

Citation: (raw/javascriptallonge.pdf p.72-73)

But what if we only supply some of the arguments?

## Related technical details

### From [[javascriptallonge-unary]]: `technical-atom-9a3ea54bbd8bfbe0` exception

Relation: nearby source page; matched terms `argument`, `arguments`, `one`, `you`

Citation: (raw/javascriptallonge.pdf p.82-83)

If you pass in a function taking only one argument, it simply ignores the additional arguments.

### From [[javascriptallonge-unary]]: `technical-atom-898e42c84ba44bb3` procedure

Relation: nearby source page; matched terms `argument`, `arguments`, `one`

Citation: (raw/javascriptallonge.pdf p.82-83)

'Unary' is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

### From [[javascriptallonge-unary]]: `technical-atom-a2d71108f315692a` worked-example

Relation: nearby source page; matched terms `argument`, `one`, `you`

Citation: (raw/javascriptallonge.pdf p.82-83)

In that example, it looks exactly like the mapping function you'll find in most languages: You pass it a function, and it calls the function with one argument, the element of the array.

### From [[javascriptallonge-combinators]]: `technical-atom-0c6ee2e3b1a2e9c0` exception

Relation: nearby source page; matched terms `arguments`, `functions`, `take`, `using`, `will`

Citation: (raw/javascriptallonge.pdf p.68-69)

In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function.
