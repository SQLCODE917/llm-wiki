---
page_id: javascriptallonge-section-that-constant-coffee-craving-75082210
page_kind: source
summary: That Constant Coffee Craving: 116 source-backed entries and 34 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-that-constant-coffee-craving-75082210@312fe9abed6e8fc24150c33378e0c131
---

# That Constant Coffee Craving

From [[javascriptallonge]].

## Statements

- Up to now, all we’ve really seen are _anonymous functions_ , functions that don’t have a name. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- Naming things is a critical part of programming, but all we’ve seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. _(javascriptallonge.pdf (source-range-83ecb080-00548))_
- This one has a few more moving parts, that’s all. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- But we can use it just like (diameter) => diameter * 3.14159265. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- This expression, when evaluated, returns a function that calculates circumferences. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- All of our “functions” are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind.[29] _(javascriptallonge.pdf (source-range-83ecb080-00559))_
- There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- A “magic literal” like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-83ecb080-00565))_
- Well, the first one seems simplest, but a half-century of experience has taught us that names matter. _(javascriptallonge.pdf (source-range-83ecb080-00565))_
- The third one is easiest for most people to read. _(javascriptallonge.pdf (source-range-83ecb080-00566))_
- Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated “IIFE.” _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- That’s how it should be, naming PI is its concern, not ours. _(javascriptallonge.pdf (source-range-83ecb080-00571))_
- Everything else is encapsulated in its body. _(javascriptallonge.pdf (source-range-83ecb080-00571))_
- “Exposes” naming PI first, and we have to look inside to find out why we care. _(javascriptallonge.pdf (source-range-83ecb080-00575))_
- “Exposes” naming PI first, and we have to look inside to find out why we care. _(javascriptallonge.pdf (source-range-83ecb080-00575))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. _(javascriptallonge.pdf (source-range-83ecb080-00577))_
- But then we’ve obfuscated our code, and we don’t want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-83ecb080-00579))_
- But then we’ve obfuscated our code, and we don’t want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-83ecb080-00579))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00580))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00580))_
- Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-83ecb080-00582))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-83ecb080-00589))_
- We’ll learn a lot more about const in future chapters, but here’s the most important thing we can do with const: _(javascriptallonge.pdf (source-range-83ecb080-00589))_
- That’s much better than what we were writing. _(javascriptallonge.pdf (source-range-83ecb080-00592))_
- We use the const keyword in a _const statement_ . _(javascriptallonge.pdf (source-range-83ecb080-00593))_
- We can bind any expression. _(javascriptallonge.pdf (source-range-83ecb080-00602))_
- Amazing how such an important idea–naming functions–can be explained _en passant_ in just a few words. _(javascriptallonge.pdf (source-range-83ecb080-00605))_
- We can bind more than one name-value pair by separating them with commas. _(javascriptallonge.pdf (source-range-83ecb080-00606))_
- > 30We’re into the second chapter and we’ve finally named a function. _(javascriptallonge.pdf (source-range-83ecb080-00608))_
- Up to now, we’ve only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-83ecb080-00612))_
- But there are other kinds of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00612))_
- Up to now, we’ve only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-83ecb080-00612))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. _(javascriptallonge.pdf (source-range-83ecb080-00616))_
- We’ve used a block as the else clause, and since it’s a block, we’ve placed a const statement inside it. _(javascriptallonge.pdf (source-range-83ecb080-00621))_
- We’ve used a block as the else clause, and since it’s a block, we’ve placed a const statement inside it. _(javascriptallonge.pdf (source-range-83ecb080-00621))_
- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we’re to place const anywhere we like. _(javascriptallonge.pdf (source-range-83ecb080-00623))_
- We can use any expression in there, and that expression can invoke diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00627))_
- It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. _(javascriptallonge.pdf (source-range-83ecb080-00627))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00631))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00631))_
- This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-83ecb080-00632))_
- We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-83ecb080-00632))_
- This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-83ecb080-00632))_
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2), the value that counts is 3.14159265, the value we bound to PI in the environment surrounding (diameter) _⇒_ diameter * PI. _(javascriptallonge.pdf (source-range-83ecb080-00635))_
- That much we can carefully work out from the way closures work. _(javascriptallonge.pdf (source-range-83ecb080-00636))_
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00642))_
- They are looked up in the environment where they are declared. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- We just saw that values bound with const use lexical scope, just like values bound with parameters. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00645))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00645))_
- We can test this by creating another conflict. _(javascriptallonge.pdf (source-range-83ecb080-00646))_
- But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-83ecb080-00646))_
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. _(javascriptallonge.pdf (source-range-83ecb080-00655))_
- This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-83ecb080-00657))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. _(javascriptallonge.pdf (source-range-83ecb080-00657))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding _shadows_ the outer binding. _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- We’ll need a gratuitous block. _(javascriptallonge.pdf (source-range-83ecb080-00666))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- Typically, we want to bind our names as close to where we need them as possible. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- Being able to bind a name inside of a block means that if the name is only needed in the block, we are not “leaking” its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-00688))_
- We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-83ecb080-00688))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const, we need never worry that its value may change. _(javascriptallonge.pdf (source-range-83ecb080-00689))_

## Technical atoms

> There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example:
_(source: javascriptallonge.pdf (source-range-83ecb080-00544))_

