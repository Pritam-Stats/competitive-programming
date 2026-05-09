import sys
input = sys.stdin.readline

DEBUG = False


def debug(*args, **kwargs):
    if not DEBUG:
        return
    print("----- DEBUG -----", file=sys.stderr)
    for arg in args:
        print(repr(arg), file=sys.stderr)
    for key, value in kwargs.items():
        print(f"{key} = {repr(value)}", file=sys.stderr)
    print("-----------------", file=sys.stderr)


def main():
    string = input()
    strList = list(string)
    if strList[0] == 'a' or strList[1] == 'b' or strList[2] == 'c':
        print("YES")
        return
    print("NO")


def solve():
    t = 1
    t = int(input())
    for _ in range(t):
       main()


if __name__ == "__main__":
    solve()

