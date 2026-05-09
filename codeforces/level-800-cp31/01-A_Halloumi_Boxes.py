# ================================
# Author: Pritam
# ================================
'''
    Link: https://codeforces.com/problemset/problem/1903/A
'''

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
    n, k = inmap()
    nums = inlt()
    if nums == sorted(nums):
        print("YES")
    else:
        if k ==1:
            print("NO")
        else:
            print("YES")            


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve()