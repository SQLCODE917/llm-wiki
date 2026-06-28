---
page_id: javascriptallonge-expression
page_kind: concept
summary: Expression: 23 statement(s) and 25 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-expression@9180d0e66f04be211d7a7ecb057f3db0
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
- The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- It’s a simple representation of an expression to be computed. _(javascriptallonge.pdf (source-range-83ecb080-00897))_
- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. _(javascriptallonge.pdf (source-range-83ecb080-01119))_
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-83ecb080-01299))_
- Expressions can be used for keys as well. _(javascriptallonge.pdf (source-range-83ecb080-01609))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02415))_
- This expression begins with a stack containing 30 elements. _(javascriptallonge.pdf (source-range-83ecb080-02788))_
- To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-83ecb080-03104))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00168))_

> All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00170))_

> And if we hand over the espresso, we get the espresso right back.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00205))_

> An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00206))_

> [2-1, 2, 2+1] [1, 1+1, 1+1+1]

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00240, source-range-83ecb080-00242))_

> In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the nam

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00241))_

> 2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00262))_

> What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00263))_

> > 16 The simplest possible function is () => {}, we’ll see that later.

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00349, source-range-83ecb080-00351))_

> There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00350))_

> () => { 2 + 2 } () => { 1 + 1; 2 + 2 }

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00354))_

> (() => { 2 + 2 })() _//=> undefined_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00355))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00353))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00356))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00364))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00362))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00364))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00365))_

> (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00366, source-range-83ecb080-00368))_

> And also: The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00367))_

> (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00548))_

> In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00549))_

> ((PI) => _// ????_ )(3.14159265)

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00561, source-range-83ecb080-00563))_

> There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: It produces the same result as our previous expressions for a diameter-calculating function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00562))_

> (diameter) => ((PI) => diameter * PI)(3.14159265)

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00602))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00604))_

> This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with ().

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00627, source-range-83ecb080-00632))_

> It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. We can use any expression in there, and that expression can invoke diameter_fn. For example: This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where dia

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00630))_

> ((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00655, source-range-83ecb080-00657))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the “outer” environment? Let’s rewrite things slightly differently: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00656))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01119))_

> The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01120))_

> **const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01609))_

> Expressions can be used for keys as well. The syntax is to enclose the key’s expression in [ and ]:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01610))_

> { ["p" + "i"]: 3.14159265 } _//=> {"pi":3.14159265}_

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02328))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02326))_

> `foobar` _//=> 'foobar'_

### Technical atom 20

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02328))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02327))_

> `fizz` + `buzz` _//=> 'fizzbuzz'_

### Technical atom 21

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02329, source-range-83ecb080-02332))_

> For example: A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02330))_

> - `A popular number for nerds is **${** 40 + 2 **}** `

### Technical atom 22

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02338))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02336))_

> - 'A popular number for nerds is ' + (40 + 2)

### Technical atom 23

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02338))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02339))_

> - 'A popular number for nerds is' + (40 + 2)

### Technical atom 24

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02781))_

> Both expressions evaluate to 220. And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02783))_

> When working with very large collections and many operations, this can be important.

### Technical atom 25

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02781))_

> Both expressions evaluate to 220. And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02784))_

> The effect is even more pronounced when we use methods like first, until, or take:


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-quasi-literal]] - shared statements and technical atoms (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-warm-cup-string]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-second]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms (5 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms (4 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-environment]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements (1 shared statement(s))
- [[javascriptallonge-method]] - shared statements (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
