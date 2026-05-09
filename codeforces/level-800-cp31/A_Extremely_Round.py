# Link https://codeforces.com/problemset/problem/1766/A


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


# store all the round numbers
# roundNums = list(range(1, 11))
# for x in range(11, 1000000):
#     p = len(str(x)) - 1
#     if x % (10**p) == 0:
#         roundNums.append(x)

def solve():
    n = str(inp())
    d = len(n)
    first = int(n[0])

    ans = (d - 1) * 9 + first
    print(ans)
    
    # ans = 0
    # for nums in roundNums:
    #     if nums <= n:
    #         ans += 1
    #     else:
    #         break
    # print(ans)


'''TLE    if n<=10:
        print(n)
        return
    ans = 10
    for x in range(11, n+1):
        p = len(str(x)) - 1
        if x%(10**p) == 0:
            ans += 1
    print(ans)
    
    # TC: 10^9
    
    '''


# ---------- Main ----------
if __name__ == "__main__":
    
    t = 1
    t = inp()
    for _ in range(t):
        solve() 