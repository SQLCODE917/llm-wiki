---
page_id: javascriptallonge-javascript
page_kind: concept
summary: Javascript: 69 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript@0de653c0542a021a27b7e6a660441ebe
---

# Javascript

What [[javascriptallonge]] covers about javascript:

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

### values are expressions

- xiv

Prelude: Values and Expressions over Coffee

## **values are expressions**

All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, “I want one of these.” The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista).

Let’s try this with something the computer understands easily:

## 42

Is this an expression? A value? Neither? Or both?

The answer is, this is both an expression _and_ a value.[10] The way you can tell that it’s both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:

## 42

_//=> 42_

All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water.

Astute readers will realize we’re omitting something. Congratulations! Take a sip of espresso. We’ll get to that in a moment.

Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn’t a value.[11] Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression.

Let’s try this as well with something else the computer understands easily:

> "JavaScript" + " " + "Allonge"

> _//=> "JavaScript Allonge"_

> 10Technically, it’s a _representation_ of a value using Base10 notation, but we needn’t worry about that in this book. You and I both understand that this means “42,” and so does the computer.

> 11In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. _(javascriptallonge.pdf (source-range-83ecb080-00030))_

### values and identity

- xvi

Prelude: Values and Expressions over Coffee

## **values and identity**

In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:

2 === 2 _//=> true_ 'hello' !== 'goodbye' _//=> true_

How does === work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities:

First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different _types_ . For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical:

2 === '2' _//=> false_ **true** !== 'true' _//=> true_

Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2.

**true** === **false** _//=> false_ 2 !== 5 _//=> true_ 'two' === 'five' _//=> false_

What if the cups are of the same type _and_ the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. _(javascriptallonge.pdf (source-range-83ecb080-00033))_

### A Rich Aroma: Basic Numbers

- A Rich Aroma: Basic Numbers

2 all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actually 34 base 10.

Internally, both 042 and 34 have the same representation, as double-precision floating point[13] numbers. A computer’s internal representation for numbers is important to understand. The machine’s representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer’s behaviour surprises us if we don’t know a little about what it’s doing “under the hood.” For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

## **floating**

Most programmers never encounter the limit on the magnitude of an integer. But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers.

It’s tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, “Nooooooooooooooooooooo.” A computer’s internal representation for a floating point number is binary, while our literal number was in base ten. This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2.

One of the most oft-repeated examples is this:

- 1.0 _//=> 1_

- 1.0 + 1.0 _//=> 2_

- 1.0 + 1.0 + 1.0 _//=> 3_ However:

> 13http://en.wikipedia.org/wiki/Double-precision_floating-point_format

> 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. _(javascriptallonge.pdf (source-range-83ecb080-00038))_

- A Rich Aroma: Basic Numbers

3

0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_

This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.

But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic[15] . Professional programmers almost never use floating point numbers to represent monetary amounts. For example, “$43.21” will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21. In this book, we need not think about such details, but outside of this book, we must.

## **operations on numbers**

As we’ve seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 - 34 or even 6 / 2. These can be combined to make more complex expressions, like 2 * 5 + 1.

In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So:

2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_

JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus, of course).

In addition to the common +, -, *, and /, JavaScript also supports modulus, %, and unary negation, -:

15https://en.wikipedia.org/wiki/IEEE_floating_point _(javascriptallonge.pdf (source-range-83ecb080-00039))_

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

7

## **As Little As Possible About Functions, But No Less**

In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let’s start with the second simplest possible function.[16] In JavaScript, it looks like this:

## () => 0

This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:

- (() => 0) _//=> [Function]_ What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else.

> 16 The simplest possible function is () => {}, we’ll see that later. _(javascriptallonge.pdf (source-range-83ecb080-00044))_

- The first sip: Basic Functions

8

I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function.

## **functions and identities**

You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not.

Which kind are functions? Let’s try them out and see. For reasons of appeasing the JavaScript parser, we’ll enclose our functions in parentheses: (() => 0) === (() => 0) _//=> false_

Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. “Function” is a reference type.

## **applying functions**

