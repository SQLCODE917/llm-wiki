---
page_id: javascriptallonge-javascript
page_kind: concept
summary: Javascript: 84 statement(s) and 43 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript@ba05cdcbf3fb5c0cc70605afd1fa0db2
---

# Javascript

What [[javascriptallonge]] covers about javascript:

## Statements

- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00319))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-83ecb080-00055))_
- JavaScript Allongé, The “Six” Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking. _(javascriptallonge.pdf (source-range-83ecb080-00092))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg “Raganwald” Braithwaite has authored libraries[221] for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-83ecb080-03267))_
- JavaScript Allongé is a first and foremost, a book about _programming with functions_ . _(javascriptallonge.pdf (source-range-83ecb080-00032))_
- It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00032))_
- JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-83ecb080-00051))_
- JavaScript Allongé is a book about programming with functions. _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- But while JavaScript Allongé attempts to be provocative, it is not _prescriptive_ . _(javascriptallonge.pdf (source-range-83ecb080-00081))_
- With ECMAScript 6, JavaScript has become much larger as a language. _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- JavaScript holds surprising depths–its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. _(javascriptallonge.pdf (source-range-83ecb080-00131))_
- JavaScript is not such a language, expressions in and of themselves are not values. _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- This corresponds to comparing two things in JavaScript that have different _types_ . _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- > 14Implementations of JavaScript are free to handle larger numbers. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- As we’ve seen, JavaScript has many common arithmetic operators. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. _(javascriptallonge.pdf (source-range-83ecb080-00240))_
- JavaScript has many more operators. _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-83ecb080-00298))_
- In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined. _(javascriptallonge.pdf (source-range-83ecb080-00322))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- In JavaScript, every undefined is identical to every other undefined. _(javascriptallonge.pdf (source-range-83ecb080-00329))_
- We’ve seen that JavaScript represents an undefined value by typing undefined, and we’ve generated undefined values in two ways: _(javascriptallonge.pdf (source-range-83ecb080-00331))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- We’ll see below that while JavaScript always calls by value, the notion of a “value” has additional subtlety. _(javascriptallonge.pdf (source-range-83ecb080-00427))_
- JavaScript does not place copies of reference values in any environment. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00531))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-83ecb080-00589))_
- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-00688))_
- JavaScript _does_ have a syntax for naming a function, we use the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00698))_
- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- The strength of JavaScript is that you can do anything. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- > 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache. _(javascriptallonge.pdf (source-range-83ecb080-00851))_
- JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-83ecb080-00914))_
- JavaScript uses function declarations to bind functions to names within function scope. _(javascriptallonge.pdf (source-range-83ecb080-00915))_
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-00956))_
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-83ecb080-01001))_
- In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. _(javascriptallonge.pdf (source-range-83ecb080-01050))_
- In JavaScript, there is a notion of “truthiness.” Every value is either “truthy” or “falsy.” Obviously, false is falsy. _(javascriptallonge.pdf (source-range-83ecb080-01105))_
- Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. _(javascriptallonge.pdf (source-range-83ecb080-01106))_
- JavaScript inherited an operator from the C family of languages, the _ternary_ operator. _(javascriptallonge.pdf (source-range-83ecb080-01108))_
- We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. _(javascriptallonge.pdf (source-range-83ecb080-01121))_
- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-83ecb080-01189))_
- In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right: _(javascriptallonge.pdf (source-range-83ecb080-01228))_
- JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- JavaScript has a built-in function for this, but let’s write our own using linear recursion. _(javascriptallonge.pdf (source-range-83ecb080-01353))_
- So we know that JavaScript is going to hang on to 1. _(javascriptallonge.pdf (source-range-83ecb080-01404))_
- JavaScript cannot throw first away. _(javascriptallonge.pdf (source-range-83ecb080-01404))_
- Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). _(javascriptallonge.pdf (source-range-83ecb080-01405))_
- JavaScript provides this exact syntax, it’s called a _default argument_ , and it looks like this: _(javascriptallonge.pdf (source-range-83ecb080-01485))_
- Here’s the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-83ecb080-01537))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- JavaScript has dictionaries, and it calls them “objects.” The word “object” is loaded in programming circles, due to the widespread use of the term “object-oriented programming” that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-83ecb080-01584))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-83ecb080-01585))_
- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-83ecb080-01590))_
- In JavaScript, almost every type of value can _mutate_ . _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. _(javascriptallonge.pdf (source-range-83ecb080-01758))_
- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-01765))_
- JavaScript has one _more_ way to bind a name to a value, var.[71] var looks a lot like let: _(javascriptallonge.pdf (source-range-83ecb080-01793))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. _(javascriptallonge.pdf (source-range-83ecb080-01961))_
- Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-83ecb080-02022))_
- Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- Many objects in JavaScript can model collections of things. _(javascriptallonge.pdf (source-range-83ecb080-02363))_
- Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-02523))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. _(javascriptallonge.pdf (source-range-83ecb080-02649))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00051))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00052))_

> **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ }

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00055))_

> But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00056))_

> **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00188))_

> Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00189))_

> **true** === **false** _//=> false_ 2 !== 5 _//=> true_ 'two' === 'five' _//=> false_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00195))_

> - 2 + 2 === 4 _//=> true_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00196))_

> - (2 + 2 === 4) === (2 !== 5) _//=> true_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00198))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00232))_

> > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00235))_

> 0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00236))_

> This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00237))_

> Professional programmers almost never use floating point numbers to represent monetary amounts.

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00240, source-range-83ecb080-00242))_

> In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the nam

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00241))_

> 2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00262))_

> What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00263))_

