"""
# 백준
# No. 1753
# Python 3.11.9
# by "nno0obb"
"""

import heapq
import sys
from collections import defaultdict


def main():
    # Input
    V, E = map(int, input().split())
    K = int(input())
    G = defaultdict(dict)
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().strip().split())
        G[u][v] = w if v not in G[u] else min(w, G[u][v])

    # Logic
    dp = [-1] * (V + 1)
    dp[K] = 0

    que = [(0, K)]
    while que:
        curr_dist, curr_node = heapq.heappop(que)

        for next_node, next_dist in G[curr_node].items():
            if dp[next_node] == -1 or dp[next_node] > curr_dist + next_dist:
                dp[next_node] = curr_dist + next_dist
                heapq.heappush(que, (curr_dist + next_dist, next_node))

    # Output
    for i in range(1, V + 1):
        print("INF" if dp[i] == -1 else 0 if i == K else dp[i])


if __name__ == "__main__":
    main()
