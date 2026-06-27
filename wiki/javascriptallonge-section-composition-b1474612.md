---
page_id: javascriptallonge-section-composition-b1474612
page_kind: source
summary: **composition**: 18 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composition-b1474612@6ad26a3b7097eb4dca9fe5d6d8809185
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

> **const** cookAndEat = (food) => eat(cook(food));
_(source: javascriptallonge.pdf (source-range-83ecb080-00827))_

> Context: It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:
_(context: javascriptallonge.pdf (source-range-83ecb080-00828))_

> **const** compose = (a, b) => (c) => a(b(c));
_(source: javascriptallonge.pdf (source-range-83ecb080-00829))_

> Context: It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:
_(context: javascriptallonge.pdf (source-range-83ecb080-00828))_

> **const** cookAndEat = compose(eat, cook);
_(source: javascriptallonge.pdf (source-range-83ecb080-00830))_

> Context: It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:
_(context: javascriptallonge.pdf (source-range-83ecb080-00828))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.
_(source: javascriptallonge.pdf (source-range-83ecb080-00831))_

> Context: If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.
_(context: javascriptallonge.pdf (source-range-83ecb080-00831))_

> Of course, you needn’t use combinators to implement either of these ideas, you can use if statements.
_(source: javascriptallonge.pdf (source-range-83ecb080-00833))_

> Context: Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00833))_

> - **const** actuallyTransfer= (from, to, amount) => _// do something_
_(source: javascriptallonge.pdf (source-range-83ecb080-00834))_

> Context: Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00833))_

> **const** invokeTransfer = once(maybe(actuallyTransfer(...)));
_(source: javascriptallonge.pdf (source-range-83ecb080-00835))_
