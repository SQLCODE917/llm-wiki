---
page_id: javascriptallonge-section-partial-application-0ab7f284
page_kind: source
summary: partial application: 14 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-partial-application-0ab7f284@aecaf5fd51611d7448c86892899b7273
---

# partial application

From [[javascriptallonge]].

## Statements

- Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-31a4cf47-00592))_
- Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-31a4cf47-00593))_
- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-31a4cf47-00598))_
- We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-31a4cf47-00600))_
- Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe. _(javascriptallonge.pdf (source-range-31a4cf47-00604))_

## Technical atoms

### Technical frame 1: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00598))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00594))_

```
_.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9]
```

### Technical frame 2: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00598))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00597))_

```
const squareAll = (array) => map(array, (n) => n * n);
```

### Technical frame 3: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00600))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00599))_

```
const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9]
```

### Technical frame 4: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00604))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00602))_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 5: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00604))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00603))_

```
safeSquareAll([1, null , 2, 3]) //=> [1, null, 4, 9]
```
