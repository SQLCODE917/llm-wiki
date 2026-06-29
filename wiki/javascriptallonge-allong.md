---
page_id: javascriptallonge-allong
page_kind: concept
summary: Allong: 11 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-allong@d094a49982a0b64ec9b8046a76a9b1a9
---

# Allong

What [[javascriptallonge]] covers about allong:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé

- JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. If those terms seem unfamiliar, don't worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter. _(javascriptallonge.pdf (source-range-7239e085-00016))_

- JavaScript Allongé begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances. _(javascriptallonge.pdf (source-range-7239e085-00017))_

### A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

- JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-7239e085-00039))_

### A Pull of the Lever: Prefaces / About JavaScript Allongé / that's nice. is that the only reason?

- But there's more to it than that . The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. Thus, the focus on things like writing decorators. _(javascriptallonge.pdf (source-range-7239e085-00043))_

### A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

- JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions. _(javascriptallonge.pdf (source-range-7239e085-00052))_

- But while JavaScript Allongé attempts to be provocative, it is not prescriptive . There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-7239e085-00054))_

- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. _(javascriptallonge.pdf (source-range-7239e085-00063))_

### ECMAScript 6 has three major groups of features:

- With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces. _(javascriptallonge.pdf (source-range-7239e085-00079))_

### ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-7239e085-00087))_

### ECMAScript 6 has three major groups of features: / About The Sample PDF

- This sample edition of the book includes just a portion of the complete book. Buying the book in progress entitles you to free updates, so download it today 7 ! Besides, there's really no risk at all . If you read JavaScript Allongé, The 'six' edition and it doesn't blow your mind, your money will be cheerfully refunded. _(javascriptallonge.pdf (source-range-7239e085-00093))_

### The Golden Crema: Appendices and Afterwords / Thanks! / Daniel Friedman and Matthias Felleisen

- JavaScript Allongé was inspired by The Little Schemer 104 by Daniel Friedman and Matthias Felleisen. But where The Little Schemer's primary focus is recursion, JavaScript Allongé's primary focus is functions as first-class values . _(javascriptallonge.pdf (source-range-7239e085-01988))_


## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00038))_

> And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00037))_

```
function foo (first, ...rest) {
// ...
}
```

### Technical atom 2

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

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01463))_

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

<details>
<summary>Raw table text</summary>

```
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

</details>


## Related pages

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of b ... [truncated]; Javascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: function foo (first, ...rest) { // ... } (11 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Function shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Functional shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Program shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Programming shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: function foo (first, ...rest) { // ... } (2 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (2 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-data]] - shared technical atoms: Data shares technical table: 84 https://github.com/raganwald/allong.es 85 http://underscorejs.org (1 shared atom(s))
- [[javascriptallonge-different]] - shared technical atoms: Different shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-writing]] - shared technical atoms: Writing shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
