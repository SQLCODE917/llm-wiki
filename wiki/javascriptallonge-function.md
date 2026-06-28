---
page_id: javascriptallonge-function
page_kind: concept
summary: Function: 97 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function@d3a763f4844edc261385ea590d24f315
---

# Function

What [[javascriptallonge]] covers about function:

## Statements

### About JavaScript Allongé

- ii

A Pull of the Lever: Prefaces

## **About JavaScript Allongé**

JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. If those terms seem unfamiliar, don’t worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter.

_JavaScript Allongé_ begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances.

It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor.

_JavaScript Allongé_ teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down. As a result, _JavaScript Allongé_ is a rich read releasing many of JavaScript’s subtleties, much like the Café Allongé beloved by coffee enthusiasts everywhere.

## **why the “six” edition?**

ECMAScript 2015 (formerly called ECMAScript 6 or “ES6”), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive.

Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features.

For example, block-structured languages allow us to write: **for** ( **int** i = 0; i < array.length; ++i) { _// ..._ } And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00012))_

### Forewords to the First Edition

- ix

A Pull of the Lever: Prefaces

## **Forewords to the First Edition**

## **michael fogus**

As a life-long bibliophile and long-time follower of Reg’s online work, I was excited when he started writing books. However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. So as you might imagine I was “skeptical” about the decision to release JavaScript Allongé as an ongoing ebook, with a pay-what-you-want model. However, Reg sent me a copy of his book and I was humbled. Not only was this a great book, but it was also a great way to write and distribute books. Having written books myself, I know the pain of soliciting and receiving feedback.

The act of writing is an iterative process with (very often) tight revision loops. However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. On more than one occasion I’ve found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. However, with the Leanpub model the read-feedback-change process is extremely efficient, leaving in its wake a quality book that continues to get better as others likewise read and comment into infinitude.

In the case of JavaScript Allongé, you’ll find the Leanpub model a shining example of effectiveness. Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. I kid.

As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you’ll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time.

Enjoy.

– Fogus, fogus.me[5]

## **matthew knox**

A different kind of language requires a different kind of book.

JavaScript holds surprising depths–its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many

5http://www.fogus.me _(javascriptallonge.pdf (source-range-83ecb080-00022))_

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

7

## **As Little As Possible About Functions, But No Less**

In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let’s start with the second simplest possible function.[16] In JavaScript, it looks like this:

## () => 0

This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:

- (() => 0) _//=> [Function]_ What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else.

> 16 The simplest possible function is () => {}, we’ll see that later. _(javascriptallonge.pdf (source-range-83ecb080-00044))_

- The first sip: Basic Functions

8

I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function.

## **functions and identities**

You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not.

Which kind are functions? Let’s try them out and see. For reasons of appeasing the JavaScript parser, we’ll enclose our functions in parentheses: (() => 0) === (() => 0) _//=> false_

Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. “Function” is a reference type.

## **applying functions**

Let’s put functions to work. The way we use functions is to _apply_ them to zero or more values called _arguments_ . Just as 2 + 2 produces a value (in this case 4), applying a function to zero or more arguments produces a value as well.

Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. Let’s call the arguments _args_ . Here’s how to apply a function to some arguments:

## _fn_expr_ ( _args_ )

Right now, we only know about one such expression: () => 0, so let’s use it. We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). Since we aren’t giving it any arguments, we’ll simply write () after the expression. So we write: (() => 0)() _//=> 0_

> 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-83ecb080-00045))_

- The first sip: Basic Functions

9

## **functions that return values and evaluate expressions**

We’ve seen () => 0. We know that (() => 0)() returns 0, and this is unsurprising. Likewise, the following all ought to be obvious: (() => 1)() _//=> 1_ (() => "Hello, JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** )() _//=> Infinity_

Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2. Can we put an expression to the right of the arrow?

(() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)()?

Let’s try it: (() => (() => 0)())() _//=> 0_

Yes we can! Functions can return the value of evaluating another function.

When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. So we can also write: _(javascriptallonge.pdf (source-range-83ecb080-00046))_

- The first sip: Basic Functions

15

- (() => **return** 0)() - _//=> ERROR_

Statements belong inside blocks and only inside blocks. Some languages simplify this by making everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we also learn about statements like function declarations, for loops, if statements, and so forth. We’ll see a few more of these later.

## **functions that evaluate to functions**

If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… _Can we put an expression that evaluates to a function on the right side of a function expression?_

Yes: () => () => 0 That’s a function! It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. So we have _a function, that returns a function, that returns zero_ . Likewise: () => () => **true** That’s a function, that returns a function, that returns true: (() => () => **true** )()() - _//=> true_

We could, of course, do the same thing with a block if we wanted: () => () => { **return true** ; } But we generally don’t.

Well. We’ve been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical. _(javascriptallonge.pdf (source-range-83ecb080-00052))_

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

- The first sip: Basic Functions

24

The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

> _a_ https://en.wikipedia.org/wiki/Currying

> _b_ https://en.wikipedia.org/wiki/Partial_application

## **shadowy variables from a shadowy planet**

An interesting thing happens when a variable has the same name as an ancestor environment’s variable. Consider:

- (x) => (x, y) => x + y

The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: (x) => (x, y) => (w, z) => (w) => x + y + z

When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both ws. When a variable has the same name as an ancestor environment’s binding, it is said to _shadow_ the ancestor.

This is often a good thing.

## **which came first, the chicken or the egg?**

This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state.

But before we do so, there’s one final question: Where does the ancestry start? If there’s no other code in a file, what is (x) => x’s parent environment? _(javascriptallonge.pdf (source-range-83ecb080-00059))_

### That Constant Coffee Craving

- The first sip: Basic Functions

26

## **That Constant Coffee Craving**

Up to now, all we’ve really seen are _anonymous functions_ , functions that don’t have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we’ve seen so far is how to name arguments.

There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example: (diameter) => diameter * 3.14159265

What is this “3.14159265” number? PI[28] , obviously. We’d like to name it so that we can write something like: (diameter) => diameter * PI

In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:

((PI) => _// ????_ )(3.14159265) What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:

((PI) => (diameter) => diameter * PI )(3.14159265) This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our “functions” are expressions. This one has a few more moving parts, that’s all. But we can use it just like (diameter) => diameter * 3.14159265.

Let’s test it:

28https://en.wikipedia.org/wiki/Pi _(javascriptallonge.pdf (source-range-83ecb080-00062))_

- 30

The first sip: Basic Functions ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_

We can bind any expression. Functions are expressions, so we can bind helper functions: (d) => { **const** calc = (diameter) => { **const** PI = 3.14159265; **return** diameter * PI }; **return** "The circumference is " + calc(d) } Notice calc(d)? This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with (). A name that’s bound to a function is a valid expression evaluating to a function.[30] Amazing how such an important idea–naming functions–can be explained _en passant_ in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as “first class entities.” Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

We can bind more than one name-value pair by separating them with commas. For readability, most people put one binding per line: (d) => { **const** PI = 3.14159265, calc = (diameter) => diameter * PI; **return** "The circumference is " + calc(d) } > 30We’re into the second chapter and we’ve finally named a function. Sheesh. _(javascriptallonge.pdf (source-range-83ecb080-00066))_

- 40

The first sip: Basic Functions **function** (n) { **return** (1.618**n - -1.618**-n) / 2.236; } This still does not _name_ a function, but as we noted above, functions written with the function keyword have an optional “something else.” Could that “something else” name a function? Yes, of course.[33] Here are our example functions written with names: **const** repeat = **function** repeat (str) { **return** str + str; }; **const** fib = **function** fib (n) { **return** (1.618**n - -1.618**-n) / 2.236; };

Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write: **const double** = **function** repeat (str) { **return** str + str; } In this expression, double is the name in the environment, but repeat is the function’s actual name. This is a _named function expression_ . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

And indeed the name _is_ a property: **double** .name

_//=> 'repeat'_

In this book we are not examining JavaScript’s tooling such as debuggers baked into browsers, but we will note that when you are navigating call stacks in all modern tools, the function’s binding name is ignored but its actual name is displayed, so naming functions is very useful even if they don’t get a formal binding, e.g.

> 33“Yes of course?” Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-83ecb080-00076))_

