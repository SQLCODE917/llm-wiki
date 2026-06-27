---
page_id: javascriptallonge-section-generating-iterables-0cf65eec
page_kind: source
summary: Generating Iterables: 119 source-backed entries and 22 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generating-iterables-0cf65eec@3e3c0ae69e0a36f7608267ca3eddb58a
---

# Generating Iterables

From [[javascriptallonge]].

## Statements

- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-83ecb080-02530))_
- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-83ecb080-02530))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- This seems blindingly obvious and simple. _(javascriptallonge.pdf (source-range-83ecb080-02532))_
- The Numbers iterable returns an object that updates a mutable variable, n, to deliver number after number. _(javascriptallonge.pdf (source-range-83ecb080-02536))_
- There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- Then it waits for the next request. _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- It waits until given a request, and then it returns exactly one item. _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- Of course, when we have some code that makes a bunch of something, we don’t usually write it like that. _(javascriptallonge.pdf (source-range-83ecb080-02538))_
- We would _generate_ numbers. _(javascriptallonge.pdf (source-range-83ecb080-02541))_
- And magically, the numbers would pour forth. _(javascriptallonge.pdf (source-range-83ecb080-02541))_
- Well, there are some collections that are much easier to generate than to iterate over. _(javascriptallonge.pdf (source-range-83ecb080-02545))_
- Iterators maintain state, that’s what they do. _(javascriptallonge.pdf (source-range-83ecb080-02547))_
- Generators have to manage the exact same amount of state, but sometimes, it’s much easier to manage that state in a generator. _(javascriptallonge.pdf (source-range-83ecb080-02547))_
- Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- For example, iterating over a tree. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we’re left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. _(javascriptallonge.pdf (source-range-83ecb080-02555))_
- In essence, both the generation and iteration implementations have stacks, but the generation version’s stack is _implicit_ , while the iteration version’s stack is _explicit_ . _(javascriptallonge.pdf (source-range-83ecb080-02555))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-83ecb080-02558))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-83ecb080-02558))_
- Some iterables can be modelled as state machines. _(javascriptallonge.pdf (source-range-83ecb080-02560))_
- - The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-83ecb080-02561))_
- - The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-83ecb080-02562))_
- - Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-83ecb080-02563))_
- This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] : _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] : _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning the natural linear state. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. _(javascriptallonge.pdf (source-range-83ecb080-02588))_
- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. _(javascriptallonge.pdf (source-range-83ecb080-02590))_
- Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-83ecb080-02590))_
- An iterator written in a generation style is called a _generator_ . _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- We can write an iterator, but use a generation style of programming. _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- An iterator written in a generation style is called a _generator_ . _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-83ecb080-02598))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-83ecb080-02598))_
- Generator functions can take an argument. _(javascriptallonge.pdf (source-range-83ecb080-02599))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- It yields the value of something, and then it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02608))_
- This is where generators behave very, very differently from ordinary functions. _(javascriptallonge.pdf (source-range-83ecb080-02617))_
- The iterator is in a nascent or “newborn” state. _(javascriptallonge.pdf (source-range-83ecb080-02619))_
- When we call interator.next(), the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02620))_
- - The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02626))_
- - The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02627))_
- - The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02631))_
- - The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02632))_
- - The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02636))_
- - The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02637))_
- There are no more lines of code, so it ends. _(javascriptallonge.pdf (source-range-83ecb080-02638))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement. _(javascriptallonge.pdf (source-range-83ecb080-02638))_
- This behaviour is not unique to JavaScript, generators are called coroutines[92] in other languages: _(javascriptallonge.pdf (source-range-83ecb080-02640))_
- Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. _(javascriptallonge.pdf (source-range-83ecb080-02641))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-83ecb080-02641))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-83ecb080-02641))_
- With an iterator, we can call them the _producer_ and the _consumer_ . _(javascriptallonge.pdf (source-range-83ecb080-02642))_
- The iterator is the producer, and the code that iterates over it is the consumer. _(javascriptallonge.pdf (source-range-83ecb080-02642))_
- For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): _(javascriptallonge.pdf (source-range-83ecb080-02647))_
- Of course, generators need not be implemented exactly as coroutines. _(javascriptallonge.pdf (source-range-83ecb080-02647))_
- For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): _(javascriptallonge.pdf (source-range-83ecb080-02647))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. _(javascriptallonge.pdf (source-range-83ecb080-02649))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-02649))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-02649))_
- Our generator function oneTwoThree is not an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02651))_
- As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3. _(javascriptallonge.pdf (source-range-83ecb080-02652))_
- Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-83ecb080-02652))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing _(javascriptallonge.pdf (source-range-83ecb080-02659))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a _generator_ method for [Symbol.iterator]. _(javascriptallonge.pdf (source-range-83ecb080-02665))_
- Our OneTwoThree example used implicit state to output the numbers in sequence. _(javascriptallonge.pdf (source-range-83ecb080-02672))_
- We’ve writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-83ecb080-02681))_
- And the generator’s syntax allows us to use JavaScript’s natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-83ecb080-02681))_
- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] _(javascriptallonge.pdf (source-range-83ecb080-02689))_
- > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-02690))_
- > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-02690))_
- If e is not an iterable, yield e. _(javascriptallonge.pdf (source-range-83ecb080-02694))_
- We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. _(javascriptallonge.pdf (source-range-83ecb080-02694))_
- This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-83ecb080-02695))_
- These three lines say, in essence, “yield all the elements of TreeIterable(e), in order.” This comes up quite often when we have collections that are compounds, collections made from other collections. _(javascriptallonge.pdf (source-range-83ecb080-02698))_
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02704))_
- yield* is handy when writing generator functions that operate on or create iterables. _(javascriptallonge.pdf (source-range-83ecb080-02711))_
- Now that we know about iterables, we can rewrite our iterable operations as generators. _(javascriptallonge.pdf (source-range-83ecb080-02713))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. _(javascriptallonge.pdf (source-range-83ecb080-02719))_
- No need to return an object with a .next() method. _(javascriptallonge.pdf (source-range-83ecb080-02719))_
- We can do the same thing with our other operations like filterWith and untilWith. _(javascriptallonge.pdf (source-range-83ecb080-02720))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-83ecb080-02726))_
- Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. _(javascriptallonge.pdf (source-range-83ecb080-02731))_
- And we don’t need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-83ecb080-02731))_
- This is especially useful for making iterables. _(javascriptallonge.pdf (source-range-83ecb080-02732))_

