---
page_id: javascriptallonge-higher-order-functions
page_kind: source
summary: higher-order functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.68-68
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé discusses higher-order functions, which are functions that take functions as arguments, return functions, or both.

## Key supported claims

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. (raw/javascriptallonge.pdf p.68-68)
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. (raw/javascriptallonge.pdf p.68-68)
- Higher-order functions dominate JavaScript Allongé. (raw/javascriptallonge.pdf p.68-68)
- But before we go on, we'll talk about some specific types of higher-order functions. (raw/javascriptallonge.pdf p.68-68)

## Technical details

### `technical-atom-4156650bc7d6a27a` code

Citation: (raw/javascriptallonge.pdf p.68)

```javascript
const repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)) : undefined repeat(3, function (n) { console.log(`Hello ${ n } `) }) //=> 'Hello 1' 'Hello 2' 'Hello 3' undefined
```

## Related technical details

### From [[javascriptallonge-combinators]]: `technical-atom-0c6ee2e3b1a2e9c0` exception

Relation: nearby source page; matched terms `arguments`, `function`, `functions`, `higher-order`, `return`, `take`

Citation: (raw/javascriptallonge.pdf p.68-69)

In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function.

### From [[javascriptallonge-combinators]]: `technical-atom-573c28eb9a1b4a43` exception

Relation: nearby source page; matched terms `arguments`, `function`, `higher-order`

Citation: (raw/javascriptallonge.pdf p.68-69)

'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35

### From [[javascriptallonge-function-declaration-caveats-34]]: `technical-atom-4140475af23ddd75` code

Relation: nearby source page; matched terms `can`, `function`, `return`

Citation: (raw/javascriptallonge.pdf p.66-67)

```javascript
( function (camelCase) { return fizzbuzz(); if (camelCase) { function fizzbuzz () { return "Fizz" + "Buzz"; } } else { function fizzbuzz () { return "Fizz" + "Buzz"; } } })( true ) //=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?
```

### From [[javascriptallonge-function-declaration-caveats-34]]: `technical-atom-68210eea018a360c` code

Relation: nearby source page; matched terms `but`, `function`, `return`

Citation: (raw/javascriptallonge.pdf p.66-67)

```javascript
function trueDat () { return true } But this is not: ( function trueDat () { return true })
```
