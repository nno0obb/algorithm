"""
# 백준
# No. 3943
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    T = int(input())
    MAX_N = 100_000
    dp = [-1] * (MAX_N + 1)
    for _ in range(T):
        N = int(sys.stdin.readline().strip())

        # Logic
        if dp[N] == -1:
            M = N
            dp[N] = M
            while M != 1:
                if M % 2 == 0:
                    M //= 2
                else:
                    M = 3 * M + 1
                dp[N] = max(dp[N], M)

        # Output
        print(dp[N])


if __name__ == "__main__":
    main()
