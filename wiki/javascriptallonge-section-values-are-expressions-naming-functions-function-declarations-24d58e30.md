---
page_id: javascriptallonge-section-values-are-expressions-naming-functions-function-declarations-24d58e30
page_kind: source
summary: values are expressions / Naming Functions / function declarations: 6 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-naming-functions-function-declarations-24d58e30@87dcd504e015dda6675a737e42dcc04e
---

# values are expressions / Naming Functions / function declarations

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-naming-functions-b33e71f9]] - broader source section

## Statements

- There is another syntax for naming and/or defining a function. _(javascriptallonge.pdf (source-range-83ecb080-00546))_
- However, there are two important differences. _(javascriptallonge.pdf (source-range-83ecb080-00546))_
- First, function declarations are _hoisted_ to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-83ecb080-00546))_
- This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code. _(javascriptallonge.pdf (source-range-83ecb080-00552))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00546))_

> There is another syntax for naming and/or defining a function. It’s called a _function declaration statement_ , and it looks a lot like a named function expression, only we use it as a statement: **function** someName () { _// ..._ } This behaves a _little_ like: **const** someName = **function** someName () { _// ..._ } In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are _hoisted_ to the top of the functi

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00547))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:
