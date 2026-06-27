---
page_id: javascriptallonge-expression
page_kind: concept
summary: Expression: 23 statement(s) and 20 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-expression@fe371964648276bebdd101ad1b3584ee
---

# Expression

What [[javascriptallonge]] covers about expression:

## Statements

- For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00881))_
- The x in the expression that we call a “variable” is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-83ecb080-01159))_
- An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and operators[87] _(javascriptallonge.pdf (source-range-83ecb080-02319))_
- > 11In some languages, expressions are a kind of value unto themselves and can be manipulated. _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- We saw that an expression consisting solely of numbers, like 42, is a literal. _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- An expression is a JavaScript statement. _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- The expression ‘x’ (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-83ecb080-00448))_
- This expression, when evaluated, returns a function that calculates circumferences. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- In this expression, double is the name in the environment, but repeat is the function’s actual name. _(javascriptallonge.pdf (source-range-83ecb080-00720))_

## Technical atoms

> Context: All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water.
_(context: javascriptallonge.pdf (source-range-83ecb080-00168))_

> And if we hand over the espresso, we get the espresso right back.
_(source: javascriptallonge.pdf (source-range-83ecb080-00170))_

> Context: An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00205))_

> [2-1, 2, 2+1] [1, 1+1, 1+1+1]
_(source: javascriptallonge.pdf (source-range-83ecb080-00206))_

> Context: What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else.
_(context: javascriptallonge.pdf (source-range-83ecb080-00262))_

> > 16 The simplest possible function is () => {}, we’ll see that later.
_(source: javascriptallonge.pdf (source-range-83ecb080-00263))_

> Context: There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:
_(context: javascriptallonge.pdf (source-range-83ecb080-00349, source-range-83ecb080-00351))_

> () => { 2 + 2 } () => { 1 + 1; 2 + 2 }
_(source: javascriptallonge.pdf (source-range-83ecb080-00350))_

> Context: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:
_(context: javascriptallonge.pdf (source-range-83ecb080-00353))_

> (() => { 2 + 2 })() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00354))_

> Context: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:
_(context: javascriptallonge.pdf (source-range-83ecb080-00353))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00355))_


## Source

- [[javascriptallonge]]
