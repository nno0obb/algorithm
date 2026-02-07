"""
# 백준
# No. 2098
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]

    # Logic
    dp = [[None] * (1 << N) for _ in range(N)]

    def dfs(c, v):
        if v == (1 << N) - 1:
            if W[c][0] > 0:
                return W[c][0]
            else:
                return float("inf")

        if dp[c][v] is not None:
            return dp[c][v]

        dp[c][v] = float("inf")
        for i in range(N):
            if v & (1 << i) == 0 and W[c][i] > 0:
                dp[c][v] = min(dp[c][v], dfs(i, v | (1 << i)) + W[c][i])
        return dp[c][v]

    # Output
    print(dfs(0, 1 << 0))


if __name__ == "__main__":
    main()
