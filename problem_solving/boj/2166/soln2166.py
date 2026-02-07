"""
# 백준
# No. 2166
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # Logic
    P.append(P[0])

    ans = 0
    for i in range(N):
        ans += P[i][0] * P[i + 1][1] - P[i][1] * P[i + 1][0]
    ans = abs(ans) / 2

    # Output
    print(ans)


if __name__ == "__main__":
    main()
