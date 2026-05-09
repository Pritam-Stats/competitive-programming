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
    L = inlt()

    curr = 0.5
    cnt = 0
    for l in L:
        if curr < 0:
            curr += l
            if curr > 0:
                cnt += 1
        elif curr > 0:
            curr -= l
            if curr < 0:
                cnt += 1
        else:
            continue
        
    print(cnt)




# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        solve() 