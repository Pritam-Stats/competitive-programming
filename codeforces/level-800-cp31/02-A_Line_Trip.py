'''
    Problem: https://codeforces.com/problemset/problem/1901/A
'''

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
    n, x = inmap()
    nums = inlt()
    nums = [0] + nums
    dis = 0
    maxDis = (x - nums[-1])*2
    for i in range(n):
        dis = nums[i+1] - nums[i]
        maxDis = max(maxDis, dis)
    print(maxDis)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve()