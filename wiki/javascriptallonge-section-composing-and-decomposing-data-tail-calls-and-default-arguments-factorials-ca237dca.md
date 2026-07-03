---
page_id: javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-factorials-ca237dca
page_kind: source
page_family: section-reference
summary: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials: 9 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-factorials-ca237dca@8bb1f808e9e8d98877d27115ac24f068
---

# Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-e2a54ac1]] - broader source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)

## Statements

- In mathematics, the factorial of a non-negative integer n , denoted by n! , is the product of all positive integers less than or equal to n . For example: _(javascriptallonge.pdf (source-range-7239e085-00989))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done: _(javascriptallonge.pdf (source-range-7239e085-00994))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00994))_

> Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00990))_

<a id="atom-technical-atom-14dcd70f2adfcb00"></a>

```
5! = 5
x
4
x
3
x
2
x
1 = 120.
```

### Technical frame 2: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00994))_

> Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00992))_

<a id="atom-technical-atom-2b5a4752af84217f"></a>

```
const factorial = (n) =>
n == 1
? n
: n * factorial(n - 1);
factorial(1)
//=> 1
factorial(5)
//=> 120
```

### Technical frame 3: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00999))_

> Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00995))_

<a id="atom-technical-atom-dac620c9ed32ea69"></a>

```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```
