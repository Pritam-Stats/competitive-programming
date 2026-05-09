# Link https://codeforces.com/problemset/problem/1788/A

# ================================
# Author: Pritam
# ================================


import sys
input = sys.stdin.readline
# ---------- Helpers ----------
def ceil(a, b):    ##relation b/w floor division and ceil division
    return (a+b-1)//b
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
from collections import Counter
def solve():
    n = inp()
    a = inlt()

    c = Counter(a)
    totalCnt = c[2]
    currCnt = 0
    ans = -1
    for i in range(n):
        if a[i] == 2:
            currCnt += 1
        
        if currCnt == (totalCnt - currCnt):
            ans = i+1

            break
    
    print(ans)






# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 