"""
# 백준
# No. 13251
# Python 3.11.9
# by "nno0obb"
"""

from math import comb


def main():
    # Input
    M = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    # Logic
    N = sum(A)
    ans = 0
    for a in A:
        ans += comb(a, K)
    ans /= comb(N, K)

    # Output
    print(f"{ans:.20f}")


if __name__ == "__main__":
    main()