Let’s put functions to work. The way we use functions is to _apply_ them to zero or more values called _arguments_ . Just as 2 + 2 produces a value (in this case 4), applying a function to zero or more arguments produces a value as well.

Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. Let’s call the arguments _args_ . Here’s how to apply a function to some arguments:

## _fn_expr_ ( _args_ )

Right now, we only know about one such expression: () => 0, so let’s use it. We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). Since we aren’t giving it any arguments, we’ll simply write () after the expression. So we write: (() => 0)() _//=> 0_

> 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-83ecb080-00045))_

- 10

The first sip: Basic Functions (() => (() => 0 )() )() _//=> 0_

It evaluates to the same thing, 0.

## **commas**

The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

(1, 2) _//=> 2_

(1 + 1, 2 + 2) _//=> 4_

We can use commas with functions to create functions that evaluate multiple expressions: (() => (1 + 1, 2 + 2))() _//=> 4_

This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write: () => (1 + 1, 2 + 2) Or even: () => ( 1 + 1, 2 + 2 ) _(javascriptallonge.pdf (source-range-83ecb080-00047))_

- The first sip: Basic Functions

11

## **the simplest possible block**

There’s another thing we can put to the right of an arrow, a _block_ . A block has zero or more _statements_ , separated by semicolons.[18] So, this is a valid function:

## () => {}

It returns the result of evaluating a block that has no statements. What would that be? Let’s try it: (() => {})() _//=> undefined_

What is this undefined?

## **undefined**

In JavaScript, the absence of a value is written undefined, and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type:

## **undefined**

_//=> undefined_

Like numbers, booleans and strings, JavaScript can print out the value undefined.

**undefined** === **undefined**

_//=> true_ (() => {})() === (() => {})() _//=> true_ (() => {})() === **undefined** _//=> true_

No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-)

> 18Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it’s helpful to know it exists. _(javascriptallonge.pdf (source-range-83ecb080-00048))_

- 13

The first sip: Basic Functions

## (() => {})()

_//=> undefined_

We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } We haven’t discussed these _statements_ . What’s a statement?

There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: () => { 1 + 1; 2 + 2 } But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => { 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:

> 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00050))_

- The first sip: Basic Functions

20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

What about reference types? JavaScript does not place copies of reference values in any environment. JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original.

Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.

And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to: (value) =>

- ((ref1, ref2) => ref1 === ref2)(value, value) > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-83ecb080-00054))_

### Closures and Scope

- The first sip: Basic Functions

24

The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

> _a_ https://en.wikipedia.org/wiki/Currying

> _b_ https://en.wikipedia.org/wiki/Partial_application

## **shadowy variables from a shadowy planet**

An interesting thing happens when a variable has the same name as an ancestor environment’s variable. Consider:

- (x) => (x, y) => x + y

The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: (x) => (x, y) => (w, z) => (w) => x + y + z

When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both ws. When a variable has the same name as an ancestor environment’s binding, it is said to _shadow_ the ancestor.

This is often a good thing.

## **which came first, the chicken or the egg?**

This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state.

But before we do so, there’s one final question: Where does the ancestry start? If there’s no other code in a file, what is (x) => x’s parent environment? _(javascriptallonge.pdf (source-range-83ecb080-00059))_

- The first sip: Basic Functions

25

JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.

Sometimes, programmers wish to avoid this. If you don’t want your code to operate directly within the global environment, what can you do? Create an environment for them, of course. Many programmers choose to write every JavaScript file like this:

_// top of the file_ (() => { _// ... lots of JavaScript ..._ })();

_// bottom of the file_

The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': _global environment_ }}. As we’ll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-83ecb080-00060))_

### That Constant Coffee Craving

- 29

The first sip: Basic Functions ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_

This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name.

JavaScript gives us a way to do that, the const keyword. We’ll learn a lot more about const in future chapters, but here’s the most important thing we can do with const: (diameter) => { **const** PI = 3.14159265; **return** diameter * PI } The const keyword introduces one or more bindings in the block that encloses it. It doesn’t incur the cost of a function invocation. That’s great. Even better, it puts the symbol (like PI) close to the value (3.14159265). That’s much better than what we were writing.