- The first sip: Basic Functions

41 someBackboneView.on('click', **function** clickHandler () { _//..._ });

Now, the function’s actual name has no effect on the environment in which it is used. To whit: **const** bindingName = **function** actualName () { _//..._ }; bindingName _//=> [Function: actualName]_ actualName _//=> ReferenceError: actualName is not defined_ So “actualName” isn’t bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here’s a function that determines whether a positive integer is even or not. We’ll use it in an IIFE so that we don’t have to bind it to a name with const:

( **function** even (n) { **if** (n === 0) { **return true** } **else return** !even(n - 1) })(5) _//=> false_ ( **function** even (n) { **if** (n === 0) { **return true** } **else return** !even(n - 1) })(2) _//=> true_

Clearly, the name even is bound to the function _within the function’s body_ . Is it bound to the function outside of the function’s body? _(javascriptallonge.pdf (source-range-83ecb080-00077))_

- 43

The first sip: Basic Functions

( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })() The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code.

## **function declaration caveats**[34]

Function declarations are formally only supposed to be made at what we might call the “top level” of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:

34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00079))_

- 44

The first sip: Basic Functions

( **function** (camelCase) { **return** fizzbuzz(); **if** (camelCase) { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } **else** { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } })( **true** ) _//=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?_

Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. So this is a function declaration: **function** trueDat () { **return true** } But this is not:

( **function** trueDat () { **return true** }) The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-83ecb080-00080))_

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

- The first sip: Basic Functions

47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress. But like compose, we could write either: **const** something = (x) => x != **null** ; And elsewhere, write: **const** nothing = (x) => !something(x); Or we could write: **const** nothing = not(something); not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. You’ll see other function decorators in the recipes, like once and maybe. Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00084))_

### Building Blocks

- The first sip: Basic Functions

48

## **Building Blocks**

When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks.

## **composition**

: One of the most basic of these building blocks is _composition_ **const** cookAndEat = (food) => eat(cook(food));

It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators: **const** compose = (a, b) => (c) => a(b(c)); **const** cookAndEat = compose(eat, cook);

If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument.

Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

- **const** actuallyTransfer= (from, to, amount) => _// do something_ **const** invokeTransfer = once(maybe(actuallyTransfer(...))); _(javascriptallonge.pdf (source-range-83ecb080-00086))_

- The first sip: Basic Functions

49

## **partial application**

Another basic building block is _partial application_ . When a function takes multiple arguments, we “apply” the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can’t get the final value, but we can get a function that represents _part_ of our application.

Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this:

_.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_ We don’t want to fool around writing _., so we can use it by writing:[41] This code implements a partial application of the map function by applying the function (n) => n * n as its second argument: **const** squareAll = (array) => map(array, (n) => n * n);

The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**const** mapWith = (fn) => (array) => map(array, fn); **const** squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) _//=> [1, 4, 9]_ We’ll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

> 39http://underscorejs.org

> 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache.

> 41If we don’t want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven’t discussed methods yet. const map = _.map; _(javascriptallonge.pdf (source-range-83ecb080-00087))_

### Magic Names

- The first sip: Basic Functions

51

## **Magic Names**

When a function is applied to arguments (or “called”), JavaScript binds the values of arguments to the function’s argument names in an environment created for the function’s execution. What we haven’t discussed so far is that JavaScript also binds values to some “magic” names in addition to any you put in the argument list.[42]

## **the function keyword**

There are two separate rules for these “magic” names, one for when you invoke a function using the function keyword, and another for functions defined with “fat arrows.” We’ll begin with how things work for functions defined with the function keyword.

The first magic name is this, and it is bound to something called the function’s context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function: **const** plus = **function** (a, b) { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_ Although arguments looks like an array, it isn’t an array: It’s more like an object[43] that happens to bind some values to properties with names that look like integers starting with zero: **const** args = **function** (a, b) { **return** arguments; } args(2,3) _//=> { '0': 2, '1': 3 }_ arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

> 42You should never attempt to define your own bindings against “magic” names that JavaScript binds for you. It is wise to treat them as read-only at all times.

> 43We’ll look at arrays and plain old javascript objects in depth later. _(javascriptallonge.pdf (source-range-83ecb080-00090))_

- 52

The first sip: Basic Functions **const** plus = **function** () { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_

When discussing objects, we’ll discuss properties in more depth. Here’s something interesting about arguments: **const** howMany = **function** () { **return** arguments['length']; } howMany() _//=> 0_ howMany('hello') _//=> 1_ howMany('sharks', 'are', 'apex', 'predators') _//=> 4_

The most common use of the arguments binding is to build functions that can take a variable number of arguments. We’ll see it used in many of the recipes, starting off with partial application and ellipses.

## **magic names and fat arrows**

The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding.

For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00091))_

- The first sip: Basic Functions

54 **const** row = **function** () { **return** mapWith( **function** (column) { **return** column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) _//=> [1,4,9,16,25,36,49,64,81,100,121,144]_ Now our inner function binds arguments[0] every time it is invoked, so we get the same result as if we’d written function (column) { return column * column }.

Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it’s a first-class entity in the code.

But sometimes, a function is a small-f function. It’s a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply.

Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00093))_

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

### Unary

- Recipes with Basic Functions

59

## **Unary**

“Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:

['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_ In that example, it looks exactly like the mapping function you’ll find in most languages: You pass it a function, and it calls the function with one argument, the element of the array. However, that’s not the whole story. JavaScript’s map actually calls each function with _three_ arguments: The element, the index of the element in the array, and the array itself.

Let’s try it:

[1, 2, 3].map( **function** (element, index, arr) { console.log({element: element, index: index, arr: arr}) }) _//=> { element: 1, index: 0, arr: [ 1, 2, 3 ] } // { element: 2, index: 1, arr: [ 1, 2, 3 ] } // { element: 3, index: 2, arr: [ 1, 2, 3 ] }_ If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_ This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us: _(javascriptallonge.pdf (source-range-83ecb080-00102))_

### Once

- Recipes with Basic Functions

65

## **Once**

once is an extremely helpful combinator. It ensures that a function can only be called, well, _once_ . Here’s the recipe: **const** once = (fn) => { **let** done = **false** ; **return function** () { **return** done ? **void** 0 : ((done = **true** ), fn.apply( **this** , arguments)) } } Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it: **const** askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() _//=> 'sure, why not?'_

askedOnBlindDate() _//=> undefined_ askedOnBlindDate() _//=> undefined_

It seems some people will only try blind dating once.

(Note: There are some subtleties with decorators like once that involve the intersection of state with methods. We’ll look at that again in stateful method decorators.) _(javascriptallonge.pdf (source-range-83ecb080-00111))_

### Left-Variadic Functions

- Recipes with Basic Functions

66

## **Left-Variadic Functions**

A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. For example: **const** abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5] This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015: **function** team(coach, captain, ...players) { console.log(` **${** captain **}** (captain)`); **for** ( **let** player **of** players) { console.log(player); } console.log(`squad coached by **${** coach **}** `); } team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen', 'Martín Montoya', 'Gerard Piqué') _//=>_ Xavi Hernández (captain) Marc-André ter Stegen Martín Montoya Gerard Piqué squad coached by Luis Enrique

