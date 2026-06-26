---
page_id: javascriptallonge-combinators-and-function-decorators
page_kind: source
summary: Combinators and Function Decorators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.68-70
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses combinators and function decorators in JavaScript, focusing on higher-order functions that take functions as arguments or return functions.

## Key supported claims

- Combinators are higher-order functions that take functions as arguments and return functions (raw/javascriptallonge.pdf p.68-70).
- The compose combinator combines two functions (raw/javascriptallonge.pdf p.68-70).
- Function decorators modify function behavior (raw/javascriptallonge.pdf p.68-70).
- Combinators use only function application and previously defined combinators (raw/javascriptallonge.pdf p.68-70).

## Technical details

### `technical-atom-4ec0e2f5cfc99090` code

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.
```

### `technical-atom-569779904b729c3c` code

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
const repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)): undefined repeat(3, function (n) { console.log(`Hello ${ n } `) }) //=> 'Hello 1' 'Hello 2' 'Hello 3' undefined
```

### `technical-atom-19cee075a1ed9852` code

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
const addOne = (number) => number + 1;
```

### `technical-atom-5fe0f122259530d3` code

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
const doubleOf = (number) => number * 2;
```

### `technical-atom-0cc66a37a049c37c` code

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
const doubleOfAddOne = (number) => doubleOf(addOne(number));
```

### `technical-atom-8eaf429f1d02d168` code

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
const doubleOfAddOne = compose(doubleOf, addOne);
```

### `technical-atom-e99637951e8b3ce4` code

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
const not = (fn) => (x) => !fn(x)
```

### `technical-atom-a8a73b1ffdea31e3` formula

Citation: (raw/javascriptallonge.pdf p.68-70)

> 36http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20

## Related technical details

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-6ef9e0d67016949b` code

Relation: nearby source page; matched terms `function`, `functions`, `only`, `two`

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => ....
```

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please]]: `technical-atom-059258f79c64cecb` code

Relation: nearby source page; matched terms `function`, `functions`, `return`, `use`

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
This loose definition is recursive, so we can intuit (or use our experience with other languages) that since a function can contain a return statement with an expression, we can write a function that returns a function, or an array that contains another array expression. Or a function that returns an array, an array of functions, a function that returns an array of functions, and so forth:
```

### From [[javascriptallonge-naming-functions]]: `technical-atom-e6e76a5e6be15c59` code

Relation: nearby source page; matched terms `function`, `functions`, `return`, `use`

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
5. We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword
```

### From [[javascriptallonge-naming-functions]]: `technical-atom-5a7c2c2feec03b0b` code

Relation: nearby source page; matched terms `function`, `functions`, `return`

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
function (str) { return str + str }
```
