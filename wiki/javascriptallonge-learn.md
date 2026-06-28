---
page_id: javascriptallonge-learn
page_kind: concept
summary: Learn: 4 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-learn@3030dc077ff8cb45410fca467c1f2e84
---

# Learn

What [[javascriptallonge]] covers about learn:

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

### Combinators and Function Decorators

- The first sip: Basic Functions

45

## **Combinators and Function Decorators**

## **higher-order functions**

As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.

Here’s a very simple higher-order function that takes a function as an argument: **const** repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)) : **undefined** repeat(3, **function** (n) { console.log(`Hello **${** n **}** `) }) _//=>_ 'Hello 1' 'Hello 2' 'Hello 3' **undefined**

Higher-order functions dominate _JavaScript Allongé_ . But before we go on, we’ll talk about some specific types of higher-order functions.

## **combinators**

The word “combinator” has a precise technical meaning in mathematics:

“A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] If we were learning Combinatorial Logic, we’d start with the most basic combinators like S, K, and I, and work up from there to practical combinators. We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] .

> 35https://en.wikipedia.org/wiki/Combinatory_logic

> 36http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 _(javascriptallonge.pdf (source-range-83ecb080-00082))_

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

101 **const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_

By writing our parameter list as (n, work = 1) =>, we’re stating that if a second parameter is not provided, work is to be bound to 1. We can do similar things with our other tail-recursive functions: **const** length = ([first, ...rest], numberToBeAdded = 0) => first === **undefined** ? numberToBeAdded : length(rest, 1 + numberToBeAdded) length(["foo", "bar", "baz"]) _//=> 3_ **const** mapWith = (fn, [first, ...rest], prepend = []) => first === **undefined** ? prepend : mapWith(fn, rest, [...prepend, fn(first)]); mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ Now we don’t need to use two functions. A default argument is concise and readable.

## **defaults and destructuring**

We saw earlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-83ecb080-00149))_

### Flip

- Recipes with Data

173 **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);

Sometimes you want to flip, but not curry: **const** flip = (fn) => (first, second) => fn(second, first);

This is gold. Consider how we define mapWith now: **var** mapWith = flipAndCurry(map);

Much nicer!

## **self-currying flip**

Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We _could_ make that into flip: **const** flip = (fn) => **function** (first, second) { **if** (arguments.length === 2) { **return** fn(second, first); } **else** { **return function** (second) { **return** fn(second, first); }; }; };

Now if we write mapWith = flip(map), we can call mapWith(fn, list) or mapWith(fn)(list), our choice.

## **flipping methods**

When we learn about context and methods, we’ll see that flip throws the current context away, so it can’t be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-83ecb080-00232))_


## Technical atoms

### Technical frame 1: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00149))_

> Composing and Decomposing Data

101 **const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_

By writing our parameter list as (n, work = 1) =>, we’re stating that if a second parameter is not provided, work is to be bound to 1. We can do similar things with our other tail-recursive functions: **const** length = ([first, ...rest], numberToBeAdded = 0) => first === **undefined** ? numberToBeAdded : length(rest, 1 + numberToB

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00150))_

> 102 **const** [first, second = "two"] = ["one"];


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated]; Function shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms: Length shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-closure]] - shared statements: Closure shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated] (1 shared statement(s))
- [[javascriptallonge-combinator]] - shared statements: Combinator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  45  ## **Combinators and Function Decorators**  ## **higher-order functions**  As we’ve seen, JavaScript functions take values as arg ... [truncated] (1 shared statement(s))
- [[javascriptallonge-method]] - shared statements: Method shares source evidence from Flip: Recipes with Data  173 **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);  Sometimes you want to flip, but not curry: **const** flip = (fn) = ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pure]] - shared statements: Pure shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
