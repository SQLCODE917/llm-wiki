---
page_id: javascriptallonge-feature
page_kind: concept
summary: Feature: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-feature@8210ea811715db62ddefa614b1aa4a7b
---

# Feature

What [[javascriptallonge]] covers about feature:

## Statements

### About JavaScript Allongé

- ii

A Pull of the Lever: Prefaces

## **About JavaScript Allongé**

JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. If those terms seem unfamiliar, don’t worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter.

_JavaScript Allongé_ begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances.

It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor.

_JavaScript Allongé_ teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down. As a result, _JavaScript Allongé_ is a rich read releasing many of JavaScript’s subtleties, much like the Café Allongé beloved by coffee enthusiasts everywhere.

## **why the “six” edition?**

ECMAScript 2015 (formerly called ECMAScript 6 or “ES6”), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive.

Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features.

For example, block-structured languages allow us to write: **for** ( **int** i = 0; i < array.length; ++i) { _// ..._ } And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00012))_

- iii

A Pull of the Lever: Prefaces **var** i; **for** (i = 0; i < array.length; ++i) { ( **function** (i) { _// ..._ })(i) } To create the same scoping with an Immediately Invoked Function Expression, or “IIFE.” Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write: def foo (first, *rest) # ... end

Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ } The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn’t to explain how to work around JavaScript’s missing features: The intention was to explain why the style of programming exemplified by the missing features is important.

Working around the missing features was a necessary evil.

But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write: **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ } And i is scoped to the for loop. We can also write: _(javascriptallonge.pdf (source-range-83ecb080-00013))_

- iv

A Pull of the Lever: Prefaces **function** foo (first, ...rest) { _// ..._ } And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments. Not having to work around these kinds of missing features makes JavaScript Allongé a _better book_ , because it can focus on the _why_ to do something and _when_ to do it, instead of on the how to make it work

JavaScript Allongé, The “Six” Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript.

## **that’s nice. is that the only reason?**

Actually, no.

If it were just a matter of updating the syntax, the original version of JavaScript Allongé could have simply iterated, slowly replacing old syntax with new. It would have continued to say much the same things, only with new syntax.

_But there’s more to it than that_ . The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. Thus, the focus on things like writing decorators.

As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and having certain language features that happen to work well with this style of programming.

ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. It makes a number of interesting programming techniques easy to explain and easy to use. And these techniques dovetail nicely with Allongé’s focus on composing entities and working with functions.

Thus, the “six” edition introduces classes and mixins. It introduces the notion of implementing private properties with symbols. It introduces iterators and generators. But the common thread that runs through all these things is that since they are all simple objects and simple functions, we can use the same set of “programming with functions” techniques to build programs by composing small, flexible, and decoupled entities.

We just call some of those functions constructors, others decorators, others functional mixins, and yet others, policies.

Introducing so many new ideas did require a major rethink of the way the book was organized. And introducing these new ideas did add substantially to its bulk. But even so, in a way it is still explaining the exact same original idea that programs are built out of small, flexible functions composed together. _(javascriptallonge.pdf (source-range-83ecb080-00014))_

### Foreword to the Six'' edition

- viii

A Pull of the Lever: Prefaces

## **Foreword to the “Six” edition**

ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17. Getting there took a while – in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. That version was planned to have numerous new features (interfaces, namespaces, packages, multimethods, etc.), which would have turned JavaScript into a completely new language. After internal conflict, a settlement was reached in July 2008 and a new plan was made – to abandon ECMAScript 4 and to replace it with two upgrades:

- A smaller upgrade would bring a few minor enhancements to ECMAScript 3. This upgrade became ECMAScript 5.

- A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were initially discussed will show up later, in upcoming ECMAScript versions).

ECMAScript 6 has three major groups of features:

- Better syntax for features that already exist (e.g. via libraries). For example: classes and modules.

- New functionality in the standard library. For example:

- New methods for strings and arrays

- Promises (for asynchronous programming) - Maps and sets

- Completely new features. For example: Generators, proxies and WeakMaps.

With ECMAScript 6, JavaScript has become much larger as a language. _JavaScript Allongé, the “Six” Edition_ is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you’ll do so via ES6 code, handed to you in small, easily digestible pieces.

- Axel Rauschmayer Blogger[2] , trainer[3] and author of “Exploring ES6[4] ” > 2http://www.2ality.com

> 3http://ecmanauten.de

> 4http://exploringjs.com _(javascriptallonge.pdf (source-range-83ecb080-00020))_

### As Little As Possible About Functions, But No Less

- 13

The first sip: Basic Functions

## (() => {})()

_//=> undefined_

We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } We haven’t discussed these _statements_ . What’s a statement?

There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: () => { 1 + 1; 2 + 2 } But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => { 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:

> 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00050))_


## Related pages

- [[javascriptallonge-block]] - shared statements: Block shares source evidence from About JavaScript Allongé: ii  A Pull of the Lever: Prefaces  ## **About JavaScript Allongé**  JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s writ ... [truncated] (1 shared statement(s))
- [[javascriptallonge-ecmascript]] - shared statements: Ecmascript shares source evidence from Foreword to the Six'' edition: viii  A Pull of the Lever: Prefaces  ## **Foreword to the “Six” edition**  ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
