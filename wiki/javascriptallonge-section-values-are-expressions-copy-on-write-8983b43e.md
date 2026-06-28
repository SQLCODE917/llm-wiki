---
page_id: javascriptallonge-section-values-are-expressions-copy-on-write-8983b43e
page_kind: source
summary: values are expressions / Copy on Write: 26 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-copy-on-write-8983b43e@eaa7a65386f8f9ffbdfe914cc7da105a
---

# values are expressions / Copy on Write

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section
- [[javascriptallonge-section-values-are-expressions-copy-on-write-a-few-utilities-adf7d07d]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-copy-on-write-copy-on-read-4f7421de]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-copy-on-write-newparentlist-7ac1accc]] - narrower source section

## Statements

- We’ve seen how to build lists with arrays and with linked lists. _(javascriptallonge.pdf (source-range-83ecb080-01218))_
- - When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01219))_
- - When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-83ecb080-01220))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- If we _know_ that a list doesn’t share any elements with another list, we can safely modify it. _(javascriptallonge.pdf (source-range-83ecb080-01225))_
- Let’s confirm our understanding: **const** parentArray = [1, 2, 3]; **const** [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray _//=> [1,2,"three"]_ childArray _//=> ["two",3]_ **const** EMPTY = { first: {}, rest: {} }; **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = parentList.rest; parentList.rest.rest.first = "three"; childList.first = "two"; parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ This is remarkably unsafe. _(javascriptallonge.pdf (source-range-83ecb080-01225))_
- We’ll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-83ecb080-01225))_

## Statements by subsection

### values are expressions / Copy on Write / a few utilities

- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01227))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01227))_
- The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list. _(javascriptallonge.pdf (source-range-83ecb080-01231))_

### values are expressions / Copy on Write / copy-on-read

- One strategy for avoiding problems is to be _pessimistic_ . _(javascriptallonge.pdf (source-range-83ecb080-01233))_
- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-83ecb080-01233))_
- Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-83ecb080-01234))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-01235))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node). _(javascriptallonge.pdf (source-range-83ecb080-01235))_
- As we expected, making a copy lets us modify the copy without interfering with the original. _(javascriptallonge.pdf (source-range-83ecb080-01235))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-01235))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-01236))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-01236))_

### values are expressions / Copy on Write / newParentList

- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” Composing and Decomposing Data _(javascriptallonge.pdf (source-range-83ecb080-01246))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” Composing and Decomposing Data _(javascriptallonge.pdf (source-range-83ecb080-01246))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01249))_
- Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-83ecb080-01249))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01220))_

> When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01221))_

> The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array.

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01224))_

> Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list.
