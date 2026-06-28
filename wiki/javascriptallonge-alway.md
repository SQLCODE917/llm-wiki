---
page_id: javascriptallonge-alway
page_kind: concept
summary: Alway: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-alway@20bb567d99bd5bbd5561e734720dded2
---

# Alway

What [[javascriptallonge]] covers about alway:

## Statements

### Closures and Scope

- The first sip: Basic Functions

22

## **if functions without free variables are pure, are closures impure?**

The function (y) => x is interesting. It contains a _free variable_ , x.[27] A free variable is one that is not bound within the function. Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn’t have an argument named x, the variable x isn’t bound in this function, which makes it “free.” Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without:

- Functions containing no free variables are called _pure functions_ .

- Functions containing one or more free variables are called _closures_ .

Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen:

## () => {}

## (x) => x

- (x) => (y) => x

The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => ....

From this, we learn something: A pure function can contain a closure.

**==> picture [29 x 30] intentionally omitted <==**

If pure functions can contain closures, can a closure contain a pure function? Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. If you can’t, give your reasoning for why it’s impossible.

Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.

27You may also hear the term “non-local variable.” Both are correct. _(javascriptallonge.pdf (source-range-83ecb080-00057))_

- The first sip: Basic Functions

25

JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.

Sometimes, programmers wish to avoid this. If you don’t want your code to operate directly within the global environment, what can you do? Create an environment for them, of course. Many programmers choose to write every JavaScript file like this:

_// top of the file_ (() => { _// ... lots of JavaScript ..._ })();

_// bottom of the file_

The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': _global environment_ }}. As we’ll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-83ecb080-00060))_

### That Constant Coffee Craving

- The first sip: Basic Functions

37 })(2) _//=> 6.2831853_

Ah! const statements don’t just shadow values bound within the environments created by functions, they shadow values bound within environments created by blocks!

This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: ((diameter) => { **const** PI = 3.14159265; **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_

If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:” ((diameter) => { **if** ( **true** ) { **const** PI = 3.14159265; } **return** diameter * PI; })(2) _//=> would return 6.2831853 if const had function scope_ Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not “leaking” its binding to other parts of the code that do not need to interact with it.

## **rebinding**

By default, JavaScript permits us to _rebind_ new values to names bound with a parameter. For example, we can write:

> 32https://en.wikipedia.org/wiki/Principle_of_least_privilege _(javascriptallonge.pdf (source-range-83ecb080-00073))_

### Summary

- The first sip: Basic Functions

55

## **Summary**

**==> picture [29 x 29] intentionally omitted <==**

## **Functions**

- Functions are values that can be part of expressions, returned from other functions, and so forth.

- Functions are _reference values_ .

- Functions are applied to arguments.

- The arguments are passed by sharing, which is also called “pass by value.” - Fat arrow functions have expressions or blocks as their bodies.

- function keyword functions always have blocks as their bodies.

- Function bodies have zero or more statements.

- Expression bodies evaluate to the value of the expression.

- Block bodies evaluate to whatever is returned with the return keyword, or to undefined.

- JavaScript uses const to bind values to names within block scope.

- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are “hoisted.” - Function application creates a scope.

- Blocks also create scopes if const statements are within them.

- Scopes are nested and free variable references closed over.

- Variables can shadow variables in an enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

104

Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious.[64] The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend.

We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

**Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded.

So here’s a question: If this is such a slow approach, why do some examples of “functional” algorithms work this exact way?

> 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-00153))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated] (2 shared statement(s))
- [[javascriptallonge-bound]] - shared statements: Bound shares source evidence from That Constant Coffee Craving: The first sip: Basic Functions  37 })(2) _//=> 6.2831853_  Ah! const statements don’t just shadow values bound within the environments created by functions, they sha ... [truncated] (1 shared statement(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from That Constant Coffee Craving: The first sip: Basic Functions  37 })(2) _//=> 6.2831853_  Ah! const statements don’t just shadow values bound within the environments created by functions, they sha ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Closures and Scope: The first sip: Basic Functions  25  JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things ... [truncated] (1 shared statement(s))
- [[javascriptallonge-needn]] - shared statements: Needn shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  104  Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious. ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pure]] - shared statements: Pure shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated] (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from That Constant Coffee Craving: The first sip: Basic Functions  37 })(2) _//=> 6.2831853_  Ah! const statements don’t just shadow values bound within the environments created by functions, they sha ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
