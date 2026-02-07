"""
# 백준
# No. 11049
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    M = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    # Logic
    dp = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for l in range(1, N):
        for i in range(N - l):
            j = i + l
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + M[i][0] * M[k][1] * M[j][1])

    ans = dp[0][N - 1]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
