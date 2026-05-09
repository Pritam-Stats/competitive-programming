'''
Problem: https://codeforces.com/problemset/problem/1873/C
'''

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
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    cnt5 = 0
    ans = 0
    mat = []
    for _ in range(10):
        mat.append(list(ins()))

    #outer ring
    for col in range(10):
        if mat[0][col] == "X":
            cnt1 += 1
        if mat[9][col] == "X":
            cnt1 += 1

    for row in range(1, 9):
        if mat[row][0] == "X":
            cnt1 += 1
        if mat[row][9] == "X":
            cnt1 += 1

    ans += cnt1*1


    #2nd ring
    for col in range(1, 9):
        if mat[1][col] == "X":
            cnt2 += 1
        if mat[8][col] == "X":
            cnt2 += 1

    for row in range(2, 8):
        if mat[row][1] == "X":
            cnt2 += 1
        if mat[row][8] == "X":
            cnt2 += 1
    ans += cnt2 *2
    
    
    #3rd ring
    for col in range(2,8):
        if mat[2][col] == "X":
            cnt3 += 1
        if mat[7][col] == "X":
            cnt3 += 1

    for row in range(3, 7):
        if mat[row][2] == "X":
            cnt3 += 1
        if mat[row][7] == "X":
            cnt3 += 1
    ans += cnt3 * 3
    

    #4th ring
    for col in range(3,7):
        if mat[3][col] == "X":
            cnt4 += 1
        if mat[6][col] == "X":
            cnt4 += 1

    for row in range(4, 6):
        if mat[row][3] == "X":
            cnt4 += 1
        if mat[row][6] == "X":
            cnt4 += 1
    ans += cnt4 * 4
    
    #5th ring
    for col in range(4,6):
        if mat[4][col] == "X":
            cnt5 += 1
        if mat[5][col] == "X":
            cnt5 += 1
    
    ans += cnt5 * 5
    print(ans)


    # print(mat)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 