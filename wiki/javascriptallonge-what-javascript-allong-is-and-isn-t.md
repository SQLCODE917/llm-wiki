---
page_id: javascriptallonge-what-javascript-allong-is-and-isn-t
page_kind: source
summary: What JavaScript Allongé is. And isn't. from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.10-12
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé is a book about thinking about programs and programming with functions. It focuses on underlying ideas and fundamentals, aiming to improve how we think about programs. It is not prescriptive and does not suggest that any techniques shown are the only, best, or even acceptable way to write programs.

## Key supported claims

- JavaScript Allongé is a book about thinking about programs, focusing on underlying ideas and fundamentals to improve how we think about programs (raw/javascriptallonge.pdf p.10-12).
- The book is about programming with functions, exploring ideas from decorators to methods to delegation and mixins (raw/javascriptallonge.pdf p.10-12).
- While the book attempts to be provocative, it is not prescriptive, and does not suggest that any shown techniques are the only, best, or acceptable way to write programs (raw/javascriptallonge.pdf p.10-12).

## Technical details

### `technical-atom-0223e65089dcbedc` code

Citation: (raw/javascriptallonge.pdf p.10-12)

```javascript
const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } });
```

### `technical-atom-f16b184216c43f2a` code

Citation: (raw/javascriptallonge.pdf p.10-12)

```javascript
const filterWith = (fn, iterable) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { if (!!fn(element)) yield element; } } });
```

### `technical-atom-8b4d41ba5847a40d` requirement

Citation: (raw/javascriptallonge.pdf p.10-12)

People often say that software should be written for people to read.

### `technical-atom-eb7fee542c8a70fd` requirement

Citation: (raw/javascriptallonge.pdf p.10-12)

Should code written by a small team of specialists use the same techniques and patterns as code maintained by a continuously changing cast of inexperienced interns?

### `technical-atom-bc75ab19b26c4fc7` requirement

Citation: (raw/javascriptallonge.pdf p.10-12)

Choices in software development are also often driven by requirements specific to the type of software being developed.

### `technical-atom-438687fd29c77817` exception

Citation: (raw/javascriptallonge.pdf p.10-12)

There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others.

### `technical-atom-bb875d34f256ddae` worked-example

Citation: (raw/javascriptallonge.pdf p.10-12)

Choices in development are often driven by social considerations.

### `technical-atom-b6ecd018f1b8a40c` worked-example

Citation: (raw/javascriptallonge.pdf p.10-12)

For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source.

## Related technical details

### From [[javascriptallonge-about-javascript-allong]]: `technical-atom-e1907bc36d10e981` exception

Relation: nearby source page; matched terms `about`, `allong`, `how`, `javascript`

Citation: (raw/javascriptallonge.pdf p.7-9)

_JavaScript Allongé_ teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down.

### From [[javascriptallonge-a-rich-aroma-basic-numbers]]: `technical-atom-1fc4f4d7cccf56ac` exception

Relation: nearby source page; matched terms `does`, `javascript`, `not`, `programming`

Citation: (raw/javascriptallonge.pdf p.24-27)

Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

### From [[javascriptallonge-about-javascript-allong]]: `technical-atom-fcef76e420062c39` code

Relation: nearby source page; matched terms `about`, `allong`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```

### From [[javascriptallonge-about-javascript-allong]]: `technical-atom-2c2deb7ff6b1c072` code

Relation: nearby source page; matched terms `about`, `allong`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.7-9)

```javascript
function foo () { var first = arguments[0], rest = [].slice.call(arguments, 1); // ... }
```
