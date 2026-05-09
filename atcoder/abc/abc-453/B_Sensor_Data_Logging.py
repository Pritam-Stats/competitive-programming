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
    t, x = inmap()
    nums = inlt()

    saved = []
    saved.append(0)

    for i in range(1, t+1):
        if abs(nums[i] - nums[saved[-1]]) >= x:
            saved.append(i)

    for t in saved:
        print(*[t, nums[t]])


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        solve() 