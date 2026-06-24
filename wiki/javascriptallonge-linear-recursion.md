---
page_id: javascriptallonge-linear-recursion
page_kind: source
summary: linear recursion from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.111-113
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section from JavaScript Allongé introduces linear recursion as a form of divide and conquer strategy for problem solving in programming.

## Key supported claims

- Linear recursion is a divide and conquer strategy (raw/javascriptallonge.pdf p.111-113).
- It breaks problems into smaller subproblems (raw/javascriptallonge.pdf p.111-113).
- It solves subproblems recursively (raw/javascriptallonge.pdf p.111-113).
- Flattening arrays uses linear recursion (raw/javascriptallonge.pdf p.111-113).
- Terminal case is empty or non-array element (raw/javascriptallonge.pdf p.111-113).

## Technical details

### `technical-atom-b90d24c56b098191` code

Citation: (raw/javascriptallonge.pdf p.111-113)

```javascript
Array.isArray("foo") //=> false Array.isArray(["foo"]) //=> true
```

### `technical-atom-0f5d51c0613f0645` code

Citation: (raw/javascriptallonge.pdf p.111-113)

```javascript
const flatten = ([first, ...rest]) => { if (first === undefined ) { return []; } else if (!Array.isArray(first)) { return [first, ...flatten(rest)]; } else { return [...flatten(first), ...flatten(rest)]; } } flatten(["foo", [3, 4, []]]) //=> ["foo",3,4]
```

### `technical-atom-aea77c39cd5beb20` procedure

Citation: (raw/javascriptallonge.pdf p.111-113)

Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame.

### `technical-atom-71d716e00f67fd7f` procedure

Citation: (raw/javascriptallonge.pdf p.111-113)

After a bit the water boils, and they turn off the burner and are lead to a second bench.

### `technical-atom-cc18b4c0ba818b9d` procedure

Citation: (raw/javascriptallonge.pdf p.111-113)

Sometimes we want to flatten an array, that is, an array of arrays needs to be turned into one array of elements that aren't arrays.

### `technical-atom-88748102cb4ec364` procedure

Citation: (raw/javascriptallonge.pdf p.111-113)

The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly.

### `technical-atom-bd467fb3a5b55878` procedure

Citation: (raw/javascriptallonge.pdf p.111-113)

62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array.

### `technical-atom-39ae632b99dd8d86` worked-example

Citation: (raw/javascriptallonge.pdf p.111-113)

Let's take another example.
