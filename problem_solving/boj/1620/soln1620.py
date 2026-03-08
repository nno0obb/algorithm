"""
# 백준
# No. 1620
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, M = map(int, input().split())
    P = [sys.stdin.readline().strip() for _ in range(N)]
    Q = [sys.stdin.readline().strip() for _ in range(M)]

    # Logic
    name2idx = {}
    idx2name = {}
    for i in range(N):
        name2idx[P[i]] = i
        idx2name[i] = P[i]

    # Output
    for q in Q:
        if q.isdigit():
            idx = int(q) - 1
            print(idx2name[idx])
        else:
            name = q
            print(name2idx[name] + 1)


if __name__ == "__main__":
    main()
