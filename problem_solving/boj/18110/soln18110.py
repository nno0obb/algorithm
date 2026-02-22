"""
# 백준
# No. 18110
# Python 3.11.9
# by "nno0obb"
"""

import sys
from math import floor


def main():
    # Input
    N = int(input())
    A = [int(sys.stdin.readline().strip()) for _ in range(N)]

    # Logic
    A.sort()
    k = floor(N * 0.15 + 0.5)
    _sum = sum(A[k : N - k])
    avg = sum(A[k : N - k]) / (N - 2 * k) if _sum > 0 else 0
    ans = floor(avg + 0.5)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
