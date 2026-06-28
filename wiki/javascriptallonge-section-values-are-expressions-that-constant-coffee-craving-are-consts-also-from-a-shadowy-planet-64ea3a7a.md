---
page_id: javascriptallonge-section-values-are-expressions-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-64ea3a7a
page_kind: source
summary: values are expressions / That Constant Coffee Craving / are consts also from a shadowy planet?: 22 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-64ea3a7a@bb4692a7b353b10068385fc7b8b1ace9
---

# values are expressions / That Constant Coffee Craving / are consts also from a shadowy planet?

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-that-constant-coffee-craving-bda5fc85]] - broader source section

## Statements

- We just saw that values bound with const use lexical scope, just like values bound with parameters. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- They are looked up in the environment where they are declared. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00487))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00487))_
- But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-83ecb080-00488))_
- We can test this by creating another conflict. _(javascriptallonge.pdf (source-range-83ecb080-00488))_
- This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-83ecb080-00495))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00502))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00502))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00502))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00502))_
- We’ll need a gratuitous block. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00506))_
- Typically, we want to bind our names as close to where we need them as possible. _(javascriptallonge.pdf (source-range-83ecb080-00506))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00506))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00489))_

> Let’s start, as above, by doing this with parameters. We’ll start with:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00490))_

> ((PI) => (diameter) => diameter * PI )(3.14159265) And gratuitously wrap it in another IIFE so that we can bind PI to something else:

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00490, source-range-83ecb080-00495))_

> ((PI) => (diameter) => diameter * PI )(3.14159265) And gratuitously wrap it in another IIFE so that we can bind PI to something else: ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265) Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner bindin

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00493))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3) This still evaluates to a function that calculates diameters:

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00495))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265) Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00496))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)(2) _//=> 6.2831853_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00505))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: ((diameter) => { **const** PI = 3.14159265; **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00506))_

> If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.
