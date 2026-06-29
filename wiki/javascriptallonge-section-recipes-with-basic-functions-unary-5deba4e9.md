---
page_id: javascriptallonge-section-recipes-with-basic-functions-unary-5deba4e9
page_kind: source
summary: Recipes with Basic Functions / Unary: 15 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-unary-5deba4e9@fd28f136e43037b6d2d806cd41fd6e2f
---

# Recipes with Basic Functions / Unary

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-c9137465]] - broader source section: Recipes with Basic Functions

## Statements

- The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action: _(javascriptallonge.pdf (source-range-7239e085-00669))_
- If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: _(javascriptallonge.pdf (source-range-7239e085-00674))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-7239e085-00676))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . _(javascriptallonge.pdf (source-range-7239e085-00676))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-7239e085-00676))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00670))_

```
['1', '2', '3'].map(parseFloat)
//=> [1, 2, 3]
```

### Technical frame 2: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00673))_

```
[1, 2, 3].map(function (element, index, arr) {
console.log({element: element, index: index, arr: arr})
})
//=> { element: 1, index: 0, arr: [ 1, 2, 3 ] }
//
{ element: 2, index: 1, arr: [ 1, 2, 3 ] }
//
{ element: 3, index: 2, arr: [ 1, 2, 3 ] }
```

### Technical frame 3: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical frame 4: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00675))_

```
['1', '2', '3'].map(parseInt)
//=> [1, NaN, NaN]
```

### Technical frame 5: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00677))_

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

### Technical frame 6: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00678))_

```
const unary = (fn) =>
fn.length === 1
? fn
: function (something) {
return fn.call(this, something)
}
```

### Technical frame 7: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00680))_

```
['1', '2', '3'].map(unary(parseInt))
//=> [1, 2, 3]
```
