---
page_id: javascriptallonge-section-that-constant-coffee-craving-744fb942
page_kind: source
summary: That Constant Coffee Craving: 92 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-that-constant-coffee-craving-744fb942@2a9168495bfb5910fb4a6ab2cf92f175
---

# That Constant Coffee Craving

From [[javascriptallonge]].

## Statements

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
- 27

The first sip: Basic Functions ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_

((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_ That works! We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind.[29]

## **inside-out**

There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: (diameter) => ((PI) => diameter * PI)(3.14159265) It produces the same result as our previous expressions for a diameter-calculating function: ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_ ((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_ ((diameter) => ((PI) => diameter * PI)(3.14159265))(2) _//=> 6.2831853_ Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A “magic literal” like 3.14159265 is anathema to sustainable software development.

The third one is easiest for most people to read. It separates concerns nicely: The “outer” function describes its parameters:

> 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated “IIFE.” _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- The first sip: Basic Functions

28

- (diameter) => _// ..._

Everything else is encapsulated in its body. That’s how it should be, naming PI is its concern, not ours. The other formulation:

((PI) => _// ..._ )(3.14159265) “Exposes” naming PI first, and we have to look inside to find out why we care. So, should we should always write this?

- (diameter) => ((PI) => diameter * PI)(3.14159265) Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we’ll invoke the inner function. We could get around this by writing

((PI) => (diameter) => diameter * PI )(3.14159265) But then we’ve obfuscated our code, and we don’t want to do that unless we absolutely have to.

What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. And JavaScript does.

## **const**

Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this: (diameter, PI) => diameter * PI And we could use it like this: _(javascriptallonge.pdf (source-range-83ecb080-00064))_
- 29

The first sip: Basic Functions ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_

This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name.

JavaScript gives us a way to do that, the const keyword. We’ll learn a lot more about const in future chapters, but here’s the most important thing we can do with const: (diameter) => { **const** PI = 3.14159265; **return** diameter * PI } The const keyword introduces one or more bindings in the block that encloses it. It doesn’t incur the cost of a function invocation. That’s great. Even better, it puts the symbol (like PI) close to the value (3.14159265). That’s much better than what we were writing.

We use the const keyword in a _const statement_ . const statements occur inside blocks, we can’t use them when we write a fat arrow that has an expression as its body.

It works just as we want. Instead of: ((diameter) => ((PI) => diameter * PI)(3.14159265))(2) Or: ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_

We write: _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- 30

The first sip: Basic Functions ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_

We can bind any expression. Functions are expressions, so we can bind helper functions: (d) => { **const** calc = (diameter) => { **const** PI = 3.14159265; **return** diameter * PI }; **return** "The circumference is " + calc(d) } Notice calc(d)? This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with (). A name that’s bound to a function is a valid expression evaluating to a function.[30] Amazing how such an important idea–naming functions–can be explained _en passant_ in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as “first class entities.” Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

We can bind more than one name-value pair by separating them with commas. For readability, most people put one binding per line: (d) => { **const** PI = 3.14159265, calc = (diameter) => diameter * PI; **return** "The circumference is " + calc(d) } > 30We’re into the second chapter and we’ve finally named a function. Sheesh. _(javascriptallonge.pdf (source-range-83ecb080-00066))_
- The first sip: Basic Functions

31

## **nested blocks**

Up to now, we’ve only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) } And it works for fairly small numbers: ((n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) })(13) _//=> false_

The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else** { **const** odd = (y) => !even(y); **return** odd(x - 1); } _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- 32

The first sip: Basic Functions } **return** even(n) } And this also works: ((n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else** { **const** odd = (y) => !even(y); **return** odd(x - 1); } } **return** even(n) })(42) _//=> true_

We’ve used a block as the else clause, and since it’s a block, we’ve placed a const statement inside it.

## **const and lexical scope**

This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we’re to place const anywhere we like. The first thing to ask ourselves is, what happens if we use const to bind two different values to the “same” name?

Let’s back up and reconsider how closures work. What happens if we use parameters to bind two different values to the same name?

