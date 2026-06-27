---
page_id: javascriptallonge-section-why-the-six-edition-e4ab9acb
page_kind: source
summary: **why the “six” edition?**: 26 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-why-the-six-edition-e4ab9acb@24af9d609c29b71b58c8ea7b29e2ee37
---

# **why the “six” edition?**

From [[javascriptallonge]].

## Statements

- Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- ECMAScript 2015 (formerly called ECMAScript 6 or “ES6”), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- And the variable i is scoped locally to the code within the braces. _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- And the variable i is scoped locally to the code within the braces. _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. _(javascriptallonge.pdf (source-range-83ecb080-00049))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-83ecb080-00051))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-83ecb080-00051))_
- The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn’t to explain how to work around JavaScript’s missing features: The intention was to explain why the style of programming exemplified by the missing features is important. _(javascriptallonge.pdf (source-range-83ecb080-00053))_
- Working around the missing features was a necessary evil. _(javascriptallonge.pdf (source-range-83ecb080-00054))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-83ecb080-00055))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-83ecb080-00055))_
- And i is scoped to the for loop. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a _better book_ , because it can focus on the _why_ to do something and _when_ to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a _better book_ , because it can focus on the _why_ to do something and _when_ to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- JavaScript Allongé, The “Six” Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-00063))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00039))_

> For example, block-structured languages allow us to write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00040))_

> **for** ( **int** i = 0; i < array.length; ++i) {

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00047))_

> **for** (i = 0; i < array.length; ++i) { ( **function** (i) { _// ..._ })(i) }

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00051))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00052))_

> **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ }

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00055))_

> But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00056))_

> **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }
