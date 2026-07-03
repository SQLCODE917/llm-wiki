---
page_id: javascriptallonge-iterable
page_kind: concept
page_family: topic-concept
summary: Iterable: 2 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterable@bb71ab74593e944cf18b46c88f5863f9
---

# Iterable

What [[javascriptallonge]] covers about iterable:

## Statements

### We'll keep it simple: / generators and iterables

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-7239e085-01714))_

- So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] . _(javascriptallonge.pdf (source-range-7239e085-01715))_


## Technical atoms

### Technical frame 1: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01709))_

<a id="atom-technical-atom-f851858a3f0a60d5"></a>

> If we call our generator function more than once, we get new iterators.

### Technical frame 2: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01710))_

<a id="atom-technical-atom-df68b9aee54b4fac"></a>

```
const ThreeNumbers = {
[Symbol.iterator]: function * () {
yield 1;
yield 2;
yield 3
}
}
for (const i of ThreeNumbers) {
console.log(i);
}
//=>
1
2
3
[...ThreeNumbers]
//=>
[1,2,3]
const iterator = ThreeNumbers[Symbol.iterator]();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

### Technical frame 3: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01714))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01713))_

<a id="atom-technical-atom-08b3d4cd0486cddf"></a>

```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```


## Related pages

### Source structure

- [[javascriptallonge-section-like-this-iterables-ed92ad54]] - source section: Like this: / iterables shares source evidence from Like this: / iterables: People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts ... [truncated]; Like this: / iterables shares technical record from Like this: / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (16 shared statement(s), 5 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from We'll keep it simple: / generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Function shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-generator]] - shared statements and technical atoms: Generator shares source evidence from We'll keep it simple: / generators and iterables: So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] .; Generator shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from We'll keep it simple: / generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Iterator shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-symbol]] - shared statements and technical atoms: Symbol shares source evidence from We'll keep it simple: / generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Symbol shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from We'll keep it simple: / generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Object shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-pattern]] - shared technical atoms: Pattern shares technical record from We'll keep it simple: / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared atom(s))

## Source

- [[javascriptallonge]]
