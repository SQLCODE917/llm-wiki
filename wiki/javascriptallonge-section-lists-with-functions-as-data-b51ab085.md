---
page_id: javascriptallonge-section-lists-with-functions-as-data-b51ab085
page_kind: source
summary: lists with functions as data: 9 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lists-with-functions-as-data-b51ab085@4db514492066c316170691fd002d6e9a
---

# lists with functions as data

From [[javascriptallonge]].

## Statements

- Here's another look at linked lists using POJOs. We use the term rest instead of second , but it's otherwise identical to what we have above: _(javascriptallonge.pdf (source-range-8eb13d6b-01376))_
- Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-8eb13d6b-01384))_
- We used functions to replace arrays and POJOs, but we still use JavaScript's built-in operators to test for equality ( === ) and to branch ?: . _(javascriptallonge.pdf (source-range-8eb13d6b-01386))_

## Technical atoms

### Technical frame 1: lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01384))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01377))_

```
const first = ({first, rest}) => first, rest = ({first, rest}) => rest, pair = (first, rest) => ({first, rest}), EMPTY = ({}); const l123 = pair(1, pair(2, pair(3, EMPTY))); first(l123) //=> 1 first(rest(l123)) //=> 2 first(rest(rest(l123))) //=3
```

### Technical frame 2: lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01384))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01379))_

```
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair)); length(l123) //=> 3 const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(rest(aPair), pair(first(aPair), delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed)); const doubled = mapWith((x) => x * 2, l123); first(doubled) //=> 2 first(rest(doubled)) //=> 4 first(rest(rest(doubled))) //=> 6 Can we do the same with the linked lists we build out of functions? Yes: const first = K, l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```

### Technical frame 3: lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01384))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01380))_

```
rest = K(I), pair = V, EMPTY = (() => {}); const l123(first) //=> 1 l123(rest)(first)
```

### Technical frame 4: lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01384))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01381))_

```
//=> 2 return l123(rest)(rest)(first) //=> 3 We write them in a backwards way, but they seem to work. How about
```

### Technical frame 5: lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01384))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01383))_

```
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest)); length(l123) //=> 3 And mapWith ? const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(aPair(rest), pair(aPair(first))(delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, aPair(rest), pair(fn(aPair(first)))(delayed)); const doubled = mapWith((x) => x * 2, l123) doubled(first) //=> 2 doubled(rest)(first) //=> 4 doubled(rest)(rest)(first) //=> 6
```
