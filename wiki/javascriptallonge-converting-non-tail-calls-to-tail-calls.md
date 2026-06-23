---
page_id: javascriptallonge-converting-non-tail-calls-to-tail-calls
page_kind: source
summary: converting non-tail-calls to tail-calls from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.120-121
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section is from JavaScript Allongé, focusing on transforming recursive functions to use tail calls for better performance.

## Key supported claims

- The obvious solution is to push computation into the recursive call, making it a tail call. (raw/javascriptallonge.pdf p.120-121)
- This transformation allows handling large arrays without memory overhead. (raw/javascriptallonge.pdf p.120-121)
- Technique applies to functions like lengthDelaysWork and mapWithDelaysWork. (raw/javascriptallonge.pdf p.120-121)
- JavaScript optimizes tail calls not to take up memory proportional to input length. (raw/javascriptallonge.pdf p.120-121)

## Technical details

### `technical-atom-1dc65b7c327c82d3` code

Citation: (raw/javascriptallonge.pdf p.120-121)

```javascript
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysWork(["foo", "bar", "baz"], 0) //=> 3
```

### `technical-atom-6413578d990f26d4` code

Citation: (raw/javascriptallonge.pdf p.120-121)

```javascript
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) const length = (n) => lengthDelaysWork(n, 0);
```

### `technical-atom-5080818b4c497075` code

Citation: (raw/javascriptallonge.pdf p.120-121)

```javascript
Or we could use partial application: const callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const length = callLast(lengthDelaysWork, 0); length(["foo", "bar", "baz"]) //=> 3
```

### `technical-atom-8cb648f5e6238d12` code

Citation: (raw/javascriptallonge.pdf p.120-121)

```javascript
const mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === undefined ? prepend : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); const mapWith = callLast(mapWithDelaysWork, []); mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25] We can use it with ridiculously large arrays:
```

### `technical-atom-e9baa91a5eaa5b28` code

Citation: (raw/javascriptallonge.pdf p.120-121)

```javascript
mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, // ... 2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ]) //=> [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196, ...
```

### `technical-atom-e3f41d95f21c1456` exception

Citation: (raw/javascriptallonge.pdf p.120-121)

We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls.

### `technical-atom-0cbba5b5d2e15ff8` exception

Citation: (raw/javascriptallonge.pdf p.120-121)

And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.
