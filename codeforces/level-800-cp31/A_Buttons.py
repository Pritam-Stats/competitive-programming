# Link https://codeforces.com/problemset/problem/1858/A

# ================================
# Author: Pritam
# ================================


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
    a, b, c = inmap()

    if a > b:
        print("First")
    elif a == b:
        if c % 2 != 0:
            print("First")
        else:
            print("Second")
    else:
        print("Second")


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 