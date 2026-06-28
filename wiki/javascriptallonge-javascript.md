---
page_id: javascriptallonge-javascript
page_kind: concept
summary: Javascript: 85 statement(s) and 62 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript@c5c5ef6f1c989b7ff2c92d8f8e038e9c
---

# Javascript

What [[javascriptallonge]] covers about javascript:

## Statements

### About JavaScript Allongé

- JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. If those terms seem unfamiliar, don't worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter. _(javascriptallonge.pdf (source-range-31a4cf47-00016))_

- JavaScript Allongé begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances. _(javascriptallonge.pdf (source-range-31a4cf47-00017))_

- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript's power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-31a4cf47-00018))_

### why the 'six' edition?

- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-31a4cf47-00022))_

- And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-31a4cf47-00025))_

- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-31a4cf47-00030))_

- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write: _(javascriptallonge.pdf (source-range-31a4cf47-00034))_

- JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-31a4cf47-00039))_

### that's nice. is that the only reason?

- But there's more to it than that . The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. Thus, the focus on things like writing decorators. _(javascriptallonge.pdf (source-range-31a4cf47-00043))_

### What JavaScript Allongé is. And isn't.

- JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions. _(javascriptallonge.pdf (source-range-31a4cf47-00052))_

- But while JavaScript Allongé attempts to be provocative, it is not prescriptive . There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-31a4cf47-00054))_

- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. _(javascriptallonge.pdf (source-range-31a4cf47-00063))_

### ECMAScript 6 has three major groups of features:

- With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces. _(javascriptallonge.pdf (source-range-31a4cf47-00079))_

### michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-31a4cf47-00087))_

### matthew knox

- JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many books try to hide most of those capabilities away, giving you recipes for writing JavaScript in a way that approximates class-centric programming in other languages. Not JavaScript Allongé. It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors. _(javascriptallonge.pdf (source-range-31a4cf47-00092))_

### About The Sample PDF

- This sample edition of the book includes just a portion of the complete book. Buying the book in progress entitles you to free updates, so download it today 7 ! Besides, there's really no risk at all . If you read JavaScript Allongé, The 'six' edition and it doesn't blow your mind, your money will be cheerfully refunded. _(javascriptallonge.pdf (source-range-31a4cf47-00098))_

### values and identity

- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-31a4cf47-00122))_

- Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-31a4cf47-00124))_

### A Rich Aroma: Basic Numbers

- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits. _(javascriptallonge.pdf (source-range-31a4cf47-00149))_

### operations on numbers

- As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 . These can be combined to make more complex expressions, like 2 * 5 + 1 . _(javascriptallonge.pdf (source-range-31a4cf47-00161))_

- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: _(javascriptallonge.pdf (source-range-31a4cf47-00162))_

- JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course). _(javascriptallonge.pdf (source-range-31a4cf47-00164))_

### As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-31a4cf47-00172))_

### commas

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-31a4cf47-00205))_

- This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write: _(javascriptallonge.pdf (source-range-31a4cf47-00209))_

### undefined

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-31a4cf47-00221))_

- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-31a4cf47-00224))_

- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it's helpful to know it exists. _(javascriptallonge.pdf (source-range-31a4cf47-00227))_

- You might think that undefined in JavaScript is equivalent to NULL in SQL. No. In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-31a4cf47-00228))_

### void

- We've seen that JavaScript represents an undefined value by typing undefined , and we've generated undefined values in two ways: _(javascriptallonge.pdf (source-range-31a4cf47-00230))_

- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

### call by value

- We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. But before we do, let's look at variables. _(javascriptallonge.pdf (source-range-31a4cf47-00299))_

### call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-31a4cf47-00325))_

- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-31a4cf47-00327))_

### shadowy variables from a shadowy planet

- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-31a4cf47-00378))_

### which came first, the chicken or the egg?

- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } . _(javascriptallonge.pdf (source-range-31a4cf47-00383))_

### inside-out

- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-31a4cf47-00407))_

### const

- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-31a4cf47-00423))_

### rebinding

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-31a4cf47-00499))_

### the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-31a4cf47-00506))_

### function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-31a4cf47-00551))_

### higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-31a4cf47-00560))_

### Building Blocks

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-31a4cf47-00581))_

### Functions

- JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-31a4cf47-00647))_

- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are 'hoisted.' _(javascriptallonge.pdf (source-range-31a4cf47-00648))_

