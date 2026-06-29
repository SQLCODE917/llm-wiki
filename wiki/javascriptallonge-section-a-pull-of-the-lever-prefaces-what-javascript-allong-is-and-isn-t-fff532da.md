---
page_id: javascriptallonge-section-a-pull-of-the-lever-prefaces-what-javascript-allong-is-and-isn-t-fff532da
page_kind: source
summary: A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.: 30 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-pull-of-the-lever-prefaces-what-javascript-allong-is-and-isn-t-fff532da@3dfe05f28cf9ea667a4568a792b03b96
---

# A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-a-pull-of-the-lever-prefaces-9a15e9b7]] - broader source section: A Pull of the Lever: Prefaces
- [[javascriptallonge-section-a-pull-of-the-lever-prefaces-what-javascript-allong-is-and-isn-t-how-this-book-is-organized-1eb5000c]] - narrower source section: A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't. / how this book is organized

## Statements

- JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions. _(javascriptallonge.pdf (source-range-7239e085-00052))_
- The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. The intention is to improve the way we think about programs. That's a good thing. _(javascriptallonge.pdf (source-range-7239e085-00053))_
- But while JavaScript Allongé attempts to be provocative, it is not prescriptive . There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-7239e085-00054))_
- Software development is a complex field. Choices in development are often driven by social considerations. People often say that software should be written for people to read. Doesn't that depend upon the people in question? Should code written by a small team of specialists use the same techniques and patterns as code maintained by a continuously changing cast of inexperienced interns? _(javascriptallonge.pdf (source-range-7239e085-00055))_
- Choices in software development are also often driven by requirements specific to the type of software being developed. For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-7239e085-00056))_
- Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this: _(javascriptallonge.pdf (source-range-7239e085-00057))_
- Then it can be jarring to add new helpers written that place the verb first, like this: _(javascriptallonge.pdf (source-range-7239e085-00059))_
- Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. The use of source-code control systems with integrated diffing rewards making certain types of focused changes. The use of linters 1 makes checking for certain types of undesirable code very cheap. Debuggers encourage the use of functions with explicit or implicit names. Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites. _(javascriptallonge.pdf (source-range-7239e085-00062))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. _(javascriptallonge.pdf (source-range-7239e085-00063))_
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-7239e085-00054))_
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-7239e085-00056))_
- Then it can be jarring to add new helpers written that place the verb first, like this: _(javascriptallonge.pdf (source-range-7239e085-00059))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. _(javascriptallonge.pdf (source-range-7239e085-00063))_

## Statements by subsection

### A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't. / how this book is organized

- JavaScript Allongé introduces new aspects of programming with functions in each chapter, explaining exactly how JavaScript works. Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-7239e085-00065))_
- Following some of the chapters are a series of recipes designed to show the application of the chapter's ideas in practical form. While the content of each chapter builds naturally on what was discussed in the previous chapter, the recipes may draw upon any aspect of the JavaScript programming language. _(javascriptallonge.pdf (source-range-7239e085-00067))_
- Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-7239e085-00065))_

## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00052))_

> JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00050))_

> [Figure] (p.10)

### Technical frame 2: A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00059))_

> Then it can be jarring to add new helpers written that place the verb first, like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00058))_

```
const mapWith = (iterable, fn) =>
({
[Symbol.iterator]: function* () {
for (let element of iterable) {
yield fn(element);
}
}
});
```

### Technical frame 3: A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00062))_

> Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. The use of source-code control systems with integrated diffing rewards making certain types of focused changes. The use of linters 1 makes checking for certain types of undesirable code very cheap. Debuggers encourage the use of functions with explicit or implicit names. Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation o

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00060))_

```
const filterWith = (fn, iterable) =>
({
[Symbol.iterator]: function* () {
for (let element of iterable) {
if (!!fn(element)) yield element;
}
}
});
```