Here’s the second formulation of our diameter function, bound to a name using an IIFE: ((diameter_fn) => _// ..._ )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. We can use any expression in there, and that expression can invoke diameter_fn. For example: _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- 33

The first sip: Basic Functions ((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_

We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn.

This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where diameter_fn is invoked.

We can test this by deliberately creating a “conflict:” ((diameter_fn) => ((PI) => diameter_fn(2) )(3) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_ Although we have bound 3 to PI in the environment surrounding diameter_fn(2), the value that counts is 3.14159265, the value we bound to PI in the environment surrounding (diameter) _⇒_ diameter * PI.

That much we can carefully work out from the way closures work. Does const work the same way? Let’s find out:

31https://en.wikipedia.org/wiki/Scope_(computer_science)#Lexical_scope_vs._dynamic_scope _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- 34

The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => diameter * PI })() ) _//=> 6.2831853_

Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.

## **are consts also from a shadowy planet?**

We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions.

But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block?

We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other.

Let’s start, as above, by doing this with parameters. We’ll start with:

((PI) => (diameter) => diameter * PI )(3.14159265) And gratuitously wrap it in another IIFE so that we can bind PI to something else: _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- 35

The first sip: Basic Functions

((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3) This still evaluates to a function that calculates diameters:

((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)(2) _//=> 6.2831853_ And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the “outer” environment? Let’s rewrite things slightly differently:

((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265) Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding:

((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)(2) _//=> 6.2831853_

We say that when we bind a variable using a parameter inside another binding, the inner binding _shadows_ the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

So what about const. Does it work the same way? _(javascriptallonge.pdf (source-range-83ecb080-00071))_
- 36

The first sip: Basic Functions ((diameter) => { **const** PI = 3.14159265; (() => { **const** PI = 3; })(); **return** diameter * PI; })(2) _//=> 6.2831853_

Yes, names bound with const shadow enclosing bindings just like parameters. But wait! There’s more!!!

Parameters are only bound when we invoke a function. That’s why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block?

We’ll need a gratuitous block. We’ve seen if statements, what could be more gratuitous than: **if** ( **true** ) { _// an immediately invoked block statement (IIBS)_ } Let’s try it: ((diameter) => { **const** PI = 3; **if** ( **true** ) { **const** PI = 3.14159265; **return** diameter * PI; } })(2) _//=> 6.2831853_ ((diameter) => { **const** PI = 3.14159265; **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- The first sip: Basic Functions

37 })(2) _//=> 6.2831853_

Ah! const statements don’t just shadow values bound within the environments created by functions, they shadow values bound within environments created by blocks!

This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: ((diameter) => { **const** PI = 3.14159265; **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_

If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:” ((diameter) => { **if** ( **true** ) { **const** PI = 3.14159265; } **return** diameter * PI; })(2) _//=> would return 6.2831853 if const had function scope_ Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not “leaking” its binding to other parts of the code that do not need to interact with it.

## **rebinding**

By default, JavaScript permits us to _rebind_ new values to names bound with a parameter. For example, we can write:

> 32https://en.wikipedia.org/wiki/Principle_of_least_privilege _(javascriptallonge.pdf (source-range-83ecb080-00073))_
- 38

The first sip: Basic Functions **const** evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { n = n - 2; **return** evenStevens(n); } } evenStevens(42) _//=> true_

The line n = n - 2; _rebinds_ a new value to the name n. We will discuss this at much greater length in Reassignment, but long before we do, let’s try a similar thing with a name bound using const. We’ve already bound evenStevens using const, let’s try rebinding it: evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { **return** evenStevens(n - 2); } } _//=> ERROR, evenStevens is read-only_ JavaScript does not permit us to rebind a name that has been bound with const. We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const, we need never worry that its value may change. _(javascriptallonge.pdf (source-range-83ecb080-00074))_
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
- There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind.[29] There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00064))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- Up to now, we’ve only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- We’ve used a block as the else clause, and since it’s a block, we’ve placed a const statement inside it. _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00071))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00073))_
- If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. _(javascriptallonge.pdf (source-range-83ecb080-00073))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-83ecb080-00080))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00080))_

## Technical atoms

### Technical frame 1: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00068))_

> 32

The first sip: Basic Functions } **return** even(n) } And this also works: ((n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else** { **const** odd = (y) => !even(y); **return** odd(x - 1); } } **return** even(n) })(42) _//=> true_

We’ve used a block as the else clause, and since it’s a block, we’ve placed a const statement inside it.

## **const and lexical scope**

This seems very straightforward, but alas, there are some semantics of binding names that we need to u

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00067))_

> One of the places you can find blocks is in an if statement.

### Technical frame 2: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00079))_

> 43

The first sip: Basic Functions

( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })() The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). This behaviour is in

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00078))_

> The first sip: Basic Functions
> 
> 42 even _//=> Can't find variable: even_ even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don’t _need_ to name it anywhere else, you needn’t.
> 
> ## **function declarations**
> 
> There is another syntax for naming and/or defining a function. It’s called a _function declaration statement_ , and it looks a lot like a named function expression, only we use it as a statement: **function** someName () { _// ..._ } This behaves a _little_ like: **const** someName = **function** someName () { _// ..._ } In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are _hoisted_ to the top of the function in which they occur.
> 
> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:
> 
> ( **function** () { **return** fizzbuzz(); **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> undefined is not a function (evaluating 'fizzbuzz()')_ We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function _declaration_ works differently:

### Technical frame 3: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00079))_

> 43

The first sip: Basic Functions

( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })() The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). This behaviour is in

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00080))_

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

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
