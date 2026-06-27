---
page_id: javascriptallonge-section-reassignment-f7a3e866
page_kind: source
summary: Reassignment: 53 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-reassignment-f7a3e866@15747419377ef1bf7c7ea8d85592dfe1
---

# Reassignment

From [[javascriptallonge]].

## Statements

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. _(javascriptallonge.pdf (source-range-83ecb080-01758))_
- We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-83ecb080-01765))_
- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-01765))_
- What we want is a statement that works like const, but permits us to rebind variables. _(javascriptallonge.pdf (source-range-83ecb080-01766))_
- The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-83ecb080-01769))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-01772))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-01772))_
- However, if we don’t shadow age with let, reassigning within the block changes the original: _(javascriptallonge.pdf (source-range-83ecb080-01780))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- The suggestion is that shadowing a variable is confusing code. _(javascriptallonge.pdf (source-range-83ecb080-01784))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-01787))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-01791))_
- JavaScript has one _more_ way to bind a name to a value, var.[71] var looks a lot like let: _(javascriptallonge.pdf (source-range-83ecb080-01793))_
- First, var is not block scoped, it’s function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-83ecb080-01799))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. _(javascriptallonge.pdf (source-range-83ecb080-01801))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- But, again, it is unwise to expect consistency. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- But it’s not like const and let in that it’s function scoped, not block scoped. _(javascriptallonge.pdf (source-range-83ecb080-01818))_
- In that way, var is a little like const and let, we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-83ecb080-01818))_
- In that way, var is a little like const and let, we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-83ecb080-01818))_
- For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). _(javascriptallonge.pdf (source-range-83ecb080-01820))_
- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-83ecb080-01820))_
- We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. _(javascriptallonge.pdf (source-range-83ecb080-01821))_
- Hopefully, you can think of a faster way to calculate this sum.[72] And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. _(javascriptallonge.pdf (source-range-83ecb080-01823))_
- > 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- The other kids were adding the numbers like this: 1 + 2 + 3 + . _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- There are 50 pairs of numbers, so the answer is 50*101 = 5050. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- If you notice every pair of numbers adds up to 101. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- The answer is that pesky var i. _(javascriptallonge.pdf (source-range-83ecb080-01833))_
- But at the time we _call_ one of the functions, i has the value 3, which is why the loop terminated. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- Now, at the time we created each function, i had a sensible value, like 0, 1, or 2. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- This small error was a frequent cause of confusion, and in the days when there was no block-scoped let, programmers would need to know how to fake it, usually with an IIFE: _(javascriptallonge.pdf (source-range-83ecb080-01840))_
- This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. _(javascriptallonge.pdf (source-range-83ecb080-01844))_
- The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-83ecb080-01845))_
- The purpose of your own code is to get things done. _(javascriptallonge.pdf (source-range-83ecb080-01845))_
- That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. _(javascriptallonge.pdf (source-range-83ecb080-01845))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01766))_

> Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01767))_

> **let** age = 52;

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01766))_

> Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01768))_

> age = 53; age _//=> 53_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01785))_

> If you dislike deliberately shadowing variables, you’ll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01798))_

> **return** n * factorial2(x); } } factorial2(5) _//=> 120_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01802))_

> But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. Note this example of a function that uses a helper:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01803))_

> **const** factorial = (n) => {

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01809))_

> JavaScript hoists the let and the assignment. But not so with var:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01810))_

> **const** factorial = (n) => {

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01812))_

> JavaScript hoists the declaration, but not the assignment. It is as if we’d written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01815))_

> **const** factorial = (n) => {

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01816))_

> **let** innerFactorial = **undefined** ; **return** innerFactorial(n, 1);

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01821, source-range-83ecb080-01824))_

> We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var: > 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + .

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01822))_

> **var** sum = 0; **for** ( **var** i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01831, source-range-83ecb080-01833))_

> Again, so far, so good. Let’s try one of our functions: What went wrong? Why didn’t it give us ‘Hello, Raganwald, my name is Friedrich’? The answer is that pesky var i. Remember that i is bound in the surrounding environment, so it’s as if we wrote:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01832))_

> introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is undefined'_
