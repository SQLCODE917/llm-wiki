---
page_id: javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-factorials-ca237dca
page_kind: source
summary: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials: 10 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-factorials-ca237dca@9cf98a2bf904d486a5f48f62579efcfb
---

# Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-e2a54ac1]] - broader source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)

## Statements

- In mathematics, the factorial of a non-negative integer n , denoted by n! , is the product of all positive integers less than or equal to n . For example: _(javascriptallonge.pdf (source-range-7239e085-00989))_
- While this is mathematically elegant, it is computational filigree 63 . _(javascriptallonge.pdf (source-range-7239e085-00993))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done: _(javascriptallonge.pdf (source-range-7239e085-00994))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00993))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00990))_

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

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00993))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00992))_

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

```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```

### Technical frame 4: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00999))_

> Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00998))_

```
const callLast = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const factorial = callLast(factorialWithDelayedWork, 1);
factorial(1)
//=> 1
factorial(5)
//=> 120
```