## But we can’t go the other way around:

> 52English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be “variary?” No! They have to be “variadic.” _(javascriptallonge.pdf (source-range-83ecb080-00113))_

- Recipes with Basic Functions

68

We don’t need rightVariadic any more, because instead of: **var** firstAndButFirst = rightVariadic( **function** test (first, butFirst) { **return** [first, butFirst] });

We now simply write: **const** firstAndButFirst = (first, ...butFirst) => [first, butFirst];

This is a _right-variadic function_ , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

## **overcoming limitations**

It’s nice to have progress. But as noted above, we can’t write: **const** butLastAndLast = (...butLast, last) => [butLast, last]; That’s a _left-variadic function_ . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn’t do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function?

We sure can, by using the techniques from rightVariadic. Mind you, we can take advantage of modern JavaScript to simplify the code: **const** leftVariadic = (fn) => { **if** (fn.length < 1) { **return** fn; } **else** { **return function** (...args) { **const** gathered = args.slice(0, args.length - fn.length + 1), spread = args.slice(args.length - fn.length + 1); **return** fn.apply( **this** , [gathered].concat(spread) _(javascriptallonge.pdf (source-range-83ecb080-00115))_

- 69

Recipes with Basic Functions ); } } }; **const** butLastAndLast = leftVariadic((butLast, last) => [butLast, last]); butLastAndLast('why', 'hello', 'there', 'little', 'droid') _//=> [["why","hello","there","little"],"droid"]_ Our leftVariadic function is a decorator that turns any function into a function that gathers parameters _from the left_ , instead of from the right.

## **left-variadic destructuring**

Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this: **const** [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid']; first _//=> 'why'_ butFirst _//=> ["hello","there","little","droid"]_ As with parameters, we can’t gather values from the left when destructuring an array: **const** [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid']; _//=> Unexpected token_

We could use leftVariadic the hard way: _(javascriptallonge.pdf (source-range-83ecb080-00116))_

- 76

Picking the Bean: Choice and Truthiness **const** or = (a, b) => a() || b() **const** and = (a, b) => a() && b() **const** even = (n) => or(() => n === 0, () => and(() => n !== 1, () => even(n - 2))) even(7) _//=> false_

Here we’ve passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation.

## **summary**

- Logical operators are based on truthiness and falsiness, not the strict values true and false.

- ! is a logical operator, it always returns true or false.

- The ternary operator (?:), ||, and && are control flow operators, they do not always return true or false, and they have short-cut semantics.

- Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-83ecb080-00120))_

### Arrays and Destructuring Arguments

- Composing and Decomposing Data

88 its .length. But as an exercise, how would we write a length function using just what we have already?

First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0: **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_

We need something for when the array isn’t empty. If an array is not empty, and we break it into two pieces, first and rest, the length of our array is going to be length(first) + length(rest). Well, the length of first is 1, there’s just one element at the front. But we don’t know the length of rest. If only there was a function we could call… Like length!

**const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

Let’s try it!

length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_

Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

## **linear recursion**

“Recursion” sometimes seems like an elaborate party trick. There’s even a joke about this:

When promising students are trying to choose between pure mathematics and applied engineering, they are given a two-part aptitude test. In the first part, they are led to a laboratory bench and told to follow the instructions printed on the card. They find a bunsen burner, a sparker, a tap, an empty beaker, a stand, and a card with the instructions “boil water.” _(javascriptallonge.pdf (source-range-83ecb080-00134))_

- Composing and Decomposing Data

91 **const** truthyAll = ([first, ...rest]) => first === **undefined**

? [] : [!!first, ...truthyAll(rest)]; truthyAll([ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_ This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let’s “extract” the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

Given the signature: **const** mapWith = (fn, array) => _// ..._

We can write it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ mapWith((x) => !!x, [ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_

## **folding**

With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-00137))_

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

94

## **Tail Calls (and Default Arguments)**

The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded.

Let’s look at how. Here’s our extremely simple mapWith function again: **const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ Let’s step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined, so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)].

This is roughly equivalent to writing: **const** mapWith = **function** (fn, [first, ...rest]) { **if** (first === **undefined** ) { **return** []; } **else** { **const** _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; **return** _temp3; } } Note that while evaluating mapWith(fn, rest), JavaScript must retain the value first or fn(first), plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1.

Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). And the same thing happens: JavaScript has to hang on to 2 (or 4, or both, _(javascriptallonge.pdf (source-range-83ecb080-00141))_

- Composing and Decomposing Data

96

## **tail-call optimization**

A “tail-call” occurs when a function’s last act is to invoke another function, and then return whatever the other function returns. For example, consider the maybe function decorator: **const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** ; } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } **return** fn.apply( **this** , args); } } There are three places it returns. The first two don’t return anything, they don’t matter. But the third is fn.apply(this, args). This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. It isn’t going to do any more work, so it can throw its existing stack frame away.

And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. This is a very important characteristic of JavaScript: **If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space.**

That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).

The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call.

The obvious solution? _(javascriptallonge.pdf (source-range-83ecb080-00143))_

- Composing and Decomposing Data

98 **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === **undefined**

- ? prepend

- : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); **const** mapWith = callLast(mapWithDelaysWork, []); mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ We can use it with ridiculously large arrays: mapWith((x) => x * x, [

|0,|1,|2,|3,|4,|5,|6,|7,|8,|9,|

|---|---|---|---|---|---|---|---|---|---|

|10,|11,|12,|13,|14,|15,|16,|17,|18,|19,|

|20,|21,|22,|23,|24,|25,|26,|27,|28,|29,|

|30,|31,|32,|33,|34,|35,|36,|37,|38,|39,|

|40,|41,|42,|43,|44,|45,|46,|47,|48,|49,|

|50,|51,|52,|53,|54,|55,|56,|57,|58,|59,|

|60,|61,|62,|63,|64,|65,|66,|67,|68,|69,|

|70,|71,|72,|73,|74,|75,|76,|77,|78,|79,|

|80,|81,|82,|83,|84,|85,|86,|87,|88,|89,|

|90,|91,|92,|93,|94,|95,|96,|97,|98,|99,|

_// ..._

2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ])

_//=> [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196, ..._ Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

## **factorials**

Introductions to recursion often mention calculating factorials:

In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: _(javascriptallonge.pdf (source-range-83ecb080-00145))_

### Mutation

- Composing and Decomposing Data

120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsEve _//=> [2012, 10, 31]_ The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?