We use the const keyword in a _const statement_ . const statements occur inside blocks, we can’t use them when we write a fat arrow that has an expression as its body.

It works just as we want. Instead of: ((diameter) => ((PI) => diameter * PI)(3.14159265))(2) Or: ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_

We write: _(javascriptallonge.pdf (source-range-83ecb080-00065))_

- 43

The first sip: Basic Functions

( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })() The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code.

## **function declaration caveats**[34]

Function declarations are formally only supposed to be made at what we might call the “top level” of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:

34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00079))_

### Combinators and Function Decorators

- The first sip: Basic Functions

45

## **Combinators and Function Decorators**

## **higher-order functions**

As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.

Here’s a very simple higher-order function that takes a function as an argument: **const** repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)) : **undefined** repeat(3, **function** (n) { console.log(`Hello **${** n **}** `) }) _//=>_ 'Hello 1' 'Hello 2' 'Hello 3' **undefined**

Higher-order functions dominate _JavaScript Allongé_ . But before we go on, we’ll talk about some specific types of higher-order functions.

## **combinators**

The word “combinator” has a precise technical meaning in mathematics:

“A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] If we were learning Combinatorial Logic, we’d start with the most basic combinators like S, K, and I, and work up from there to practical combinators. We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] .

> 35https://en.wikipedia.org/wiki/Combinatory_logic

> 36http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 _(javascriptallonge.pdf (source-range-83ecb080-00082))_

### Building Blocks

- The first sip: Basic Functions

48

## **Building Blocks**

When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks.

## **composition**

: One of the most basic of these building blocks is _composition_ **const** cookAndEat = (food) => eat(cook(food));

It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators: **const** compose = (a, b) => (c) => a(b(c)); **const** cookAndEat = compose(eat, cook);

If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument.

Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

- **const** actuallyTransfer= (from, to, amount) => _// do something_ **const** invokeTransfer = once(maybe(actuallyTransfer(...))); _(javascriptallonge.pdf (source-range-83ecb080-00086))_

- The first sip: Basic Functions

49

## **partial application**

Another basic building block is _partial application_ . When a function takes multiple arguments, we “apply” the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can’t get the final value, but we can get a function that represents _part_ of our application.

Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this:

_.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_ We don’t want to fool around writing _., so we can use it by writing:[41] This code implements a partial application of the map function by applying the function (n) => n * n as its second argument: **const** squareAll = (array) => map(array, (n) => n * n);

The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**const** mapWith = (fn) => (array) => map(array, fn); **const** squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) _//=> [1, 4, 9]_ We’ll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

> 39http://underscorejs.org

> 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache.

> 41If we don’t want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven’t discussed methods yet. const map = _.map; _(javascriptallonge.pdf (source-range-83ecb080-00087))_

### Summary

- The first sip: Basic Functions

55

## **Summary**

**==> picture [29 x 29] intentionally omitted <==**

## **Functions**

- Functions are values that can be part of expressions, returned from other functions, and so forth.

- Functions are _reference values_ .

- Functions are applied to arguments.

- The arguments are passed by sharing, which is also called “pass by value.” - Fat arrow functions have expressions or blocks as their bodies.

- function keyword functions always have blocks as their bodies.

- Function bodies have zero or more statements.

- Expression bodies evaluate to the value of the expression.

- Block bodies evaluate to whatever is returned with the return keyword, or to undefined.

- JavaScript uses const to bind values to names within block scope.

- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are “hoisted.” - Function application creates a scope.

- Blocks also create scopes if const statements are within them.

- Scopes are nested and free variable references closed over.

- Variables can shadow variables in an enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_

### Unary

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

### Maybe

- Recipes with Basic Functions

63

## **Maybe**

A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing.

