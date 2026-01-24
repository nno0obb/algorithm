"""
# 백준
# No. 2252
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import defaultdict, deque


def main():
    # Input
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        G[A].append(B)

    # Logic
    E = defaultdict(int)
    for i in range(1, N + 1):
        for j in G[i]:
            E[j] += 1

    ans = []
    que = deque()
    for i in range(1, N + 1):
        if E[i] == 0:
            que.append(i)

    while que:
        c = que.popleft()
        ans.append(c)

        for n in G[c]:
            E[n] -= 1
            if E[n] == 0:
                que.append(n)

    # Output
    print(*ans)


if __name__ == "__main__":
    main()
