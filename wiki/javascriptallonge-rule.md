---
page_id: javascriptallonge-rule
page_kind: concept
summary: Rule: 4 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-rule@92b9f1735f2ffe84c22acd53f61571f2
---

# Rule

What [[javascriptallonge]] covers about rule:

## Statements

### A Rich Aroma: Basic Numbers / floating

- But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 . Professional programmers almost never use floating point numbers to represent monetary amounts. For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . In this book, we need not think about such details, but outside of this book, we must. _(javascriptallonge.pdf (source-range-7239e085-00155))_

### Or even: / back on the block

- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-7239e085-00246))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-7239e085-00489))_

### Composing and Decomposing Data / Self-Similarity

- Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list: _(javascriptallonge.pdf (source-range-7239e085-00890))_


## Technical atoms

### Technical frame 1: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00247))_

```
(() => 2 + 2)()
//=> 4
(() => { 2 + 2 })()
//=> undefined
(() => (1 + 1, 2 + 2))()
//=> 4
(() => { 1 + 1; 2 + 2 })()
//=> undefined
```

### Technical frame 2: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00248))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 3: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00892))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00891))_

```
[]
//=> []
["baz", ...[]]
//=> ["baz"]
["bar", ...["baz"]]
//=> ["bar","baz"]
["foo", ...["bar", "baz"]]
//=> ["foo","bar","baz"]
```

### Technical frame 4: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00895))_

```
const [first, ...rest] = [];
first
//=> undefined
rest
//=> []:
const [first, ...rest] = ["foo"];
first
//=> "foo"
rest
//=> []
const [first, ...rest] = ["foo", "bar"];
first
//=> "foo"
rest
//=> ["bar"]
const [first, ...rest] = ["foo", "bar", "baz"];
first
//=> "foo"
rest
//=> ["bar","baz"]
For the purpose of this exploration, we will presume the following:61
const isEmpty = ([first, ...rest]) => first === undefined;
```

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00091))_

| entry | content |
| --- | --- |
| 5 | http://www.fogus.me Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy! -Matthew Knox, mattknox.com 6 |
| 6 | http://mattknox.com |

<details>
<summary>Raw table text</summary>

```
matthew knox
A different kind of language requires a different kind of book.
JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many books try to hide most of those capabilities away, giving you recipes for writing JavaScript in a way that approximates class-centric programming in other languages. Not JavaScript Allongé. It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors.
5 http://www.fogus.me
Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy!
-Matthew Knox, mattknox.com 6
6 http://mattknox.com
```

</details>


## Related pages

- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Code shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Javascript shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-follow]] - shared statements and technical atoms: Follow shares source evidence from Or even: / back on the block: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Follow shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (2 shared atom(s))
- [[javascriptallonge-literal]] - shared technical atoms: Literal shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (2 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from Or even: / back on the block: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-allong]] - shared technical atoms: Allong shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-different]] - shared technical atoms: Different shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-element]] - shared technical atoms: Element shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (1 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-programming]] - shared technical atoms: Programming shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Composing and Decomposing Data / Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-writing]] - shared technical atoms: Writing shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
