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

    ans = []
    div6 = []
    div3 = []
    div2 = []
    div = []
    for x in nums:
        if x %6 == 0:
            div6.append(x)
        elif x%2 == 0:
            div2.append(x)
        elif x%3 == 0:
            div3.append(x)
        else:
            div.append(x)

    ans = div2 + div + div3 + div6

    print_fast(*ans)

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 