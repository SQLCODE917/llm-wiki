---
page_id: javascriptallonge-tail-calls-and-default-arguments
page_kind: source
summary: Tail Calls (and Default Arguments) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.117-118
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on tail calls and default arguments in JavaScript Allong’e.

## Key supported claims

- JavaScript retains values and housekeeping information on a call stack during recursion, which is expensive (raw/javascriptallonge.pdf p.117-118).
- Doubling the length of an array doubles the stack space and work required for each call frame (raw/javascriptallonge.pdf p.117-118).
- Call stack information is saved and is quite expensive (raw/javascriptallonge.pdf p.117-118).

## Technical details

### `technical-atom-ef68d75b7e638c72` code

Citation: (raw/javascriptallonge.pdf p.117-118)

```javascript
const mapWith = (fn, [first, ...rest]) => first === undefined ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### `technical-atom-14898c90c9499167` code

Citation: (raw/javascriptallonge.pdf p.117-118)

```javascript
const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```

### `technical-atom-bcaa3437933aa54d` code

Citation: (raw/javascriptallonge.pdf p.117-118)

```javascript
mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99 ]) //=> ???
```

### `technical-atom-20e31d5cf1c3bd85` procedure

Citation: (raw/javascriptallonge.pdf p.117-118)

First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked.

### `technical-atom-1bdf58391d739d60` procedure

Citation: (raw/javascriptallonge.pdf p.117-118)

To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] .

### `technical-atom-39097d4eaba37f6d` procedure

Citation: (raw/javascriptallonge.pdf p.117-118)

Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) .

### `technical-atom-2072bdc8f0d30ba8` requirement

Citation: (raw/javascriptallonge.pdf p.117-118)

Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result.

### `technical-atom-7f9ad434c94a3fdb` exception

Citation: (raw/javascriptallonge.pdf p.117-118)

JavaScript cannot throw first away.

## Related technical details

### From [[javascriptallonge-folding]]: `technical-atom-f8baa94a1544e5b8` code

Relation: nearby source page; matched terms `array`, `length`

Citation: (raw/javascriptallonge.pdf p.114-116)

```javascript
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5
```

### From [[javascriptallonge-tail-call-optimization]]: `technical-atom-d64971ca777393ea` exception

Relation: nearby source page; matched terms `call`, `happens`, `length`, `tail`, `work`

Citation: (raw/javascriptallonge.pdf p.119)

The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call.

### From [[javascriptallonge-tail-call-optimization]]: `technical-atom-d96c8d42a851c268` code

Relation: nearby source page; matched terms `call`, `function`, `length`, `tail`

Citation: (raw/javascriptallonge.pdf p.119)

```javascript
const maybe = (fn) => function (...args) { if (args.length === 0) { return ; } else { for ( let arg of args) { if (arg == null ) return ; } return fn.apply( this , args); } }
```

### From [[javascriptallonge-tail-call-optimization]]: `technical-atom-7f8f26fdd9419454` exception

Relation: nearby source page; matched terms `call`, `frame`, `stack`, `tail`

Citation: (raw/javascriptallonge.pdf p.119)

And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call.
