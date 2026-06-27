---
page_id: javascriptallonge-reassignment
page_kind: concept
summary: Reassignment: 36 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-reassignment@f8393989fd968553245f97a728f9fc2d
---

# Reassignment

What [[javascriptallonge]] covers about reassignment:

## Statements

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. _(javascriptallonge.pdf (source-range-83ecb080-01758))_
- We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-83ecb080-01765))_
- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-01765))_
- What we want is a statement that works like const, but permits us to rebind variables. _(javascriptallonge.pdf (source-range-83ecb080-01766))_
- The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-83ecb080-01769))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-01772))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- The suggestion is that shadowing a variable is confusing code. _(javascriptallonge.pdf (source-range-83ecb080-01784))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-01787))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-01791))_
- JavaScript has one _more_ way to bind a name to a value, var.[71] var looks a lot like let: _(javascriptallonge.pdf (source-range-83ecb080-01793))_
- First, var is not block scoped, it’s function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-83ecb080-01799))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. _(javascriptallonge.pdf (source-range-83ecb080-01801))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-01802))_

## Technical atoms

> Context: Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:
_(context: javascriptallonge.pdf (source-range-83ecb080-01766))_

> **let** age = 52;
_(source: javascriptallonge.pdf (source-range-83ecb080-01767))_

> Context: Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:
_(context: javascriptallonge.pdf (source-range-83ecb080-01766))_

> age = 53; age _//=> 53_
_(source: javascriptallonge.pdf (source-range-83ecb080-01768))_

> If you dislike deliberately shadowing variables, you’ll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:
_(source: javascriptallonge.pdf (source-range-83ecb080-01785))_

> **return** n * factorial2(x); } } factorial2(5) _//=> 120_
_(source: javascriptallonge.pdf (source-range-83ecb080-01798))_

> Context: But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. Note this example of a function that uses a helper:
_(context: javascriptallonge.pdf (source-range-83ecb080-01802))_

> **const** factorial = (n) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-01803))_

> Context: JavaScript hoists the let and the assignment. But not so with var:
_(context: javascriptallonge.pdf (source-range-83ecb080-01809))_

> **const** factorial = (n) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-01810))_


## Source

- [[javascriptallonge]]
