---
page_id: javascriptallonge-section-naming-functions-3c1fa48f
page_kind: source
page_family: section-reference
summary: Naming Functions: 6 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-naming-functions-3c1fa48f@a9177463af27abc69b470c3ab973b852
---

# Naming Functions

From [[javascriptallonge]].

## Statements

- 44 

The first sip: Basic Functions 

( **function** (camelCase) { **return** fizzbuzz(); 

**if** (camelCase) { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } **else** { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } })( **true** ) _//=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?_ 

Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. 

Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. So this is a function declaration: 

**function** trueDat () { **return true** } 

But this is not: 

( **function** trueDat () { **return true** }) 

The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-af806fb1-00076))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-af806fb1-00076))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-af806fb1-00076))_
