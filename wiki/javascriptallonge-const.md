---
page_id: javascriptallonge-const
page_kind: concept
summary: Const: 15 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-const@566fd9ea39cccc5024a935ad63f05d50
---

# Const

What [[javascriptallonge]] covers about const:

## Statements

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

### Combinators and Function Decorators

- The first sip: Basic Functions

47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress. But like compose, we could write either: **const** something = (x) => x != **null** ; And elsewhere, write: **const** nothing = (x) => !something(x); Or we could write: **const** nothing = not(something); not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. You’ll see other function decorators in the recipes, like once and maybe. Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00084))_

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

### Arrays and Destructuring Arguments

- Composing and Decomposing Data

80 **const** x = [], a = [x]; a[0] === x

_//=> true, arrays store references to the things you put in them._

## **destructuring arrays**

There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name: **const** wrap = (something) => [something];

Let’s expand it to use a block and an extra name: **const** wrap = (something) => { **const** wrapped = [something]; **return** wrapped; } wrap("package") _//=> ["package"]_ The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right: **const** unwrap = (wrapped) => { **const** [something] = wrapped; **return** something; } unwrap(["present"]) _//=> "present"_

The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-83ecb080-00126))_

- Composing and Decomposing Data

83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore: **const** [what] = []; what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_ And if there aren’t any items to assign with ..., JavaScript assigns an empty array: **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_ From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

## **destructuring and return values**

Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring: _(javascriptallonge.pdf (source-range-83ecb080-00129))_

### Plain Old JavaScript Objects

- 117

Composing and Decomposing Data

Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away.

Mind you, this is still much, much faster than making partial copies of arrays. For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-00167))_

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

127 {age: 49, '..': global-environment} However, if we don’t shadow age with let, reassigning within the block changes the original: (() => { **let** age = 49; **if** ( **true** ) { age = 50; } **return** age; })() _//=> 50_

Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

## **mixing let and const**

Some programmers dislike deliberately shadowing variables. The suggestion is that shadowing a variable is confusing code. If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around.

If you dislike deliberately shadowing variables, you’ll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable: (() => { **let** age = 49; **if** ( **true** ) { **const** age = 50; } age = 51; **return** age; })() _//=> 51_

Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And: _(javascriptallonge.pdf (source-range-83ecb080-00179))_

- Composing and Decomposing Data

131 **const** factorial = (n) => { **let** innerFactorial = **undefined** ; **return** innerFactorial(n, 1); innerFactorial = **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } } factorial(4) _//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')_ In that way, var is a little like const and let, we should always declare and bind names before using them. But it’s not like const and let in that it’s function scoped, not block scoped.

## **why const and let were invented**

const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). However, its functional scope was a problem.

We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var: **var** sum = 0; **for** ( **var** i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050

Hopefully, you can think of a faster way to calculate this sum.[72] And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

> 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . . . . + 99 + 100 = ? But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . . . . + (50 + 51) = ? If you notice every pair of numbers adds up to 101. There are 50 pairs of numbers, so the answer is 50*101 = 5050. Of course Gauss came up with the answer about 20 times faster than the other kids. _(javascriptallonge.pdf (source-range-83ecb080-00183))_

### Copy on Write

- Composing and Decomposing Data

140

Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] Like all strategies, it makes a tradeoff: It’s much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren’t sharing, it’s more expensive.

Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write.

> 73https://en.wikipedia.org/wiki/Copy-on-write _(javascriptallonge.pdf (source-range-83ecb080-00193))_


## Technical atoms

### Technical atom 1

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


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated]; Function shares technical table: Naming Functions The first sip: Basic Functions  39  ## **Naming Functions**  Let’s get right to it. This code does _not_ name a function:  **const** repeat = (str) ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-coffee]] - shared technical atoms: Coffee shares technical table: Naming Functions The first sip: Basic Functions  39  ## **Naming Functions**  Let’s get right to it. This code does _not_ name a function:  **const** repeat = (str) ... [truncated] (1 shared atom(s))
- [[javascriptallonge-statement]] - shared statements: Statement shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (4 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (3 shared statement(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  80 **const** x = [], a = [x]; a[0] === x  _//=> true, arrays store references to the things you put in them._  ## **destructuring arr ... [truncated] (2 shared statement(s))
- [[javascriptallonge-bound]] - shared statements: Bound shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (2 shared statement(s))
- [[javascriptallonge-alway]] - shared statements: Alway shares source evidence from That Constant Coffee Craving: The first sip: Basic Functions  37 })(2) _//=> 6.2831853_  Ah! const statements don’t just shadow values bound within the environments created by functions, they sha ... [truncated] (1 shared statement(s))
- [[javascriptallonge-bind]] - shared statements: Bind shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-binding]] - shared statements: Binding shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-block]] - shared statements: Block shares source evidence from Summary: The first sip: Basic Functions  55  ## **Summary**  **==> picture [29 x 29] intentionally omitted <==**  ## **Functions**  - Functions are values that can be part of ... [truncated] (1 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated] (1 shared statement(s))
- [[javascriptallonge-parameter]] - shared statements: Parameter shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-variable]] - shared statements: Variable shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-writing]] - shared statements: Writing shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
