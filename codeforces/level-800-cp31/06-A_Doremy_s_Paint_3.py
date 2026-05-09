# ================================
# Author: Pritam
# ================================

'''
Problem: https://codeforces.com/problemset/problem/1890/A
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

    if n == 2:
        print("YES")
    elif n > 2:
        uniq = len(set(nums))
        if uniq == 1:
            print("YES")
        elif uniq > 2:
            print("NO")
        else:
            #calculate freq
            from collections import Counter
            freq = Counter(nums)
            vals = list(freq.values())
            if abs(vals[0] - vals[1]) <= 1:
                print("YES")
            else:
                print("NO")





# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 