---
page_id: javascriptallonge-section-yes-consider-this-variation-copy-on-write-copy-on-read-4f68c68b
page_kind: source
summary: Yes. Consider this variation: / Copy on Write / copy-on-read: 10 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-copy-on-write-copy-on-read-4f68c68b@82322c7e3f5c00794075540cbaa7d817
---

# Yes. Consider this variation: / Copy on Write / copy-on-read

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-c844813d]] - broader source section: Yes. Consider this variation: / Copy on Write

## Statements

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-7239e085-01239))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-7239e085-01241))_
- As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy because we won't be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-7239e085-01242))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-7239e085-01241))_
- Sometimes we don't need to make a copy because we won't be modifying the list. _(javascriptallonge.pdf (source-range-7239e085-01242))_

## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Copy on Write / copy-on-read

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01241))_

> This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01240))_

```
const rest = ({first, rest}) => copy(rest);
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```
