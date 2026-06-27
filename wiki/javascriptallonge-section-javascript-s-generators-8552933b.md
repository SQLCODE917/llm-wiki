---
page_id: javascriptallonge-section-javascript-s-generators-8552933b
page_kind: source
summary: **javascript’s generators**: 17 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-javascript-s-generators-8552933b@caa3c50e33b2b6a121be9179251133b6
---

# **javascript’s generators**

From [[javascriptallonge]].

## Statements

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. _(javascriptallonge.pdf (source-range-83ecb080-02590))_
- Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-83ecb080-02590))_
- An iterator written in a generation style is called a _generator_ . _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- We can write an iterator, but use a generation style of programming. _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- An iterator written in a generation style is called a _generator_ . _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-83ecb080-02598))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-83ecb080-02598))_
- Generator functions can take an argument. _(javascriptallonge.pdf (source-range-83ecb080-02599))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- It yields the value of something, and then it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02608))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02593))_

> 2. We don’t return values or output them to console.log. We “yield” values using the yield keyword.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02594))_

> When we invoke the function, we get an iterator object back.

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02598))_

> When we invoke empty, we get an iterator with no elements.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02604))_

> Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02605))_

> only("you").next() _//=>_ {"done": **false** , value: "you"} only("the lonely").next() _//=>_ {"done": **false** , value: "the lonely"}

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02606))_

> We can invoke the same iterator twice:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02607))_

> **const** sixteen = only("sixteen"); sixteen.next() _//=>_ {"done": **false** , value: "sixteen"} sixteen.next() _//=>_ {"done": **true** }
