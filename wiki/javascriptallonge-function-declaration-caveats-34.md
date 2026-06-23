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

### `technical-atom-f822e3366648ac82` worked-example

Citation: (raw/javascriptallonge.pdf p.66-67)

Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:

### `technical-atom-578a630465f4b26d` exception

Citation: (raw/javascriptallonge.pdf p.66-67)

Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression.
