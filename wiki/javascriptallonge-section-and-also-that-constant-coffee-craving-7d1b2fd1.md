---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-7d1b2fd1
page_kind: source
summary: And also: / That Constant Coffee Craving: 120 source-backed entries and 43 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-7d1b2fd1@db6f9af93b5b006fbf21f1240daee6da
---

# And also: / That Constant Coffee Craving

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-3f50274e]] - broader source section: And also:
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-96a0dd3a]] - narrower source section: And also: / That Constant Coffee Craving / inside-out
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-const-1d605a7f]] - narrower source section: And also: / That Constant Coffee Craving / const
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-nested-blocks-e1d3b152]] - narrower source section: And also: / That Constant Coffee Craving / nested blocks
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-const-and-lexical-scope-518692ba]] - narrower source section: And also: / That Constant Coffee Craving / const and lexical scope
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-0a0a1685]] - narrower source section: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-rebinding-c21c4915]] - narrower source section: And also: / That Constant Coffee Craving / rebinding

## Statements

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-7239e085-00385))_
- In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . If we put our function expression in parentheses, we can apply it to the argument of 3.14159265 : _(javascriptallonge.pdf (source-range-7239e085-00388))_
- This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 . _(javascriptallonge.pdf (source-range-7239e085-00392))_
- That works! We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind. 29 _(javascriptallonge.pdf (source-range-7239e085-00396))_

## Statements by subsection

### And also: / That Constant Coffee Craving / inside-out

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-7239e085-00398))_
- Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-7239e085-00402))_
- The third one is easiest for most people to read. It separates concerns nicely: The 'outer' function describes its parameters: _(javascriptallonge.pdf (source-range-7239e085-00403))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-7239e085-00404))_
- Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation: _(javascriptallonge.pdf (source-range-7239e085-00406))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing _(javascriptallonge.pdf (source-range-7239e085-00410))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-7239e085-00412))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. And JavaScript does. _(javascriptallonge.pdf (source-range-7239e085-00413))_
- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-7239e085-00398))_
- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-7239e085-00398))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-7239e085-00404))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-7239e085-00412))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-7239e085-00413))_

### And also: / That Constant Coffee Craving / const

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-7239e085-00415))_
- This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-7239e085-00419))_
- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-7239e085-00420))_
- The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing. _(javascriptallonge.pdf (source-range-7239e085-00422))_
- We use the const keyword in a const statement . const statements occur inside blocks, we can't use them when we write a fat arrow that has an expression as its body. _(javascriptallonge.pdf (source-range-7239e085-00423))_
- We can bind any expression. Functions are expressions, so we can bind helper functions: _(javascriptallonge.pdf (source-range-7239e085-00430))_
- Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30 _(javascriptallonge.pdf (source-range-7239e085-00432))_
- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-7239e085-00433))_
- 30 We're into the second chapter and we've finally named a function. Sheesh. _(javascriptallonge.pdf (source-range-7239e085-00436))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-7239e085-00419))_

### And also: / That Constant Coffee Craving / nested blocks

- Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: _(javascriptallonge.pdf (source-range-7239e085-00438))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: _(javascriptallonge.pdf (source-range-7239e085-00442))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-7239e085-00446))_
- Up to now, we've only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-7239e085-00438))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-7239e085-00446))_

### And also: / That Constant Coffee Craving / const and lexical scope

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. The first thing to ask ourselves is, what happens if we use const to bind two different values to the 'same' name? _(javascriptallonge.pdf (source-range-7239e085-00448))_
- It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example: _(javascriptallonge.pdf (source-range-7239e085-00452))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-7239e085-00454))_
- This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-7239e085-00455))_
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI. _(javascriptallonge.pdf (source-range-7239e085-00458))_
- That much we can carefully work out from the way closures work. Does const work the same way? Let's find out: _(javascriptallonge.pdf (source-range-7239e085-00459))_
- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-7239e085-00462))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-7239e085-00454))_
- This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-7239e085-00455))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-7239e085-00464))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block? _(javascriptallonge.pdf (source-range-7239e085-00465))_
- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-7239e085-00466))_
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently: _(javascriptallonge.pdf (source-range-7239e085-00473))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-7239e085-00475))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-7239e085-00477))_
- Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than: _(javascriptallonge.pdf (source-range-7239e085-00481))_
- Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-7239e085-00489))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-7239e085-00465))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-7239e085-00477))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-7239e085-00481))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-7239e085-00481))_
- This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-7239e085-00489))_

### And also: / That Constant Coffee Craving / rebinding

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-7239e085-00496))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. _(javascriptallonge.pdf (source-range-7239e085-00497))_

## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00388))_

> In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . If we put our function expression in parentheses, we can apply it to the argument of 3.14159265 :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00386))_

