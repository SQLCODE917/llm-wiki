---
page_id: javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-913f90c6
page_kind: source
page_family: section-reference
summary: And also: / Combinators and Function Decorators / function decorators: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-913f90c6@75c7cd50d977aaf1475acf13f55276c6
---

# And also: / Combinators and Function Decorators / function decorators

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-c48f42db]] - broader source section: And also: / Combinators and Function Decorators

### Topics

- [[javascriptallonge-function-decorator]] - topic hub: opens the topic page for Function Decorator

## Statements

- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-7239e085-00578))_

## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00578))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00577))_

<a id="atom-technical-atom-16403f5e9983b595"></a>

```
const nothing = not(something);
```

### Technical atom 2

<a id="atom-technical-atom-004428297e1534ac"></a>

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00570))_

```text
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) =>!fn(...args) |

</details>
