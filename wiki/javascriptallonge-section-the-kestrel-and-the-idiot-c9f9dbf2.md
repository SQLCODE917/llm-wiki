---
page_id: javascriptallonge-section-the-kestrel-and-the-idiot-c9f9dbf2
page_kind: source
summary: the kestrel and the idiot: 12 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-kestrel-and-the-idiot-c9f9dbf2@2937131c7371e49f59298fe14614023a
---

# the kestrel and the idiot

From [[javascriptallonge]].

## Statements

- A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K , is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-8eb13d6b-01337))_
- The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42 . Very simple, but useful. Now we'll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value. _(javascriptallonge.pdf (source-range-8eb13d6b-01340))_
- This is very interesting. Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-8eb13d6b-01343))_
- This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value. _(javascriptallonge.pdf (source-range-8eb13d6b-01351))_

## Technical atoms

### Technical frame 1: the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01340))_

> The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42 . Very simple, but useful. Now we'll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01339))_

```
const K = (x) => (y) => x; const fortyTwo = K(42); fortyTwo(6) //=> 42 fortyTwo("Hello") //=> 42
```

### Technical frame 2: the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01343))_

> This is very interesting. Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works).

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01342))_

```
K(6)(7) //=> 6 K(12)(24) //=> 12
```

### Technical frame 3: the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01351))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01345))_

```
Therefore, K(I)(x)(y) => y :
```

### Technical frame 4: the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01351))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01346))_

```
K(I)(6)(7) //=> 7 K(I)(12)(24) //=> 24
```

### Technical frame 5: the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01351))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01348))_

```
K("primus")("secundus") //=> "primus" K(I)("primus")("secundus") //=> "secundus"
```

### Technical frame 6: the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01351))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01350))_

```
const first = K, second = K(I); first("primus")("secundus") //=> "primus" second("primus")("secundus") //=> "secundus"
```
