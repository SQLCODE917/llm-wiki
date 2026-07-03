---
page_id: javascriptallonge-recipe-interactive-generators
page_kind: recipe
page_family: recipe-pattern
summary: interactive generators: reusable source-backed pattern with 6 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: interactive-generators
projection_coverage: recipe-javascriptallonge-recipe-interactive-generators@4f852caf3dbbe6c80477b116eea13db6
---

# interactive generators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-get-interactive-generators-6808178d]].
- Evidence roles: decision, constraint, procedure, explanation, example.

## Applicability And Rationale

- If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-7239e085-01938))_
- So far, we have called iterators (and generators) with .next() . _(javascriptallonge.pdf (source-range-7239e085-01938))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-7239e085-01941))_
- It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-7239e085-01942))_
- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-7239e085-01943))_
- And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-7239e085-01943))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01940)_

```
function* generatorNaughtsAndCrosses () {
const x1 = yield 0;
switch (x1) {
case 1:
const x2 = yield 6;
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
yield 3;
break;
case 3:
const x3 = yield 8;
switch (x3) {
case 2:
case 5:
case 7:
yield 4;
break;
case 4:
yield 7;
break;
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-get-interactive-generators-6808178d]]
