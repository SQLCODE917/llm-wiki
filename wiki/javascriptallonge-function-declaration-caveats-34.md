---
page_id: javascriptallonge-function-declaration-caveats-34
page_kind: source
summary: Summary of function declaration caveats from javascriptallonge.pdf, pages 66-67
sources: raw/javascriptallonge.pdf p.66-67
updated: 2026-06-20
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