> There are other ways to name things in JavaScript, but before we learn some of those, let's see how to use what we already have to name things. Let's revisit a very simple example:

### Technical frame 2: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00392))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00389))_

```
((PI) =>
// ????
)(3.14159265)
```

### Technical frame 3: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00392))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00391))_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 4: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00396))_

> That works! We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind. 29

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00395))_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
```

### Technical frame 5: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00402))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00399))_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Technical frame 6: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00402))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00401))_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
((diameter) =>
((PI) =>
diameter * PI)(3.14159265))(2)
//=> 6.2831853
```

### Technical frame 7: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00406))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00405))_

```
(diameter) =>
// ...
```

### Technical frame 8: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00410))_

> Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00407))_

```
((PI) =>
// ...
)(3.14159265)
```

### Technical frame 9: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00410))_

> Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00409))_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Technical frame 10: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00412))_

> But then we've obfuscated our code, and we don't want to do that unless we absolutely have to.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00411))_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 11: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00419))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00416))_

```
(diameter, PI) => diameter * PI
```

### Technical frame 12: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00419))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00418))_

```
((diameter, PI) => diameter * PI)(2, 3.14159265)
//=> 6.2831853
```

### Technical frame 13: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00422))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00421))_

```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

### Technical frame 14: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00430))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00425))_

```
((diameter) =>
((PI) =>
```

### Technical frame 15: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00430))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00426))_

```
diameter * PI)(3.14159265))(2)
Or:
((diameter, PI) => diameter * PI)(2, 3.14159265)
```

### Technical frame 16: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00430))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00427))_

```
//=> 6.2831853
```

### Technical frame 17: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00430))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00429))_

```
((diameter) => {
const PI = 3.14159265;
return diameter * PI
})(2)
//=> 6.2831853
```

### Technical frame 18: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00432))_

> Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00431))_

```
(d) => {
const calc = (diameter) => {
const PI = 3.14159265;
return diameter * PI
};
return "The circumference is " + calc(d)
}
```

### Technical frame 19: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00433))_

> Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00432))_

> This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () .

### Technical frame 20: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00436))_

> 30 We're into the second chapter and we've finally named a function. Sheesh.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00435))_

```
(d) => {
const PI
= 3.14159265,
calc = (diameter) => diameter * PI;
return "The circumference is " + calc(d)
}
```

### Technical frame 21: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00438))_

> One of the places you can find blocks is in an if statement.

### Technical frame 22: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00439))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

### Technical frame 23: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00441))_

```
((n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
})(13)
//=> false
```

### Technical frame 24: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00443))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

### Technical frame 25: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00444))_

```
}
return even(n)
}
And this also works:
((n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
}
return even(n)
})(42)
```

### Technical frame 26: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00445))_

```
//=> true
```

### Technical frame 27: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00452))_

> It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00451))_

```
((diameter_fn) =>
// ...
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
```

### Technical frame 28: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00454))_

> We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00453))_

```
((diameter_fn) =>
diameter_fn(2)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Technical frame 29: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00458))_

> Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00457))_

```
((diameter_fn) =>
((PI) =>
diameter_fn(2)
)(3)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Technical frame 30: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00462))_

> Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00461))_

```
((diameter_fn) => {
const PI = 3;
return diameter_fn(2)
})(
(() => {
const PI = 3.14159265;
return (diameter) => diameter * PI
})()
)
//=> 6.2831853
```

### Technical frame 31: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00473))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00468))_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 32: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00473))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00470))_

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)
```

### Technical frame 33: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00473))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00472))_

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)(2)
//=> 6.2831853
```

### Technical frame 34: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00475))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00474))_

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
```

### Technical frame 35: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00477))_

> We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00476))_

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)(2)
//=> 6.2831853
```

### Technical frame 36: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00481))_

> Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00479))_

```
((diameter) => {
const PI = 3.14159265;
(() => {
const PI = 3;
})();
return diameter * PI;
})(2)
//=> 6.2831853
```

### Technical frame 37: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00482))_

```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

### Technical frame 38: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00483))_

```
})(2)
//=> 6.2831853
```

### Technical frame 39: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00486))_

```
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
})(2)
//=> would return 6 if const had function scope
```

### Technical frame 40: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00487))_

> If const always bound its value to the name defined in the function's environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.

### Technical frame 41: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00488))_

```
((diameter) => {
if (true) {
const PI = 3.14159265;
}
return diameter * PI;
})(2)
//=> would return 6.2831853 if const had function scope
```

### Technical frame 42: And also: / That Constant Coffee Craving / rebinding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00496))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00493))_

```
const evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
n = n - 2;
return evenStevens(n);
}
}
evenStevens(42)
//=> true
```

### Technical frame 43: And also: / That Constant Coffee Craving / rebinding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00496))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00495))_

```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```
