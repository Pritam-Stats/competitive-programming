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
from collections import Counter
def solve():
    A = [inlt() for _ in range(3)]
    # print(A)
    cnt = 0
    for x in A[0]:
        for y in A[1]:
            for z in A[2]:
                d = [x, y, z]

                if sorted(d) == [4, 5, 6]:
                    cnt += 1


    print(f"{cnt/(6**3):.6f}")


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        solve() 