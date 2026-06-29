---
page_id: javascriptallonge-section-why-the-six-edition-c2a6b7fa
page_kind: source
summary: why the 'six' edition?: 28 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-why-the-six-edition-c2a6b7fa@0e716d78d5ec09da974b0995690a848c
---

# why the 'six' edition?

From [[javascriptallonge]].

## Statements

- ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-8eb13d6b-00021))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-8eb13d6b-00022))_
- And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-8eb13d6b-00025))_
- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write: _(javascriptallonge.pdf (source-range-8eb13d6b-00028))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-8eb13d6b-00030))_
- The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important. _(javascriptallonge.pdf (source-range-8eb13d6b-00032))_
- Working around the missing features was a necessary evil. _(javascriptallonge.pdf (source-range-8eb13d6b-00033))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write: _(javascriptallonge.pdf (source-range-8eb13d6b-00034))_
- And i is scoped to the for loop. We can also write: _(javascriptallonge.pdf (source-range-8eb13d6b-00036))_
- And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-8eb13d6b-00038))_
- JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-8eb13d6b-00039))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-8eb13d6b-00022))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-8eb13d6b-00022))_
- And the variable i is scoped locally to the code within the braces. _(javascriptallonge.pdf (source-range-8eb13d6b-00025))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-8eb13d6b-00025))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-8eb13d6b-00030))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-8eb13d6b-00034))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-8eb13d6b-00038))_

## Technical atoms

### Technical frame 1: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00025))_

> And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00024))_

```
for ( int i = 0; i < array.length; ++i) { // ... }
```

### Technical frame 2: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00028))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00026))_

```
var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```

### Technical frame 3: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00030))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00029))_

```
def foo (first, *rest) # ... end
```

### Technical frame 4: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00032))_

> The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00031))_

```
function foo () { var first = arguments[0], rest = [].slice.call(arguments, 1); // ... }
```

### Technical frame 5: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00036))_

> And i is scoped to the for loop. We can also write:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00035))_

```
for ( let i = 0; i < array.length; ++i) { // ... }
```

### Technical frame 6: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00038))_

> And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00037))_

```
function foo (first, ...rest) { // ... }
```