This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: **const** isSomething = (value) => value !== **null** && value !== **void** 0; **const** checksForSomething = (value) => { **if** (isSomething(value)) { _// function's true logic_ } } Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: **var** something = isSomething(value) ? doesntCheckForSomething(value) : value;

Naturally, there’s a function decorator recipe for that, borrowed from Haskell’s maybe monad[50] , Ruby’s andand[51] , and CoffeeScript’s existential method invocation: **const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } > 50https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad > 51https://github.com/raganwald/andand _(javascriptallonge.pdf (source-range-83ecb080-00108))_

### Left-Variadic Functions

- Recipes with Basic Functions

67 **function** team2(...players, captain, coach) { console.log(` **${** captain **}** (captain)`); **for** ( **let** player **of** players) { console.log(player); } console.log(`squad coached by **${** coach **}** `); } _//=> Unexpected token_

ECMAScript 2015 only permits gathering parameters from the _end_ of the parameter list. Not the beginning. What to do?

## **a history lesson**

In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory: **var** __slice = Array.prototype.slice; **function** rightVariadic (fn) { **if** (fn.length < 1) **return** fn; **return function** () { **var** ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1) : []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]) : []); **return** fn.apply( **this** , args); } }; **var** firstAndButFirst = rightVariadic( **function** test (first, butFirst) { **return** [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') _//=> ["why",["hello","there","little","droid"]]_ 53Another history lesson. “Ye” in “Ye Olde,” was not actually spelled with a “Y” in days of old, it was spelled with a thorn, and is pronounced “the.” Another word, “Ye” in “Ye of little programming faith,” is pronounced “ye,” but it’s a different word altogether. _(javascriptallonge.pdf (source-range-83ecb080-00114))_

### Arrays and Destructuring Arguments

- Composing and Decomposing Data

78

## **Arrays and Destructuring Arguments**

While we have mentioned arrays briefly, we haven’t had a close look at them. Arrays are JavaScript’s “native” representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality.

## **array literals**

JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: [] _//=> []_ We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. Whitespace is optional:

[1] _//=> [1]_ [2, 3, 4] _//=> [2,3,4]_ Any expression will work:

[ 2, 3, 2 + 2 ] _//=> [2,3,4]_ Including an expression denoting another array: [[[[[]]]]] This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

Any expression will do, including names: _(javascriptallonge.pdf (source-range-83ecb080-00124))_

- Composing and Decomposing Data

83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore: **const** [what] = []; what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_ And if there aren’t any items to assign with ..., JavaScript assigns an empty array: **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_ From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

## **destructuring and return values**

Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring: _(javascriptallonge.pdf (source-range-83ecb080-00129))_

- 90

Composing and Decomposing Data **const** flatten = ([first, ...rest]) => { **if** (first === **undefined** ) { **return** []; } **else if** (!Array.isArray(first)) { **return** [first, ...flatten(rest)]; } **else** { **return** [...flatten(first), ...flatten(rest)]; } } flatten(["foo", [3, 4, []]]) _//=> ["foo",3,4]_ Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions.

## **mapping**

Another common problem is applying a function to every element of an array. JavaScript has a built-in function for this, but let’s write our own using linear recursion.

If we want to square each number in a list, we could write: **const** squareAll = ([first, ...rest]) => first === **undefined** ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ And if we wanted to “truthify” each element in a list, we could write: _(javascriptallonge.pdf (source-range-83ecb080-00136))_

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

94

## **Tail Calls (and Default Arguments)**

The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded.

Let’s look at how. Here’s our extremely simple mapWith function again: **const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ Let’s step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined, so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)].

This is roughly equivalent to writing: **const** mapWith = **function** (fn, [first, ...rest]) { **if** (first === **undefined** ) { **return** []; } **else** { **const** _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; **return** _temp3; } } Note that while evaluating mapWith(fn, rest), JavaScript must retain the value first or fn(first), plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1.

Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). And the same thing happens: JavaScript has to hang on to 2 (or 4, or both, _(javascriptallonge.pdf (source-range-83ecb080-00141))_

- 100

Composing and Decomposing Data **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** factorial = callLast(factorialWithDelayedWork, 1); factorial(1) _//=> 1_ factorial(5) _//=> 120_ As before, we wrote a factorialWithDelayedWork function, then used partial application (callLast) to make a factorial function that took just the one argument and supplied the initial work value.

## **default arguments**

Our problem is that we can directly write: **const** factorial = (n, work) => n === 1 ? work : factorial(n - 1, n * work); factorial(1, 1) _//=> 1_ factorial(5, 1) _//=> 120_ But it is hideous to have to always add a 1 parameter, we’d be demanding that everyone using the factorial function know that we are using a tail-recursive implementation.

What we really want is this: We want to write something like factorial(6), and have JavaScript automatically know that we really mean factorial(6, 1). But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1).

