"""
# 백준
# No. 2231
# Python 3.11.9
# by "nno0obb"
"""

from math import ceil, log10


def main():
    # Input
    N = int(input())

    # Logic
    ans = 0
    for i in range(max(1, N - ceil(log10(N)) * 9), N):
        if i + sum(map(int, str(i))) == N:
            ans = i
            break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