**const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween[0] = 2013; })(allHallowsEve); allHallowsEve _//=> [2013, 10, 31]_ This is different. We haven’t rebound the inner name to a different variable, we’ve mutated the value that both bindings share. Now that we’ve finished with mutation and aliases, let’s have a look at it.

**==> picture [29 x 29] intentionally omitted <==**

JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value.

**==> picture [29 x 29] intentionally omitted <==**

Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction.

## **mutation and data structures**

Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell[70] don’t permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about.

One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let’s recall linked lists from Plain Old JavaScript Objects. While we’re executing the mapWith function, we’re constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith.

But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:

70https://en.wikipedia.org/wiki/Haskell_ _(javascriptallonge.pdf (source-range-83ecb080-00171))_

### Reassignment

- Composing and Decomposing Data

129 **return** n * factorial2(x); } } factorial2(5) _//=> 120_ But of course, it’s not exactly like let. It’s just different enough to present a source of confusion. First, var is not block scoped, it’s function scoped, just like function declarations: (() => { **var** age = 49; **if** ( **true** ) { **var** age = 50; } **return** age; })() _//=> 50_

Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. Note this example of a function that uses a helper: **const** factorial = (n) => { **return** innerFactorial(n, 1); **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } } factorial(4) _//=> 24_ _(javascriptallonge.pdf (source-range-83ecb080-00181))_

- Composing and Decomposing Data

131 **const** factorial = (n) => { **let** innerFactorial = **undefined** ; **return** innerFactorial(n, 1); innerFactorial = **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } } factorial(4) _//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')_ In that way, var is a little like const and let, we should always declare and bind names before using them. But it’s not like const and let in that it’s function scoped, not block scoped.

## **why const and let were invented**

const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). However, its functional scope was a problem.

We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var: **var** sum = 0; **for** ( **var** i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050

Hopefully, you can think of a faster way to calculate this sum.[72] And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

> 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . . . . + 99 + 100 = ? But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . . . . + (50 + 51) = ? If you notice every pair of numbers adds up to 101. There are 50 pairs of numbers, so the answer is 50*101 = 5050. Of course Gauss came up with the answer about 20 times faster than the other kids. _(javascriptallonge.pdf (source-range-83ecb080-00183))_

- Composing and Decomposing Data

132

Yes. Consider this variation: **var** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **var** i = 0; i < 3; i++) { introductions[i] = "Hello, my name is " + names[i] } introductions _//=> [ 'Hello, my name is Karl', // 'Hello, my name is Friedrich', // 'Hello, my name is Gauss' ]_ So far, so good. Hey, remember that functions in JavaScript are values? Let’s get fancy!

**var** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **var** i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, **${** soAndSo **}** , my name is **${** names[i] **}** ` } introductions _//=> [ [Function], // [Function], // [Function] ]_ Again, so far, so good. Let’s try one of our functions: introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is undefined'_

What went wrong? Why didn’t it give us ‘Hello, Raganwald, my name is Friedrich’? The answer is that pesky var i. Remember that i is bound in the surrounding environment, so it’s as if we wrote: _(javascriptallonge.pdf (source-range-83ecb080-00184))_

- 133

Composing and Decomposing Data **var** introductions = [], names = ['Karl', 'Friedrich', 'Gauss'], i = **undefined** ; **for** (i = 0; i < 3; i++) { introductions[i] = **function** (soAndSo) { **return** "Hello, " + soAndSo + ", my name is " + names[i] } } introductions

Now, at the time we created each function, i had a sensible value, like 0, 1, or 2. But at the time we _call_ one of the functions, i has the value 3, which is why the loop terminated. So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. That’s not what we want at all.

The error wouldn’t exist at all if we’d used let in the first place **let** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **let** i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, **${** soAndSo **}** , my name is **${** names[i] **}** ` } introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is Friedrich'_

This small error was a frequent cause of confusion, and in the days when there was no block-scoped let, programmers would need to know how to fake it, usually with an IIFE: **var** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **var** i = 0; i < 3; i++) { ((i) => { introductions[i] = (soAndSo) => `Hello, **${** soAndSo **}** , my name is **${** names[i] **}** ` } })(i) } introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is Friedrich'_ _(javascriptallonge.pdf (source-range-83ecb080-00185))_

### Copy on Write

- Composing and Decomposing Data

138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ Our new at and set functions behave similarly to array[index] and array[index] = value. The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list.

## **copy-on-read**

So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**const** rest = ({first, rest}) => copy(rest); **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = rest(parentList); **const** newParentList = set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}} This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don’t need to make a copy because we won’t be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node).

There’s also a bug: What happens when we modify the first element of a list? But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-00191))_

- Composing and Decomposing Data

140

Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] Like all strategies, it makes a tradeoff: It’s much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren’t sharing, it’s more expensive.

Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write.

> 73https://en.wikipedia.org/wiki/Copy-on-write _(javascriptallonge.pdf (source-range-83ecb080-00193))_

### Functional Iterators

- 145

Composing and Decomposing Data **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); **const** foldArray = (array) => callRight(foldArrayWith, array); **const** sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldArray([1, 4, 9, 16, 25])) _//=> 55_

What we’ve done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array);. The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable.

Here it is summing a tree of numbers: **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldTreeWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : Array.isArray(first) ? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\ e, rest)) : fn(first, foldTreeWith(fn, terminalValue, rest)); **const** foldTree = (tree) => callRight(foldTreeWith, tree); **const** sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldTree([1, [4, [9, 16]], 25])) _//=> 55_

We’ve found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we’ve completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-83ecb080-00200))_

- 148

Composing and Decomposing Data sum += eachIteration.value; } **return** sum; } iteratorSum(arrayIterator([1, 4, 9, 16, 25])) _//=> 55_

Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true }.

We can write a different iterator for a different data structure. Here’s one for linked lists: **const** EMPTY = **null** ; **const** isEmpty = (node) => node === EMPTY; **const** pair = (first, rest = EMPTY) => ({first, rest}); **const** list = (...elements) => { **const** [first, ...rest] = elements; **return** elements.length === 0 ? EMPTY : pair(first, list(...rest)) } **const** print = (aPair) => isEmpty(aPair) ? "" : ` **${** aPair.first **} ${** print(aPair.rest) **}** ` **const** listIterator = (aPair) => () => { **const** done = isEmpty(aPair); **if** (done) { **return** {done}; } **else** { **const** {first, rest} = aPair; aPair = aPair.rest; _(javascriptallonge.pdf (source-range-83ecb080-00203))_

- Composing and Decomposing Data

150 **const** FibonacciIterator = () => { **let** previous = 0, current = 1; **return** () => { **const** value = current; [previous, current] = [current, current + previous]; **return** {done: **false** , value}; }; }; **const** fib = FibonacciIterator() fib().value _//=> 1_ fib().value _//=> 1_ fib().value _//=> 2_ fib().value _//=> 3_ fib().value _//=> 5_

A function that starts with a seed and expands it into a data structure is called an _unfold_ . It’s the opposite of a fold. It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators.

For starters, we can map an iterator, just like we map a collection: **const** mapIteratorWith = (fn, iterator) => () => { **const** {done, value} = iterator(); **return** ({done, value: done ? **undefined** : fn(value)}); } **const** squares = mapIteratorWith((x) => x * x, NumberIterator(1)); squares().value _//=> 1_ squares().value _(javascriptallonge.pdf (source-range-83ecb080-00205))_

- Composing and Decomposing Data

153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);

This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: **const** firstInArray = (fn, array) => array.filter(fn)[0];

JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

## **caveat**

Please note that unlike most of the other functions discussed in this book, iterators are _stateful_ . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you’re changing the state of the original!

For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-00208))_

