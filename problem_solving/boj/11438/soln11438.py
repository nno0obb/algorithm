"""
# 백준
# No. 11437
# Python 3.11.9
# by "nno0obb"
"""

import math
import sys
from collections import defaultdict, deque


def main():
    # Input
    N = int(input())
    G = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        G[a].append(b)
        G[b].append(a)
    M = int(input())
    Q = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

    # Logic
    k = math.ceil(math.log2(N))
    P = [[0] * (N + 1) for _ in range(k + 1)]  # P[k][n]
    D = [-1] * (N + 1)
    que = deque()

    P[1][0] = 0
    D[1] = 0
    que.append((1, 0))

    while que:
        c, d = que.popleft()
        for n in G[c]:
            if D[n] == -1:
                P[0][n] = c
                D[n] = d + 1
                que.append((n, d + 1))

    for i in range(1, k + 1):
        for j in range(1, N + 1):
            P[i][j] = P[i - 1][P[i - 1][j]]

    for a, b in Q:
        if D[a] < D[b]:
            a, b = b, a

        for i in range(k, -1, -1):
            if D[a] - D[b] >= (2**i):
                a = P[i][a]

        for i in range(k, -1, -1):
            if a == b:
                break

            if P[i][a] != P[i][b]:

                a = P[i][a]
                b = P[i][b]

        if a != b:
            a = P[0][a]

        # Output
        print(a)


if __name__ == "__main__":
    main()
