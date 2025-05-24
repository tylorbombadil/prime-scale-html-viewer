# Bug Framing Cheat Card: How to Ask for a Fast, Clean Fix

## Purpose
Use this guide to frame your bug reports in a way that makes it easy for ChatGPT (or any dev assistant) to zero in on the problem and solve it quickly.

---

## 1. Mention What the Code *Should* Be Doing
Example:
> “There should be only one dot drawn per note, and it should appear above the prime field.”

This sets a clear expectation boundary.

---

## 2. Ask to Scan All Draw or Effect Calls
Example:
> “Can you grep the file for `ctx.arc` or anything drawing on the canvas?”

This forces a wide scan instead of narrow patching.

---

## 3. Add a Console Debug Print
Even just:
```js
console.log("drawing dot")
```
Tells you immediately whether the loop is being reached or skipped.

---

## 4. Declare “This Should Be the Only Drawing Function”
Example:
> “drawLineReadout should be the only place anything is drawn.”

This lets the assistant know if other behavior is rogue.

---

## 5. If Something’s Still Wrong, Ask for a Function Audit
> “Can you list all functions that touch `ctx`?”

This surfaces hidden draw logic, transformations, or rogue copies.

---

## 6. Ask for a Structural Sanity Pass
> “Before patching, can you do a structural pass on the file to confirm how drawing is triggered?”

This adds a pre-flight before any changes are made.

---

## Endgame Tip
The best bug fix starts by *mapping the system*, not *swapping a part*.
