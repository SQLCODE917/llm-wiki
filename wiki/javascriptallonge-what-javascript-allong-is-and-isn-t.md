---
page_id: javascriptallonge-what-javascript-allong-is-and-isn-t
page_kind: source
summary: Summary of the 'What JavaScript Allongé is. And isn't.' section from javascriptallonge.pdf
sources: raw/javascriptallonge.pdf p.10-11
updated: 2026-06-22
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé is a book about thinking about programs and programming with functions, focusing on underlying ideas and fundamentals. It is not prescriptive and does not suggest that any techniques shown are the only, best, or acceptable way to write programs. The book emphasizes thinking over practice and does not address broader software development best practices.

## Key supported claims

- JavaScript Allongé is a book about programming with functions, and from functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions (raw/javascriptallonge.pdf p.10-11).
- The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas, with the intention to improve the way we think about programs (raw/javascriptallonge.pdf p.10-11).
- But while JavaScript Allongé attempts to be provocative, it is not prescriptive. There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others (raw/javascriptallonge.pdf p.10-11).

## Technical details

### `technical-atom-a43838c767b6eaed` code

Citation: (raw/javascriptallonge.pdf p.10-11)

```javascript
const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } });
```

### `technical-atom-b1be71a4ab47a537` code

Citation: (raw/javascriptallonge.pdf p.10-11)

```javascript
const filterWith = (fn, iterable) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { if (!!fn(element)) yield element; } } });
```

### `technical-atom-7dbf2228f0f08721` exception

Citation: (raw/javascriptallonge.pdf p.10-11)

There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others.

### `technical-atom-4ee1f22174e92535` requirement

Citation: (raw/javascriptallonge.pdf p.10-11)

People often say that software should be written for people to read.

### `technical-atom-7e00a5ef835a9f73` requirement

Citation: (raw/javascriptallonge.pdf p.10-11)

Should code written by a small team of specialists use the same techniques and patterns as code maintained by a continuously changing cast of inexperienced interns?

### `technical-atom-61d1c0ce145cce8b` requirement

Citation: (raw/javascriptallonge.pdf p.10-11)

Choices in software development are also often driven by requirements specific to the type of software being developed.

### `technical-atom-a88c178dfe08b992` worked-example

Citation: (raw/javascriptallonge.pdf p.10-11)

For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source.

### `technical-atom-5f5993ab18ad4d54` worked-example

Citation: (raw/javascriptallonge.pdf p.10-11)

Choices in software development must also consider the question of consistency.
