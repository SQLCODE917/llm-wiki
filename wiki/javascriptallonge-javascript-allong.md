---
page_id: javascriptallonge-javascript-allong
page_kind: concept
page_family: topic-concept
summary: Javascript Allong: 3 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript-allong@1dd295f3d28479c3b403c25fa98a2c82
---

# Javascript Allong

What [[javascriptallonge]] covers about javascript allong:

## Statements

### A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

- JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions. _(javascriptallonge.pdf (source-range-7239e085-00052))_

- But while JavaScript Allongé attempts to be provocative, it is not prescriptive . There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-7239e085-00054))_

- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. _(javascriptallonge.pdf (source-range-7239e085-00063))_


## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00062))_

> Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. The use of source-code control systems with integrated diffing rewards making certain types of focused changes. The use of linters 1 makes checking for certain types of undesirable code very cheap. Debuggers encourage the use of functions with explicit or implicit names. Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation o

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00058))_

<a id="atom-technical-atom-86e655121c91ba7a"></a>

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

### Technical frame 2: A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00062))_

> Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. The use of source-code control systems with integrated diffing rewards making certain types of focused changes. The use of linters 1 makes checking for certain types of undesirable code very cheap. Debuggers encourage the use of functions with explicit or implicit names. Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation o

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00060))_

<a id="atom-technical-atom-cc0500110141510a"></a>

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


## Related pages

### Source structure

- [[javascriptallonge-section-a-pull-of-the-lever-prefaces-about-javascript-allong-21ea31b9]] - source section: A Pull of the Lever: Prefaces / About JavaScript Allongé shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of b ... [truncated]; A Pull of the Lever: Prefaces / About JavaScript Allongé shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé: If those terms seem unfamiliar, don't worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter. (27 shared statement(s), 7 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-software]] - shared technical atoms: Software shares technical record from A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.: const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function* () { for (let element of iterable) { yield fn(element); } } }); (1 shared atom(s))

### Topics

- [[javascriptallonge-allong]] - broader topic: Allong shares source evidence from A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.: JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so ... [truncated] (3 shared statement(s))
- [[javascriptallonge-javascript]] - broader topic: Javascript shares source evidence from A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.: JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so ... [truncated] (3 shared statement(s))

## Source

- [[javascriptallonge]]
