"""
# 백준
# No. 11404
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    M = int(input())
    A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

    # Logic
    dp = [[float("inf")] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][i] = 0
    for a, b, c in A:
        dp[a][b] = min(dp[a][b], c)

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # Output
    for i in range(1, N + 1):
        print(*map(lambda x: x if x != float("inf") else 0, dp[i][1:]))


if __name__ == "__main__":
    main()
