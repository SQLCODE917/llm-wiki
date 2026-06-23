---
page_id: javascriptallonge-destructuring-arrays
page_kind: source
summary: destructuring arrays from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.103-104
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on destructuring arrays from JavaScript Allongé, covering the basics of array destructuring and its use in JavaScript.

## Key supported claims

- Destructuring is a feature going back to Common Lisp (raw/javascriptallonge.pdf p.103-104).
- Destructuring allows code that resembles the data it consumes, a valuable coding style (raw/javascriptallonge.pdf p.103-104).
- The statement const [something] = wrapped; destructures the array represented by wrapped, binding the value of its single element to the name something (raw/javascriptallonge.pdf p.103-104).
- We saw how to construct an array literal using [ , expressions, , and ] (raw/javascriptallonge.pdf p.103-104).

## Technical details

### `technical-atom-2b49b2c4f34b42b9` code

Citation: (raw/javascriptallonge.pdf p.103-104)

```javascript
const wrap = (something) => [something]; Let's expand it to use a block and an extra name: wrapped = [something];
```

### `technical-atom-823b6abfea2ddeab` code

Citation: (raw/javascriptallonge.pdf p.103-104)

```javascript
const wrap = (something) => { const return wrapped; } wrap("package") //=> ["package"]
```

### `technical-atom-980204d14c5689c7` code

Citation: (raw/javascriptallonge.pdf p.103-104)

```javascript
const unwrap = (wrapped) => { const [something] = wrapped; return something; } unwrap(["present"]) //=> "present"
```

### `technical-atom-a84bd5b0bb352c4d` code

Citation: (raw/javascriptallonge.pdf p.103-104)

```javascript
const surname = (name) => { const [first, last] = name; return last; } surname(["Reginald", "Braithwaite"]) //=> "Braithwaite"
```

### `technical-atom-1e5a58d3eb938f40` code

Citation: (raw/javascriptallonge.pdf p.103-104)

```javascript
const description = (nameAndOccupation) => { const [[first, last], occupation] = nameAndOccupation; return ` ${ first } is a ${ occupation } `; } description([["Reginald", "Braithwaite"], "programmer"]) //=> "Reginald is a programmer"
```

### `technical-atom-ac5ee271e8f4ce47` formula

Citation: (raw/javascriptallonge.pdf p.103-104)

The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

### `technical-atom-49fd918f2d639091` worked-example

Citation: (raw/javascriptallonge.pdf p.103-104)

Here's an example of an array literal that uses a name:

### `technical-atom-4128e2b98a3a50ce` formula

Citation: (raw/javascriptallonge.pdf p.103-104)

The line const wrapped = [something]; is interesting.
