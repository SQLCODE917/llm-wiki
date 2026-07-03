---
page_id: javascriptallonge-section-yes-consider-this-variation-functional-iterators-unfolding-and-laziness-bcf7ec6a
page_kind: source
page_family: section-reference
summary: Yes. Consider this variation: / Functional Iterators / unfolding and laziness: 17 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-functional-iterators-unfolding-and-laziness-bcf7ec6a@1c949734bda8d997eba1fa6fdc5eceae
---

# Yes. Consider this variation: / Functional Iterators / unfolding and laziness

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-53aff37b]] - broader source section: Yes. Consider this variation: / Functional Iterators

## Statements

- Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example: _(javascriptallonge.pdf (source-range-7239e085-01299))_
- A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-7239e085-01303))_
- This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-7239e085-01307))_
- How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly: _(javascriptallonge.pdf (source-range-7239e085-01309))_
- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-7239e085-01312))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-7239e085-01314))_
- A function that starts with a seed and expands it into a data structure is called an unfold . _(javascriptallonge.pdf (source-range-7239e085-01303))_
- We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-7239e085-01307))_
