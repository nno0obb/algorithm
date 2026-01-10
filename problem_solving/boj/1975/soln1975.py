"""
# 백준
# No. 1975
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import Counter
from functools import reduce


def main():
    # Logic
    MAX_N = 1000
    dp = [0] * (MAX_N + 1)
    for i in range(2, MAX_N + 1):
        for j in range(2, i + 1):
            num = i
            while num % j == 0:
                num //= j
                dp[i] += 1

    # Input
    T = int(input())
    for _ in range(T):
        N = int(sys.stdin.readline().strip())

        # Output
        print(dp[N])


if __name__ == "__main__":
    main()
