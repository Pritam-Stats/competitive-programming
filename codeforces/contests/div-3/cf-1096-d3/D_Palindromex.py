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
    present = [False]*(n+1)
    palNums = []
    maxMex = 0
    for c in range(4*n -1):
        if c%2 == 0:
            l, r = c//2, c//2
        else:
            l, r = c//2, c//2 + 1
        
        while l>=0 and r < 2*n and nums[l] == nums[r]:
            if not present[nums[l]]:
                present[nums[l]] = True
                palNums.append(nums[l])
        
            l -= 1
            r += 1
        if palNums:
            mex = 0
            while present[mex]:
                mex += 1
            
            if mex > maxMex:
                maxMex = mex

            for x in palNums:
                present[x] = False
            palNums.clear()
    print_fast(maxMex)





# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 