---
page_id: javascriptallonge-third
page_kind: concept
summary: Third: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-third@42a8c0b3bb4529221a0ff5a0dca612f4
---

# Third

What [[javascriptallonge]] covers about third:

## Statements

### values and identity

- xvii

Prelude: Values and Expressions over Coffee

## **value types**

Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far.

- 2 + 2 === 4 _//=> true_

- (2 + 2 === 4) === (2 !== 5) _//=> true_

Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

**==> picture [288 x 217] intentionally omitted <==**

**Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia**

## **reference types**

So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the _Array_ (other languages sometimes call it a List or a Vector). _(javascriptallonge.pdf (source-range-83ecb080-00034))_

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

### That Constant Coffee Craving

- 27

The first sip: Basic Functions ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_

((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_ That works! We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind.[29]

## **inside-out**

There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: (diameter) => ((PI) => diameter * PI)(3.14159265) It produces the same result as our previous expressions for a diameter-calculating function: ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_ ((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_ ((diameter) => ((PI) => diameter * PI)(3.14159265))(2) _//=> 6.2831853_ Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A “magic literal” like 3.14159265 is anathema to sustainable software development.

The third one is easiest for most people to read. It separates concerns nicely: The “outer” function describes its parameters:

> 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated “IIFE.” _(javascriptallonge.pdf (source-range-83ecb080-00063))_

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

96

## **tail-call optimization**

A “tail-call” occurs when a function’s last act is to invoke another function, and then return whatever the other function returns. For example, consider the maybe function decorator: **const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** ; } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } **return** fn.apply( **this** , args); } } There are three places it returns. The first two don’t return anything, they don’t matter. But the third is fn.apply(this, args). This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. It isn’t going to do any more work, so it can throw its existing stack frame away.

And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. This is a very important characteristic of JavaScript: **If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space.**

That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).

The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call.

The obvious solution? _(javascriptallonge.pdf (source-range-83ecb080-00143))_


## Related pages

- [[javascriptallonge-type]] - shared statements: Type shares source evidence from values and identity: xvii  Prelude: Values and Expressions over Coffee  ## **value types**  Third, some types of cups have no distinguishing marks on them. If they are the same kind of c ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
