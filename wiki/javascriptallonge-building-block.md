---
page_id: javascriptallonge-building-block
page_kind: concept
summary: Building Blocks: 24 statement(s) and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-building-block@a3556eff9d2db8e281d2767760fc0c38
---

# Building Blocks

What [[javascriptallonge]] covers about building blocks:

## Statements

- Another basic building block is _partial application_ . _(javascriptallonge.pdf (source-range-83ecb080-00839))_
- Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- The weakness is that you will. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- There are ifs, fors, returns, everything thrown higgledy piggledy together. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- The strength of JavaScript is that you can do anything. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- You can compose them with explicit JavaScript code as we’ve just done. _(javascriptallonge.pdf (source-range-83ecb080-00828))_
- It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. _(javascriptallonge.pdf (source-range-83ecb080-00828))_
- If that was all there was to it, composition wouldn’t matter much. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Once is useful for ensuring that certain side effects are not repeated. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Thereafter, it does nothing. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
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


## Source

- [[javascriptallonge]]
