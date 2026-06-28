---
page_id: javascriptallonge-section-values-are-expressions-partial-application-667a6672
page_kind: source
summary: values are expressions / Partial Application: 7 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-partial-application-667a6672@1b197af0884a43d4364517f11126b792
---

# values are expressions / Partial Application

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section
- [[javascriptallonge-partial-application]] - topic hub
- [[javascriptallonge-section-values-are-expressions-building-blocks-partial-application-75c3f473]] - same source heading

## Statements

- In Building Blocks, we discussed partial application, but we didn’t write a generalized recipe for it. _(javascriptallonge.pdf (source-range-83ecb080-00672))_
- This is such a common tool that many libraries provide some form of partial application. _(javascriptallonge.pdf (source-range-83ecb080-00672))_
- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost.[48] If you want to bind more than one argument, or you want to leave a “hole” in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. _(javascriptallonge.pdf (source-range-83ecb080-00673))_
- We’d need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-83ecb080-00674))_
- > 48 callFirst and callLast were inspired by Michael Fogus’ Lemonad. _(javascriptallonge.pdf (source-range-83ecb080-00678))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: **const** callLeft = (fn, ...args) => _(javascriptallonge.pdf (source-range-83ecb080-00681))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00681))_

> We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: **const** callLeft = (fn, ...args) =>

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00682))_

> (...remainingArgs) => fn(...args, ...remainingArgs); **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
