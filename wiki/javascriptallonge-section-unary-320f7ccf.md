---
page_id: javascriptallonge-section-unary-320f7ccf
page_kind: source
summary: Unary: 11 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-unary-320f7ccf@0e5a7469af768235f5a553a3852f5ace
---

# Unary

From [[javascriptallonge]].

## Statements

- Recipes with Basic Functions

59

## **Unary**

“Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:

['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_ In that example, it looks exactly like the mapping function you’ll find in most languages: You pass it a function, and it calls the function with one argument, the element of the array. However, that’s not the whole story. JavaScript’s map actually calls each function with _three_ arguments: The element, the index of the element in the array, and the array itself.

Let’s try it:

[1, 2, 3].map( **function** (element, index, arr) { console.log({element: element, index: index, arr: arr}) }) _//=> { element: 1, index: 0, arr: [ 1, 2, 3 ] } // { element: 2, index: 1, arr: [ 1, 2, 3 ] } // { element: 3, index: 2, arr: [ 1, 2, 3 ] }_ If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_ This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us: _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- ['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_ This doesn’t work because parseInt is defined as parseInt(string[, radix]). _(javascriptallonge.pdf (source-range-83ecb080-00102))_

## Technical atoms

### Technical frame 1: Unary

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00102))_

> Recipes with Basic Functions

59

## **Unary**

“Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:

['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_ In that example, it looks exactly like the mapping funct

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00103))_

> 60 **const** unary = (fn) => fn.length === 1
