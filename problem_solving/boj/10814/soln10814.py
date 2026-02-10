"""
# 백준
# No. 10814
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    A = [sys.stdin.readline().split() for _ in range(N)]

    # Logic
    A.sort(key=lambda x: int(x[0]))

    # Output
    for a in A:
        print(*a)


if __name__ == "__main__":
    main()
