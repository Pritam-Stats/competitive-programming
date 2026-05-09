# ================================
# Author: Pritam
# ================================

# https://codeforces.com/problemset/problem/1837/A

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
def print_fast(*args):
    sys.stdout.write(" ".join(map(str, args)) + '\n')
# ---------- Solve Function ----------

def solve():
    x, k = inmap()

    if x % k == 0:
        print(2)
        print(x-1, 1)
    else:
        print(1)
        print(x)

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 