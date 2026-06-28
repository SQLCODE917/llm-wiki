---
page_id: javascriptallonge-function
page_kind: concept
summary: Function: 109 statement(s) and 136 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function@210122465642c0d5258b7739c75485fc
---

# Function

What [[javascriptallonge]] covers about function:

## Statements

### About JavaScript Allongé

- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript's power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-31a4cf47-00018))_

### why the 'six' edition?

- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write: _(javascriptallonge.pdf (source-range-31a4cf47-00028))_

### michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-31a4cf47-00087))_

### As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-31a4cf47-00172))_

- What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else. _(javascriptallonge.pdf (source-range-31a4cf47-00176))_

### functions that return values and evaluate expressions

- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-31a4cf47-00200))_

### void

- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21 _(javascriptallonge.pdf (source-range-31a4cf47-00239))_

### functions that evaluate to functions

- That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . So we have a function, that returns a function, that returns zero . Likewise: _(javascriptallonge.pdf (source-range-31a4cf47-00264))_

### Ah. I'd Like to Have an Argument, Please. 22

- This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body: _(javascriptallonge.pdf (source-range-31a4cf47-00277))_

### call by value

- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . Then our circumference function was applied to 2 . 24 _(javascriptallonge.pdf (source-range-31a4cf47-00298))_

### variables and bindings

- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary that maps variables to values by name. The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-31a4cf47-00306))_

- How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write: _(javascriptallonge.pdf (source-range-31a4cf47-00308))_

- The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-31a4cf47-00318))_

### if functions without free variables are pure, are closures impure?

- Functions containing no free variables are called pure functions . _(javascriptallonge.pdf (source-range-31a4cf47-00348))_

- Functions containing one or more free variables are called closures . _(javascriptallonge.pdf (source-range-31a4cf47-00349))_

- Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: _(javascriptallonge.pdf (source-range-31a4cf47-00350))_

- The first function doesn't have any variables, therefore doesn't have any free variables. The second doesn't have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ... , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... . _(javascriptallonge.pdf (source-range-31a4cf47-00351))_

- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-31a4cf47-00352))_

- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . _(javascriptallonge.pdf (source-range-31a4cf47-00355))_

### it's always the environment

- To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ? Let's fill in the blanks! _(javascriptallonge.pdf (source-range-31a4cf47-00358))_

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-31a4cf47-00369))_

### which came first, the chicken or the egg?

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-31a4cf47-00381))_

### That Constant Coffee Craving

- This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 . _(javascriptallonge.pdf (source-range-31a4cf47-00395))_

### const

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-31a4cf47-00418))_

- Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30 _(javascriptallonge.pdf (source-range-31a4cf47-00435))_

- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-31a4cf47-00436))_

### Naming Functions

- It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-31a4cf47-00504))_

### the function keyword

- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

- Now, the function's actual name has no effect on the environment in which it is used. To whit: _(javascriptallonge.pdf (source-range-31a4cf47-00532))_

- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-31a4cf47-00534))_

### function declarations

- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-31a4cf47-00543))_

- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently: _(javascriptallonge.pdf (source-range-31a4cf47-00546))_

### function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-31a4cf47-00551))_

- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-31a4cf47-00554))_

### higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-31a4cf47-00560))_

### a balanced statement about combinators

- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-31a4cf47-00579))_

### partial application

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-31a4cf47-00598))_

### Magic Names

- When a function is applied to arguments (or 'called'), JavaScript binds the values of arguments to the function's argument names in an environment created for the function's execution. What we haven't discussed so far is that JavaScript also binds values to some 'magic' names in addition to any you put in the argument list. 42 _(javascriptallonge.pdf (source-range-31a4cf47-00606))_

### magic names and fat arrows

- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-31a4cf47-00621))_

- Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code. _(javascriptallonge.pdf (source-range-31a4cf47-00632))_

- But sometimes, a function is a small-f function. It's a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-31a4cf47-00633))_

- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith . _(javascriptallonge.pdf (source-range-31a4cf47-00634))_

### Functions

- Functions are values that can be part of expressions, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-31a4cf47-00638))_

- Functions are reference values . _(javascriptallonge.pdf (source-range-31a4cf47-00639))_

- Functions are applied to arguments. _(javascriptallonge.pdf (source-range-31a4cf47-00640))_

- Fat arrow functions have expressions or blocks as their bodies. _(javascriptallonge.pdf (source-range-31a4cf47-00642))_

- function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-31a4cf47-00643))_

- Function bodies have zero or more statements. _(javascriptallonge.pdf (source-range-31a4cf47-00644))_

### Unary

