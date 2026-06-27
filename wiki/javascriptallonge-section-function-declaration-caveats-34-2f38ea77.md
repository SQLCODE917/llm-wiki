---
page_id: javascriptallonge-section-function-declaration-caveats-34-2f38ea77
page_kind: source
summary: **function declaration caveats**[34]: 11 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-function-declaration-caveats-34-2f38ea77@37e9fff7799b0cde73eec2e09b1ce242
---

# **function declaration caveats**[34]

From [[javascriptallonge]].

## Statements

- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00765))_
- The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-83ecb080-00771))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-83ecb080-00771))_
- The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-83ecb080-00775))_

## Technical atoms

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.
_(source: javascriptallonge.pdf (source-range-83ecb080-00770))_
