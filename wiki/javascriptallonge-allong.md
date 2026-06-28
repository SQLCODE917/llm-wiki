---
page_id: javascriptallonge-allong
page_kind: concept
summary: Allong: 12 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-allong@75841d445e211f13e2fd8fd697dc7f43
---

# Allong

What [[javascriptallonge]] covers about allong:

## Statements

### Table of Contents

- ## **Contents**

|**A Pull of the Lever: Prefaces** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**i**|

|---|---|

|About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|ii|

|What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|v|

|Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|viii|

|Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|ix|

|About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xi|

|**Prelude: Values and Expressions over Coffee**<br>. . . . . . . . . . . . . . . . . . . . . . . . .|**xiii**|

|values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xiv|

|values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xvi|

|**A Rich Aroma: Basic Numbers** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**1**|

|**The first sip: Basic Functions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**5**|

|As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . .|7|

|Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . .|16|

|Closures and Scope<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|

|That Constant Coffee Craving<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|26|

|Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|39|

|Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . .|45|

|Building Blocks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|48|

|Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|

|Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|55|

|**Recipes with Basic Functions**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**56**|

|Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|

|Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|59|

|Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|61|

|Maybe<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|63|

|Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|65|

|Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|66|

|**Picking the Bean: Choice and Truthiness** . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**71**| _(javascriptallonge.pdf (source-range-83ecb080-00005))_

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

### What JavaScript Allongé is. And isn't.

- A Pull of the Lever: Prefaces v

## **What JavaScript Allongé is. And isn’t.**

**==> picture [468 x 275] intentionally omitted <==**

**JavaScript Allongé is a book about thinking about programs**

JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions.

The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. The intention is to improve the way we think about programs. That’s a good thing.

But while JavaScript Allongé attempts to be provocative, it is not _prescriptive_ . There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others.

Software development is a complex field. Choices in development are often driven by social considerations. People often say that software should be written for people to read. Doesn’t that depend upon the people in question? Should code written by a small team of specialists use the same techniques and patterns as code maintained by a continuously changing cast of inexperienced interns?

Choices in software development are also often driven by requirements specific to the type of software being developed. For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-83ecb080-00016))_

- vi

A Pull of the Lever: Prefaces

Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this: **const** mapWith = (iterable, fn) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **yield** fn(element); } } }); Then it can be jarring to add new helpers written that place the verb first, like this: **const** filterWith = (fn, iterable) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **if** (!!fn(element)) **yield** element; } } });

There are reasons why the second form is more flexible, especially when used in combination with partial application, but does that outweigh the benefit of having an entire codebase do everything consistently the first way or the second way?

Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. The use of source-code control systems with integrated diffing rewards making certain types of focused changes. The use of linters[1] makes checking for certain types of undesirable code very cheap. Debuggers encourage the use of functions with explicit or implicit names. Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites.

JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking.

## **how this book is organized**

_JavaScript Allongé_ introduces new aspects of programming with functions in each chapter, explaining exactly how JavaScript works. Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use.

1https://en.wikipedia.org/wiki/Lint_ _(javascriptallonge.pdf (source-range-83ecb080-00017))_

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

### Forewords to the First Edition

- ix

A Pull of the Lever: Prefaces

## **Forewords to the First Edition**

## **michael fogus**

As a life-long bibliophile and long-time follower of Reg’s online work, I was excited when he started writing books. However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. So as you might imagine I was “skeptical” about the decision to release JavaScript Allongé as an ongoing ebook, with a pay-what-you-want model. However, Reg sent me a copy of his book and I was humbled. Not only was this a great book, but it was also a great way to write and distribute books. Having written books myself, I know the pain of soliciting and receiving feedback.

The act of writing is an iterative process with (very often) tight revision loops. However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. On more than one occasion I’ve found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. However, with the Leanpub model the read-feedback-change process is extremely efficient, leaving in its wake a quality book that continues to get better as others likewise read and comment into infinitude.

In the case of JavaScript Allongé, you’ll find the Leanpub model a shining example of effectiveness. Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. I kid.

As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you’ll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time.

Enjoy.

– Fogus, fogus.me[5]

## **matthew knox**

A different kind of language requires a different kind of book.

JavaScript holds surprising depths–its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many

5http://www.fogus.me _(javascriptallonge.pdf (source-range-83ecb080-00022))_

### About The Sample PDF

- xi

A Pull of the Lever: Prefaces

## **About The Sample PDF**

This sample edition of the book includes just a portion of the complete book. Buying the book in progress entitles you to free updates, so download it today[7] ! Besides, **there’s really no risk at all** . If you read _JavaScript Allongé, The “six” edition_ and it doesn’t blow your mind, your money will be cheerfully refunded.

–Reginald “Raganwald” Braithwaite, Toronto, 2015

> 7http://leanpub.com/javascriptallongesix _(javascriptallonge.pdf (source-range-83ecb080-00025))_

### Thanks!

- The Golden Crema: Appendices and Afterwords

268

## **Thanks!**

## **Daniel Friedman and Matthias Felleisen**

**==> picture [240 x 330] intentionally omitted <==**

**The Little Schemer**

_JavaScript Allongé_ was inspired by The Little Schemer[104] by Daniel Friedman and Matthias Felleisen. But where _The Little Schemer’s_ primary focus is recursion, _JavaScript Allongé’s_ primary focus is **functions as first-class values** .

> 104http://www.amzn.com/0262560992?tag=raganwald001-20 _(javascriptallonge.pdf (source-range-83ecb080-00338))_


## Technical atoms

### Technical frame 1: Table of Contents

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00007))_

> ## CONTENTS

|**Composing and Decomposing Data** . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|**77**|

|---|---|---|

|Arrays and Destructuring Arguments<br>. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|78|

|Self-Similarity . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|86|

|Tail Calls (and Default Arguments) . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|94|

|Garbage, Garbage Everywhere . . . . . . . .|. . . . . . . .

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00006))_

| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |

<details>
<summary>Raw table text</summary>

```
| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |
```

</details>


## Related pages

- [[javascriptallonge-javascript-allong]] - narrower topic: Javascript Allong shares source evidence from What JavaScript Allongé is. And isn't.: A Pull of the Lever: Prefaces v  ## **What JavaScript Allongé is. And isn’t.**  **==> picture [468 x 275] intentionally omitted <==**  **JavaScript Allongé is a book ... [truncated] (3 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Table of Contents: ## **Contents**  |**A Pull of the Lever: Prefaces** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**i**|  |---|---|  |About JavaScript Allong ... [truncated]; Javascript shares technical record from Table of Contents: | A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i | | --- | --- | | About JavaScript Allongé . . . . . . . . ... [truncated] (8 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-edition]] - shared statements: Edition shares source evidence from About JavaScript Allongé: iv  A Pull of the Lever: Prefaces **function** foo (first, ...rest) { _// ..._ } And presto, rest collects the rest of the arguments without a lot of malarky involvi ... [truncated] (3 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
