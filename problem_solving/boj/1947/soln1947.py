"""
# 백준
# No. 1947
# Python 3.11.9
# by "nno0obb"
"""

# Global Variables
MOD = 1_000_000_000
MAX_N = 1_000_000


def main():
    # Input
    N = int(input())

    # Logic
    dp = [0] * (max(3, N) + 1)
    dp[1] = 0
    dp[2] = 1
    for i in range(3, N + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
        dp[i] %= MOD

    # Output
    print(dp[N])


if __name__ == "__main__":
    main()
