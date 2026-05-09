# Link: https://codeforces.com/problemset/problem/1853/A

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
def print_fast(*args):
    sys.stdout.write(" ".join(map(str, args)) + '\n')
# ---------- Solve Function ----------

def solve():
    n = inp()
    nums = inlt()

    minDifference = float("inf")
    for i in range(1, n):
        minDifference = min(nums[i] - nums[i-1], minDifference)

    if minDifference < 0:   #already sorted
        print(0)
        # return
    elif minDifference == 0:
        print(1)
    else:
        print(int(minDifference/2) + 1)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 