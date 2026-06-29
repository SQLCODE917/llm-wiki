---
page_id: javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-vireo-6fe9a149
page_kind: source
summary: Yes. Consider this variation: / Making Data Out Of Functions / the vireo: 11 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-vireo-6fe9a149@5c55e94b5cf9da5ea1cf69aca3b39a06
---

# Yes. Consider this variation: / Making Data Out Of Functions / the vireo

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-f095c99b]] - broader source section: Yes. Consider this variation: / Making Data Out Of Functions

## Statements

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. For arrays, we'd write cons = (first, second) => [first, second] . For objects we'd write: cons = (first, second) => {first, second} . In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-7239e085-01364))_
- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function: _(javascriptallonge.pdf (source-range-7239e085-01367))_
- As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-7239e085-01374))_

## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01367))_

> For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01366))_

```
(first, second) => (selector) => selector(first)(second)
```

### Technical frame 2: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01368))_

```
(first) => (second) => (selector) => selector(first)(second)
```

### Technical frame 3: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01370))_

```
const first = K,
second = K(I),
pair = (first) => (second) => (selector) => selector(first)(second);
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Technical frame 4: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01371))_

> If we change the names to x , y , and z , we get: (x) => (y) => (z) => z(x)(y) .

### Technical frame 5: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01373))_

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