### Making Data Out Of Functions

- Composing and Decomposing Data

154

## **Making Data Out Of Functions**

**==> picture [469 x 352] intentionally omitted <==**

**Coffee served at the CERN particle accelerator**

In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case.

For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-00210))_

- 156

Composing and Decomposing Data **const** K = (x) => (y) => x; **const** I = (x) => (x); **const** V = (x) => (y) => (z) => z(x)(y);

## **the kestrel and the idiot**

A _constant function_ is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K, is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value.

For example: **const** K = (x) => (y) => x; **const** fortyTwo = K(42); fortyTwo(6) _//=> 42_ fortyTwo("Hello") _//=> 42_

The _identity function_ is a function that evaluates to whatever parameter you pass it. So I(42) => 42. Very simple, but useful. Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.

Like so:

K(6)(7) _//=> 6_

K(12)(24) _//=> 12_

This is very interesting. Given two values, we can say that K always returns the _first_ value: K(x)(y) => x (that’s not valid JavaScript, but it’s essentially how it works).

Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.

Therefore, K(I)(x)(y) => y: _(javascriptallonge.pdf (source-range-83ecb080-00212))_

- Composing and Decomposing Data

157

K(I)(6)(7) _//=> 7_

K(I)(12)(24) _//=> 24_

Aha! Given two values, K(I) always returns the _second_ value.

K("primus")("secundus") _//=> "primus"_

K(I)("primus")("secundus") _//=> "secundus"_

If we are not feeling particularly academic, we can name our functions: **const** first = K, second = K(I); first("primus")("secundus") _//=> "primus"_ second("primus")("secundus") _//=> "secundus"_

This is very interesting. Given two values, we can say that K always returns the _first_ value, and given two values, K(I) always returns the _second_ value.

## **backwardness**

Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we’d write them like this: _(javascriptallonge.pdf (source-range-83ecb080-00213))_

- Composing and Decomposing Data

158 **const** first = ([first, second]) => first, second = ([first, second]) => second; **const** latin = ["primus", "secundus"]; first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_ Or if we were using a POJO, we’d write them like this: **const** first = ({first, second}) => first, second = ({first, second}) => second; **const** latin = {first: "primus", second: "secundus"}; first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_

In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

But the first and second we built out of K and I don’t work that way. You call them and pass them the bits, and they choose what to return. So if we wanted to use them with a two-element array, we’d need to have a piece of code that calls some code.

Here’s the first cut: **const** first = K, second = K(I); **const** latin = (selector) => selector("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_ _(javascriptallonge.pdf (source-range-83ecb080-00214))_

- Composing and Decomposing Data

160 **const** first = K, second = K(I), pair = V; **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_ As an aside, the Vireo is a little like JavaScript’s .apply function. It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. One notable example is the “thrush” or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap.

Armed with nothing more than K, I, and V, we can make a little data structure that holds two values, the cons cell of Lisp and the node of a linked list. Without arrays, and without objects, just with functions. We’d better try it out to check.

## **lists with functions as data**

Here’s another look at linked lists using POJOs. We use the term rest instead of second, but it’s otherwise identical to what we have above: **const** first = ({first, rest}) => first, rest = ({first, rest}) => rest, pair = (first, rest) => ({first, rest}), EMPTY = ({}); **const** l123 = pair(1, pair(2, pair(3, EMPTY))); first(l123) _//=> 1_ first(rest(l123)) _//=> 2_ first(rest(rest(l123))) _//=3_

We can write length and mapWith functions over it: _(javascriptallonge.pdf (source-range-83ecb080-00216))_

- 165

Composing and Decomposing Data **const** reverse = (list, delayed = EMPTYLIST) => list( () => delayed, (aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed)) ); print(reverse(l123)); _//=> 3 2 1_ **const** mapWith = (fn, list, delayed = EMPTYLIST) => list( () => reverse(delayed), (aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed)) ); print(mapWith(x => x * x, reverse(l123))) _//=> 941_

We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else.

## **functions are not the real point**

There are lots of similar texts explaining how to construct complex semantics out of functions. You can establish that K and K(I) can represent true and false, model magnitudes with Church Numerals[79] or Surreal Numbers[80] , and build your way up to printing FizzBuzz.

The superficial conclusion reads something like this:

Functions are a fundamental building block of computation. They are “axioms” of combinatory logic, and can be used to compute anything that JavaScript can compute.

However, that is not the interesting thing to note here. Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. Knowing how to make a linked list out of functions is not really necessary for the working programmer. (Knowing that it can be done, on the other hand, is very important to understanding computer science.) Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons[81] of the electromagnetic force. It’s the QED of physics that underpins the Maxwell’s Equations of programming. Deeply important, but not practical when you’re building a bridge.

> 79https://en.wikipedia.org/wiki/Church_encoding

> 80https://en.wikipedia.org/wiki/Surreal_number

> 81https://en.wikipedia.org/wiki/Gauge_boson _(javascriptallonge.pdf (source-range-83ecb080-00221))_

- Composing and Decomposing Data

167

We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list: **const** length = (node, delayed = 0) => node === EMPTY

- ? delayed

- : length(node.rest, delayed + 1);

The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we’re pushing even more knowledge about the structure of lists into the code that uses them.

Having a list know itself whether it is empty hides implementation information from the code that uses lists. This is a fundamental principle of good design. It is a tenet of Object-Oriented Programming, but it is **not** exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both.

There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns:

- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want.

- And instead of testing some property of an entity and making a choice of our own with ?: (or if), pass the entity the work we want done for each case and let it test itself. _(javascriptallonge.pdf (source-range-83ecb080-00223))_

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

### Why?

- Recipes with Data

178

## **Why?**

This is the canonical Y Combinator[86] : **const** Y = (f) => ( x => f(v => x(x)(v)) )( x => f(v => x(x)(v)) );

You use it like this: **const** factorial = Y( **function** (fac) { **return function** (n) { **return** (n == 0 ? 1 : n * fac(n - 1)); } }); factorial(5) _//=> 120_

Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it’s essential: With fixed-point combinators it’s possible to compute everything computable without binding names.

So again, why include the recipe? Well, besides all of the practical applications that combinators provide, there is this little thing called _The joy of working things out._

There are many explanations of the Y Combinator’s mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. Use it as an excuse to get familiar with your environment’s debugging facility.

One tip is to use JavaScript to name things. For example, you could start by writing: **const** Y = (f) => { **const** something = x => f(v => x(x)(v)); **return** something(something); };

What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces.

Work things out for yourself!

> 86https://en.wikipedia.org/wiki/Fixed-point_combinator#Example_in_JavaScript _(javascriptallonge.pdf (source-range-83ecb080-00239))_

### A Warm Cup: Basic Strings and Quasi-Literals

- A Warm Cup: Basic Strings and Quasi-Literals

181

- 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

- 'A popular number for nerds is' + (40 + 2) - _//=> 'A popular number for nerds is42'_

## **evaluation time**

