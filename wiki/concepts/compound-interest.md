---
title: Compound Interest
type: concept
tags: []
status: draft
last_updated: 2026-05-02
sources: [../sources/compound-interest.md]
---

# Compound Interest

Compound interest is interest calculated on a principal amount after previous interest has been added back into that principal.

## Source-backed details

The source states that compound interest adds interest to principal, then calculates future interest on the new total.

The source gives the formula:

```text
A = P(1 + r/n)^(nt)
```

Where:

- `P` = principal
- `r` = annual interest rate
- `n` = compounds per year
- `t` = years

Compound interest is used in finance, savings accounts, loans, and investing.

## Executable implementation

- [TypeScript](../../packages/concepts/src/compoundInterest.ts)
- [Tests](../../packages/concepts/tests/compoundInterest.test.ts)

## Source pages

- [Compound Interest Notes](../sources/compound-interest.md)