JavaScript provides this exact syntax, it’s called a _default argument_ , and it looks like this: _(javascriptallonge.pdf (source-range-83ecb080-00148))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneToFive = node1;

This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. But it works the same way: If we want the head of a list, we call car on it: car(oneToFive) _//=> 1_ car is very fast, it simply extracts the first element of the cons cell.

But what about the rest of the list? cdr does the trick: cdr(oneToFive) _//=> [2,[3,[4,[5,null]]]]_ Again, it’s just extracting a reference from a cons cell, it’s very fast. In Lisp, it’s blazingly fast because it happens in hardware. There’s no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements.

So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible.

Getting back to JavaScript now, when we write [first, ...rest] to gather or spread arrays, we’re emulating the semantics of car and cdr, but not the implementation. We’re doing something laborious and memory-inefficient compared to using a linked list as Lisp did and as we can still do if we choose.

That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car/cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins.

We’ll look at linked lists again when we look at Plain Old JavaScript Objects.

68https://en.wikipedia.org/wiki/Linked_list _(javascriptallonge.pdf (source-range-83ecb080-00156))_

### Plain Old JavaScript Objects

- Composing and Decomposing Data

109

## **Plain Old JavaScript Objects**

Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list: **const** remember = ["the milk", "the coffee beans", "the biscotti"]; And they can be used to store heterogeneous things in various levels of structure: **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];

Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: **const** NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1; **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];

Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0]. Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary[69] data type, a mapping from a unique set of objects to another set of objects.

Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0, we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else.

JavaScript has dictionaries, and it calls them “objects.” The word “object” is loaded in programming circles, due to the widespread use of the term “object-oriented programming” that was coined by Alan Kay but has since come to mean many, many things to many different people.

In JavaScript, an object is a map from string keys to values.

> 69https://en.wikipedia.org/wiki/Associative_array _(javascriptallonge.pdf (source-range-83ecb080-00159))_

- Composing and Decomposing Data

110

## **literal object syntax**

JavaScript has a literal syntax for creating objects. This object maps values to the keys year, month, and day:

- { year: 2012, month: 6, day: 14 } Two objects created with separate evaluations have differing identities, just like arrays:

- { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_

Objects use [] to access the values by name, using a string:

- { year: 2012, month: 6, day: 14 }['day'] _//=> 14_

Values contained within an object work just like values contained within an array, we access them by reference to the original: **const** unique = () => [], - x = unique(), - y = unique(), - z = unique(), o = { a: x, b: y, c: z };

- o['a'] === x && o['b'] === y && o['c'] === z _//=> true_

Names needn’t be alphanumeric strings. For anything else, enclose the label in quotes:

- { 'first name': 'reginald', 'last name': 'lewis' }['first name'] _//=> 'reginald'_

If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-83ecb080-00160))_

### Mutation

- Composing and Decomposing Data

118

## **Mutation**

**==> picture [240 x 321] intentionally omitted <==**

**Cupping Grinds**

In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =: **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_ You can even add a value: _(javascriptallonge.pdf (source-range-83ecb080-00169))_

### Reassignment

- Composing and Decomposing Data

125

## **Reassignment**

Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. We saw this earlier in rebinding

By default, JavaScript permits us to _rebind_ new values to names bound with a parameter. For example, we can write: **const** evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { n = n - 2; **return** evenStevens(n); } } evenStevens(42) _//=> true_

The line n = n - 2; _rebinds_ a new value to the name n. We will discuss this at much greater length in Reassignment, but long before we do, let’s try a similar thing with a name bound using const. We’ve already bound evenStevens using const, let’s try rebinding it: evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { **return** evenStevens(n - 2); } } _//=> ERROR, evenStevens is read-only_ _(javascriptallonge.pdf (source-range-83ecb080-00177))_

- Composing and Decomposing Data

