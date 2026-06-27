---
page_id: javascriptallonge-section-flip-73a3aeb5
page_kind: source
summary: Flip: 19 source-backed entries and 14 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-flip-73a3aeb5@2fd0674483365a54a4295c18eaecef27
---

# Flip

From [[javascriptallonge]].

## Statements

- Let’s consider the case whether we have a map function of our own, perhaps from the allong.es[84] library, perhaps from Underscore[85] . _(javascriptallonge.pdf (source-range-83ecb080-02240))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-02253))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-02253))_
- Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-83ecb080-02266))_
- When we learn about context and methods, we’ll see that flip throws the current context away, so it can’t be used to flip methods. _(javascriptallonge.pdf (source-range-83ecb080-02270))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02238))_

> We wrote mapWith like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02239))_

> **const** mapWith = (fn) => (list) => list.map(fn);

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02240))_

> Let’s consider the case whether we have a map function of our own, perhaps from the allong.es[84] library, perhaps from Underscore[85] . We could write our function something like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02241))_

> **const** mapWith = (fn) => (list) => map(list, fn);

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02241))_

> **const** mapWith = (fn) => (list) => map(list, fn);

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02242))_

> You can see that if we simplify it:

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02242))_

> Looking at this, we see we’re conflating two separate transformations. First, we’re reversing the order of arguments. You can see that if we simplify it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02243))_

> **const** mapWith = (fn, list) => map(list, fn);

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02244))_

> Second, we’re “currying” the function so that instead of defining a function that takes two arguments, it returns a function that takes the first argument and returns a function that takes the second argument and applies them both, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02245))_

> **const** mapper = (list) => (fn) => map(list, fn);

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02246))_

> Let’s return to the implementation of mapWith that relies on a map function rather than a method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02247))_

> **const** mapWith = (fn) => (list) => map(list, fn);

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02248))_

> We’re going to extract these two operations by refactoring our function to paramaterize map. The first step is to give our parameters generic names:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02249))_

> **const** mapWith = (first) => (second) => map(second, first);

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02248))_

> We’re going to extract these two operations by refactoring our function to paramaterize map. The first step is to give our parameters generic names:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02251))_

> **const** wrapper = (fn) =>

### Technical atom 9

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02252))_

> (first) => (second) => fn(second, first);

### Technical atom 10

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02258))_

> **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02259))_

> Sometimes you want to flip, but not curry:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02260))_

> **const** flip = (fn) =>

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02259))_

> Sometimes you want to flip, but not curry:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02261))_

> (first, second) => fn(second, first);

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02262))_

> This is gold. Consider how we define mapWith now:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02263))_

> **var** mapWith = flipAndCurry(map);

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02266))_

> Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We _could_ make that into flip:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02268))_

> Now if we write mapWith = flip(map), we can call mapWith(fn, list) or mapWith(fn)(list), our choice.
