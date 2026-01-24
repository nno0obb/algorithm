"""
# 백준
# No. 1516
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    # Logic
    T = [-1] * (N + 1)
    G = [[] for _ in range(N + 1)]
    for i, a in enumerate(A, start=1):
        time, *S, _ = a
        T[i] = time
        G[i] = S

    dp = [-1] * (N + 1)

    def dfs(i):
        if dp[i] != -1:
            return dp[i]

        dp[i] = T[i]
        for j in G[i]:
            dp[i] = max(dp[i], dfs(j) + T[i])

        return dp[i]

    for i in range(1, N + 1):
        if dp[i] == -1:
            dfs(i)

    # Output
    print(*dp[1:], sep="\n")


if __name__ == "__main__":
    main()
