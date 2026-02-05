"""
# 백준
# No. 1256
# Python 3.11.9
# by "nno0obb"
"""

import math


def main():
    # Input
    N, M, K = map(int, input().split())

    # Logic
    ans = ""
    while N > 0 or M > 0:
        if N == 0:
            ans += "z"
            M -= 1
        elif M == 0:
            ans += "a"
            N -= 1
        else:
            offset = math.comb(N + M - 1, N - 1)
            if K > offset:
                ans += "z"
                K -= offset
                M -= 1
            else:
                ans += "a"
                N -= 1

    if K != 1:
        ans = -1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
