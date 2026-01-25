"""
# 백준
# No. 11657
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, M = map(int, input().split())
    E = []
    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().strip().split())
        E.append((A, B, C))

    # Logic
    dp = [float("inf")] * (N + 1)
    dp[1] = 0

    for i in range(1, N + 1):
        for a, b, c in E:
            if dp[a] == float("inf"):
                continue
            if dp[b] > dp[a] + c:
                dp[b] = dp[a] + c

    has_negative_cycle = False
    for a, b, c in E:
        if dp[a] == float("inf"):
            continue
        if dp[b] > dp[a] + c:
            has_negative_cycle = True
            break

    # Output
    if has_negative_cycle:
        print(-1)
    else:
        for i in range(2, N + 1):
            print(dp[i] if dp[i] != float("inf") else -1)


if __name__ == "__main__":
    main()
