---
page_id: javascriptallonge-section-combinators-14ec3c73
page_kind: source
summary: **combinators**: 16 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-combinators-14ec3c73@a1ba03847e8a26be9a3e4d1f3ce01923
---

# **combinators**

From [[javascriptallonge]].

## Statements

- “A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] _(javascriptallonge.pdf (source-range-83ecb080-00787))_
- “A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] _(javascriptallonge.pdf (source-range-83ecb080-00787))_
- We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] . _(javascriptallonge.pdf (source-range-83ecb080-00788))_
- If we were learning Combinatorial Logic, we’d start with the most basic combinators like S, K, and I, and work up from there to practical combinators. _(javascriptallonge.pdf (source-range-83ecb080-00788))_
- We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] . _(javascriptallonge.pdf (source-range-83ecb080-00788))_
- We won’t be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-83ecb080-00793))_
- We won’t be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-83ecb080-00793))_
- Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation: _(javascriptallonge.pdf (source-range-83ecb080-00794))_
- This is, of course, just one example of many. _(javascriptallonge.pdf (source-range-83ecb080-00803))_
- While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-83ecb080-00803))_
- While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-83ecb080-00803))_

## Technical atoms

> Context: Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation:
_(context: javascriptallonge.pdf (source-range-83ecb080-00794))_

> - **const** compose = (a, b) => (c) => a(b(c))
_(source: javascriptallonge.pdf (source-range-83ecb080-00795))_

> **const** addOne = (number) => number + 1;
_(source: javascriptallonge.pdf (source-range-83ecb080-00797))_

> **const** doubleOf = (number) => number * 2;
_(source: javascriptallonge.pdf (source-range-83ecb080-00798))_

> **const** doubleOfAddOne = (number) => doubleOf(addOne(number));
_(source: javascriptallonge.pdf (source-range-83ecb080-00800))_

> Context: You could also write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00801))_

> **const** doubleOfAddOne = compose(doubleOf, addOne);
_(source: javascriptallonge.pdf (source-range-83ecb080-00802))_
