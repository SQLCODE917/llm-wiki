---
page_id: javascriptallonge-seen
page_kind: concept
page_family: broad-topic
summary: Seen: 8 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-seen@30d00125f24c5359fee574b521bef2cb
---

# Seen

What [[javascriptallonge]] covers about seen:


## Related pages

### Shared technical atoms

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from We'll keep it simple: / yielding iterables: We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function tha ... [truncated]; Function shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (3 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: if (true) { // an immediately invoked block statement (IIBS) } Let’s try it: ((diameter) => { const PI = 3; if (true) { const PI = 3.14159265; return diameter * PI; ... [truncated] (2 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from And also: / That Constant Coffee Craving / nested blocks: Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statem ... [truncated]; Block shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms: Length shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls: const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysW ... [truncated] (1 shared atom(s))

### Shared claims

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from A Rich Aroma: Basic Numbers / operations on numbers: As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write ... [truncated] (2 shared statement(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Yes. Consider this variation: / Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from We'll keep it simple: / yielding iterables: We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function tha ... [truncated] (1 shared statement(s))
## Statements by source section

### A Rich Aroma: Basic Numbers / operations on numbers

- As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 . These can be combined to make more complex expressions, like 2 * 5 + 1 . _(javascriptallonge.pdf (source-range-7239e085-00157))_

### Or even: / void

- We've seen that JavaScript represents an undefined value by typing undefined , and we've generated undefined values in two ways: _(javascriptallonge.pdf (source-range-7239e085-00226))_

### And also: / That Constant Coffee Craving

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-7239e085-00385))_

### And also: / That Constant Coffee Craving / nested blocks

- Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: _(javascriptallonge.pdf (source-range-7239e085-00438))_

### Picking the Bean: Choice and Truthiness / || and && are control-flow operators

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-7239e085-00793))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

- This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that: _(javascriptallonge.pdf (source-range-7239e085-00980))_

### Yes. Consider this variation: / Copy on Write

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-7239e085-01225))_

### We'll keep it simple: / yielding iterables

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-7239e085-01731))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00439))_

<a id="atom-technical-atom-179dd365e9382c9f"></a>

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

### Technical frame 2: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00482))_

<a id="atom-technical-atom-2dde6743679c8a4b"></a>

```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

### Technical frame 3: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00483))_

<a id="atom-technical-atom-bdd5dd7c22cb3cef"></a>

```
})(2)
//=> 6.2831853
```

### Technical frame 4: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00980))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00979))_

<a id="atom-technical-atom-d0492cb61af780f2"></a>

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? 0 + numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
lengthDelaysWork(["foo", "bar", "baz"], 0)
//=> 3
```

### Technical frame 5: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00981))_

<a id="atom-technical-atom-04ddfbb646c44eec"></a>

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
const length = (n) =>
lengthDelaysWork(n, 0);
```

### Technical frame 6: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00982))_

<a id="atom-technical-atom-fb0a210bf03406d6"></a>

```
Or we could use partial application:
const callLast = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const length = callLast(lengthDelaysWork, 0);
length(["foo", "bar", "baz"])
//=> 3
```


## Source

- [[javascriptallonge]]
