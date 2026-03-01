"""
# 백준
# No. 10828
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    CMD = [sys.stdin.readline().strip() for _ in range(N)]

    # Logic
    stack = []
    for cmd in CMD:
        a, *b = cmd.split()
        if a == "push":
            stack.append(int(b[0]))
        elif a == "pop":
            # Output
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif a == "size":
            # Output
            print(len(stack))
        elif a == "empty":
            # Output
            print(0 if stack else 1)
        elif a == "top":
            # Output
            if stack:
                print(stack[-1])
            else:
                print(-1)


if __name__ == "__main__":
    main()
