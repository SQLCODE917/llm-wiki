---
page_id: javascriptallonge-bound
page_kind: concept
summary: Bound: 3 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-bound@62f3df36f5ff2cef6371a5939909cdaa
---

# Bound

What [[javascriptallonge]] covers about bound:

## Statements

### That Constant Coffee Craving

- 30

The first sip: Basic Functions ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_

We can bind any expression. Functions are expressions, so we can bind helper functions: (d) => { **const** calc = (diameter) => { **const** PI = 3.14159265; **return** diameter * PI }; **return** "The circumference is " + calc(d) } Notice calc(d)? This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with (). A name that’s bound to a function is a valid expression evaluating to a function.[30] Amazing how such an important idea–naming functions–can be explained _en passant_ in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as “first class entities.” Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

We can bind more than one name-value pair by separating them with commas. For readability, most people put one binding per line: (d) => { **const** PI = 3.14159265, calc = (diameter) => diameter * PI; **return** "The circumference is " + calc(d) } > 30We’re into the second chapter and we’ve finally named a function. Sheesh. _(javascriptallonge.pdf (source-range-83ecb080-00066))_

- 34

The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => diameter * PI })() ) _//=> 6.2831853_

Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.

## **are consts also from a shadowy planet?**

We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions.

But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block?

We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other.

Let’s start, as above, by doing this with parameters. We’ll start with:

((PI) => (diameter) => diameter * PI )(3.14159265) And gratuitously wrap it in another IIFE so that we can bind PI to something else: _(javascriptallonge.pdf (source-range-83ecb080-00070))_

- The first sip: Basic Functions

37 })(2) _//=> 6.2831853_

Ah! const statements don’t just shadow values bound within the environments created by functions, they shadow values bound within environments created by blocks!

This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: ((diameter) => { **const** PI = 3.14159265; **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_

If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:” ((diameter) => { **if** ( **true** ) { **const** PI = 3.14159265; } **return** diameter * PI; })(2) _//=> would return 6.2831853 if const had function scope_ Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not “leaking” its binding to other parts of the code that do not need to interact with it.

## **rebinding**

By default, JavaScript permits us to _rebind_ new values to names bound with a parameter. For example, we can write:

> 32https://en.wikipedia.org/wiki/Principle_of_least_privilege _(javascriptallonge.pdf (source-range-83ecb080-00073))_


## Related pages

- [[javascriptallonge-const]] - shared statements: Const shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (2 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (2 shared statement(s))
- [[javascriptallonge-alway]] - shared statements: Alway shares source evidence from That Constant Coffee Craving: The first sip: Basic Functions  37 })(2) _//=> 6.2831853_  Ah! const statements don’t just shadow values bound within the environments created by functions, they sha ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from That Constant Coffee Craving: 30  The first sip: Basic Functions ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_  We can bind any expression. Functions ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
