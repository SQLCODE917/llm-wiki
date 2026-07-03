---
page_id: javascriptallonge-section-yes-consider-this-variation-functional-iterators-caveat-c90295dd
page_kind: source
page_family: section-reference
summary: Yes. Consider this variation: / Functional Iterators / caveat: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-functional-iterators-caveat-c90295dd@a8625d3df309b0f16b6574fdbafc33d0
---

# Yes. Consider this variation: / Functional Iterators / caveat

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-53aff37b]] - broader source section: Yes. Consider this variation: / Functional Iterators

## Statements

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you're changing the state of the original! _(javascriptallonge.pdf (source-range-7239e085-01323))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-7239e085-01324))_
