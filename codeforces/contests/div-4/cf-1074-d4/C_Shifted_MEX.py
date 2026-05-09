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
    a = set(inlt())
    a.sort()

    mex = 0
    for x in a:
        if x<=mex:
            mex+=1
        else:
            break
    
    print(mex)
    

    




# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve()