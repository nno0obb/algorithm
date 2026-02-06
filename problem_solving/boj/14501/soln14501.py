"""
# 백준
# No. 14501
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    T, P = [None], [None]
    for _ in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)

    # Logic
    dp = [0] * (N + 2)
    for i in range(1, N + 1):
        dp[i] = max(dp[i], dp[i - 1])
        if i + T[i] <= N + 1:
            dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])
    dp[N + 1] = max(dp[N + 1], dp[N])

    # Output
    print(dp[N + 1])


if __name__ == "__main__":
    main()
