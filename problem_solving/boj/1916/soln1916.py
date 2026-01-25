"""
# 백준
# No. 1916
# Python 3.11.9
# by "nno0obb"
"""

import heapq
import sys
from collections import defaultdict


def main():
    # Input
    N = int(input())
    M = int(input())
    G = defaultdict(dict)
    for _ in range(M):
        s, e, c = map(int, sys.stdin.readline().strip().split())
        G[s][e] = c if e not in G[s] else min(c, G[s][e])
    S, E = map(int, input().split())

    # Logic
    dp = [float("inf")] * (N + 1)

    que = [(0, S)]
    dp[S] = 0

    while que:
        curr_cost, curr_node = heapq.heappop(que)
        if dp[curr_node] < curr_cost:
            continue
        if curr_node == E:
            break
        for next_node, next_cost in G[curr_node].items():
            if dp[next_node] > curr_cost + next_cost:
                dp[next_node] = curr_cost + next_cost
                heapq.heappush(que, (curr_cost + next_cost, next_node))

    # Output
    print(dp[E])


if __name__ == "__main__":
    main()
