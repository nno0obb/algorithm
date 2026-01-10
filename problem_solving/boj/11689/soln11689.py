"""
# 백준
# No. 11689
# Python 3.11.9
# by "nno0obb"
"""

from math import sqrt


def main():
    # Input
    N = int(input())

    # Logic
    ans = N
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            ans -= ans // i
            while N % i == 0:
                N //= i

    if N > 1:
        ans -= ans // N

    # Output
    print(ans)


if __name__ == "__main__":
    main()
