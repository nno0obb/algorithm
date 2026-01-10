"""
# 백준
# No. 1033
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque
from math import gcd, lcm


def main():
    # Input
    N = int(input())
    ABPQ = [list(map(int, input().split())) for _ in range(N - 1)]

    # Logic
    G = [[] for _ in range(N)]
    R = [[None] * N for _ in range(N)]
    P = 1
    for a, b, p, q in ABPQ:
        _gcd = gcd(p, q)
        _p, _q = p // _gcd, q // _gcd
        P *= _p
        P *= _q
        R[a][b] = (_p, _q)
        R[b][a] = (_q, _p)
        G[a].append(b)
        G[b].append(a)

    dp = [-1] * N
    is_visited = [False] * N
    que = deque()

    dp[0] = P
    que.append(0)
    is_visited[0] = True

    while que:
        c = que.popleft()
        for n in G[c]:
            if not is_visited[n]:
                p, q = R[c][n]
                dp[n] = dp[c] * q // p
                is_visited[n] = True
                que.append(n)

    A_gcd = gcd(*dp)
    for i in range(N):
        dp[i] //= A_gcd

    # Output
    print(*dp)


if __name__ == "__main__":
    main()
