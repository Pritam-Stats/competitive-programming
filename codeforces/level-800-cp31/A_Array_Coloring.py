# Link https://codeforces.com/problemset/problem/1857/A

# ================================
# Author: Pritam
# ================================
'''
Argument : If the count of the odd numbers is odd, then yes, otherwise no

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
    n = inp()
    nums = inlt()

    odd_cnt = 0
    for x in nums:
        if x%2 != 0:
            odd_cnt += 1
    
    if odd_cnt % 2 == 0:
        print("YES")
    else:
        print("NO")


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 