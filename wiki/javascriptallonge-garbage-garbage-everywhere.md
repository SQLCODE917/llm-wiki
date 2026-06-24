---
page_id: javascriptallonge-garbage-garbage-everywhere
page_kind: source
summary: Garbage, Garbage Everywhere from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.126-128
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains tail‑call recursion for array mapping, the memory cost of temporary arrays, and contrasts JavaScript arrays with Lisp linked lists, noting possible performance drawbacks.

## Key supported claims

- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using (raw/javascriptallonge.pdf p.126-128).
- Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another (raw/javascriptallonge.pdf p.126-128).
- Lather, rinse, repeat: Every time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend (raw/javascriptallonge.pdf p.126-128).
- It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made (raw/javascriptallonge.pdf p.126-128).

## Technical details

### `technical-atom-bb88808ab8488fcf` code

Citation: (raw/javascriptallonge.pdf p.126-128)

```javascript
const mapWith = (fn, [first, ...rest], prepend = []) => first === undefined ? prepend : mapWith(fn, rest, [...prepend, fn(first)]); mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### `technical-atom-41b060c77014dd3f` procedure

Citation: (raw/javascriptallonge.pdf p.126-128)

To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith .

### `technical-atom-5d1ebb19d843b288` procedure

Citation: (raw/javascriptallonge.pdf p.126-128)

Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend .

### `technical-atom-ebf22f50d193ae3e` procedure

Citation: (raw/javascriptallonge.pdf p.126-128)

Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded.

### `technical-atom-426a230840ec0066` exception

Citation: (raw/javascriptallonge.pdf p.126-128)

Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

### `technical-atom-ff30dd9aed90995c` exception

Citation: (raw/javascriptallonge.pdf p.126-128)

64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made.

## Related technical details

### From [[javascriptallonge-converting-non-tail-calls-to-tail-calls]]: `technical-atom-0cbba5b5d2e15ff8` exception

Relation: nearby source page; matched terms `call`, `does`, `function`, `make`, `not`, `programmers`

Citation: (raw/javascriptallonge.pdf p.120-121)

And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

### From [[javascriptallonge-some-history]]: `technical-atom-04ba09a2311c5fc1` exception

Relation: nearby source page; matched terms `all`, `array`, `elements`, `javascript`, `linked`

Citation: (raw/javascriptallonge.pdf p.128-130)

In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array.

### From [[javascriptallonge-factorials]]: `technical-atom-6d9212df7fc2c4c0` procedure

Relation: nearby source page; matched terms `function`, `make`, `one`, `procedure`, `then`, `used`

Citation: (raw/javascriptallonge.pdf p.121-123)

Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-d529e9b6bf45d57d` exception

Relation: nearby source page; matched terms `data`, `javascript`, `lists`, `not`, `only`, `very`

Citation: (raw/javascriptallonge.pdf p.132)

Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer.
