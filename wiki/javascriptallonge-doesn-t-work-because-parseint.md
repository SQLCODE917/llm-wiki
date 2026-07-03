---
page_id: javascriptallonge-doesn-t-work-because-parseint
page_kind: concept
page_family: topic-concept
summary: Doesn'T Work Because Parseint: 1 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-doesn-t-work-because-parseint@993c284f8d4bcbe989992e576143b0e6
---

# Doesn'T Work Because Parseint

What [[javascriptallonge]] covers about doesn't work because parseint:

## Statements

### Recipes with Basic Functions / Unary

- This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-7239e085-00676))_


## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00674))_

<a id="atom-technical-atom-e63879039d2b786d"></a>

> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical frame 2: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00675))_

<a id="atom-technical-atom-39444c72b711b290"></a>

```
['1', '2', '3'].map(parseInt)
//=> [1, NaN, NaN]
```

### Technical frame 3: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00677))_

<a id="atom-technical-atom-c6eb6eaeb3b33791"></a>

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

### Technical frame 4: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00678))_

<a id="atom-technical-atom-9a39c2bf7cea62fd"></a>

```
const unary = (fn) =>
fn.length === 1
? fn
: function (something) {
return fn.call(this, something)
}
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from Recipes with Basic Functions / Unary: If you pass in a function taking only one argument, it simply ignores the additional arguments. (3 shared atom(s))

## Source

- [[javascriptallonge]]
