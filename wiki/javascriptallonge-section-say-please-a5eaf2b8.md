---
page_id: javascriptallonge-section-say-please-a5eaf2b8
page_kind: source
summary: **say “please”**: 14 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-say-please-a5eaf2b8@af6c388755de32c3bc64307d8206b493
---

# **say “please”**

From [[javascriptallonge]].

## Statements

- This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-83ecb080-02139))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-02140))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-02140))_
- Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. _(javascriptallonge.pdf (source-range-83ecb080-02142))_
- Now we’ll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. _(javascriptallonge.pdf (source-range-83ecb080-02144))_
- We can write reverse and mapWith as well. _(javascriptallonge.pdf (source-range-83ecb080-02158))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-02162))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02140))_

> We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here’s length again:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02141))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest));

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02142))_

> Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. Instead of writing length(list) and examining a list, we’ll write something like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02143))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(rest))) );

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02149))_

> We’ll also write a handy list printer:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02150))_

> **const** print = (list) => list( () => "", (aPair) => ` **${** aPair(pairFirst) **} ${** print(aPair(pairRest)) **}** ` );

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02151))_

> How would all this work? Let’s start with the obvious. What is an empty list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02152))_

> **const** EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02153))_

> And what is a node of a list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02154))_

> **const** node = (x) => (y) => (whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02156))_

> **const** l123 = node(1)(node(2)(node(3)(EMPTYLIST)));

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02157))_

> print(l123) _//=> 1 2 3_