- If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: _(javascriptallonge.pdf (source-range-31a4cf47-00674))_

### Maybe

- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-31a4cf47-00698))_

- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-31a4cf47-00700))_

### Once

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-31a4cf47-00710))_

### Left-Variadic Functions

- A variadic function is a function that is designed to accept a variable number of arguments. 52 In JavaScript, you can make a variadic function by gathering parameters. For example: _(javascriptallonge.pdf (source-range-31a4cf47-00717))_

### overcoming limitations

- That's a left-variadic function . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn't do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function? _(javascriptallonge.pdf (source-range-31a4cf47-00735))_

- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right. _(javascriptallonge.pdf (source-range-31a4cf47-00739))_

### left-variadic destructuring

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-31a4cf47-00741))_

### function parameters are eager

- In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated : _(javascriptallonge.pdf (source-range-31a4cf47-00801))_

### summary

- Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-31a4cf47-00811))_

### Self-Similarity

- Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

### mapping

- Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-31a4cf47-00933))_

### folding

- With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn't. A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-31a4cf47-00936))_

- And now we supply a function that does slightly more than our mapping functions: _(javascriptallonge.pdf (source-range-31a4cf47-00943))_

- Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code: _(javascriptallonge.pdf (source-range-31a4cf47-00945))_

### Tail Calls (and Default Arguments)

- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not 'production-ready' implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-31a4cf47-00954))_

### tail-call optimization

- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-31a4cf47-00974))_

### converting non-tail-calls to tail-calls

- Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-31a4cf47-00986))_

### factorials

- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-31a4cf47-00999))_

### mutation and data structures

- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-31a4cf47-01143))_

### var

- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-31a4cf47-01194))_

- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-31a4cf47-01200))_

### why const and let were invented

- const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-31a4cf47-01202))_

### Yes. Consider this variation:

- Now, at the time we created each function, i had a sensible value, like 0 , 1 , or 2 . But at the time we call one of the functions, i has the value 3 , which is why the loop terminated. So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . That's not what we want at all. _(javascriptallonge.pdf (source-range-31a4cf47-01215))_

### copy-on-read

- As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy because we won't be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-31a4cf47-01242))_

### copy-on-write

- And now functions like that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-31a4cf47-01251))_

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-31a4cf47-01255))_

### Functional Iterators

- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-31a4cf47-01280))_

### iterating

- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-31a4cf47-01294))_

### unfolding and laziness

- A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-31a4cf47-01303))_

### caveat

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-31a4cf47-01324))_

### Making Data Out Of Functions

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-31a4cf47-01328))_

### the kestrel and the idiot

- A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K , is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-31a4cf47-01338))_

- The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42 . Very simple, but useful. Now we'll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value. _(javascriptallonge.pdf (source-range-31a4cf47-01341))_

### backwardness

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we'd write them like this: _(javascriptallonge.pdf (source-range-31a4cf47-01354))_

- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-31a4cf47-01358))_

### the vireo

- As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-31a4cf47-01374))_

### functions are not the real point

- Functions are a fundamental building block of computation. They are 'axioms' of combinatory logic, and can be used to compute anything that JavaScript can compute. _(javascriptallonge.pdf (source-range-31a4cf47-01403))_

### a return to backward thinking

- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-31a4cf47-01422))_

### self-currying flip

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip : _(javascriptallonge.pdf (source-range-31a4cf47-01466))_

### Why?

- What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-31a4cf47-01494))_

### evaluation time

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-31a4cf47-01519))_

### a look back at functional iterators

- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-31a4cf47-01543))_

### iterator objects

- Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators. _(javascriptallonge.pdf (source-range-31a4cf47-01546))_

- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-31a4cf47-01548))_

### from

- We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-31a4cf47-01614))_

### summary

- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-31a4cf47-01621))_

### Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-31a4cf47-01626))_

### javascript's generators

- Generator functions can take an argument. Let's use that to illustrate yield : _(javascriptallonge.pdf (source-range-31a4cf47-01669))_

### generators and iterables

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-31a4cf47-01709))_

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-31a4cf47-01715))_

### more generators

- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-31a4cf47-01726))_

### yielding iterables

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-31a4cf47-01732))_

### interactive generators

- But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-31a4cf47-01944))_


## Technical atoms

### Technical frame 1: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00030))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00029))_

```
def foo (first, *rest) # ... end
```

### Technical frame 2: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00174))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00173))_

```
() => 0
```

### Technical frame 3: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00176))_

> What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a br

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00175))_

```
(() => 0) //=> [Function]
```

### Technical frame 4: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00178))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00176))_

> If you try the same thing in a browser, you may see something else.

