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

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Compound interest adds interest to principal and then calculates future interest on the updated total. | "Compound interest means interest is added to the principal, and then future interest is calculated on the new total." | `normalized:L3` | [Compound Interest Notes](../sources/compound-interest.md) |
| The source gives the standard compound interest formula for calculating final amount. | "Formula: A = P(1 + r/n)^(nt)" | `normalized:L5-L6` | [Compound Interest Notes](../sources/compound-interest.md) |
| Compound interest applies to finance, savings accounts, loans, and investing. | "Used in finance, savings accounts, loans, and investing." | `normalized:L8` | [Compound Interest Notes](../sources/compound-interest.md) |

Formula terms:

- `P` = principal
- `r` = annual interest rate
- `n` = compounds per year
- `t` = years

## Executable implementation

- [TypeScript](../../packages/concepts/src/compoundInterest.ts)
- [Tests](../../packages/concepts/tests/compoundInterest.test.ts)

## Source pages

- [Compound Interest Notes](../sources/compound-interest.md)
