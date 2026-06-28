---
page_id: javascriptallonge-section-unary-2da4aa66
page_kind: source
summary: Unary: 15 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-unary-2da4aa66@4e522ea6a7326c49ea8c9c6b008f33f4
---

# Unary

From [[javascriptallonge]].

## Statements

- The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action: _(javascriptallonge.pdf (source-range-31a4cf47-00669))_
- If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: _(javascriptallonge.pdf (source-range-31a4cf47-00674))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-31a4cf47-00676))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . _(javascriptallonge.pdf (source-range-31a4cf47-00676))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-31a4cf47-00676))_

## Technical atoms

### Technical frame 1: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00670))_

```
['1', '2', '3'].map(parseFloat) //=> [1, 2, 3]
```

### Technical frame 2: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00673))_

```
[1, 2, 3].map( function (element, index, arr) { console.log({element: element, index: index, arr: arr}) }) //=> { element: 1, index: 0, arr: [ 1, 2, 3 ] } // { element: 2, index: 1, arr: [ 1, 2, 3 ] } // { element: 3, index: 2, arr: [ 1, 2, 3 ] }
```

### Technical frame 3: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical frame 4: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00675))_

```
['1', '2', '3'].map(parseInt) //=> [1, NaN, NaN]
```

### Technical frame 5: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00677))_

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

### Technical frame 6: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00678))_

```
const unary = (fn) => fn.length === 1 ? fn : function (something) { return fn.call( this , something) }
```

### Technical frame 7: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00680))_

```
['1', '2', '3'].map(unary(parseInt)) //=> [1, 2, 3]
```
