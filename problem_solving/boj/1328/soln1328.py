"""
# 백준
# No. 1328
# Python 3.11.9
# by "nno0obb"
"""

# Global Variables
MOD = 1_000_000_007


def main():
    # Input
    N, L, R = map(int, input().split())

    # Logic
    dp = [[[0] * (R + 1) for _ in range(L + 1)] for _ in range(N + 1)]
    dp[1][1][1] = 1
    for i in range(2, N + 1):
        for j in range(1, L + 1):
            for k in range(1, R + 1):
                # 가장 작은 빌딩을...
                dp[i][j][k] += dp[i - 1][j][k] * (i - 2)  # 가운데
                dp[i][j][k] += dp[i - 1][j][k - 1]  # 오른쪽
                dp[i][j][k] += dp[i - 1][j - 1][k]  # 왼쪽
                dp[i][j][k] %= MOD

    # Output
    print(dp[N][L][R])


if __name__ == "__main__":
    main()
