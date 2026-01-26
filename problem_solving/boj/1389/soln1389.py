"""
# 백준
# No. 1389
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, M = map(int, input().split())
    A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

    # Logic
    dp = [[float("inf")] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][i] = 0
    for a, b in A:
        dp[a][b] = 1
        dp[b][a] = 1

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    cnt, ans = float("inf"), 0
    for i in range(1, N + 1):
        num = sum(dp[i][1:])
        if cnt > num:
            cnt = num
            ans = i

    # Output
    print(ans)


if __name__ == "__main__":
    main()
