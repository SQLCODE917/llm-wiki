---
page_id: javascriptallonge-section-values-are-expressions-generating-iterables-yielding-iterables-bf80ac84
page_kind: source
summary: values are expressions / Generating Iterables / yielding iterables: 7 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-generating-iterables-yielding-iterables-bf80ac84@4add37cddb8e309fd62a450b59f6dd46
---

# values are expressions / Generating Iterables / yielding iterables

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-generating-iterables-c4db81d9]] - broader source section

## Statements

- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- If e is not an iterable, yield e. _(javascriptallonge.pdf (source-range-83ecb080-01750))_
- We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. _(javascriptallonge.pdf (source-range-83ecb080-01750))_
- This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-83ecb080-01751))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01744))_

> Here’s a first crack at a function that returns an iterable object for iterating over trees:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01747))_

> But if you can write it as a simple generator, write it as a simple generator.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01751))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01752))_

> But while we’re here, let’s look at one bit of this code: **for** ( **const** ee **of** tree(e)) { **yield** ee; } These three lines say, in essence, “yield all the elements of TreeIterable(e), in order.” This comes up quite often when we have collections that are compounds, collections made from other collections. Consider this operation on iterables:
