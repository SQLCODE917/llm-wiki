---
page_id: javascriptallonge-javascript-allong
page_kind: concept
summary: About JavaScript Allongé: 29 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript-allong@540ed0d45b40634be1360395e31e9944
---

# About JavaScript Allongé

What [[javascriptallonge]] covers about about javascript allongé:

## Statements

_Showing 14 of 29 statements selected for this topic._

- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-83ecb080-00055))_
- JavaScript Allongé, The “Six” Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- JavaScript Allongé is a first and foremost, a book about _programming with functions_ . _(javascriptallonge.pdf (source-range-83ecb080-00032))_
- It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00032))_
- _JavaScript Allongé_ begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances. _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-83ecb080-00051))_
- Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a _better book_ , because it can focus on the _why_ to do something and _when_ to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- If it were just a matter of updating the syntax, the original version of JavaScript Allongé could have simply iterated, slowly replacing old syntax with new. _(javascriptallonge.pdf (source-range-83ecb080-00066))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00032))_

> If those terms seem unfamiliar, don’t worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00039))_

> For example, block-structured languages allow us to write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00040))_

> **for** ( **int** i = 0; i < array.length; ++i) {

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00047))_

> **for** (i = 0; i < array.length; ++i) { ( **function** (i) { _// ..._ })(i) }

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00051))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00052))_

> **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ }

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00055))_

> But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00056))_

> **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }


## Source

- [[javascriptallonge]]
