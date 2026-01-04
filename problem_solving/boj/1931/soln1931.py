"""
# 백준
# No. 1931
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # Logic
    M.sort(key=lambda x: (x[1], x[0]))
    ce, ans = 0, 0
    for ms, me in M:
        if ms >= ce:
            ans += 1
            ce = me

    # Output
    print(ans)


if __name__ == "__main__":
    main()
