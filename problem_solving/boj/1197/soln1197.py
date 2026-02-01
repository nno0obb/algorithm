"""
# 백준
# No. 1197
# Python 3.11.9
# by "nno0obb"
"""

import sys

sys.setrecursionlimit(1_000_000)


def main():
    # Input
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        A, B, C = map(int, sys.stdin.readline().strip().split())
        edges.append((A, B, C))

    # Logic
    edges.sort(key=lambda x: x[::-1])

    P = list(range(V + 1))

    def find(x: int) -> int:
        if P[x] != x:
            P[x] = find(P[x])
        return P[x]

    def union(x: int, y: int) -> None:
        a = find(min(x, y))
        b = find(max(x, y))
        if a != b:
            P[b] = a

    ans = 0
    for A, B, C in edges:
        if find(A) != find(B):
            union(A, B)
            ans += C

    # Output
    print(ans)


if __name__ == "__main__":
    main()
