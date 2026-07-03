---
page_id: javascriptallonge-section-like-this-generating-iterables-state-machines-774a067e
page_kind: source
page_family: section-reference
summary: Like this: / Generating Iterables / state machines: 10 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-like-this-generating-iterables-state-machines-774a067e@8755e23a6cc43b400dd43af717a514a1
---

# Like this: / Generating Iterables / state machines

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-like-this-generating-iterables-283d51ed]] - broader source section: Like this: / Generating Iterables

## Statements

- Some iterables can be modelled as state machines. Let's revisit the Fibonacci sequence. Again. One way to define it is: _(javascriptallonge.pdf (source-range-7239e085-01646))_
- The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-7239e085-01647))_
- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-7239e085-01648))_
- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-7239e085-01649))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-7239e085-01653))_
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-7239e085-01653))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. _(javascriptallonge.pdf (source-range-7239e085-01653))_
