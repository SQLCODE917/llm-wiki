---
page_id: closures-and-scope
page_kind: source
summary: Chapter on closures and scope in JavaScriptAllonge.
sources: raw/javascriptallonge.pdf p.44-48
updated: 2026-06-19
---

## Closures and Scope

It's time to see how a function within a function works:

- ((x) => (y) => x)(1)(2) _//=> 1_

First off, let's use what we learned above. Given ( _some function_ )( _some argument_ ), we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function's expression. So we do that first with this code:

## ((x) => (y) => x)(1)

- _//=> [Function]_

The environment belonging to the function with signature (x) => ... becomes {x: 1, ...}, and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ...'s body is:

## (y) => x

So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2, something like this:

- ((y) => x)(2)

So we seem to get a new environment {y: 2, ...}. How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else.

This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from "outside" of a function that are referenced inside a function. For example, here's the equivalent code in Ruby:

lambda { |x| lambda { |y| x } }[1][2] _#=> 1_

Now let's enjoy a relaxed Allongé before we continue!

## if functions without free variables are pure, are closures impure?

The function (y) => x is interesting. It contains a _free variable_, x.[27] A free variable is one that is not bound within the function. Up to now, we've only seen one way to "bind" a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn't have an argument named x, the variable x isn't bound in this function, which makes it "free."

Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without:

- Functions containing no free variables are called _pure functions_.

- Functions containing one or more free variables are called _closures_.

Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen:

## () => {}

## (x) => x

- (x) => (y) => x

The first function doesn't have any variables, therefore doesn't have any free variables. The second doesn't have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn't have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => ....

From this, we learn something: A pure function can contain a closure.

![Kestrel Combinator](harness/cache/c98ab3e62b35ab0f/images/javascriptallonge.pdf-0045-13.jpg)

If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible. Pure functions always mean the same thing because all of their "inputs" are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x.

27You may also hear the term "non-local variable." Both are correct.

## it's always the environment

To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let's fill in the blanks!

The environment for ((y) => x)(2) is _actually_ {y: 2, '..': {x: 1, ...}}. '..' means something like "parent" or "enclosure" or "super-environment." It's (x) => ...'s environment, because the function (y) => x is within (x) => ...'s body. So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

And now you can guess how we evaluate ((y) => x)(2) in the environment {y: 2, '..': {x: 1, ...}}. The variable x isn't in (y) => ...'s immediate environment, but it is in its parent's environment, so it evaluates to 1 and that's what ((y) => x)(2) returns even though it ended up ignoring its own argument.

(x) => x is called the I Combinator, or the _Identity Function_. (x) => (y) => x is called the K Combinator, or _Kestrel_. Some people get so excited by this that they write entire books about them, some are great _[a]_, some–how shall I put this–are interesting _[b]_ if you use Ruby.

> _a_ http://www.amzn.com/0192801422?tag=raganwald001-20

> _b_ https://leanpub.com/combinators

Functions can have grandparents too:

(x) => (y) => (z) => x + y + z

This function does much the same thing as:

(x, y, z) => x + y + z

Only you call it with (1)(2)(3) instead of (1, 2, 3). The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3).

The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

> _a_ https://en.wikipedia.org/wiki/Currying

> _b_ https://en.wikipedia.org/wiki/Partial_application

## shadowy variables from a shadowy planet

An interesting thing happens when a variable has the same name as an ancestor environment's variable. Consider:

- (x) => (x, y) => x + y

The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

(x) => (x, y) => (w, z) => (w) => x + y + z

When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both ws. When a variable has the same name as an ancestor environment's binding, it is said to _shadow_ the ancestor.

This is often a good thing.

## which came first, the chicken or the egg?

This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state.

But before we do so, there's one final question: Where does the ancestry start? If there's no other code in a file, what is (x) => x's parent environment?

JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.

Sometimes, programmers wish to avoid this. If you don't want your code to operate directly within the global environment, what can you do? Create an environment for them, of course. Many programmers choose to write every JavaScript file like this:

_// top of the file_

(() => {

_// ... lots of JavaScript ..._

})(); 

_// bottom of the file_

The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': _global environment_ }}. As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.