126

JavaScript does not permit us to rebind a name that has been bound with const. We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let: **let** age = 52; age = 53; age _//=> 53_

We took the time to carefully examine what happens with bindings in environments. Let’s take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment.

So let’s consider what happens with a shadowed variable: (() => { **let** age = 49; **if** ( **true** ) { **let** age = 50; } **return** age; })() _//=> 49_

Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. We go from: {age: 49, '..': global-environment} To: {age: 50, '..': {age: 49, '..': global-environment}} Then back to: _(javascriptallonge.pdf (source-range-83ecb080-00178))_

### Functional Iterators

- Composing and Decomposing Data

146

## **iterating**

Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration.

JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: **const** arraySum = (array) => { **let** sum = 0; **for** ( **let** i = 0; i < array.length; ++i) { sum += array[i]; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_

Once again, we’re mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we’re getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0.

We can write this a slightly different way, using a while loop: **const** arraySum = (array) => { **let** done, sum = 0, i = 0; **while** ((done = i == array.length, !done)) { **const** value = array[i++]; sum += value; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_

Notice that buried inside our loop, we have bound the names done and value. We can put those into a POJO (a Plain Old JavaScript Object). It’ll be a little awkward, but we’ll be patient: _(javascriptallonge.pdf (source-range-83ecb080-00201))_

- Composing and Decomposing Data

152 **const** odds = () => { **let** number = 1; **return** () => { **const** value = number; number += 2; **return** {done: **false** , value}; } } **const** squareOf = callLeft(mapIteratorWith, (x) => x * x) toArray(take(squareOf(odds()), 5)) _//=> [1, 9, 25, 49, 81]_ We could also write a filter for iterators to accompany our mapping function: **const** filterIteratorWith = (fn, iterator) => () => { **do** { **const** {done, value} = iterator(); } **while** (!done && !fn(value)); **return** {done, value}; } **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1); toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_ Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

## **bonus**

Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect, select, and detect.

We haven’t written anything that finds the first element of an iteration that meets a certain criteria. Or have we? _(javascriptallonge.pdf (source-range-83ecb080-00207))_

- Composing and Decomposing Data

153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);

This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: **const** firstInArray = (fn, array) => array.filter(fn)[0];

JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

## **caveat**

Please note that unlike most of the other functions discussed in this book, iterators are _stateful_ . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you’re changing the state of the original!

For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-00208))_

### Making Data Out Of Functions

- 165

Composing and Decomposing Data **const** reverse = (list, delayed = EMPTYLIST) => list( () => delayed, (aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed)) ); print(reverse(l123)); _//=> 3 2 1_ **const** mapWith = (fn, list, delayed = EMPTYLIST) => list( () => reverse(delayed), (aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed)) ); print(mapWith(x => x * x, reverse(l123))) _//=> 941_

We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else.

## **functions are not the real point**

There are lots of similar texts explaining how to construct complex semantics out of functions. You can establish that K and K(I) can represent true and false, model magnitudes with Church Numerals[79] or Surreal Numbers[80] , and build your way up to printing FizzBuzz.

The superficial conclusion reads something like this:

Functions are a fundamental building block of computation. They are “axioms” of combinatory logic, and can be used to compute anything that JavaScript can compute.

However, that is not the interesting thing to note here. Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. Knowing how to make a linked list out of functions is not really necessary for the working programmer. (Knowing that it can be done, on the other hand, is very important to understanding computer science.) Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons[81] of the electromagnetic force. It’s the QED of physics that underpins the Maxwell’s Equations of programming. Deeply important, but not practical when you’re building a bridge.

> 79https://en.wikipedia.org/wiki/Church_encoding

> 80https://en.wikipedia.org/wiki/Surreal_number

> 81https://en.wikipedia.org/wiki/Gauge_boson _(javascriptallonge.pdf (source-range-83ecb080-00221))_

### mapWith

- Recipes with Data

170

## **mapWith**

In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

[1, 2, 3, 4, 5].map(x => x * x) _//=> [1, 4, 9, 16, 25]_ We could write a function that behaves like the .map method if we wanted: **const** map = (list, fn) => list.map(fn);

