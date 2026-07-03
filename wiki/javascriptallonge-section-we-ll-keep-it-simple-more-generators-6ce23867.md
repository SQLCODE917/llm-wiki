---
page_id: javascriptallonge-section-we-ll-keep-it-simple-more-generators-6ce23867
page_kind: source
page_family: section-reference
summary: We'll keep it simple: / more generators: 9 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-more-generators-6ce23867@03b21b51ab6cc0bb832a7ad9f6300dbd
---

# We'll keep it simple: / more generators

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-1104ef0d]] - broader source section: We'll keep it simple:

### Topics

- [[javascriptallonge-generator]] - topic hub: opens the topic page for Generator

## Statements

- Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state: _(javascriptallonge.pdf (source-range-7239e085-01720))_
- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-7239e085-01725))_

## Technical atoms

### Technical frame 1: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01720))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01718))_

<a id="atom-technical-atom-2e01e3085500fe57"></a>

```
const Numbers = {
*[Symbol.iterator] () {
let i = 0;
while (true) {
yield i++;
}
}
};
for (const i of Numbers) {
console.log(i);
}
//=>
0
1
2
3
4
5
6
7
```

### Technical frame 2: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01720))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01719))_

<a id="atom-technical-atom-5b9d980be748a7cb"></a>

```
8
9
10
...
```

### Technical frame 3: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01725))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01724))_

<a id="atom-technical-atom-f4b0f57efe02590e"></a>

```
const Fibonacci = {
*[Symbol.iterator] () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
}
for (const i of Fibonacci) {
console.log(i);
}
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
55
89
144
...
```

### Technical frame 4: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01725))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01727))_

<a id="atom-technical-atom-10237a444786ad38"></a>

```
function * fibonacci () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
for (const i of fibonacci()) {
console.log(i);
}
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
55
89
144
...
```
