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
    a = ins()
    b = ins()

    # ans = []
    bal_a, bal_b = 0, 0
    for i in range(n):
        if a[i] == b[i]:
            if a[i] == "(":
                bal_a += 1
                bal_b += 1
            else:
                bal_a -= 1
                bal_b -= 1
        else:
            if bal_a < bal_b:
                bal_a += 1
                bal_b -= 1
            else:
                bal_a -= 1
                bal_b += 1

        if bal_a < 0 or bal_b < 0:
            print("NO")
            return

    if bal_a == 0 and bal_b == 0:
        print("YES")
    else:
        print("NO")
    

        

        



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve()



I=input().strip()
if I:
    for _ in range(int(I)):
        r, a, b, c, ok = int(input()), input().strip(), input().strip(), 0, True
        for i, (x, y) in enumerate(zip(a, b), 1):
            c+=(x=='(')+(y=='(')-1
            if c<i%2: ok=False
        print("YES" if ok and c==0 else "NO")
