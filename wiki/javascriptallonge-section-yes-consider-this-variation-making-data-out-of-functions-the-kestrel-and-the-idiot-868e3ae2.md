---
page_id: javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-kestrel-and-the-idiot-868e3ae2
page_kind: source
page_family: section-reference
summary: Yes. Consider this variation: / Making Data Out Of Functions / the kestrel and the idiot: 12 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-kestrel-and-the-idiot-868e3ae2@d7aedc7b48371c87d10551febd38d5d8
---

# Yes. Consider this variation: / Making Data Out Of Functions / the kestrel and the idiot

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-f095c99b]] - broader source section: Yes. Consider this variation: / Making Data Out Of Functions

## Statements

- A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K , is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-7239e085-01338))_
- The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42 . Very simple, but useful. Now we'll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value. _(javascriptallonge.pdf (source-range-7239e085-01341))_
- This is very interesting. Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-7239e085-01344))_
- This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value. _(javascriptallonge.pdf (source-range-7239e085-01352))_