## Technical atoms

> Context: Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.
_(context: javascriptallonge.pdf (source-range-83ecb080-02531))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.
_(source: javascriptallonge.pdf (source-range-83ecb080-02532))_

> Context: Of course, when we have some code that makes a bunch of something, we don’t usually write it like that. We usually just write something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02538))_

> **let** n = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02539))_

> Context: They’re of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let’s look at one:
_(context: javascriptallonge.pdf (source-range-83ecb080-02545))_

> One of those cases is when we have to recursively enumerate something.
_(source: javascriptallonge.pdf (source-range-83ecb080-02547))_

> Context: For example, iterating over a tree. Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. elements that are not, themselves, iterable.
_(context: javascriptallonge.pdf (source-range-83ecb080-02548))_

> _// Generation_ **const** isIterable = (something) => !!something[Symbol.iterator];
_(source: javascriptallonge.pdf (source-range-83ecb080-02549))_

> Context: Let’s write a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02564))_

> **const** fibonacci = () => { **let** a, b;
_(source: javascriptallonge.pdf (source-range-83ecb080-02566))_

> Context: Let’s write a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02564))_

> console.log(a = 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-02567))_

> console.log(b = 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-02568))_

> **while** ( **true** ) { [a, b] = [b, a + b]; console.log(b); }
_(source: javascriptallonge.pdf (source-range-83ecb080-02569))_

> Whereas the iteration version must make that state explicit.
_(source: javascriptallonge.pdf (source-range-83ecb080-02588))_

> Context: 2. We don’t return values or output them to console.log. We “yield” values using the yield keyword.
_(context: javascriptallonge.pdf (source-range-83ecb080-02593))_

> When we invoke the function, we get an iterator object back.
_(source: javascriptallonge.pdf (source-range-83ecb080-02594))_

> When we invoke empty, we get an iterator with no elements.
_(source: javascriptallonge.pdf (source-range-83ecb080-02598))_

> Context: Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". Invoking only more than once gives us fresh iterators each time:
_(context: javascriptallonge.pdf (source-range-83ecb080-02604))_

> only("you").next() _//=>_ {"done": **false** , value: "you"} only("the lonely").next() _//=>_ {"done": **false** , value: "the lonely"}
_(source: javascriptallonge.pdf (source-range-83ecb080-02605))_

> Context: We can invoke the same iterator twice:
_(context: javascriptallonge.pdf (source-range-83ecb080-02606))_

> **const** sixteen = only("sixteen"); sixteen.next() _//=>_ {"done": **false** , value: "sixteen"} sixteen.next() _//=>_ {"done": **true** }
_(source: javascriptallonge.pdf (source-range-83ecb080-02607))_

> Context: Here’s a generator that yields three numbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-02610))_

> **const** oneTwoThree = **function** * () { **yield** 1; **yield** 2; **yield** 3; };
_(source: javascriptallonge.pdf (source-range-83ecb080-02613))_

> oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: 1}
_(source: javascriptallonge.pdf (source-range-83ecb080-02614))_

> **const** iterator = oneTwoThree();
_(source: javascriptallonge.pdf (source-range-83ecb080-02615))_

> Context: Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.
_(context: javascriptallonge.pdf (source-range-83ecb080-02651))_

> If we call our generator function more than once, we get new iterators.
_(source: javascriptallonge.pdf (source-range-83ecb080-02652))_

> Context: Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method.
_(context: javascriptallonge.pdf (source-range-83ecb080-02658))_

> **const** iterator = ThreeNumbers[Symbol.iterator]();
_(source: javascriptallonge.pdf (source-range-83ecb080-02656))_

> Context: generator methods for objects: This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator.
_(context: javascriptallonge.pdf (source-range-83ecb080-02662, source-range-83ecb080-02664))_

> **const** ThreeNumbers = { *[Symbol.iterator] () { **yield** 1; **yield** 2; **yield** 3 } }
_(source: javascriptallonge.pdf (source-range-83ecb080-02663))_

> But if you can write it as a simple generator, write it as a simple generator.
_(source: javascriptallonge.pdf (source-range-83ecb080-02690))_

> Context: first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02726))_

> **const** first = (iterable) => iterable[Symbol.iterator]().next().value;
_(source: javascriptallonge.pdf (source-range-83ecb080-02727))_

> Context: first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02726))_

> **function** * rest (iterable) { **const** iterator = iterable[Symbol.iterator]();
_(source: javascriptallonge.pdf (source-range-83ecb080-02728))_