### Technical frame 5: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00178))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00177))_

> 16 The simplest possible function is () => {} , we'll see that later.

### Technical frame 6: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00197))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00196))_

```
(() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity
```

### Technical frame 7: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00200))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00201))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical frame 8: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00239))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00238))_

```
(() => {})() //=> undefined
```

### Technical frame 9: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00244))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00243))_

```
() => { 2 + 2 } () => { 1 + 1; 2 + 2 }
```

### Technical frame 10: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00246))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00245))_

```
() => { 1 + 1; 2 + 2 }
```

### Technical frame 11: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 12: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00252))_

```
(() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World'
```

### Technical frame 13: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00254))_

```
(() => { 1 + 1; return 2 + 2 })() //=> 4
```

### Technical frame 14: functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00271))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00265))_

```
() => () => true
```

### Technical frame 15: functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00271))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00267))_

```
(() => () => true )()() //=> true
```

### Technical frame 16: Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00277))_

> This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00276))_

```
(room) => {}
```

### Technical frame 17: Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00279))_

> I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . What does one do with the arguments? Use them in the body, of course. What do you think this is?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00278))_

```
(room, board) => {}
```

### Technical frame 18: Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00281))_

> It's a function for calculating the circumference of a circle given the diameter. I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.'

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00280))_

```
(diameter) => diameter * 3.14159265
```

### Technical frame 19: Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00284))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00283))_

```
((diameter) => diameter * 3.14159265)(2) //=> 6.2831853
```

### Technical frame 20: Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00284))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00286))_

```
((room, board) => room + board)(800, 150) //=> 950
```

### Technical frame 21: variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00303))_

> (x) => (y) => x just looks crazy, as if we are learning English as a second language and the teacher promises us that soon we will be using words like antidisestablishmentarianism . Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00302))_

```
(x) => (y) => x
```

### Technical frame 22: variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00317))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00309))_

```
((x) => x)(2) //=> 2
```

### Technical frame 23: if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00355))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00354))_

> If pure functions can contain closures, can a closure contain a pure function?

### Technical frame 24: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00361))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00359))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical frame 25: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00363))_

```
b
```

### Technical frame 26: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00365))_

```
(x) => (y) => (z) => x + y + z
```

### Technical frame 27: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00367))_

```
(x, y, z) => x + y + z
```

### Technical frame 28: which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00386))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00384))_

> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 29: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00395))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00392))_

```
((PI) => // ???? )(3.14159265)
```

### Technical frame 30: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00395))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00394))_

```
((PI) => (diameter) => diameter * PI )(3.14159265)
```

### Technical frame 31: const

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00422))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00419))_

```
(diameter, PI) => diameter * PI
```

### Technical frame 32: const

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00435))_

> Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00434))_

```
(d) => { const calc = (diameter) => { const PI = 3.14159265; return diameter * PI }; return "The circumference is " + calc(d) }
```

### Technical frame 33: const

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00436))_

> Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00435))_

> This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () .

### Technical frame 34: Naming Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00504))_

> It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00503))_

```
const repeat = (str) => str + str
```

### Technical frame 35: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00513))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00508))_

```
(str) => str + str
```

### Technical frame 36: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00513))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00510))_

```
function (str) { return str + str }
```

### Technical frame 37: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00518))_

