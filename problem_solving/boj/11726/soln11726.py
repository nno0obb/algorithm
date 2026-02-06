"""
# 백준
# No. 11726
# Python 3.11.9
# by "nno0obb"
"""

# Gloval Variables
MOD = 10_007


def main():
    # Input
    N = int(input())

    # Logic
    dp = [0] * (max(3, N) + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= MOD

    # Output
    print(dp[N])


if __name__ == "__main__":
    main()
