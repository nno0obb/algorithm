"""
# 백준
# No. 1854
# Python 3.11.9
# by "nno0obb"
"""

import heapq
import sys
from collections import defaultdict


def main():
    # Input
    N, M, K = map(int, input().split())
    G = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        G[a].append((b, c))

    # Logic
    for val in G.values():
        val.sort(key=lambda x: x[1])

    dp = [[float("inf")] * (K + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = -1

    que = [(0, 1)]
    dp[1][1] = 0

    while que:
        curr_time, curr_node = heapq.heappop(que)
        for next_node, next_time in G[curr_node]:
            if dp[next_node][K] > curr_time + next_time:
                dp[next_node][K] = curr_time + next_time
                dp[next_node].sort()
                heapq.heappush(que, (curr_time + next_time, next_node))

    # Output
    for i in range(1, N + 1):
        print(-1 if dp[i][K] == float("inf") else dp[i][K])


if __name__ == "__main__":
    main()
