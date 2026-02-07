"""
# 백준
# No. 1915
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, M = map(int, input().split())
    B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    # Logic
    dp = [[0] * M for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if B[i][j] == 1:
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 1
                ans = max(ans, dp[i][j] ** 2)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
