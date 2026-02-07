"""
# 백준
# No. 11758
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    P1 = tuple(map(int, input().split()))
    P2 = tuple(map(int, input().split()))
    P3 = tuple(map(int, input().split()))

    # Logic
    v1 = (P2[0] - P1[0], P2[1] - P1[1])
    v2 = (P3[0] - P1[0], P3[1] - P1[1])
    cross_product = v1[0] * v2[1] - v1[1] * v2[0]

    # Output
    print(0 if cross_product == 0 else 1 if cross_product > 0 else -1)


if __name__ == "__main__":
    main()
