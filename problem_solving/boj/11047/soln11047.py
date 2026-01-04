"""
# 백준
# No. 11047
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, K = map(int, input().split())
    C = [int(input()) for _ in range(N)]

    # Logic
    ans = 0
    for c in C[::-1]:
        ans += K // c
        K %= c

    # Output
    print(ans)


if __name__ == "__main__":
    main()
