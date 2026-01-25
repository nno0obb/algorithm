"""
# 백준
# No. 1948
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import defaultdict, deque


def main():
    # Input
    N = int(input())
    M = int(input())
    G = defaultdict(dict)
    E = [0] * (N + 1)
    for _ in range(M):
        U, V, W = map(int, sys.stdin.readline().split())
        G[U][V] = W
        E[V] += 1
    한걸음, 로마 = map(int, input().split())

    # Logic
    dp1 = [-1] * (N + 1)  # for 시간
    dp2 = [[] for _ in range(N + 1)]  # for 도로

    que = deque()
    que.append(한걸음)
    dp1[한걸음] = 0

    while que:
        c = que.popleft()
        if c == 로마:
            continue

        for n in G[c]:
            E[n] -= 1
            if dp1[n] < dp1[c] + G[c][n]:
                dp1[n] = dp1[c] + G[c][n]
                dp2[n] = [c]
            elif dp1[n] == dp1[c] + G[c][n]:
                dp2[n].append(c)

            if E[n] == 0:
                que.append(n)

    ans_1 = dp1[로마]

    que = deque()
    is_visited = set()
    que.append(로마)

    ans_2 = 0
    while que:
        c = que.popleft()
        for n in dp2[c]:
            if not (c, n) in is_visited:
                is_visited.add((c, n))
                que.append(n)
                ans_2 += 1

    # Output
    print(ans_1)
    print(ans_2)


if __name__ == "__main__":
    main()
