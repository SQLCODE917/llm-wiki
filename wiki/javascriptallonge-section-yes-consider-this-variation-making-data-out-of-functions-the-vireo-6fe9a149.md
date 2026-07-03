---
page_id: javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-vireo-6fe9a149
page_kind: source
page_family: section-reference
summary: Yes. Consider this variation: / Making Data Out Of Functions / the vireo: 10 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-vireo-6fe9a149@be54cb312852ebf61c9886a456955d2e
---

# Yes. Consider this variation: / Making Data Out Of Functions / the vireo

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-f095c99b]] - broader source section: Yes. Consider this variation: / Making Data Out Of Functions

## Statements

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. For arrays, we'd write cons = (first, second) => [first, second] . For objects we'd write: cons = (first, second) => {first, second} . In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-7239e085-01364))_
- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function: _(javascriptallonge.pdf (source-range-7239e085-01367))_
- As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-7239e085-01374))_

## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01373))_

<a id="atom-technical-atom-848abd9361a0c2c5"></a>

```
const first = K,
second = K(I),
pair = V;
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```
