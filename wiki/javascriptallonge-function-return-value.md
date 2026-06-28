---
page_id: javascriptallonge-function-return-value
page_kind: concept
summary: Function Return Value: 4 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-return-value@37a1d5afb1820850a567a67516019005
---

# Function Return Value

What [[javascriptallonge]] covers about function return value:

## Statements

- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-83ecb080-00245))_
- We know that (() => 0)() returns 0, and this is unsurprising. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- Values like 0 are expressions, as are things like 40 + 2. _(javascriptallonge.pdf (source-range-83ecb080-00241))_
- Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00240))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00240))_

> Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00242))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00245))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00246))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.


## Related pages

- [[javascriptallonge-function]] - broader topic (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-return]] - broader topic (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-value]] - broader topic (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-idea]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-evaluate-expression]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
