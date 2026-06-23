---
page_id: javascriptallonge-once
page_kind: source
summary: Once from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.88-88
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

The "Once" chapter from JavaScript Allongé introduces the once combinator, a function that ensures another function can only be called once.

## Key supported claims

- once is an extremely helpful combinator. (raw/javascriptallonge.pdf p.88-88)
- It ensures that a function can only be called, well, once. (raw/javascriptallonge.pdf p.88-88)
- That function will call your function once, and thereafter will return undefined whenever it is called. (raw/javascriptallonge.pdf p.88-88)
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. (raw/javascriptallonge.pdf p.88-88)

## Technical details

### `technical-atom-86c133660af7308d` code

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
const once = (fn) => { let done = false ; return function () { return done ? void 0 : ((done = true ), fn.apply( this , arguments)) } }
```

### `technical-atom-94efa685814f6560` code

Citation: (raw/javascriptallonge.pdf p.88)

```javascript
const askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() //=> 'sure, why not?' askedOnBlindDate() //=> undefined askedOnBlindDate() //=> undefined
```

### `technical-atom-f74baf81c6759358` exception

Citation: (raw/javascriptallonge.pdf p.88)

It ensures that a function can only be called, well, once .

### `technical-atom-7b7d103b3baeda3d` exception

Citation: (raw/javascriptallonge.pdf p.88)

It seems some people will only try blind dating once.
