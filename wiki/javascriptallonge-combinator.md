---
page_id: javascriptallonge-combinator
page_kind: concept
summary: Combinator: 10 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-combinator@3335f0ef11d3ec0c6ce0212b7200480a
---

# Combinator

What [[javascriptallonge]] covers about combinator:

## Statements

- “A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] _(javascriptallonge.pdf (source-range-83ecb080-00787))_
- We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] . _(javascriptallonge.pdf (source-range-83ecb080-00788))_
- Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation: _(javascriptallonge.pdf (source-range-83ecb080-00794))_
- > 37As we’ll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. _(javascriptallonge.pdf (source-range-83ecb080-00808))_
- If we were learning Combinatorial Logic, we’d start with the most basic combinators like S, K, and I, and work up from there to practical combinators. _(javascriptallonge.pdf (source-range-83ecb080-00788))_
- We won’t be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-83ecb080-00793))_
- While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-83ecb080-00803))_
- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf, addOne, and compose) while avoiding language keywords and the names of nouns (like number). _(javascriptallonge.pdf (source-range-83ecb080-00805))_
- So one perspective is that combinators are useful when you want to emphasize what you’re doing and how it fits together, and more explicit code is useful when you want to emphasize what you’re working with. _(javascriptallonge.pdf (source-range-83ecb080-00805))_
- Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00819))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00794))_

> Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00795))_

> - **const** compose = (a, b) => (c) => a(b(c))

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00817, source-range-83ecb080-00819))_

> Or we could write: not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. You’ll see other function decorators in the recipes, like once and maybe. Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00818))_

> **const** nothing = not(something);


## Related pages

- [[javascriptallonge-program]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-code]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