### Unary

- The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action: _(javascriptallonge.pdf (source-range-31a4cf47-00669))_

### Maybe

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-31a4cf47-00695))_

### Left-Variadic Functions

- A variadic function is a function that is designed to accept a variable number of arguments. 52 In JavaScript, you can make a variadic function by gathering parameters. For example: _(javascriptallonge.pdf (source-range-31a4cf47-00717))_

### a history lesson

- In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory: _(javascriptallonge.pdf (source-range-31a4cf47-00725))_

### truthiness and the ternary operator

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-31a4cf47-00765))_

- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-31a4cf47-00766))_

- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-31a4cf47-00768))_

- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-31a4cf47-00775))_

### array literals

- JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: _(javascriptallonge.pdf (source-range-31a4cf47-00820))_

### destructuring arrays

- In JavaScript, we can actually reverse the statement and place the template on the left and a value on the right: _(javascriptallonge.pdf (source-range-31a4cf47-00845))_

### destructuring is not pattern matching

- That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore: _(javascriptallonge.pdf (source-range-31a4cf47-00865))_

- From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-31a4cf47-00869))_

### Tail Calls (and Default Arguments)

- Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 . _(javascriptallonge.pdf (source-range-31a4cf47-00960))_

- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . _(javascriptallonge.pdf (source-range-31a4cf47-00961))_

### default arguments

- JavaScript provides this exact syntax, it's called a default argument , and it looks like this: _(javascriptallonge.pdf (source-range-31a4cf47-01005))_

### Garbage, Garbage Everywhere

- Here's the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-31a4cf47-01034))_

- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-31a4cf47-01046))_

### Plain Old JavaScript Objects

- JavaScript has dictionaries, and it calls them 'objects.' The word 'object' is loaded in programming circles, due to the widespread use of the term 'object-oriented programming' that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-31a4cf47-01068))_

- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-31a4cf47-01069))_

### literal object syntax

- JavaScript has a literal syntax for creating objects. This object maps values to the keys year , month , and day : _(javascriptallonge.pdf (source-range-31a4cf47-01072))_

### Mutation

- In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = : _(javascriptallonge.pdf (source-range-31a4cf47-01121))_

### Reassignment

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-31a4cf47-01162))_

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-31a4cf47-01167))_

### var

- JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let : _(javascriptallonge.pdf (source-range-31a4cf47-01187))_

### iterating

- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: _(javascriptallonge.pdf (source-range-31a4cf47-01286))_

### bonus

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-31a4cf47-01316))_

- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-31a4cf47-01321))_

### functions are not the real point

- However, that is not the interesting thing to note here. Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. Knowing how to make a linked list out of functions is not really necessary for the working programmer. (Knowing that it can be done, on the other hand, is very important to understanding computer science.) _(javascriptallonge.pdf (source-range-31a4cf47-01404))_

### evaluation time

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-31a4cf47-01519))_

### Iteration and Iterables

- Many objects in JavaScript can model collections of things. A collection is like a box containing stuff. Sometimes you just want to move the box around. But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-31a4cf47-01528))_

### summary

- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-31a4cf47-01621))_

### generators are coroutines

- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-31a4cf47-01707))_

### Daniel Friedman and Matthias Felleisen

- JavaScript Allongé was inspired by The Little Schemer 104 by Daniel Friedman and Matthias Felleisen. But where The Little Schemer's primary focus is recursion, JavaScript Allongé's primary focus is functions as first-class values . _(javascriptallonge.pdf (source-range-31a4cf47-01989))_

### About The Author

- When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg 'Raganwald' Braithwaite has authored libraries 221 for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-31a4cf47-02063))_


## Technical atoms

### Technical frame 1: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00028))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00026))_

```
var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```

### Technical frame 2: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00032))_

> The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00031))_

```
function foo () { var first = arguments[0], rest = [].slice.call(arguments, 1); // ... }
```

### Technical frame 3: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00036))_

> And i is scoped to the for loop. We can also write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00035))_

```
for ( let i = 0; i < array.length; ++i) { // ... }
```

### Technical frame 4: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00038))_

> And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00037))_

```
function foo (first, ...rest) { // ... }
```

### Technical frame 5: values and identity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00122))_

> First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00120))_

```
2 === 2 //=> true 'hello' !== 'goodbye' //=> true
```

### Technical frame 6: values and identity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00124))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00123))_

```
2 === '2' //=> false true !== 'true' //=> true
```