Like any other expression, quasi-literals are evaluated _late_ , when that line or lines of code is evaluated.

So for example, **const** name = "Harry"; **const** greeting = (name) => `Hello my name is **${** name **}** `; greeting('Arthur Dent') - _//=> 'Hello my name is Arthur Dent'_

JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked.

This is exactly what we’d expect if we’d written it like this: **const** greeting = (name) => 'Hello my name is ' + name; greeting('Arthur Dent') - _//=> 'Hello my name is Arthur Dent'_ _(javascriptallonge.pdf (source-range-83ecb080-00243))_

### Iteration and Iterables

- Served by the Pot: Collections

185 **const** iter = stack.iterator(); iter().value _//=> "you!"_ iter().value _//=> "to"_ The way we’ve written .iterator as a method, each object knows how to return an iterator for itself.

The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is defined with a fat arrow () => { ... }. What is the value of this within that function?

Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that’s where this is bound to the value of stack.

Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter().

And here’s a sum function implemented as a fold over a functional iterator: **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0; **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } We can use it with our stack: _(javascriptallonge.pdf (source-range-83ecb080-00249))_

- 186

Served by the Pot: Collections **const** stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) _//=> 6_

We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method: **const** collectionSum = (collection) => { **const** iterator = collection.iterator(); **let** eachIteration, sum = 0; **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 6_

If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

This is a good thing.

## **iterator objects**

Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators.

In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-00250))_

- 187

Served by the Pot: Collections

Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. Like this: **const** Stack2 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty () { **return this** .index < 0 }, iterator () { **let** iterationIndex = **this** .index; **return** { next () { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } } }); _(javascriptallonge.pdf (source-range-83ecb080-00251))_

- 199

Served by the Pot: Collections

One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:

Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_ We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ]. And if we assign a function to a property, we’ve created a method.

So let’s do that:

Stack3.from = **function** (iterable) { **const** stack = **this** (); **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } Pair1.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next(); **return** done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()) Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: **const** numberList = Pair1.from(untilWith((x) => x > 10, Numbers));

Pair1.from(Squares) _//=> {"first":0,_ "rest":{"first":1, "rest":{"first":4, "rest":{ ... _(javascriptallonge.pdf (source-range-83ecb080-00263))_

- Served by the Pot: Collections

200

## **summary**

Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _Iterable_ ordered collections can be iterated over or gathered into another collection.

Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-00264))_

### Generating Iterables

- Served by the Pot: Collections

201

## **Generating Iterables**

**==> picture [469 x 314] intentionally omitted <==**

**Banco do Café**

Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. What is there they don’t do well?

Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.

Iterators have to arrange its own state such that when you call them, they compute and return the next item. This seems blindingly obvious and simple. If, for example, you want numbers, you write: _(javascriptallonge.pdf (source-range-83ecb080-00266))_

- Served by the Pot: Collections

207

21 34 55 89 144

...

Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning the natural linear state. In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on.

So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. Whereas the iteration version must make that state explicit.

## **javascript’s generators**

It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible.

We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a _generator_ . To write a generator, we write a function, but we make two changes:

1. We declare the function using the function * syntax. Not a fat arrow. Not a plain function.

2. We don’t return values or output them to console.log. We “yield” values using the yield keyword.

When we invoke the function, we get an iterator object back. Let’s start with the degenerate example, the empty iterator:[91] **function** * empty () {}; empty().next() _//=>_ {"done": **true** } When we invoke empty, we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it’s done immediately.

Generator functions can take an argument. Let’s use that to illustrate yield:

> 91We wrote a _generator declaration_ . We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword, but we don’t need to do that here. _(javascriptallonge.pdf (source-range-83ecb080-00272))_

- Served by the Pot: Collections

211 it “suspends” and the producer starts running. When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next().

Of course, generators need not be implemented exactly as coroutines. For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): **const** oneTwoThree = **function** () { **let** state = 'newborn'; **return** { next () { **switch** (state) { **case** 'newborn': state = 1; **return** {value: 1}; **case** 1: state = 2; **return** {value: 2} **case** 2: state = 3; **return** {value: 3} **case** 3: **return** {done: **true** }; } } } }; But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded.

## **generators and iterables**

Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3. Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-83ecb080-00275))_

- 216

Served by the Pot: Collections

We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use JavaScript’s natural management of state instead of constantly rolling our own.

Of course, we could just as easily write a generator function for Fibonacci numbers: **function** * fibonacci () { **let** a, b; **yield** a = 0; **yield** b = 1; **while** ( **true** ) { [a, b] = [b, a + b] **yield** b; } } **for** ( **const** i **of** fibonacci()) { console.log(i); } _//=>_ 0 1 1 2 3 5 8 13 21 34 55 89 144 ...

## **yielding iterables**

Here’s a first crack at a function that returns an iterable object for iterating over trees: _(javascriptallonge.pdf (source-range-83ecb080-00279))_

### Interactive Generators

- Served by the Pot: Collections

250

## **Interactive Generators**

We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let’s start by looking at a very simple example of a function that can be written statefully.

**==> picture [469 x 313] intentionally omitted <==**

**Coffee and Chess**

Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made.

Let’s take a look at a very simple example, naughts and crosses[99] (We really ought to do something like Chess, but that might be a little out of scope for this chapter). To save space, we’ll ignore rotations and reflections, and we’ll model the first player’s moves as a stream.

The first player will always be o, and they will always place their chequer in the top-left corner, coincidentally numbered o:

> 99https://en.wikipedia.org/wiki/naughts-and-crosses _(javascriptallonge.pdf (source-range-83ecb080-00316))_

- Served by the Pot: Collections

260 } } **break** ; _// ..._ } } **const** aNaughtsAndCrossesGame = generatorNaughtsAndCrosses();

We can then get the first move by calling .next(). Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. If we wanted to pass some state to the generator before it begins, we’d do that with parameters.): aNaughtsAndCrossesGame.next().value

_//=> 0_ aNaughtsAndCrossesGame.next(1).value

_//=> 6_ aNaughtsAndCrossesGame.next(3).value

_//=> 8_ aNaughtsAndCrossesGame.next(7).value

_//=> 4_

Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn’t call us. It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block.

But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data.

## **summary**

We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it’s also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function.

Again, the salient difference is that an “interactive” generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-83ecb080-00326))_


## Technical atoms

### Technical frame 1: Unary

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00102))_

> Recipes with Basic Functions

59

## **Unary**

“Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:

['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_ In that example, it looks exactly like the mapping funct

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00103))_

> 60 **const** unary = (fn) => fn.length === 1

### Technical frame 2: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00147))_

> Composing and Decomposing Data

99

5! = 5 x 4 x 3 x 2 x 1 = 120.

The naïve function for calcuating the factorial of a positive integer follows directly from the definition: **const** factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) _//=> 1_ factorial(5) _//=> 120_ While this is mathematically elegant, it is computational filigree[63] .

Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n *

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00146))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>

### Technical frame 3: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00149))_

> Composing and Decomposing Data

101 **const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_

By writing our parameter list as (n, work = 1) =>, we’re stating that if a second parameter is not provided, work is to be bound to 1. We can do similar things with our other tail-recursive functions: **const** length = ([first, ...rest], numberToBeAdded = 0) => first === **undefined** ? numberToBeAdded : length(rest, 1 + numberToB

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00150))_

> 102 **const** [first, second = "two"] = ["one"];

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00076))_

