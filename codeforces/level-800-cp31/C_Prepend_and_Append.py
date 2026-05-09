# ================================
# Author: Pritam
# ================================


import sys
input = sys.stdin.readline
# ---------- Helpers ----------


def ceil(a, b):  # relation b/w floor division and ceil division
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


def solve():
    n = inp()
    s = ins()

    l, r = 0, n-1
    L = 0
    R = 0

    while l <= r:
        if s[l] != s[r]:
            l += 1
            r -= 1
        else:
            L = l
            R = r
            break
    print(R-L+1)
    # print(r-l+1)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve()