### Technical frame 7: values and identity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00124))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00125))_

```
true === false //=> false 2 !== 5 //=> true 'two' === 'five' //=> false
```

### Technical frame 8: operations on numbers

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00164))_

> JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course).

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00163))_

```
2 * 5 + 1 //=> 11 1 + 5 * 2 //=> 11
```

### Technical frame 9: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00174))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00173))_

```
() => 0
```

### Technical frame 10: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00176))_

> What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a br

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00175))_

```
(() => 0) //=> [Function]
```

### Technical frame 11: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00178))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00177))_

> 16 The simplest possible function is () => {} , we'll see that later.

### Technical frame 12: commas

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00209))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00206))_

```
//=> 2 (1 + 1, 2 + 2)
```

### Technical frame 13: commas

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00209))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00210))_

```
() => (1 + 1, 2 + 2)
```

### Technical frame 14: undefined

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00224))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00222))_

```
undefined
```

### Technical frame 15: undefined

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00224))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00223))_

```
//=> undefined
```

### Technical frame 16: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00235))_

> void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00234))_

```
void 0 //=> undefined void 1 //=> undefined void (2 + 2) //=> undefined
```

### Technical frame 17: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00239))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00238))_

```
(() => {})() //=> undefined
```

### Technical frame 18: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00244))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00243))_

```
() => { 2 + 2 } () => { 1 + 1; 2 + 2 }
```

### Technical frame 19: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00250))_

```
(() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### Technical frame 20: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 21: shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00376))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00375))_

```
(x) => (x, y) => x + y
```

### Technical frame 22: shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00378))_

> When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00377))_

```
(x) => (x, y) => (w, z) => (w) => x + y + z
```

### Technical frame 23: which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00386))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00384))_

> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 24: which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00386))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00385))_

```
// top of the file (() => { // ... lots of JavaScript ... })(); // bottom of the file
```

### Technical frame 25: inside-out

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00409))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00408))_

```
(diameter) => // ...
```

### Technical frame 26: const

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00425))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00424))_

```
(diameter) => { const PI = 3.14159265; return diameter * PI }
```

### Technical frame 27: rebinding

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00499))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00496))_

```
const evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { n = n - 2; return evenStevens(n); } } evenStevens(42) //=> true
```

### Technical frame 28: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00532))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00531))_

```
someBackboneView.on('click', function clickHandler () { //... });
```

### Technical frame 29: Unary

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00670))_

```
['1', '2', '3'].map(parseFloat) //=> [1, 2, 3]
```

### Technical frame 30: Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00719))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00718))_

```
const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5]
```

### Technical frame 31: a history lesson

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00726))_

```
var __slice = Array.prototype.slice; function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1) : []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]) : []); return fn.apply( this , args); } }; var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') //=> ["why",["hello","there","little","droid"]]
```

### Technical frame 32: array literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00822))_

> We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00821))_

```
[] //=> []
```

### Technical frame 33: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00847))_

> The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00846))_

```
const unwrap = (wrapped) => { const [something] = wrapped; return something; } unwrap(["present"]) //=> "present"
```

### Technical frame 34: destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00865))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00864))_

```
const [what] = [];
```

### Technical frame 35: destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00866))_

```
const [what] = []; what //=> undefined const [which, what, who //=> undefined
```

### Technical frame 36: destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00867))_

```
const [...they] = []; they //=> [] const [which, what, they //=> []
```

### Technical frame 37: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00960))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00959))_

```
const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```

### Technical frame 38: default arguments

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01009))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01006))_

```
const factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) //=> 1 factorial(6) //=> 720
```

### Technical frame 39: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01041))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01035))_

```
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
```

### Technical frame 40: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01041))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01040))_

```
const node5 = [5, null ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1;
```

### Technical frame 41: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01046))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01045))_

```
cdr(oneToFive) //=> [2,[3,[4,[5,null]]]]
```

### Technical frame 42: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01076))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01073))_

```
{ year: 2012, month: 6, day: 14 }
```

### Technical frame 43: Mutation

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01122))_

```
const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ]
```

### Technical frame 44: Mutation

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01129))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01128))_

```
const allHallowsEve = [2012, 10, 31] const halloween = allHallowsEve;
```

### Technical frame 45: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01167))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01164))_

```
const evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { n = n - 2; return evenStevens(n); } } evenStevens(42) //=> true
```

### Technical frame 46: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01170))_

> We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01169))_

```
let age = 52; age = 53; age //=> 53
```

### Technical frame 47: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01191))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01188))_

```
const factorial = (n) => { let x = n; if (x === 1) { return 1; } else { --x; return n * factorial(x); } } factorial(5) //=> 120 const factorial2 = (n) => { var x = n; if (x === 1) { return 1; } else { --x;
```

### Technical frame 48: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01191))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01190))_

```
return n * factorial2(x); } } factorial2(5) //=> 120
```

### Technical frame 49: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01195))_

```
const factorial = (n) => { return innerFactorial(n, 1); function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> 24
```

### Technical frame 50: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01197))_

```
const factorial = (n) => { let innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } return innerFactorial(n, 1); } JavaScript hoists the let and the assignment. But not so with var : const factorial = (n) => { return innerFactorial(n, 1); var innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### Technical frame 51: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01199))_

```
const factorial = (n) => { let innerFactorial = undefined ; return innerFactorial(n, 1); innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### Technical frame 52: iterating

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01288))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01287))_

```
const arraySum = (array) => { let sum = 0; for ( let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 53: iterating

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01294))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01292))_

