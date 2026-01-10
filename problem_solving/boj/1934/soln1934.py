"""
# 백준
# No. 1934
# Python 3.11.9
# by "nno0obb"
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    # Input
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())

        # Output
        print(lcm(A, B))


if __name__ == "__main__":
    main()
