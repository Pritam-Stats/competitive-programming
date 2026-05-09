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
    n, m = inmap()
    F = inlt()

    if len(set(F)) == len(F):
        print("Yes")
    else:
        print("No")

    if len(set(F)) >= m:
        print("Yes")
    else:
        print("No")


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        solve()