```
const arraySum = (array) => { let iter, sum = 0, index = 0; while ( (eachIteration = { done: index === array.length, value: index < array.length ? array[index] : undefined }, ++index, !eachIteration.done) ) { sum += eachIteration.value; } return sum; } arraySum([1, 4, 9, 16, 25]) //=> 55 With this code, we make a POJO that has done and value keys. All the summing code needs to know is to add eachIteration.value . Now we can extract the ickiness into a separate function: const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ? undefined : array[i++] } } } const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) {
```

### Technical frame 54: iterating

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01294))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01293))_

```
sum += eachIteration.value; } return sum; } iteratorSum(arrayIterator([1, 4, 9, 16, 25])) //=> 55
```

### Technical frame 55: bonus

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01319))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01318))_

```
const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);
```

### Technical atom 56

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00114))_

> Let's try this as well with something else the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00116))_

| entry | content |
| --- | --- |
| 10 | Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer. |
| 11 | In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. |

<details>
<summary>Raw table text</summary>

```
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

</details>

### Technical atom 57

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00156))_

| entry | content |
| --- | --- |
| 13 | http://en.wikipedia.org/wiki/Double-precision_floating-point_format |
| 14 | Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. |

<details>
<summary>Raw table text</summary>

```
13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format
14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
```

</details>

### Technical atom 58

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

### Technical atom 59

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

### Technical atom 60

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

### Technical atom 61

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

### Technical atom 62

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


## Related pages

- [[javascriptallonge-javascript-allong]] - narrower topic: Javascript Allong shares source evidence from What JavaScript Allongé is. And isn't.: JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so ... [truncated] (3 shared statement(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from About JavaScript Allongé: It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or ... [truncated]; Function shares technical record from As Little As Possible About Functions, But No Less: () => 0 (6 shared statement(s), 16 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from values and identity: Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to co ... [truncated]; Value shares technical record from values and identity: 2 === 2 //=> true 'hello' !== 'goodbye' //=> true (7 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Program shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (5 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-programmer]] - shared statements and technical atoms: Programmer shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Programmer shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (3 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Language shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (6 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Garbage, Garbage Everywhere: Here's the scheme in JavaScript, using two-element arrays to represent cons cells:; Array shares technical record from As Little As Possible About Functions, But No Less: () => 0 (1 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-allong]] - shared statements and technical atoms: Allong shares source evidence from About JavaScript Allongé: JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of b ... [truncated]; Allong shares technical record from why the 'six' edition?: function foo (first, ...rest) { // ... } (11 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Bind shares technical record from destructuring is not pattern matching: const [what] = []; (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared statements and technical atoms: Ecmascript shares source evidence from why the 'six' edition?: Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did ... [truncated]; Ecmascript shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (4 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Code shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-evaluating]] - shared statements and technical atoms: Evaluating shares source evidence from shadowy variables from a shadowy planet: When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is igno ... [truncated]; Evaluating shares technical record from void: (() => {})() //=> undefined (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Garbage, Garbage Everywhere: Here's the scheme in JavaScript, using two-element arrays to represent cons cells:; Element shares technical record from Garbage, Garbage Everywhere: const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d; (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Write shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from truthiness and the ternary operator: Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .; Evaluate shares technical record from void: void 0 //=> undefined void 1 //=> undefined void (2 + 2) //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-follow]] - shared statements and technical atoms: Follow shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Follow shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Functional shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Plain Old JavaScript Objects: In JavaScript, an object is a map from string keys to values.; Object shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms: Type shares source evidence from call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Type shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from the function keyword: JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions.; the function keyword shares technical record from the function keyword: someBackboneView.on('click', function clickHandler () { //... }); (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-reference]] - shared statements and technical atoms: Reference shares source evidence from call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Reference shares technical record from Garbage, Garbage Everywhere: const node5 = [5, null ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Rest shares technical record from Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_te ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-rule]] - shared statements and technical atoms: Rule shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Rule shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-string]] - shared statements and technical atoms: String shares source evidence from undefined: Like numbers, booleans and strings, JavaScript can print out the value undefined .; String shares technical record from values and identity: 2 === '2' //=> false true !== 'true' //=> true (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-alway]] - shared statements and technical atoms: Alway shares source evidence from call by value: We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. But before we do, let's look at variables.; Alway shares technical record from which came first, the chicken or the egg?: If you don't want your code to operate directly within the global environment, what can you do? (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Programming shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated]; Literal shares technical record from array literals: [] //=> [] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms: Mapwith shares source evidence from Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Mapwith shares technical record from Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_te ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical record from why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) } (4 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from why the 'six' edition?: for ( let i = 0; i < array.length; ++i) { // ... } (4 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from void: (() => {})() //=> undefined (4 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from default arguments: const factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) //=> 1 factorial(6) //=> 720 (3 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from void: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } (3 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from void: (() => {})() //=> undefined (3 shared atom(s))
- [[javascriptallonge-declaration]] - shared technical atoms: Declaration shares technical record from var: const factorial = (n) => { return innerFactorial(n, 1); function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } fa ... [truncated] (2 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Garbage, Garbage Everywhere: const node5 = [5, null ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (2 shared atom(s))
- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical record from destructuring arrays: const unwrap = (wrapped) => { const [something] = wrapped; return something; } unwrap(["present"]) //=> "present" (2 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (2 shared atom(s))
- [[javascriptallonge-binding]] - shared technical atoms: Binding shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-copy]] - shared technical atoms: Copy shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-different]] - shared technical atoms: Different shares technical record from Mutation: const allHallowsEve = [2012, 10, 31] const halloween = allHallowsEve; (1 shared atom(s))
- [[javascriptallonge-gathering]] - shared technical atoms: Gathering shares technical record from Left-Variadic Functions: const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5] (1 shared atom(s))
- [[javascriptallonge-important]] - shared technical atoms: Important shares technical record from const: (diameter) => { const PI = 3.14159265; return diameter * PI } (1 shared atom(s))
- [[javascriptallonge-learn]] - shared technical atoms: Learn shares technical record from const: (diameter) => { const PI = 3.14159265; return diameter * PI } (1 shared atom(s))
- [[javascriptallonge-needn]] - shared technical atoms: Needn shares technical table: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (1 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from Left-Variadic Functions: const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5] (1 shared atom(s))
- [[javascriptallonge-pass]] - shared technical atoms: Pass shares technical record from destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, they //=> [] (1 shared atom(s))
- [[javascriptallonge-pattern]] - shared technical atoms: Pattern shares technical record from inside-out: (diameter) => // ... (1 shared atom(s))
- [[javascriptallonge-purpose]] - shared technical atoms: Purpose shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recall]] - shared technical atoms: Recall shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-second]] - shared technical atoms: Second shares technical record from void: void 0 //=> undefined void 1 //=> undefined void (2 + 2) //=> undefined (1 shared atom(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated] (2 shared statement(s))
- [[javascriptallonge-seen]] - shared statements: Seen shares source evidence from operations on numbers: As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write ... [truncated] (2 shared statement(s))
- [[javascriptallonge-coffee]] - shared statements: Coffee shares source evidence from About The Author: When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg 'Raganwald' Braithwaite has authored libraries 221 ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (1 shared statement(s))
- [[javascriptallonge-matter]] - shared statements: Matter shares source evidence from generators are coroutines: But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it retur ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-ternary-operator]] - shared statements: Ternary Operator shares source evidence from truthiness and the ternary operator: JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-truthiness]] - shared statements: Truthiness shares source evidence from truthiness and the ternary operator: In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that seman ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
