---
page_id: javascriptallonge-generators-and-iterables
page_kind: source
summary: Chapter on generators and iterables from JavaScript Allongé
sources: raw/javascriptallonge.pdf p.234-236
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Chapter on generators and iterables from JavaScript Allongé

## Key supported claims

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it, and JavaScript takes care of turning this into an object with a .next() function we can call (raw/javascriptallonge.pdf p.234-236).
- If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 (raw/javascriptallonge.pdf p.234-236).
- Recalling the way we wrote ordered collections, we could make a collection that uses a generator function (raw/javascriptallonge.pdf p.234-236).
- Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method (raw/javascriptallonge.pdf p.234-236).
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects (raw/javascriptallonge.pdf p.234-236).
