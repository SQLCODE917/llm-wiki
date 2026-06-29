---
page_id: javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-913f90c6
page_kind: source
summary: And also: / Combinators and Function Decorators / function decorators: 8 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-913f90c6@b042d04b0c6d254bc50214f07eab7200
---

# And also: / Combinators and Function Decorators / function decorators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-c48f42db]] - broader source section: And also: / Combinators and Function Decorators
- [[javascriptallonge-function-decorator]] - topic hub: opens the topic page for Function Decorator

## Statements

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either: _(javascriptallonge.pdf (source-range-7239e085-00572))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-7239e085-00578))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-7239e085-00578))_

## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00572))_

> So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00571))_

```
const not = (fn) => (x) => !fn(x)
```

### Technical frame 2: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00578))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00573))_

```
const something = (x) => x != null;
```

### Technical frame 3: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00578))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00575))_

```
const nothing = (x) => !something(x);
```

### Technical frame 4: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00578))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00577))_

```
const nothing = not(something);
```

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00562))_

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

<details>
<summary>Raw table text</summary>

```
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

</details>

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00570))_

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) |

<details>
<summary>Raw table text</summary>

```
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

</details>