> Context: There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example:
_(context: javascriptallonge.pdf (source-range-83ecb080-00544))_

> (diameter) => diameter * 3.14159265
_(source: javascriptallonge.pdf (source-range-83ecb080-00545))_

> Context: What is this “3.14159265” number? PI[28] , obviously. We’d like to name it so that we can write something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00546))_

> (diameter) => diameter * PI
_(source: javascriptallonge.pdf (source-range-83ecb080-00547))_

> Context: In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:
_(context: javascriptallonge.pdf (source-range-83ecb080-00548))_

> ((PI) => _// ????_ )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00549))_

> Context: What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:
_(context: javascriptallonge.pdf (source-range-83ecb080-00550))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00551))_

> ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00557))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00558))_

> Context: There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: It produces the same result as our previous expressions for a diameter-calculating function:
_(context: javascriptallonge.pdf (source-range-83ecb080-00561, source-range-83ecb080-00563))_

> (diameter) => ((PI) => diameter * PI)(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00562))_

> - (diameter) => ((PI) => diameter * PI)(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00576))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00578))_

> Context: Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00582))_

> (diameter, PI) => diameter * PI
_(source: javascriptallonge.pdf (source-range-83ecb080-00583))_

> Context: And we could use it like this: This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name.
_(context: javascriptallonge.pdf (source-range-83ecb080-00584, source-range-83ecb080-00588))_

> ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00587))_

> Context: JavaScript gives us a way to do that, the const keyword. We’ll learn a lot more about const in future chapters, but here’s the most important thing we can do with const:
_(context: javascriptallonge.pdf (source-range-83ecb080-00589))_

> (diameter) => { **const** PI = 3.14159265;
_(source: javascriptallonge.pdf (source-range-83ecb080-00590))_

> Context: It works just as we want. Instead of:
_(context: javascriptallonge.pdf (source-range-83ecb080-00594))_

> ((diameter) => ((PI) => diameter * PI)(3.14159265))(2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00595))_

> ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00597))_

> Context: We write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00598))_

> ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00601))_

> Context: We can bind any expression. Functions are expressions, so we can bind helper functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-00602))_

> This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with ().
_(source: javascriptallonge.pdf (source-range-83ecb080-00604))_

> Context: We can bind more than one name-value pair by separating them with commas. For readability, most people put one binding per line:
_(context: javascriptallonge.pdf (source-range-83ecb080-00606))_

> (d) => { **const** PI = 3.14159265, calc = (diameter) => diameter * PI; **return** "The circumference is " + calc(d) }
_(source: javascriptallonge.pdf (source-range-83ecb080-00607))_

> One of the places you can find blocks is in an if statement.
_(source: javascriptallonge.pdf (source-range-83ecb080-00612))_

> Context: Here’s the second formulation of our diameter function, bound to a name using an IIFE:
_(context: javascriptallonge.pdf (source-range-83ecb080-00625))_

> ((diameter_fn) => _// ..._ )( ((PI) => (diameter) => diameter * PI )(3.14159265) )
_(source: javascriptallonge.pdf (source-range-83ecb080-00626))_

> Context: It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. We can use any expression in there, and that expression can invoke diameter_fn. For example: This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where dia
_(context: javascriptallonge.pdf (source-range-83ecb080-00627, source-range-83ecb080-00632))_

> ((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00630))_

> Context: We can test this by deliberately creating a “conflict:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00633))_

> ((diameter_fn) => ((PI) => diameter_fn(2) )(3) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00634))_

> ((diameter_fn) => { **const** PI = 3;
_(source: javascriptallonge.pdf (source-range-83ecb080-00640))_

> **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => diameter * PI })() ) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00641))_

> Context: Let’s start, as above, by doing this with parameters. We’ll start with:
_(context: javascriptallonge.pdf (source-range-83ecb080-00647))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00648))_

> Context: And gratuitously wrap it in another IIFE so that we can bind PI to something else:
_(context: javascriptallonge.pdf (source-range-83ecb080-00649))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)
_(source: javascriptallonge.pdf (source-range-83ecb080-00652))_

> Context: This still evaluates to a function that calculates diameters:
_(context: javascriptallonge.pdf (source-range-83ecb080-00653))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00654))_

> Context: And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the “outer” environment? Let’s rewrite things slightly differently: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the
_(context: javascriptallonge.pdf (source-range-83ecb080-00655, source-range-83ecb080-00657))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00656))_

> Context: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding:
_(context: javascriptallonge.pdf (source-range-83ecb080-00657))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00658))_

> ((diameter) => { **const** PI = 3.14159265; (() => { **const** PI = 3; })(); **return** diameter * PI; })(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00663))_

> Context: This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> ((diameter) => { **const** PI = 3.14159265;
_(source: javascriptallonge.pdf (source-range-83ecb080-00674))_

> Context: This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_
_(source: javascriptallonge.pdf (source-range-83ecb080-00675))_

> Context: This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00673))_

> If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.
_(source: javascriptallonge.pdf (source-range-83ecb080-00676))_

> Context: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00676))_

> **if** ( **true** ) { **const** PI = 3.14159265; } **return** diameter * PI; })(2) _//=> would return 6.2831853 if const had function scope_
_(source: javascriptallonge.pdf (source-range-83ecb080-00678))_
