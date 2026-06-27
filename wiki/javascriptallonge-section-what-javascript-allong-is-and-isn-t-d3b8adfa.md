---
page_id: javascriptallonge-section-what-javascript-allong-is-and-isn-t-d3b8adfa
page_kind: source
summary: **What JavaScript Allongé is. And isn’t.**: 24 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-what-javascript-allong-is-and-isn-t-d3b8adfa@591822a2e909baf41b51b286a9ca63d1
---

# **What JavaScript Allongé is. And isn’t.**

From [[javascriptallonge]].

## Statements

- JavaScript Allongé is a book about programming with functions. _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. _(javascriptallonge.pdf (source-range-83ecb080-00080))_
- The intention is to improve the way we think about programs. _(javascriptallonge.pdf (source-range-83ecb080-00080))_
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-83ecb080-00081))_
- But while JavaScript Allongé attempts to be provocative, it is not _prescriptive_ . _(javascriptallonge.pdf (source-range-83ecb080-00081))_
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-83ecb080-00081))_
- Choices in development are often driven by social considerations. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- Software development is a complex field. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- People often say that software should be written for people to read. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- Choices in software development are also often driven by requirements specific to the type of software being developed. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- If a particular codebase is written with lots of helper functions that place the subject first, like this: _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- Choices in software development must also consider the question of consistency. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- Then it can be jarring to add new helpers written that place the verb first, like this: _(javascriptallonge.pdf (source-range-83ecb080-00088))_
- Then it can be jarring to add new helpers written that place the verb first, like this: _(javascriptallonge.pdf (source-range-83ecb080-00088))_
- Debuggers encourage the use of functions with explicit or implicit names. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- The use of linters[1] makes checking for certain types of undesirable code very cheap. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- The use of source-code control systems with integrated diffing rewards making certain types of focused changes. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking. _(javascriptallonge.pdf (source-range-83ecb080-00092))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking. _(javascriptallonge.pdf (source-range-83ecb080-00092))_

## Technical atoms

> Context: Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00086))_

> **const** mapWith = (iterable, fn) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **yield** fn(element); } } });
_(source: javascriptallonge.pdf (source-range-83ecb080-00087))_
