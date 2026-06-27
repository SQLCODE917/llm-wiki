---
page_id: javascriptallonge-section-copy-on-read-7bfd1130
page_kind: source
summary: **copy-on-read**: 13 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-read-7bfd1130@c98332335e73e027b71a2fad65e389e1
---

# **copy-on-read**

From [[javascriptallonge]].

## Statements

- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- One strategy for avoiding problems is to be _pessimistic_ . _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- As we expected, making a copy lets us modify the copy without interfering with the original. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node). _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-01881))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-01881))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01875))_

> So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01876))_

> **const** rest = ({first, rest}) => copy(rest);

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01875, source-range-83ecb080-01879))_

> So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy. This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01878))_

> parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
