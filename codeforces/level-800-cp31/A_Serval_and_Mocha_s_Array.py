# Link https://codeforces.com/problemset/problem/1789/A

# ================================
# Author: Pritam
# ================================


import sys
input = sys.stdin.readline
# ---------- Helpers ----------
def ceil(a, b):    ##relation b/w floor division and ceil division
    return (a+b-1)//b
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def ins():
    return input().strip()
def inmap():
    return map(int, input().split())
def print_fast(*args):
    sys.stdout.write(" ".join(map(str, args)) + '\n')
# ---------- Solve Function ----------

from math import gcd
def solve():
    n = inp()
    nums = inlt()

    isBeautiful = False
    for i in range(n):
        for j in range(i+1, n): ## Just check if gcd of any pair is less than or equal to 2
            if gcd(nums[i], nums[j]) <= 2:      ## O(log2 min(a, b))
                isBeautiful = True

    ##since we only checked for len of at least 2
    if isBeautiful:
        print("Yes")
    else:
        print("No")


### TC: O(n^2 * log_2(min(a, b))) = O(10^4 * 20) = O(2 * 10^5)
### SC: O(1)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 