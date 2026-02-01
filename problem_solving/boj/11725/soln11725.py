"""
# 백준
# No. 11725
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import deque


def main():
    # Input
    N = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        A, B = map(int, sys.stdin.readline().strip().split())
        G[A].append(B)
        G[B].append(A)

    # Logic
    P = [-1] * (N + 1)

    que = deque()
    que.append(1)
    P[1] = 0

    while que:
        c = que.popleft()
        for n in G[c]:
            if P[n] == -1:
                que.append(n)
                P[n] = c

    # Output
    print(*P[2:], sep="\n")


if __name__ == "__main__":
    main()
