"""
# 백준
# No. 11650
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    # Logic
    A.sort()

    # Output
    for x, y in A:
        print(x, y)


if __name__ == "__main__":
    main()
