---
page_id: javascriptallonge-section-backwardness-80b1b688
page_kind: source
summary: backwardness: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-backwardness-80b1b688@e58ddb54c0794a6932ee0002ef1b25d2
---

# backwardness

From [[javascriptallonge]].

## Statements

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we'd write them like this: _(javascriptallonge.pdf (source-range-8eb13d6b-01353))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-8eb13d6b-01357))_
- But the first and second we built out of K and I don't work that way. You call them and pass them the bits, and they choose what to return. So if we wanted to use them with a two-element array, we'd need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-8eb13d6b-01358))_
- Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data. _(javascriptallonge.pdf (source-range-8eb13d6b-01361))_

## Technical atoms

### Technical frame 1: backwardness

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01357))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01354))_

```
const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus"
```

### Technical frame 2: backwardness

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01357))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01356))_

```
const first = ({first, second}) => first, second = ({first, second}) => second; const latin = {first: "primus", second: "secundus"}; first(latin) //=> "primus" second(latin) //=> "secundus"
```

### Technical frame 3: backwardness

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01361))_

> Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01360))_

```
const first = K, second = K(I); const latin = (selector) => selector("primus")("secundus"); latin(first) //=> "primus" latin(second) //=> "secundus"
```