```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Technical frame 38: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00520))_

```
function (n) { return (1.618**n - -1.618**-n) / 2.236; }
```

### Technical frame 39: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00523))_

```
const repeat = function repeat (str) { return str + str; }; const fib = function fib (n) { return (1.618**n - -1.618**-n) / 2.236; };
```

### Technical frame 40: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00525))_

```
const double = function repeat (str) { return str + str; }
```

### Technical frame 41: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00532))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00531))_

```
someBackboneView.on('click', function clickHandler () { //... });
```

### Technical frame 42: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00534))_

> So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00533))_

```
const bindingName = function actualName () { //... }; bindingName //=> [Function: actualName] actualName //=> ReferenceError: actualName is not defined
```

### Technical frame 43: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00536))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00535))_

```
( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(2) //=> true
```

### Technical frame 44: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00538))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00537))_

```
even //=> Can't find variable: even
```

### Technical frame 45: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00543))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00541))_

```
function someName () { // ... } This behaves a little like: const someName = function someName () // ... }
```

### Technical frame 46: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00543))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00542))_

```
{
```

### Technical frame 47: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00546))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00545))_

```
( function () { return fizzbuzz(); const fizzbuzz = function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> undefined is not a function (evaluating 'fizzbuzz()')
```

### Technical frame 48: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00549))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00547))_

```
( function () { return fizzbuzz(); function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> 'FizzBuzz' Although fizzbuzz is declared later in the function, JavaScript behaves as if we'd written: ( function () { {
```

### Technical frame 49: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00549))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00548))_

```
const fizzbuzz = function fizzbuzz () return "Fizz" + "Buzz"; } return fizzbuzz(); })()
```

### Technical frame 50: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00554))_

> Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00553))_

```
( function (camelCase) { return fizzbuzz(); if (camelCase) { function fizzbuzz () { return "Fizz" + "Buzz"; } } else { function fizzbuzz () { return "Fizz" + "Buzz"; } } })( true ) //=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?
```

### Technical frame 51: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00555))_

> Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00554))_

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

### Technical frame 52: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00557))_

> The parentheses make this an expression, not a function declaration.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00556))_

```
function trueDat () { return true } But this is not: ( function trueDat () { return true })
```

### Technical frame 53: higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00565))_

> In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00562))_

```
const repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)) : undefined repeat(3, function (n) { console.log(`Hello ${ n } `) }) //=> 'Hello 1' 'Hello 2' 'Hello 3' undefined
```

### Technical frame 54: a balanced statement about combinators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00579))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00578))_

```
const nothing = not(something);
```

### Technical frame 55: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00598))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00594))_

```
_.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9]
```

### Technical frame 56: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00598))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00597))_

```
const squareAll = (array) => map(array, (n) => n * n);
```

### Technical frame 57: partial application

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00600))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00599))_

```
const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9]
```

### Technical frame 58: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00623))_

> But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . And thus arguments[0] will refer to "outer" , not to "inner" :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00622))_

```
( function () { return ( function () { return arguments[0]; })('inner'); })('outer') //=> "inner"
```

### Technical frame 59: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00625))_

> Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00624))_

```
( function () { return (() => arguments[0])('inner'); })('outer') //=> "outer"
```

### Technical frame 60: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00628))_

> This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00627))_

```
const row = function () { return mapWith( (column) => column * arguments[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [3,6,9,12,15,18,21,24,27,30,33,36]
```

### Technical frame 61: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00632))_

> Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00630))_

```
const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

### Technical frame 62: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00670))_

```
['1', '2', '3'].map(parseFloat) //=> [1, 2, 3]
```

### Technical frame 63: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical frame 64: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00675))_

```
['1', '2', '3'].map(parseInt) //=> [1, NaN, NaN]
```

### Technical frame 65: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00677))_

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

### Technical frame 66: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00698))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00697))_

```
const isSomething = (value) => value !== null && value !== void 0; const checksForSomething = (value) => { if (isSomething(value)) { // function's true logic } }
```

### Technical frame 67: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00699))_

```
var something = isSomething(value) ? doesntCheckForSomething(value) : value;
```

### Technical frame 68: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00701))_

```
const maybe = (fn) => function (...args) { if (args.length === 0) { return } else { for ( let arg of args) { if (arg == null ) return ; }
```

### Technical frame 69: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00703))_

```
return fn.apply( this , args) } }
```

### Technical frame 70: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00705))_

```
maybe((a, b, c) => a + b + c)(1, 2, 3) //=> 6 maybe((a, b, c) => a + b + c)(1, null , 3) //=> undefined
```

### Technical frame 71: Once

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00711))_

```
const once = (fn) => { let done = false ; return function () { return done ? void 0 : ((done = true ), fn.apply( this , arguments)) } }
```

### Technical frame 72: Once

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00713))_

```
const askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() //=> 'sure, why not?' askedOnBlindDate() //=> undefined askedOnBlindDate() //=> undefined
```

### Technical frame 73: Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00719))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00718))_

```
const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5]
```

### Technical frame 74: Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00721))_

> 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.'

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00720))_

```
function team(coach, captain, ...players) { console.log(` ${ captain } (captain)`); for ( let player of players) { console.log(player); } console.log(`squad coached by ${ coach } `); } team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen', 'Martín Montoya', 'Gerard Piqué') //=> Xavi Hernández (captain) Marc-André ter Stegen Martín Montoya Gerard Piqué squad coached by Luis Enrique But we can't go the other way around:
```

### Technical frame 75: Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00723))_

> ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00722))_

```
function team2(...players, captain, coach) { console.log(` ${ captain } (captain)`); for ( let player of players) { console.log(player); } console.log(`squad coached by ${ coach } `); } //=> Unexpected token
```

