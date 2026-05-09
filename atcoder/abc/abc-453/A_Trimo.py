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

    cnt = 0
    idx = 0
    for i in range(n):
        if s[i] != 'o':
            idx = i
            break
        else:
            cnt += 1
    
    
    print(s[idx:] if cnt != n else "")



    


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        solve() 