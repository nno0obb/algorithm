"""
# 백준
# No. 1717
# Python 3.11.9
# by "nno0obb"
"""

import sys

sys.setrecursionlimit(1_000_000)


def main():
    # Input
    N, M = map(int, input().split())
    CMD = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

    # Logic
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

    for t, a, b in CMD:
        if t == 0:
            union(a, b)
        elif t == 1:
            # Output
            print("YES" if find(a) == find(b) else "NO")


if __name__ == "__main__":
    main()
