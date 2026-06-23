---
page_id: javascriptallonge-function-declarations
page_kind: source
summary: function declarations from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.65-66
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Function declarations are a syntax for naming and/or defining a function in JavaScript, with specific behaviors like hoisting.

## Key supported claims

- First, function declarations are hoisted to the top of the function in which they occur (raw/javascriptallonge.pdf p.65-66).
- There is another syntax for naming and/or defining a function (raw/javascriptallonge.pdf p.65-66).
- Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const : (raw/javascriptallonge.pdf p.65-66).
- It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code (raw/javascriptallonge.pdf p.65-66).
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error (raw/javascriptallonge.pdf p.65-66).

## Technical details

### `technical-atom-310fe4d8bbcf0361` code

Citation: (raw/javascriptallonge.pdf p.65-66)

```javascript
function someName () { // ... } This behaves a little like: const someName = function someName () // ... }
```

### `technical-atom-3a136658747d88f1` code

Citation: (raw/javascriptallonge.pdf p.65-66)

```
{
```

### `technical-atom-f1f1d87b3f0d9fe4` code

Citation: (raw/javascriptallonge.pdf p.65-66)

```javascript
( function () { return fizzbuzz(); const fizzbuzz = function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> undefined is not a function (evaluating 'fizzbuzz()')
```

### `technical-atom-f07b324de3d238c3` code

Citation: (raw/javascriptallonge.pdf p.65-66)

```javascript
( function () { return fizzbuzz(); function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> 'FizzBuzz' Although fizzbuzz is declared later in the function, JavaScript behaves as if we'd written: ( function () { {
```

### `technical-atom-cd64891a81b132ff` code

Citation: (raw/javascriptallonge.pdf p.65-66)

```javascript
const fizzbuzz = function fizzbuzz () return "Fizz" + "Buzz"; } return fizzbuzz(); })()
```

### `technical-atom-824639bdc70ea377` exception

Citation: (raw/javascriptallonge.pdf p.65-66)

It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement:

### `technical-atom-298fe34c71a743c1` formula

Citation: (raw/javascriptallonge.pdf p.65-66)

} This behaves a little like: const someName = function someName () // ...

### `technical-atom-ce3f07fc430dd604` procedure

Citation: (raw/javascriptallonge.pdf p.65-66)

First, function declarations are hoisted to the top of the function in which they occur.
