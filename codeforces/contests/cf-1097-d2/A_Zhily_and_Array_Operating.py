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
    a = inlt()
    cnt = 0
    for x in a:
        if x > 0:
            cnt += 1
    ans = cnt


    i = n-2
    while i >= 0:
        if a[i+1] >0:
            a[i] = a[i]+a[i+1]
        i -= 1

    cnt = 0
    for x in a:
        if x > 0:
            cnt += 1
    ans = max(ans, cnt)
    print(ans)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve()
