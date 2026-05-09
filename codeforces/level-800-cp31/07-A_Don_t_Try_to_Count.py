'''
Link: https://codeforces.com/problemset/problem/1881/A
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
    n, m = inmap()
    x = ins()
    s = ins()

    cnt = 0
    while n < m:
        x += x
        cnt += 1
        n = len(x)
        
    for _ in range(2):
        if s in x:
            print(cnt)
            return
        x += x
        cnt += 1
    print(-1)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 