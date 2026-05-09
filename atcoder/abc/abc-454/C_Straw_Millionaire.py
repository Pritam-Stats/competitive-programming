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
    A = []
    B = []
    for _ in range(m):
        a, b = inmap()
        A.append(a)
        B.append(b)

    types = set()
    types.add(1)

    typesUpdated = True
    while typesUpdated:
        typesUpdated = False
        for a, b in zip(A, B):
            if a in types and b not in types:
                types.add(b)
                typesUpdated = True
    print(len(types))


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        solve() 