---
page_id: javascriptallonge-writing
page_kind: concept
summary: Writing: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-writing@918c305839616068205ad5a09c4540b9
---

# Writing

What [[javascriptallonge]] covers about writing:

## Statements

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

### Combinators and Function Decorators

- The first sip: Basic Functions

47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress. But like compose, we could write either: **const** something = (x) => x != **null** ; And elsewhere, write: **const** nothing = (x) => !something(x); Or we could write: **const** nothing = not(something); not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. You’ll see other function decorators in the recipes, like once and maybe. Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00084))_

### A Warm Cup: Basic Strings and Quasi-Literals

- A Warm Cup: Basic Strings and Quasi-Literals

180

An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and operators[87] Like most programming languages, JavaScript also has string literals, like 'fubar' or 'fizzbuzz'. Special characters can be included in a string literal by means of an _escape sequence_ . For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line'.

There are operators that can be used on strings. The most common is +, it _concatenates_ : 'fu' + 'bar' _//=> 'fubar'_

String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing.

## **quasi-literals**

JavaScript supports _quasi-literal strings_ , a/k/a “Template Strings” or “String Interpolation Expressions.” A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g.

`foobar` _//=> 'foobar'_ `fizz` + `buzz` _//=> 'fizzbuzz'_

Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

For example:

- `A popular number for nerds is **${** 40 + 2 **}** `

- _//=> 'A popular number for nerds is 42'_

A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:

> 87https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators _(javascriptallonge.pdf (source-range-83ecb080-00242))_

### Generating Iterables

- 216

Served by the Pot: Collections

We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use JavaScript’s natural management of state instead of constantly rolling our own.

Of course, we could just as easily write a generator function for Fibonacci numbers: **function** * fibonacci () { **let** a, b; **yield** a = 0; **yield** b = 1; **while** ( **true** ) { [a, b] = [b, a + b] **yield** b; } } **for** ( **const** i **of** fibonacci()) { console.log(i); } _//=>_ 0 1 1 2 3 5 8 13 21 34 55 89 144 ...

## **yielding iterables**

Here’s a first crack at a function that returns an iterable object for iterating over trees: _(javascriptallonge.pdf (source-range-83ecb080-00279))_

- Served by the Pot: Collections

222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield** fn(element); } } first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **function** * rest (iterable) { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **yield** * iterator; }

## **Summary**

A generator is a function that is defined with function * and uses yield (or yield *) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. And we don’t need to worry about wrapping our values in an object with .done and .value properties.

This is especially useful for making iterables. _(javascriptallonge.pdf (source-range-83ecb080-00285))_

### How to run the examples

- The Golden Crema: Appendices and Afterwords

267 **const** before = (decoration) => (method) => **function** (...args) { decoration.apply( **this** , args); **return** method.apply( **this** , args) }; And it would be “transpiled” into: **var** before = **function** (decoration) { **return function** (method) { **return function** () { **for** ( **let** _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( **this** , args); **return** method.apply( **this** , args); }; }; };

Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

So instead of just writing: (() => 2 + 2)() And having 4 displayed, you’d need to write: console.log( (() => 2 + 2)() ) And 4 would appear in your browser’s development console.

You can also install the transpilers on your development system and use them with Node[102] on the command line[103] . The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node.

> 102http://nodejs.org/

> 103https://en.wikipedia.org/wiki/REPL _(javascriptallonge.pdf (source-range-83ecb080-00336))_


## Related pages

- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress ... [truncated] (3 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Generating Iterables: 216  Served by the Pot: Collections  We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use ... [truncated] (2 shared statement(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Generating Iterables: 216  Served by the Pot: Collections  We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use ... [truncated] (1 shared statement(s))
- [[javascriptallonge-generator]] - shared statements: Generator shares source evidence from Generating Iterables: Served by the Pot: Collections  222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield ... [truncated] (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Generating Iterables: Served by the Pot: Collections  222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Generating Iterables: 216  Served by the Pot: Collections  We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
