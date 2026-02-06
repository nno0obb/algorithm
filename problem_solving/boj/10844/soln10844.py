"""
# 백준
# No. 10844
# Python 3.11.9
# by "nno0obb"
"""

# Gloval Variables
MOD = 1_000_000_000


def main():
    # Input
    N = int(input())

    # Logic
    dp = [[0] * 10 for _ in range(N + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                dp[i][0] = dp[i - 1][1]
            elif j == 9:
                dp[i][9] = dp[i - 1][8]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
                dp[i][j] %= MOD

    ans = sum(dp[N]) % MOD

    # Output
    print(ans)


if __name__ == "__main__":
    main()
