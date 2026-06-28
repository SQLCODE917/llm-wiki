---
page_id: javascriptallonge-binding
page_kind: concept
summary: Binding: 3 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-binding@7098a43fd4c1dd459b028e2e5e911f00
---

# Binding

What [[javascriptallonge]] covers about binding:

## Statements

- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-01177))_
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00484))_
- But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-83ecb080-00488))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00490, source-range-83ecb080-00495))_

> ((PI) => (diameter) => diameter * PI )(3.14159265) And gratuitously wrap it in another IIFE so that we can bind PI to something else: ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265) Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner bindin

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00493))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3) This still evaluates to a function that calculates diameters:

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00495))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265) Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00496))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)(2) _//=> 6.2831853_


## Related pages

- [[javascriptallonge-bind]] - shared statements and technical atoms (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-value]] - shared statements (2 shared statement(s))
- [[javascriptallonge-const]] - shared statements (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements (1 shared statement(s))
- [[javascriptallonge-lexical-scope]] - shared statements (1 shared statement(s))
- [[javascriptallonge-parameter]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
