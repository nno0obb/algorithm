"""
# 백준
# No. 1976
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    M = int(input())
    G = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    cities = list(map(int, input().split()))

    # Logic
    G.insert(0, [0] * N)
    for row in G:
        row.insert(0, 0)

    P = list(range(N + 1))

    def find(x: int) -> int:
        if P[x] != x:
            P[x] = find(P[x])
        return P[x]

    def union(x: int, y: int):
        a = find(min(x, y))
        b = find(max(x, y))
        if a != b:
            P[b] = a

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if G[i][j] == 1:
                union(i, j)

    ans = "YES"
    for city in cities[1:]:
        if find(city) != find(cities[0]):
            ans = "NO"
            break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
