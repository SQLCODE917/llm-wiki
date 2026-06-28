---
page_id: javascriptallonge-section-composition-9e6eae84
page_kind: source
summary: composition: 13 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composition-9e6eae84@72f71c37d3ea7b7457550b4e9fa74590
---

# composition

From [[javascriptallonge]].

## Statements

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators: _(javascriptallonge.pdf (source-range-31a4cf47-00585))_
- If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. _(javascriptallonge.pdf (source-range-31a4cf47-00587))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-31a4cf47-00588))_
- Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-31a4cf47-00589))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-31a4cf47-00587))_

## Technical atoms

### Technical frame 1: composition

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00585))_

> It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00584))_

```
const cookAndEat = (food) => eat(cook(food));
```

### Technical frame 2: composition

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00587))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00586))_

```
const compose = (a, b) => (c) => a(b(c)); const cookAndEat = compose(eat, cook);
```

### Technical frame 3: composition

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00588))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00587))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical frame 4: composition

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00588))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00589))_

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements.

### Technical frame 5: composition

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00589))_

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00590))_

```
const actuallyTransfer= (from, to, amount) => // do something const invokeTransfer = once(maybe(actuallyTransfer(...)));
```
