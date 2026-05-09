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
    n = inp()
    a = inlt()

    if len(set(a)) == 1:
        print(-1)
        return
    
    b, c = [], []
    mx = max(a)

    for x in a:
        if x == mx:
            c.append(x)
        else:
            b.append(x)

    lens = [len(b), len(c)]

    print(*lens)
    print(*b)
    print(*c)

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 