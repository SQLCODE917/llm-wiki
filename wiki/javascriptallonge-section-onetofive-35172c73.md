---
page_id: javascriptallonge-section-onetofive-35172c73
page_kind: source
summary: oneToFive: 15 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-onetofive-35172c73@29c2e659cf2ac193fbfd3446abfab147
---

# oneToFive

From [[javascriptallonge]].

## Statements

- This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. _(javascriptallonge.pdf (source-range-83ecb080-01548))_
- This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. _(javascriptallonge.pdf (source-range-83ecb080-01548))_
- car is very fast, it simply extracts the first element of the cons cell. _(javascriptallonge.pdf (source-range-83ecb080-01551))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- There’s no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- In Lisp, it’s blazingly fast because it happens in hardware. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-83ecb080-01556))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-83ecb080-01556))_
- That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. _(javascriptallonge.pdf (source-range-83ecb080-01558))_
- And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car/cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins. _(javascriptallonge.pdf (source-range-83ecb080-01558))_
- We’ll look at linked lists again when we look at Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-83ecb080-01559))_

## Technical atoms

> Context: Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like:
_(context: javascriptallonge.pdf (source-range-83ecb080-01543))_

> **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2];
_(source: javascriptallonge.pdf (source-range-83ecb080-01546))_

> **const** oneToFive = node1;
_(source: javascriptallonge.pdf (source-range-83ecb080-01547))_
