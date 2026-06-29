---
page_id: javascriptallonge-section-a-balanced-statement-about-combinators-85a0e2e7
page_kind: source
summary: a balanced statement about combinators: 10 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-balanced-statement-about-combinators-85a0e2e7@c15e3ffc12dfd92500e3e4e88242c08b
---

# a balanced statement about combinators

From [[javascriptallonge]].

## Statements

- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf , addOne , and compose ) while avoiding language keywords and the names of nouns (like number ). So one perspective is that combinators are useful when you want to emphasize what you're doing and how it fits together, and more explicit code is useful when you want to emphasize what you're working with. _(javascriptallonge.pdf (source-range-8eb13d6b-00570))_
- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either: _(javascriptallonge.pdf (source-range-8eb13d6b-00573))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-8eb13d6b-00579))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-8eb13d6b-00579))_

## Technical atoms

### Technical frame 1: a balanced statement about combinators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00573))_

> So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00572))_

```
const not = (fn) => (x) => !fn(x)
```

### Technical frame 2: a balanced statement about combinators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00579))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00574))_

```
const something = (x) => x != null ;
```

### Technical frame 3: a balanced statement about combinators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00579))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00576))_

```
const nothing = (x) => !something(x);
```

### Technical frame 4: a balanced statement about combinators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00579))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00578))_

```
const nothing = not(something);
```

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00571))_

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
