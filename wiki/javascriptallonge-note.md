---
page_id: javascriptallonge-note
page_kind: concept
summary: Note: 4 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-note@15be49f43e500df97bc69952b9fabf61
---

# Note

What [[javascriptallonge]] covers about note:

## Statements

### Picking the Bean: Choice and Truthiness

- Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently. _(javascriptallonge.pdf (source-range-7239e085-00763))_

### Composing and Decomposing Data / Mutation

- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction. _(javascriptallonge.pdf (source-range-7239e085-01140))_

### Like this: / iterables

- Nowis the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal: _(javascriptallonge.pdf (source-range-7239e085-01565))_

### Like this: / Generating Iterables / state machines

- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-7239e085-01653))_


## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00126))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00125))_

```
2 + 2 === 4
//=> true
(2 + 2 === 4) === (2 !== 5)
//=> true
```

### Technical frame 2: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00129))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00127))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical frame 3: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01155))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01154))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const copy = (node) => reverse(reverse(node));
```

### Technical frame 4: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01570))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01566))_

```
['some squares', ...someSquares]
//=> ["some squares", 1, 4, 9, 16, 25]
```

### Technical frame 5: Like this: / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01653))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01651))_

```
// Generation
const fibonacci = () => {
let a, b;
console.log(a = 0);
console.log(b = 1);
while (true) {
[a, b] = [b, a + b];
console.log(b);
}
}
fibonacci()
//=>
0
1
1
2
3
5
8
13
21
34
```

### Technical frame 6: Like this: / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01653))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01652))_

```
55
89
144
...
```


## Related pages

- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from Like this: / Generating Iterables / state machines: // Generation const fibonacci = () => { let a, b; console.log(a = 0); console.log(b = 1); while (true) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical record from Like this: / Generating Iterables / state machines: // Generation const fibonacci = () => { let a, b; console.log(a = 0); console.log(b = 1); while (true) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Like this: / Generating Iterables / state machines: // Generation const fibonacci = () => { let a, b; console.log(a = 0); console.log(b = 1); while (true) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared atom(s))
- [[javascriptallonge-string]] - shared technical atoms: String shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms: Type shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared atom(s))
- [[javascriptallonge-algorithm]] - shared technical atoms: Algorithm shares technical record from Composing and Decomposing Data / Mutation / building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))
- [[javascriptallonge-copy]] - shared technical atoms: Copy shares technical record from Composing and Decomposing Data / Mutation / building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))
- [[javascriptallonge-element]] - shared technical atoms: Element shares technical record from Like this: / iterables: ['some squares', ...someSquares] //=> ["some squares", 1, 4, 9, 16, 25] (1 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Composing and Decomposing Data / Mutation / building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))

## Source

- [[javascriptallonge]]
