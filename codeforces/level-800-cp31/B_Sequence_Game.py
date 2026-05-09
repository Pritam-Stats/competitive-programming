# ================================
# Author: Pritam
# ================================

# Link: https://codeforces.com/problemset/problem/1862/B

import sys
input = sys.stdin.readline
# ---------- Helpers ----------
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def ins():
    return input().strip()
def inmap():
    return map(int, input().split())
# ---------- Solve Function ----------

def solve():
    n = inp()
    b = inlt()

    a = []
    a.append(b[0])
    for i in range(1, n):
        if b[i-1] <=b[i] :
            a.append(b[i])
        else:
            a.append(1)
            a.append(b[i])
    print(len(a))
    print(*a)

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 