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
    s = ins()
    mod = 998244353
    n = len(s)
    ans = 0
    l= 1
    for i in range(1, n):
        if s[i-1] != s[i]:
            l += 1
        else:
            ans += (l* (l+1)//2)
            ans = ans%mod

            l = 1

    ans += (l * (l+1)//2)
    ans = ans%mod
    print(ans)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        solve() 