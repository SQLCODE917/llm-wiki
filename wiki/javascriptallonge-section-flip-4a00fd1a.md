---
page_id: javascriptallonge-section-flip-4a00fd1a
page_kind: source
summary: **Flip**: 16 source-backed entries and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-flip-4a00fd1a@168423637473249d55af09f4bdbcc521
---

# **Flip**

From [[javascriptallonge]].

## Statements

- Let’s consider the case whether we have a map function of our own, perhaps from the allong.es[84] library, perhaps from Underscore[85] . _(javascriptallonge.pdf (source-range-83ecb080-02240))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-02253))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-02253))_

## Technical atoms

> Context: We wrote mapWith like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02238))_

> **const** mapWith = (fn) => (list) => list.map(fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02239))_

> Context: Let’s consider the case whether we have a map function of our own, perhaps from the allong.es[84] library, perhaps from Underscore[85] . We could write our function something like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02240))_

> **const** mapWith = (fn) => (list) => map(list, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02241))_

> Context: **const** mapWith = (fn) => (list) => map(list, fn);
_(context: javascriptallonge.pdf (source-range-83ecb080-02241))_

> You can see that if we simplify it:
_(source: javascriptallonge.pdf (source-range-83ecb080-02242))_

> Context: Looking at this, we see we’re conflating two separate transformations. First, we’re reversing the order of arguments. You can see that if we simplify it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02242))_

> **const** mapWith = (fn, list) => map(list, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02243))_

> Context: Second, we’re “currying” the function so that instead of defining a function that takes two arguments, it returns a function that takes the first argument and returns a function that takes the second argument and applies them both, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02244))_

> **const** mapper = (list) => (fn) => map(list, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02245))_

> Context: Let’s return to the implementation of mapWith that relies on a map function rather than a method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02246))_

> **const** mapWith = (fn) => (list) => map(list, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02247))_

> Context: We’re going to extract these two operations by refactoring our function to paramaterize map. The first step is to give our parameters generic names:
_(context: javascriptallonge.pdf (source-range-83ecb080-02248))_

> **const** mapWith = (first) => (second) => map(second, first);
_(source: javascriptallonge.pdf (source-range-83ecb080-02249))_

> Context: We’re going to extract these two operations by refactoring our function to paramaterize map. The first step is to give our parameters generic names:
_(context: javascriptallonge.pdf (source-range-83ecb080-02248))_

> **const** wrapper = (fn) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-02251))_

> (first) => (second) => fn(second, first);
_(source: javascriptallonge.pdf (source-range-83ecb080-02252))_

> **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);
_(source: javascriptallonge.pdf (source-range-83ecb080-02258))_

> Context: Sometimes you want to flip, but not curry:
_(context: javascriptallonge.pdf (source-range-83ecb080-02259))_

> **const** flip = (fn) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-02260))_

> Context: Sometimes you want to flip, but not curry:
_(context: javascriptallonge.pdf (source-range-83ecb080-02259))_

> (first, second) => fn(second, first);
_(source: javascriptallonge.pdf (source-range-83ecb080-02261))_

> Context: This is gold. Consider how we define mapWith now:
_(context: javascriptallonge.pdf (source-range-83ecb080-02262))_

> **var** mapWith = flipAndCurry(map);
_(source: javascriptallonge.pdf (source-range-83ecb080-02263))_
