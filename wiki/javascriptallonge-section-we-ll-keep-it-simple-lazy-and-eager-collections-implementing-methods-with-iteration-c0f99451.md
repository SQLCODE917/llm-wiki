---
page_id: javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-implementing-methods-with-iteration-c0f99451
page_kind: source
page_family: section-reference
summary: We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration: 14 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-implementing-methods-with-iteration-c0f99451@18237c12bd5786a8d137c71dc33491e4
---

# We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-b2c43c7f]] - broader source section: We'll keep it simple: / Lazy and Eager Collections

## Statements

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-7239e085-01769))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-7239e085-01770))_
- To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs: _(javascriptallonge.pdf (source-range-7239e085-01776))_