> 40 The first sip: Basic Functions **function** (n) { **return** (1.618**n - -1.618**-n) / 2.236; } This still does not _name_ a function, but as we noted above, functions written with the function keyword have an optional “something else.” Could that “something else” name a function? Yes, of course.[33] Here are our example functions written with names: **const** repeat = **function** repeat (str) { **return** str + str; }; **const** fib = **function** fib (n) { **return** (1.618**n - -1.618**-n

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00075))_

| entry | content |
| --- | --- |
| 1 | We introduce a function with the function keyword. |
| 2 | Something else we’re about to discuss is optional. |
| 3 | We have arguments in parentheses, just like fat arrow functions. |
| 4 | We do not have a fat arrow, we go directly to the body. |
| 5 | We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g. |

<details>
<summary>Raw table text</summary>

```
Naming Functions
The first sip: Basic Functions 

39 

## **Naming Functions** 

Let’s get right to it. This code does _not_ name a function: 

**const** repeat = (str) => str + str 

It doesn’t name the function “repeat” for the same reason that const answer = 42 doesn’t name the number 42. This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. 

## **the function keyword** 

JavaScript _does_ have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. 

Here’s our repeat function written using a “fat arrow” 

(str) => str + str 

And here’s (almost) the exact same function written using the function keyword: 

**function** (str) { **return** str + str } 

Let’s look at the obvious differences: 

1. We introduce a function with the function keyword. 

2. Something else we’re about to discuss is optional. 

3. We have arguments in parentheses, just like fat arrow functions. 

4. We do not have a fat arrow, we go directly to the body. 

5. We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword 

If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g. 

(n) => (1.618**n - -1.618**-n) / 2.236 

Can be written as:
```

</details>

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00118))_

