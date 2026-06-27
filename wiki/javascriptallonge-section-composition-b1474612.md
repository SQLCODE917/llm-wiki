---
page_id: javascriptallonge-section-composition-b1474612
page_kind: source
summary: **composition**: 18 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composition-b1474612@9c16225bf9ed09861a51d084df113f4f
---

# **composition**

From [[javascriptallonge]].

## Statements

- You can compose them with explicit JavaScript code as we’ve just done. _(javascriptallonge.pdf (source-range-83ecb080-00828))_
- It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. _(javascriptallonge.pdf (source-range-83ecb080-00828))_
- If that was all there was to it, composition wouldn’t matter much. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Once is useful for ensuring that certain side effects are not repeated. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Thereafter, it does nothing. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-83ecb080-00833))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00827))_

> **const** cookAndEat = (food) => eat(cook(food));

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00828))_

> It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00829))_

> **const** compose = (a, b) => (c) => a(b(c));

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00828))_

> It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00830))_

> **const** cookAndEat = compose(eat, cook);

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00828))_

> It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00831))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00831))_

> If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00833))_

> Of course, you needn’t use combinators to implement either of these ideas, you can use if statements.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00833))_

> Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00834))_

> - **const** actuallyTransfer= (from, to, amount) => _// do something_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00833))_

> Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00835))_

> **const** invokeTransfer = once(maybe(actuallyTransfer(...)));
