---
page_id: javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-default-arguments-ec839e44
page_kind: source
summary: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments: 9 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-default-arguments-ec839e44@1e9d388c0df3bbb5ce8b935666ee9997
---

# Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-e2a54ac1]] - broader source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)

## Statements

- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . _(javascriptallonge.pdf (source-range-7239e085-01004))_
- JavaScript provides this exact syntax, it's called a default argument , and it looks like this: _(javascriptallonge.pdf (source-range-7239e085-01005))_
- Now we don't need to use two functions. A default argument is concise and readable. _(javascriptallonge.pdf (source-range-7239e085-01009))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01004))_

> What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01002))_

```
const factorial = (n, work) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1, 1)
//=> 1
factorial(5, 1)
//=> 120
```

### Technical frame 2: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01004))_

> What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01003))_

> But it is hideous to have to always add a 1 parameter, we'd be demanding that everyone using the factorial function know that we are using a tail-recursive implementation.

### Technical frame 3: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01009))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01006))_

```
const factorial = (n, work = 1) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1)
//=> 1
factorial(6)
//=> 720
```

### Technical frame 4: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01009))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01008))_

```
const length = ([first, ...rest], numberToBeAdded = 0) =>
first === undefined
? numberToBeAdded
: length(rest, 1 + numberToBeAdded)
length(["foo", "bar", "baz"])
//=> 3
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```
