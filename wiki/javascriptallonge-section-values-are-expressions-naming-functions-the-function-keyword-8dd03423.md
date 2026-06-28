---
page_id: javascriptallonge-section-values-are-expressions-naming-functions-the-function-keyword-8dd03423
page_kind: source
summary: values are expressions / Naming Functions / the function keyword: 16 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-naming-functions-the-function-keyword-8dd03423@21b6de1cf5a195358f6ed957ee80ef6e
---

# values are expressions / Naming Functions / the function keyword

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-naming-functions-b33e71f9]] - broader source section
- [[javascriptallonge-function-keyword]] - topic hub
- [[javascriptallonge-section-values-are-expressions-magic-names-the-function-keyword-7c5583f4]] - same source heading

## Statements

- JavaScript _does_ have a syntax for naming a function, we use the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00521))_
- Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-83ecb080-00521))_
- Something else we’re about to discuss is optional. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-83ecb080-00525))_
- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-83ecb080-00526))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-83ecb080-00527))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-83ecb080-00527))_
- > 33“Yes of course?” Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-83ecb080-00537))_
- Here’s a function that determines whether a positive integer is even or not. _(javascriptallonge.pdf (source-range-83ecb080-00540))_
- Now, the function’s actual name has no effect on the environment in which it is used. _(javascriptallonge.pdf (source-range-83ecb080-00540))_
- Clearly, the name even is bound to the function _within the function’s body_ . _(javascriptallonge.pdf (source-range-83ecb080-00542))_
- This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don’t _need_ to name it anywhere else, you needn’t. _(javascriptallonge.pdf (source-range-83ecb080-00544))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00527))_

> We always use a block, we cannot write function (str) str + str.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00527))_

> 5. We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00528))_

> If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00528))_

> If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00529))_

> (n) => (1.618**n - -1.618**-n) / 2.236

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00530))_

> Can be written as:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00533))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write: **const double** = **function** repeat (str) { **return** str + str; } In this expression, double is the name in the environment, but repeat is the function’s actual name. This is a _named function expression_ . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.
