

## CodeForces Problems
- [Level 800 Problems](./level-800-cp31)

---



### Codeforces 1881A — Don't Try to Count

#### Problem Idea

You are given two strings:

* `x` (initial string)
* `s` (target substring)

Operation:

* In one step, you can **append `x` to itself** → `x = x + x`

Goal:

* Find the **minimum number of operations** required so that `s` appears as a **substring of `x`**
* If impossible, return `-1`

---

#### Key Insight

Instead of simulating indefinitely, observe:

1. Keep doubling `x` until:

   ```
   len(x) >= len(s)
   ```

   Because a shorter string can never contain a longer substring.

2. Even after reaching sufficient length, `s` might not appear due to **boundary overlap**.

3. So, check at most **2 additional doublings**.

---

#### Approach

1. Initialize `cnt = 0`
2. While `len(x) < len(s)`:

   * Double `x`
   * Increment `cnt`
3. Try up to **2 more expansions**:

   * If `s in x`, return `cnt`
   * Else, double again
4. If still not found → return `-1`


#### Complexity

* Time: `O(len(s))` (amortized, due to bounded expansions)
* Space: `O(len(s))`

---

#### Common Mistakes

* Stopping early using arbitrary limits (e.g., `n <= 25`)
* Not checking substring after reaching required length
* Missing edge cases where substring appears after overlap

---

#### Takeaway

This is a **string growth + pattern alignment** problem:

* Grow until feasible
* Then check limited extra cases for alignment



---


## CF 1866 A - Ambitious Kid
Link:: https://codeforces.com/problemset/problem/1866/A

## CF 1862 B - 
Link: https://codeforces.com/problemset/problem/1862/B