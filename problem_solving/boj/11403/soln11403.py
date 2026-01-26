"""
# 백준
# No. 11403
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    G = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    # Logic
    dp = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1:
                dp[i][j] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # Output
    for i in range(N):
        print(*map(lambda x: int(x != float("inf")), dp[i]))


if __name__ == "__main__":
    main()
