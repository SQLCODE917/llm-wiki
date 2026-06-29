---
page_id: javascriptallonge-development
page_kind: concept
summary: Development: 5 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-development@f66edfe0091c91874ca055634524e3d9
---

# Development

What [[javascriptallonge]] covers about development:

## Statements

### What JavaScript Allongé is. And isn't.

- Software development is a complex field. Choices in development are often driven by social considerations. People often say that software should be written for people to read. Doesn't that depend upon the people in question? Should code written by a small team of specialists use the same techniques and patterns as code maintained by a continuously changing cast of inexperienced interns? _(javascriptallonge.pdf (source-range-8eb13d6b-00055))_

- Choices in software development are also often driven by requirements specific to the type of software being developed. For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-8eb13d6b-00056))_

- Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this: _(javascriptallonge.pdf (source-range-8eb13d6b-00057))_

- Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. The use of source-code control systems with integrated diffing rewards making certain types of focused changes. The use of linters 1 makes checking for certain types of undesirable code very cheap. Debuggers encourage the use of functions with explicit or implicit names. Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites. _(javascriptallonge.pdf (source-range-8eb13d6b-00062))_


## Technical atoms

### Technical frame 1: What JavaScript Allongé is. And isn't.

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00059))_

> Then it can be jarring to add new helpers written that place the verb first, like this:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00058))_

```
const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } });
```


## Related pages

- [[javascriptallonge-software]] - shared statements and technical atoms: Software shares source evidence from What JavaScript Allongé is. And isn't.: Software development is a complex field. Choices in development are often driven by social considerations. People often say that software should be written for peopl ... [truncated]; Software shares technical record from What JavaScript Allongé is. And isn't.: const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } }); (4 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from What JavaScript Allongé is. And isn't.: const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } }); (1 shared atom(s))

## Source

- [[javascriptallonge]]