This recipe isn’t for map: It’s for mapWith, a function that wraps around map and turns any other function into a mapper. mapWith is very simple:[82] **const** mapWith = (fn) => (list) => list.map(fn); mapWith differs from map in two ways. It reverses the arguments, taking the function first and the list second. It also “curries” the function: Instead of taking two arguments, it takes one argument and returns a function that takes another argument.

That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map: **const** squaresOf = (list) => list.map(x => x * x); squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_ We can call mapWith in one step:

> 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00228))_

### A Warm Cup: Basic Strings and Quasi-Literals

- A Warm Cup: Basic Strings and Quasi-Literals

181

- 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

- 'A popular number for nerds is' + (40 + 2) - _//=> 'A popular number for nerds is42'_

## **evaluation time**

Like any other expression, quasi-literals are evaluated _late_ , when that line or lines of code is evaluated.

So for example, **const** name = "Harry"; **const** greeting = (name) => `Hello my name is **${** name **}** `; greeting('Arthur Dent') - _//=> 'Hello my name is Arthur Dent'_

JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked.

This is exactly what we’d expect if we’d written it like this: **const** greeting = (name) => 'Hello my name is ' + name; greeting('Arthur Dent') - _//=> 'Hello my name is Arthur Dent'_ _(javascriptallonge.pdf (source-range-83ecb080-00243))_

### Iteration and Iterables

- Served by the Pot: Collections

183

## **Iteration and Iterables**

**==> picture [469 x 313] intentionally omitted <==**

**Coffee Labels at the Saltspring Coffee Processing Facility**

Many objects in JavaScript can model collections of things. A collection is like a box containing stuff. Sometimes you just want to move the box around. But sometimes you want to open it up and do things with its contents.

Things like “put a label on every bag of coffee in this box,” Or, “Open the box, take out the bags of decaf, and make a new box with just the decaf.” Or, “go through the bags in this box, and take out the first one marked ‘Espresso’ that contains at least 454 grams of beans.” All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections.

## **a look back at functional iterators**

When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here’s a stack that has its own functional iterator method: _(javascriptallonge.pdf (source-range-83ecb080-00247))_

- Served by the Pot: Collections

200

## **summary**

Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _Iterable_ ordered collections can be iterated over or gathered into another collection.

Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-00264))_

### About The Author

- The Golden Crema: Appendices and Afterwords

274

## **About The Author**

When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg “Raganwald” Braithwaite has authored libraries[221] for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others.

He writes about programming on “Raganwald[222] ,” as well as general-purpose ruminations on “Braythwayt Dot Com[223] ”.

## **contact**

Twitter: @raganwald[224] Email: reg@braythwayt.com[225] **==> picture [206 x 308] intentionally omitted <==**

**Reg “Raganwald” Braithwaite**

> 221http://github.com/raganwald

> 222http://raganwald

> 223http://braythwayt.com

> 224https://twitter.com/raganwald

> 225mailto:reg@braythwayt.com _(javascriptallonge.pdf (source-range-83ecb080-00346))_


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

### Technical frame 2: Unary

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00102))_

> Recipes with Basic Functions

59

## **Unary**

“Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:

['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_ In that example, it looks exactly like the mapping funct

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00103))_

> 60 **const** unary = (fn) => fn.length === 1


## Related pages

