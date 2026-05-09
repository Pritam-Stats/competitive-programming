'''
Problem: https://codeforces.com/problemset/problem/1900/A
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
    s = ins()

    continuous_3_empty_cells = False
    total_cnt_empty_cells = 0
    for i in range(n):
        if s[i] == '.' and i+2< n and s[i+1] == s[i+2] == '.':
            continuous_3_empty_cells = True
        
        if s[i] == '.':
            total_cnt_empty_cells += 1

    if continuous_3_empty_cells:
        print(2)
    else:
        print(total_cnt_empty_cells)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 