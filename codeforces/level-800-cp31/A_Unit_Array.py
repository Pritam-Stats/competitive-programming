# Link: https://codeforces.com/problemset/problem/1834/A

# ================================
# Author: Pritam
# ================================

from collections import Counter
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
    c = Counter(nums)
    ans = 0
    pc = c[1]
    nc = c[-1]
    # print(pc, nc)
    while nc > pc or nc % 2 != 0:
        ans += 1
        pc += 1
        nc -= 1
    
    print(ans)





# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 