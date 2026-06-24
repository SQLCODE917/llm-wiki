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

## Related technical details

### From [[javascriptallonge-a-few-utilities]]: `technical-atom-7d32301f2d7c15dd` code

Relation: nearby source page; matched terms `copy`, `list`, `mapwith`, `node`, `rest`, `value`

Citation: (raw/javascriptallonge.pdf p.159-161)

```javascript
const copy = (node, head = null , tail = null ) => { if (node === EMPTY) { return head; } else if (tail === null ) { const { first, rest } = node; const newNode = { first, rest }; return copy(rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first, rest }; tail.rest = newNode; return copy(node.rest, head, newNode); } } const first = ({first, rest}) => first; const rest = ({first, rest}) => rest; const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(rest(node), { first: first(node), rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed }); const at = (index, list) => index === 0 ? first(list) : at(index - 1, rest(list)); const set = (index, value, list, originalList = list) => index === 0 ? (list.first = value, originalList) : set(index - 1, value, rest(list), originalList) const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }};
```

### From [[javascriptallonge-copy-on-write]]: `technical-atom-7b66382009088ae1` exception

Relation: nearby source page; matched terms `child`, `copy`, `interfering`, `lists`, `our`, `parent`

Citation: (raw/javascriptallonge.pdf p.158-159)

But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

### From [[javascriptallonge-a-few-utilities]]: `technical-atom-490e44302ed3a6a8` code

Relation: nearby source page; matched terms `list`, `mapwith`, `node`, `rest`

Citation: (raw/javascriptallonge.pdf p.159-161)

```
reverse(delayed) : mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed }); const at = (index, list) => index === 0 ?
```

### From [[javascriptallonge-functional-iterators]]: `technical-atom-66284ad4815503e0` code

Relation: nearby source page; matched terms `call`, `function`, `javascript`, `method`, `our`, `value`

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... } . Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . But what about the function .iterator() returns? It is defined with a fat arrow () => { ... } . What is the value of this within that function? Since JavaScript doesn't bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that's where this is bound to the value of stack . Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter() .
```
