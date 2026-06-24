---
page_id: javascriptallonge-magic-names-and-fat-arrows
page_kind: source
summary: magic names and fat arrows from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.75-77
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé – A modular guide to JavaScript fundamentals and advanced techniques.

## Key supported claims

- The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding. (raw/javascriptallonge.pdf p.75-77)
- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. (raw/javascriptallonge.pdf p.75-77)
- 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: (raw/javascriptallonge.pdf p.75-77)
- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. (raw/javascriptallonge.pdf p.75-77)
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. (raw/javascriptallonge.pdf p.75-77)

## Technical details

### `technical-atom-fa080dbd9241b746` code

Citation: (raw/javascriptallonge.pdf p.75-77)

```javascript
( function () { return ( function () { return arguments[0]; })('inner'); })('outer') //=> "inner"
```

### `technical-atom-d7978015c6cde9aa` code

Citation: (raw/javascriptallonge.pdf p.75-77)

```javascript
( function () { return (() => arguments[0])('inner'); })('outer') //=> "outer"
```

### `technical-atom-d6de82851c455de8` code

Citation: (raw/javascriptallonge.pdf p.75-77)

```javascript
const row = function () { return mapWith( (column) => column * arguments[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [3,6,9,12,15,18,21,24,27,30,33,36]
```

### `technical-atom-75b3d22c3da35056` code

Citation: (raw/javascriptallonge.pdf p.75-77)

```javascript
const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

### `technical-atom-d8ec84799d7fc331` requirement

Citation: (raw/javascriptallonge.pdf p.75-77)

The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding.

### `technical-atom-af507181bbc4076e` worked-example

Citation: (raw/javascriptallonge.pdf p.75-77)

For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" :

### `technical-atom-edd8469edf0e78dd` worked-example

Citation: (raw/javascriptallonge.pdf p.75-77)

Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax.

### `technical-atom-32a6dfcc19fe05d0` worked-example

Citation: (raw/javascriptallonge.pdf p.75-77)

To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table.

## Related technical details

### From [[javascriptallonge-unary]]: `technical-atom-a2d71108f315692a` worked-example

Relation: nearby source page; matched terms `function`, `like`, `mapping`, `worked-example`, `you`

Citation: (raw/javascriptallonge.pdf p.82-83)

In that example, it looks exactly like the mapping function you'll find in most languages: You pass it a function, and it calls the function with one argument, the element of the array.

### From [[javascriptallonge-tap]]: `technical-atom-29b21e75a59e70f6` requirement

Relation: nearby source page; matched terms `always`, `function`, `you`

Citation: (raw/javascriptallonge.pdf p.84-85)

It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects.

### From [[javascriptallonge-partial-application]]: `technical-atom-6fce045843894525` code

Relation: nearby source page; matched terms `function`, `name`, `you`

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const callFirst = (fn, larg) => function (...rest) { return fn.call( this , larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call( this , ...rest, rarg); } const greet = (me, you) => `Hello, ${ you } , my name is ${ me } `; const heliosSaysHello = callFirst(greet, 'Helios'); heliosSaysHello('Eartha') //=> 'Hello, Eartha, my name is Helios' const sayHelloToCeline = callLast(greet, 'Celine'); sayHelloToCeline('Eartha') //=> 'Hello, Celine, my name is Eartha'
```

### From [[javascriptallonge-unary]]: `technical-atom-898e42c84ba44bb3` procedure

Relation: nearby source page; matched terms `any`, `arguments`, `function`

Citation: (raw/javascriptallonge.pdf p.82-83)

'Unary' is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.
