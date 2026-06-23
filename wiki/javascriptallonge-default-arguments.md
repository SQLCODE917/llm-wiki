---
page_id: javascriptallonge-default-arguments
page_kind: source
summary: default arguments from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.123-124
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Default arguments in JavaScript, including tail-recursive function examples and syntax.

## Key supported claims

- JavaScript provides default argument syntax, which allows specifying a default value for function parameters. (raw/javascriptallonge.pdf p.123-124)
- Default arguments are concise and readable. (raw/javascriptallonge.pdf p.123-124)
- Using default arguments avoids the need to always provide all parameters, improving usability for tail-recursive functions. (raw/javascriptallonge.pdf p.123-124)

## Technical details

### `technical-atom-f2ed8fe527bc0e91` code

Citation: (raw/javascriptallonge.pdf p.123-124)

```javascript
const factorial = (n, work) => n === 1 ? work : factorial(n - 1, n * work); factorial(1, 1) //=> 1 factorial(5, 1) //=> 120
```

### `technical-atom-0182e3897129027a` code

Citation: (raw/javascriptallonge.pdf p.123-124)

```javascript
const factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) //=> 1 factorial(6) //=> 720
```

### `technical-atom-2d53c10c10907cc0` code

Citation: (raw/javascriptallonge.pdf p.123-124)

```javascript
const length = ([first, ...rest], numberToBeAdded = 0) => first === undefined ? numberToBeAdded : length(rest, 1 + numberToBeAdded) length(["foo", "bar", "baz"]) //=> 3 const mapWith = (fn, [first, ...rest], prepend = []) => first === undefined ? prepend : mapWith(fn, rest, [...prepend, fn(first)]); mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### `technical-atom-b90d9e1958a2a2f0` requirement

Citation: (raw/javascriptallonge.pdf p.123-124)

But it is hideous to have to always add a 1 parameter, we'd be demanding that everyone using the factorial function know that we are using a tail-recursive implementation.

### `technical-atom-fbc8e2fa2b6e56d8` code

Citation: (raw/javascriptallonge.pdf p.123-124)

```
numberToBeAdded : length(rest, 1 + numberToBeAdded) length(["foo", "bar", "baz"]) //=> 3 const mapWith = (fn, [first, ...rest], prepend = []) => first === undefined ?
```
