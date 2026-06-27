---
page_id: javascriptallonge-section-section-56917229
page_kind: source
summary: (() => {})(): 22 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-section-56917229@2cbcdd40df2d3787fe5554b6872dbcdf
---

# (() => {})()

From [[javascriptallonge]].

## Statements

- We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] _(javascriptallonge.pdf (source-range-83ecb080-00346))_
- We haven’t discussed these _statements_ . _(javascriptallonge.pdf (source-range-83ecb080-00348))_
- An expression is a JavaScript statement. _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- There are many kinds of JavaScript statements, but the first kind is one we’ve already met. _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: _(javascriptallonge.pdf (source-range-83ecb080-00351))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- This feature was originally created as a kind of helpful error-correction. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- > 21You can also separate statements with line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Statements belong inside blocks and only inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00373))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00349, source-range-83ecb080-00351))_

> There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00350))_

> () => { 2 + 2 } () => { 1 + 1; 2 + 2 }

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00351))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00352))_

> () => { 1 + 1; 2 + 2 }

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00354))_

> (() => { 2 + 2 })() _//=> undefined_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00355))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00356))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00364))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00362))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00364))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00365))_

> (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00366, source-range-83ecb080-00368))_

> And also: The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00367))_

> (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_

### Technical atom 9

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00368))_

> The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:
