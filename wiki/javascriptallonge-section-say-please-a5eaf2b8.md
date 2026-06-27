---
page_id: javascriptallonge-section-say-please-a5eaf2b8
page_kind: source
summary: **say “please”**: 14 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-say-please-a5eaf2b8@a951de80bccc11efa70a90d169155089
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

> Context: We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here’s length again:
_(context: javascriptallonge.pdf (source-range-83ecb080-02140))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest));
_(source: javascriptallonge.pdf (source-range-83ecb080-02141))_

> Context: Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. Instead of writing length(list) and examining a list, we’ll write something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02142))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(rest))) );
_(source: javascriptallonge.pdf (source-range-83ecb080-02143))_

> Context: We’ll also write a handy list printer:
_(context: javascriptallonge.pdf (source-range-83ecb080-02149))_

> **const** print = (list) => list( () => "", (aPair) => ` **${** aPair(pairFirst) **} ${** print(aPair(pairRest)) **}** ` );
_(source: javascriptallonge.pdf (source-range-83ecb080-02150))_

> Context: How would all this work? Let’s start with the obvious. What is an empty list?
_(context: javascriptallonge.pdf (source-range-83ecb080-02151))_

> **const** EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()
_(source: javascriptallonge.pdf (source-range-83ecb080-02152))_

> Context: And what is a node of a list?
_(context: javascriptallonge.pdf (source-range-83ecb080-02153))_

> **const** node = (x) => (y) => (whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
_(source: javascriptallonge.pdf (source-range-83ecb080-02154))_

> **const** l123 = node(1)(node(2)(node(3)(EMPTYLIST)));
_(source: javascriptallonge.pdf (source-range-83ecb080-02156))_

> print(l123) _//=> 1 2 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-02157))_
