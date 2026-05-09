# ================================
# Author: Pritam
# ================================

## 1777A
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
    a = inlt()

    ans = 0
    for i in range(n-1, 0, -1):
        if (a[i]&1) == a[i-1]&1:
            #same last bit ==> same parity
            ans += 1
            a[i-1] = a[i]*a[i-1]
            a.pop()
    print(ans)


# Time: O(n)
# Space: O(1)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 