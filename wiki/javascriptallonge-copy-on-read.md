---
page_id: javascriptallonge-copy-on-read
page_kind: source
summary: copy-on-read from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.161-161
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses the copy-on-read strategy as a method for handling structure sharing in immutable data structures, particularly in the context of linked lists in JavaScript.

## Key supported claims

- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child (raw/javascriptallonge.pdf p.161-161).
- Our mapWith function would be very expensive if we make a copy every time we call rest(node) (raw/javascriptallonge.pdf p.161-161).
- As we expected, making a copy lets us modify the copy without interfering with the original (raw/javascriptallonge.pdf p.161-161).

## Technical details

### `technical-atom-173bdbccb7a23701` code

Citation: (raw/javascriptallonge.pdf p.161)

```javascript
const rest = ({first, rest}) => copy(rest); const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); const newParentList = set(2, "three", parentList); set(0, "two", childList); parentList //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### `technical-atom-d02f674000d49e1a` exception

Citation: (raw/javascriptallonge.pdf p.161)

As we expected, making a copy lets us modify the copy without interfering with the original.
