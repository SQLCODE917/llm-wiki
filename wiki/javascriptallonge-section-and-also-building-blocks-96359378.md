---
page_id: javascriptallonge-section-and-also-building-blocks-96359378
page_kind: source
summary: And also: / Building Blocks: 31 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-building-blocks-96359378@a46dcb603f7e7aa1c0b1a585da4fe03a
---

# And also: / Building Blocks

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-3f50274e]] - broader source section: And also:
- [[javascriptallonge-section-and-also-building-blocks-composition-b915cf07]] - narrower source section: And also: / Building Blocks / composition
- [[javascriptallonge-section-and-also-building-blocks-partial-application-a5e51d71]] - narrower source section: And also: / Building Blocks / partial application

## Statements

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-7239e085-00580))_

## Statements by subsection

### And also: / Building Blocks / composition

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators: _(javascriptallonge.pdf (source-range-7239e085-00584))_
- If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. _(javascriptallonge.pdf (source-range-7239e085-00586))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-7239e085-00587))_
- Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-7239e085-00588))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-7239e085-00586))_

### And also: / Building Blocks / partial application

- Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-7239e085-00591))_
- Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-7239e085-00592))_
- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-7239e085-00597))_
- We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-7239e085-00599))_
- Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe. _(javascriptallonge.pdf (source-range-7239e085-00603))_

## Technical atoms

### Technical frame 1: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00584))_

> It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00583))_

```
const cookAndEat = (food) => eat(cook(food));
```

### Technical frame 2: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00586))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00585))_

```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Technical frame 3: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00587))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00586))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical frame 4: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00587))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00588))_

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements.

### Technical frame 5: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00588))_

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00589))_

```
const actuallyTransfer= (from, to, amount) =>
// do something
const invokeTransfer = once(maybe(actuallyTransfer(...)));
```

### Technical frame 6: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00593))_

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 7: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00596))_

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 8: And also: / Building Blocks / partial application

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

### Technical frame 9: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00601))_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 10: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00602))_

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```
