---
page_id: javascriptallonge-section-the-vireo-8403bb31
page_kind: source
summary: **the vireo**: 15 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-vireo-8403bb31@722ff11f66f2d3adf500b46eddc053c3
---

# **the vireo**

From [[javascriptallonge]].

## Statements

- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-02095))_
- For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: _(javascriptallonge.pdf (source-range-83ecb080-02098))_
- Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): _(javascriptallonge.pdf (source-range-83ecb080-02100))_
- It is known to most programmers as .tap. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- One notable example is the “thrush” or T combinator: It takes one value and applies it to a function. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- As an aside, the Vireo is a little like JavaScript’s .apply function. _(javascriptallonge.pdf (source-range-83ecb080-02114))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02096))_

> For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02097))_

> (first, second) => (selector) => selector(first)(second)

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02098))_

> For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02099))_

> (first) => (second) => (selector) => selector(first)(second)

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02100))_

> Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default):

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02101))_

> **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second);

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02100))_

> Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default):

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02102))_

> **const** latin = pair("primus")("secundus");

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02107))_

> If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y).

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02111))_

> **const** first = K, second = K(I), pair = V;

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02112))_

> **const** latin = pair("primus")("secundus");

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02113))_

> latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_