- [[javascriptallonge-javascript-allong]] - narrower topic: Javascript Allong shares source evidence from What JavaScript Allongé is. And isn't.: A Pull of the Lever: Prefaces v  ## **What JavaScript Allongé is. And isn’t.**  **==> picture [468 x 275] intentionally omitted <==**  **JavaScript Allongé is a book ... [truncated] (3 shared statement(s))
- [[javascriptallonge-allong]] - shared statements and technical atoms: Allong shares source evidence from Table of Contents: ## **Contents**  |**A Pull of the Lever: Prefaces** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**i**|  |---|---|  |About JavaScript Allong ... [truncated]; Allong shares technical record from Table of Contents: | A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i | | --- | --- | | About JavaScript Allongé . . . . . . . . ... [truncated] (8 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from About JavaScript Allongé: ii  A Pull of the Lever: Prefaces  ## **About JavaScript Allongé**  JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s writ ... [truncated]; Function shares technical record from Unary: 60 **const** unary = (fn) => fn.length === 1 (7 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (6 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from values and identity: xvi  Prelude: Values and Expressions over Coffee  ## **values and identity**  In JavaScript, we test whether two values are identical with the === operator, and whet ... [truncated] (5 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (3 shared statement(s))
- [[javascriptallonge-ecmascript]] - shared statements: Ecmascript shares source evidence from About JavaScript Allongé: ii  A Pull of the Lever: Prefaces  ## **About JavaScript Allongé**  JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s writ ... [truncated] (3 shared statement(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (2 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (2 shared statement(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (2 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Plain Old JavaScript Objects: Composing and Decomposing Data  109  ## **Plain Old JavaScript Objects**  Lists are not the only way to represent collections of things, but they are the “oldest” da ... [truncated] (2 shared statement(s))
- [[javascriptallonge-operator]] - shared statements: Operator shares source evidence from A Rich Aroma: Basic Numbers: A Rich Aroma: Basic Numbers  3  0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_  This kind of “inexactitude” can be ignored when perfo ... [truncated] (2 shared statement(s))
- [[javascriptallonge-programmer]] - shared statements: Programmer shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (2 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (2 shared statement(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (2 shared statement(s))
- [[javascriptallonge-alway]] - shared statements: Alway shares source evidence from Closures and Scope: The first sip: Basic Functions  25  JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things ... [truncated] (1 shared statement(s))
- [[javascriptallonge-apply]] - shared statements: Apply shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  8  I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really count ... [truncated] (1 shared statement(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  78  ## **Arrays and Destructuring Arguments**  While we have mentioned arrays briefly, we haven’t had a close look at them. Arrays ar ... [truncated] (1 shared statement(s))
- [[javascriptallonge-bind]] - shared statements: Bind shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. But this is not how Java ... [truncated] (1 shared statement(s))
- [[javascriptallonge-coffee]] - shared statements: Coffee shares source evidence from About The Author: The Golden Crema: Appendices and Afterwords  274  ## **About The Author**  When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to ... [truncated] (1 shared statement(s))
- [[javascriptallonge-decorator]] - shared statements: Decorator shares source evidence from About JavaScript Allongé: ii  A Pull of the Lever: Prefaces  ## **About JavaScript Allongé**  JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s writ ... [truncated] (1 shared statement(s))
- [[javascriptallonge-edition]] - shared statements: Edition shares source evidence from About JavaScript Allongé: iv  A Pull of the Lever: Prefaces **function** foo (first, ...rest) { _// ..._ } And presto, rest collects the rest of the arguments without a lot of malarky involvi ... [truncated] (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneTo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-game]] - shared statements: Game shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-implementation]] - shared statements: Implementation shares source evidence from Building Blocks: The first sip: Basic Functions  49  ## **partial application**  Another basic building block is _partial application_ . When a function takes multiple arguments, we ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Iteration and Iterables: Served by the Pot: Collections  200  ## **summary**  Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection fr ... [truncated] (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Tail Calls (and Default Arguments): Composing and Decomposing Data  94  ## **Tail Calls (and Default Arguments)**  The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustra ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements: Reference shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements: Rest shares source evidence from Tail Calls (and Default Arguments): Composing and Decomposing Data  94  ## **Tail Calls (and Default Arguments)**  The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustra ... [truncated] (1 shared statement(s))
- [[javascriptallonge-rule]] - shared statements: Rule shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-scope]] - shared statements: Scope shares source evidence from Closures and Scope: The first sip: Basic Functions  24  The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its argument ... [truncated] (1 shared statement(s))
- [[javascriptallonge-seen]] - shared statements: Seen shares source evidence from A Rich Aroma: Basic Numbers: A Rich Aroma: Basic Numbers  3  0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_  This kind of “inexactitude” can be ignored when perfo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-string]] - shared statements: String shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  11  ## **the simplest possible block**  There’s another thing we can put to the right of an arrow, a _block_ . A block has zero or mo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
