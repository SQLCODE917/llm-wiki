---
page_id: javascriptallonge-recipe-factorials
page_kind: recipe
page_family: recipe-pattern
summary: factorials: reusable source-backed pattern with 4 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: factorials
projection_coverage: recipe-javascriptallonge-recipe-factorials@8ac7dbc1f4838fada90e64b56034d4d1
---

# factorials

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-factorials-ca237dca]].
- Evidence roles: decision, constraint, procedure, explanation, example.

## Applicability And Rationale

- , is the product of all positive integers less than or equal to n . _(javascriptallonge.pdf (source-range-7239e085-00989))_
- In mathematics, the factorial of a non-negative integer n , denoted by n! _(javascriptallonge.pdf (source-range-7239e085-00989))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . _(javascriptallonge.pdf (source-range-7239e085-00994))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00990)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00992)_

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

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00995)_

```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00998)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-factorials-ca237dca]]
