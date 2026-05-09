# ================================
# Author: Pritam
# ================================
# Link https://codeforces.com/problemset/problem/1805/A

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

def solve():
    n = inp()
    nums = inlt()
    total_xor = 0   ## 0 ^ a = a
    for num in nums:
        total_xor ^= num
    
    if n%2 == 1:
        print(total_xor)
    else:
        print(0 if total_xor == 0 else -1)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 