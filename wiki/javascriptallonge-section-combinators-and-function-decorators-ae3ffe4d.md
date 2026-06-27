---
page_id: javascriptallonge-section-combinators-and-function-decorators-ae3ffe4d
page_kind: source
summary: Combinators and Function Decorators: 32 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-combinators-and-function-decorators-ae3ffe4d@c92705a528a95719542cd90f2e487c57
---

# Combinators and Function Decorators

From [[javascriptallonge]].

## Statements

- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- But before we go on, we’ll talk about some specific types of higher-order functions. _(javascriptallonge.pdf (source-range-83ecb080-00784))_
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
- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf, addOne, and compose) while avoiding language keywords and the names of nouns (like number). _(javascriptallonge.pdf (source-range-83ecb080-00805))_
- So one perspective is that combinators are useful when you want to emphasize what you’re doing and how it fits together, and more explicit code is useful when you want to emphasize what you’re working with. _(javascriptallonge.pdf (source-range-83ecb080-00805))_
- A _function decorator_ is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. _(javascriptallonge.pdf (source-range-83ecb080-00807))_
- > 37As we’ll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. _(javascriptallonge.pdf (source-range-83ecb080-00808))_
- > 38 We’ll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) _(javascriptallonge.pdf (source-range-83ecb080-00809))_
- So instead of writing !someFunction(42), we can write not(someFunction)(42). _(javascriptallonge.pdf (source-range-83ecb080-00813))_
- Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00819))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. _(javascriptallonge.pdf (source-range-83ecb080-00819))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. _(javascriptallonge.pdf (source-range-83ecb080-00819))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00794))_

> Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00795))_

> - **const** compose = (a, b) => (c) => a(b(c))

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00797))_

> **const** addOne = (number) => number + 1;

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00798))_

> **const** doubleOf = (number) => number * 2;

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00800))_

> **const** doubleOfAddOne = (number) => doubleOf(addOne(number));

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00801))_

> You could also write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00802))_

> **const** doubleOfAddOne = compose(doubleOf, addOne);

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00812))_

> **const** not = (fn) => (x) => !fn(x)

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00813))_

> So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress. But like compose, we could write either:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00814))_

> **const** something = (x) => x != **null** ;

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00815))_

> And elsewhere, write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00816))_

> **const** nothing = (x) => !something(x);

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00817, source-range-83ecb080-00819))_

> Or we could write: not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. You’ll see other function decorators in the recipes, like once and maybe. Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00818))_

> **const** nothing = not(something);
