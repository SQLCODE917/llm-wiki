---
page_id: javascriptallonge-functional-iterators
page_kind: source
summary: Functional Iterators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.167-176
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter introduces functional iterators, demonstrating how to separate traversal from operations using folding and iteration, and explores lazy evaluation and iterator composition.

## Key supported claims

- Folding separates traversal from operations, using functions to traverse data (raw/javascriptallonge.pdf p.167-176).
- Iterators use while loops to traverse data structures (raw/javascriptallonge.pdf p.167-176).
- Iterator functions return values and done status (raw/javascriptallonge.pdf p.167-176).
- Mapping and filtering compose iterator operations (raw/javascriptallonge.pdf p.167-176).
- Iterators can generate sequences like numbers and Fibonacci (raw/javascriptallonge.pdf p.167-176).

## Technical details

### `technical-atom-55a3b25b6d53e5c4` code

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator: arraySum(rest, first + accumulator)
```

### `technical-atom-445b82ae95bfc8a6` code

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
const callLeft = (fn, ...args) => (...remainingArgs) => fn(...args, ...remainingArgs); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue: fn(first, foldArrayWith(fn, terminalValue, rest));
```

### `technical-atom-90beddf380ece81e` code

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0); arraySum([1, 4, 9, 16, 25]) //=> 55
```

### `technical-atom-0a1cd9a8e7a80d48` code

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
```

### `technical-atom-c934adcf157b84bb` code

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue: fn(first, foldArrayWith(fn, terminalValue, rest));
```

### `technical-atom-9f3302597c2bd11c` code

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
const foldArray = (array) => callRight(foldArrayWith, array);
```

### `technical-atom-85b01b680d34d967` code

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
```

### `technical-atom-9b454b81a7c87331` code

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
What we’ve done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array);. The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable.
```

## Related technical details

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-cd36d849b171aa54` code

Relation: nearby source page; matched terms `data`, `function`, `functions`, `identity`, `one`, `take`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42. Very simple, but useful. Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-aea76708de48efca` code

Relation: nearby source page; matched terms `data`, `function`, `functions`, `returns`, `thing`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K, is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value.
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-5c8bfdbaaac4c2b2` code

Relation: nearby source page; matched terms `data`, `functions`, `one`, `thing`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.
```

### From [[javascriptallonge-mapwith]]: `technical-atom-49f118af13215ae0` code

Relation: nearby source page; matched terms `can`, `function`, `mapping`, `return`

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map:
```
