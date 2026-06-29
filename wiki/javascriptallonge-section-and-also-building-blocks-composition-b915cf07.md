---
page_id: javascriptallonge-section-and-also-building-blocks-composition-b915cf07
page_kind: source
summary: And also: / Building Blocks / composition: 13 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-building-blocks-composition-b915cf07@75c246961972434f8bb55572d74fbf16
---

# And also: / Building Blocks / composition

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-building-blocks-96359378]] - broader source section: And also: / Building Blocks

## Statements

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators: _(javascriptallonge.pdf (source-range-7239e085-00584))_
- If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. _(javascriptallonge.pdf (source-range-7239e085-00586))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-7239e085-00587))_
- Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-7239e085-00588))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-7239e085-00586))_

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
