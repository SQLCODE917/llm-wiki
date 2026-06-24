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

### `technical-atom-fbc8e2fa2b6e56d8` code

Citation: (raw/javascriptallonge.pdf p.123-124)

```
numberToBeAdded : length(rest, 1 + numberToBeAdded) length(["foo", "bar", "baz"]) //=> 3 const mapWith = (fn, [first, ...rest], prepend = []) => first === undefined ?
```

### `technical-atom-b90d9e1958a2a2f0` requirement

Citation: (raw/javascriptallonge.pdf p.123-124)

But it is hideous to have to always add a 1 parameter, we'd be demanding that everyone using the factorial function know that we are using a tail-recursive implementation.

## Related technical details

### From [[javascriptallonge-factorials]]: `technical-atom-6d9212df7fc2c4c0` procedure

Relation: nearby source page; matched terms `argument`, `function`, `value`

Citation: (raw/javascriptallonge.pdf p.121-123)

Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-39097d4eaba37f6d` procedure

Relation: nearby source page; matched terms `arguments`, `default`, `javascript`, `which`

Citation: (raw/javascriptallonge.pdf p.117-118)

Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) .

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-2072bdc8f0d30ba8` requirement

Relation: nearby source page; matched terms `arguments`, `default`, `javascript`, `value`

Citation: (raw/javascriptallonge.pdf p.117-118)

Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result.

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-14898c90c9499167` code

Relation: nearby source page; matched terms `arguments`, `default`, `function`

Citation: (raw/javascriptallonge.pdf p.117-118)

```javascript
const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```
