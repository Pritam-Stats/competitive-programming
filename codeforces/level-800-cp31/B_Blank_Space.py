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

def solve():
    n = inp()
    nums = inlt()

    maxLen = 0
    currLen = 0
    for i in range(n):
        if nums[i] == 0:
            currLen += 1
        else:
            currLen = 0
        maxLen = max(currLen, maxLen)
    print(maxLen)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 