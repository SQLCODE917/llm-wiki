---
page_id: javascriptallonge-function-declaration-caveats-34
page_kind: source
summary: function declaration caveats 34 from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.66-67
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea. Function declarations are not supposed to occur inside of blocks. Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression.

## Key supported claims

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. (raw/javascriptallonge.pdf p.66-67)
- Function declarations are not supposed to occur inside of blocks. (raw/javascriptallonge.pdf p.66-67)
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. (raw/javascriptallonge.pdf p.66-67)
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified. (raw/javascriptallonge.pdf p.66-67)
- The parentheses make this an expression, not a function declaration. (raw/javascriptallonge.pdf p.66-67)

## Technical details

### `technical-atom-4140475af23ddd75` code

Citation: (raw/javascriptallonge.pdf p.66-67)

```javascript
( function (camelCase) { return fizzbuzz(); if (camelCase) { function fizzbuzz () { return "Fizz" + "Buzz"; } } else { function fizzbuzz () { return "Fizz" + "Buzz"; } } })( true ) //=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?
```

### `technical-atom-68210eea018a360c` code

Citation: (raw/javascriptallonge.pdf p.66-67)

```javascript
function trueDat () { return true } But this is not: ( function trueDat () { return true })
```

### `technical-atom-35777e45f5f631bf` exception

Citation: (raw/javascriptallonge.pdf p.66-67)

Function declarations are formally only supposed to be made at what we might call the 'top level' of a function.

### `technical-atom-578a630465f4b26d` exception

Citation: (raw/javascriptallonge.pdf p.66-67)

Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression.

### `technical-atom-f822e3366648ac82` worked-example

Citation: (raw/javascriptallonge.pdf p.66-67)

Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:

## Related technical details

### From [[javascriptallonge-function-declarations]]: `technical-atom-824639bdc70ea377` exception

Relation: nearby source page; matched terms `declaration`, `declarations`, `expression`, `function`, `named`, `only`

Citation: (raw/javascriptallonge.pdf p.65-66)

It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement:

### From [[javascriptallonge-function-declarations]]: `technical-atom-f1f1d87b3f0d9fe4` code

Relation: nearby source page; matched terms `code`, `declarations`, `function`, `not`

Citation: (raw/javascriptallonge.pdf p.65-66)

```javascript
( function () { return fizzbuzz(); const fizzbuzz = function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> undefined is not a function (evaluating 'fizzbuzz()')
```

### From [[javascriptallonge-function-declarations]]: `technical-atom-ce3f07fc430dd604` procedure

Relation: nearby source page; matched terms `declarations`, `function`, `occur`, `top`

Citation: (raw/javascriptallonge.pdf p.65-66)

First, function declarations are hoisted to the top of the function in which they occur.

### From [[javascriptallonge-function-declarations]]: `technical-atom-f07b324de3d238c3` code

Relation: nearby source page; matched terms `although`, `code`, `declarations`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.65-66)

```javascript
( function () { return fizzbuzz(); function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> 'FizzBuzz' Although fizzbuzz is declared later in the function, JavaScript behaves as if we'd written: ( function () { {
```
