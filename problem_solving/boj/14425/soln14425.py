"""
# 백준
# No. 14425
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, M = map(int, input().split())
    S = set()
    for _ in range(N):
        S.add(sys.stdin.readline().strip())
    T = []
    for _ in range(M):
        T.append(sys.stdin.readline().strip())

    # Logic
    ans = len(list(filter(lambda x: x in S, T)))

    # Output
    print(ans)


if __name__ == "__main__":
    main()
