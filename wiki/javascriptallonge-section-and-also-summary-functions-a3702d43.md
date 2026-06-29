---
page_id: javascriptallonge-section-and-also-summary-functions-a3702d43
page_kind: source
summary: And also: / Summary / Functions: 15 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-summary-functions-a3702d43@bbd98641ea939a8dea919e3a89346003
---

# And also: / Summary / Functions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-summary-ece908a9]] - broader source section: And also: / Summary
- [[javascriptallonge-function]] - topic hub: opens the topic page for Function

## Statements

- Functions are values that can be part of expressions, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-7239e085-00637))_
- Functions are reference values . _(javascriptallonge.pdf (source-range-7239e085-00638))_
- Functions are applied to arguments. _(javascriptallonge.pdf (source-range-7239e085-00639))_
- Fat arrow functions have expressions or blocks as their bodies. _(javascriptallonge.pdf (source-range-7239e085-00641))_
- function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-7239e085-00642))_
- Function bodies have zero or more statements. _(javascriptallonge.pdf (source-range-7239e085-00643))_
- Block bodies evaluate to whatever is returned with the return keyword, or to undefined . _(javascriptallonge.pdf (source-range-7239e085-00645))_
- JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-7239e085-00646))_
- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are 'hoisted.' _(javascriptallonge.pdf (source-range-7239e085-00647))_
- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-7239e085-00649))_
- Scopes are nested and free variable references closed over. _(javascriptallonge.pdf (source-range-7239e085-00650))_
- Variables can shadow variables in an enclosing scope. _(javascriptallonge.pdf (source-range-7239e085-00651))_
- - JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-7239e085-00646))_
- - JavaScript uses function declarations to bind functions to names within function scope. _(javascriptallonge.pdf (source-range-7239e085-00647))_
- - Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-7239e085-00649))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00562))_

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

<details>
<summary>Raw table text</summary>

```
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

</details>

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00570))_

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) |

<details>
<summary>Raw table text</summary>

```
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

</details>

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00612))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00613))_

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

<details>
<summary>Raw table text</summary>

```
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

</details>

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00659))_

| entry | content |
| --- | --- |
| 45 | from Michael Fogus, Functional JavaScript |
| 46 | from Oliver Steele and the terse but handy node-ap |
| 47 | from James Halliday. |

<details>
<summary>Raw table text</summary>

```
Partial Application
In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You'll find examples in Lemonad 45 from Michael Fogus, Functional JavaScript 46 from Oliver Steele and the terse but handy node-ap 47 from James Halliday.
```

</details>

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00660))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00663))_

| entry | content |
| --- | --- |
| 45 | https://github.com/fogus/lemonad |
| 46 | http://osteele.com/sources/javascript/functional/ |
| 47 | https://github.com/substack/node-ap 48 |

<details>
<summary>Raw table text</summary>

```
45 https://github.com/fogus/lemonad 46 http://osteele.com/sources/javascript/functional/ 47 https://github.com/substack/node-ap 48
```

</details>

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00702))_

| entry | content |
| --- | --- |
| 50 | https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad |
| 51 | https://github.com/raganwald/andand |

<details>
<summary>Raw table text</summary>

```
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```

</details>

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01335))_

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

<details>
<summary>Raw table text</summary>

```
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

</details>
