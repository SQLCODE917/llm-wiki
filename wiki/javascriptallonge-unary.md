---
page_id: javascriptallonge-unary
page_kind: source
summary: Unary from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.82-83
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on unary functions and decorators in JavaScript Allongé, covering the concept of unary function decorators and their use case with Array.map.

## Key supported claims

- Unary is a function decorator that modifies the number of arguments a function takes, turning it into a function taking exactly one argument (raw/javascriptallonge.pdf p.82-83).
- The most common use case for unary is to fix problems with JavaScript's .map method, which calls functions with three arguments instead of one (raw/javascriptallonge.pdf p.82-83).
- The unary decorator can convert functions like parseInt, which take optional arguments, to take only one argument for use with map (raw/javascriptallonge.pdf p.82-83).

## Technical details

### `technical-atom-8daef56ebba255d1` code

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
[1, 2, 3].map( function (element, index, arr) { console.log({element: element, index: index, arr: arr}) }) //=> { element: 1, index: 0, arr: [ 1, 2, 3] } // { element: 2, index: 1, arr: [ 1, 2, 3] } // { element: 3, index: 2, arr: [ 1, 2, 3] }
```

### `technical-atom-01bc81e68a1b6bd9` code

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
const unary = (fn) =>
```

### `technical-atom-ec926fbbeb68e94d` code

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
? fn: function (something) { return fn.call( this, something) }
```

### `technical-atom-1be1f5c9da1bd1c2` code

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
fn: function (something) { return fn.call( this, something) }
```

### `technical-atom-2fb846e09e5cacfd` procedure

Citation: (raw/javascriptallonge.pdf p.82-83)

“Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

### `technical-atom-369044853fe1be31` exception

Citation: (raw/javascriptallonge.pdf p.82-83)

If you pass in a function taking only one argument, it simply ignores the additional arguments.

### `technical-atom-7e9f2eb7cb12d3b5` exception

Citation: (raw/javascriptallonge.pdf p.82-83)

What we want is to convert parseInt into a function taking only one argument.

### `technical-atom-da0b0aabac601340` worked-example

Citation: (raw/javascriptallonge.pdf p.82-83)

In that example, it looks exactly like the mapping function you’ll find in most languages: You pass it a function, and it calls the function with one argument, the element of the array.

## Related technical details

### From [[javascriptallonge-partial-application]]: `technical-atom-a4e2222067936b67` procedure

Relation: nearby source page; matched terms `argument`, `can`, `one`, `procedure`, `take`, `use`

Citation: (raw/javascriptallonge.pdf p.80-81)

We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

### From [[javascriptallonge-combinators-and-function-decorators]]: `technical-atom-4ec0e2f5cfc99090` code

Relation: nearby source page; matched terms `arguments`, `can`, `decorators`, `function`, `functions`, `javascript`

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.
```

### From [[javascriptallonge-building-blocks]]: `technical-atom-cc7f0e20542b4dff` code

Relation: nearby source page; matched terms `argument`, `function`, `map`

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:
```

### From [[javascriptallonge-tap]]: `technical-atom-2c8eaeb0663fecee` requirement

Relation: nearby source page; matched terms `function`, `takes`

Citation: (raw/javascriptallonge.pdf p.84-85)

It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects.
