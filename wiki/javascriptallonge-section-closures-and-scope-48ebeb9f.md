---
page_id: javascriptallonge-section-closures-and-scope-48ebeb9f
page_kind: source
summary: Closures and Scope: 65 source-backed entries and 11 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-closures-and-scope-48ebeb9f@68fedd13263fafa05254e3cb9a3b4f8f
---

# Closures and Scope

From [[javascriptallonge]].

## Statements

- First off, let’s use what we learned above. _(javascriptallonge.pdf (source-range-83ecb080-00472))_
- So now we have a value representing that function. _(javascriptallonge.pdf (source-range-83ecb080-00477))_
- Then we’re going to take the value of that function and apply it to the argument 2, something like this: _(javascriptallonge.pdf (source-range-83ecb080-00477))_
- There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-83ecb080-00479))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-83ecb080-00480))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-83ecb080-00480))_
- Now let’s enjoy a relaxed Allongé before we continue! _(javascriptallonge.pdf (source-range-83ecb080-00482))_
- Now let’s enjoy a relaxed Allongé before we continue! _(javascriptallonge.pdf (source-range-83ecb080-00482))_
- It contains a _free variable_ , x.[27] A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- It contains a _free variable_ , x.[27] A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: _(javascriptallonge.pdf (source-range-83ecb080-00487))_
- - Functions containing no free variables are called _pure functions_ . _(javascriptallonge.pdf (source-range-83ecb080-00488))_
- - Functions containing one or more free variables are called _closures_ . _(javascriptallonge.pdf (source-range-83ecb080-00489))_
- They always mean the same thing wherever you use them. _(javascriptallonge.pdf (source-range-83ecb080-00490))_
- Pure functions are easiest to understand. _(javascriptallonge.pdf (source-range-83ecb080-00490))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The first function doesn’t have any variables, therefore doesn’t have any free variables. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The first function doesn’t have any variables, therefore doesn’t have any free variables. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => .... _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-83ecb080-00495))_
- If you can’t, give your reasoning for why it’s impossible. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- 27You may also hear the term “non-local variable.” Both are correct. _(javascriptallonge.pdf (source-range-83ecb080-00499))_
- We also hand-waved something when describing our environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- To understand how closures are evaluated, we need to revisit environments. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- As we’ve said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- As we’ve said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- The variable x isn’t in (y) => ...’s immediate environment, but it is in its parent’s environment, so it evaluates to 1 and that’s what ((y) => x)(2) returns even though it ended up ignoring its own argument. _(javascriptallonge.pdf (source-range-83ecb080-00505))_
- Some people get so excited by this that they write entire books about them, some are great _[a]_ , some–how shall I put this–are interesting _[b]_ if you use Ruby. _(javascriptallonge.pdf (source-range-83ecb080-00506))_
- The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3). _(javascriptallonge.pdf (source-range-83ecb080-00513))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3). _(javascriptallonge.pdf (source-range-83ecb080-00513))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- The first function is the result of currying _[a]_ the second function. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- An interesting thing happens when a variable has the same name as an ancestor environment’s variable. _(javascriptallonge.pdf (source-range-83ecb080-00520))_
- Although its parent also defines an x, it is ignored when evaluating x + y. _(javascriptallonge.pdf (source-range-83ecb080-00522))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-00522))_
- When a variable has the same name as an ancestor environment’s binding, it is said to _shadow_ the ancestor. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- The x in the great-great-grandparent scope is ignored, as are both ws. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-83ecb080-00525))_
- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. _(javascriptallonge.pdf (source-range-83ecb080-00527))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00531))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00531))_
- As we’ll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-83ecb080-00538))_

## Technical atoms

> Context: It’s time to see how a function within a function works: First off, let’s use what we learned above. Given ( _some function_ )( _some argument_ ), we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function’s expression. So we do that first with this code:
_(context: javascriptallonge.pdf (source-range-83ecb080-00470, source-range-83ecb080-00472))_

> - ((x) => (y) => x)(1)(2) _//=> 1_
_(source: javascriptallonge.pdf (source-range-83ecb080-00471))_

> Context: So now we have a value representing that function. Then we’re going to take the value of that function and apply it to the argument 2, something like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00477))_

> - ((y) => x)(2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00478))_

> Context: This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. For example, here’s the equivalent code in Ruby:
_(context: javascriptallonge.pdf (source-range-83ecb080-00480))_

> lambda { |x| lambda { |y| x } }[1][2] _#=> 1_
_(source: javascriptallonge.pdf (source-range-83ecb080-00481))_

> Context: Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen: The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The 
_(context: javascriptallonge.pdf (source-range-83ecb080-00490, source-range-83ecb080-00494))_

> - (x) => (y) => x
_(source: javascriptallonge.pdf (source-range-83ecb080-00493))_

> Context: Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.
_(context: javascriptallonge.pdf (source-range-83ecb080-00498))_

> If pure functions can contain closures, can a closure contain a pure function?
_(source: javascriptallonge.pdf (source-range-83ecb080-00497))_

> Context: To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!
_(context: javascriptallonge.pdf (source-range-83ecb080-00503))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.
_(source: javascriptallonge.pdf (source-range-83ecb080-00504))_

> Context: Functions can have grandparents too:
_(context: javascriptallonge.pdf (source-range-83ecb080-00509))_

> (x) => (y) => (z) => x + y + z
_(source: javascriptallonge.pdf (source-range-83ecb080-00510))_

> Context: This function does much the same thing as:
_(context: javascriptallonge.pdf (source-range-83ecb080-00511))_

> (x, y, z) => x + y + z
_(source: javascriptallonge.pdf (source-range-83ecb080-00512))_

> Context: An interesting thing happens when a variable has the same name as an ancestor environment’s variable. Consider: The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:
_(context: javascriptallonge.pdf (source-range-83ecb080-00520, source-range-83ecb080-00522))_

> - (x) => (x, y) => x + y
_(source: javascriptallonge.pdf (source-range-83ecb080-00521))_

> Context: The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:
_(context: javascriptallonge.pdf (source-range-83ecb080-00522))_

> (x) => (x, y) => (w, z) => (w) => x + y + z
_(source: javascriptallonge.pdf (source-range-83ecb080-00523))_

> Context: JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.
_(context: javascriptallonge.pdf (source-range-83ecb080-00531))_

> If you don’t want your code to operate directly within the global environment, what can you do?
_(source: javascriptallonge.pdf (source-range-83ecb080-00532))_
