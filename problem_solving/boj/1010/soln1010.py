"""
# 백준
# No. 1010
# Python 3.11.9
# by "nno0obb"
"""

import math

# Global Variables
MAX_N = 30
MAX_M = 30


def main():
    # Logic
    dp = [[0] * (MAX_N + 1) for _ in range(MAX_M + 1)]
    for m in range(MAX_M + 1):
        for n in range(MAX_N + 1):
            if n == 0 or m == n:
                dp[m][n] = 1
            else:
                dp[m][n] = dp[m - 1][n - 1] + dp[m - 1][n]
    # Input
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        ans = dp[M][N]

        # Output
        print(ans)


if __name__ == "__main__":
    main()
