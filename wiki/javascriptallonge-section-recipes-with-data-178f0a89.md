---
page_id: javascriptallonge-section-recipes-with-data-178f0a89
page_kind: source
page_family: section-reference
summary: Recipes with Data: 53 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-178f0a89@e2b2f7c9f5b03c53514ddbe5f2253dbd
---

# Recipes with Data

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-recipes-with-data-disclaimer-92143eef]] - narrower source section: Recipes with Data / Disclaimer
- [[javascriptallonge-section-recipes-with-data-flip-2cae94c7]] - narrower source section: Recipes with Data / Flip
- [[javascriptallonge-section-recipes-with-data-mapwith-588e9415]] - narrower source section: Recipes with Data / mapWith
- [[javascriptallonge-section-recipes-with-data-object-assign-c62f7bb5]] - narrower source section: Recipes with Data / Object.assign
- [[javascriptallonge-section-recipes-with-data-why-d85ef4c4]] - narrower source section: Recipes with Data / Why?

## Statements by subsection

### Recipes with Data / Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-7239e085-01428))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-7239e085-01428))_
- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-7239e085-01428))_

### Recipes with Data / mapWith

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map : _(javascriptallonge.pdf (source-range-7239e085-01437))_
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-01440))_
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-7239e085-01442))_
- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-7239e085-01444))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-7239e085-01437))_

### Recipes with Data / Flip

- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry : _(javascriptallonge.pdf (source-range-7239e085-01462))_
- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-7239e085-01462))_

### Recipes with Data / Flip / self-currying flip

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip : _(javascriptallonge.pdf (source-range-7239e085-01466))_

### Recipes with Data / Flip / flipping methods

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-7239e085-01470))_

### Recipes with Data / Object.assign

- Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object: _(javascriptallonge.pdf (source-range-7239e085-01477))_

### Recipes with Data / Why?

- Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-7239e085-01489))_
- So again, why include the recipe? Well, besides all of the practical applications that combinators provide, there is this little thing called The joy of working things out. _(javascriptallonge.pdf (source-range-7239e085-01490))_
- There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. Use it as an excuse to get familiar with your environment's debugging facility. _(javascriptallonge.pdf (source-range-7239e085-01491))_
- One tip is to use JavaScript to name things. For example, you could start by writing: _(javascriptallonge.pdf (source-range-7239e085-01492))_
- What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-7239e085-01494))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-7239e085-01494))_

## Technical atoms

### Technical atom 1

<a id="atom-technical-atom-f0038b4fa2ed7051"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01463))_

```text
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

</details>
