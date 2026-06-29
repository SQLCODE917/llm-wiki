---
page_id: javascriptallonge-instead
page_kind: concept
summary: Instead: 8 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-instead@3cf59824bae4c5091215dede4db402ba
---

# Instead

What [[javascriptallonge]] covers about instead:

## Statements

### michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-8eb13d6b-00087))_

### values are expressions

- All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water. _(javascriptallonge.pdf (source-range-8eb13d6b-00111))_

### are consts also from a shadowy planet?

- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-8eb13d6b-00469))_

### a balanced statement about combinators

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either: _(javascriptallonge.pdf (source-range-8eb13d6b-00573))_

### a return to backward thinking

- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-8eb13d6b-01421))_

### iterator objects

- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-8eb13d6b-01547))_

### iterables

- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-8eb13d6b-01554))_

### Summary

- A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. And we don't need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-8eb13d6b-01758))_


## Technical atoms

### Technical frame 1: values are expressions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00112))_

> Astute readers will realize we're omitting something. Congratulations! Take a sip of espresso. We'll get to that in a moment.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00113))_

> And if we hand over the espresso, we get the espresso right back.

### Technical frame 2: a balanced statement about combinators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00579))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00574))_

```
const something = (x) => x != null ;
```

### Technical frame 3: iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01561))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01559))_

```
const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, [Symbol.iterator] () { let iterationIndex = this .index; return { next () { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } }); const stack = Stack3();
```

### Technical frame 4: iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01561))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01560))_

```
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```


## Related pages

- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Summary: A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object th ... [truncated]; Iterator shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Summary: A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object th ... [truncated]; Object shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-writing]] - shared statements and technical atoms: Writing shares source evidence from a balanced statement about combinators: So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either:; Writing shares technical record from a balanced statement about combinators: const something = (x) => x != null ; (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Value shares technical record from values are expressions: And if we hand over the espresso, we get the espresso right back. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared atom(s))
- [[javascriptallonge-symbol]] - shared technical atoms: Symbol shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared atom(s))
- [[javascriptallonge-coffee]] - shared technical atoms: Coffee shares technical record from values are expressions: And if we hand over the espresso, we get the espresso right back. (1 shared atom(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (2 shared statement(s))
- [[javascriptallonge-bind]] - shared statements: Bind shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated] (1 shared statement(s))
- [[javascriptallonge-binding]] - shared statements: Binding shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated] (1 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from iterables: So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict wi ... [truncated] (1 shared statement(s))
- [[javascriptallonge-different]] - shared statements: Different shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated] (1 shared statement(s))
- [[javascriptallonge-directly]] - shared statements: Directly shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated] (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from iterables: So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict wi ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pass]] - shared statements: Pass shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (1 shared statement(s))

## Source

- [[javascriptallonge]]
