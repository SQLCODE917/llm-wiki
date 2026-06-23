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

### `technical-atom-a2d71108f315692a` worked-example

Citation: (raw/javascriptallonge.pdf p.82-83)

In that example, it looks exactly like the mapping function you'll find in most languages: You pass it a function, and it calls the function with one argument, the element of the array.

### `technical-atom-9a3ea54bbd8bfbe0` exception

Citation: (raw/javascriptallonge.pdf p.82-83)

If you pass in a function taking only one argument, it simply ignores the additional arguments.
