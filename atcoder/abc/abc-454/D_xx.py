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


def get_canonical(s):
    stack = []
    for char in s:
        stack.append(char)
        # Check if the last 4 characters form '(xx)'
        if len(stack) >= 4 and stack[-4:] == ['(', 'x', 'x', ')']:
            # Remove the '(xx)'
            del stack[-4:]
            # Add 'xx' back to the stack
            stack.extend(['x', 'x'])
    return "".join(stack)

def solve():
    a = ins()
    b = ins()

    if a == b:
        print("Yes")
    else:
        if get_canonical(a) == get_canonical(b):
            print("Yes")
        else:
            print("No")

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    t = inp()
    for _ in range(t):
        solve() 