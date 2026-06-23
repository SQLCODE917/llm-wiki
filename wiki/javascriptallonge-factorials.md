---
page_id: javascriptallonge-factorials
page_kind: source
summary: factorials from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.121-123
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses the calculation of factorials in JavaScript, focusing on recursive and tail-recursive approaches.

## Key supported claims

- The naïve function for calcuating the factorial of a positive integer follows directly from the definition: const factorial = (n) => n == 1 ? n : n * factorial(n - 1); (raw/javascriptallonge.pdf p.121-123)
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1). (raw/javascriptallonge.pdf p.121-123)
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. (raw/javascriptallonge.pdf p.121-123)

## Technical details

### `technical-atom-074e17d2524ec651` code

Citation: (raw/javascriptallonge.pdf p.121-123)

```
5! = 5 x 4 x 3 x 2 x 1 = 120.
```

### `technical-atom-e6354925d283c367` code

Citation: (raw/javascriptallonge.pdf p.121-123)

```javascript
const factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) //=> 1 factorial(5) //=> 120
```

### `technical-atom-b124f323580a3a6b` code

Citation: (raw/javascriptallonge.pdf p.121-123)

```javascript
const factorialWithDelayedWork = (n, work) => n === 1 ? work : factorialWithDelayedWork(n - 1, n * work); const factorial = (n) => factorialWithDelayedWork(n, 1);
```

### `technical-atom-66eafe6e25ff4c7e` code

Citation: (raw/javascriptallonge.pdf p.121-123)

```javascript
const callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const factorial = callLast(factorialWithDelayedWork, 1); factorial(1) //=> 1 factorial(5) //=> 120
```

### `technical-atom-6d9212df7fc2c4c0` procedure

Citation: (raw/javascriptallonge.pdf p.121-123)

Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.
