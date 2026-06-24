---
page_id: javascriptallonge-if-functions-without-free-variables-are-pure-are-closures-impure
page_kind: source
summary: if functions without free variables are pure, are closures impure? from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.45-45
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses the distinction between pure functions and closures, focusing on free variables.

## Key supported claims

- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: Functions containing no free variables are called pure functions. (raw/javascriptallonge.pdf p.45-45)
- Functions containing one or more free variables are called closures. (raw/javascriptallonge.pdf p.45-45)
- The second doesn't have any free variables, because its only variable is bound. (raw/javascriptallonge.pdf p.45-45)
- We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x. (raw/javascriptallonge.pdf p.45-45)

## Technical details

### `technical-atom-182b7d333da55239` requirement

Citation: (raw/javascriptallonge.pdf p.45)

They always mean the same thing wherever you use them.

### `technical-atom-13b88e2f8ae6faf9` requirement

Citation: (raw/javascriptallonge.pdf p.45)

Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments.

### `technical-atom-03b34627456d18c0` exception

Citation: (raw/javascriptallonge.pdf p.45)

Up to now, we've only seen one way to 'bind' a variable, namely by passing in an argument with the same name.

### `technical-atom-62b29dbab26e9d26` exception

Citation: (raw/javascriptallonge.pdf p.45)

Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without:

### `technical-atom-8dbe6a3e02aebe8c` exception

Citation: (raw/javascriptallonge.pdf p.45)

The second doesn't have any free variables, because its only variable is bound.

### `technical-atom-42abf56c3c9079e9` exception

Citation: (raw/javascriptallonge.pdf p.45)

, and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ...

### `technical-atom-4188fdbc17cb0805` exception

Citation: (raw/javascriptallonge.pdf p.45)

Using only what we've learned so far, attempt to compose a closure that contains a pure function.

### `technical-atom-af17d347e3c83d79` exception

Citation: (raw/javascriptallonge.pdf p.45)

We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

## Related technical details

### From [[javascriptallonge-a-quick-summary-of-functions-and-bodies]]: `technical-atom-5e2b194ce75f5bf0` exception

Relation: nearby source page; matched terms `any`, `called`, `functions`, `used`

Citation: (raw/javascriptallonge.pdf p.40)

How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure).

### From [[javascriptallonge-iterator-objects]]: `technical-atom-ccb654b6a11d4ba0` procedure

Relation: nearby source page; matched terms `function`, `have`, `method`

Citation: (raw/javascriptallonge.pdf p.209-210)

Instead of having a function that you call to get the next element, you have an object with a .next() method.
