---
page_id: javascriptallonge-functional
page_kind: concept
summary: Functional: 5 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-functional@96aff78e1a9e8403fa51076c39c0be5a
---

# Functional

What [[javascriptallonge]] covers about functional:

## Statements

### ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-7239e085-00087))_

### Composing and Decomposing Data / Reassignment / why const and let were invented

- const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-7239e085-01202))_

### Like this: / summary

- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-7239e085-01621))_

### Like this: / Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-7239e085-01626))_


## Technical atoms

### Technical frame 1: Like this: / Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01630))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01627))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical frame 2: Like this: / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01643))_

> If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01642))_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
const treeIterator = (iterable) => {
const iterators = [ iterable[Symbol.iterator]() ];
return () => {
while (!!iterators[0]) {
const iterationResult = iterators[0].next();
if (iterationResult.done) {
iterators.shift();
}
else if (isIterable(iterationResult.value)) {
iterators.unshift(iterationResult.value[Symbol.iterator]());
}
else {
return iterationResult.value;
}
}
return;
}
}
const i = treeIterator([1, [2, [3, 4], 5]]);
let n;
while (n = i()) {
console.log(n)
}
//=>
1
2
3
4
5
```

### Technical frame 3: Like this: / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01653))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01651))_

```
// Generation
const fibonacci = () => {
let a, b;
console.log(a = 0);
console.log(b = 1);
while (true) {
[a, b] = [b, a + b];
console.log(b);
}
}
fibonacci()
//=>
0
1
1
2
3
5
8
13
21
34
```

### Technical frame 4: Like this: / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01653))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01652))_

```
55
89
144
...
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

### Technical atom 6

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

### Technical atom 7

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

### Technical atom 8

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


## Related pages

- [[javascriptallonge-functional-iterator]] - narrower topic: Functional Iterators shares source evidence from Like this: / summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Function shares technical record from Like this: / Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (5 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Like this: / summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated]; Iterator shares technical record from Like this: / Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Javascript shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Like this: / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Object shares technical record from Like this: / Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Program shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Programming shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-allong]] - shared statements and technical atoms: Allong shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Allong shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from Like this: / summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated]; Language shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from Like this: / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Method shares technical record from Like this: / Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (4 shared atom(s))
- [[javascriptallonge-note]] - shared technical atoms: Note shares technical record from Like this: / Generating Iterables / state machines: // Generation const fibonacci = () => { let a, b; console.log(a = 0); console.log(b = 1); while (true) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-partial-application]] - shared technical atoms: partial application shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (2 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-different]] - shared technical atoms: Different shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-version]] - shared technical atoms: Version shares technical record from Like this: / Generating Iterables / recursive iterators: const isIterable = (something) => !!something[Symbol.iterator]; const treeIterator = (iterable) => { const iterators = [ iterable[Symbol.iterator]() ]; return () => ... [truncated] (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-writing]] - shared technical atoms: Writing shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
