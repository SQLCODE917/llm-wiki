---
page_id: javascriptallonge-section-threetofive-cdb4eaca
page_kind: source
summary: ThreeToFive: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-threetofive-cdb4eaca@03974ec164b188125ef09186adfdd088
---

# ThreeToFive

From [[javascriptallonge]].

## Statements

- When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes. _(javascriptallonge.pdf (source-range-83ecb080-01731))_
- Changes made to ThreeToFive affect OneToFive, because they share the same structure. _(javascriptallonge.pdf (source-range-83ecb080-01731))_
- Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. _(javascriptallonge.pdf (source-range-83ecb080-01732))_
- We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be “safe.” _(javascriptallonge.pdf (source-range-83ecb080-01738))_

## Technical atoms

> Context: Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes.
_(context: javascriptallonge.pdf (source-range-83ecb080-01731))_

> OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}}
_(source: javascriptallonge.pdf (source-range-83ecb080-01730))_

> Context: Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so:
_(context: javascriptallonge.pdf (source-range-83ecb080-01732))_

> **const** OneToFive = [1, 2, 3, 4, 5];
_(source: javascriptallonge.pdf (source-range-83ecb080-01735))_

> We don’t have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.
_(source: javascriptallonge.pdf (source-range-83ecb080-01738))_
