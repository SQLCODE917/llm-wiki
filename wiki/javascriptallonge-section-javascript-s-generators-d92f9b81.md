---
page_id: javascriptallonge-section-javascript-s-generators-d92f9b81
page_kind: source
summary: javascript's generators: 17 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-javascript-s-generators-d92f9b81@2790d877e2d59b57056a94ed97f55bb8
---

# javascript's generators

From [[javascriptallonge]].

## Statements

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-31a4cf47-01662))_
- We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator . To write a generator, we write a function, but we make two changes: _(javascriptallonge.pdf (source-range-31a4cf47-01663))_
- When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately. _(javascriptallonge.pdf (source-range-31a4cf47-01668))_
- Generator functions can take an argument. Let's use that to illustrate yield : _(javascriptallonge.pdf (source-range-31a4cf47-01669))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-31a4cf47-01672))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-31a4cf47-01663))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-31a4cf47-01668))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-31a4cf47-01672))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . _(javascriptallonge.pdf (source-range-31a4cf47-01672))_

## Technical atoms

### Technical frame 1: javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01668))_

> When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01667))_

```
function * empty () {}; empty().next() //=> {"done": true }
```

### Technical frame 2: javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01669))_

> Generator functions can take an argument. Let's use that to illustrate yield :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01668))_

> When we invoke empty , we get an iterator with no elements.

### Technical frame 3: javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01672))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01671))_

```
function * only (something) { yield something; }; only("you").next() //=> {"done": false , value: "you"}
```

### Technical frame 4: javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01672))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01673))_

```
only("you").next() //=> {"done": false , value: "you"} only("the lonely").next() //=> {"done": false , value: "the lonely"}
```

### Technical frame 5: javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01672))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01675))_

```
const sixteen = only("sixteen"); sixteen.next() //=> {"done": false , value: "sixteen"} sixteen.next() //=> {"done": true }
```
