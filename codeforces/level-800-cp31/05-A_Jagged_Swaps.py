'''
Problem: https://codeforces.com/problemset/problem/1896/A
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
    n = inp()
    p = inlt()
    cnt = 0
    if p[0] == 1:
        print("YES")
    else:
        print("NO")


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 