### Technical frame 76: left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00742))_

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid']; first //=> 'why' butFirst //=> ["hello","there","little","droid"]
```

### Technical frame 77: left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00748))_

```
const leftGather = (outputArrayLength) => { return function (inputArray) { return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\ at( inputArray.slice(inputArray.length - outputArrayLength + 1) ) } }; const [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\ ']); butLast //=> ['why', 'hello', 'there', 'little'] last //=> 'droid'
```

### Technical frame 78: function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00804))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00802))_

```
const or = (a, b) => a || b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n !== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded.
```

### Technical frame 79: function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00806))_

> Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00805))_

```
const or = (a, b) => a() || b() const and = (a, b) => a() && b() const even = (n) => or(() => n === 0, () => and(() => n !== 1, () => even(n - 2))) even(7) //=> false
```

### Technical frame 80: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00901))_

> We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length !

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00900))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : // ???
```

### Technical frame 81: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00902))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let's try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"])
```

### Technical frame 82: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00903))_

```
//=> 3
```

### Technical frame 83: mapping

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00933))_

> Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00934))_

```
const mapWith = (fn, [first, ...rest]) => first === undefined ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25] mapWith((x) => !!x, [ null , true , 25, false , "foo"]) //=> [false,true,true,false,true]
```

### Technical frame 84: folding

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00937))_

```
const sumSquares = ([first, ...rest]) => first === undefined ? 0 : first * first + sumSquares(rest); sumSquares([1, 2, 3, 4, 5]) //=> 55
```

### Technical frame 85: folding

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00944))_

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5]) //=> 55
```

### Technical frame 86: folding

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00946))_

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\ [], array); squareAll([1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### Technical frame 87: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00957))_

> Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00956))_

```
const mapWith = (fn, [first, ...rest]) => first === undefined ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### Technical frame 88: tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00970))_

> There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00969))_

```
const maybe = (fn) => function (...args) { if (args.length === 0) { return ; } else { for ( let arg of args) { if (arg == null ) return ; } return fn.apply( this , args); } }
```

### Technical frame 89: tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00974))_

> The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00973))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest);
```

### Technical frame 90: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00980))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00979))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysWork(["foo", "bar", "baz"], 0) //=> 3
```

### Technical frame 91: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00981))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) const length = (n) => lengthDelaysWork(n, 0);
```

### Technical frame 92: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00982))_

```
Or we could use partial application: const callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const length = callLast(lengthDelaysWork, 0); length(["foo", "bar", "baz"]) //=> 3
```

### Technical frame 93: factorials

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00993))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00992))_

```
const factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) //=> 1 factorial(5) //=> 120
```

### Technical frame 94: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01193))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01192))_

```
(() => { var age = 49; if ( true ) { var age = 50; } return age; })() //=> 50
```

### Technical frame 95: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01195))_

```
const factorial = (n) => { return innerFactorial(n, 1); function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> 24
```

### Technical frame 96: Yes. Consider this variation:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01213))_

> What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01212))_

```
introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is undefined'
```

### Technical frame 97: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01300))_

```
const NumberIterator = (number = 0) => () => ({ done: false , value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne().value; //=> 3 fromOne().value; //=> 4 fromOne().value; //=> 5
```

### Technical frame 98: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01309))_

> How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01308))_

```
const take = (iterator, numberToTake) => { let count = 0; return () => { if (++count <= numberToTake) { return iterator(); } else { return {done: true }; } }; }; const toArray = (iterator) => { let eachIteration, array = []; while ((eachIteration = iterator(), !eachIteration.done)) { array.push(eachIteration.value); } return array; } toArray(take(FibonacciIterator(), 5)) //=> [1, 1, 2, 3, 5] toArray(take(squares, 5)) //=> [1, 4, 9, 16, 25]
```

### Technical frame 99: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01314))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01313))_

```
const filterIteratorWith = (fn, iterator) => () => { do { const {done, value} = iterator(); } while (!done && !fn(value)); return {done, value}; } const oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1); toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) //=> [1, 9, 25, 49, 81]
```

### Technical frame 100: Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01330))_

> A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01329))_

```
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest.first //=> 2 OneTwoThree.rest.rest.first //=> 3 const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) //=> 3
```

### Technical frame 101: the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01352))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01346))_

```
Therefore, K(I)(x)(y) => y :
```

### Technical frame 102: the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01352))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01347))_

```
K(I)(6)(7) //=> 7 K(I)(12)(24) //=> 24
```

### Technical frame 103: the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01352))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01351))_

```
const first = K, second = K(I); first("primus")("secundus") //=> "primus" second("primus")("secundus") //=> "secundus"
```

### Technical frame 104: backwardness

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01358))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01355))_

```
const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus"
```

### Technical frame 105: the vireo

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01367))_

> For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01366))_

```
(first, second) => (selector) => selector(first)(second)
```

