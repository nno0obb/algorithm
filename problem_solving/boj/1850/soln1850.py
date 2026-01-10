"""
# 백준
# No. 1850
# Python 3.11.9
# by "nno0obb"
"""

from math import gcd


def main():
    # Input
    A, B = map(int, input().split())

    # Logic
    ans = "1" * gcd(A, B)

    # Output
    print(ans)

    # Hint
    # gcd(x, y) = gcd(y, x)
    # gcd(x, y) = gcd(x-y, y)
    # = gcd(x, y) = gcd(x-y*10^x, y)
    # ---
    # ex: gcd(11111, 111)
    # = gcd(11111 - 111*100, 111)
    # = gcd(11, 111)
    # = gcd(111, 11)
    # = gcd(111 - 11*10, 11)
    # = gcd(1, 11)
    # = gcd(11, 1)


if __name__ == "__main__":
    main()
