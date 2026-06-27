---
page_id: javascriptallonge-closure-and-scope
page_kind: concept
summary: Closures and Scope: 37 statement(s) and 11 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-closure-and-scope@bf33117525ac9915c5fa21f13fa05d53
---

# Closures and Scope

What [[javascriptallonge]] covers about closures and scope:

## Statements

_Showing 14 of 37 statements selected for this topic._

- To understand how closures are evaluated, we need to revisit environments. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- The x in the great-great-grandparent scope is ignored, as are both ws. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. _(javascriptallonge.pdf (source-range-83ecb080-00527))_
- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: _(javascriptallonge.pdf (source-range-83ecb080-00487))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-83ecb080-00495))_
- Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- The variable x isn’t in (y) => ...’s immediate environment, but it is in its parent’s environment, so it evaluates to 1 and that’s what ((y) => x)(2) returns even though it ended up ignoring its own argument. _(javascriptallonge.pdf (source-range-83ecb080-00505))_
- The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3). _(javascriptallonge.pdf (source-range-83ecb080-00513))_
- When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- First off, let’s use what we learned above. _(javascriptallonge.pdf (source-range-83ecb080-00472))_
- So now we have a value representing that function. _(javascriptallonge.pdf (source-range-83ecb080-00477))_
- There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-83ecb080-00479))_
- Now let’s enjoy a relaxed Allongé before we continue! _(javascriptallonge.pdf (source-range-83ecb080-00482))_

## Technical atoms

_Showing 6 of 11 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00470, source-range-83ecb080-00472))_

> It’s time to see how a function within a function works: First off, let’s use what we learned above. Given ( _some function_ )( _some argument_ ), we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function’s expression. So we do that first with this code:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00471))_

> - ((x) => (y) => x)(1)(2) _//=> 1_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00477))_

> So now we have a value representing that function. Then we’re going to take the value of that function and apply it to the argument 2, something like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00478))_

> - ((y) => x)(2)

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00480))_

> This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. For example, here’s the equivalent code in Ruby:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00481))_

> lambda { |x| lambda { |y| x } }[1][2] _#=> 1_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00490, source-range-83ecb080-00494))_

> Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen: The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00493))_

> - (x) => (y) => x

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00498))_

> Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00497))_

> If pure functions can contain closures, can a closure contain a pure function?

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00503))_

> To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00504))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.


## Source

- [[javascriptallonge]]
