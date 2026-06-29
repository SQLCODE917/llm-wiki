---
page_id: javascriptallonge-section-and-also-closures-and-scope-d1679ec0
page_kind: source
summary: And also: / Closures and Scope: 66 source-backed entries and 16 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-closures-and-scope-d1679ec0@713b31d1edbb82acf2f8b4c91914b8c2
---

# And also: / Closures and Scope

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-3f50274e]] - broader source section: And also:
- [[javascriptallonge-section-and-also-closures-and-scope-if-functions-without-free-variables-are-pure-are-closures-impure-f58a7619]] - narrower source section: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?
- [[javascriptallonge-section-and-also-closures-and-scope-it-s-always-the-environment-47a785c5]] - narrower source section: And also: / Closures and Scope / it's always the environment
- [[javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-1dde456f]] - narrower source section: And also: / Closures and Scope / shadowy variables from a shadowy planet
- [[javascriptallonge-section-and-also-closures-and-scope-which-came-first-the-chicken-or-the-egg-48a59db6]] - narrower source section: And also: / Closures and Scope / which came first, the chicken or the egg?

## Statements

- The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is: _(javascriptallonge.pdf (source-range-7239e085-00334))_
- So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this: _(javascriptallonge.pdf (source-range-7239e085-00336))_
- So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-7239e085-00338))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby: _(javascriptallonge.pdf (source-range-7239e085-00339))_
- It makes sense that the result value is a function, because the expression for (x) => ... _(javascriptallonge.pdf (source-range-7239e085-00334))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-7239e085-00339))_

## Statements by subsection

### And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

- The function (y) => x is interesting. It contains a free variable , x . 27 A free variable is one that is not bound within the function. Up to now, we've only seen one way to 'bind' a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn't have an argument named x , the variable x isn't bound in this function, which makes it 'free.' _(javascriptallonge.pdf (source-range-7239e085-00343))_
- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: _(javascriptallonge.pdf (source-range-7239e085-00344))_
- Functions containing no free variables are called pure functions . _(javascriptallonge.pdf (source-range-7239e085-00345))_
- Functions containing one or more free variables are called closures . _(javascriptallonge.pdf (source-range-7239e085-00346))_
- Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: _(javascriptallonge.pdf (source-range-7239e085-00347))_
- The first function doesn't have any variables, therefore doesn't have any free variables. The second doesn't have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ... , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... . _(javascriptallonge.pdf (source-range-7239e085-00348))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-7239e085-00349))_
- If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible. _(javascriptallonge.pdf (source-range-7239e085-00351))_
- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . _(javascriptallonge.pdf (source-range-7239e085-00352))_
- 27 You may also hear the term 'non-local variable.' Both are correct. _(javascriptallonge.pdf (source-range-7239e085-00353))_
- 27 A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-7239e085-00343))_
- , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... _(javascriptallonge.pdf (source-range-7239e085-00348))_
- The second doesn't have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-7239e085-00348))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-7239e085-00348))_
- The first function doesn't have any variables, therefore doesn't have any free variables. _(javascriptallonge.pdf (source-range-7239e085-00348))_
- Using only what we've learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-7239e085-00351))_
- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. _(javascriptallonge.pdf (source-range-7239e085-00352))_

### And also: / Closures and Scope / it's always the environment

- To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ? Let's fill in the blanks! _(javascriptallonge.pdf (source-range-7239e085-00355))_
- (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20 _(javascriptallonge.pdf (source-range-7239e085-00358))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) . _(javascriptallonge.pdf (source-range-7239e085-00365))_
- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-7239e085-00366))_
- As we've said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-7239e085-00355))_
- Calling a curried function with only some of its arguments is sometimes called partial application b . _(javascriptallonge.pdf (source-range-7239e085-00366))_

### And also: / Closures and Scope / shadowy variables from a shadowy planet

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. Consider: _(javascriptallonge.pdf (source-range-7239e085-00371))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: _(javascriptallonge.pdf (source-range-7239e085-00373))_
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-7239e085-00375))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-7239e085-00376))_

### And also: / Closures and Scope / which came first, the chicken or the egg?

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-7239e085-00378))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } . _(javascriptallonge.pdf (source-range-7239e085-00380))_
- The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-7239e085-00383))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-7239e085-00380))_

## Technical atoms

### Technical frame 1: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00334))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00331))_

```
((x) => (y) => x)(1)(2)
//=> 1
```

### Technical frame 2: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00334))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00333))_

```
((x) => (y) => x)(1)
//=> [Function]
```

### Technical frame 3: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00336))_

> So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00335))_

```
(y) => x
```

### Technical frame 4: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00338))_

> So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00337))_

```
((y) => x)(2)
```

### Technical frame 5: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00339))_

> This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00340))_

```
lambda { |x|
lambda { |y| x }
}[1][2]
#=> 1
```

### Technical frame 6: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00351))_

> If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00350))_

> [Figure] (p.45)

### Technical frame 7: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00352))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00351))_

> If pure functions can contain closures, can a closure contain a pure function?

### Technical frame 8: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00358))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00356))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical frame 9: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00360))_

```
bh
```

### Technical frame 10: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00362))_

```
(x) =>
(y) =>
(z) => x + y + z
```

### Technical frame 11: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00364))_

```
(x, y, z) => x + y + z
```

### Technical frame 12: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00366))_

> The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00367))_

```
ah
bh
```

### Technical frame 13: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00373))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00372))_

```
(x) =>
(x, y) => x + y
```

### Technical frame 14: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00375))_

> When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00374))_

```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

### Technical frame 15: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00383))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00381))_

> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 16: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00383))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00382))_

```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```
