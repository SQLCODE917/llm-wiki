---
page_id: javascriptallonge-unary
page_kind: source
summary: Unary from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.82-83
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

'Unary' is a function decorator that modifies the number of arguments a function takes.

## Key supported claims

- Unary modifies the number of arguments a function takes, converting any function into one that accepts exactly one argument (raw/javascriptallonge.pdf p.82-83).
- Unary fixes issues with JavaScript's map method when using functions like parseInt that have optional arguments (raw/javascriptallonge.pdf p.82-83).
- Unary is implemented as a function decorator that checks function length and wraps functions taking more than one argument (raw/javascriptallonge.pdf p.82-83).

## Technical details

### `technical-atom-d2fd11856095016c` code

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
['1', '2', '3'].map(parseFloat) //=> [1, 2, 3]
```

### `technical-atom-e608877a91e748ad` code

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
[1, 2, 3].map( function (element, index, arr) { console.log({element: element, index: index, arr: arr}) }) //=> { element: 1, index: 0, arr: [ 1, 2, 3 ] } // { element: 2, index: 1, arr: [ 1, 2, 3 ] } // { element: 3, index: 2, arr: [ 1, 2, 3 ] }
```

### `technical-atom-18542209ec3d17d3` code

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
['1', '2', '3'].map(parseInt) //=> [1, NaN, NaN]
```

### `technical-atom-6630b376b8107ac2` code

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
const unary = (fn) => fn.length === 1 ? fn : function (something) { return fn.call( this , something) }
```

### `technical-atom-509eeaf46e48d60d` code

Citation: (raw/javascriptallonge.pdf p.82-83)

```javascript
['1', '2', '3'].map(unary(parseInt)) //=> [1, 2, 3]
```

### `technical-atom-898e42c84ba44bb3` procedure

Citation: (raw/javascriptallonge.pdf p.82-83)

'Unary' is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

### `technical-atom-9a3ea54bbd8bfbe0` exception

Citation: (raw/javascriptallonge.pdf p.82-83)

If you pass in a function taking only one argument, it simply ignores the additional arguments.

### `technical-atom-a2d71108f315692a` worked-example

Citation: (raw/javascriptallonge.pdf p.82-83)

In that example, it looks exactly like the mapping function you'll find in most languages: You pass it a function, and it calls the function with one argument, the element of the array.

## Related technical details

### From [[javascriptallonge-tap]]: `technical-atom-29b21e75a59e70f6` requirement

Relation: nearby source page; matched terms `function`, `pass`, `takes`, `you`

Citation: (raw/javascriptallonge.pdf p.84-85)

It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects.

### From [[javascriptallonge-magic-names-and-fat-arrows]]: `technical-atom-32a6dfcc19fe05d0` worked-example

Relation: nearby source page; matched terms `example`, `function`, `number`, `takes`, `worked-example`

Citation: (raw/javascriptallonge.pdf p.75-77)

To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table.

### From [[javascriptallonge-magic-names-and-fat-arrows]]: `technical-atom-d8ec84799d7fc331` requirement

Relation: nearby source page; matched terms `any`, `arguments`, `function`, `have`, `like`, `when`

Citation: (raw/javascriptallonge.pdf p.75-77)

The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding.

### From [[javascriptallonge-magic-names-and-fat-arrows]]: `technical-atom-af507181bbc4076e` worked-example

Relation: nearby source page; matched terms `argument`, `arguments`, `example`, `function`, `when`, `worked-example`

Citation: (raw/javascriptallonge.pdf p.75-77)

For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" :
