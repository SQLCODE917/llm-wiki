---
page_id: javascriptallonge-self-similarity
page_kind: source
summary: Self-Similarity from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.109-111
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chunk introduces recursion as the root of computation and explores self-similar data structures, linear recursion, tail-call optimization, and default arguments in JavaScript.

## Key supported claims

- Recursion is the root of computation since it trades description for time—Alan Perlis, Epigrams in Programming 60 (raw/javascriptallonge.pdf p.109-111).
- Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists (raw/javascriptallonge.pdf p.109-111).
- Consists of an element concatenated with a list (raw/javascriptallonge.pdf p.109-111).

## Technical details

### `technical-atom-7d4d3530db6d8743` code

Citation: (raw/javascriptallonge.pdf p.109-111)

```javascript
[] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"]
```

### `technical-atom-9991d4627b6a366f` code

Citation: (raw/javascriptallonge.pdf p.109-111)

```javascript
const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar"]; first //=> "foo" rest //=> ["bar"] const [first, ...rest] = ["foo", "bar", "baz"]; first //=> "foo" rest //=> ["bar","baz"] For the purpose of this exploration, we will presume the following: const isEmpty = ([first, ...rest]) => first === undefined ;
```

### `technical-atom-5925101597ee7da0` code

Citation: (raw/javascriptallonge.pdf p.109-111)

```javascript
isEmpty([]) //=> true isEmpty([0]) //=> false isEmpty([[]]) //=> false
```

### `technical-atom-312728236eb44815` code

Citation: (raw/javascriptallonge.pdf p.109-111)

```javascript
const length = ([first, ...rest]) => first === undefined ? 0 : // ???
```

### `technical-atom-b6969a4fa3096986` code

Citation: (raw/javascriptallonge.pdf p.109-111)

```javascript
const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let's try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"])
```

### `technical-atom-c2bd4f426bf0f84c` code

Citation: (raw/javascriptallonge.pdf p.109-111)

```javascript
//=> 3
```

### `technical-atom-5d9fe5bf28074a51` exception

Citation: (raw/javascriptallonge.pdf p.109-111)

61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples.

### `technical-atom-9f1556f765136bb2` code

Citation: (raw/javascriptallonge.pdf p.109-111)

```
A more robust implementation would be (array) => array.length === 0 , but we are doing backflips to keep this within a very small and contrived playground.
```
