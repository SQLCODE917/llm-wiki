---
page_id: javascriptallonge-section-we-ll-keep-it-simple-javascript-s-generators-a7436505
page_kind: source
summary: We'll keep it simple: / javascript's generators: 17 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-javascript-s-generators-a7436505@5bb6f06bcbf3fae7d2a7233e8ec9214e
---

# We'll keep it simple: / javascript's generators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-ll-keep-it-simple-1104ef0d]] - broader source section: We'll keep it simple:

## Statements

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-7239e085-01661))_
- We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator . To write a generator, we write a function, but we make two changes: _(javascriptallonge.pdf (source-range-7239e085-01662))_
- When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately. _(javascriptallonge.pdf (source-range-7239e085-01667))_
- Generator functions can take an argument. Let's use that to illustrate yield : _(javascriptallonge.pdf (source-range-7239e085-01668))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-7239e085-01671))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-7239e085-01662))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-7239e085-01667))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . _(javascriptallonge.pdf (source-range-7239e085-01671))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-7239e085-01671))_

## Technical atoms

### Technical frame 1: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01667))_

> When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01666))_

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

### Technical frame 2: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01668))_

> Generator functions can take an argument. Let's use that to illustrate yield :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01667))_

> When we invoke empty , we get an iterator with no elements.

### Technical frame 3: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01670))_

```
function * only (something) {
yield something;
};
only("you").next()
//=>
{"done":false, value: "you"}
```

### Technical frame 4: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01672))_

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

### Technical frame 5: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01674))_

```
const sixteen = only("sixteen");
sixteen.next()
//=>
{"done":false, value: "sixteen"}
sixteen.next()
//=>
{"done":true}
```
