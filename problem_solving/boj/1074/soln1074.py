"""
# 백준
# No. 1074
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, r, c = map(int, input().split())

    # Logic
    ans = 0
    for i in range(N, 0, -1):
        k = 2 ** (i - 1)
        match (r // k, c // k):
            case (0, 0):
                ans += 0 * (k**2)
            case (0, 1):
                ans += 1 * (k**2)
            case (1, 0):
                ans += 2 * (k**2)
            case (1, 1):
                ans += 3 * (k**2)
            case _:
                raise RuntimeError()
        r %= k
        c %= k

    # Output
    print(ans)


if __name__ == "__main__":
    main()
