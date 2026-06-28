---
page_id: javascriptallonge-environment
page_kind: concept
summary: Environment: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-environment@93aa6675827409ee00be9aa8692c17af
---

# Environment

What [[javascriptallonge]] covers about environment:

## Statements

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

What about reference types? JavaScript does not place copies of reference values in any environment. JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original.

Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.

And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to: (value) =>

- ((ref1, ref2) => ref1 === ref2)(value, value) > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-83ecb080-00054))_

### Closures and Scope

- The first sip: Basic Functions

23

## **it’s always the environment**

To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!

The environment for ((y) => x)(2) is _actually_ {y: 2, '..': {x: 1, ...}}. '..' means something like “parent” or “enclosure” or “super-environment.” It’s (x) => ...’s environment, because the function (y) => x is within (x) => ...’s body. So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

And now you can guess how we evaluate ((y) => x)(2) in the environment {y: 2, '..': {x: 1, ...}}. The variable x isn’t in (y) => ...’s immediate environment, but it is in its parent’s environment, so it evaluates to 1 and that’s what ((y) => x)(2) returns even though it ended up ignoring its own argument.

(x) => x is called the I Combinator, or the _Identity Function_ . (x) => (y) => x is called the K Combinator, or _Kestrel_ . Some people get so excited by this that they write entire books about them, some are great _[a]_ , some–how shall I put this–are interesting _[b]_ if you use Ruby.

> _a_ http://www.amzn.com/0192801422?tag=raganwald001-20

> _b_ https://leanpub.com/combinators

Functions can have grandparents too: (x) => (y) => (z) => x + y + z

This function does much the same thing as: (x, y, z) => x + y + z

Only you call it with (1)(2)(3) instead of (1, 2, 3). The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3). _(javascriptallonge.pdf (source-range-83ecb080-00058))_

### That Constant Coffee Craving

- 34

The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => diameter * PI })() ) _//=> 6.2831853_

Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.

## **are consts also from a shadowy planet?**

We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions.

But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block?

We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other.

Let’s start, as above, by doing this with parameters. We’ll start with:

((PI) => (diameter) => diameter * PI )(3.14159265) And gratuitously wrap it in another IIFE so that we can bind PI to something else: _(javascriptallonge.pdf (source-range-83ecb080-00070))_

- 43

The first sip: Basic Functions

( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })() The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code.

## **function declaration caveats**[34]

Function declarations are formally only supposed to be made at what we might call the “top level” of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:

34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00079))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

104

Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious.[64] The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend.

We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

**Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded.

So here’s a question: If this is such a slow approach, why do some examples of “functional” algorithms work this exact way?

> 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-00153))_


## Related pages

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (2 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (2 shared statement(s))
- [[javascriptallonge-variable]] - shared statements: Variable shares source evidence from Closures and Scope: The first sip: Basic Functions  23  ## **it’s always the environment**  To understand how closures are evaluated, we need to revisit environments. As we’ve said befo ... [truncated] (2 shared statement(s))
- [[javascriptallonge-bind]] - shared statements: Bind shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-binding]] - shared statements: Binding shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from That Constant Coffee Craving: 43  The first sip: Basic Functions  ( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Althou ... [truncated] (1 shared statement(s))
- [[javascriptallonge-different]] - shared statements: Different shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from That Constant Coffee Craving: 43  The first sip: Basic Functions  ( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Althou ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements: Reference shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (1 shared statement(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
