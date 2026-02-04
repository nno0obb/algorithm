"""
# 백준
# No. 11050
# Python 3.11.9
# by "nno0obb"
"""

from math import factorial


def main():
    # Input
    N, K = map(int, input().split())

    # Logic
    ans = factorial(N) // factorial(K) // factorial(N - K)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