| entry | content |
| --- | --- |
| 0 | ? 'Hello' : 'Good bye' _//=> 'Good bye'_ The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. Our logical operators !, &&, and \|\| are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser(), this is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user. Thus, !! is the way we write “is truthy” in JavaScript. How about && and \|\|? What haven’t we discussed? First, and unlike !, && and \|\| do not necessarily evaluate to true or false. To be precise: - && evaluates its left-hand expression. - If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression. - If its left-hand expression evaluates to something truthy, && evaluates its right-hand expression and returns the value of the right-hand expression. - \|\| evaluates its left-hand expression. - If its left-hand expression evaluates to something truthy, \|\| returns the value of its lefthand expression without evaluating its right-hand expression. - If its left-hand expression evaluates to something false, \|\| evaluates its right-hand expression and returns the value of the right-hand expression. If we look at our examples above, we see that when we pass true and false to && and \|\|, we do indeed get true or false as a result. But when we pass other values, we no longer get true or false: |
| 1 | - [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' _//=> 'Pentatonic'_ **const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; ## **truthiness and operators** !5 _//=> false_ ! **undefined** _//=> true_ Picking the Bean: Choice and Truthiness 74 \|\| 2 _//=> 1_ In JavaScript, && and \|\| aren’t boolean logical operators in the logical sense. They don’t operate strictly on logical values, and they don’t commute: a \|\| b is not always equal to b \|\| a, and the same goes for &&. This is not a subtle distinction. We’ve seen the ternary operator: It is a _control-flow_ operator, not a logical operator. The same is true of && and \|\|. Consider this tail-recursive function that determines whether a positive integer is even: |

<details>
<summary>Raw table text</summary>

```
Picking the Bean: Choice and Truthiness
## **Picking the Bean: Choice and Truthiness** 

**==> picture [469 x 264] intentionally omitted <==**

**Decaf and the Antidote** 

We’ve seen operators that act on numeric values, like + and %. In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. Is this array empty? Does this person have a middle name? Is this user logged in? 

JavaScript does have “boolean” values, they’re written true and false: 

## **true** 

_//=> true_ 

## **false** 

_//=> false_ 

true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. To being with, ! is a unary prefix operator that negates its argument. So:
Picking the Bean: Choice and Truthiness 

72 

! **true** _//=> false_ ! **false** _//=> true_ 

The && and || operators are binary infix operators that perform “logical and” and “logical or” respectively: 

**false** && **false** _//=> false_ **false** && **true** _//=> false_ **true** && **false** _//=> false_ **true** && **true** _//=> true_ **false** || **false** _//=> false_ **false** || **true** _//=> true_ **true** || **false** _//=> true_ **true** || **true** _//=> true_ 

Now, note well: We have said what happens if you pass boolean values to !, &&, and ||, but we’ve said nothing about expressions or about passing other values. We’ll look at those presently. 

## **truthiness and the ternary operator** 

In JavaScript, there is a notion of “truthiness.” Every value is either “truthy” or “falsy.” Obviously, false is falsy. So are null and undefined, values that semantically represent “no value.” NaN is falsy, a value representing the result of a calculation that is not a number.[54] And there are more: 0 is falsy, a value representing “none of something.” The empty string, '' is falsy, a value representing having no characters. 

Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) 

The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on _truthiness_ , not on boolean values. This affects the way the !, &&, and || operators work. We’ll look at them in a moment, but first, we’ll look at one more operator. 

JavaScript inherited an operator from the C family of languages, the _ternary_ operator. It’s the only operator that takes _three_ arguments. It looks like this: first ? second : third. It evaluates first, 

> 54We will not discuss JavaScript’s numeric behaviour in much depth in this book, but the most important thing to know is that it implements the IEEE Standard for Floating-Point Arithmetic (IEEE 754), a technical standard for floating-point computation established in 1985 by the Institute of Electrical and Electronics Engineers (IEEE).
73 

Picking the Bean: Choice and Truthiness 

and if first is “truthy”, it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. 

This is a lot like the if statement, however it is an _expression_ , not a statement, and that can be very valuable. It also doesn’t introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. 

Here’re some simple examples of the ternary operator: 

**true** ? 'Hello' : 'Good bye' 

_//=> 'Hello'_ 

- 0 ? 'Hello' : 'Good bye' _//=> 'Good bye'_ 

- [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' _//=> 'Pentatonic'_ 

The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: 

**const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; 

We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. 

## **truthiness and operators** 

Our logical operators !, &&, and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: 

!5 

_//=> false_ 

! **undefined** 

_//=> true_ 

Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser(), this
Picking the Bean: Choice and Truthiness 

74 

is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user. 

Thus, !! is the way we write “is truthy” in JavaScript. How about && and ||? What haven’t we discussed? 

First, and unlike !, && and || do not necessarily evaluate to true or false. To be precise: 

- && evaluates its left-hand expression. 

   - If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression. 

   - If its left-hand expression evaluates to something truthy, && evaluates its right-hand expression and returns the value of the right-hand expression. 

- || evaluates its left-hand expression. 

   - If its left-hand expression evaluates to something truthy, || returns the value of its lefthand expression without evaluating its right-hand expression. 

   - If its left-hand expression evaluates to something false, || evaluates its right-hand expression and returns the value of the right-hand expression. 

If we look at our examples above, we see that when we pass true and false to && and ||, we do indeed get true or false as a result. But when we pass other values, we no longer get true or false: 

1 || 2 _//=> 1_ 

**null** && **undefined** 

_//=> null_ 

**undefined** && **null** 

_//=> undefined_ 

In JavaScript, && and || aren’t boolean logical operators in the logical sense. They don’t operate strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the same goes for &&. 

This is not a subtle distinction. 

## **|| and && are control-flow operators** 

We’ve seen the ternary operator: It is a _control-flow_ operator, not a logical operator. The same is true of && and ||. Consider this tail-recursive function that determines whether a positive integer is even: 

For example:
```

</details>


## Related pages

- [[javascriptallonge-function-decorator]] - narrower topic: Function Decorator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from About JavaScript Allongé: ii  A Pull of the Lever: Prefaces  ## **About JavaScript Allongé**  JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s writ ... [truncated]; Javascript shares technical record from Unary: 60 **const** unary = (fn) => fn.length === 1 (7 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms: Mapwith shares source evidence from Building Blocks: The first sip: Basic Functions  49  ## **partial application**  Another basic building block is _partial application_ . When a function takes multiple arguments, we ... [truncated]; Mapwith shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (4 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  45  ## **Combinators and Function Decorators**  ## **higher-order functions**  As we’ve seen, JavaScript functions take values as arg ... [truncated]; Argument shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-const]] - shared statements and technical atoms: Const shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated]; Const shares technical table: Naming Functions The first sip: Basic Functions  39  ## **Naming Functions**  Let’s get right to it. This code does _not_ name a function:  **const** repeat = (str) ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-length]] - shared statements and technical atoms: Length shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  88 its .length. But as an exercise, how would we write a length function using just what we have already?  First, we pick what we cal ... [truncated]; Length shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (3 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-learn]] - shared statements and technical atoms: Learn shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated]; Learn shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-choice]] - shared technical atoms: Choice shares technical table: Picking the Bean: Choice and Truthiness ## **Picking the Bean: Choice and Truthiness**  **==> picture [469 x 264] intentionally omitted <==**  **Decaf and the Antido ... [truncated] (1 shared atom(s))
- [[javascriptallonge-coffee]] - shared technical atoms: Coffee shares technical table: Naming Functions The first sip: Basic Functions  39  ## **Naming Functions**  Let’s get right to it. This code does _not_ name a function:  **const** repeat = (str) ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recursion]] - shared technical atoms: Recursion shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (5 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (5 shared statement(s))
- [[javascriptallonge-declaration]] - shared statements: Declaration shares source evidence from That Constant Coffee Craving: 43  The first sip: Basic Functions  ( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Althou ... [truncated] (4 shared statement(s))
- [[javascriptallonge-pure]] - shared statements: Pure shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated] (4 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  45  ## **Combinators and Function Decorators**  ## **higher-order functions**  As we’ve seen, JavaScript functions take values as arg ... [truncated] (4 shared statement(s))
- [[javascriptallonge-apply]] - shared statements: Apply shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  8  I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really count ... [truncated] (3 shared statement(s))
- [[javascriptallonge-generator]] - shared statements: Generator shares source evidence from Generating Iterables: Served by the Pot: Collections  207  21 34 55 89 144  ...  Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning ... [truncated] (3 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (3 shared statement(s))
- [[javascriptallonge-variable]] - shared statements: Variable shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated] (3 shared statement(s))
- [[javascriptallonge-alway]] - shared statements: Alway shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated] (2 shared statement(s))
- [[javascriptallonge-closure]] - shared statements: Closure shares source evidence from Closures and Scope: The first sip: Basic Functions  22  ## **if functions without free variables are pure, are closures impure?**  The function (y) => x is interesting. It contains a _f ... [truncated] (2 shared statement(s))
- [[javascriptallonge-data]] - shared statements: Data shares source evidence from Functional Iterators: 145  Composing and Decomposing Data **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldArrayWith = (fn, termin ... [truncated] (2 shared statement(s))
- [[javascriptallonge-decorator]] - shared statements: Decorator shares source evidence from About JavaScript Allongé: ii  A Pull of the Lever: Prefaces  ## **About JavaScript Allongé**  JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s writ ... [truncated] (2 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from Closures and Scope: The first sip: Basic Functions  24  The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its argument ... [truncated] (2 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  167  We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a databa ... [truncated] (2 shared statement(s))
- [[javascriptallonge-iteration]] - shared statements: Iteration shares source evidence from Iteration and Iterables: 186  Served by the Pot: Collections **const** stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) _//=> 6_  We could save a ... [truncated] (2 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from Closures and Scope: The first sip: Basic Functions  24  The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its argument ... [truncated] (2 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Iteration and Iterables: 186  Served by the Pot: Collections **const** stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) _//=> 6_  We could save a ... [truncated] (2 shared statement(s))
- [[javascriptallonge-pass]] - shared statements: Pass shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (2 shared statement(s))
- [[javascriptallonge-second]] - shared statements: Second shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  157  K(I)(6)(7) _//=> 7_  K(I)(12)(24) _//=> 24_  Aha! Given two values, K(I) always returns the _second_ value.  K("primus")("secund ... [truncated] (2 shared statement(s))
- [[javascriptallonge-start]] - shared statements: Start shares source evidence from Functional Iterators: Composing and Decomposing Data  150 **const** FibonacciIterator = () => { **let** previous = 0, current = 1; **return** () => { **const** value = current; [previous, ... [truncated] (2 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  8  I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really count ... [truncated] (2 shared statement(s))
- [[javascriptallonge-allong]] - shared statements: Allong shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (1 shared statement(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  91 **const** truthyAll = ([first, ...rest]) => first === **undefined**  ? [] : [!!first, ...truthyAll(rest)]; truthyAll([ **null** , ... [truncated] (1 shared statement(s))
- [[javascriptallonge-bound]] - shared statements: Bound shares source evidence from That Constant Coffee Craving: 30  The first sip: Basic Functions ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_  We can bind any expression. Functions ... [truncated] (1 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-combinator]] - shared statements: Combinator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Iteration and Iterables: 187  Served by the Pot: Collections  Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get t ... [truncated] (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements: Expression shares source evidence from Magic Names: 52  The first sip: Basic Functions **const** plus = **function** () { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_  When discussing objects, we’ll di ... [truncated] (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  91 **const** truthyAll = ([first, ...rest]) => first === **undefined**  ? [] : [!!first, ...truthyAll(rest)]; truthyAll([ **null** , ... [truncated] (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-method]] - shared statements: Method shares source evidence from Generating Iterables: Served by the Pot: Collections  201  ## **Generating Iterables**  **==> picture [469 x 314] intentionally omitted <==**  **Banco do Café**  Iterables look cool, but ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-purpose]] - shared statements: Purpose shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-recall]] - shared statements: Recall shares source evidence from Iteration and Iterables: 199  Served by the Pot: Collections  One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in ... [truncated] (1 shared statement(s))
- [[javascriptallonge-structure]] - shared statements: Structure shares source evidence from Functional Iterators: 145  Composing and Decomposing Data **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldArrayWith = (fn, termin ... [truncated] (1 shared statement(s))
- [[javascriptallonge-whenever]] - shared statements: Whenever shares source evidence from Closures and Scope: The first sip: Basic Functions  23  ## **it’s always the environment**  To understand how closures are evaluated, we need to revisit environments. As we’ve said befo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-writing]] - shared statements: Writing shares source evidence from Generating Iterables: 216  Served by the Pot: Collections  We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