> > 16 The simplest possible function is () => {}, we’ll see that later.

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00298))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00300))_

> (1 + 1, 2 + 2) _//=> 4_

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00303))_

> This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00304))_

> () => (1 + 1, 2 + 2)

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00334, source-range-83ecb080-00336))_

> There’s a third way, with JavaScript’s void operator. Behold: void is an operator that takes any value and evaluates to undefined, always. So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. By convention, use void 0.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00335))_

> **void** 0 _//=> undefined_ **void** 1 _//=> undefined_ **void** (2 + 2) _//=> undefined_

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00349, source-range-83ecb080-00351))_

> There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00350))_

> () => { 2 + 2 } () => { 1 + 1; 2 + 2 }

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00461))_

> Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00459))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00520, source-range-83ecb080-00522))_

> An interesting thing happens when a variable has the same name as an ancestor environment’s variable. Consider: The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00521))_

> - (x) => (x, y) => x + y

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00522))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00523))_

> (x) => (x, y) => (w, z) => (w) => x + y + z

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00531))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00532))_

> If you don’t want your code to operate directly within the global environment, what can you do?

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00589))_

> JavaScript gives us a way to do that, the const keyword. We’ll learn a lot more about const in future chapters, but here’s the most important thing we can do with const:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00590))_

> (diameter) => { **const** PI = 3.14159265;

### Technical atom 20

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00828))_

> It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00829))_

> **const** compose = (a, b) => (c) => a(b(c));

### Technical atom 21

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00828))_

> It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00830))_

> **const** cookAndEat = compose(eat, cook);

### Technical atom 22

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00828))_

> It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00831))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical atom 23

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00956))_

> The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00957))_

> ['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_

### Technical atom 24

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01050))_

> In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01051))_

> **var** __slice = Array.prototype.slice;

### Technical atom 25

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01228))_

> In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01229))_

> **const** unwrap = (wrapped) => { **const** [something] = wrapped;

### Technical atom 26

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01228))_

> In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01231))_

> unwrap(["present"]) _//=> "present"_

### Technical atom 27

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01269))_

> That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01271))_

> what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_

### Technical atom 28

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01272, source-range-83ecb080-01274))_

> And if there aren’t any items to assign with ..., JavaScript assigns an empty array: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01273))_

> **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_

### Technical atom 29

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01444))_

> This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01447))_

> **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) =>

### Technical atom 30

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01530))_

> > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. 67https://en.wikipedia.org/wiki/IBM_704

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01533))_

> If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.

### Technical atom 31

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01537))_

> Here’s the scheme in JavaScript, using two-element arrays to represent cons cells:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01538))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

### Technical atom 32

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01543))_

> Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01546))_

> **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2];

### Technical atom 33

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01636))_

> Terrible grammar and capitalization, but let’s move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it’s often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01637))_

> **const** description = ({name: { first }, occupation: { title } }) => ` **${** first **}** is a **${** title **}** `;

### Technical atom 34

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01688))_

> In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01689))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_

### Technical atom 35

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01696))_

> We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01697))_

> **const** allHallowsEve = [2012, 10, 31] **const** halloween = allHallowsEve;

### Technical atom 36

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01766))_

> Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01767))_

> **let** age = 52;

### Technical atom 37

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01766))_

> Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01768))_

> age = 53; age _//=> 53_

### Technical atom 38

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01809))_

> JavaScript hoists the let and the assignment. But not so with var:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01810))_

> **const** factorial = (n) => {

### Technical atom 39

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01812))_

> JavaScript hoists the declaration, but not the assignment. It is as if we’d written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01815))_

> **const** factorial = (n) => {

### Technical atom 40

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01821, source-range-83ecb080-01824))_

> We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var: > 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01822))_

> **var** sum = 0; **for** ( **var** i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050

### Technical atom 41

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02508))_

> One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02509))_

> Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_

### Technical atom 42

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00016))_

| **A Pull of the Lever: Prefaces** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **i** |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| **Prelude: Values and Expressions over Coffee**<br>. . . . . . . . . . . . . . . . . . . . . . . . . | **xiii** |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| **A Rich Aroma: Basic Numbers** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **1** |
| **The first sip: Basic Functions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **5** |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| **Recipes with Basic Functions**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **56** |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| **Picking the Bean: Choice and Truthiness** . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **71** |

<details>
<summary>Raw table text</summary>

```
|**A Pull of the Lever: Prefaces** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**i**|
|---|---|
|About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|ii|
|What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|v|
|Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|viii|
|Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|ix|
|About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xi|
|**Prelude: Values and Expressions over Coffee**<br>. . . . . . . . . . . . . . . . . . . . . . . . .|**xiii**|
|values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xiv|
|values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xvi|
|**A Rich Aroma: Basic Numbers** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**1**|
|**The first sip: Basic Functions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**5**|
|As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . .|7|
|Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . .|16|
|Closures and Scope<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
|That Constant Coffee Craving<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|26|
|Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|39|
|Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . .|45|
|Building Blocks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|48|
|Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
|Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|55|
|**Recipes with Basic Functions**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**56**|
|Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|
|Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|59|
|Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|61|
|Maybe<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|63|
|Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|65|
|Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|66|
|**Picking the Bean: Choice and Truthiness** . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**71**|
```

</details>

### Technical atom 43

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00017))_

| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |

<details>
<summary>Raw table text</summary>

```
| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |
```

</details>


## Related pages

- [[javascriptallonge-value]] - shared statements and technical atoms (8 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms (7 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-program]] - shared statements and technical atoms (4 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms (6 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms (3 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-second]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-environment]] - shared statements (2 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements (2 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
