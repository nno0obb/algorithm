"""
# 백준
# No. 1219
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, S, E, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().strip().split())
        edges.append((u, v, w))
    money = list(map(int, input().split()))

    # Logic
    dp = [float("inf")] * N
    dp[S] = -money[S]

    for _ in range(N - 1):
        for u, v, w in edges:
            if dp[u] == float("inf"):
                continue
            if dp[v] > dp[u] + w - money[v]:
                dp[v] = dp[u] + w - money[v]

    dp1 = dp.copy()

    for u, v, w in edges:
        if dp[u] == float("inf"):
            continue
        if dp[v] > dp[u] + w - money[v]:
            dp[v] = dp[u] + w - money[v]

    dp2 = dp.copy()

    nodes_in_negative_cycle = []
    for i in range(N):
        if dp1[i] != dp2[i]:
            nodes_in_negative_cycle.append(i)

    is_Gee = False
    for T in nodes_in_negative_cycle:
        dp = [float("inf")] * N
        dp[T] = -money[T]

        for _ in range(N - 1):
            for u, v, w in edges:
                if dp[u] == float("inf"):
                    continue
                if dp[v] > dp[u] + w - money[v]:
                    dp[v] = dp[u] + w - money[v]

        if not is_Gee:
            is_Gee = dp1[T] != float("inf") and dp[E] != float("inf")

    # Output
    if is_Gee:
        print("Gee")
    elif dp1[E] == float("inf"):
        print("gg")
    else:
        print(-dp1[E])


if __name__ == "__main__":
    main()
