"""
# 백준
# No. 18352
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import deque


def main():
    # Input
    N, M, K, X = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().strip().split())
        G[A].append(B)

    # Logic
    is_visited = [False] * (N + 1)
    que = deque()

    que.append((X, 0))
    is_visited[X] = True

    ans = []
    while que:
        c, d = que.popleft()

        if d == K:
            ans.append(c)
            continue

        for n in G[c]:
            if not is_visited[n]:
                que.append((n, d + 1))
                is_visited[n] = True

    if not ans:
        ans.append(-1)

    # Output
    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