### Technical frame 106: the vireo

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01368))_

```
(first) => (second) => (selector) => selector(first)(second)
```

### Technical frame 107: the vireo

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01370))_

```
const first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second); const latin = pair("primus")("secundus"); latin(first) //=> "primus" latin(second) //=> "secundus"
```

### Technical frame 108: the vireo

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01371))_

> If we change the names to x , y , and z , we get: (x) => (y) => (z) => z(x)(y) .

### Technical frame 109: the vireo

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01373))_

```
const first = K, second = K(I), pair = V; const latin = pair("primus")("secundus"); latin(first) //=> "primus" latin(second) //=> "secundus"
```

### Technical frame 110: a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01416))_

> We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01415))_

```
const length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );
```

### Technical frame 111: a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01419))_

> The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01418))_

```
const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);
```

### Technical frame 112: self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01467))_

```
const flip = (fn) => function (first, second) { if (arguments.length === 2) { return fn(second, first); } else { return function (second) { return fn(second, first); }; }; };
```

### Technical frame 113: self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01468))_

> Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### Technical frame 114: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01533))_

```
const Stack1 = () => ({ array:[], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, iterator () { let iterationIndex = this .index; return () => { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } }); const stack = Stack1(); stack.push("Greetings"); stack.push("to"); stack.push("you!")
```

### Technical frame 115: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01534))_

```
const iter = stack.iterator(); iter().value //=> "you!" iter().value //=> "to"
```

### Technical frame 116: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01538))_

```
const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum }
```

### Technical frame 117: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01543))_

> If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01542))_

```
const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 6
```

### Technical frame 118: from

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01614))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01613))_

```
Array.from(UpTo1000) //=> [1,81,121,361,441,841,961]
```

### Technical frame 119: Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01630))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01627))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical frame 120: javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01672))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01671))_

```
function * only (something) { yield something; }; only("you").next() //=> {"done": false , value: "you"}
```

### Technical frame 121: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01713))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01710))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 122: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01713))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01711))_

```
const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } } for ( const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumbers] //=> [1,2,3] const iterator = ThreeNumbers[Symbol.iterator](); iterator.next() //=> {"done": false , value: 1} iterator.next() //=> {"done": false , value: 2} iterator.next() //=> {"done": false , value: 3} iterator.next() //=> {"done": true }
```

### Technical frame 123: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01715))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01714))_

```
const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } }
```

### Technical frame 124: more generators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01726))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01728))_

```
function * fibonacci () { let a, b; yield a = 0; yield b = 1; while ( true ) { [a, b] = [b, a + b] yield b; } } for ( const i of fibonacci()) { console.log(i); } //=> 0 1 1 2 3 5 8 13 21 34 55 89 144 ...
```

### Technical frame 125: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01732))_

> We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01731))_

```
const isIterable = (something) => !!something[Symbol.iterator]; const TreeIterable = (iterable) => ({ [Symbol.iterator]: function * () { for ( const e of iterable) { if (isIterable(e)) { for ( const ee of TreeIterable(e)) { yield ee; } } else { yield e; } } } }) for ( const i of TreeIterable([1, [2, [3, 4], 5]])) { console.log(i); } //=> 1 2 3 4 5
```

### Technical frame 126: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01735))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01733))_

> But if you can write it as a simple generator, write it as a simple generator.

### Technical frame 127: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01735))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01734))_

```
function * tree (iterable) { for ( const e of iterable) { if (isIterable(e)) { for ( const ee of tree(e)) { yield ee; } } else { yield e; } } }; for ( const i of tree([1, [2, [3, 4], 5]])) { console.log(i); } //=> 1 2 3 4 5
```

### Technical frame 128: interactive generators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01942))_

> Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1)

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01941))_

```
function * generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3; break ; case 3: const x3 = yield 8; switch (x3) { case 2: case 5: case 7: yield 4; break ; case 4: yield 7; break ;
```

### Technical atom 129

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00239))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00237))_

| entry | content |
| --- | --- |
| 19 | Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace. |
| 20 | As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea. |

<details>
<summary>Raw table text</summary>

```
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

</details>

### Technical atom 130

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00564))_

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

<details>
<summary>Raw table text</summary>

```
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

</details>

### Technical atom 131

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00571))_

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) |

<details>
<summary>Raw table text</summary>

```
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

</details>

### Technical atom 132

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00614))_

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

<details>
<summary>Raw table text</summary>

```
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

</details>

### Technical atom 133

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00659))_

| entry | content |
| --- | --- |
| 45 | from Michael Fogus, Functional JavaScript |
| 46 | from Oliver Steele and the terse but handy node-ap |
| 47 | from James Halliday. |

