---
page_id: javascriptallonge-section-the-function-keyword-6b28f876
page_kind: source
summary: **the function keyword**: 28 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-function-keyword-6b28f876@84cb5c233c469b68955106a2b5731bf7
---

# **the function keyword**

From [[javascriptallonge]].

## Statements

- JavaScript _does_ have a syntax for naming a function, we use the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00698))_
- Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-83ecb080-00698))_
- Something else we’re about to discuss is optional. _(javascriptallonge.pdf (source-range-83ecb080-00705))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-83ecb080-00706))_
- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-83ecb080-00707))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-83ecb080-00708))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-83ecb080-00708))_
- While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- That may seem confusing, but think of the binding names as properties of the environment, not of the function. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- This is a _named function expression_ . _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- In this expression, double is the name in the environment, but repeat is the function’s actual name. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- > 33“Yes of course?” Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-83ecb080-00725))_
- Now, the function’s actual name has no effect on the environment in which it is used. _(javascriptallonge.pdf (source-range-83ecb080-00729))_
- So “actualName” isn’t bound in the environment where we use the named function expression. _(javascriptallonge.pdf (source-range-83ecb080-00733))_
- Here’s a function that determines whether a positive integer is even or not. _(javascriptallonge.pdf (source-range-83ecb080-00733))_
- Clearly, the name even is bound to the function _within the function’s body_ . _(javascriptallonge.pdf (source-range-83ecb080-00735))_
- This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don’t _need_ to name it anywhere else, you needn’t. _(javascriptallonge.pdf (source-range-83ecb080-00740))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-83ecb080-00740))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-83ecb080-00740))_

## Technical atoms

> Context: Here’s our repeat function written using a “fat arrow”
_(context: javascriptallonge.pdf (source-range-83ecb080-00699))_

> (str) => str + str
_(source: javascriptallonge.pdf (source-range-83ecb080-00700))_

> We always use a block, we cannot write function (str) str + str.
_(source: javascriptallonge.pdf (source-range-83ecb080-00708))_

> Context: 5. We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword
_(context: javascriptallonge.pdf (source-range-83ecb080-00708))_

> If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.
_(source: javascriptallonge.pdf (source-range-83ecb080-00709))_

> Context: If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.
_(context: javascriptallonge.pdf (source-range-83ecb080-00709))_

> (n) => (1.618**n - -1.618**-n) / 2.236
_(source: javascriptallonge.pdf (source-range-83ecb080-00710))_

> Context: Here are our example functions written with names:
_(context: javascriptallonge.pdf (source-range-83ecb080-00716))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:
_(source: javascriptallonge.pdf (source-range-83ecb080-00718))_

> Context: Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00718))_

> **const double** = **function** repeat (str) { **return** str + str; }
_(source: javascriptallonge.pdf (source-range-83ecb080-00719))_

> Context: Now, the function’s actual name has no effect on the environment in which it is used. To whit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00729))_

> **const** bindingName = **function** actualName () { _//..._
_(source: javascriptallonge.pdf (source-range-83ecb080-00730))_

> Context: Now, the function’s actual name has no effect on the environment in which it is used. To whit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00729))_

> }; bindingName _//=> [Function: actualName]_
_(source: javascriptallonge.pdf (source-range-83ecb080-00731))_

> Context: Now, the function’s actual name has no effect on the environment in which it is used. To whit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00729))_

> actualName _//=> ReferenceError: actualName is not defined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00732))_
