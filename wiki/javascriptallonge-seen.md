---
page_id: javascriptallonge-seen
page_kind: concept
summary: Seen: 8 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-seen@b056223ce1aeb6aa989e540e8428d612
---

# Seen

What [[javascriptallonge]] covers about seen:

## Statements

### operations on numbers

- As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 . These can be combined to make more complex expressions, like 2 * 5 + 1 . _(javascriptallonge.pdf (source-range-31a4cf47-00161))_

### void

- We've seen that JavaScript represents an undefined value by typing undefined , and we've generated undefined values in two ways: _(javascriptallonge.pdf (source-range-31a4cf47-00230))_

### That Constant Coffee Craving

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-31a4cf47-00388))_

### nested blocks

- Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: _(javascriptallonge.pdf (source-range-31a4cf47-00441))_

### || and && are control-flow operators

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-31a4cf47-00793))_

### converting non-tail-calls to tail-calls

- This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that: _(javascriptallonge.pdf (source-range-31a4cf47-00980))_

### Copy on Write

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-31a4cf47-01225))_

### yielding iterables

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-31a4cf47-01732))_


## Technical atoms

### Technical frame 1: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00445))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00442))_

```
(n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) }
```

### Technical frame 2: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00980))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00979))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysWork(["foo", "bar", "baz"], 0) //=> 3
```

### Technical frame 3: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00981))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) const length = (n) => lengthDelaysWork(n, 0);
```

### Technical frame 4: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00982))_

```
Or we could use partial application: const callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const length = callLast(lengthDelaysWork, 0); length(["foo", "bar", "baz"]) //=> 3
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from yielding iterables: We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function tha ... [truncated]; Function shares technical record from converting non-tail-calls to tail-calls: const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysW ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from nested blocks: Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statem ... [truncated]; Block shares technical record from nested blocks: (n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms: Length shares technical record from converting non-tail-calls to tail-calls: const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysW ... [truncated] (3 shared atom(s))
- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical record from nested blocks: (n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) } (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from operations on numbers: As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write ... [truncated] (2 shared statement(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (1 shared statement(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from yielding iterables: We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function tha ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
