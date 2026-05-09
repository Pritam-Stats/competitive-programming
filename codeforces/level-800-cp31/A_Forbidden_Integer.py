# Link: https://codeforces.com/problemset/problem/1845/A

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
def print_fast(*args):
    sys.stdout.write(" ".join(map(str, args)) + '\n')
# ---------- Solve Function ----------

def solve():
    n, k, x = inmap()

    if x != 1:
        print(f"YES")
        print(n)
        print(*([1]*n))
    else:
        if k == 1 or (k == 2 and n%2 == 1):
            print("NO")
        else:
            print("YES")
            if n%2 == 0:
                print(n//2)
                print(*([2]*(n//2)))
            else:
                #all 2s and one 3
                print((n-3)//2+1)
                ans = [2]*(((n-3)//2)) + [3]
                print(*ans)

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 