"""
# 백준
# No. 10773
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    K = int(input())
    A = [int(sys.stdin.readline().strip()) for _ in range(K)]

    # Logic
    stack = []
    for num in A:
        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    ans = sum(stack)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