<details>
<summary>Raw table text</summary>

```
Partial Application
In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You'll find examples in Lemonad 45 from Michael Fogus, Functional JavaScript 46 from Oliver Steele and the terse but handy node-ap 47 from James Halliday.
```

</details>

### Technical atom 134

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00660))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00663))_

| entry | content |
| --- | --- |
| 45 | https://github.com/fogus/lemonad |
| 46 | http://osteele.com/sources/javascript/functional/ |
| 47 | https://github.com/substack/node-ap 48 |

<details>
<summary>Raw table text</summary>

```
45 https://github.com/fogus/lemonad 46 http://osteele.com/sources/javascript/functional/ 47 https://github.com/substack/node-ap 48
```

</details>

### Technical atom 135

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00702))_

| entry | content |
| --- | --- |
| 50 | https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad |
| 51 | https://github.com/raganwald/andand |

<details>
<summary>Raw table text</summary>

```
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```

</details>

### Technical atom 136

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01335))_

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

<details>
<summary>Raw table text</summary>

```
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

</details>


## Related pages

- [[javascriptallonge-function-keyword]] - narrower topic: the function keyword shares source evidence from the function keyword: In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, b ... [truncated]; the function keyword shares technical record from the function keyword: (str) => str + str (4 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-function-return-value]] - narrower topic: Function Return Value shares source evidence from functions that return values and evaluate expressions: Yes we can! Functions can return the value of evaluating another function.; Function Return Value shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from variables and bindings: How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dicti ... [truncated]; Argument shares technical record from Ah. I'd Like to Have an Argument, Please. 22: (room) => {} (4 shared statement(s), 20 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from About JavaScript Allongé: It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or ... [truncated]; Javascript shares technical record from As Little As Possible About Functions, But No Less: () => 0 (6 shared statement(s), 16 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from void: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Return shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (6 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from variables and bindings: The expression 'x' (the right side of the function) is evaluated within the environment we just created.; Expression shares technical record from void: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } (2 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-length]] - shared statements and technical atoms: Length shares source evidence from Self-Similarity: Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to c ... [truncated]; Length shares technical record from Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : // ??? (3 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change.; Iterator shares technical record from unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false , value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne ... [truncated] (5 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-declaration]] - shared statements and technical atoms: Declaration shares source evidence from function declarations: In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of ... [truncated]; Declaration shares technical record from function declarations: function someName () { // ... } This behaves a little like: const someName = function someName () // ... } (4 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-result]] - shared statements and technical atoms: Result shares source evidence from void: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Result shares technical record from void: (() => {})() //=> undefined (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from Naming Functions: It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an ... [truncated]; Bind shares technical record from That Constant Coffee Craving: ((PI) => // ???? )(3.14159265) (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Functional shares technical record from Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (5 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Functional Iterators shares technical record from a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (4 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Program shares technical record from why the 'six' edition?: def foo (first, *rest) # ... end (4 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from iterating: Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iterator ... [truncated]; Array shares technical record from As Little As Possible About Functions, But No Less: () => 0 (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated]; Code shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms: Environment shares source evidence from Naming Functions: It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an ... [truncated]; Environment shares technical record from variables and bindings: ((x) => x)(2) //=> 2 (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Language shares technical record from why the 'six' edition?: def foo (first, *rest) # ... end (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from folding: With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn't. A function to compu ... [truncated]; List shares technical record from Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let's try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"]) (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from iterator objects: Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional i ... [truncated]; Object shares technical record from Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-bound]] - shared statements and technical atoms: Bound shares source evidence from const: Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is ... [truncated]; Bound shares technical record from the function keyword: ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - ... [truncated] (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Evaluate shares technical record from void: (() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World' (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from const: Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this:; Write shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from void: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Block shares technical record from void: (() => {})() //=> undefined (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-evaluating]] - shared statements and technical atoms: Evaluating shares source evidence from void: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Evaluating shares technical record from void: (() => {})() //=> undefined (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-parameter]] - shared statements and technical atoms: Parameter shares source evidence from function parameters are eager: In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated :; Parameter shares technical record from Left-Variadic Functions: const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5] (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-recipe]] - shared statements and technical atoms: Recipe shares source evidence from Maybe: Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:; Recipe shares technical record from Maybe: const isSomething = (value) => value !== null && value !== void 0; const checksForSomething = (value) => { if (isSomething(value)) { // function's true logic } } (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms: Mapwith shares source evidence from partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Mapwith shares technical record from partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (4 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; Programming shares technical record from why the 'six' edition?: def foo (first, *rest) # ... end (4 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-gathering]] - shared statements and technical atoms: Gathering shares source evidence from left-variadic destructuring: Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this:; Gathering shares technical record from Left-Variadic Functions: const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-generator]] - shared statements and technical atoms: Generator shares source evidence from generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Generator shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Iterable shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-seen]] - shared statements and technical atoms: Seen shares source evidence from yielding iterables: We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function tha ... [truncated]; Seen shares technical record from converting non-tail-calls to tail-calls: const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysW ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-symbol]] - shared statements and technical atoms: Symbol shares source evidence from generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Symbol shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from the vireo: As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar comb ... [truncated]; Value shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-alway]] - shared statements and technical atoms: Alway shares source evidence from if functions without free variables are pure, are closures impure?: Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure fu ... [truncated]; Alway shares technical record from if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-data]] - shared statements and technical atoms: Data shares source evidence from Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Data shares technical record from backwardness: const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus" (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-idea]] - shared statements and technical atoms: Idea shares source evidence from const: Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really ... [truncated]; Idea shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-pattern]] - shared statements and technical atoms: Pattern shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated]; Pattern shares technical record from Maybe: const isSomething = (value) => value !== null && value !== void 0; const checksForSomething = (value) => { if (isSomething(value)) { // function's true logic } } (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-purpose]] - shared statements and technical atoms: Purpose shares source evidence from caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change.; Purpose shares technical record from magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-behaviour]] - shared statements and technical atoms: Behaviour shares source evidence from which came first, the chicken or the egg?: This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as wel ... [truncated]; Behaviour shares technical record from function parameters are eager: const or = (a, b) => a || b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n !== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded. (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-second]] - shared statements and technical atoms: Second shares source evidence from backwardness: Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of va ... [truncated]; Second shares technical record from backwardness: const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus" (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-follow]] - shared statements and technical atoms: Follow shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated]; Follow shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Method shares technical record from Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-recall]] - shared statements and technical atoms: Recall shares source evidence from from: We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And i ... [truncated]; Recall shares technical record from generators and iterables: const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } } for ( const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumber ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-doesn-t-work-because-parseint]] - shared technical atoms: Doesn'T Work Because Parseint shares technical record from Unary: If you pass in a function taking only one argument, it simply ignores the additional arguments. (3 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (3 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical record from Left-Variadic Functions: function team(coach, captain, ...players) { console.log(` ${ captain } (captain)`); for ( let player of players) { console.log(player); } console.log(`squad coached ... [truncated] (2 shared atom(s))
- [[javascriptallonge-fat-arrow]] - shared technical atoms: Fat Arrow shares technical record from magic names and fat arrows: ( function () { return (() => arguments[0])('inner'); })('outer') //=> "outer" (2 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-binding]] - shared technical atoms: Binding shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from interactive generators: function * generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield ... [truncated] (1 shared atom(s))
- [[javascriptallonge-discussing]] - shared technical atoms: Discussing shares technical record from magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-string]] - shared technical atoms: String shares technical record from As Little As Possible About Functions, But No Less: () => 0 (1 shared atom(s))
- [[javascriptallonge-third]] - shared technical atoms: Third shares technical record from tail-call optimization: const maybe = (fn) => function (...args) { if (args.length === 0) { return ; } else { for ( let arg of args) { if (arg == null ) return ; } return fn.apply( this , args); } } (1 shared atom(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from copy-on-write: And now functions like that make copies without modifying anything, work at full speed. (2 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (2 shared statement(s))
- [[javascriptallonge-pass]] - shared statements: Pass shares source evidence from caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. (2 shared statement(s))
- [[javascriptallonge-allong]] - shared statements: Allong shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-directly]] - shared statements: Directly shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated] (1 shared statement(s))
- [[javascriptallonge-important]] - shared statements: Important shares source evidence from const: Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really ... [truncated] (1 shared statement(s))
- [[javascriptallonge-learn]] - shared statements: Learn shares source evidence from if functions without free variables are pure, are closures impure?: From this, we learn something: A pure function can contain a closure. (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements: Literal shares source evidence from evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-writing]] - shared statements: Writing shares source evidence from more generators: We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of s ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-functions-a259562e]] - source section: Functions shares source evidence from Functions: Functions are values that can be part of expressions, returned from other functions, and so forth.; Functions shares technical table: combinators The word 'combinator' has a precise technical meaning in mathematics: 'A combinator is a higher-order function that uses only function application and ea ... [truncated] (12 shared statement(s), 3 shared atom(s))

## Source

- [[javascriptallonge]]
