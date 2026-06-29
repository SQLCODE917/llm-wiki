---
page_id: javascriptallonge-section-and-also-building-blocks-partial-application-a5e51d71
page_kind: source
summary: And also: / Building Blocks / partial application: 14 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-building-blocks-partial-application-a5e51d71@1718752464615f370005e9e0dc9eed33
---

# And also: / Building Blocks / partial application

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-building-blocks-96359378]] - broader source section: And also: / Building Blocks
- [[javascriptallonge-partial-application]] - topic hub: opens the topic page for Partial Application
- [[javascriptallonge-section-recipes-with-basic-functions-partial-application-583028a8]] - same source heading: another source section with the same heading, Recipes with Basic Functions / Partial Application

## Statements

- Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-7239e085-00591))_
- Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-7239e085-00592))_
- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-7239e085-00597))_
- We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-7239e085-00599))_
- Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe. _(javascriptallonge.pdf (source-range-7239e085-00603))_

## Technical atoms

### Technical frame 1: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00593))_

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 2: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00596))_

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 3: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00599))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00598))_

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Technical frame 4: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00601))_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 5: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00602))_

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00659))_

| entry | content |
| --- | --- |
| 45 | from Michael Fogus, Functional JavaScript |
| 46 | from Oliver Steele and the terse but handy node-ap |
| 47 | from James Halliday. |

<details>
<summary>Raw table text</summary>

```
Partial Application
In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You'll find examples in Lemonad 45 from Michael Fogus, Functional JavaScript 46 from Oliver Steele and the terse but handy node-ap 47 from James Halliday.
```

</details>

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00660))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00663))_

| entry | content |
| --- | --- |
| 45 | https://github.com/fogus/lemonad |
| 46 | http://osteele.com/sources/javascript/functional/ |
| 47 | https://github.com/substack/node-ap 48 |

<details>
<summary>Raw table text</summary>

```
45 https://github.com/fogus/lemonad 46 http://osteele.com/sources/javascript/functional/ 47 https://github.com/substack/node-ap 48
```

</details>
