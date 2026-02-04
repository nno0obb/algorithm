"""
# 백준
# No. 11051
# Python 3.11.9
# by "nno0obb"
"""

# Gloval Variables
MOD = 10_007


def main():
    # Input
    N, K = map(int, input().split())

    # Logic
    K = min(K, N - K)
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(K + 1):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                dp[i][j] %= MOD

    # Output
    print(dp[N][K])


if __name__ == "__main__":
    main()
