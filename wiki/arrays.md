---
category: concept
summary: JavaScript arrays allow mutation via element reassignment even with `const`, and destructuring creates copies (unlike linked lists).
sources: raw/javascriptallonge.pdf p.141-157
updated: 2026-06-11
---

JavaScript arrays can be mutated by reassigning elements (e.g., `arr[0] = 'new'`), even when declared with `const`. Destructuring creates a copy rather than a reference, as shown in the example where modifying a destructured array does not affect the original. This contrasts with linked list structure sharing, where mutations propagate to aliases. See [[javascriptallonge-mutation]] for details on mutation mechanics and closure issues with `var`.
